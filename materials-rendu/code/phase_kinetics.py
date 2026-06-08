"""
phase_kinetics.py
=================
《打通材料基础任督二脉》Ch9 配套模块

主题:相变动力学 —— 形核与长大

核心思想:热力学(Ch5/Ch6)告诉我们"该不该变、变成什么"(相图),
  但"变多快、怎么变"是动力学的问题。相变要先"形核"(克服能垒
  造出一个临界核),再"长大"(扩散驱动)。形核率是"驱动力"和
  "扩散"的竞争 —— 这个竞争产生了著名的 C 形 TTT 曲线。

  这是 Ch5/Ch6(静)的动态对仗:静说"该去哪",动说"怎么去多快"。

演示:
  1. 经典形核理论:临界半径 r* 和形核功 ΔG*(过冷度的函数)
  2. 形核率的 C 曲线:驱动力 vs 扩散的竞争
  3. Avrami 方程(JMAK):相变分数的 S 形曲线
  4. TTT 曲线(等温转变图)的生成
  5. 过冷度对临界核的影响

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

K_B = 1.380649e-23  # J/K
R = 8.314


# ============================================================
# 第 1 部分:经典形核理论
# ============================================================

def nucleation_energy(r, dGv, gamma):
    """
    形核的总自由能变化:
    ΔG(r) = -(4/3)πr³·dGv + 4πr²·γ
    第一项:体积项(驱动力,降低能量)
    第二项:表面项(界面能,升高能量)
    dGv: 单位体积自由能下降 (J/m³, 正值表示驱动力)
    gamma: 界面能 (J/m²)
    """
    volume_term = -(4/3) * np.pi * r**3 * dGv
    surface_term = 4 * np.pi * r**2 * gamma
    return volume_term + surface_term


def critical_nucleus(dGv, gamma):
    """
    临界半径 r* = 2γ/dGv
    形核功 ΔG* = 16πγ³/(3·dGv²)
    """
    r_star = 2 * gamma / dGv
    dG_star = 16 * np.pi * gamma**3 / (3 * dGv**2)
    return r_star, dG_star


def undercooling_effect(gamma=0.2, dHf=2.1e9, T_m=1085+273):
    """
    过冷度对临界核的影响
    驱动力 dGv ≈ dHf·ΔT/T_m (近似,ΔT=过冷度)
    gamma: 界面能 J/m²
    dHf: 熔化潜热 J/m³ (Cu ~ 1.8e9)
    T_m: 熔点 K
    """
    results = []
    for dT in [10, 50, 100, 200, 300]:
        dGv = dHf * dT / T_m   # J/m³
        r_star, dG_star = critical_nucleus(dGv, gamma)
        results.append({'undercooling_K': dT, 'dGv': dGv,
                        'r_star_nm': r_star * 1e9,
                        'dG_star_J': dG_star,
                        'atoms_in_nucleus': (4/3)*np.pi*r_star**3 / (0.23e-9)**3})
    return results


# ============================================================
# 第 2 部分:形核率的 C 曲线
# ============================================================

def nucleation_rate(T, T_m=1085+273, gamma=0.2, dHf=2.1e9,
                    Q_diff=2.4e-19, A=1e40):
    """
    形核率 I = A·exp(-ΔG*/kT)·exp(-Q_diff/kT)
    第一项:热力学障碍(形核功,过冷度大则小 → 低温有利)
    第二项:动力学障碍(扩散,温度低则慢 → 高温有利)
    两者竞争 → C 曲线(中温最快)
    """
    dT = T_m - T
    if dT <= 0:
        return 0.0  # 高于熔点不形核
    dGv = dHf * dT / T_m
    _, dG_star = critical_nucleus(dGv, gamma)
    thermo = np.exp(-dG_star / (K_B * T))      # 形核功障碍
    kinetic = np.exp(-Q_diff / (K_B * T))      # 扩散障碍
    return A * thermo * kinetic


def c_curve_demo():
    """形核率随温度变化 —— C 曲线"""
    T_m = 1085 + 273
    results = []
    for T in [1340, 1300, 1200, 1100, 1000, 900, 800, 700]:
        I = nucleation_rate(T)
        dT = T_m - T
        results.append({'T_K': T, 'T_C': T-273, 'undercooling': dT, 'rate': I})
    return results


# ============================================================
# 第 3 部分:Avrami 方程(JMAK)
# ============================================================

def avrami(t, k, n):
    """
    Avrami(JMAK)方程:相变分数
    f = 1 - exp(-k·t^n)
    n: Avrami 指数(1-4,反映形核+长大机制)
    k: 速率常数
    """
    return 1 - np.exp(-k * t**n)


def avrami_demo():
    """相变分数的 S 形曲线"""
    k, n = 0.001, 2.5
    results = []
    for t in [1, 5, 10, 20, 40, 80, 160]:
        f = avrami(t, k, n)
        results.append({'time': t, 'fraction': f})
    return results


def avrami_fit_time(k, n, target_fraction):
    """反解:达到某转变分数需要的时间"""
    # f = 1 - exp(-k t^n) => t = (-ln(1-f)/k)^(1/n)
    return (-np.log(1 - target_fraction) / k)**(1/n)


# ============================================================
# 第 4 部分:TTT 曲线
# ============================================================

def ttt_curve():
    """
    TTT 曲线(Time-Temperature-Transformation,等温转变)
    在每个温度,转变开始(1%)和结束(99%)的时间
    由形核率 + 长大率共同决定 → C 形
    """
    T_m = 1085 + 273
    results = []
    for T in [1300, 1200, 1100, 1000, 900, 800, 700, 600]:
        I = nucleation_rate(T)
        if I < 1e-10:
            t_start = np.inf
        else:
            # 转变开始时间反比于形核率(简化)
            t_start = 1e30 / I
        results.append({'T_C': T - 273, 'rate': I,
                        't_start_rel': t_start})
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("相变动力学 · 形核与长大(Ch5/Ch6的动态对仗)")
    print("=" * 64)

    print("\n【静与动的对仗】")
    print("  Ch5/Ch6(静):热力学+相图说'该不该变、变成什么相'")
    print("  Ch9(动):动力学说'变多快、怎么变、能不能变'")
    print("  关键:相变要先'形核'(造临界核),再'长大'(扩散)")

    # --- 临界核 ---
    print("\n【1. 经典形核理论:临界核 r* 和形核功 ΔG*】")
    print("  ΔG(r) = -(4/3)πr³·dGv + 4πr²·γ(体积降 vs 表面升)")
    print("  临界半径 r*=2γ/dGv, 形核功 ΔG*=16πγ³/(3dGv²)")
    print(f"\n  过冷度对临界核的影响(Cu,γ=0.2 J/m²):")
    print(f"  {'过冷度ΔT(K)':>12} {'r*(nm)':>10} {'核内原子数':>12}")
    for r in undercooling_effect():
        print(f"  {r['undercooling_K']:10} {r['r_star_nm']:10.2f} {r['atoms_in_nucleus']:10.0f}")
    print("  → 过冷度越大,临界核越小越易形成(r* ∝ 1/ΔT)")
    print("    这就是为什么要'过冷':不过冷,临界核大到造不出来")

    # --- C 曲线 ---
    print("\n【2. 形核率的 C 曲线:驱动力 vs 扩散的竞争】")
    print("  形核率 I = A·exp(-ΔG*/kT)·exp(-Q_diff/kT)")
    print("    高温:驱动力小(ΔG*大)→ 形核慢")
    print("    低温:扩散慢(原子跳不动)→ 形核慢")
    print("    中温:两者平衡 → 形核最快!")
    print(f"\n  {'温度°C':>8} {'过冷度':>8} {'形核率(相对)':>16}")
    rates = c_curve_demo()
    max_rate = max(r['rate'] for r in rates)
    for r in rates:
        bar = '█' * int(40 * r['rate']/max_rate) if max_rate > 0 else ''
        print(f"  {r['T_C']:8} {r['undercooling']:8} {r['rate']:12.2e} {bar}")
    peak = max(rates, key=lambda r: r['rate'])
    print(f"  → 形核率峰值在 {peak['T_C']}°C(中温)—— 这就是 C 曲线的'鼻尖'!")

    # --- Avrami ---
    print("\n【3. Avrami 方程:相变分数的 S 形曲线】")
    print("  f = 1 - exp(-k·t^n),n=Avrami指数(反映机制)")
    print(f"  {'时间':>8} {'转变分数':>10} {'进度':>22}")
    for r in avrami_demo():
        bar = '█' * int(20 * r['fraction'])
        print(f"  {r['time']:8} {r['fraction']:10.3f}  {bar}")
    t10 = avrami_fit_time(0.001, 2.5, 0.10)
    t50 = avrami_fit_time(0.001, 2.5, 0.50)
    t90 = avrami_fit_time(0.001, 2.5, 0.90)
    print(f"  → 10%转变需 {t10:.0f}, 50%需 {t50:.0f}, 90%需 {t90:.0f}(时间单位)")
    print("    S形:开始慢(形核)→ 中间快(长大)→ 末尾慢(碰撞)")

    # --- TTT ---
    print("\n【4. TTT 曲线(等温转变图):C 形的来源】")
    print(f"  {'温度°C':>8} {'转变开始时间(相对)':>20}")
    for r in ttt_curve():
        t = r['t_start_rel']
        ts = f"{t:.2e}" if t != np.inf else "∞(太慢)"
        print(f"  {r['T_C']:8} {ts:>20}")
    print("  → 中温转变最快(鼻尖),高温低温都慢 → C 形曲线")
    print("    淬火要'躲过鼻尖'快速冷却 → 得到马氏体(Ch11高潮!)")

    print("\n" + "=" * 64)
    print("热力学说'该变'(Ch5),动力学说'多快变':形核(造核)+长大(扩散)")
    print("形核率的 C 曲线 → TTT 的鼻尖 → 淬火躲鼻尖得马氏体(Ch11)")
    print("=" * 64)
