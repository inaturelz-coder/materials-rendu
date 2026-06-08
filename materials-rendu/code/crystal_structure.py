"""
crystal_structure.py
=====================
《打通材料基础任督二脉》Ch2 配套模块

主题:原子键合与晶体结构 —— 原子怎么周期性堆叠

核心思想:原子像硬球一样尽量密堆,堆法决定了
  配位数、堆垛因子、密度,进而影响一切性质。

演示:
  1. 三大金属结构(FCC/BCC/HCP)的堆垛因子(APF)
  2. 从晶体结构 + 原子量算理论密度,与实测对比
  3. 配位数与最近邻距离
  4. 布拉格定律:XRD 怎么测出晶面间距("怎么看见它")
  5. 立方晶系晶面间距与衍射峰位置

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

# 物理常数
N_A = 6.02214076e23   # 阿伏伽德罗常数 (/mol)


# ============================================================
# 第 1 部分:堆垛因子(Atomic Packing Factor, APF)
# ============================================================

def packing_factor(structure):
    """
    计算原子堆垛因子 APF = 原子占体积 / 晶胞体积
    用硬球模型:原子半径 r 与晶格常数 a 的关系由结构决定
    """
    if structure == 'SC':       # 简单立方:a = 2r,1 个原子/胞
        n_atoms = 1
        # a = 2r => r = a/2
        r_over_a = 0.5
    elif structure == 'BCC':    # 体心立方:体对角线 4r = √3 a,2 个原子/胞
        n_atoms = 2
        r_over_a = np.sqrt(3) / 4
    elif structure == 'FCC':    # 面心立方:面对角线 4r = √2 a,4 个原子/胞
        n_atoms = 4
        r_over_a = np.sqrt(2) / 4
    else:
        raise ValueError(structure)
    # APF = n * (4/3 π r³) / a³ = n * 4/3 π (r/a)³
    apf = n_atoms * (4/3) * np.pi * r_over_a**3
    return {'structure': structure, 'n_atoms': n_atoms,
            'r_over_a': r_over_a, 'APF': apf}


def hcp_apf():
    """
    HCP(六方密堆)的 APF
    理想 c/a = sqrt(8/3) ≈ 1.633
    APF 与 FCC 相同 = 0.74(都是最密堆积)
    """
    # 理想 HCP:6 个原子/胞,c/a = sqrt(8/3)
    c_over_a = np.sqrt(8/3)
    apf = np.pi / (3 * np.sqrt(2))  # = 0.7405
    return {'structure': 'HCP', 'c_over_a': c_over_a, 'APF': apf}


# ============================================================
# 第 2 部分:从结构算理论密度
# ============================================================

def theoretical_density(structure, atomic_mass, atomic_radius_nm):
    """
    理论密度 ρ = n·M / (V_cell · N_A)
    atomic_mass: g/mol
    atomic_radius_nm: nm
    返回 g/cm³
    """
    info = packing_factor(structure)
    n = info['n_atoms']
    r = atomic_radius_nm * 1e-7  # nm -> cm
    # 由 r/a 反推 a
    a = r / info['r_over_a']     # cm
    V_cell = a**3                # cm³
    rho = n * atomic_mass / (V_cell * N_A)
    return {'structure': structure, 'a_nm': a * 1e7,
            'density_g_cm3': rho}


def density_comparison():
    """几个金属:理论密度 vs 实测密度"""
    # (元素, 结构, 原子量 g/mol, 金属原子半径 nm, 实测密度 g/cm³)
    metals = [
        ('Al 铝', 'FCC', 26.98, 0.1431, 2.70),
        ('Cu 铜', 'FCC', 63.55, 0.1278, 8.96),
        ('Fe 铁(α)', 'BCC', 55.85, 0.1241, 7.87),
        ('W 钨', 'BCC', 183.84, 0.1371, 19.25),
        ('Ni 镍', 'FCC', 58.69, 0.1246, 8.90),
        ('Cr 铬', 'BCC', 52.00, 0.1249, 7.19),
    ]
    results = []
    for name, struct, M, r, rho_exp in metals:
        td = theoretical_density(struct, M, r)
        err = abs(td['density_g_cm3'] - rho_exp) / rho_exp * 100
        results.append({
            'name': name, 'structure': struct,
            'a_nm': td['a_nm'],
            'rho_calc': td['density_g_cm3'],
            'rho_exp': rho_exp, 'error_pct': err
        })
    return results


# ============================================================
# 第 3 部分:配位数
# ============================================================

COORDINATION = {
    'SC':  {'CN': 6,  'APF': 0.52, '密排面': '无'},
    'BCC': {'CN': 8,  'APF': 0.68, '密排面': '{110}'},
    'FCC': {'CN': 12, 'APF': 0.74, '密排面': '{111}'},
    'HCP': {'CN': 12, 'APF': 0.74, '密排面': '(0001)基面'},
}


# ============================================================
# 第 4 部分:布拉格定律("怎么看见它"——XRD)
# ============================================================

def d_spacing_cubic(a_nm, h, k, l):
    """立方晶系晶面间距 d = a / sqrt(h²+k²+l²)"""
    return a_nm / np.sqrt(h**2 + k**2 + l**2)


def bragg_angle(d_nm, wavelength_nm=0.15406, n=1):
    """
    布拉格定律 nλ = 2d·sinθ => θ = arcsin(nλ/2d)
    默认波长 = Cu Kα = 0.15406 nm
    返回 2θ(度)
    """
    sin_theta = n * wavelength_nm / (2 * d_nm)
    if sin_theta > 1:
        return None  # 该晶面不衍射
    theta = np.arcsin(sin_theta)
    return np.degrees(2 * theta)


def allowed_reflections(structure):
    """
    选择定则:哪些 (hkl) 会出现衍射峰
    FCC: h,k,l 全奇或全偶
    BCC: h+k+l 为偶数
    """
    planes = []
    for h in range(0, 4):
        for k in range(0, 4):
            for l in range(0, 4):
                if h == 0 and k == 0 and l == 0:
                    continue
                s = h*h + k*k + l*l
                if structure == 'FCC':
                    allowed = (h % 2 == k % 2 == l % 2)
                elif structure == 'BCC':
                    allowed = ((h + k + l) % 2 == 0)
                else:
                    allowed = True
                if allowed:
                    planes.append((h, k, l, s))
    # 去重 + 按 s 排序
    seen = set(); out = []
    for h, k, l, s in sorted(planes, key=lambda x: x[3]):
        if s not in seen:
            seen.add(s)
            out.append((h, k, l, s))
    return out[:6]


def xrd_pattern(structure, a_nm):
    """模拟 XRD 衍射峰位置(Cu Kα)"""
    peaks = []
    for h, k, l, s in allowed_reflections(structure):
        d = d_spacing_cubic(a_nm, h, k, l)
        two_theta = bragg_angle(d)
        if two_theta is not None:
            peaks.append({'hkl': f'({h}{k}{l})', 'd_nm': d, 'two_theta': two_theta})
    return peaks


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("原子键合与晶体结构 · 原子怎么周期性堆叠")
    print("=" * 64)

    # --- 堆垛因子 ---
    print("\n【1. 堆垛因子 APF:原子占了多少空间】")
    print(f"  {'结构':6} {'原子/胞':>7} {'配位数':>6} {'APF':>7} {'密排面':>10}")
    print("  " + "-" * 44)
    for s in ['SC', 'BCC', 'FCC']:
        pf = packing_factor(s)
        cn = COORDINATION[s]
        print(f"  {s:6} {pf['n_atoms']:7} {cn['CN']:6} {pf['APF']:7.4f} {cn['密排面']:>10}")
    h = hcp_apf()
    print(f"  {'HCP':6} {6:7} {12:6} {h['APF']:7.4f} {'(0001)':>10}")
    print(f"  → FCC 和 HCP 都是 0.74 —— 这是硬球能达到的最密堆积")
    print(f"    (开普勒 1611 年猜想,2014 年才被严格证明!)")

    # --- 理论密度 ---
    print("\n【2. 从晶体结构算密度:理论 vs 实测】")
    print(f"  {'金属':12} {'结构':5} {'a(nm)':>7} {'理论ρ':>8} {'实测ρ':>8} {'误差':>6}")
    print("  " + "-" * 56)
    for r in density_comparison():
        print(f"  {r['name']:12} {r['structure']:5} {r['a_nm']:7.4f} "
              f"{r['rho_calc']:7.2f}  {r['rho_exp']:7.2f}  {r['error_pct']:5.1f}%")
    print(f"  → 仅凭'结构+原子量+半径',就能算出金属密度,误差几个%")
    print(f"    W(钨)密度 19.25 = 把原子塞得又重又密,所以做穿甲弹/灯丝")

    # --- 布拉格定律 / XRD ---
    print("\n【3. 怎么看见它:XRD 布拉格定律】")
    print("  X 射线打到晶体,只在特定角度反射(布拉格定律 nλ=2d·sinθ)")
    print("  Cu Kα 波长 = 0.15406 nm\n")
    print("  铝(FCC, a=0.4049 nm)的 XRD 衍射峰:")
    print(f"    {'晶面':8} {'d(nm)':>8} {'2θ(度)':>8}")
    for pk in xrd_pattern('FCC', 0.4049):
        print(f"    {pk['hkl']:8} {pk['d_nm']:8.4f} {pk['two_theta']:8.2f}")
    print(f"  → 测出衍射峰角度,反推 d,反推晶格常数 a")
    print(f"    这就是 XRD '看见'晶体结构的原理")

    print("\n【4. 选择定则:为什么有些峰'消失'了】")
    print("  FCC 允许的前 6 个衍射: ", end="")
    print(', '.join(f"({h}{k}{l})" for h, k, l, s in allowed_reflections('FCC')))
    print("  BCC 允许的前 6 个衍射: ", end="")
    print(', '.join(f"({h}{k}{l})" for h, k, l, s in allowed_reflections('BCC')))
    print("  → FCC 看不到(100)(110),BCC 看不到(100)(111)")
    print("    峰'消失'是因为晶胞内原子的散射波相消干涉")
    print("    XRD 通过'哪些峰在/不在',就能区分 FCC 还是 BCC!")

    print("\n" + "=" * 64)
    print("堆垛方式 → 配位数/密度/密排面 → 塑性/强度:结构决定性能")
    print("=" * 64)
