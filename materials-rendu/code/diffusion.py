"""
diffusion.py
============
《打通材料基础任督二脉》Ch8 配套模块

主题:扩散 —— 原子怎么搬家(督脉第一章,从"静"到"动")

核心思想:平衡态(任脉)告诉我们"该去哪",但原子怎么"走过去"?
  靠扩散——原子借助空位(Ch3)一步步跳跃。
  扩散是一切动力学过程的基础:相变、蠕变、烧结、渗碳全靠它。

  这一章是全书从"静"(平衡)转"动"(过程)的转折点。

演示:
  1. Fick 第二定律的误差函数解(钢渗碳 —— 经典 Aha)
  2. 扩散系数的 Arrhenius 温度依赖 D=D0·exp(-Q/RT)
  3. 扩散距离标度律 x ~ √(Dt)
  4. 空位机制:连接 Ch3 的空位浓度
  5. 数值解扩散方程(有限差分,为相场 Ch12 铺垫)
  6. Kirkendall 效应:不同原子扩散速率不同

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np
from scipy.special import erf, erfc

R = 8.314  # J/mol·K


# ============================================================
# 第 1 部分:Fick 第二定律 —— 渗碳的误差函数解
# ============================================================

def carburizing(x_mm, t_hours, T_C=927, C_surface=1.0, C_initial=0.2):
    """
    钢渗碳:表面碳浓度恒定的半无限固体扩散
    解析解(误差函数):
    (C(x,t) - C_s) / (C_0 - C_s) = erf(x / (2√(Dt)))
    碳在 γ-Fe(奥氏体)中:D0=2.3e-5 m²/s, Q=148 kJ/mol
    x_mm: 距表面深度(mm)
    t_hours: 时间(小时)
    """
    D0 = 2.3e-5    # m²/s
    Q = 148000     # J/mol
    T = T_C + 273.15
    D = D0 * np.exp(-Q / (R * T))   # m²/s
    x = np.asarray(x_mm) * 1e-3     # mm -> m
    t = t_hours * 3600              # h -> s
    C = C_surface - (C_surface - C_initial) * erf(x / (2 * np.sqrt(D * t)))
    return {'D': D, 'C_profile': C, 'x_mm': x_mm}


def case_depth(t_hours, T_C=927, C_target=0.4, C_surface=1.0, C_initial=0.2):
    """
    计算"渗碳层深度":碳浓度降到某目标值(如0.4%)的深度
    """
    D0 = 2.3e-5; Q = 148000
    T = T_C + 273.15
    D = D0 * np.exp(-Q / (R * T))
    t = t_hours * 3600
    # erf(z) = (C_s - C_target)/(C_s - C_0) 反解 z
    ratio = (C_surface - C_target) / (C_surface - C_initial)
    from scipy.special import erfinv
    z = erfinv(ratio)
    x = z * 2 * np.sqrt(D * t)
    return x * 1e3  # m -> mm


# ============================================================
# 第 2 部分:Arrhenius 温度依赖
# ============================================================

def diffusion_coefficient(T_C, D0, Q_kJ):
    """D = D0 · exp(-Q/RT)"""
    T = T_C + 273.15
    return D0 * np.exp(-Q_kJ * 1000 / (R * T))


def arrhenius_demo():
    """碳在 γ-Fe 中扩散系数随温度变化"""
    D0 = 2.3e-5; Q = 148  # kJ/mol
    results = []
    for T_C in [727, 827, 927, 1027, 1127]:
        D = diffusion_coefficient(T_C, D0, Q)
        results.append({'T_C': T_C, 'D': D})
    return results


def compare_diffusers():
    """不同扩散物种的对比(室温附近差异巨大)"""
    # (物种, D0 m²/s, Q kJ/mol)
    species = [
        ('C 在 γ-Fe(间隙)', 2.3e-5, 148),
        ('Fe 在 γ-Fe(自扩散)', 5.0e-5, 284),
        ('C 在 α-Fe(间隙)', 6.2e-7, 80),
        ('Cu 在 Cu(自扩散)', 7.8e-5, 211),
    ]
    results = []
    T_C = 727
    for name, D0, Q in species:
        D = diffusion_coefficient(T_C, D0, Q)
        results.append({'species': name, 'D_at_727C': D})
    return results


# ============================================================
# 第 3 部分:扩散距离标度律
# ============================================================

def diffusion_distance(D, t_seconds):
    """特征扩散距离 x ~ √(Dt)"""
    return np.sqrt(D * t_seconds)


def scaling_demo():
    """扩散距离的 √t 标度律"""
    D = diffusion_coefficient(927, 2.3e-5, 148)  # 碳在γ-Fe @927°C
    results = []
    for t_h in [1, 4, 9, 16, 25]:
        x = diffusion_distance(D, t_h * 3600)
        results.append({'t_hours': t_h, 'sqrt_t': np.sqrt(t_h),
                        'distance_mm': x * 1e3})
    return results


# ============================================================
# 第 4 部分:空位机制(连接 Ch3)
# ============================================================

def vacancy_diffusion_link(T_C, Q_f_eV=2.0, Q_m_eV=1.0):
    """
    空位机制扩散:激活能 Q = 空位形成能 Q_f + 空位迁移能 Q_m
    扩散系数 D ∝ exp(-(Q_f+Q_m)/kT)
    连接 Ch3:扩散需要空位(形成)+ 原子跳进空位(迁移)
    """
    k_B = 8.617e-5  # eV/K
    T = T_C + 273.15
    # 空位浓度 ∝ exp(-Q_f/kT) (Ch3)
    c_vacancy = np.exp(-Q_f_eV / (k_B * T))
    # 跳跃频率 ∝ exp(-Q_m/kT)
    jump_freq = np.exp(-Q_m_eV / (k_B * T))
    # 扩散系数 ∝ 两者乘积
    D_relative = c_vacancy * jump_freq
    return {'T_C': T_C, 'c_vacancy': c_vacancy,
            'jump_freq': jump_freq, 'D_relative': D_relative,
            'total_Q_eV': Q_f_eV + Q_m_eV}


# ============================================================
# 第 5 部分:数值解扩散方程(有限差分,为相场Ch12铺垫)
# ============================================================

def solve_diffusion_1d(D, L_mm=2.0, t_total_h=10, nx=100, C_surface=1.0, C_initial=0.2):
    """
    用有限差分(显式)解 Fick 第二定律 ∂C/∂t = D ∂²C/∂x²
    与解析解对比,验证数值方法(为 Ch12 相场铺垫)
    """
    L = L_mm * 1e-3
    dx = L / nx
    t_total = t_total_h * 3600
    # 稳定性:dt < dx²/(2D)
    dt = 0.4 * dx**2 / D
    nt = int(t_total / dt)
    C = np.full(nx, C_initial)
    C[0] = C_surface  # 表面固定
    for _ in range(nt):
        C_new = C.copy()
        C_new[1:-1] = C[1:-1] + D * dt / dx**2 * (C[2:] - 2*C[1:-1] + C[:-2])
        C_new[0] = C_surface
        C_new[-1] = C[-2]  # 零通量边界
        C = C_new
    x_mm = np.linspace(0, L_mm, nx)
    return {'x_mm': x_mm, 'C_numerical': C, 'n_steps': nt, 'dt': dt}


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("扩散 · 原子怎么搬家(督脉第一章:从'静'到'动')")
    print("=" * 64)

    print("\n【从静到动】")
    print("  任脉(静)告诉我们'平衡态是什么样'(相图、自由能最低)")
    print("  但材料怎么'走到'平衡态?—— 靠扩散:原子借空位一步步跳")
    print("  扩散是一切动力学的基础:相变/蠕变/烧结/渗碳全靠它")

    # --- 渗碳(误差函数解)---
    print("\n【1. Fick 第二定律:钢渗碳(误差函数解)】")
    print("  齿轮表面渗碳:927°C,表面碳1.0%,基体0.2%")
    r = carburizing([0, 0.2, 0.5, 1.0, 1.5, 2.0], t_hours=10)
    print(f"  扩散系数 D = {r['D']:.3e} m²/s")
    print(f"  {'深度(mm)':>10} {'碳浓度(%)':>12}")
    for x, C in zip(r['x_mm'], r['C_profile']):
        print(f"  {x:8.1f} {C:10.3f}")
    cd = case_depth(10)
    print(f"  → 渗碳10小时,碳降到0.4%的深度(渗碳层)= {cd:.2f} mm")
    print(f"    表面硬(高碳耐磨)+ 芯部韧(低碳)= 齿轮的理想组合")

    # --- Arrhenius ---
    print("\n【2. Arrhenius 温度依赖 D=D0·exp(-Q/RT)】")
    print("  碳在 γ-Fe 中,温度每升高,D 指数增大:")
    print(f"  {'温度°C':>8} {'D(m²/s)':>14}")
    base = None
    for r in arrhenius_demo():
        if base is None: base = r['D']
        print(f"  {r['T_C']:8} {r['D']:12.3e}")
    top = arrhenius_demo()[-1]['D']
    print(f"  → 727°C→1127°C,扩散系数增大 {top/base:.0f} 倍")
    print(f"    所以扩散控制的工艺都要'加热'—— 高温让原子跑得快")

    # --- 标度律 ---
    print("\n【3. 扩散距离标度律 x ~ √(Dt)】")
    print(f"  {'时间(h)':>8} {'√t':>8} {'扩散距离(mm)':>14}")
    for r in scaling_demo():
        print(f"  {r['t_hours']:8} {r['sqrt_t']:8.2f} {r['distance_mm']:12.4f}")
    print("  → 距离正比于 √t:要扩散2倍深,需要4倍时间!")
    print("    这个'平方根定律'支配所有扩散控制过程")

    # --- 空位机制(连接Ch3)---
    print("\n【4. 空位机制:连接 Ch3 的空位浓度】")
    print("  扩散激活能 Q = 空位形成能 Q_f + 空位迁移能 Q_m")
    print(f"  {'温度°C':>8} {'空位浓度':>12} {'跳跃频率':>12} {'D(相对)':>12}")
    for T_C in [327, 727, 1127]:
        v = vacancy_diffusion_link(T_C)
        print(f"  {T_C:8} {v['c_vacancy']:10.2e} {v['jump_freq']:10.2e} {v['D_relative']:10.2e}")
    print("  → 扩散需要两步:先有空位(Ch3),原子才能跳进去")
    print("    这就是为什么扩散激活能 = 形成能 + 迁移能")

    # --- 数值解验证 ---
    print("\n【5. 数值解扩散方程(有限差分,为相场Ch12铺垫)】")
    D = diffusion_coefficient(927, 2.3e-5, 148)
    num = solve_diffusion_1d(D, t_total_h=10)
    ana = carburizing(list(num['x_mm']), t_hours=10)
    # 对比几个点
    print(f"  显式有限差分 vs 误差函数解析解(927°C, 10h):")
    print(f"  {'深度(mm)':>10} {'数值解':>10} {'解析解':>10} {'误差':>8}")
    for i in [0, 20, 40, 60]:
        xc = num['x_mm'][i]
        cn = num['C_numerical'][i]
        ca = ana['C_profile'][i]
        err = abs(cn - ca)
        print(f"  {xc:8.2f} {cn:10.3f} {ca:10.3f} {err:8.4f}")
    print(f"  → 数值解({num['n_steps']}步)与解析解吻合")
    print("    有限差分是相场(Ch12)、扩散模拟的通用方法")

    print("\n" + "=" * 64)
    print("扩散:原子借空位搬家,x~√(Dt),D~exp(-Q/RT)")
    print("这是'动'的起点 —— 材料如何走向平衡")
    print("=" * 64)
