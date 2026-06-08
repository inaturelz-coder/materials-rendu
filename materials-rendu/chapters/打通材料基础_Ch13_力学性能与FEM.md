---
title: ""
documentclass: book
geometry: a4paper, margin=2.3cm, includefoot
fontsize: 11pt
CJKmainfont: "Noto Serif CJK SC"
numbersections: false
---

```{=latex}
\thispagestyle{empty}
\vspace*{2cm}
\begin{flushright}
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 13}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 力学性能与强化}\\[0.2em]
{\color{mergecolor}\Large\bfseries + 有限元(FEM)}\\[0.3em]
{\color{mergecolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{mergecolor} 任督交汇 · 结构与过程汇聚成性能}\\[0.5em]
{\color{primarycolor!60} Mechanical Properties \& Finite Element Method}
\vspace{2em}
```

> "前面十二章,我们从原子讲到相场——但所有这些,最终是为了回答工程师
> 最关心的问题:\textbf{这材料能承受多大的力?会不会断?变形多少?}
> 强度从哪来?是 Ch3 的缺陷、Ch10 的位错、Ch11 的热处理共同决定的。
> 而要算一个真实零件(不是理想试样)在复杂载荷下的应力——\textbf{需要有限元}。
> 任脉与督脉,在'性能'这里交汇。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任督交汇的第一章}。\textbf{任脉(静,结构)和督脉(动,过程)在这里汇聚成"性能"}。

\textbf{材料的强度,是前面所有章节的总和}:\textbf{Ch3 缺陷、Ch4 组织、Ch10 位错、Ch11 热处理——
四大强化机制在此汇聚成一个屈服强度的公式}。\textbf{而把"材料属性"接到"宏观构件"
(算真实零件的应力分布),需要有限元(FEM)}——\textbf{这是全书多尺度计算暗线的"宏观"一环}
(原子 DFT → 微观相场 → 宏观 FEM)。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{力学性能 = 材料抵抗变形和断裂的能力}。\textbf{它由微观结构决定(前面所有章节),
可以用四大强化机制定量叠加}。\textbf{而真实构件的应力分布,用有限元(FEM)计算}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 应力-应变曲线包含一切}:弹性模量(刚度)、屈服强度、抗拉强度、延展性、韧性(曲线下面积)。

\textbf{2. 四大强化机制可叠加}:\textbf{细晶 + 固溶 + 加工硬化 + 析出}——汇聚 Ch3/Ch4/Ch10/Ch11。

\textbf{3. 有限元 = 离散 + 组装 + 求解}:把构件切成小单元,组装刚度矩阵,解出应力位移。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{强度与延展性是一对矛盾("香蕉曲线"),退火钢软而韧,马氏体强而脆};
\textbf{四大强化机制定量叠加成屈服强度};\textbf{有限元算出的杆件应力与解析解 $F/A$ 完全吻合};
\textbf{圆孔边应力集中 3 倍(Kt=3),这就是失效从孔、缺口、裂纹开始的原因}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{力学性能指标}

