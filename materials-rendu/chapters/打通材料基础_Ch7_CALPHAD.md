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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 7}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries CALPHAD 与计算热力学}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 相图的现代语言 · 任脉收官}\\[0.5em]
{\color{primarycolor!60} CALPHAD \& Computational Thermodynamics}
\vspace{2em}
```

> "上一章我们手工画了二元相图。但真实合金有五六种元素——
> 手工根本画不出来。\textbf{怎么算一个含 Fe-Cr-Ni-Mo-C 的不锈钢的相图}?
> 答案是 CALPHAD:\textbf{给每个相一个自由能函数,用计算机算平衡}。
> 这是任脉'静'的终点——\textbf{从单个原子(Ch1)到多元相图,
> 材料的平衡态被彻底打通}。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的收官章}。Ch5 给了自由能 $G=H-TS$,Ch6 把它变成相图,
\textbf{CALPHAD 把这一切工程化、计算化、可外推到多元}。

\textbf{CALPHAD = CALculation of PHAse Diagrams}。\textbf{它是现代材料热力学的标准工具},
也是\textbf{ICME(集成计算材料工程)的热力学引擎}。\textbf{学完这章,任脉"静"全线贯通:
原子 → 晶体 → 缺陷 → 组织 → 热力学 → 相图 → CALPHAD}。\textbf{下一章进督脉"动"}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{CALPHAD 的核心三步}:\textbf{(1) 给每个相一个 Gibbs 自由能函数 $G(x,T)$};
\textbf{(2) 用实验数据 + 第一性原理数据拟合函数里的参数};\textbf{(3) 用能量最小化/公切线
计算相图——而且能从二元外推到多元}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. CALPHAD 是"参数化的热力学"}——\textbf{每个相的 $G(x,T)$ 写成带可调参数的函数(Redlich-Kister)}。

\textbf{2. 参数靠"优化"得到}——\textbf{拟合实验相图、热化学数据、DFT 数据,让计算匹配现实}。

\textbf{3. 最强大处是"多元外推"}——\textbf{用二元参数算出五六元真实合金的相图(手工绝不可能)}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{Redlich-Kister 多项式加几项参数,就能拟合任意复杂的自由能曲线};
\textbf{从带噪声的实验数据,最小二乘能反推出相互作用参数(误差几 \%)};
\textbf{Muggianu 几何模型用三个二元参数外推三元——这就是 CALPHAD 能算多元相图的秘密}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{CALPHAD 方法的历史}

\begin{itemize}
\item \textbf{1908}:van Laar 用自由能曲线推相图(思想萌芽)
\item \textbf{1970s}:Kaufman \& Bernstein 系统化,\textbf{CALPHAD 方法成型}
\item \textbf{1980s-90s}:Thermo-Calc、SGTE 数据库建立
\item \textbf{今天}:多元数据库覆盖钢、铝、镍、钛合金;ICME 的核心引擎
\end{itemize}

\subsection{CALPHAD 的基本要素}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{要素} & \textbf{作用} \\
\hline
端元自由能 & 纯组元各相的 $G$(SGTE 数据库提供)\\
理想混合熵 & $RT[x\ln x + \ldots]$ \\
过剩自由能 & Redlich-Kister 多项式(可调参数 $L_v$)\\
子格模型 & 描述有序相、化合物、间隙相 \\
参数优化 & 拟合实验 + DFT 数据 \\
平衡计算 & 最小化总 $G$ / 公切线 \\
\hline
\end{longtable}

\subsection{主流软件与数据库}

\begin{itemize}
\item \textbf{Thermo-Calc}(瑞典):工业标准,功能最全
\item \textbf{Pandat}(美国):自动相图计算
\item \textbf{FactSage}:冶金/陶瓷强
\item \textbf{OpenCALPHAD / pycalphad}:开源,可编程
\item \textbf{数据库}:TDB 文件格式;SGTE 纯元素数据;各类商业评估数据库
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{Redlich-Kister 多项式为什么这么设计}(对称/非对称项的物理)
\item \textbf{参数优化到底在优化什么}(同时拟合多种异质数据的艺术)
\item \textbf{多元外推为什么可行}(几何模型 Muggianu/Kohler/Toop)
\item \textbf{CALPHAD 的现代前沿}(贝叶斯不确定度、机器学习、第一性原理融合)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{把自由能"参数化"}

\textbf{Ch5 我们用规则溶液 $\Omega x(1-x)$ 描述过剩能——但这太简单,拟合不了真实合金}。
\textbf{CALPHAD 用更灵活的 Redlich-Kister 多项式}:
$$G_{\text{xs}} = x(1-x)\sum_{v=0}^{n} L_v (1-2x)^v$$

\begin{itemize}
\item \textbf{$L_0$}:对称项(就是规则溶液的 $\Omega$)
\item \textbf{$L_1$}:一阶非对称项(让曲线偏向一边)
\item \textbf{$L_2, L_3\ldots$}:更高阶,拟合更复杂的形状
\end{itemize}

\textbf{每个 $L_v$ 还可以是温度的函数 $L_v = a_v + b_v T$}。\textbf{加足够多项,
能拟合任意复杂的实验自由能曲线}——\textbf{这就是 CALPHAD 灵活性的来源}。

\subsection{参数从哪来:优化}

\textbf{CALPHAD 工作者的核心日常,是"优化参数"}。\textbf{目标:让计算的相图/热化学量,
匹配所有实验和理论数据}。

\textbf{拟合的数据种类}(异质数据融合):
\begin{itemize}
\item \textbf{相图数据}:实验测的相界温度、共晶点、固溶度
\item \textbf{热化学数据}:量热测的混合焓、活度(Ch5 的 DSC)
\item \textbf{第一性原理数据}:DFT 算的形成能、端元能量
\end{itemize}

\textbf{优化方法}:\textbf{最小化"计算值与实验值的加权平方差"}(最小二乘的推广)。
\textbf{这是个反问题——已知相图,反推自由能参数}。\textbf{几十个参数同时优化,是门手艺}。

\subsection{子格模型:描述化合物和有序相}

\textbf{溶液模型(Redlich-Kister)适合无序固溶体,但化合物(如 Fe$_3$C)、
有序相(如 Ni$_3$Al)需要"子格模型"}。

\textbf{思想}:\textbf{把晶体分成多个"亚点阵",每个亚点阵上原子的占据有自己的规则}。
\textbf{例如 (A,B)$_1$(A,B)$_3$ 描述一个有两种晶位的化合物}。\textbf{这是 CALPHAD 描述
复杂相的关键工具}——\textbf{从间隙固溶体(碳在铁中)到金属间化合物,都用子格模型}。

\subsection{多元外推:CALPHAD 最强大的地方}

\textbf{这是 CALPHAD 真正的威力}。\textbf{真实合金有五六种元素,不可能测全多元相图
(成分组合是天文数字)}。\textbf{CALPHAD 的解法}:

\begin{enumerate}
\item \textbf{先评估好所有的二元体系}(每个二元的 $G(x,T)$ 参数)
\item \textbf{用"几何模型"(Muggianu/Kohler/Toop)从二元外推到三元、多元}
\item \textbf{加少量三元修正参数(如果有数据)}
\end{enumerate}

\textbf{结果}:\textbf{用 $\binom{n}{2}$ 个二元数据库,算出 $n$ 元合金的相图}。
\textbf{一个含 10 种元素的高温合金,只需 45 个二元 + 少量三元评估,就能算相图}——
\textbf{这是手工方法做梦都做不到的}。

\section{4. 真正的数学}

\subsection{溶液相的完整自由能}

CALPHAD 中一个溶液相的摩尔 Gibbs 自由能:
$$G_m = \underbrace{\sum_i x_i\, {}^0G_i}_{\text{端元参考}} + \underbrace{RT\sum_i x_i\ln x_i}_{\text{理想混合}} + \underbrace{{}^{\text{xs}}G_m}_{\text{过剩}}$$

其中过剩项用 Redlich-Kister:
$${}^{\text{xs}}G_m = \sum_{i<j} x_i x_j \sum_{v} {}^v L_{ij}(x_i - x_j)^v$$

\textbf{${}^0G_i$ 来自 SGTE 纯元素数据库,${}^vL_{ij}$ 是待优化的相互作用参数}。

\subsection{子格模型的自由能}

对 $(A,B)$ 两亚点阵模型,自由能含\textbf{端元、组态熵、过剩}三部分:
$$G_m = \sum_{I,J} y_I' y_J'' \, G_{I:J} + RT\sum_s a_s \sum_i y_i^{(s)}\ln y_i^{(s)} + {}^{\text{xs}}G_m$$

\textbf{$y_i^{(s)}$ 是亚点阵 $s$ 上组元 $i$ 的占据分数}。\textbf{这个框架统一描述了
固溶体、化合物、有序相、间隙相}——\textbf{CALPHAD 的"万能模型"}。

\subsection{平衡计算:全局能量最小化}

\textbf{给定整体成分和温度,平衡态 = 让系统总 Gibbs 自由能最小的相组合}:
$$\min \sum_\phi f_\phi G_m^\phi \quad \text{s.t.} \quad \text{质量守恒}$$

\textbf{这是带约束的全局优化}——\textbf{Thermo-Calc 的核心算法(如 Lukas 的方法)}。
\textbf{对两相,等价于公切线(Ch5);对多相多元,是高维凸优化}。

\subsection{Muggianu 几何外推}

三元过剩能从三个二元外推:
$${}^{\text{xs}}G_{123} = \sum_{i<j} \frac{4 x_i x_j}{(1+x_i-x_j)(1+x_j-x_i)} \cdot [\text{二元} ij \text{在投影点的值}]$$

\textbf{核心思想}:\textbf{在三元成分点,沿特定几何路径投影到三个二元边,加权求和}。
\textbf{这让二元数据库"组装"成多元相图}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:几个参数拟合任意自由能曲线}

运行配套模块 \texttt{calphad.py}:

\begin{verbatim}
Redlich-Kister: G_xs = x(1-x)·Σ L_v·(1-2x)^v
x=0.3, 仅 L0(规则溶液)  : G_xs = 2100.0 J/mol
x=0.3, L0+L1(非对称)   : G_xs = 2352.0 J/mol
x=0.3, L0+L1+L2        : G_xs = 2284.8 J/mol
\end{verbatim}

\textbf{Aha}:\textbf{规则溶液(Ch5)只有一个对称参数,拟合不了真实合金的不对称自由能}。
\textbf{Redlich-Kister 加 $L_1$、$L_2$ 项,就能逐步逼近任意复杂的曲线形状}——
\textbf{像泰勒展开一样,加更多项,拟合越精确}。\textbf{这就是 CALPHAD 灵活性的数学根源}。

\subsection{从实验数据反推参数}

运行参数优化:

\begin{verbatim}
从(带噪声的)实验数据,最小二乘拟合:
真实值: L0=12000, L1=3000
拟合值: L0=11769, L1=3267
误差:   L0 1.9%, L1 8.9%
\end{verbatim}

\textbf{Aha}:\textbf{即使实验数据有噪声,最小二乘也能反推出相互作用参数(误差几 \%)}。
\textbf{这正是 CALPHAD 工作者每天做的事——给定实验相图/热化学数据,优化出自由能参数}。
\textbf{真实情况更复杂:同时拟合相图 + 焓 + 活度 + DFT,几十个参数联合优化}——
\textbf{这是一门科学,也是一门手艺}。

\subsection{多元外推:CALPHAD 的魔法}

运行 Muggianu 三元外推:

\begin{verbatim}
用三个二元参数(L12,L13,L23)外推三元过剩能:
成分           (x1,x2,x3)        G_xs(J/mol)
等比 1:1:1     (0.33,0.33,0.33)     1000.0
富组元1        (0.60,0.20,0.20)      680.0
1-2边二元      (0.50,0.50,0.00)     3000.0
\end{verbatim}

\textbf{Aha}:\textbf{只用三个二元的相互作用参数,就外推出整个三元体系的过剩自由能}——
\textbf{进而算出三元相图}。\textbf{推广开:用所有二元 + 少量三元评估,
就能算五六元真实合金的相图}。\textbf{这就是为什么 CALPHAD 能处理工业合金,而手工相图不能}。
\textbf{一个不锈钢(Fe-Cr-Ni-Mo-Mn-C...)的相图,就是这么算出来的}。

\subsection{怎么看见它:CALPHAD 的"验证"}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{CALPHAD 算出的相图,要靠实验"验证"——
最有力的验证是关键实验点 + 微观组织对照}。
\end{bluebox}

\textbf{CALPHAD 不是闭门造车,它的可靠性靠多重数据交叉验证}:
\begin{itemize}
\item \textbf{相变温度}:DSC/热分析(Ch5/Ch6)测的相界,对照计算
\item \textbf{相组成}:SEM-EDS / EPMA 测实际样品中各相的成分,对照计算的 tie-line
\item \textbf{相比例}:定量金相(Ch4)测各相体积分数,对照杠杆定律计算
\item \textbf{晶体结构}:XRD(Ch2)确认计算预测的相确实存在
\end{itemize}

\textbf{现代的"逆向"验证}:\textbf{用第一性原理(DFT)算端元和化合物的形成能,
作为 CALPHAD 优化的输入或检验}——\textbf{减少对实验的依赖}。

\textbf{能做什么}:算多元相图、相分数 vs 温度、凝固路径(Scheil 模型)、
驱动力(用于相变动力学 Ch8-9)、热力学性质。\textbf{局限}:\textbf{参数质量决定结果质量
(garbage in garbage out)};\textbf{外推到数据稀少区不可靠};\textbf{只给平衡态,
不给动力学(那是督脉)}。

\textbf{现代前沿(你的领域)}:\textbf{贝叶斯 CALPHAD 给相图配"误差棒"(不确定度量化);
机器学习势加速生成训练数据;第一性原理 + CALPHAD 融合,从头预测相图}——
\textbf{这是计算热力学正在发生的革命}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{合金设计}:算相图选成分,预测析出相、避开脆性相
\item \textbf{凝固模拟}:Scheil 模型算铸造偏析
\item \textbf{热处理设计}:算不同温度的平衡相,指导工艺(Ch11)
\item \textbf{新材料开发}:高熵合金、高温合金的相稳定性预测
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{ICME 引擎}:CALPHAD 是"成分-工艺-组织-性能"链条的热力学核心
\item \textbf{相场耦合(Ch12)}:CALPHAD 提供自由能 → 相场算组织演化——\textbf{静(相图)驱动动(演化)}
\item \textbf{高通量筛选}:扫描成千上万成分,预测稳定相,加速材料发现
\item \textbf{贝叶斯 + ML CALPHAD}:不确定度量化 + 机器学习加速——\textbf{当代前沿}
\end{itemize}

\begin{bluebox}
\textbf{CALPHAD 是连接"静"与"动"的枢纽}:\textbf{它给出平衡态(静)的完整描述,
但它的输出(自由能、驱动力)正是相变动力学(督脉 Ch8-9)和相场模拟(Ch12)的输入}。
\textbf{你做的相图相关计算,正是这个枢纽的工作}——\textbf{CALPHAD 算"该去哪",
动力学算"怎么去",合起来才是完整的材料演化}。\textbf{这正是全书"一静一动"的交汇点}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{你用的不锈钢}:成分是 CALPHAD 算过相图、避开脆性 $\sigma$ 相设计的
\item \textbf{飞机发动机叶片}:镍基高温合金的 $\gamma/\gamma'$ 组织靠 CALPHAD 设计
\item \textbf{无铅焊料}:Sn-Ag-Cu 共晶成分靠 CALPHAD 优化
\item \textbf{3D 打印合金}:快速凝固的相选择靠 CALPHAD + 动力学预测
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:calphad.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{redlich\_kister} & Redlich-Kister 过剩自由能多项式 \\
\texttt{total\_gibbs} & 溶液相完整自由能(端元+理想+过剩)\\
\texttt{sublattice\_two} & 两亚点阵模型(化合物/有序相)\\
\texttt{least\_squares\_demo} & 从实验数据拟合 RK 参数 \\
\texttt{common\_tangent\_two\_phase} & 公切线算相平衡 \\
\texttt{muggianu\_extrapolation} & 二元 → 三元几何外推 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 calphad.py}——\textbf{纯 numpy。真实 CALPHAD 用 pycalphad/Thermo-Calc}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(Redlich-Kister)} 为什么 $L_1$ 项乘的是 $(1-2x)$ 而不是 $x$?
($x=0.5$ 时 $(1-2x)=0$ 有什么意义?提示:对称性)

\item \textbf{(参数优化)} 用 \texttt{least\_squares\_demo} 的思路,如果实验数据噪声更大,
拟合误差会怎样?CALPHAD 如何应对(提示:更多数据 + 加权)?

\item \textbf{(子格)} 碳在 $\gamma$-Fe(FCC)中是间隙固溶。
怎么用子格模型 (Fe)$_1$(C,Va)$_1$ 描述?(Va = 空位)

\item \textbf{(多元外推)} 为什么 CALPHAD 能用二元数据算多元相图,
而手工方法不能?几何外推的代价是什么(精度)?

\item \textbf{(现代前沿)} 贝叶斯 CALPHAD 给相图配"误差棒"有什么实际价值?
(提示:实验设计、风险评估、告诉你"哪里数据不够")
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Lukas, Fries \& Sundman, \textit{Computational Thermodynamics: The Calphad Method}
\item \textbf{全面指南}:Saunders \& Miodownik, \textit{CALPHAD: A Comprehensive Guide}
\item \textbf{开源工具}:pycalphad(Python,可编程学习 CALPHAD)
\item \textbf{期刊}:\textit{CALPHAD} 期刊;\textit{Journal of Phase Equilibria and Diffusion}
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲 TDB 文件的具体语法}——pycalphad/Thermo-Calc 文档
\item \textbf{没讲优化算法的细节}(Marquardt、贝叶斯 MCMC)——专业文献
\item \textbf{没讲动力学数据库(DICTRA)}——那属于督脉(扩散 Ch8)
\item \textbf{没讲第一性原理的具体方法}——Ch14 的 DFT 部分
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:CALPHAD = \textbf{参数化的热力学}。\textbf{三步}:给每相一个 $G(x,T)$ 函数(Redlich-Kister 多项式 + 子格模型)→ 拟合实验 + DFT 数据优化参数 → 能量最小化算相图。\textbf{核心 Aha:几个 RK 参数拟合任意自由能曲线;从噪声数据反推参数;Muggianu 用二元外推多元}——\textbf{这是 CALPHAD 能算五六元真实合金相图的秘密}。\textbf{怎么看见它:用 DSC/EPMA/金相/XRD 多重交叉验证计算相图}。\textbf{CALPHAD 是连接静与动的枢纽}:它给平衡态(静),其输出(自由能、驱动力)是相变动力学和相场(督脉)的输入。\textbf{现代前沿:贝叶斯不确定度 + 机器学习 + 第一性原理融合}。\textbf{至此任脉"静"全线贯通——从原子(Ch1)到多元相图(Ch7),材料的平衡态彻底打通}。\textbf{下一章进督脉"动":材料怎么从一个平衡态走向另一个——扩散}。
\end{bluebox}

\begin{flushright}
\textit{第 7 章 · CALPHAD 与计算热力学 · 任脉收官 · 完}
\end{flushright}
