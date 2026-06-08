# 打通材料基础任督二脉

> 一静一动，结构决定性能 —— 一本把零散的材料科学知识串成一张网的入门教材

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

「打通系列」第三本（前两本：《打通科学计算任督二脉》《说与写·完整讲义》）。

---

## 这本书想解决什么问题

材料科学基础最大的痛点是 **知识零散**：晶体结构、相图、扩散、位错、热处理……学完一堆名词，脑子里却是散沙，不知道它们怎么咬合。

这本书用一根线把散沙穿起来——**一静一动**：

- **静（任脉）**：平衡热力学 + 晶体结构 —— 回答「平衡态是什么样」
- **动（督脉）**：动力学 + 缺陷运动 —— 回答「怎么到达、为什么到不了」

每个概念都能问：它是静（平衡）还是动（过程）？它和对面那条脉的哪个概念对仗？一旦这条线在脑子里立起来，材料基础就从「背名词」变成「看一张网」。

**目标读者**：跨专业入门者（物理 / 化学 / 机械转材料），以及想要一条逻辑主线的材料专业学生。

---

## 全书结构

### ☯ 任脉 · 静（平衡与结构）
| 章 | 主题 | 配套代码 |
|---|---|---|
| Ch1 | 原子结构与电子排布 | `atomic_structure.py` |
| Ch2 | 原子键合与晶体结构 | `crystal_structure.py` |
| Ch3 | 晶体缺陷的几何 | `crystal_defects.py` |
| Ch4 | 微观组织：从缺陷到组织 | `microstructure.py` |
| Ch5 | 热力学：材料为什么变 | `thermodynamics.py` |
| Ch6 | 相图：平衡的地图 | `phase_diagram.py` |
| Ch7 | CALPHAD 与计算热力学 | `calphad.py` |

### ☯ 督脉 · 动（过程与演化）
| 章 | 主题 | 配套代码 |
|---|---|---|
| Ch8 | 扩散：原子怎么搬家 | `diffusion.py` |
| Ch9 | 相变动力学：形核与长大 | `phase_kinetics.py` |
| Ch10 | 缺陷的运动：位错与塑性 | `dislocation_motion.py` |
| Ch11 | 热处理：静与动的博弈 ★全书高潮 | `heat_treatment.py` |
| Ch12 | 相场与计算动力学 | `phase_field.py` |

### ☯ 任督交汇 · 性能与失效
| 章 | 主题 | 配套代码 |
|---|---|---|
| Ch13 | 力学性能与强化 + 有限元(FEM) | `mechanical_fem.py` |
| Ch14 | 电·磁·热性能 + DFT/MD/MLIP | `electronic_properties.py` |
| Ch15 | 失效与寿命 | `failure_life.py` |

---

## 贯穿全书的四条线

1. **主轴：一静一动** —— 四组静动对仗全部闭合
   - Ch3 缺陷几何 ↔ Ch10 缺陷运动（同一位错，静看几何、动看运动）
   - Ch5 热力学 ↔ Ch9 相变动力学（该不该变 vs 变多快）
   - Ch6/Ch7 相图·CALPHAD ↔ Ch12 相场（算平衡 vs 算演化）
   - Ch1 电子排布 ↔ Ch14 电磁热（定性 vs 定量，首尾呼应）

2. **主旋律：结构决定性能** —— 金刚石 vs 石墨（Ch1）→ 马氏体之谜（Ch11）→ 四大强化叠加（Ch13）

3. **暗线一：多尺度计算** —— 原子（DFT/MD/MLIP, Ch14）→ 微观（CALPHAD/相场, Ch7/Ch12）→ 宏观（FEM, Ch13）

4. **暗线二：怎么看见它** —— 表征手段跟着内容走，每章一节讲透（XRD/TEM/金相/DSC/EBSD/ARPES…），不是几句带过

---

## 全书的「高潮」：马氏体之谜（Ch11）

相图（静）说：钢慢冷该得珠光体。但淬火（快冷）躲过 TTT 鼻尖，碳来不及扩散，奥氏体被迫无扩散切变成马氏体——**相图里根本没有的相**。

这就是「动力学战胜热力学」：热力学说该去哪，动力学不让你去，逼出一条意想不到的路。全书所有伏笔（Ch2 铁的同素异构、Ch6 相图、Ch9 TTT 鼻尖、Ch10 强化）在这一章汇聚。

---

## 如何使用

### 阅读
- **完整阅读**：`book/打通材料基础任督二脉_v1.0.pdf`（123 页）
- **单章阅读**：`chapters/` 下每章独立 PDF
- **看大纲**：`book/封面与全书大纲.pdf`（太极三色分组 + 静动对仗图）

### 运行配套代码
每章配一个 Python 模块，**全部真实数据、纯 numpy/scipy、无需联网、可独立运行**：

```bash
pip install -r requirements.txt
cd code
python3 atomic_structure.py      # Ch1：氢谱线、电子排布、键合判据
python3 heat_treatment.py        # Ch11：马氏体之谜，冷速→组织→硬度
python3 phase_field.py           # Ch12：Cahn-Hilliard 调幅分解
# ... 每个模块对应一章
```

代码不是玩具——它们用真实材料数据演示每章的核心 Aha：
- `crystal_structure.py`：从晶体结构算金属密度，误差 < 0.3%
- `thermodynamics.py`：用熔化焓/熵算出冰的熔点 0.0°C
- `phase_field.py`：让均匀固溶体自发分离成两相（调幅分解）
- `mechanical_fem.py`：一维有限元，应力与解析解 F/A 完全吻合

详见 [`code/README.md`](code/README.md)。

### 自己编译 PDF
每章 Markdown 在 `chapters/`，用 pandoc + XeLaTeX 编译（需中文字体 Noto Serif CJK SC）：
```bash
pandoc chapters/打通材料基础_Ch1_原子结构与电子排布.md \
  -o ch1.pdf --pdf-engine=xelatex -H preamble.tex
```

---

## 每章的结构（7 件套）

1. **一句话本质** —— 三句话记住这一章
2. **教科书里你看到的** —— 标准概念
3. **但其实是什么意思** —— 直觉、图像、TikZ 图解
4. **真正的数学** —— 关键公式与推导
5. **一个让人 Aha 的例子** —— 真实数据 + 「怎么看见它」表征专节
6. **这玩意儿现在在哪** —— 工程应用 + 计算材料学现代视角
7. **让代码告诉你** —— 配套模块 + 思考题 + 延伸阅读

---

## 作者

Li Zhou · 2027

如有问题、勘误或建议，欢迎提 Issue。

## 许可

本作品采用 [CC BY-NC-SA 4.0](LICENSE) 许可：可自由分享、改编，需署名、非商业、相同方式共享。
