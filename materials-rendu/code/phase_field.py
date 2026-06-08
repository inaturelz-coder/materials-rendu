"""
phase_field.py
==============
《打通材料基础任督二脉》Ch12 配套模块(督脉收官)

主题:相场与计算动力学 —— 把"动"计算化(Ch7 CALPHAD 的对仗)

核心思想:CALPHAD(Ch7,静)算出平衡相图——"该去哪"。
  相场(本章,动)算出组织如何随时间演化——"怎么去、长什么样"。
  相场的革命:用连续的"相场变量"描述组织,界面是弥散的(几个网格宽),
  不用费力追踪尖锐界面 —— 数值上极其优雅。
  自由能泛函 = CALPHAD 的 G(体积项)+ 梯度项(界面能)。

  这是 Ch7(静,平衡)的动态对仗:CALPHAD 给自由能,相场给演化。

演示:
  1. 双势阱自由能(相分离的驱动)
  2. Cahn-Hilliard 方程一维数值解(调幅分解,连接 Ch5 spinodal)
  3. Allen-Cahn 方程(界面移动,非守恒场)
  4. 界面宽度与梯度能系数的关系
  5. 相场与 CALPHAD 的连接(自由能泛函)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np


# ============================================================
# 第 1 部分:双势阱自由能
# ============================================================

def double_well(c, W=1.0):
    """
    双势阱自由能 f(c) = W·c²(1-c)²
    两个极小在 c=0 和 c=1(两个平衡相)
    中间势垒 = 相分离的驱动来源
    """
    return W * c**2 * (1 - c)**2


def double_well_derivative(c, W=1.0):
    """df/dc = W·2c(1-c)(1-2c)"""
    return W * 2 * c * (1 - c) * (1 - 2*c)


# ============================================================
# 第 2 部分:Cahn-Hilliard 方程(守恒场,调幅分解)
# ============================================================

def cahn_hilliard_1d(nx=128, steps=8000, dx=1.0, dt=0.01,
                     M=1.0, W=2.0, kappa=1.0, seed=42):
    """
    Cahn-Hilliard 方程(守恒场,如成分):
    ∂c/∂t = M ∇²μ,  μ = df/dc - κ∇²c
    模拟调幅分解(spinodal decomposition,连接 Ch5):
    均匀混合的合金自发分离成两相(无需形核)
    返回 初始和最终的浓度场
    """
    rng = np.random.default_rng(seed)
    # 初始:均匀 c=0.5 + 小噪声(过饱和均匀固溶体)
    c = 0.5 + 0.02 * (rng.random(nx) - 0.5)
    c_initial = c.copy()

    def laplacian(f):
        return (np.roll(f, 1) + np.roll(f, -1) - 2*f) / dx**2

    for _ in range(steps):
        mu = double_well_derivative(c, W) - kappa * laplacian(c)
        c = c + dt * M * laplacian(mu)

    return {'c_initial': c_initial, 'c_final': c, 'nx': nx,
            'steps': steps}


def spinodal_analysis(c_final):
    """分析调幅分解的结果:相分离程度"""
    n_phase_A = np.sum(c_final < 0.3)   # 贫相
    n_phase_B = np.sum(c_final > 0.7)   # 富相
    n_interface = np.sum((c_final >= 0.3) & (c_final <= 0.7))
    return {'phase_A_fraction': n_phase_A / len(c_final),
            'phase_B_fraction': n_phase_B / len(c_final),
            'interface_fraction': n_interface / len(c_final),
            'c_min': c_final.min(), 'c_max': c_final.max()}


# ============================================================
# 第 3 部分:Allen-Cahn 方程(非守恒场,界面移动)
# ============================================================

def allen_cahn_1d(nx=128, steps=4000, dx=1.0, dt=0.01,
                  L=1.0, W=2.0, kappa=1.0):
    """
    Allen-Cahn 方程(非守恒场,如有序参量/相分数):
    ∂φ/∂t = -L(df/dφ - κ∇²φ)
    模拟界面移动(如晶界迁移、有序-无序转变)
    初始:左半 φ=1, 右半 φ=0,看界面如何平衡成弥散界面
    """
    # 初始:阶跃界面
    phi = np.zeros(nx)
    phi[:nx//2] = 1.0

    def laplacian(f):
        return (np.roll(f, 1) + np.roll(f, -1) - 2*f) / dx**2

    phi_initial = phi.copy()
    for _ in range(steps):
        dfdphi = double_well_derivative(phi, W)
        phi = phi - dt * L * (dfdphi - kappa * laplacian(phi))
        phi = np.clip(phi, 0, 1)

    return {'phi_initial': phi_initial, 'phi_final': phi, 'nx': nx}


def interface_width(phi, dx=1.0):
    """
    测量弥散界面宽度:从 φ=0.1 到 φ=0.9 的距离
    相场的界面是'弥散'的(几个网格),不是尖锐的
    """
    # 找过渡区
    above = np.where(phi > 0.9)[0]
    below = np.where(phi < 0.1)[0]
    if len(above) > 0 and len(below) > 0:
        width = abs(below[0] - above[-1]) * dx
        return width
    return None


# ============================================================
# 第 4 部分:界面能与梯度系数
# ============================================================

def interface_properties(W=2.0, kappa=1.0):
    """
    相场理论:界面宽度和界面能由 W(势垒)和 κ(梯度能)决定
    界面宽度 δ ∝ √(κ/W)
    界面能 γ ∝ √(κ·W)
    """
    delta = np.sqrt(kappa / W)        # 界面宽度(相对)
    gamma = np.sqrt(kappa * W)        # 界面能(相对)
    return {'W': W, 'kappa': kappa,
            'interface_width': delta, 'interface_energy': gamma}


def interface_scan():
    """扫描 κ,看界面宽度和能量的变化"""
    results = []
    for kappa in [0.5, 1.0, 2.0, 4.0]:
        p = interface_properties(W=2.0, kappa=kappa)
        results.append(p)
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("相场与计算动力学 · 把'动'计算化(Ch7 CALPHAD 的对仗)")
    print("=" * 64)

    print("\n【静与动的对仗】")
    print("  Ch7 CALPHAD(静):算平衡相图 ——'该去哪'(自由能最低)")
    print("  Ch12 相场(动):算组织演化 ——'怎么去、长什么样'(随时间)")
    print("  相场的革命:界面是'弥散'的,不用追踪尖锐界面")
    print("  自由能泛函 = CALPHAD的G(体积项)+ 梯度项(界面能)")

    # --- 双势阱 ---
    print("\n【1. 双势阱自由能:相分离的驱动】")
    print("  f(c) = W·c²(1-c)²,两个极小在 c=0 和 c=1(两相)")
    print(f"  {'成分c':>8} {'自由能f':>10}")
    for c in [0.0, 0.25, 0.5, 0.75, 1.0]:
        f = double_well(c, W=2.0)
        print(f"  {c:8.2f} {f:10.4f}")
    print("  → c=0和c=1是两个平衡相,中间c=0.5是势垒(不稳定)")

    # --- Cahn-Hilliard ---
    print("\n【2. Cahn-Hilliard 方程:调幅分解(连接 Ch5 spinodal)】")
    print("  ∂c/∂t = M∇²μ, μ = df/dc - κ∇²c")
    print("  模拟:均匀过饱和固溶体(c=0.5)自发分离成两相")
    print("  (调幅分解 = spinodal,无需形核,Ch5讲过)")
    ch = cahn_hilliard_1d()
    sa = spinodal_analysis(ch['c_final'])
    print(f"\n  初始: 均匀 c≈0.5(+小噪声)")
    print(f"  演化 {ch['steps']} 步后:")
    print(f"    最低浓度 c_min = {sa['c_min']:.3f}(贫相,趋向0)")
    print(f"    最高浓度 c_max = {sa['c_max']:.3f}(富相,趋向1)")
    print(f"    贫相区域 {sa['phase_A_fraction']*100:.0f}%, "
          f"富相区域 {sa['phase_B_fraction']*100:.0f}%, "
          f"界面 {sa['interface_fraction']*100:.0f}%")
    print("  → 从均匀自发分离成两相 —— 这就是调幅分解!")
    print("    无需形核(Ch9),直接自发长出迷宫状两相组织")

    # --- Allen-Cahn ---
    print("\n【3. Allen-Cahn 方程:界面移动(非守恒场)】")
    print("  ∂φ/∂t = -L(df/dφ - κ∇²φ)")
    print("  模拟:尖锐阶跃界面 → 弥散平衡界面")
    ac = allen_cahn_1d()
    w = interface_width(ac['phi_final'])
    print(f"  初始:阶跃界面(左φ=1,右φ=0)")
    print(f"  演化后:弥散界面,宽度 ≈ {w:.0f} 个网格")
    print("  → 相场界面是'弥散'的(几个网格宽),不是数学上的尖锐面")
    print("    这正是相场数值优雅的核心:不用显式追踪界面位置!")

    # --- 界面性质 ---
    print("\n【4. 界面宽度与能量:由 W 和 κ 决定】")
    print("  界面宽度 δ ∝ √(κ/W), 界面能 γ ∝ √(κ·W)")
    print(f"  {'κ(梯度能)':>10} {'界面宽度':>10} {'界面能':>10}")
    for p in interface_scan():
        print(f"  {p['kappa']:10.1f} {p['interface_width']:10.3f} {p['interface_energy']:10.3f}")
    print("  → κ越大界面越宽越'软';界面能γ可由DFT算(连接Ch3/Ch9)")

    print("\n【5. 相场与 CALPHAD 的连接】")
    print("  相场自由能泛函: F = ∫[f_chem(c) + (κ/2)|∇c|²] dV")
    print("    f_chem(c): 化学自由能 ← 来自 CALPHAD(Ch7)!")
    print("    (κ/2)|∇c|²: 梯度项 ← 界面能")
    print("  → CALPHAD给'热力学驱动力',相场给'演化路径'")
    print("    这就是现代ICME:静(CALPHAD)+动(相场)的完整闭环")

    print("\n" + "=" * 64)
    print("相场:把自由能最小化(静)变成时间演化(动)")
    print("CALPHAD算'该去哪',相场算'怎么去、长什么样'")
    print("督脉收官:'动'被完整计算化")
    print("=" * 64)