\begin{longtable}{|l|p{0.58\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{指标} & \textbf{含义} \\
\hline
弹性模量 $E$ & 刚度,抵抗弹性变形(原子键合强度,Ch1)\\
屈服强度 $\sigma_y$ & 开始永久变形的应力(位错开动,Ch10)\\
抗拉强度 UTS & 能承受的最大应力 \\
延展性 & 断裂前的塑性变形量(延伸率)\\
韧性 & 断裂吸收的总能量(应力-应变曲线下面积)\\
硬度 & 抵抗局部塑性变形(与强度相关)\\
\hline
\end{longtable}

\subsection{四大强化机制}

\begin{itemize}
\item \textbf{细晶强化}(Hall-Petch,Ch4):晶界阻碍位错——\textbf{唯一同时增强增韧}
\item \textbf{固溶强化}(Ch3):溶质原子畸变晶格,钉扎位错
\item \textbf{加工硬化}(Ch10):位错缠结
\item \textbf{析出/弥散强化}(Ch11):第二相阻碍位错(Orowan 机制)
\end{itemize}

\subsection{有限元方法(FEM)}

\begin{itemize}
\item \textbf{离散}:把连续构件分成有限个"单元"
\item \textbf{单元刚度}:每个单元的力-位移关系
\item \textbf{组装}:拼成全局刚度矩阵 $\mathbf{K}$
\item \textbf{求解}:$\mathbf{K}\mathbf{u} = \mathbf{F}$,解出位移,再算应力
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么强度和韧性是矛盾的}(强化机制阻碍位错 = 降低塑性)
\item \textbf{四大强化机制如何定量叠加}(合金设计的工具箱)
\item \textbf{有限元到底在算什么}(刚度矩阵组装的物理)
\item \textbf{为什么裂纹总从孔、缺口、划痕开始}(应力集中)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{应力-应变曲线:材料的"身份证"}

\textbf{一条拉伸曲线,读出材料的全部力学性格}:
\begin{itemize}
\item \textbf{弹性段(直线)}:斜率 = 弹性模量 $E$(刚度)。\textbf{源于原子键合(Ch1)——键越强 $E$ 越大}
\item \textbf{屈服点}:位错开始大量运动(Ch10),进入永久变形
\item \textbf{塑性段(加工硬化)}:应力继续上升(位错增殖,Ch10),到 UTS
\item \textbf{颈缩与断裂}:变形集中,最终失效
\item \textbf{曲线下面积 = 韧性}:断裂吸收的能量——\textbf{既要强(高)又要韧(宽)}
\end{itemize}

\textbf{刚度 vs 强度 vs 韧性是不同的概念}:\textbf{刚度是"难不难弹性变形"(E),
强度是"多大力才永久变形/断裂",韧性是"断裂前吸收多少能量"}。\textbf{钻石刚度极高但脆,
橡皮强度低但韧——别混淆}。

\subsection{四大强化:全书的汇聚}

\textbf{材料的屈服强度,是各种强化机制的叠加}:
$$\sigma_y = \sigma_0 + \underbrace{\frac{k_y}{\sqrt{d}}}_{\text{细晶 Ch4}} + \underbrace{k_s c^{2/3}}_{\text{固溶 Ch3}} + \underbrace{\alpha Gb\sqrt{\rho}}_{\text{加工硬化 Ch10}} + \underbrace{\frac{Gb}{\lambda}}_{\text{析出 Ch11}}$$

\textbf{每一项都对应前面一章}:\textbf{细晶(Ch4 组织)、固溶(Ch3 点缺陷)、
加工硬化(Ch10 位错)、析出(Ch11 第二相)}。\textbf{它们的共同本质——都在"阻碍位错运动"(Ch10)}。

\begin{bluebox}
\textbf{这就是"任督交汇"的字面意义}:\textbf{前面讲的所有结构(静)和过程(动),
在"强度"这个公式里全部汇聚}。\textbf{合金设计 = 调配这四项,凑出想要的强度}——
\textbf{而代价往往是延展性下降}。
\end{bluebox}

\subsection{强韧权衡:鱼与熊掌}

\textbf{为什么强度和韧性是矛盾的}?——\textbf{因为强化机制都在"阻碍位错运动",
而塑性恰恰需要位错运动}。\textbf{阻碍越强 → 强度越高 → 但位错越难动 → 越脆}。

\textbf{这就是材料界著名的"香蕉曲线"(strength-ductility banana)}:\textbf{强度上去,延展性下来}。
\textbf{唯一的例外是细晶强化(Ch4)——它既增强又增韧}。\textbf{现代材料研究的圣杯,
就是突破这条香蕉曲线(如 TRIP/TWIP 钢、纳米孪晶)}。

\subsection{有限元:把材料接到构件}

\textbf{材料属性(E、$\sigma_y$)是"点"的性质}。\textbf{但真实零件有复杂形状、复杂载荷——
应力分布极不均匀}。\textbf{怎么算}?——\textbf{有限元}。

\textbf{核心思想三步}:
\begin{enumerate}
\item \textbf{离散}:把构件切成许多小单元(三角形、四面体...)
\item \textbf{组装}:每个单元有"刚度"(力-位移关系),拼成全局刚度矩阵 $\mathbf{K}$
\item \textbf{求解}:解线性方程组 $\mathbf{K}\mathbf{u} = \mathbf{F}$,得到每个节点的位移,再反算应力
\end{enumerate}

\textbf{FEM 是工程力学计算的通用工具}:\textbf{从桥梁、飞机、芯片到人工关节,
应力分析都靠它}。\textbf{它是多尺度计算的"宏观"一环——把材料属性放大到工程构件}。

\section{4. 真正的数学}

\subsection{韧性 = 曲线下面积}

$$U_T = \int_0^{\varepsilon_f}\sigma\,\mathrm{d}\varepsilon$$

\textbf{断裂吸收的总能量}。\textbf{高强度(高 $\sigma$)+ 高延展性(大 $\varepsilon_f$)= 高韧性——但两者通常矛盾}。

\subsection{有限元的单元刚度}

\textbf{一维杆单元},刚度 $k = \dfrac{EA}{l_e}$,力-位移关系 $\mathbf{k}_e\mathbf{u}_e = \mathbf{f}_e$:
$$\frac{EA}{l_e}\begin{pmatrix}1 & -1\\-1 & 1\end{pmatrix}\begin{pmatrix}u_1\\u_2\end{pmatrix} = \begin{pmatrix}f_1\\f_2\end{pmatrix}$$

\textbf{组装所有单元 → 全局 $\mathbf{K}\mathbf{u}=\mathbf{F}$ → 施加边界条件 → 求解}。
\textbf{单元应力 $\sigma_e = E\dfrac{u_{e+1}-u_e}{l_e}$}。

\subsection{应力集中系数}

\textbf{无限大板中圆孔},孔边最大应力:
$$\sigma_{\max} = K_t\,\sigma_{\text{nominal}}, \quad K_t = 3 \text{(圆孔)}$$

\textbf{椭圆孔} $K_t = 1 + 2a/b$(长轴 $a$,短轴 $b$)——\textbf{越扁越尖,$K_t$ 越大;
裂纹尖端 $K_t\to\infty$}。\textbf{这是断裂力学(Ch15)的起点}。

\subsection{弹性模量的来源}

\textbf{$E$ 正比于原子键合的"刚度"}(Ch1 的势能曲线在平衡点的曲率)。\textbf{所以共价键材料
(金刚石)$E$ 极高,分子晶体(塑料)$E$ 低}——\textbf{力学性能的根扎在第一章的电子排布}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:四大强化机制汇聚}

