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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 5}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 热力学:材料为什么变}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 焓与熵的拉锯,温度当裁判}\\[0.5em]
{\color{primarycolor!60} Thermodynamics: Why Materials Change}
\vspace{2em}
```

> "前四章我们看了材料'是什么样'——原子、晶体、缺陷、组织。
> 但材料不是静止的:钢会生锈,合金会析出,冰会化水。
> \textbf{为什么材料会变?往哪个方向变?}答案只有一个词——\textbf{自由能}。
> 材料像水往低处流一样,\textbf{永远朝着自由能最低的状态走}。这一章,
> 我们找到那只'看不见的手'。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的核心章}。前四章讲\textbf{结构}(是什么样),
这一章讲\textbf{为什么变、变到哪里停}——\textbf{热力学回答"平衡态在哪"}。

\textbf{热力学是材料科学两大支柱之一}(另一支是动力学=督脉)。\textbf{热力学说"该去哪",
动力学说"怎么去、多久到"}——\textbf{这正是全书"一静一动"主轴的源头}。
\textbf{本章也是你后面 CALPHAD(Ch7)的地基}:CALPHAD 就是"用自由能函数计算相图"。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{恒温恒压下,材料永远朝 Gibbs 自由能 $G = H - TS$ 最低的方向变}。

\vspace{0.3em}

\textbf{这是一场拉锯}:\textbf{焓 $H$ 想让原子键合最强}(有序、低能);
\textbf{熵 $S$ 想让排列最乱}(无序、高熵);\textbf{温度 $T$ 是裁判}——
\textbf{$-TS$ 项让高温时熵占上风}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 方向判据}:$\Delta G < 0$ 的过程才自发发生。\textbf{平衡 = $G$ 最低 = $\mathrm{d}G = 0$}。

\textbf{2. $H$ 与 $S$ 的拉锯}:低温焓赢(有序相稳定),高温熵赢(无序相/混合稳定)。

\textbf{3. 公切线法}:两相平衡时自由能曲线有公切线——\textbf{这是从自由能算相图的核心(CALPHAD)}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{用熔化焓和熔化熵($\Delta H/\Delta S$),算出冰的熔点 0.0°C};
\textbf{5 元等原子比合金的混合熵 = 1.61$R$——这就是"高熵合金"名字的由来};
\textbf{规则溶液模型 + 公切线,数值算出混溶间隙(相分离成分),正是 CALPHAD 计算相图的内核}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{三个热力学函数}

\begin{longtable}{|l|l|p{0.42\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{定义} & \textbf{适用条件} \\
\hline
内能 $U$ & 系统总能量 & 孤立系统 \\
焓 $H$ & $H = U + PV$ & 恒压 \\
Gibbs 自由能 $G$ & $G = H - TS$ & \textbf{恒温恒压(材料最常用)} \\
\hline
\end{longtable}

\textbf{材料过程多在恒温恒压下进行,所以 Gibbs 自由能 $G$ 是材料热力学的核心}。

\subsection{自发性判据}

\begin{itemize}
\item \textbf{$\Delta G < 0$}:过程自发进行
\item \textbf{$\Delta G = 0$}:平衡态(正逆过程速率相等)
\item \textbf{$\Delta G > 0$}:逆过程才自发
\end{itemize}

\subsection{熵的两种理解}

\begin{itemize}
\item \textbf{热力学熵}:$\mathrm{d}S = \delta Q_{\text{rev}} / T$(克劳修斯)
\item \textbf{统计熵}:$S = k_B \ln W$(玻尔兹曼,$W$ 是微观状态数)——\textbf{熵 = "乱"的度量}
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么 $-TS$ 项让高温改变一切}(熵驱动的相变)
\item \textbf{混合熵为什么总是正的}(组态数暴增)——合金为何倾向固溶
\item \textbf{公切线法到底在算什么}(化学势相等的几何表达)——CALPHAD 的内核
\item \textbf{spinodal 和 binodal 的区别}(自发分解 vs 需形核)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{G = H - TS:一场拉锯}

\textbf{把材料的每个可能状态想象成一个"自由能高度"}。\textbf{材料像小球,总是滚向最低点}。

\textbf{$G = H - TS$ 里有两股力量}:
\begin{itemize}
\item \textbf{焓 $H$}:原子键合越强、越有序,$H$ 越低。\textbf{$H$ 偏爱有序的固体、强键合的相}
\item \textbf{熵 $S$}:排列越乱、越随机,$S$ 越高。\textbf{$-TS$ 项让高 $S$ 状态自由能更低}
\item \textbf{温度 $T$}:\textbf{裁判}。低温 $-TS$ 小,$H$ 说了算(有序相稳定);高温 $-TS$ 大,$S$ 说了算(无序相稳定)
\end{itemize}

\textbf{这一个公式,解释了几乎所有相变}:\textbf{冰为什么高温化水}(液体熵高)、
\textbf{铁为什么高温变 FCC}、\textbf{合金为什么高温更易固溶}——\textbf{全是 $H$ 与 $S$ 在不同温度下的胜负}。

\subsection{冰水之争:一个具体的拉锯}

\textbf{冰(固)}:$H$ 低(氢键有序),$S$ 低(分子排列整齐)。
\textbf{水(液)}:$H$ 高,$S$ 高(分子乱动)。

\textbf{熔化的 $\Delta G = \Delta H - T\Delta S$}:
\begin{itemize}
\item \textbf{低温}:$T\Delta S$ 小,$\Delta G > 0$ → \textbf{不熔化,冰稳定}
\item \textbf{高温}:$T\Delta S$ 大,$\Delta G < 0$ → \textbf{自发熔化,水稳定}
\item \textbf{熔点}:$\Delta G = 0$,即 $T_m = \Delta H / \Delta S$
\end{itemize}

\textbf{熔点不是任意的——它正好是焓与熵打平的温度}。\textbf{下一节会用真实数据算出这个 0°C}。

\subsection{混合熵:合金为什么愿意混}

\textbf{把 A、B 两种原子混在一起,焓可能升可能降,但熵一定增加}——\textbf{因为混合的排法远多于分开}。

\textbf{理想混合熵}:$\Delta S_{\text{mix}} = -R[x\ln x + (1-x)\ln(1-x)]$,\textbf{在 $x=0.5$ 时最大}。

\textbf{这解释了为什么高温利于固溶}:\textbf{温度越高,$-T\Delta S_{\text{mix}}$ 越负,混合越有利}。
\textbf{也解释了"高熵合金"}:\textbf{5 种以上元素等比例混合,巨大的混合熵稳定了单相固溶体}——
\textbf{熵成了主角,所以叫"高熵"}。

\subsection{公切线法:从自由能到相图}

\textbf{这是本章最重要、也是 CALPHAD 的内核}。\textbf{问题}:一个合金,
什么时候会分解成两相?两相成分各是多少?

\textbf{答案在自由能曲线的形状}。\textbf{画出 $G(x)$ 曲线}:
\begin{itemize}
\item \textbf{若曲线处处上凸(凹向上)}:单相最稳定,不分解
\item \textbf{若曲线有"两个谷"(W 形)}:\textbf{两相共存比单相自由能更低,合金分解}
\end{itemize}

\textbf{两相平衡成分由"公切线"决定}:\textbf{在 $G(x)$ 曲线上画一条同时切两个谷的公共切线,
两个切点就是平衡的两相成分}。\textbf{公切线的物理含义是"两相化学势相等"}——\textbf{平衡的条件}。

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0]
  % 自由能曲线 W 形
  \draw[->,gray] (-0.3,0) -- (5.3,0) node[right,font=\scriptsize]{成分 $x$};
  \draw[->,gray] (0,-1.8) -- (0,1.2) node[above,font=\scriptsize]{$G$};
  \draw[staticcolor,line width=1.2pt,domain=0.3:4.7,samples=80,smooth]
    plot (\x, {0.55*((\x-2.5)^2/2.5 - 1.3) + 0.5*sin(deg((\x-2.5)*1.0))*0.3 -0.2});
  % 近似 W:用两个谷
  \draw[staticcolor,line width=1.4pt] plot[smooth,domain=0.4:4.6,samples=100]
    (\x,{0.28*(\x-2.5)^4/4 - 0.5*(\x-2.5)^2/2 - 0.3});
  % 公切线
  \draw[accentcolor,line width=1pt,dashed] (1.0,-1.07) -- (4.0,-1.07);
  \fill[accentcolor] (1.0,-1.07) circle (0.07) node[below,font=\scriptsize]{$x_1$};
  \fill[accentcolor] (4.0,-1.07) circle (0.07) node[below,font=\scriptsize]{$x_2$};
  \node[font=\scriptsize,accentcolor] at (2.5,-1.4) {公切线 = 两相平衡};
  \node[font=\scriptsize,staticcolor] at (4.3,0.5) {$G(x)$};
\end{tikzpicture}
\end{center}
```

