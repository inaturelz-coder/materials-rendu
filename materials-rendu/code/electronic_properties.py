"""
electronic_properties.py
========================
《打通材料基础任督二脉》Ch14 配套模块(任督交汇,首尾呼应 Ch1)

主题:电·磁·热性能 + DFT/MD/MLIP

核心思想:全书的最后一组呼应 —— 回到 Ch1 的电子排布!
  Ch1 定性讲了电子排布决定材料性质;
  Ch14 用能带理论 + DFT,把电学/磁学/热学性能定量算出来。
  - 电学:能带带隙决定导体/半导体/绝缘体
  - 磁学:3d 未成对电子(Ch1 的 Fe 3d⁶!)产生磁矩
  - 热学:声子 + 电子输运
  计算方法:DFT(电子结构)、MD(热输运)、MLIP(大尺度第一性原理)

  这是 Ch1(静,电子排布)的对仗,闭合全书最后一组静动对仗。

演示:
  1. 能带与导电性(带隙决定材料类型)
  2. 本征/掺杂半导体载流子浓度
  3. 铁磁性与居里温度(呼应 Ch1 的 3d 电子)
  4. 热容(杜隆-珀蒂 + 德拜)
  5. 热导(Wiedemann-Franz:电子 vs 声子)
  6. DFT/MD/MLIP 的角色

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

K_B = 8.617333e-5   # eV/K
K_B_SI = 1.380649e-23  # J/K
R = 8.314


# ============================================================
# 第 1 部分:能带与导电性
# ============================================================

def material_by_bandgap(Eg_eV):
    """根据带隙分类材料"""
    if Eg_eV <= 0.01:
        return '导体(金属)'
    elif Eg_eV < 3.0:
        return '半导体'
    else:
        return '绝缘体'


def bandgap_demo():
    """常见材料的带隙(真实值)"""
    materials = [
        ('铜 Cu', 0.0),
        ('硅 Si', 1.12),
        ('锗 Ge', 0.67),
        ('砷化镓 GaAs', 1.42),
        ('金刚石 C', 5.47),
        ('二氧化硅 SiO2', 9.0),
    ]
    return [(name, Eg, material_by_bandgap(Eg)) for name, Eg in materials]


# ============================================================
# 第 2 部分:半导体载流子浓度
# ============================================================

def intrinsic_carrier(Eg_eV, T=300):
    """
    本征载流子浓度 ni ∝ exp(-Eg/2kT)
    相对值(以 Si 为基准的指数因子)
    """
    return np.exp(-Eg_eV / (2 * K_B * T))


def carrier_demo():
    """不同带隙的本征载流子浓度(相对)+ 温度效应"""
    results = []
    for name, Eg in [('Ge(0.67)', 0.67), ('Si(1.12)', 1.12), ('GaAs(1.42)', 1.42)]:
        ni_300 = intrinsic_carrier(Eg, 300)
        ni_400 = intrinsic_carrier(Eg, 400)
        results.append({'name': name, 'Eg': Eg,
                        'ni_300K': ni_300, 'ni_400K': ni_400,
                        'ratio': ni_400/ni_300})
    return results


# ============================================================
# 第 3 部分:铁磁性与居里温度(呼应 Ch1 的 3d 电子)
# ============================================================

def magnetic_materials():
    """
    铁磁材料的居里温度 + 磁矩来源(3d 未成对电子)
    呼应 Ch1:Fe 的 3d⁶ 排布,未成对电子产生磁矩
    """
    materials = [
        ('Fe 铁', 1043, 2.2, '3d⁶4s²'),
        ('Co 钴', 1388, 1.7, '3d⁷4s²'),
        ('Ni 镍', 627, 0.6, '3d⁸4s²'),
        ('Gd 钆', 293, 7.6, '4f⁷(稀土)'),
    ]
    return [{'name': n, 'Tc_K': tc, 'moment_uB': m, 'config': c}
            for n, tc, m, c in materials]


def curie_law(T, Tc):
    """
    居里-外斯定律:磁化率 χ ∝ 1/(T - Tc)
    T > Tc:顺磁(铁磁性消失)
    T < Tc:铁磁
    """
    if T <= Tc:
        return 'ferromagnetic'
    return 1 / (T - Tc)


# ============================================================
# 第 4 部分:热容
# ============================================================

def dulong_petit():
    """杜隆-珀蒂定律:高温摩尔热容 ≈ 3R"""
    return 3 * R  # J/mol·K


def debye_heat_capacity(T, T_debye):
    """
    德拜模型热容(低温 ∝ T³,高温 → 3R)
    简化:用插值近似
    """
    x = T / T_debye
    if x > 2:
        return 3 * R  # 高温极限
    else:
        # 低温 Debye T³ 律(简化系数)
        return 3 * R * (x)**3 * 4 if x < 0.3 else 3 * R * min(x, 1)


def heat_capacity_demo():
    """几种材料的热容"""
    print_data = []
    dp = dulong_petit()
    # Debye 温度:金刚石2230K(高),铅95K(低)
    for name, T_debye in [('金刚石', 2230), ('铜', 343), ('铅', 95)]:
        Cv_300 = debye_heat_capacity(300, T_debye)
        print_data.append({'name': name, 'T_debye': T_debye,
                           'Cv_300K': Cv_300, 'dulong_petit': dp})
    return print_data


# ============================================================
# 第 5 部分:热导(Wiedemann-Franz)
# ============================================================

def wiedemann_franz(sigma_electrical, T=300):
    """
    Wiedemann-Franz 定律:金属中电子热导 κ_e = L·σ·T
    L = 洛伦兹数 = 2.44e-8 W·Ω/K²
    说明金属里导电的电子也导热
    """
    L = 2.44e-8  # W·Ω/K²
    kappa_electronic = L * sigma_electrical * T
    return kappa_electronic


def thermal_conductivity_demo():
    """金属(电子主导) vs 非金属(声子主导)的热导"""
    materials = [
        ('铜(金属)', 5.96e7, '电子主导'),
        ('铝(金属)', 3.77e7, '电子主导'),
        ('金刚石(绝缘)', 0, '声子主导(却最高!)'),
    ]
    results = []
    for name, sigma, mechanism in materials:
        if sigma > 0:
            kappa_e = wiedemann_franz(sigma)
        else:
            kappa_e = 0
        results.append({'name': name, 'sigma': sigma,
                       'kappa_electronic': kappa_e, 'mechanism': mechanism})
    return results


# ============================================================
# 第 6 部分:计算方法的角色(DFT/MD/MLIP)
# ============================================================

def computational_methods():
    """三种计算方法在电磁热性能预测中的角色"""
    return [
        ('DFT', '密度泛函理论', '算电子结构/能带/带隙/磁矩',
         '精确,但慢(~百原子)'),
        ('MD', '分子动力学', '算热输运/扩散/相变',
         '快(~百万原子),但需要势函数'),
        ('MLIP', '机器学习势', '用神经网络拟合DFT,兼顾精度与速度',
         'DFT精度 + MD速度,前沿!'),
    ]


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("电·磁·热性能 + DFT/MD/MLIP(首尾呼应 Ch1 电子排布)")
    print("=" * 64)

    print("\n【全书最后一组呼应:回到 Ch1 的电子排布!】")
    print("  Ch1(静):定性讲电子排布决定材料性质")
    print("  Ch14(动):用能带+DFT,把电/磁/热性能定量算出来")
    print("  闭合全书最后一组对仗:Ch1电子排布 ↔ Ch14电磁热")

    # --- 能带与导电 ---
    print("\n【1. 能带与导电性:带隙决定材料类型】")
    print(f"  {'材料':16} {'带隙Eg(eV)':>12} {'类型':>12}")
    for name, Eg, kind in bandgap_demo():
        print(f"  {name:14} {Eg:10.2f} {kind:>14}")
    print("  → 带隙=0导体(金属),0-3半导体,>3绝缘体")
    print("    这就是 Ch1 提的'为什么金导电、玻璃绝缘'的定量答案")

    # --- 半导体载流子 ---
    print("\n【2. 半导体载流子:ni ∝ exp(-Eg/2kT)】")
    print(f"  {'材料':14} {'ni(300K相对)':>14} {'升到400K增加':>14}")
    for r in carrier_demo():
        print(f"  {r['name']:12} {r['ni_300K']:12.2e} {r['ratio']:12.0f}倍")
    print("  → 带隙越小载流子越多;温度升高载流子指数增加")
    print("    这是半导体器件温度敏感的根源")

    # --- 磁性(呼应Ch1)---
    print("\n【3. 铁磁性与居里温度(呼应 Ch1 的 3d 电子!)】")
    print(f"  {'材料':10} {'居里温度Tc(K)':>14} {'磁矩(μB)':>10} {'电子排布':>12}")
    for m in magnetic_materials():
        print(f"  {m['name']:8} {m['Tc_K']:12} {m['moment_uB']:10.1f} {m['config']:>12}")
    print("  → Fe的3d⁶(Ch1讲过!)未成对电子 → 磁矩 → 铁磁性")
    print("    T>Tc铁磁消失变顺磁:铁加热到1043K以上就没磁性了")

    # --- 热容 ---
    print("\n【4. 热容:杜隆-珀蒂 + 德拜】")
    print(f"  杜隆-珀蒂高温极限:Cv ≈ 3R = {dulong_petit():.1f} J/mol·K")
    print(f"  {'材料':10} {'德拜温度(K)':>12} {'300K热容':>12}")
    for r in heat_capacity_demo():
        print(f"  {r['name']:8} {r['T_debye']:10} {r['Cv_300K']:10.1f}")
    print("  → 德拜温度高(金刚石2230K),室温热容还没饱和")
    print("    低温 Cv∝T³(声子冻结),高温→3R(杜隆-珀蒂)")

    # --- 热导 ---
    print("\n【5. 热导(Wiedemann-Franz:电子 vs 声子)】")
    print("  金属:κ_e = L·σ·T(导电电子也导热,L=2.44e-8)")
    print(f"  {'材料':16} {'电子热导(W/mK)':>16} {'机制':>18}")
    for r in thermal_conductivity_demo():
        print(f"  {r['name']:14} {r['kappa_electronic']:14.0f}   {r['mechanism']:>16}")
    print("  → 金属靠电子导热(导电的也导热);")
    print("    金刚石不导电却热导最高 —— 靠声子(晶格振动)!")

    # --- 计算方法 ---
    print("\n【6. 计算方法:DFT/MD/MLIP 的角色】")
    print(f"  {'方法':6} {'全称':12} {'算什么':28} {'特点':>16}")
    for abbr, full, what, feat in computational_methods():
        print(f"  {abbr:5} {full:10} {what:26} {feat:>14}")
    print("  → DFT 算电子结构(本章的能带/磁矩都能算)")
    print("    MLIP(机器学习势)= DFT精度 + MD速度,是当代前沿")

    print("\n" + "=" * 64)
    print("电/磁/热性能的根在电子结构(Ch1)。DFT定量算出,MLIP加速")
    print("首尾呼应:Ch1定性讲电子排布,Ch14定量算电磁热 —— 全书闭环")
    print("=" * 64)