运行配套模块 \texttt{mechanical\_fem.py}:

\begin{verbatim}
σ_0(晶格摩擦):        50 MPa
+ 细晶强化(Ch4):       7 MPa  ← Hall-Petch
+ 固溶强化(Ch3):      60 MPa  ← 置换原子
+ 加工硬化(Ch10):     18 MPa  ← 位错
+ 析出强化(Ch11):     25 MPa  ← 第二相
= 总屈服强度:        160 MPa
\end{verbatim}

\textbf{Aha}:\textbf{材料的强度,是前面四章强化机制的定量叠加}。\textbf{细晶(Ch4)、
固溶(Ch3)、加工硬化(Ch10)、析出(Ch11)——每一项对应一章,加起来就是屈服强度}。
\textbf{这就是"任督交汇"的字面体现}:\textbf{结构(静)和过程(动)在"强度"这个公式里全部汇聚}。
\textbf{合金设计师的工作,就是调配这四项凑出目标强度}。

\subsection{强韧权衡:香蕉曲线}

\begin{verbatim}
状态          强度(MPa)   延展性(%)
退火态        250         35
冷加工        500         15
淬火回火      900          8
淬火马氏体    1500          3
\end{verbatim}

\textbf{Aha}:\textbf{强度从 250 升到 1500 MPa,延展性从 35\% 跌到 3\%}。\textbf{这条
"强了就脆"的香蕉曲线,是材料设计的根本矛盾}。\textbf{原因:强化机制都在阻碍位错运动,
而塑性需要位错运动}。\textbf{现代材料研究的圣杯——同时突破强度和韧性(TRIP/TWIP 钢、
纳米孪晶铜)——就是想"掰弯"这条香蕉}。