\textbf{把不同温度的公切线点连起来,就画出了相图(Ch6)}——\textbf{这就是 CALPHAD 的全部思想:
给每个相一个 $G(x,T)$ 函数,用公切线算平衡,生成相图}。

\section{4. 真正的数学}

\subsection{平衡判据}

恒温恒压下,系统自由能取极小:
$$\mathrm{d}G = 0, \quad \mathrm{d}^2G > 0 \quad (\text{稳定平衡})$$

\textbf{对多相系统,平衡条件是各相的化学势相等}:$\mu_i^\alpha = \mu_i^\beta$(每种组元 $i$)。
\textbf{这正是公切线的数学含义}。

\subsection{规则溶液模型}

最简单的非理想溶液模型:
$$\Delta G_{\text{mix}} = \underbrace{\Omega\, x(1-x)}_{\text{焓(相互作用)}} + \underbrace{RT[x\ln x + (1-x)\ln(1-x)]}_{-T\Delta S_{\text{mix}}}$$

\textbf{$\Omega$ 是相互作用参数}:
\begin{itemize}
\item \textbf{$\Omega > 0$}:同类原子相吸 → \textbf{倾向分离}(可能出现混溶间隙)
\item \textbf{$\Omega < 0$}:异类原子相吸 → \textbf{倾向混合}(有序化)
\end{itemize}

