"""
phase_diagram.py
================
《打通材料基础任督二脉》Ch6 配套模块

主题:相图 —— 平衡的地图

核心思想:把 Ch5 的公切线法在每个温度都做一遍,把平衡成分点
  连成线,就得到相图。相图是材料科学的"地图"——告诉你
  任意成分、任意温度下,平衡时有哪些相、各占多少、成分是什么。

  这一章把"热力学(Ch5)"变成"可查的地图",也是 CALPHAD(Ch7)的产品。

演示:
  1. 杠杆定律:两相区的相比例(复用 Ch5 思想)
  2. 匀晶相图(Cu-Ni 全互溶):液相线 + 固相线
  3. 共晶相图(Pb-Sn):共晶点、共晶反应
  4. 从自由能曲线生成混溶间隙相图(连接 Ch5 公切线)
  5. 冷却路径追踪:一个合金凝固时的组织演化
  6. "怎么看见它":热分析(冷却曲线)测相变温度

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

R = 8.314  # J/mol·K


# ============================================================
# 第 1 部分:杠杆定律
# ============================================================

def lever_rule(c0, c_alpha, c_beta):
    """杠杆定律:两相质量分数"""
    f_alpha = (c_beta - c0) / (c_beta - c_alpha)
    f_beta = (c0 - c_alpha) / (c_beta - c_alpha)
    return f_alpha, f_beta


# ============================================================
# 第 2 部分:匀晶相图(理想全互溶,如 Cu-Ni)
# ============================================================

def isomorphous_diagram(T_A=1085, T_B=1455, n=20):
    """
    匀晶相图(简化模型):A=Cu(熔点1085°C), B=Ni(熔点1455°C)
    用理想溶液近似,给出液相线和固相线
    返回每个温度下的液相成分和固相成分
    """
    results = []
    for i in range(n + 1):
        T = T_A + (T_B - T_A) * i / n  # °C
        # 简化:线性插值的液相线/固相线模型
        # 固相线在上(更富高熔点组元),液相线在下
        frac = (T - T_A) / (T_B - T_A)
        # 用经验:固相比液相更富B(高熔点)
        x_liquid_B = frac**1.3      # 液相线 B 含量
        x_solid_B = frac**0.7       # 固相线 B 含量
        results.append({'T_C': T, 'x_liquid_B': x_liquid_B,
                        'x_solid_B': x_solid_B})
    return results


# ============================================================
# 第 3 部分:共晶相图(Pb-Sn)
# ============================================================

def eutectic_diagram():
    """
    共晶相图关键特征(Pb-Sn 焊料,真实数据)
    """
    data = {
        'T_melt_Pb': 327,       # 纯 Pb 熔点 °C
        'T_melt_Sn': 232,       # 纯 Sn 熔点 °C
        'eutectic_T': 183,      # 共晶温度 °C
        'eutectic_comp': 61.9,  # 共晶成分 % Sn
        'max_sol_Sn_in_Pb': 19.2,  # α相最大固溶度(Sn溶于Pb)
        'max_sol_Pb_in_Sn': 2.5,   # β相最大固溶度
    }
    return data


def eutectic_reaction():
    """共晶反应:液相 → α + β(恒温,三相平衡)"""
    d = eutectic_diagram()
    # 在共晶温度,共晶成分的液体同时结晶出 α 和 β
    c_eut = d['eutectic_comp']
    c_alpha = d['max_sol_Sn_in_Pb']
    c_beta = 100 - d['max_sol_Pb_in_Sn']  # β相成分(%Sn)
    f_alpha, f_beta = lever_rule(c_eut, c_alpha, c_beta)
    return {'reaction': 'L(61.9%Sn) → α(19.2%Sn) + β(97.5%Sn)',
            'T': d['eutectic_T'],
            'f_alpha': f_alpha, 'f_beta': f_beta}


# ============================================================
# 第 4 部分:从自由能生成混溶间隙(连接 Ch5)
# ============================================================

def regular_solution_G(x, Omega, T):
    x = np.clip(x, 1e-10, 1 - 1e-10)
    return Omega * x * (1 - x) + R * T * (x * np.log(x) + (1 - x) * np.log(1 - x))


def miscibility_gap(Omega=16000, n_T=8):
    """
    扫描温度,用公切线(对称体系=两个对称极小)生成混溶间隙相图
    返回 (温度, 左边界, 右边界) 的列表 —— 这就是相图的穹顶
    """
    T_c = Omega / (2 * R)
    results = []
    for i in range(n_T):
        T = T_c * (0.95 - 0.08 * i)  # 从接近 T_c 往下扫
        if T <= 0:
            break
        # 对称体系,左半区找极小
        x_left = np.linspace(1e-4, 0.5, 3000)
        G = regular_solution_G(x_left, Omega, T)
        x1 = x_left[np.argmin(G)]
        results.append({'T': T, 'x_left': x1, 'x_right': 1 - x1})
    return {'T_c': T_c, 'dome': results}


# ============================================================
# 第 5 部分:冷却路径追踪
# ============================================================

def cooling_path_eutectic(c0_Sn=40):
    """
    追踪一个亚共晶 Pb-Sn 合金(40% Sn)从液态冷却的组织演化
    """
    d = eutectic_diagram()
    steps = []
    steps.append({'stage': '高温液相', 'desc': f'{c0_Sn}%Sn 均匀液体 L'})
    steps.append({'stage': '过液相线', 'desc': '开始析出初生 α 相(富Pb)'})
    steps.append({'stage': '接近共晶温度183°C',
                  'desc': '初生 α 长大,剩余液体成分趋向共晶点 61.9%Sn'})
    # 共晶温度刚上方:初生α + 共晶液体的比例
    c_alpha = d['max_sol_Sn_in_Pb']
    c_eut = d['eutectic_comp']
    f_alpha_pri, f_liq = lever_rule(c0_Sn, c_alpha, c_eut)
    steps.append({'stage': '共晶温度刚上方',
                  'desc': f'初生α {f_alpha_pri*100:.0f}% + 共晶液体 {f_liq*100:.0f}%'})
    steps.append({'stage': '共晶反应(183°C)',
                  'desc': '剩余液体 → 共晶组织(α+β层片状)'})
    steps.append({'stage': '室温最终组织',
                  'desc': '初生α + 共晶(α+β层片)'})
    return {'c0': c0_Sn, 'f_primary_alpha': f_alpha_pri,
            'f_eutectic': f_liq, 'steps': steps}


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("相图 · 平衡的地图(把公切线在每个温度连起来)")
    print("=" * 64)

    print("\n【1. 相图是什么】")
    print("  相图 = 成分-温度平面上的'地图'")
    print("  给定(成分,温度),查出:有哪些相 / 各相成分 / 各相比例")
    print("  做法:在每个温度做 Ch5 的公切线 → 平衡成分 → 连成相界线")

    # --- 匀晶相图 ---
    print("\n【2. 匀晶相图(Cu-Ni 全互溶):液相线 + 固相线】")
    print("  Cu(1085°C) 和 Ni(1455°C) 完全互溶")
    print(f"  {'温度°C':>8} {'液相线%Ni':>12} {'固相线%Ni':>12}")
    for r in isomorphous_diagram(n=8):
        print(f"  {r['T_C']:8.0f} {r['x_liquid_B']*100:10.1f}  {r['x_solid_B']*100:10.1f}")
    print("  → 液相线和固相线之间是'两相区'(L+固),用杠杆定律算比例")

    # --- 杠杆定律 ---
    print("\n【3. 杠杆定律:两相区的相比例】")
    print("  例:某温度下,合金 35%Ni,液相线30%Ni,固相线50%Ni")
    fl, fs = lever_rule(35, 30, 50)
    print(f"    液相分数 = (50-35)/(50-30) = {fl:.2f}")
    print(f"    固相分数 = (35-30)/(50-30) = {fs:.2f}")
    print(f"  → 成分点离哪条线近,那个相就多('杠杆'的短臂端相多)")

    # --- 共晶相图 ---
    print("\n【4. 共晶相图(Pb-Sn 焊料,真实数据)】")
    d = eutectic_diagram()
    print(f"  纯Pb熔点 {d['T_melt_Pb']}°C, 纯Sn熔点 {d['T_melt_Sn']}°C")
    print(f"  共晶点: {d['eutectic_comp']}%Sn, {d['eutectic_T']}°C(最低熔点!)")
    print(f"  α相最大固溶 {d['max_sol_Sn_in_Pb']}%Sn, β相最大固溶 {d['max_sol_Pb_in_Sn']}%Pb")
    er = eutectic_reaction()
    print(f"\n  共晶反应(恒温三相平衡): {er['reaction']}")
    print(f"    共晶组织中 α:{er['f_alpha']*100:.0f}%, β:{er['f_beta']*100:.0f}%")
    print(f"  → 共晶成分熔点最低,所以做焊料(低温就能焊接)")

    # --- 混溶间隙(连接Ch5) ---
    print("\n【5. 从自由能生成混溶间隙相图(连接 Ch5 公切线)】")
    mg = miscibility_gap(Omega=16000)
    print(f"  Ω=16000 J/mol, 临界温度 T_c={mg['T_c']:.0f}K")
    print(f"  {'温度K':>8} {'左边界x':>10} {'右边界x':>10}")
    for r in mg['dome']:
        print(f"  {r['T']:8.0f} {r['x_left']:10.3f} {r['x_right']:10.3f}")
    print("  → 把这些点连起来 = 相图的'穹顶'(dome)")
    print("    温度越低,间隙越宽 —— 这就是相图从热力学'长'出来的!")

    # --- 冷却路径 ---
    print("\n【6. 冷却路径追踪:40%Sn 亚共晶合金凝固】")
    cp = cooling_path_eutectic(40)
    for i, s in enumerate(cp['steps']):
        print(f"  {i+1}. [{s['stage']}] {s['desc']}")
    print(f"  → 最终组织 = 初生α({cp['f_primary_alpha']*100:.0f}%) + 共晶({cp['f_eutectic']*100:.0f}%)")
    print("    相图不仅告诉你'平衡有什么相',还能预测'凝固组织怎么来'!")

    print("\n" + "=" * 64)
    print("相图 = 热力学的可视化地图:查相、查成分、查比例、预测组织")
    print("=" * 64)
