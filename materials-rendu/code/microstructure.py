"""
microstructure.py
=================
《打通材料基础任督二脉》Ch4 配套模块

主题:微观组织 —— 从缺陷到组织

核心思想:缺陷(Ch3)和相在空间里如何排布,就构成"微观组织"。
  组织是连接"原子结构"和"宏观性能"的桥——四面体里的"组织"顶点。
  组织可以定量:晶粒尺寸、第二相体积分数、相比例……
  这些定量参数直接进入性能公式。

演示:
  1. ASTM 晶粒度等级 ↔ 实际晶粒尺寸
  2. 杠杆定律:两相组织的相比例
  3. 体视学:从二维截面推三维组织(Delesse 原理)
  4. 组织参数 → 性能(综合 Hall-Petch + 第二相)
  5. "怎么看见它":金相定量 + 截线法测晶粒度

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np


# ============================================================
# 第 1 部分:ASTM 晶粒度等级
# ============================================================

def astm_grain_size(G):
    """
    ASTM 晶粒度等级 G 与晶粒数/晶粒尺寸的关系
    N = 2^(G-1)  个晶粒每平方英寸(100倍下)
    返回 平均晶粒直径 (µm)
    """
    # 每 in² (100x) 的晶粒数
    N_per_in2 = 2**(G - 1)
    # 换算到实际面积:100x 下 1 in² 对应实际 (1/100 in)² = (254µm)²
    real_area_um2 = (25400 / 100)**2  # µm²
    grains_per_um2 = N_per_in2 / real_area_um2
    # 平均晶粒面积 → 等效直径
    area_per_grain = 1 / grains_per_um2
    diameter = np.sqrt(area_per_grain) * 2 / np.sqrt(np.pi)  # 等效圆直径
    return diameter


def grain_size_table():
    """ASTM 等级 vs 晶粒尺寸"""
    results = []
    for G in [1, 3, 5, 7, 8, 10, 12]:
        d = astm_grain_size(G)
        results.append({'ASTM_G': G, 'diameter_um': d})
    return results


# ============================================================
# 第 2 部分:杠杆定律(两相组织的相比例)
# ============================================================

def lever_rule(c_overall, c_alpha, c_beta):
    """
    杠杆定律:两相区里 α 相和 β 相的质量分数
    c_overall: 合金总成分
    c_alpha:   α 相成分
    c_beta:    β 相成分
    返回 (f_alpha, f_beta)
    """
    f_alpha = (c_beta - c_overall) / (c_beta - c_alpha)
    f_beta = (c_overall - c_alpha) / (c_beta - c_alpha)
    return f_alpha, f_beta


def eutectic_example():
    """共晶组织例子:Pb-Sn 合金 (典型焊料)"""
    # 共晶点 61.9% Sn, 共晶温度 183°C
    # 取 40% Sn 的合金,刚好低于共晶温度
    # α(富Pb): ~19% Sn, β(富Sn): ~97.5% Sn
    c_alpha = 19.0
    c_beta = 97.5
    results = []
    for c in [30, 40, 50, 61.9, 80]:
        fa, fb = lever_rule(c, c_alpha, c_beta)
        results.append({'overall_Sn': c, 'f_alpha': fa, 'f_beta': fb})
    return results


# ============================================================
# 第 3 部分:体视学(2D 截面 → 3D 组织)
# ============================================================

def delesse_principle(area_fraction):
    """
    Delesse 原理(1847):
    二维截面上某相的面积分数 = 三维体积分数
    A_A = V_V
    这是定量金相的理论基石
    """
    return area_fraction  # 面积分数直接等于体积分数


def intercept_method(n_intercepts, line_length_um, magnification):
    """
    截线法测晶粒尺寸:
    画一条已知长度的线,数它穿过多少晶界
    平均截距 = 真实线长 / 截点数
    """
    real_length = line_length_um / magnification * 1000  # 实际长度(µm),假设line_length以mm在照片上
    # 简化:line_length_um 已经是照片上的长度,除以放大倍数
    real_length = line_length_um / magnification
    mean_intercept = real_length / n_intercepts
    # ASTM: 平均晶粒尺寸 ≈ 1.5 × 平均截距
    grain_size = 1.5 * mean_intercept
    return {'mean_intercept_um': mean_intercept, 'grain_size_um': grain_size}


# ============================================================
# 第 4 部分:组织参数 → 性能
# ============================================================

def strength_from_microstructure(grain_um, second_phase_vol_frac,
                                  sigma_0=50, k_y=0.7, k_p=200):
    """
    综合组织-性能模型:
    σ_y = σ_0 + k_y/√d + k_p·f   (Hall-Petch + 第二相强化)
    grain_um: 晶粒尺寸
    second_phase_vol_frac: 第二相体积分数 (0-1)
    """
    d_mm = grain_um * 1e-3
    sigma_hp = k_y / np.sqrt(d_mm)
    sigma_pp = k_p * second_phase_vol_frac
    total = sigma_0 + sigma_hp + sigma_pp
    return {'sigma_0': sigma_0, 'hall_petch': sigma_hp,
            'second_phase': sigma_pp, 'total_MPa': total}


def microstructure_design():
    """对比不同组织设计的强度"""
    designs = [
        ('粗晶+无第二相', 100, 0.0),
        ('细晶+无第二相', 10, 0.0),
        ('粗晶+10%第二相', 100, 0.10),
        ('细晶+10%第二相', 10, 0.10),
        ('超细晶+15%第二相', 2, 0.15),
    ]
    results = []
    for name, d, f in designs:
        s = strength_from_microstructure(d, f)
        results.append({'design': name, 'grain_um': d,
                        'second_phase': f, 'total_MPa': s['total_MPa']})
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("微观组织 · 从缺陷到组织(四面体的'组织'顶点)")
    print("=" * 64)

    print("\n【1. 微观组织是什么】")
    print("  组织 = 缺陷(Ch3)+ 相 在空间里的排布")
    print("  尺度:介于'原子'(0.1nm)和'宏观构件'(mm-m)之间")
    print("  典型组织单元:晶粒 / 晶界网络 / 第二相 / 共晶层片 / 马氏体板条")
    print("  → 组织是连接'结构'和'性能'的桥梁(四面体的核心顶点)")

    # --- ASTM 晶粒度 ---
    print("\n【2. ASTM 晶粒度等级 ↔ 晶粒尺寸】")
    print("  N = 2^(G-1) 个晶粒/in²(100倍),G 越大晶粒越细")
    print(f"  {'ASTM G 级':>10} {'平均晶粒直径(µm)':>18}")
    for r in grain_size_table():
        print(f"  {r['ASTM_G']:8} {r['diameter_um']:16.1f}")
    print("  → 工业钢材常控制在 G=7-9(细晶,兼顾强韧)")

    # --- 杠杆定律 ---
    print("\n【3. 杠杆定律:两相组织的相比例(Pb-Sn 焊料)】")
    print("  α(富Pb,19%Sn) + β(富Sn,97.5%Sn),共晶点 61.9%Sn")
    print(f"  {'总Sn含量%':>10} {'α相分数':>10} {'β相分数':>10}")
    for r in eutectic_example():
        print(f"  {r['overall_Sn']:8.1f} {r['f_alpha']:10.3f} {r['f_beta']:10.3f}")
    print("  → 改变成分,就改变两相比例,从而改变组织和性能")
    print("    这是相图(Ch6)和组织的直接联系")

    # --- 体视学 ---
    print("\n【4. 体视学:从2D截面推3D组织】")
    print("  Delesse 原理(1847):截面上的面积分数 = 三维体积分数")
    for af in [0.05, 0.15, 0.30]:
        vf = delesse_principle(af)
        print(f"    照片上测得面积分数 {af:.2f} → 三维体积分数 {vf:.2f}")
    print("  → 这是定量金相的理论基石:")
    print("    我们只能切开看2D截面,却能推断3D组织!")
    print("\n  截线法测晶粒度(照片长度150µm,放大500x,穿过22条晶界):")
    ic = intercept_method(22, 150 * 500, 500)  # 照片150mm? 简化
    ic = intercept_method(22, 150, 1)  # 直接用实际150µm线长
    print(f"    平均截距 = {ic['mean_intercept_um']:.2f} µm")
    print(f"    晶粒尺寸 ≈ {ic['grain_size_um']:.2f} µm")

    # --- 组织→性能 ---
    print("\n【5. 组织参数 → 性能:定量设计】")
    print("  σ_y = σ_0 + k_y/√d + k_p·f (Hall-Petch + 第二相强化)")
    print(f"  {'组织设计':20} {'晶粒µm':>8} {'第二相':>8} {'强度MPa':>10}")
    for r in microstructure_design():
        print(f"  {r['design']:18} {r['grain_um']:8} {r['second_phase']:8.2f} "
              f"{r['total_MPa']:10.0f}")
    base = microstructure_design()[0]['total_MPa']
    best = microstructure_design()[-1]['total_MPa']
    print(f"  → 从'粗晶无第二相'到'超细晶+第二相',强度提升 {(best/base-1)*100:.0f}%")
    print("    同样的成分,不同的组织(工艺造就),性能天差地别!")

    print("\n" + "=" * 64)
    print("成分 + 工艺 → 组织 → 性能:材料四面体的核心就是'组织'")
    print("=" * 64)