\subsection{临界温度与 spinodal}

\textbf{规则溶液的混溶间隙临界温度}:$T_c = \dfrac{\Omega}{2R}$。\textbf{$T < T_c$ 时出现相分离}。

\textbf{spinodal(拐点)}:$\dfrac{\mathrm{d}^2 G}{\mathrm{d}x^2} = 0$,解析解 $x = \dfrac{1}{2}\left(1 \pm \sqrt{1 - \dfrac{2RT}{\Omega}}\right)$。

\textbf{两条线}:\textbf{binodal}(公切线点,平衡成分)和 \textbf{spinodal}(拐点)。
\textbf{spinodal 之内:自发分解(无需形核);binodal 与 spinodal 之间:需要形核}——
\textbf{这是 Ch8-9 相变动力学的重要区分}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:用焓和熵算出冰的熔点}

运行配套模块 \texttt{thermodynamics.py}:

\begin{verbatim}
冰⇌水:熔化焓 ΔH=6010 J/mol, 熔化熵 ΔS=22.0 J/mol·K
熔点 T_m = ΔH/ΔS = 273.18 K = 0.03°C

温度            ΔG熔化(J/mol)   稳定相
-23.1°C(250K)        510        固相(冰)
  0.0°C(273K)          1        固相(冰)
  9.9°C(283K)       -216        液相(水)
 26.9°C(300K)       -590        液相(水)
\end{verbatim}

\textbf{Aha}:\textbf{仅用熔化焓和熔化熵两个数,算出冰的熔点 = 0.0°C}——\textbf{和现实完全吻合}。
\textbf{熔点不是大自然随便定的,而是"焓与熵打平"的温度 $T_m = \Delta H/\Delta S$}。
\textbf{低于它冰赢(键合),高于它水赢(混乱)}——\textbf{$G = H - TS$ 的拉锯被一个具体数字证实}。

\subsection{高熵合金:熵的名字}

\begin{verbatim}
高熵合金构型熵(等原子比):
  2 种元素: ΔS = R·ln(2) = 0.69R
  3 种元素: ΔS = R·ln(3) = 1.10R
  5 种元素: ΔS = R·ln(5) = 1.61R