\subsection{有限元:数值与解析的吻合}

\begin{verbatim}
拉伸杆:左端固定,右端受力10kN,钢E=200GPa,A=1cm²
节点位移(mm): [0. 0.1 0.2 0.3 0.4 0.5]
单元应力(MPa): [100. 100. 100. 100. 100.]
解析解应力 F/A = 100 MPa
\end{verbatim}

\textbf{Aha}:\textbf{有限元通过"离散→刚度矩阵组装→求解",算出杆件应力 100 MPa,
与解析解 $F/A$ 完全吻合}。\textbf{对均匀杆,这是"杀鸡用牛刀";但对复杂构件
(没有解析解的形状和载荷),FEM 是唯一通用方法}。\textbf{这就是为什么飞机、桥梁、芯片、
人工关节的应力分析全靠 FEM}——\textbf{它把材料属性放大到了工程尺度}。

\subsection{怎么看见它:力学试验与 DIC}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{力学性能靠"力学试验机"直接测;应力/应变分布靠数字图像相关(DIC)看}。
\end{bluebox}

\textbf{标准力学试验}:
\begin{itemize}
\item \textbf{万能试验机(拉伸/压缩)}:夹住试样拉到断,\textbf{记录力-位移 → 应力-应变曲线}——
读出 $E$、$\sigma_y$、UTS、延伸率、韧性
\item \textbf{硬度计}:压头压入,测压痕大小——\textbf{快速、近无损,与强度相关}
\item \textbf{冲击试验(Charpy)}:测冲击韧性(吸收能量)、韧脆转变温度
\item \textbf{数字图像相关(DIC)}:在试样表面喷散斑,\textbf{相机拍变形,算全场应变分布}——\textbf{看应力集中、颈缩、裂纹}
\end{itemize}

\textbf{FEM 的验证}:\textbf{FEM 算出的应变场,与 DIC 实测的应变场对照}——\textbf{一致才说明
模型(材料本构 + 边界条件)正确}。\textbf{能测什么}:全套力学性能、应变分布、裂纹萌生位置、
本构参数。\textbf{局限}:试样制备和对中影响结果;\textbf{DIC 只测表面};\textbf{FEM 精度依赖
网格、本构模型、参数(garbage in garbage out)}。

\textbf{现代视角}:\textbf{晶体塑性有限元(CPFEM)把 Ch10 的 Schmid 定律嵌入 FEM,
算多晶的非均匀变形;原位 + DIC + EBSD 联用,把宏观应力和微观组织对应起来}——
\textbf{多尺度力学的前沿}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{合金设计}:调配四大强化机制,达到目标强度-韧性
\item \textbf{结构设计}:FEM 算零件应力,避免应力集中,优化形状
\item \textbf{选材}:用 Ashby 材料选择图(强度-密度、模量-成本)
\item \textbf{安全评估}:FEM + 断裂力学评估关键部件寿命(Ch15)
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{有限元(FEM)}:工程力学的标准工具——\textbf{多尺度的宏观一环}
\item \textbf{晶体塑性 FEM(CPFEM)}:把位错塑性(Ch10)嵌入 FEM,算多晶变形
\item \textbf{多尺度耦合}:DFT(键合,Ch1/Ch14)→ 相场(组织,Ch12)→ FEM(构件)
\item \textbf{拓扑优化}:用 FEM 反向设计最优结构(3D 打印 + AI)
\end{itemize}

