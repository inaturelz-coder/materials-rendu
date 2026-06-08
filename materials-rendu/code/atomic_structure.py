"""
atomic_structure.py
====================
《打通材料基础任督二脉》Ch1 配套模块

主题:原子结构与电子排布 —— 一切材料性质的最底层

核心思想:材料的宏观性质(导电、磁性、强度、颜色),
  最终都能追溯到原子的电子排布。这一章用真实数据,
  让你看见"电子排布 → 材料性质"这条因果链。

演示:
  1. 类氢原子能级 + 屏蔽效应(为什么周期表这样排)
  2. 电子排布自动生成(Madelung 能量排序规则)
  3. 原子半径/电离能随原子序数的周期性
  4. 键合类型判据(电负性差 → 离子/共价/金属)
  5. 库仑势井 + 玻尔半径数量级估计

Li Zhou <lizhou_alfred2011@hotmail.com> · MIT License
"""

import numpy as np


# ============================================================
# 第 1 部分:类氢原子能级 + 屏蔽
# ============================================================

# 物理常数(SI)
EV = 1.602176634e-19      # 1 电子伏特 (J)
RYDBERG_EV = 13.605693     # 里德伯能量 (eV)
BOHR_RADIUS = 5.29177e-11  # 玻尔半径 (m)


def hydrogen_energy_level(n, Z=1):
    """
    类氢原子能级 E_n = -13.6 * Z^2 / n^2  (eV)
    Z: 有效核电荷; n: 主量子数
    """
    return -RYDBERG_EV * Z**2 / n**2


def bohr_radius(n, Z=1):
    """玻尔半径 r_n = n^2 / Z * a_0"""
    return n**2 / Z * BOHR_RADIUS


def hydrogen_spectrum():
    """氢原子的几条著名谱线(Lyman/Balmer 系)"""
    lines = []
    # Balmer 系(可见光,n -> 2)
    for n in [3, 4, 5, 6]:
        dE = hydrogen_energy_level(n) - hydrogen_energy_level(2)  # 释放能量(正值)
        # E = hc/lambda  => lambda = hc/E
        hc = 1239.84  # eV·nm
        wavelength = hc / dE
        lines.append({'series': 'Balmer', 'transition': f'{n}->2',
                      'dE_eV': dE, 'wavelength_nm': wavelength})
    return lines


# ============================================================
# 第 2 部分:电子排布(Madelung 规则)
# ============================================================

def madelung_order():
    """
    生成轨道填充顺序(Madelung / 能量最低原理)
    规则:按 (n+l) 排序,(n+l) 相同则按 n 排序
    返回:[(n, l, 轨道名, 容量), ...]
    """
    l_names = {0: 's', 1: 'p', 2: 'd', 3: 'f'}
    l_capacity = {0: 2, 1: 6, 2: 10, 3: 14}
    orbitals = []
    for n in range(1, 8):
        for l in range(0, min(n, 4)):  # l 最多到 3(f 轨道)
            orbitals.append((n, l))
    # 按 (n+l, n) 排序
    orbitals.sort(key=lambda x: (x[0] + x[1], x[0]))
    result = []
    for n, l in orbitals:
        result.append((n, l, f'{n}{l_names[l]}', l_capacity[l]))
    return result


def electron_configuration(Z):
    """
    给定原子序数 Z,自动生成电子排布
    返回排布字符串(简化,不含洪特规则/特例)
    """
    order = madelung_order()
    config = []
    remaining = Z
    for n, l, name, cap in order:
        if remaining <= 0:
            break
        fill = min(remaining, cap)
        config.append(f'{name}{fill}')
        remaining -= fill
    return ' '.join(config)


def valence_electrons(Z):
    """估计价电子数(最外层 s+p,简化)"""
    order = madelung_order()
    remaining = Z
    shells = {}
    for n, l, name, cap in order:
        if remaining <= 0:
            break
        fill = min(remaining, cap)
        shells.setdefault(n, 0)
        shells[n] += fill
        remaining -= fill
    max_n = max(shells.keys())
    return shells[max_n]


# ============================================================
# 第 3 部分:周期性 —— 原子半径与电离能
# ============================================================

# 真实数据:前 20 号元素(实验值)
# 原子半径 (pm), 第一电离能 (eV), Pauling 电负性
ELEMENTS = {
    1:  ('H',  53,  13.60, 2.20),
    2:  ('He', 31,  24.59, None),
    3:  ('Li', 167, 5.39,  0.98),
    4:  ('Be', 112, 9.32,  1.57),
    5:  ('B',  87,  8.30,  2.04),
    6:  ('C',  67,  11.26, 2.55),
    7:  ('N',  56,  14.53, 3.04),
    8:  ('O',  48,  13.62, 3.44),
    9:  ('F',  42,  17.42, 3.98),
    10: ('Ne', 38,  21.56, None),
    11: ('Na', 190, 5.14,  0.93),
    12: ('Mg', 145, 7.65,  1.31),
    13: ('Al', 118, 5.99,  1.61),
    14: ('Si', 111, 8.15,  1.90),
    15: ('P',  98,  10.49, 2.19),
    16: ('S',  88,  10.36, 2.58),
    17: ('Cl', 79,  12.97, 3.16),
    18: ('Ar', 71,  15.76, None),
    19: ('K',  243, 4.34,  0.82),
    20: ('Ca', 194, 6.11,  1.00),
}