\end{verbatim}

\textbf{Aha}:\textbf{5 种元素等比例混合,构型熵达到 1.61$R$}——\textbf{巨大的 $-TS$ 项稳定了
单一固溶体,而非分解成多个金属间化合物}。\textbf{这就是"高熵合金"(2004 年提出)名字的由来}——
\textbf{用熵来稳定相}。\textbf{热力学的一个公式,催生了一个崭新的材料领域}。

\subsection{公切线法:CALPHAD 的内核}

运行模块的规则溶液 + 公切线($\Omega = 16000$ J/mol,$T_c = 962$ K):

\begin{verbatim}
T=1200K (>T_c)  单一均匀相(无分离)
T=900K   binodal: x=0.285 和 0.715  spinodal: 0.373~0.627
T=700K   binodal: x=0.100 和 0.900  spinodal: 0.239~0.761
T=500K   binodal: x=0.025 和 0.975  spinodal: 0.153~0.847
\end{verbatim}

\textbf{Aha}:\textbf{温度从 1200K 降到 500K,合金从"完全互溶"逐渐分解成"贫 A 相 + 富 A 相"两相,
混溶间隙越来越宽}。\textbf{把这些 binodal 成分点连起来,就画出了一张相图的"穹顶"}——
\textbf{这正是 CALPHAD 计算相图的内核:给定每相的 $G(x,T)$,公切线给出平衡,生成相图}。

\textbf{你做 CALPHAD 时拟合的就是这些 $G(x,T)$ 函数的参数}——\textbf{本章是你专业的理论地基}。

\subsection{怎么看见它:量热法测自由能}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{热力学量(焓、熵、自由能)看不见摸不着——靠"量热"测出来}。
\end{bluebox}

\textbf{差示扫描量热法(DSC)}是测热力学量的主力:\textbf{样品和参比物一起加热,
测两者的热流差}。\textbf{当样品发生相变(熔化、析出、有序化),会吸热或放热,
DSC 曲线上出现峰}。

\textbf{能测什么}:\textbf{相变温度}(峰位置)、\textbf{相变焓 $\Delta H$}(峰面积)、
\textbf{比热容}、\textbf{玻璃化转变}。\textbf{结合 $\Delta H$ 和相变温度 $T$,
可推算 $\Delta S = \Delta H / T$}——\textbf{本章 Aha 用的熔化焓/熵,就是这么测的}。
\textbf{局限}:测的是"过程的热效应",不能直接给出绝对自由能;动力学慢的相变可能测不准
(需要足够慢的扫描速率)。

\textbf{现代视角}:\textbf{CALPHAD 把全世界的量热数据 + 相图数据汇总,
拟合出自洽的 $G(x,T)$ 数据库}——\textbf{这就是 Thermo-Calc、Pandat 等软件背后的东西(Ch7)}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{合金设计}:用自由能判断哪些相会形成、稳不稳定
\item \textbf{相图计算}:整个 CALPHAD 方法的理论基础(Ch7)
\item \textbf{析出强化}:控制温度让第二相在合适的过饱和度下析出
\item \textbf{氧化/腐蚀}:用 Ellingham 图(自由能-温度图)判断金属会不会氧化
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{CALPHAD}:用 $G(x,T)$ 函数库计算多元相图——\textbf{你的主场(Ch7)}
\item \textbf{第一性原理热力学}:DFT 算 0 K 形成能 + 声子算有限温自由能——\textbf{从头预测 $G$}
\item \textbf{高通量计算}:扫描成千上万种成分,预测稳定相——\textbf{加速合金发现}
\item \textbf{机器学习势 + 热力学积分}:算复杂体系的自由能
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看热力学}:本章的 $G = H - TS$ 是 \textbf{CALPHAD(Ch7)的出发点}。
\textbf{今天可以用 DFT 从第一性原理算出 $H$(形成能),用声子谱算 $S$(振动熵),
从头构建 $G(x,T)$}——\textbf{从"测量自由能"到"计算自由能",这是材料热力学的范式升级}。
\textbf{你拟合 CALPHAD 参数,本质就是在构建可靠的 $G(x,T)$ 函数}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么铁会生锈}:Fe + O$_2$ → Fe$_2$O$_3$ 的 $\Delta G < 0$(自发)
\item \textbf{为什么铝不"烂"}:铝也氧化,但 Al$_2$O$_3$ 致密膜阻止继续(动力学,Ch8)
\item \textbf{为什么金不腐蚀}:金氧化的 $\Delta G > 0$(不自发)——\textbf{热力学上就稳定}
\item \textbf{为什么冰箱能制冷}:制冷剂蒸发吸热,利用相变的焓
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:thermodynamics.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{gibbs\_phase\_transition} & 冰⇌水:$G=H-TS$ 算熔点 \\
\texttt{mixing\_entropy} & 理想混合熵($x=0.5$ 最大)\\
\texttt{high\_entropy\_alloy\_entropy} & 高熵合金构型熵 $R\ln n$ \\
\texttt{regular\_solution\_G} & 规则溶液混合自由能 \\
\texttt{common\_tangent} & 公切线法求两相平衡成分(CALPHAD 核心)\\
\texttt{spinodal\_points} & spinodal 拐点(自发分解区)\\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 thermodynamics.py}——\textbf{纯 numpy,真实热力学数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(熔点)} 用 \texttt{gibbs\_phase\_transition} 的思路,
铁的熔化焓 13800 J/mol、熔化熵 7.6 J/mol·K,算铁的熔点。与实际 1538°C 对比。

