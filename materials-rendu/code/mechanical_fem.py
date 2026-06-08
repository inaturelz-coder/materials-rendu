"""
mechanical_fem.py
=================
《打通材料基础任督二脉》Ch13 配套模块(任督交汇)

主题:力学性能与强化 + 有限元(FEM)

核心思想:前面所有"结构"和"过程"最终都为了"性能"。
  力学性能(强度、韧性)是结构与缺陷的总和:
  四大强化机制(固溶/加工硬化/细晶/析出)汇聚于此(Ch3/Ch4/Ch10/Ch11)。
  然后用有限元(FEM)把"材料属性"接到"宏观构件"——
  这是多尺度计算的'宏观'一环(原子DFT→微观相场→宏观FEM)。

演示:
  1. 应力-应变曲线 + 关键力学量(E, σy, UTS, 韧性, 延伸率)
  2. 四大强化机制定量叠加(汇聚前面章节)
  3. 强度-延展性权衡(材料设计的根本矛盾)
  4. 一维有限元(刚度矩阵组装求解,FEM 内核)
  5. 应力集中(孔边 Kt,为什么裂纹从孔/缺口开始)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np


# ============================================================
# 第 1 部分:应力-应变曲线与力学量
# ============================================================

def stress_strain_analysis(E_GPa=200, sigma_y=350, UTS=550,
                           eps_fracture=0.25, n=0.15):
    """
    从应力-应变曲线提取关键力学量
    E: 弹性模量(刚度), sigma_y: 屈服强度
    UTS: 抗拉强度, eps_fracture: 断裂应变(延展性)
    韧性 = 曲线下面积(断裂吸收的能量)
    """
    E = E_GPa * 1000  # MPa
    eps_y = sigma_y / E
    # 简化:弹性段 + 塑性段(幂律硬化到 UTS)
    # 韧性 ≈ 弹性能 + 塑性功(梯形近似)
    elastic_energy = 0.5 * sigma_y * eps_y
    plastic_energy = 0.5 * (sigma_y + UTS) * (eps_fracture - eps_y)
    toughness = elastic_energy + plastic_energy  # MJ/m³
    return {'E_GPa': E_GPa, 'sigma_y': sigma_y, 'UTS': UTS,
            'eps_y': eps_y, 'eps_fracture': eps_fracture,
            'elongation_pct': eps_fracture * 100,
            'toughness_MJ_m3': toughness}


def material_comparison():
    """几种材料的力学性能对比"""
    materials = [
        ('退火低碳钢', 200, 250, 400, 0.35),
        ('调质合金钢', 210, 800, 1000, 0.12),
        ('淬火马氏体钢', 210, 1500, 1800, 0.03),
        ('铝合金7075', 72, 500, 570, 0.11),
        ('陶瓷(Al2O3)', 380, 0, 350, 0.001),  # 脆性,无屈服
    ]
    results = []
    for name, E, sy, uts, ef in materials:
        if sy > 0:
            a = stress_strain_analysis(E, sy, uts, ef)
        else:  # 脆性材料
            a = {'E_GPa': E, 'sigma_y': 0, 'UTS': uts,
                 'elongation_pct': ef*100,
                 'toughness_MJ_m3': 0.5*uts*ef}
        a['name'] = name
        results.append(a)
    return results


# ============================================================
# 第 2 部分:四大强化机制叠加(汇聚前面章节)
# ============================================================

def strengthening_mechanisms(grain_um=10, solute_pct=2.0,
                             rho_disloc=1e13, precip_vol=0.05):
    """
    四大强化机制叠加(汇聚 Ch3/Ch4/Ch10/Ch11):
    σ_y = σ_0 + Δσ_grain + Δσ_solid + Δσ_disloc + Δσ_precip
    - 细晶强化(Hall-Petch, Ch4)
    - 固溶强化(Ch3 置换原子)
    - 加工硬化(位错, Ch10)
    - 析出强化(第二相, Ch11)
    """
    sigma_0 = 50  # 晶格摩擦应力 MPa
    # 细晶(Hall-Petch)
    k_y = 0.7
    d_mm = grain_um * 1e-3
    dsigma_grain = k_y / np.sqrt(d_mm)
    # 固溶(正比于浓度^(2/3),简化为线性)
    dsigma_solid = 30 * solute_pct
    # 加工硬化(Taylor, Ch10)
    alpha, G, b = 0.5, 45e9, 0.25e-9
    dsigma_disloc = alpha * G * b * np.sqrt(rho_disloc) / 1e6
    # 析出(Orowan, 简化)
    dsigma_precip = 500 * precip_vol
    total = sigma_0 + dsigma_grain + dsigma_solid + dsigma_disloc + dsigma_precip
    return {'sigma_0': sigma_0, 'grain': dsigma_grain,
            'solid_solution': dsigma_solid, 'dislocation': dsigma_disloc,
            'precipitation': dsigma_precip, 'total_MPa': total}


# ============================================================
# 第 3 部分:强度-延展性权衡
# ============================================================

def strength_ductility_tradeoff():
    """强度-延展性的'香蕉曲线':强了就脆,韧了就软"""
    data = [
        ('退火态', 250, 35),
        ('冷加工', 500, 15),
        ('淬火回火', 900, 8),
        ('淬火马氏体', 1500, 3),
    ]
    return [{'state': s, 'strength_MPa': st, 'ductility_pct': d} for s, st, d in data]


# ============================================================
# 第 4 部分:一维有限元(FEM 内核)
# ============================================================

def fem_1d_bar(n_elements=5, L=1.0, E_GPa=200, A=1e-4, force_N=10000):
    """
    一维拉伸杆的有限元:左端固定,右端受力
    刚度矩阵组装 + 求解节点位移 + 单元应力
    这是 FEM 的核心:离散 → 组装 → 求解
    L: 总长(m), A: 截面积(m²), force: 右端力(N)
    """
    E = E_GPa * 1e9  # Pa
    n_nodes = n_elements + 1
    le = L / n_elements  # 单元长度
    k_local = E * A / le  # 单元刚度

    # 组装全局刚度矩阵
    K = np.zeros((n_nodes, n_nodes))
    for e in range(n_elements):
        K[e, e]     += k_local
        K[e, e+1]   -= k_local
        K[e+1, e]   -= k_local
        K[e+1, e+1] += k_local

    # 载荷向量(右端受力)
    F = np.zeros(n_nodes)
    F[-1] = force_N

    # 边界条件:左端固定(节点0位移=0)
    # 划去第0行第0列
    K_red = K[1:, 1:]
    F_red = F[1:]
    u_red = np.linalg.solve(K_red, F_red)
    u = np.concatenate([[0], u_red])  # 节点位移

    # 单元应力 σ = E·ε = E·(u[e+1]-u[e])/le
    stress = np.array([E * (u[e+1] - u[e]) / le for e in range(n_elements)]) / 1e6  # MPa

    # 解析解对比:σ = F/A(均匀杆)
    stress_analytical = force_N / A / 1e6  # MPa
    return {'u_nodes': u, 'stress_elements': stress,
            'stress_analytical': stress_analytical,
            'tip_displacement': u[-1]}


# ============================================================
# 第 5 部分:应力集中
# ============================================================

def stress_concentration_hole(sigma_nominal=100):
    """
    无限大板中圆孔的应力集中:Kt = 3(经典结果)
    孔边应力 = Kt × 名义应力
    这解释了为什么裂纹/失效从孔、缺口、划痕开始
    """
    Kt = 3.0  # 圆孔
    sigma_max = Kt * sigma_nominal
    return {'Kt': Kt, 'sigma_nominal': sigma_nominal, 'sigma_max': sigma_max}


def stress_concentration_demo():
    """不同几何的应力集中系数"""
    geometries = [
        ('圆孔', 3.0),
        ('椭圆孔(a/b=3)', 7.0),
        ('尖锐裂纹尖端', 100.0),  # 理论上趋于无穷
        ('圆角过渡(良好设计)', 1.5),
    ]
    return geometries


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("力学性能与强化 + 有限元(任督交汇:性能)")
    print("=" * 64)

    print("\n【任督交汇:结构与过程汇聚成性能】")
    print("  前面所有章节(原子→晶体→缺陷→组织→相变→热处理)")
    print("  最终都为了一件事:力学性能(强度/韧性/刚度)")
    print("  四大强化机制在此汇聚,再用 FEM 接到宏观构件")

    # --- 力学性能 ---
    print("\n【1. 应力-应变曲线:关键力学量】")
    print(f"  {'材料':14} {'E(GPa)':>7} {'σy(MPa)':>8} {'UTS':>6} {'延伸%':>6} {'韧性':>7}")
    for m in material_comparison():
        print(f"  {m['name']:12} {m['E_GPa']:7} {m['sigma_y']:8} {m['UTS']:6} "
              f"{m['elongation_pct']:5.0f} {m['toughness_MJ_m3']:7.1f}")
    print("  → 强度↑往往延展性↓(陶瓷强但脆,退火钢软但韧)")
    print("    韧性 = 曲线下面积 = 断裂吸收的能量(既要强又要韧)")

    # --- 强化机制 ---
    print("\n【2. 四大强化机制叠加(汇聚 Ch3/Ch4/Ch10/Ch11)】")
    s = strengthening_mechanisms()
    print(f"  σ_0(晶格摩擦):        {s['sigma_0']:6.0f} MPa")
    print(f"  + 细晶强化(Ch4):      {s['grain']:6.0f} MPa  ← Hall-Petch")
    print(f"  + 固溶强化(Ch3):      {s['solid_solution']:6.0f} MPa  ← 置换原子")
    print(f"  + 加工硬化(Ch10):     {s['dislocation']:6.0f} MPa  ← 位错")
    print(f"  + 析出强化(Ch11):     {s['precipitation']:6.0f} MPa  ← 第二相")
    print(f"  = 总屈服强度:         {s['total_MPa']:6.0f} MPa")
    print("  → 四种机制可叠加:这就是'合金设计'的定量工具箱")

    # --- 强韧权衡 ---
    print("\n【3. 强度-延展性权衡(材料设计的根本矛盾)】")
    print(f"  {'状态':14} {'强度(MPa)':>10} {'延展性(%)':>10}")
    for r in strength_ductility_tradeoff():
        print(f"  {r['state']:12} {r['strength_MPa']:10} {r['ductility_pct']:10}")
    print("  → '香蕉曲线':强了就脆,韧了就软")
    print("    现代材料研究的圣杯:同时突破强度和韧性(如TRIP/TWIP钢)")

    # --- 有限元 ---
    print("\n【4. 一维有限元(FEM):把材料属性接到构件】")
    print("  拉伸杆:左端固定,右端受力10kN,钢E=200GPa,A=1cm²")
    fem = fem_1d_bar()
    print(f"  FEM 内核:离散 → 刚度矩阵组装 → 求解")
    print(f"  节点位移(mm): {fem['u_nodes']*1000}")
    print(f"  单元应力(MPa): {fem['stress_elements']}")
    print(f"  解析解应力 F/A = {fem['stress_analytical']:.0f} MPa")
    print(f"  端部位移 = {fem['tip_displacement']*1000:.4f} mm")
    print("  → FEM 数值解与解析解吻合(均匀杆应力 = F/A)")
    print("    复杂构件没有解析解,FEM 是唯一通用方法")

    # --- 应力集中 ---
    print("\n【5. 应力集中:为什么失效从孔/缺口开始】")
    sc = stress_concentration_hole()
    print(f"  无限大板圆孔:Kt = {sc['Kt']}")
    print(f"  名义应力 {sc['sigma_nominal']} MPa → 孔边应力 {sc['sigma_max']:.0f} MPa")
    print(f"\n  {'几何':22} {'应力集中系数Kt':>14}")
    for name, kt in stress_concentration_demo():
        print(f"  {name:20} {kt:14.1f}")
    print("  → 应力在孔/缺口/裂纹处放大 → 失效从这里开始(Ch15)")
    print("    设计要点:用圆角过渡(Kt小),避免尖角(Kt大)")

    print("\n" + "=" * 64)
    print("结构+过程 → 性能。四大强化机制汇聚,FEM接到宏观构件")
    print("多尺度计算的宏观一环:原子(DFT)→微观(相场)→宏观(FEM)")
    print("=" * 64)