def periodicity_analysis():
    """分析原子半径和电离能的周期性"""
    # 第二周期 (Li-Ne) 和第三周期 (Na-Ar)
    period2 = list(range(3, 11))
    period3 = list(range(11, 19))
    out = {'period2': [], 'period3': []}
    for Z in period2:
        sym, r, ie, en = ELEMENTS[Z]
        out['period2'].append({'Z': Z, 'sym': sym, 'radius_pm': r, 'IE_eV': ie})
    for Z in period3:
        sym, r, ie, en = ELEMENTS[Z]
        out['period3'].append({'Z': Z, 'sym': sym, 'radius_pm': r, 'IE_eV': ie})
    return out


# ============================================================
# 第 4 部分:键合类型判据(电负性差)
# ============================================================

def bond_type(Z1, Z2):
    """
    根据 Pauling 电负性差判断键合类型
    ΔEN > 1.7  : 离子键
    0.4-1.7    : 极性共价键
    < 0.4      : 非极性共价键 / 金属键
    """
    en1 = ELEMENTS[Z1][3]
    en2 = ELEMENTS[Z2][3]
    if en1 is None or en2 is None:
        return None
    diff = abs(en1 - en2)
    # 离子性百分比(Pauling 公式)
    ionic_pct = (1 - np.exp(-0.25 * diff**2)) * 100
    if diff > 1.7:
        btype = '离子键'
    elif diff > 0.4:
        btype = '极性共价键'
    else:
        btype = '共价键/金属键'
    return {'EN1': en1, 'EN2': en2, 'diff': diff,
            'ionic_pct': ionic_pct, 'type': btype}


def common_materials_bonding():
    """几个常见材料的键合分析"""
    pairs = [
        ('NaCl 食盐', 11, 17),
        ('MgO 氧化镁', 12, 8),
        ('SiC 碳化硅', 14, 6),
        ('Al2O3 刚玉', 13, 8),
        ('金刚石 C-C', 6, 6),
        ('Si-Si 硅', 14, 14),
    ]
    results = []
    for name, z1, z2 in pairs:
        bt = bond_type(z1, z2)
        if bt:
            results.append((name, bt))
    return results


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 64)
    print("原子结构与电子排布 · 一切材料性质的最底层")
    print("=" * 64)

    # --- 类氢能级 ---
    print("\n【1. 类氢原子能级:为什么电子不会掉进原子核】")
    print("  氢原子能级 E_n = -13.6/n^2 eV:")
    for n in [1, 2, 3, 4]:
        E = hydrogen_energy_level(n)
        r = bohr_radius(n) * 1e12  # pm
        print(f"    n={n}: E = {E:7.3f} eV,  轨道半径 = {r:6.1f} pm")
    print(f"  基态(n=1)能量最低 = -13.6 eV —— 这是电子的'坑底'")
    print(f"  电离能 = 0-(-13.6) = 13.6 eV,与实测完全一致")

    print("\n  氢原子 Balmer 系谱线(可见光):")
    for line in hydrogen_spectrum():
        print(f"    {line['transition']}: ΔE={line['dE_eV']:.3f} eV, "
              f"λ={line['wavelength_nm']:.1f} nm")
    print("  → 656 nm 红线就是这么来的(天文学家测氢的指纹)")

    # --- 电子排布 ---
    print("\n【2. 电子排布:Madelung 规则自动生成】")
    print("  轨道填充顺序(能量从低到高):")
    order = madelung_order()
    print("   ", ' '.join(o[2] for o in order[:12]))
    print("\n  几个关键元素的电子排布:")
    for Z in [6, 11, 13, 14, 26]:
        sym = ELEMENTS.get(Z, (f'Z{Z}',))[0]
        config = electron_configuration(Z)
        print(f"    {sym:3}(Z={Z:2}): {config}")
    print("  → Fe(Z=26)的 3d 电子是它磁性的来源(后面章节细讲)")

    # --- 周期性 ---
    print("\n【3. 周期性:为什么周期表是'周期'的】")
    data = periodicity_analysis()
    print("  第二周期原子半径(pm)—— 从左到右收缩:")
    print("   ", ' '.join(f"{e['sym']}:{e['radius_pm']}" for e in data['period2']))
    print("  第二周期第一电离能(eV)—— 从左到右升高:")
    print("   ", ' '.join(f"{e['sym']}:{e['IE_eV']:.1f}" for e in data['period2']))
    r_li = ELEMENTS[3][1]; r_ne = ELEMENTS[10][1]
    print(f"  → Li→Ne 半径从 {r_li}→{r_ne} pm,缩小 {(1-r_ne/r_li)*100:.0f}%")
    print(f"    核电荷增加但电子填同一层,核拉得更紧 = 半径收缩")

    # --- 键合类型 ---
    print("\n【4. 键合判据:电负性差决定材料类型】")
    print(f"  {'材料':14} {'ΔEN':>5} {'离子性%':>8}  类型")
    print("  " + "-" * 44)
    for name, bt in common_materials_bonding():
        print(f"  {name:14} {bt['diff']:5.2f} {bt['ionic_pct']:7.1f}%  {bt['type']}")
    print("  → 同样是固体,NaCl 脆而绝缘,金刚石硬而导热")
    print("    Si 半导体 —— 根源都在这张电负性差的表里")

    print("\n" + "=" * 64)
    print("电子排布 → 键合 → 结构 → 性质:材料科学的因果链从这里开始")
    print("=" * 64)