\begin{bluebox}
\textbf{多尺度计算暗线的"宏观"一环在此}:\textbf{原子尺度(DFT 算 $E$、键合,Ch1/Ch14)→
微观尺度(CALPHAD/相场算组织,Ch7/Ch12)→ 宏观尺度(FEM 算构件应力,本章)}。
\textbf{三个尺度贯穿全书}。\textbf{CPFEM 更是直接把 Ch10 的位错塑性接进 FEM——
微观与宏观在一个模型里打通}。\textbf{这是材料计算从"原子"到"飞机"的完整链条}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么手机边框要倒圆角}:避免应力集中(Kt 小),防止跌落开裂
\item \textbf{为什么飞机舷窗是圆的}:历史教训(彗星号方窗应力集中导致空难)
\item \textbf{为什么纸张沿折痕易撕}:折痕是应力集中 + 裂纹源
\item \textbf{为什么橡皮筋拉久会断}:反复变形 + 微裂纹扩展
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:mechanical\_fem.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{stress\_strain\_analysis} & 提取力学量(E/σy/UTS/韧性)\\
\texttt{material\_comparison} & 几种材料力学性能对比 \\
\texttt{strengthening\_mechanisms} & 四大强化机制叠加(汇聚前面)\\
\texttt{strength\_ductility\_tradeoff} & 强韧权衡香蕉曲线 \\
\texttt{fem\_1d\_bar} & 一维有限元(刚度矩阵组装求解)\\
\texttt{stress\_concentration\_hole} & 应力集中(Kt)\\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 mechanical\_fem.py}——\textbf{纯 numpy,含真实 FEM 内核。
工业用 ABAQUS/ANSYS/COMSOL}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(强化叠加)} 用 \texttt{strengthening\_mechanisms},如果要把屈服强度提到 300 MPa,
调哪个参数最有效?代价是什么?

\item \textbf{(强韧权衡)} 为什么细晶强化(Ch4)是唯一"既增强又增韧"的机制?
(提示:它细化的不只是强度,还有裂纹路径)

\item \textbf{(FEM)} 用 \texttt{fem\_1d\_bar},增加单元数,结果会更准吗?
对均匀杆为什么 1 个单元就够?什么情况需要很多单元?

\item \textbf{(应力集中)} 为什么椭圆孔比圆孔的 Kt 大?裂纹尖端 Kt 为什么趋于无穷?
(这是 Ch15 断裂力学的起点)

\item \textbf{(多尺度)} 弹性模量 $E$ 来自原子键合(Ch1)。
为什么说 FEM 是"多尺度的宏观一环"?它的输入从哪些尺度来?
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{力学行为}:Courtney, \textit{Mechanical Behavior of Materials}
\item \textbf{材料选择}:Ashby, \textit{Materials Selection in Mechanical Design}
\item \textbf{有限元}:Zienkiewicz, \textit{The Finite Element Method}
\item \textbf{晶体塑性}:Roters et al., \textit{Crystal Plasticity Finite Element Methods}(DAMASK)
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲二维/三维 FEM 的细节}(形函数、高斯积分)——FEM 专著
\item \textbf{没讲非线性 FEM}(大变形、塑性、接触)——进阶
\item \textbf{没讲复合材料力学}(各向异性、层合板)——专题
\item \textbf{没讲断裂力学的定量}(应力强度因子)——留给 Ch15
\end{itemize}

\begin{bluebox}
\textbf{本章小结(任督交汇)}:力学性能 = 材料抵抗变形和断裂的能力。\textbf{应力-应变曲线}读出刚度(E)、屈服、抗拉、延展性、韧性(曲线下面积)。\textbf{核心 Aha:四大强化机制(细晶 Ch4/固溶 Ch3/加工硬化 Ch10/析出 Ch11)定量叠加成屈服强度}——这是任督交汇的字面体现。\textbf{强韧权衡(香蕉曲线):强了就脆,因为强化机制都在阻碍位错运动}。\textbf{有限元 = 离散+组装+求解},把材料属性接到宏观构件(FEM 应力与解析解 $F/A$ 吻合)。\textbf{应力集中(圆孔 Kt=3)解释失效从孔/缺口开始}。\textbf{怎么看见它:力学试验机 + DIC + CPFEM}。\textbf{多尺度暗线的宏观一环:DFT(原子)→ 相场(微观)→ FEM(宏观)}。\textbf{下一章}:回到电子排布——\textbf{电·磁·热性能 + DFT/MD/MLIP}(首尾呼应 Ch1)。
\end{bluebox}

\begin{flushright}
\textit{第 13 章 · 力学性能与强化 + 有限元 · 完}
\end{flushright}
