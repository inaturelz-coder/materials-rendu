"""
calphad.py
==========
《打通材料基础任督二脉》Ch7 配套模块

主题:CALPHAD 与计算热力学 —— 相图的现代语言

核心思想:CALPHAD(CALculation of PHAse Diagrams)的核心是:
  给每个相一个 Gibbs 自由能函数 G(x,T),其参数通过拟合
  实验数据(相图、热化学)和第一性原理数据来确定。
  有了 G(x,T),用公切线/能量最小化,就能计算任意成分、
  任意温度、甚至多元体系的相图。

  这是任脉"静"的收官:从 G=H-TS(Ch5)到相图(Ch6),
  CALPHAD 是它们的工程化、计算化、可外推到多元的现代形式。

演示:
  1. Redlich-Kister 多项式:描述过剩 Gibbs 自由能
  2. 子格模型:有序相/化合物的自由能
  3. 参数优化:从实验相平衡点拟合相互作用参数
  4. 公切线计算相平衡(复用 Ch5/Ch6)
  5. 多元外推:Muggianu 几何模型(二元 → 三元)
  6. 现代趋势:不确定度量化(贝叶斯 CALPHAD)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

R = 8.314  # J/mol·K


# ============================================================
# 第 1 部分:Redlich-Kister 多项式(CALPHAD 的核心数学)
# ============================================================

def redlich_kister(x, L_params, T=1000):
    """
    Redlich-Kister 多项式描述过剩 Gibbs 自由能:
    G_xs = x(1-x) * Σ L_v * (1-2x)^v
    L_params: [L0, L1, L2, ...] 各阶相互作用参数 (J/mol)
        L0 = 规则溶液项(对称)
        L1 = 一阶非对称项
        L2 = 二阶...
    每个 L 可以是温度的函数 L = a + b*T,这里简化为常数
    """
    x = np.asarray(x)
    G_xs = np.zeros_like(x, dtype=float)
    for v, Lv in enumerate(L_params):
        G_xs += Lv * (1 - 2*x)**v
    return x * (1 - x) * G_xs


def total_gibbs(x, L_params, T=1000, G_A=0, G_B=0):
    """
    溶液相总 Gibbs 自由能:
    G = (1-x)G_A + x G_B               # 端元参考
        + RT[x ln x + (1-x)ln(1-x)]    # 理想混合熵
        + G_xs                          # 过剩(Redlich-Kister)
    """
    x = np.clip(np.asarray(x, dtype=float), 1e-10, 1 - 1e-10)
    G_ref = (1 - x) * G_A + x * G_B
    G_ideal = R * T * (x * np.log(x) + (1 - x) * np.log(1 - x))
    G_xs = redlich_kister(x, L_params, T)
    return G_ref + G_ideal + G_xs


# ============================================================
# 第 2 部分:子格模型(化合物/有序相)
# ============================================================

def sublattice_two(y_A1, y_B2, G_AA, G_AB, G_BA, G_BB, T=1000):
    """
    两亚点阵模型 (A,B)_1 (A,B)_1 的简化
    y_A1: 第一亚点阵上 A 的占据分数
    y_B2: 第二亚点阵上 B 的占据分数
    G_IJ: 端元化合物 (I)(J) 的自由能
    返回总自由能(含组态熵)
    """
    y_B1 = 1 - y_A1
    y_A2 = 1 - y_B2
    # 端元加权
    G_end = (y_A1*y_A2*G_AA + y_A1*y_B2*G_AB +
             y_B1*y_A2*G_BA + y_B1*y_B2*G_BB)
    # 组态熵(每个亚点阵独立)
    def s(y):
        y = np.clip(y, 1e-10, 1-1e-10)
        return y*np.log(y) + (1-y)*np.log(1-y)
    S_conf = R * T * (s(y_A1) + s(y_B2))
    return G_end + S_conf


# ============================================================
# 第 3 部分:参数优化(从实验数据拟合 L)
# ============================================================

def fit_interaction_parameter(exp_points):
    """
    从实验相平衡点拟合规则溶液相互作用参数 Ω(=L0)
    exp_points: [(T, x_eq), ...] 实验测得的某温度下的平衡成分
    简化:用混溶间隙临界温度 T_c = Ω/2R 反推 Ω
    实际 CALPHAD 用最小二乘同时拟合多种数据
    """
    # 如果有临界点数据(混溶间隙顶点 T_c, x=0.5)
    T_values = [p[0] for p in exp_points]
    T_c_est = max(T_values) / 0.95  # 实验最高分离温度近似临界温度
    Omega_fit = 2 * R * T_c_est
    return {'Omega_fit': Omega_fit, 'T_c_used': T_c_est}


def least_squares_demo():
    """
    演示 CALPHAD 参数优化的本质:最小化(计算值-实验值)²
    假设我们有一些实验"活度"数据,拟合 L0, L1
    """
    # 合成"实验数据"(用已知参数 + 噪声)
    rng = np.random.default_rng(42)
    x_data = np.linspace(0.1, 0.9, 9)
    L0_true, L1_true = 12000, 3000
    G_xs_true = redlich_kister(x_data, [L0_true, L1_true])
    G_xs_noisy = G_xs_true + rng.normal(0, 200, len(x_data))

    # 最小二乘拟合 L0, L1(线性问题)
    # G_xs/(x(1-x)) = L0 + L1(1-2x)  → 线性回归
    y = G_xs_noisy / (x_data * (1 - x_data))
    A = np.column_stack([np.ones_like(x_data), (1 - 2*x_data)])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return {'L0_true': L0_true, 'L1_true': L1_true,
            'L0_fit': coef[0], 'L1_fit': coef[1]}


# ============================================================
# 第 4 部分:公切线计算相平衡
# ============================================================

def common_tangent_two_phase(L_params, T, n=4000, G_A=0, G_B=0):
    """
    用公切线找两相平衡(适用于有混溶间隙的情形)
    对非对称体系,公切线不一定水平,要找真正的公切线
    简化:找 G 的凸包(convex hull)下边界的切点
    """
    x = np.linspace(1e-4, 1-1e-4, n)
    G = total_gibbs(x, L_params, T, G_A, G_B)
    # 找下凸包:任意两点连线在曲线下方的部分被"切掉"
    # 简化的公切线:找 G''<0 区域(失稳区)的边界
    d2G = np.gradient(np.gradient(G, x), x)
    unstable = np.where(d2G < 0)[0]
    if len(unstable) < 2:
        return None  # 无相分离
    # spinodal 边界
    spin_left, spin_right = x[unstable[0]], x[unstable[-1]]
    return {'spinodal': (spin_left, spin_right),
            'has_miscibility_gap': True}


# ============================================================
# 第 5 部分:多元外推(Muggianu 几何模型)
# ============================================================

def muggianu_extrapolation(x1, x2, x3, L12, L13, L23):
    """
    Muggianu 模型:从三个二元的过剩能外推三元过剩能
    这是 CALPHAD 计算多元相图的关键(没有三元能直接拟合时)
    x1+x2+x3 = 1
    L_ij: 二元 i-j 的规则溶液参数(简化为常数 L0)
    """
    # Muggianu: 每个二元贡献用对称投影
    G_xs_12 = x1 * x2 * L12
    G_xs_13 = x1 * x3 * L13
    G_xs_23 = x2 * x3 * L23
    return G_xs_12 + G_xs_13 + G_xs_23


def ternary_demo():
    """三元体系的过剩能(从三个二元外推)"""
    L12, L13, L23 = 12000, -8000, 5000  # 三个二元参数
    points = [
        ('等比 1:1:1', 1/3, 1/3, 1/3),
        ('富组元1', 0.6, 0.2, 0.2),
        ('1-2边二元', 0.5, 0.5, 0.0),
    ]
    results = []
    for name, x1, x2, x3 in points:
        G_xs = muggianu_extrapolation(x1, x2, x3, L12, L13, L23)
        results.append({'comp': name, 'x': (x1, x2, x3), 'G_xs': G_xs})
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("CALPHAD · 相图的现代语言(给每个相一个 G(x,T))")
    print("=" * 64)

    print("\n【CALPHAD 是什么】")
    print("  CALPHAD = CALculation of PHAse Diagrams")
    print("  核心三步:")
    print("    1. 给每个相一个 Gibbs 自由能模型 G(x,T)")
    print("    2. 用实验数据 + 第一性原理数据拟合模型参数")
    print("    3. 用能量最小化/公切线计算相图(可外推到多元!)")

    # --- Redlich-Kister ---
    print("\n【1. Redlich-Kister 多项式:描述过剩自由能】")
    print("  G_xs = x(1-x)·Σ L_v·(1-2x)^v")
    print("  L0=对称项(规则溶液), L1=非对称, L2=更高阶...")
    x_test = 0.3
    for desc, L in [('仅 L0(规则溶液)', [10000]),
                    ('L0+L1(非对称)', [10000, 3000]),
                    ('L0+L1+L2', [10000, 3000, -2000])]:
        G_xs = redlich_kister(x_test, L)
        print(f"    x=0.3, {desc:20}: G_xs = {G_xs:8.1f} J/mol")
    print("  → 加更多 L 项,能拟合任意复杂的实验自由能曲线")

    # --- 参数优化 ---
    print("\n【2-3. 参数优化:CALPHAD 的核心工作】")
    r = least_squares_demo()
    print("  从(带噪声的)实验数据,最小二乘拟合 Redlich-Kister 参数:")
    print(f"    真实值: L0={r['L0_true']}, L1={r['L1_true']}")
    print(f"    拟合值: L0={r['L0_fit']:.0f}, L1={r['L1_fit']:.0f}")
    print(f"    误差:   L0 {abs(r['L0_fit']-r['L0_true'])/r['L0_true']*100:.1f}%, "
          f"L1 {abs(r['L1_fit']-r['L1_true'])/r['L1_true']*100:.1f}%")
    print("  → CALPHAD 工作者的日常:拟合参数,让计算相图匹配实验")
    print("    真实 CALPHAD 同时拟合相图+焓+活度+DFT,几十个参数")

    # --- 公切线/混溶间隙 ---
    print("\n【4. 公切线计算相平衡】")
    L_params = [16000]  # 规则溶液,倾向分离
    for T in [1200, 800, 500]:
        result = common_tangent_two_phase(L_params, T)
        if result and result['has_miscibility_gap']:
            sl, sr = result['spinodal']
            print(f"    T={T}K: 有混溶间隙, spinodal x={sl:.3f}~{sr:.3f}")
        else:
            print(f"    T={T}K: 单一相(无分离)")
    print("  → 给定 G(x,T),自动算出哪里分相、分成什么成分")

    # --- 多元外推 ---
    print("\n【5. 多元外推:Muggianu 几何模型(二元→三元)】")
    print("  CALPHAD 最强大处:用二元参数外推多元,无需重新测多元相图")
    print(f"  {'成分':16} {'(x1,x2,x3)':>20} {'G_xs(J/mol)':>14}")
    for r in ternary_demo():
        x = r['x']
        print(f"  {r['comp']:16} ({x[0]:.2f},{x[1]:.2f},{x[2]:.2f})    {r['G_xs']:12.1f}")
    print("  → 这就是为什么 CALPHAD 能算 5-6 元真实合金相图!")
    print("    二元数据库 + 几何外推 = 多元相图(无需测多元)")

    print("\n【6. 现代趋势:不确定度 + 机器学习】")
    print("  · 贝叶斯 CALPHAD:不只给相图,还给'相图的误差棒'")
    print("  · 第一性原理 + CALPHAD:DFT 算端元/形成能,减少实验依赖")
    print("  · 机器学习势 + 高通量:加速生成训练数据")
    print("  · 主流软件:Thermo-Calc / Pandat / FactSage / OpenCALPHAD")
    print("  · 数据格式:TDB 文件(热力学数据库),SGTE 纯元素数据")

    print("\n" + "=" * 64)
    print("CALPHAD:把 G=H-TS(Ch5)工程化,算出任意多元相图(Ch6)")
    print("任脉'静'的收官:从原子到相图,材料的平衡态全打通")
    print("=" * 64)
