"""
thermodynamics.py
=================
《打通材料基础任督二脉》Ch5 配套模块

主题:热力学 —— 材料为什么变

核心思想:材料在恒温恒压下,总是朝着 Gibbs 自由能 G=H-TS 最低的方向变。
  H(焓)想让原子键合最强,S(熵)想让排列最乱,
  温度 T 是它们的"裁判"——这场 H 与 S 的拉锯,决定了一切相变和平衡。

  这一章是"静"(平衡热力学)的核心,也是 CALPHAD(Ch7)的地基。

演示:
  1. Gibbs 自由能 G=H-TS:温度如何改变平衡(冰水例子)
  2. 混合熵:为什么合金倾向于混合
  3. 规则溶液模型:混合自由能曲线
  4. 公切线法:从自由能曲线求两相平衡成分(CALPHAD 核心!)
  5. 温度对相平衡的影响(为相图 Ch6 铺路)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

# 物理常数
R = 8.314          # 气体常数 (J/mol·K)
K_B = 1.380649e-23 # 玻尔兹曼常数 (J/K)


# ============================================================
# 第 1 部分:Gibbs 自由能 G = H - TS
# ============================================================

def gibbs_phase_transition():
    """
    以冰⇌水为例:G = H - TS
    固相(冰):H 低(键强),S 低(有序)
    液相(水):H 高,S 高(无序)
    在熔点 T_m,两相 G 相等
    """
    # 冰水的近似热力学数据(相对值)
    # 熔化焓 ΔH_fus = 6010 J/mol, 熔化熵 ΔS_fus = 22.0 J/mol·K
    dH_fus = 6010    # J/mol
    dS_fus = 22.0    # J/mol·K
    T_m_calc = dH_fus / dS_fus  # 熔点 = ΔH/ΔS
    results = []
    for T in [250, 263, 273.15, 283, 300]:
        # ΔG(熔化) = ΔH - TΔS;<0 则自发熔化
        dG = dH_fus - T * dS_fus
        favored = '液相(水)' if dG < 0 else '固相(冰)'
        results.append({'T_K': T, 'T_C': T - 273.15,
                        'dG_melt': dG, 'stable_phase': favored})
    return {'T_m_calc': T_m_calc, 'T_m_C': T_m_calc - 273.15,
            'data': results}


# ============================================================
# 第 2 部分:混合熵
# ============================================================

def mixing_entropy(x):
    """
    理想混合熵 ΔS_mix = -R(x ln x + (1-x) ln(1-x))
    x: A 组元的摩尔分数
    返回 J/mol·K
    """
    if x <= 0 or x >= 1:
        return 0.0
    return -R * (x * np.log(x) + (1 - x) * np.log(1 - x))


def mixing_entropy_demo():
    """混合熵随成分的变化"""
    results = []
    for x in [0.01, 0.1, 0.3, 0.5, 0.7, 0.9]:
        S = mixing_entropy(x)
        results.append({'x': x, 'dS_mix': S})
    # 最大值在 x=0.5
    return results


def high_entropy_alloy_entropy(n_elements):
    """
    高熵合金的构型熵:等原子比 n 种元素
    ΔS = R ln(n)
    """
    return R * np.log(n_elements)


# ============================================================
# 第 3 部分:规则溶液模型
# ============================================================

def regular_solution_G(x, Omega, T):
    """
    规则溶液模型混合自由能:
    ΔG_mix = Ω·x(1-x) + RT[x ln x + (1-x) ln(1-x)]
    Ω: 相互作用参数 (J/mol)
        Ω>0 倾向分离(同类相吸), Ω<0 倾向混合(异类相吸)
    """
    x = np.clip(x, 1e-10, 1 - 1e-10)
    enthalpy = Omega * x * (1 - x)
    entropy_term = R * T * (x * np.log(x) + (1 - x) * np.log(1 - x))
    return enthalpy + entropy_term


def miscibility_check(Omega, T):
    """
    检查是否会出现混溶间隙(spinodal/binodal)
    临界温度 T_c = Ω/(2R)(规则溶液)
    T < T_c 时出现混溶间隙(相分离)
    """
    T_c = Omega / (2 * R) if Omega > 0 else None
    if T_c is None:
        return {'T_c': None, 'phase_separation': False,
                'note': 'Ω<0,完全互溶'}
    return {'T_c': T_c, 'phase_separation': T < T_c,
            'note': f'T_c={T_c:.0f}K, ' +
                    ('当前温度有相分离' if T < T_c else '当前温度完全互溶')}


# ============================================================
# 第 4 部分:公切线法(CALPHAD 核心)
# ============================================================

def common_tangent(Omega, T, n=4000):
    """
    公切线法:两相平衡时,两相在各自自由能曲线上的点
    有公共切线(化学势相等)。
    对称规则溶液(G 关于 x=0.5 对称):binodal 两点关于 0.5 对称,
    在 (0, 0.5) 区间找全局极小 x1,另一点 x2 = 1 - x1。
    返回 (x1, x2) 两个平衡成分
    """
    T_c = Omega / (2 * R) if Omega > 0 else None
    if T_c is None or T >= T_c:
        return None, None  # 无混溶间隙,单一相
    # 在左半区 (0, 0.5) 找 G 的极小
    x_left = np.linspace(1e-4, 0.5, n)
    G_left = regular_solution_G(x_left, Omega, T)
    i_min = np.argmin(G_left)
    x1 = x_left[i_min]
    x2 = 1 - x1  # 对称性
    return x1, x2


def spinodal_points(Omega, T):
    """
    Spinodal(拐点):d²G/dx² = 0 的点
    规则溶液解析解:d²G/dx² = -2Ω + RT/(x(1-x)) = 0
    => x(1-x) = RT/(2Ω) => x = 0.5 ± 0.5·sqrt(1 - 2RT/Ω)
    在这两点之间,材料自发相分离(无需形核)
    """
    if Omega <= 0:
        return None, None
    discriminant = 1 - 2 * R * T / Omega
    if discriminant <= 0:
        return None, None  # 无 spinodal(T >= T_c)
    delta = 0.5 * np.sqrt(discriminant)
    return 0.5 - delta, 0.5 + delta


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("热力学 · 材料为什么变(G = H - TS 的拉锯)")
    print("=" * 64)

    # --- Gibbs 自由能 ---
    print("\n【1. Gibbs 自由能 G=H-TS:温度决定哪相稳定】")
    r = gibbs_phase_transition()
    print(f"  冰⇌水:熔化焓 ΔH=6010 J/mol, 熔化熵 ΔS=22.0 J/mol·K")
    print(f"  熔点 T_m = ΔH/ΔS = {r['T_m_calc']:.2f} K = {r['T_m_C']:.2f}°C")
    print(f"  (实际冰点 0°C = 273.15K,我们用近似数据算出 {r['T_m_C']:.1f}°C)")
    print(f"\n  {'温度':>12} {'ΔG熔化(J/mol)':>14} {'稳定相':>12}")
    for d in r['data']:
        print(f"  {d['T_C']:6.1f}°C ({d['T_K']:.0f}K) {d['dG_melt']:12.0f}  {d['stable_phase']:>12}")
    print("  → 低温 ΔG>0 冰稳定,高温 ΔG<0 水稳定,熔点处两相平衡")
    print("    H 想结冰(键合),S 想化水(混乱),T 是裁判")

    # --- 混合熵 ---
    print("\n【2. 混合熵:为什么合金倾向于混合】")
    print("  ΔS_mix = -R(x ln x + (1-x)ln(1-x)),x=0.5 时最大")
    print(f"  {'成分 x':>8} {'混合熵(J/mol·K)':>16}")
    for d in mixing_entropy_demo():
        print(f"  {d['x']:8.2f} {d['dS_mix']:14.2f}")
    print("  → 混合总是增加熵(-TS 降低自由能),所以高温利于固溶")
    print("\n  高熵合金的构型熵(等原子比):")
    for n in [2, 3, 5]:
        S = high_entropy_alloy_entropy(n)
        print(f"    {n} 种元素: ΔS = R·ln({n}) = {S:.2f} J/mol·K = {S/R:.2f}R")
    print("  → 5 元等比 = 1.61R,这就是'高熵'合金名字的由来")

    # --- 规则溶液 + 公切线 ---
    print("\n【3-4. 规则溶液模型 + 公切线法(CALPHAD 核心)】")
    Omega = 16000  # J/mol, Ω>0 倾向分离
    print(f"  相互作用参数 Ω = {Omega} J/mol (>0,同类相吸,倾向分离)")
    T_c = Omega / (2 * R)
    print(f"  临界温度 T_c = Ω/2R = {T_c:.0f} K")
    print()
    for T in [1200, 900, 700, 500]:
        mc = miscibility_check(Omega, T)
        x1, x2 = common_tangent(Omega, T)
        spin1, spin2 = spinodal_points(Omega, T)
        print(f"  T={T}K ({mc['note']})")
        if x1 is not None and x2 is not None:
            print(f"    公切线平衡成分(binodal): x={x1:.3f} 和 x={x2:.3f}")
            print(f"    → 合金分离成贫A相(x={x1:.2f})和富A相(x={x2:.2f})两相")
            if spin1 is not None:
                print(f"    spinodal(自发分解区): x={spin1:.3f} ~ {spin2:.3f}")
        else:
            print(f"    单一均匀相(无分离)")
    print("\n  → 公切线法是 CALPHAD 计算相图的核心算法!")
    print("    给定每相的 G(x,T) 曲线,公切线给出平衡成分 → 画出相图(Ch6)")

    print("\n" + "=" * 64)
    print("G=H-TS:焓求键合(静),熵求混乱(动),温度定胜负 → 一切相变的根")
    print("=" * 64)
