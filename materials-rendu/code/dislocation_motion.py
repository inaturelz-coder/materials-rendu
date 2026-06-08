"""
dislocation_motion.py
======================
《打通材料基础任督二脉》Ch10 配套模块

主题:缺陷的运动 —— 位错与塑性(Ch3 的动态对仗)

核心思想:Ch3 讲了位错"长什么样"(几何、柏氏矢量、密度)。
  这一章讲位错"怎么动"——位错滑移让金属能塑性变形。
  没有位错运动,金属会像玻璃一样脆。
  位错越动越多越缠,于是越来越硬(加工硬化)。

  这是 Ch3(静,缺陷几何)的动态对仗:静看几何,动看运动。

演示:
  1. Schmid 定律:分切应力 = 外应力 × Schmid 因子
  2. 软取向 vs 硬取向(单晶塑性的方向性)
  3. 理论强度 vs 实际强度(位错让金属"软"1000倍)
  4. 加工硬化:Taylor 关系(位错密度→强度,连接 Ch3)
  5. 应力-应变曲线(弹性 + 屈服 + 加工硬化)
  6. 位错攀移(高温,扩散辅助,连接 Ch8)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

R = 8.314


# ============================================================
# 第 1 部分:Schmid 定律
# ============================================================

def schmid_factor(phi_deg, lambda_deg):
    """
    Schmid 因子 m = cos(φ)·cos(λ)
    φ: 滑移面法线与拉伸轴的夹角
    λ: 滑移方向与拉伸轴的夹角
    分切应力 τ = σ·m
    """
    phi = np.radians(phi_deg)
    lam = np.radians(lambda_deg)
    return np.cos(phi) * np.cos(lam)


def resolved_shear_stress(sigma_MPa, phi_deg, lambda_deg):
    """分切应力 τ = σ·cos(φ)·cos(λ)"""
    m = schmid_factor(phi_deg, lambda_deg)
    return sigma_MPa * m


def orientation_demo():
    """不同取向的 Schmid 因子(软取向 vs 硬取向)"""
    orientations = [
        ('软取向(45°/45°)', 45, 45),
        ('中等(30°/60°)', 30, 60),
        ('硬取向(近90°)', 80, 10),
        ('硬取向(轴平行滑移面)', 90, 45),
    ]
    results = []
    for name, phi, lam in orientations:
        m = schmid_factor(phi, lam)
        results.append({'name': name, 'phi': phi, 'lambda': lam, 'm': m})
    return results


def critical_resolved_shear(sigma_yield_MPa, m):
    """从屈服强度和 Schmid 因子求临界分切应力 CRSS"""
    return sigma_yield_MPa * m


# ============================================================
# 第 2 部分:理论强度 vs 实际强度
# ============================================================

def theoretical_vs_real_strength(G_GPa=45):
    """
    理论剪切强度(完美晶体整层滑移)≈ G/(2π) ~ G/10
    实际屈服强度比理论低 100-1000 倍 —— 因为位错!
    G: 剪切模量 (GPa)
    """
    tau_theoretical = G_GPa / (2 * np.pi) * 1000  # MPa
    # 实际金属屈服强度典型值
    tau_real_annealed = 50    # MPa (退火纯金属)
    ratio = tau_theoretical / tau_real_annealed
    return {'tau_theoretical_MPa': tau_theoretical,
            'tau_real_MPa': tau_real_annealed,
            'ratio': ratio}


# ============================================================
# 第 3 部分:加工硬化(Taylor 关系,连接 Ch3)
# ============================================================

def taylor_hardening(rho_disloc, alpha=0.5, G=45e9, b=0.25e-9):
    """
    Taylor 关系:Δτ = α·G·b·√ρ(同 Ch3)
    加工硬化的本质:位错运动 → 增殖 → 密度增大 → 互相缠结阻挡
    """
    delta_tau = alpha * G * b * np.sqrt(rho_disloc)
    return delta_tau / 1e6  # MPa


def work_hardening_curve():
    """变形过程中位错密度增加 → 强度上升"""
    states = [
        ('屈服初期', 1e11, 0.002),
        ('小塑性变形', 1e12, 0.02),
        ('中等变形', 1e13, 0.10),
        ('大变形', 1e14, 0.30),
        ('重度冷加工', 1e15, 0.60),
    ]
    results = []
    for name, rho, strain in states:
        tau = taylor_hardening(rho)
        results.append({'state': name, 'rho': rho,
                        'strain': strain, 'delta_tau': tau})
    return results


# ============================================================
# 第 4 部分:应力-应变曲线
# ============================================================

def stress_strain_curve(E_GPa=200, sigma_y=250, K=600, n=0.2):
    """
    工程应力-应变曲线(简化)
    弹性段:σ = E·ε
    塑性段:σ = K·ε^n(加工硬化,Hollomon 方程)
    E: 弹性模量 GPa, sigma_y: 屈服强度 MPa
    K: 强度系数, n: 加工硬化指数
    """
    E = E_GPa * 1000  # MPa
    eps_yield = sigma_y / E
    results = []
    for eps in [0.0005, 0.001, eps_yield, 0.005, 0.02, 0.05, 0.10, 0.20]:
        if eps <= eps_yield:
            sigma = E * eps  # 弹性
            regime = '弹性'
        else:
            sigma = K * eps**n  # 塑性(加工硬化)
            regime = '塑性'
        results.append({'strain': eps, 'stress': sigma, 'regime': regime})
    return results, eps_yield


# ============================================================
# 第 5 部分:位错攀移(高温,连接 Ch8 扩散)
# ============================================================

def dislocation_climb_vs_glide(T_C):
    """
    位错运动两种方式:
    - 滑移(glide):低温,不需扩散,沿滑移面
    - 攀移(climb):高温,需要空位扩散(连接 Ch8),可越过障碍
    攀移速率 ∝ 扩散系数 ∝ exp(-Q/RT)
    """
    Q = 200000  # J/mol, 自扩散激活能
    T = T_C + 273.15
    climb_rate = np.exp(-Q / (R * T))  # 相对攀移速率
    return {'T_C': T_C, 'climb_rate_rel': climb_rate}


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("缺陷的运动 · 位错与塑性(Ch3 的动态对仗)")
    print("=" * 64)

    print("\n【静与动的对仗】")
    print("  Ch3(静):位错'长什么样'—— 几何、柏氏矢量、密度")
    print("  Ch10(动):位错'怎么动'—— 滑移让金属能塑性变形")
    print("  没有位错运动,金属会像玻璃一样脆!")

    # --- 理论 vs 实际强度 ---
    print("\n【1. 理论强度 vs 实际强度:位错让金属'软'】")
    r = theoretical_vs_real_strength()
    print(f"  理论剪切强度(完美晶体整层滑移)≈ G/2π = {r['tau_theoretical_MPa']:.0f} MPa")
    print(f"  实际屈服强度(退火纯金属)≈ {r['tau_real_MPa']:.0f} MPa")
    print(f"  → 实际比理论低 {r['ratio']:.0f} 倍!")
    print("    原因:位错让滑移'逐个原子'进行(地毯褶皱),不用整层同时动")

    # --- Schmid 定律 ---
    print("\n【2. Schmid 定律:分切应力 τ = σ·cos(φ)·cos(λ)】")
    print("  位错滑移由'分切应力'驱动,不是全部外应力")
    print(f"  {'取向':24} {'φ':>5} {'λ':>5} {'Schmid因子':>10}")
    for r in orientation_demo():
        print(f"  {r['name']:22} {r['phi']:5} {r['lambda']:5} {r['m']:10.3f}")
    print("  → Schmid 因子最大 0.5(45°/45°软取向),最易变形")
    print("    轴平行/垂直滑移面时因子=0,位错根本不动(硬取向)")

    # --- 加工硬化 ---
    print("\n【3. 加工硬化:位错越动越多越缠(连接 Ch3)】")
    print("  Δτ = α·G·b·√ρ(同 Ch3 的 Taylor 关系)")
    print(f"  {'变形状态':14} {'位错密度(/m²)':>16} {'应变':>8} {'强化(MPa)':>12}")
    for r in work_hardening_curve():
        print(f"  {r['state']:12} {r['rho']:14.0e} {r['strain']:8.2f} {r['delta_tau']:10.0f}")
    print("  → 位错运动 → 增殖 → 密度暴增 → 互相缠结 → 越来越难动")
    print("    这就是'越锤越硬'(加工硬化)的物理:动出来的硬")

    # --- 应力应变曲线 ---
    print("\n【4. 应力-应变曲线:弹性→屈服→加工硬化】")
    curve, eps_y = stress_strain_curve()
    print(f"  屈服应变 = {eps_y:.4f}")
    print(f"  {'应变':>8} {'应力(MPa)':>12} {'区域':>8}")
    for r in curve:
        print(f"  {r['strain']:8.4f} {r['stress']:10.1f}  {r['regime']:>6}")
    print("  → 弹性段(可恢复)→ 屈服(位错开始动)→ 塑性加工硬化(越拉越强)")

    # --- 位错攀移 ---
    print("\n【5. 位错攀移:高温靠扩散越障(连接 Ch8)】")
    print("  滑移(低温,不需扩散) vs 攀移(高温,需空位扩散)")
    print(f"  {'温度°C':>8} {'攀移速率(相对)':>16}")
    base = None
    for T_C in [300, 600, 900, 1200]:
        r = dislocation_climb_vs_glide(T_C)
        if base is None: base = r['climb_rate_rel']
        print(f"  {r['T_C']:8} {r['climb_rate_rel']:14.3e}")
    print("  → 高温下位错能'攀移'越过障碍(靠空位扩散)")
    print("    这是高温蠕变的机制 —— 位错运动 + 扩散(动 + 动)")

    print("\n" + "=" * 64)
    print("位错运动 = 塑性的本质。Ch3 看几何(静),本章看运动(动)")
    print("位错让金属软(易变形),又越动越硬(加工硬化)")
    print("=" * 64)
