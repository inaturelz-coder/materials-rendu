"""
heat_treatment.py
=================
《打通材料基础任督二脉》Ch11 配套模块(全书高潮)

主题:热处理 —— 静与动的博弈(马氏体之谜)

核心思想:这是全书"一静一动"的总决战。
  相图(Ch6,静)说:钢慢冷该得珠光体(平衡相)。
  但淬火(快冷)躲过 TTT 鼻尖(Ch9),碳来不及扩散,
  奥氏体(FCC)被迫无扩散切变成马氏体(BCT,体心四方)。
  => 动力学(冷速)战胜了热力学(相图)!
  得到的马氏体过饱和碳 + 切变畸变 = 超硬但脆,需回火。

  汇聚的伏笔:Ch2(铁同素异构 FCC↔BCC)、Ch6(Fe-C相图)、
  Ch9(TTT鼻尖)、Ch10(强化机制)。

演示:
  1. Fe-C 相图关键点(共析反应)
  2. 临界冷却速率:躲过 TTT 鼻尖
  3. 不同冷速 → 不同组织 → 不同硬度
  4. 马氏体转变(无扩散,Ms/Mf 温度)
  5. 回火:硬度-韧性的权衡
  6. 淬透性(Jominy 端淬)

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np


# ============================================================
# 第 1 部分:Fe-C 相图关键点
# ============================================================

def fe_c_diagram():
    """Fe-C 相图(钢侧)关键数据"""
    return {
        'eutectoid_C': 0.76,       # 共析点碳含量 %
        'eutectoid_T': 727,        # 共析温度 °C
        'eutectoid_reaction': 'γ(0.76%C) → α(0.022%C) + Fe3C(6.67%C)',
        'max_C_in_austenite': 2.14,  # γ最大溶碳(1147°C)
        'max_C_in_ferrite': 0.022,   # α最大溶碳(727°C)
        'cementite_C': 6.67,         # 渗碳体 Fe3C
    }


def pearlite_fractions(C_steel):
    """
    共析钢以下(亚共析):杠杆定律算先共析铁素体 + 珠光体
    C_steel: 钢的碳含量 %
    """
    fe_c = fe_c_diagram()
    C_eut = fe_c['eutectoid_C']
    C_alpha = fe_c['max_C_in_ferrite']
    if C_steel < C_eut:
        # 727°C 刚上方:先共析α + 剩余γ(将变珠光体)
        f_proeutectoid_alpha = (C_eut - C_steel) / (C_eut - C_alpha)
        f_pearlite = 1 - f_proeutectoid_alpha
    else:
        f_proeutectoid_alpha = 0
        f_pearlite = 1.0
    return {'proeutectoid_alpha': f_proeutectoid_alpha, 'pearlite': f_pearlite}


# ============================================================
# 第 2 部分:冷速 → 组织 → 硬度
# ============================================================

def cooling_microstructure(cooling_rate_C_per_s):
    """
    冷速决定组织(共析钢简化模型)
    慢冷→珠光体, 中冷→贝氏体, 快冷(>临界)→马氏体
    返回 组织类型 + 大致硬度(HRC)
    """
    # 临界冷却速率(躲过 TTT 鼻尖)约 ~100-200 °C/s(简化)
    critical_rate = 150
    if cooling_rate_C_per_s < 0.1:
        return {'rate': cooling_rate_C_per_s, 'microstructure': '粗珠光体',
                'hardness_HRC': 15, 'mechanism': '完全扩散(平衡)'}
    elif cooling_rate_C_per_s < 10:
        return {'rate': cooling_rate_C_per_s, 'microstructure': '细珠光体',
                'hardness_HRC': 25, 'mechanism': '扩散(接近平衡)'}
    elif cooling_rate_C_per_s < critical_rate:
        return {'rate': cooling_rate_C_per_s, 'microstructure': '贝氏体',
                'hardness_HRC': 45, 'mechanism': '半扩散'}
    else:
        return {'rate': cooling_rate_C_per_s, 'microstructure': '马氏体',
                'hardness_HRC': 65, 'mechanism': '无扩散切变(躲过鼻尖!)'}


def cooling_demo():
    """不同冷速的组织和硬度"""
    rates = [0.01, 1, 50, 200, 1000]
    return [cooling_microstructure(r) for r in rates]


# ============================================================
# 第 3 部分:马氏体转变
# ============================================================

def martensite_start(C_percent):
    """
    马氏体开始转变温度 Ms(经验公式,Andrews)
    Ms(°C) = 539 - 423·C - ... (简化只考虑碳)
    C_percent: 碳含量 %
    """
    Ms = 539 - 423 * C_percent
    Mf = Ms - 215  # 马氏体结束温度(近似)
    return {'C': C_percent, 'Ms': Ms, 'Mf': Mf}


def martensite_fraction(T, Ms, alpha=0.011):
    """
    Koistinen-Marburger 方程:马氏体转变量
    f = 1 - exp(-α(Ms - T))  (T < Ms)
    马氏体转变只取决于温度,不取决于时间(无扩散!)
    """
    if T >= Ms:
        return 0.0
    return 1 - np.exp(-alpha * (Ms - T))


def martensite_demo():
    """马氏体转变随温度(无扩散,只看过冷到多少)"""
    ms_data = martensite_start(0.76)
    Ms = ms_data['Ms']
    results = []
    for T in [Ms, Ms-50, Ms-100, Ms-150, Ms-215]:
        f = martensite_fraction(T, Ms)
        results.append({'T': T, 'fraction': f})
    return {'Ms': Ms, 'Mf': ms_data['Mf'], 'data': results}


# ============================================================
# 第 4 部分:回火(硬度-韧性权衡)
# ============================================================

def tempering(temper_T_C):
    """
    回火:重新加热马氏体,让碳析出,降硬度增韧性
    temper_T_C: 回火温度
    返回 硬度(HRC)和韧性(相对)
    """
    # 回火温度越高,硬度越低,韧性越高
    hardness = 65 - 0.06 * temper_T_C   # 简化线性
    toughness = 10 + 0.15 * temper_T_C  # 相对韧性
    return {'temper_T': temper_T_C, 'hardness_HRC': max(hardness, 20),
            'toughness_rel': toughness}


def tempering_demo():
    """不同回火温度的硬度-韧性权衡"""
    return [tempering(T) for T in [150, 300, 450, 600]]


# ============================================================
# 第 5 部分:淬透性(Jominy)
# ============================================================

def jominy_hardness(distance_mm, hardenability='low'):
    """
    Jominy 端淬:距淬火端不同距离的硬度
    距离越远冷速越慢 → 硬度越低
    淬透性高的钢(含合金元素)硬度下降慢
    """
    if hardenability == 'high':  # 合金钢(如4340)
        return 60 * np.exp(-distance_mm / 50)
    else:  # 碳钢(如1040)
        return 60 * np.exp(-distance_mm / 8)


def jominy_demo():
    """碳钢 vs 合金钢的淬透性对比"""
    results = []
    for d in [1.5, 5, 10, 20, 40]:
        h_low = jominy_hardness(d, 'low')
        h_high = jominy_hardness(d, 'high')
        results.append({'distance_mm': d, 'carbon_steel': h_low,
                        'alloy_steel': h_high})
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("热处理 · 静与动的博弈(全书高潮:马氏体之谜)")
    print("=" * 64)

    print("\n【全书伏笔在此汇聚】")
    print("  Ch2: 铁的同素异构 FCC(γ) ↔ BCC(α)")
    print("  Ch6: Fe-C 相图说'该得珠光体'(平衡/静)")
    print("  Ch9: TTT 曲线的'鼻尖'(动力学)")
    print("  Ch10: 强化机制")
    print("  => 这一章,静(相图)与动(冷速)正面对决!")

    # --- Fe-C 相图 ---
    print("\n【1. Fe-C 相图:共析反应】")
    fc = fe_c_diagram()
    print(f"  共析点: {fc['eutectoid_C']}%C, {fc['eutectoid_T']}°C")
    print(f"  共析反应: {fc['eutectoid_reaction']}")
    print(f"  → 平衡冷却:奥氏体分解成珠光体(α+Fe3C层片)")
    pf = pearlite_fractions(0.4)
    print(f"  0.4%C亚共析钢: 先共析铁素体 {pf['proeutectoid_alpha']*100:.0f}% + 珠光体 {pf['pearlite']*100:.0f}%")

    # --- 冷速→组织 ---
    print("\n【2. 冷速 → 组织 → 硬度(核心!)】")
    print(f"  {'冷速(°C/s)':>12} {'组织':>10} {'硬度HRC':>8} {'机制':>18}")
    for r in cooling_demo():
        print(f"  {r['rate']:10} {r['microstructure']:>10} {r['hardness_HRC']:6} "
              f"  {r['mechanism']:>16}")
    print("  → 同一块钢,冷速不同,硬度从15到65 HRC(差4倍多)!")
    print("    慢冷=扩散=平衡=珠光体(软);快冷=躲鼻尖=马氏体(硬)")

    # --- 马氏体转变 ---
    print("\n【3. 马氏体转变:无扩散切变(动力学的胜利)】")
    md = martensite_demo()
    print(f"  共析钢(0.76%C): Ms={md['Ms']:.0f}°C, Mf={md['Mf']:.0f}°C")
    print(f"  {'温度°C':>8} {'马氏体分数':>12}")
    for r in md['data']:
        print(f"  {r['T']:8.0f} {r['fraction']:10.3f}")
    print("  → 关键:马氏体转变只看'冷到多少温度',与时间无关!")
    print("    因为无扩散——FCC瞬间切变成BCT,碳被困在里面(过饱和)")
    print("    过饱和碳撑开晶格 + 切变畸变 = 超硬(但脆)")

    # --- 回火 ---
    print("\n【4. 回火:硬度-韧性的权衡】")
    print("  马氏体太脆,要回火(重新加热)让碳部分析出")
    print(f"  {'回火温度°C':>12} {'硬度HRC':>8} {'韧性(相对)':>12}")
    for r in tempering_demo():
        print(f"  {r['temper_T']:10} {r['hardness_HRC']:8.0f} {r['toughness_rel']:10.0f}")
    print("  → 回火温度越高,越软越韧:鱼和熊掌的权衡")
    print("    刀刃要硬(低温回火),弹簧要韧(高温回火)")

    # --- 淬透性 ---
    print("\n【5. 淬透性(Jominy端淬):碳钢 vs 合金钢】")
    print(f"  {'距淬火端(mm)':>14} {'碳钢HRC':>10} {'合金钢HRC':>10}")
    for r in jominy_demo():
        print(f"  {r['distance_mm']:12} {r['carbon_steel']:8.0f} {r['alloy_steel']:10.0f}")
    print("  → 合金元素让'鼻尖右移',即使慢冷也能得马氏体(淬透性好)")
    print("    大截面零件必须用合金钢,否则芯部淬不硬")

    print("\n" + "=" * 64)
    print("马氏体之谜解开:相图(静)说该得珠光体,淬火(动)躲过鼻尖")
    print("冻住扩散,逼出无扩散切变 => 动力学战胜热力学!")
    print("这就是'一静一动'的总决战 —— 全书主轴的高潮")
    print("=" * 64)
