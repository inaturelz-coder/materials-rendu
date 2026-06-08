# 配套代码模块

每章一个 Python 模块，演示该章的核心概念与「Aha 时刻」。

**特点**：纯 `numpy`/`scipy`，真实材料数据，无需联网，可独立运行。每个模块直接 `python3 xxx.py` 即可看到带注释的输出。

```bash
pip install numpy scipy
python3 atomic_structure.py
```

## 模块索引

### 任脉 · 静
| 模块 | 章 | 核心演示 |
|---|---|---|
| `atomic_structure.py` | Ch1 | 类氢能级 / 电子排布(Fe=3d⁶) / 周期性 / 电负性键合判据 |
| `crystal_structure.py` | Ch2 | 堆垛因子 / 理论密度(误差<0.3%) / 布拉格定律 / XRD 选择定则 |
| `crystal_defects.py` | Ch3 | 空位 Arrhenius / Taylor 位错强化 / Hall-Petch / TEM g·b 判据 |
| `microstructure.py` | Ch4 | ASTM 晶粒度 / 杠杆定律 / 体视学(2D→3D) / 组织设计强度差 83% |
| `thermodynamics.py` | Ch5 | Gibbs 自由能 / 混合熵 / 规则溶液 / 公切线法(CALPHAD 内核) |
| `phase_diagram.py` | Ch6 | 杠杆定律 / 匀晶 / 共晶(Pb-Sn) / 冷却路径 / 从自由能生成相图 |
| `calphad.py` | Ch7 | Redlich-Kister / 子格模型 / 参数优化 / Muggianu 多元外推 |

### 督脉 · 动
| 模块 | 章 | 核心演示 |
|---|---|---|
| `diffusion.py` | Ch8 | 渗碳误差函数解 / Arrhenius / √Dt 标度律 / 空位机制 / 数值解 |
| `phase_kinetics.py` | Ch9 | 临界核 r* / 形核率 C 曲线 / Avrami / TTT 曲线 |
| `dislocation_motion.py` | Ch10 | Schmid 定律 / 理论vs实际强度 / 加工硬化 / 应力应变曲线 |
| `heat_treatment.py` | Ch11 | Fe-C 相图 / 冷速→组织→硬度 / 马氏体(Koistinen-Marburger) / 回火 / 淬透性 |
| `phase_field.py` | Ch12 | 双势阱 / Cahn-Hilliard 调幅分解 / Allen-Cahn / 界面标度律 |

### 任督交汇
| 模块 | 章 | 核心演示 |
|---|---|---|
| `mechanical_fem.py` | Ch13 | 力学量提取 / 四大强化叠加 / 强韧权衡 / 一维有限元 / 应力集中 |
| `electronic_properties.py` | Ch14 | 能带带隙 / 半导体载流子 / 铁磁居里温度 / 热容 / Wiedemann-Franz |
| `failure_life.py` | Ch15 | 断裂韧性 / S-N 疲劳 / 蠕变速率 / 电化学序 / 牺牲阳极 |

## 注意

- 所有数据均为真实材料参数（取自标准教科书），不是编造的演示值。
- 代码以**清晰、可读、可教学**为第一目标，不追求工业级性能。
- 工业级计算请用专业软件：Thermo-Calc/pycalphad(CALPHAD)、MOOSE/PRISMS-PF(相场)、ABAQUS/ANSYS(FEM)、VASP/Quantum ESPRESSO(DFT)。
