"""
failure_life.py
===============
《打通材料基础任督二脉》Ch15 配套模块(全书收官)

主题:失效与寿命 —— 材料的终点

核心思想:材料终会失效。四种主要失效模式,每一种都连着前面的章节:
  - 断裂(接 Ch13 应力集中):裂纹扩展,断裂力学 K_IC
  - 疲劳(接 Ch10 位错往复):循环载荷下裂纹萌生扩展
  - 蠕变(接 Ch8 扩散 + Ch10 攀移):高温长期缓慢变形
  - 腐蚀(接 Ch1 电子转移 + Ch5 氧化ΔG):电化学损耗

  这是全书收官:把所有失效伏笔收拢,讲材料如何"死亡",如何预测寿命。

演示:
  1. 断裂力学:应力强度因子 K、断裂韧性 K_IC、临界裂纹尺寸
  2. 疲劳:S-N 曲线、疲劳极限
  3. 蠕变:稳态蠕变速率(接 Ch10 攀移)
  4. 腐蚀:电化学序、相对腐蚀倾向
  5. 寿命预测综合

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

R = 8.314


# ============================================================
# 第 1 部分:断裂力学(接 Ch13 应力集中)
# ============================================================

def stress_intensity(sigma_MPa, crack_a_mm, Y=1.12):
    """
    应力强度因子 K = Y·σ·√(πa)
    Y: 几何因子(表面裂纹~1.12)
    a: 裂纹尺寸(mm)
    当 K 达到断裂韧性 K_IC 时,裂纹失稳扩展 → 断裂
    """
    a = crack_a_mm * 1e-3  # m
    K = Y * sigma_MPa * np.sqrt(np.pi * a)  # MPa·√m
    return K


def critical_crack_size(sigma_MPa, K_IC, Y=1.12):
    """
    临界裂纹尺寸:K = K_IC 时的裂纹长度
    a_c = (K_IC / (Y·σ))² / π
    小于此尺寸的裂纹安全,大于则灾难性断裂
    """
    a_c = (K_IC / (Y * sigma_MPa))**2 / np.pi
    return a_c * 1e3  # m -> mm


def fracture_demo():
    """不同材料的断裂韧性与临界裂纹"""
    # (材料, 断裂韧性 K_IC MPa·√m, 工作应力 MPa)
    materials = [
        ('高强钢', 50, 1000),
        ('铝合金', 30, 300),
        ('陶瓷Al2O3', 4, 200),
        ('韧性钢', 100, 400),
    ]
    results = []
    for name, kic, sigma in materials:
        a_c = critical_crack_size(sigma, kic)
        results.append({'name': name, 'K_IC': kic, 'sigma': sigma,
                        'a_critical_mm': a_c})
    return results


# ============================================================
# 第 2 部分:疲劳(接 Ch10 位错往复)
# ============================================================

def fatigue_life(stress_amplitude, sigma_f=900, b=-0.1):
    """
    Basquin 定律:S-N 曲线
    σ_a = σ_f' · (2N)^b
    反解循环数 N
    sigma_f: 疲劳强度系数, b: 疲劳强度指数
    """
    # σ_a = σ_f·(2N)^b => N = 0.5·(σ_a/σ_f)^(1/b)
    N = 0.5 * (stress_amplitude / sigma_f)**(1/b)
    return N


def fatigue_demo():
    """S-N 曲线:应力幅 vs 寿命"""
    results = []
    for sigma_a in [600, 450, 350, 280, 250]:
        N = fatigue_life(sigma_a)
        results.append({'stress_amp': sigma_a, 'cycles': N})
    return results


def endurance_limit():
    """疲劳极限:钢有(应力低于此无限寿命),铝没有"""
    return {
        '钢': {'has_limit': True, 'limit_MPa': 250,
               'note': '低于250MPa可无限循环'},
        '铝合金': {'has_limit': False, 'limit_MPa': None,
                   'note': '无疲劳极限,总会失效(定10^7次的疲劳强度)'},
    }


# ============================================================
# 第 3 部分:蠕变(接 Ch8 扩散 + Ch10 攀移)
# ============================================================

def steady_creep_rate(sigma_MPa, T_C, A=1e-5, n=5, Q_kJ=300):
    """
    稳态蠕变速率(幂律蠕变,接 Ch10 位错攀移):
    ε̇ = A·σ^n·exp(-Q/RT)
    σ^n:应力依赖(位错蠕变 n~3-8)
    exp(-Q/RT):温度依赖(攀移靠扩散,接 Ch8)
    """
    T = T_C + 273.15
    rate = A * sigma_MPa**n * np.exp(-Q_kJ*1000 / (R * T))
    return rate


def creep_demo():
    """蠕变速率的温度和应力依赖"""
    results = []
    for T_C in [500, 600, 700, 800]:
        rate = steady_creep_rate(100, T_C)
        results.append({'T_C': T_C, 'rate': rate})
    return results


def creep_stress_demo():
    """蠕变速率的应力依赖(幂律)"""
    results = []
    for sigma in [50, 100, 150, 200]:
        rate = steady_creep_rate(sigma, 700)
        results.append({'sigma': sigma, 'rate': rate})
    return results


# ============================================================
# 第 4 部分:腐蚀(接 Ch1 电子 + Ch5 氧化)
# ============================================================

def galvanic_series():
    """
    电化学序(标准电极电位,V vs SHE)
    电位越负越活泼(易腐蚀/被氧化);越正越惰性(耐腐蚀)
    接 Ch1(电子转移倾向)+ Ch5(氧化 ΔG)
    """
    series = [
        ('金 Au', 1.50, '最惰性(不腐蚀)'),
        ('铂 Pt', 1.18, '惰性'),
        ('银 Ag', 0.80, '较惰性'),
        ('铜 Cu', 0.34, '较惰性'),
        ('氢 H', 0.00, '参考'),
        ('铁 Fe', -0.44, '活泼(易锈)'),
        ('锌 Zn', -0.76, '活泼(牺牲阳极)'),
        ('铝 Al', -1.66, '活泼(但有钝化膜)'),
        ('镁 Mg', -2.37, '最活泼'),
    ]
    return series


def galvanic_corrosion(metal1, E1, metal2, E2):
    """
    电偶腐蚀:两种金属接触,电位低的(活泼)被腐蚀
    电位差越大,腐蚀越剧烈
    """
    if E1 < E2:
        anode, cathode = metal1, metal2
    else:
        anode, cathode = metal2, metal1
    driving = abs(E1 - E2)
    return {'anode_corroded': anode, 'cathode_protected': cathode,
            'driving_force_V': driving}


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("失效与寿命 · 材料的终点(全书收官)")
    print("=" * 64)

    print("\n【四种失效模式,每种都连着前面的章节】")
    print("  断裂 ← Ch13 应力集中(裂纹扩展)")
    print("  疲劳 ← Ch10 位错往复(循环载荷)")
    print("  蠕变 ← Ch8 扩散 + Ch10 攀移(高温长期)")
    print("  腐蚀 ← Ch1 电子转移 + Ch5 氧化ΔG(电化学)")

    # --- 断裂力学 ---
    print("\n【1. 断裂力学:K = Y·σ·√(πa)(接 Ch13 应力集中)】")
    print("  应力强度因子 K 达到断裂韧性 K_IC → 裂纹失稳 → 断裂")
    print(f"  {'材料':12} {'K_IC':>8} {'应力MPa':>8} {'临界裂纹(mm)':>14}")
    for r in fracture_demo():
        print(f"  {r['name']:10} {r['K_IC']:8} {r['sigma']:8} {r['a_critical_mm']:12.2f}")
    print("  → 陶瓷K_IC低,几十微米的裂纹就崩(脆);韧性钢能容忍mm级裂纹")
    print("    这就是为什么陶瓷怕磕碰 —— 小裂纹=大灾难")

    # --- 疲劳 ---
    print("\n【2. 疲劳:S-N 曲线(接 Ch10 位错往复)】")
    print("  80%的机械失效是疲劳:循环载荷下裂纹萌生→扩展→断裂")
    print(f"  {'应力幅(MPa)':>12} {'循环寿命(次)':>16}")
    for r in fatigue_demo():
        print(f"  {r['stress_amp']:10} {r['cycles']:16.2e}")
    print("  → 应力越高,寿命越短(指数关系)")
    el = endurance_limit()
    for metal, info in el.items():
        print(f"  {metal}: {info['note']}")
    print("  → 钢有疲劳极限(低应力无限寿命),铝没有(总会失效)")

    # --- 蠕变 ---
    print("\n【3. 蠕变:ε̇ = A·σ^n·exp(-Q/RT)(接 Ch10 攀移+Ch8 扩散)】")
    print("  高温长期受力,缓慢变形(涡轮叶片、锅炉管的寿命杀手)")
    print(f"  温度依赖(σ=100MPa):")
    print(f"  {'温度°C':>8} {'蠕变速率(相对)':>16}")
    base = None
    for r in creep_demo():
        if base is None: base = r['rate']
        print(f"  {r['T_C']:8} {r['rate']:14.3e}")
    top = creep_demo()[-1]['rate']
    print(f"  → 500→800°C,蠕变速率增大 {top/base:.0f} 倍(攀移靠扩散,Arrhenius)")
    print(f"  应力依赖(700°C,幂律 n=5):")
    for r in creep_stress_demo():
        print(f"    σ={r['sigma']}MPa: 速率 {r['rate']:.3e}")
    print("  → 应力翻倍,蠕变速率涨 2^5=32 倍(幂律敏感)")

    # --- 腐蚀 ---
    print("\n【4. 腐蚀:电化学序(接 Ch1 电子 + Ch5 氧化)】")
    print("  电位越负越活泼(易腐蚀);越正越惰性(耐蚀)")
    print(f"  {'金属':10} {'电极电位(V)':>12} {'倾向':>18}")
    for name, E, note in galvanic_series():
        print(f"  {name:8} {E:10.2f}   {note:>16}")
    print("\n  电偶腐蚀例子:钢船用锌块保护(牺牲阳极)")
    gc = galvanic_corrosion('铁 Fe', -0.44, '锌 Zn', -0.76)
    print(f"    锌(-0.76V)比铁(-0.44V)活泼 → {gc['anode_corroded']}被腐蚀")
    print(f"    铁被保护! 驱动力 {gc['driving_force_V']:.2f}V")
    print("  → 镀锌、牺牲阳极:用更活泼的金属保护主体(电化学原理)")

    print("\n" + "=" * 64)
    print("四种失效都连着前面章节:断裂(Ch13)/疲劳(Ch10)/蠕变(Ch8+10)/腐蚀(Ch1+5)")
    print("材料终会失效 —— 但懂了机理,就能预测寿命、延缓终点")
    print("=" * 64)

    print("\n" + "=" * 64)
    print("【全书终】打通材料基础任督二脉")
    print("  任脉(静):原子→晶体→缺陷→组织→热力学→相图→CALPHAD")
    print("  督脉(动):扩散→相变→位错→热处理→相场")
    print("  交汇:力学+FEM→电磁热+DFT→失效")
    print("  四组对仗 + 结构决定性能 + 多尺度计算 + 怎么看见它")
    print("=" * 64)