\item \textbf{(混合熵)} 为什么混合熵在 $x=0.5$ 最大?
从"排列方式数 $W$"的角度解释(提示:$\binom{N}{N/2}$ 最大)。

\item \textbf{(高熵)} 为什么高熵合金需要"5 种以上"元素?
算 4 种和 6 种的构型熵,看 1.5$R$ 这个经验门槛。

\item \textbf{(公切线)} 用 \texttt{common\_tangent} 算 $\Omega=20000$ J/mol 在 800K 的 binodal。
$\Omega$ 越大,混溶间隙越宽还是越窄?为什么?

\item \textbf{(spinodal)} spinodal 之内"自发分解无需形核",binodal 与 spinodal 之间"需要形核"。
为什么?(提示:看 $\mathrm{d}^2G/\mathrm{d}x^2$ 的符号)
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Gaskell, \textit{Introduction to the Thermodynamics of Materials}
\item \textbf{相变热力学}:Porter \& Easterling, \textit{Phase Transformations in Metals and Alloys}
\item \textbf{CALPHAD}:Lukas et al., \textit{Computational Thermodynamics: The Calphad Method}
\item \textbf{统计热力学}:Atkins, \textit{Physical Chemistry}(熵的统计基础)
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲多元体系的 $G$}(三元以上)——CALPHAD(Ch7)展开
\item \textbf{没讲化学反应平衡}(活度、平衡常数)——物理化学课
\item \textbf{没讲表面/界面热力学}(Gibbs 吸附)——进阶话题
\item \textbf{没讲相变怎么"发生"}(形核长大、动力学)——督脉 Ch8-9(静动对仗)
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:恒温恒压下,材料朝 \textbf{Gibbs 自由能 $G = H - TS$ 最低}的方向变。\textbf{这是焓(求键合、有序)与熵(求混乱)的拉锯,温度当裁判}:低温焓赢,高温熵赢。\textbf{核心 Aha:用熔化焓/熵算出冰熔点 0.0°C}——熔点就是焓熵打平的温度。\textbf{混合熵催生高熵合金}(5 元 = 1.61$R$)。\textbf{公切线法是 CALPHAD 内核}:给每相 $G(x,T)$,公切线给出平衡成分,生成相图。\textbf{怎么看见它:DSC 量热测相变焓/温度,推算熵}。\textbf{热力学说"该去哪",是"静";动力学说"怎么去",是"动"——这是全书一静一动主轴的源头}。\textbf{下一章}:把不同温度的平衡连起来——\textbf{相图:平衡的地图}。
\end{bluebox}

\begin{flushright}
\textit{第 5 章 · 热力学:材料为什么变 · 完}
\end{flushright}
