"""
crystal_defects.py
==================
《打通材料基础任督二脉》Ch3 配套模块

主题:晶体缺陷的几何 —— 完美晶体里的"不完美"

核心思想:真实晶体没有完美的。点缺陷(空位)、线缺陷(位错)、
  面缺陷(晶界)——这些"缺陷"恰恰决定了材料的强度、塑性、扩散。
  本章讲缺陷的"几何"(静态);它们怎么"运动"留给 Ch10(动态对仗)。

演示:
  1. 平衡空位浓度的 Arrhenius 行为(温度的指数敏感)
  2. 位错密度与强度(Taylor 关系)
  3. 缺陷的维度分类与尺度
  4. Hall-Petch:晶粒越细越强
  5. "怎么看见它":TEM 衍射衬度 + g·b=0 不可见判据

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np

# 物理常数
K_B = 8.617333e-5   # 玻尔兹曼常数 (eV/K)


# ============================================================
# 第 1 部分:平衡空位浓度(点缺陷)
# ============================================================

def vacancy_concentration(T, Q_f=0.9):
    """
    平衡空位浓度 n_v/N = exp(-Q_f / k_B T)
    Q_f: 空位形成能 (eV),典型金属 0.7-1.1 eV
    T: 温度 (K)
    """
    return np.exp(-Q_f / (K_B * T))


def vacancy_vs_temperature():
    """空位浓度随温度的剧烈变化(以铜为例,Q_f≈0.9 eV)"""
    results = []
    for T in [300, 500, 800, 1000, 1356]:  # 1356 K = 铜熔点
        c = vacancy_concentration(T, Q_f=0.9)
        results.append({'T_K': T, 'T_C': T - 273,
                        'concentration': c,
                        'one_per': 1/c if c > 0 else np.inf})
    return results


# ============================================================
# 第 2 部分:位错密度与强度(线缺陷)
# ============================================================

def taylor_strengthening(rho_disloc, alpha=0.5, G=45e9, b=0.256e-9):
    """
    Taylor 关系:位错强化 Δτ = α·G·b·√ρ
    rho_disloc: 位错密度 (/m²)
    alpha: 常数 ~0.3-0.6
    G: 剪切模量 (Pa),默认铁 ~45 GPa(用铜的 b)
    b: 柏氏矢量 (m)
    返回 强度增量 (MPa)
    """
    delta_tau = alpha * G * b * np.sqrt(rho_disloc)
    return delta_tau / 1e6  # Pa -> MPa


def dislocation_density_effect():
    """退火态 vs 冷加工态的位错密度与强度"""
    states = [
        ('充分退火', 1e10),    # /m²
        ('轻度冷加工', 1e12),
        ('中度冷加工', 1e14),
        ('重度冷加工', 1e15),
    ]
    results = []
    for name, rho in states:
        dtau = taylor_strengthening(rho)
        results.append({'state': name, 'rho': rho, 'delta_tau_MPa': dtau})
    return results


# ============================================================
# 第 3 部分:缺陷的维度分类
# ============================================================

DEFECT_TAXONOMY = [
    ('0维 点缺陷', '空位 / 间隙原子 / 置换原子', '~0.1 nm', '扩散 / 电阻 / 掺杂'),
    ('1维 线缺陷', '刃位错 / 螺位错', '长度 µm 级', '塑性 / 强度 / 加工硬化'),
    ('2维 面缺陷', '晶界 / 相界 / 孪晶界 / 表面', '~nm 厚', '强度 / 腐蚀 / 晶粒长大'),
    ('3维 体缺陷', '孔洞 / 夹杂 / 第二相', 'µm-mm', '断裂 / 疲劳源'),
]


# ============================================================
# 第 4 部分:Hall-Petch(晶粒越细越强)
# ============================================================

def hall_petch(grain_size_um, sigma_0=50, k_y=0.7):
    """
    Hall-Petch 关系:σ_y = σ_0 + k_y / √d
    grain_size_um: 晶粒尺寸 (µm)
    sigma_0: 晶格摩擦应力 (MPa)
    k_y: Hall-Petch 系数 (MPa·√mm),典型低碳钢 ~0.7
    返回 屈服强度 (MPa)
    """
    d_mm = grain_size_um * 1e-3
    return sigma_0 + k_y / np.sqrt(d_mm)


def grain_size_effect():
    """晶粒尺寸对屈服强度的影响(低碳钢)"""
    results = []
    for d in [100, 50, 20, 10, 5, 1]:  # µm
        sigma = hall_petch(d)
        results.append({'grain_um': d, 'sigma_y_MPa': sigma})
    return results


# ============================================================
# 第 5 部分:"怎么看见它"——TEM g·b 不可见判据
# ============================================================

def gb_invisibility(g, b):
    """
    TEM 位错衬度的 g·b 判据:
    当 g·b = 0 时,位错在该衍射条件下"不可见"
    g: 衍射矢量 (hkl), b: 柏氏矢量 [uvw]
    返回 点积(=0 则不可见)
    """
    return int(np.dot(g, b))


def burgers_vector_analysis():
    """
    用两个不同 g,通过 g·b=0 判据确定未知位错的柏氏矢量
    这是 TEM 测位错柏氏矢量的实际方法
    """
    # FCC 中常见柏氏矢量(省略 1/2 因子,只看方向)
    candidate_b = {
        '[110]': np.array([1, 1, 0]),
        '[1-10]': np.array([1, -1, 0]),
        '[101]': np.array([1, 0, 1]),
        '[011]': np.array([0, 1, 1]),
    }
    # 实验:用两个衍射矢量观察
    g1 = np.array([2, 0, 0])   # g=(200) 时位错可见
    g2 = np.array([1, 1, 1])   # g=(111) 时位错不可见
    results = []
    for name, b in candidate_b.items():
        gb1 = gb_invisibility(g1, b)
        gb2 = gb_invisibility(g2, b)
        # 实验观察:g1 下可见(g·b≠0), g2 下不可见(g·b=0)
        consistent = (gb1 != 0) and (gb2 == 0)
        results.append({'b': name, 'g1_dot_b': gb1, 'g2_dot_b': gb2,
                        'matches_observation': consistent})
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("晶体缺陷的几何 · 完美晶体里的'不完美'")
    print("=" * 64)

    # --- 缺陷分类 ---
    print("\n【1. 缺陷的维度分类】")
    print(f"  {'维度':14} {'例子':28} {'尺度':12} 影响")
    print("  " + "-" * 70)
    for dim, ex, scale, effect in DEFECT_TAXONOMY:
        print(f"  {dim:12} {ex:26} {scale:10} {effect}")

    # --- 空位浓度 ---
    print("\n【2. 点缺陷:平衡空位浓度的 Arrhenius 行为】")
    print("  铜的空位形成能 Q_f ≈ 0.9 eV, n_v/N = exp(-Q_f/kT):")
    print(f"  {'温度':>10} {'空位浓度':>14} {'每多少个原子有1个空位':>22}")
    for r in vacancy_vs_temperature():
        print(f"  {r['T_C']:5}°C ({r['T_K']}K) {r['concentration']:12.3e}  "
              f"  1 / {r['one_per']:.3e}")
    print("  → 室温几乎没有空位,熔点附近每万个原子就有约 1 个空位")
    print("    温度每升高一点,空位浓度指数暴涨 —— 这是扩散的前提(Ch8)")

    # --- 位错强化 ---
    print("\n【3. 线缺陷:位错密度决定强度(Taylor 关系)】")
    print("  Δτ = α·G·b·√ρ  (位错越多越强 —— 加工硬化的本质)")
    print(f"  {'状态':14} {'位错密度(/m²)':>16} {'强度增量(MPa)':>16}")
    for r in dislocation_density_effect():
        print(f"  {r['state']:12} {r['rho']:14.0e}  {r['delta_tau_MPa']:14.1f}")
    print("  → 重度冷加工位错密度比退火高 10万倍,强度增量大幅上升")
    print("    反直觉:'缺陷'(位错)越多,金属反而越强!")

    # --- Hall-Petch ---
    print("\n【4. 面缺陷:晶界越多(晶粒越细)越强(Hall-Petch)】")
    print("  σ_y = σ_0 + k_y/√d  (晶界阻挡位错运动)")
    print(f"  {'晶粒尺寸(µm)':>14} {'屈服强度(MPa)':>16}")
    for r in grain_size_effect():
        print(f"  {r['grain_um']:12} {r['sigma_y_MPa']:14.1f}")
    s100 = hall_petch(100); s1 = hall_petch(1)
    print(f"  → 晶粒从 100µm 细化到 1µm,强度提升 {(s1/s100-1)*100:.0f}%")
    print("    这是唯一'既增强又增韧'的强化方式 —— 晶界是好缺陷")

    # --- TEM g·b ---
    print("\n【5. 怎么看见它:TEM 的 g·b=0 不可见判据】")
    print("  位错在 TEM 下是黑线,但当衍射矢量 g 垂直于柏氏矢量 b 时")
    print("  (即 g·b=0),位错'消失'—— 这反而用来测未知位错的 b!")
    print(f"\n  实验:位错在 g=(200) 下可见,在 g=(111) 下不可见")
    print(f"  {'候选 b':10} {'(200)·b':>10} {'(111)·b':>10} {'符合观察?':>10}")
    for r in burgers_vector_analysis():
        mark = '★ 是它!' if r['matches_observation'] else ''
        print(f"  {r['b']:10} {r['g1_dot_b']:10} {r['g2_dot_b']:10}  {mark}")
    print("  → 用两个 g 做'不可见判据',就能唯一确定位错的柏氏矢量")
    print("    这是 TEM 研究位错的标准方法,不是'看一眼'那么简单")

    print("\n" + "=" * 64)
    print("缺陷不是'瑕疵'而是'功能'：空位→扩散,位错→塑性,晶界→强化")
    print("=" * 64)
