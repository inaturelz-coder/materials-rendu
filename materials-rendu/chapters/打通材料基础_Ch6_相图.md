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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 6}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 相图:平衡的地图}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 查相、查成分、查比例的导航图}\\[0.5em]
{\color{primarycolor!60} Phase Diagrams: The Map of Equilibrium}
\vspace{2em}
```

> "上一章我们有了自由能这只看不见的手。但每次都画自由能曲线太麻烦。
> \textbf{能不能做一张'地图',一眼查出任意成分、任意温度下材料是什么状态}?
> 能——\textbf{这就是相图}。它是材料科学最重要的工具,
> 一张图浓缩了无数次自由能计算。读懂相图,你就有了材料世界的导航。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的第六章}。Ch5 给了我们\textbf{自由能}这个判据,
\textbf{这一章把它变成可查的"地图"}——\textbf{相图}。

\textbf{相图是 Ch5 公切线法的产物}:\textbf{在每个温度做一次公切线,把平衡成分连成线,就是相图}。
\textbf{它也是 Ch7 CALPHAD 的直接产品}——CALPHAD 就是"用计算机算相图"。
\textbf{本章是任脉"静"的应用高峰,下一章 CALPHAD 是它的现代计算化}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{相图 = 成分-温度平面上的"地图"}。\textbf{给定一个点(某成分、某温度),
相图立刻告诉你三件事}:\textbf{有哪些相、各相什么成分、各相占多少比例}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 相图是自由能的可视化}——\textbf{在每个温度做公切线(Ch5),把平衡点连成相界线}。

\textbf{2. 杠杆定律算比例}——\textbf{在两相区,相分数与"对臂长度"成正比(像杠杆)}。

\textbf{3. 相图能预测凝固组织}——\textbf{沿冷却路径走一遍,就知道最终组织怎么来}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{Pb-Sn 共晶点 61.9\%Sn 的熔点只有 183°C}(比纯 Pb 327°C、纯 Sn 232°C 都低)——
\textbf{这就是焊料用共晶成分的原因};\textbf{把 Ch5 的公切线在不同温度连起来,
真的"长"出了相图的穹顶};\textbf{相图能算出 40\%Sn 合金凝固后是"初生 α + 共晶"组织}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{相、组元、相律}

\begin{itemize}
\item \textbf{相(Phase)}:成分和结构均匀的区域(固/液/气,或不同晶体结构的固相)
\item \textbf{组元(Component)}:构成体系的独立化学物质(如 Cu、Ni)
\item \textbf{Gibbs 相律}:$F = C - P + 2$($F$ 自由度,$C$ 组元数,$P$ 相数)——\textbf{决定相图的几何}
\end{itemize}

\subsection{二元相图的基本类型}

\begin{longtable}{|l|p{0.5\textwidth}|l|}
\hline
\rowcolor{primarycolor!10}
\textbf{类型} & \textbf{特征} & \textbf{例子} \\
\hline
匀晶 & 两组元完全互溶,只有液相线+固相线 & Cu-Ni \\
共晶 & L → $\alpha$ + $\beta$(液体同时结晶两固相)& Pb-Sn, Al-Si \\
包晶 & L + $\alpha$ → $\beta$ & Fe-C(部分)\\
共析 & $\gamma$ → $\alpha$ + $\beta$(固态版共晶)& Fe-C(钢的核心)\\
\hline
\end{longtable}

\subsection{相图上的线}

\begin{itemize}
\item \textbf{液相线(Liquidus)}:开始凝固的温度——线之上全是液体
\item \textbf{固相线(Solidus)}:完全凝固的温度——线之下全是固体
\item \textbf{固溶度线(Solvus)}:固相中溶解度的极限
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{相图是怎么"算"出来的}(公切线在不同温度的轨迹,即 CALPHAD)
\item \textbf{为什么共晶成分熔点最低}(自由能竞争的结果)
\item \textbf{相图怎么预测凝固组织}(冷却路径 + 杠杆定律)
\item \textbf{平衡相图 vs 实际组织的差异}(动力学不允许达到平衡——埋 Ch8-11 伏笔)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{相图是自由能曲线的"俯视图"}

\textbf{Ch5 我们画了某个温度下的自由能曲线 $G(x)$,用公切线找两相平衡成分}。
\textbf{但每个温度都有一条曲线}——\textbf{画几十条曲线太繁琐}。

\textbf{相图的妙处}:\textbf{在每个温度做一次公切线,只记录"平衡成分点",
然后把不同温度的点连成线}。\textbf{这条线就是相界}。\textbf{相图 = 把无数自由能曲线的
公切线点,投影到"成分-温度"平面}。

\textbf{所以相图不是经验画的,是从热力学"算"出来的}——\textbf{这正是 CALPHAD(Ch7)做的事}。

\subsection{读相图:三步定乾坤}

\textbf{给定一个点(成分 $c_0$,温度 $T$),怎么读}?

\begin{enumerate}
\item \textbf{看落在哪个区}:单相区(就是那个相)还是两相区?
\item \textbf{若在两相区,画水平线(等温线)}:它与两条相界的交点,\textbf{给出两个平衡相的成分}
\item \textbf{用杠杆定律}:算两相各占多少
\end{enumerate}

\textbf{这三步,是材料工程师每天都在做的事}——\textbf{相图是查得最多的一张图}。

\subsection{杠杆定律:为什么像杠杆}

\textbf{在两相区,合金总成分 $c_0$ 介于两相成分 $c_\alpha$、$c_\beta$ 之间}。
\textbf{质量守恒要求}:
$$f_\alpha = \frac{c_\beta - c_0}{c_\beta - c_\alpha}, \quad f_\beta = \frac{c_0 - c_\alpha}{c_\beta - c_\alpha}$$

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0]
  \draw[line width=1.2pt] (0,0) -- (6,0);
  \fill[staticcolor] (0,0) circle (0.08) node[below,font=\scriptsize]{$c_\alpha$};
  \fill[accentcolor] (6,0) circle (0.08) node[below,font=\scriptsize]{$c_\beta$};
  \fill[black] (2,0) circle (0.1) node[above,font=\scriptsize]{$c_0$(支点)};
  \draw[staticcolor,<->] (0,-0.5) -- (2,-0.5) node[midway,below,font=\scriptsize]{短臂};
  \draw[accentcolor,<->] (2,-0.5) -- (6,-0.5) node[midway,below,font=\scriptsize]{长臂};
  \node[font=\scriptsize,staticcolor] at (1,0.6) {$f_\beta \propto$ 短臂};
  \node[font=\scriptsize,accentcolor] at (4,0.6) {$f_\alpha \propto$ 长臂};
\end{tikzpicture}
\end{center}
```

\textbf{像跷跷板}:\textbf{成分点是支点,两端是两相成分}。\textbf{哪个相离支点远(长臂),
另一个相就多}——\textbf{对臂规则}。\textbf{这是质量守恒的几何表达,不是巧合}。

\subsection{共晶:为什么熔点最低}

\textbf{共晶反应}:$L \to \alpha + \beta$——\textbf{液体在恒温下同时结晶出两种固相}。
\textbf{共晶成分的熔点比任一纯组元都低}。

\textbf{为什么}?——\textbf{从自由能看,混合的液体熵高、自由能低,在更低温度仍稳定}。
\textbf{从相图看,两条液相线从两端往下走,交于最低点(共晶点)}。

\textbf{这有巨大实用价值}:\textbf{Pb-Sn 共晶焊料 183°C 就熔化,远低于纯金属,所以能低温焊接电路板}。
\textbf{除冰盐(NaCl-H$_2$O 共晶 -21°C)、低熔点合金,都用了这个原理}。

\section{4. 真正的数学}

\subsection{Gibbs 相律}

$$F = C - P + 2$$

$F$ 是自由度(可独立变化的变量数),$C$ 组元数,$P$ 相数,$+2$ 代表温度和压力。
\textbf{恒压时 $F = C - P + 1$}。

\textbf{例}:二元系($C=2$)恒压,\textbf{单相区 $F = 2$}(温度、成分可独立变);
\textbf{两相区 $F = 1$}(给定温度,两相成分就定了);\textbf{三相共存 $F = 0$}(温度、成分全固定——
这就是共晶点恒温反应的原因)。

\subsection{从自由能到相界}

\textbf{相界线 = 公切线点的轨迹}。在温度 $T$,两相 $\alpha$、$\beta$ 平衡的条件:
$$\frac{\partial G_\alpha}{\partial x}\bigg|_{x_\alpha} = \frac{\partial G_\beta}{\partial x}\bigg|_{x_\beta} \quad(\text{公切线斜率相等})$$
$$\mu_i^\alpha = \mu_i^\beta \quad(\text{化学势相等})$$

\textbf{扫描所有温度,解这组方程,得到的 $(x_\alpha, T)$ 和 $(x_\beta, T)$ 就连成相界}。

\subsection{杠杆定律的质量守恒推导}

设 $\alpha$ 相分数 $f_\alpha$,$\beta$ 相分数 $f_\beta = 1 - f_\alpha$。\textbf{组元质量守恒}:
$$c_0 = f_\alpha c_\alpha + f_\beta c_\beta$$
解出 $f_\alpha = \dfrac{c_\beta - c_0}{c_\beta - c_\alpha}$。\textbf{就这么简单——纯粹的质量守恒}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:共晶成分熔点最低}

运行配套模块 \texttt{phase\_diagram.py}:

\begin{verbatim}
Pb-Sn 焊料(真实数据):
纯Pb熔点 327°C, 纯Sn熔点 232°C
共晶点: 61.9%Sn, 183°C(最低熔点!)
共晶反应: L(61.9%Sn) → α(19.2%Sn) + β(97.5%Sn)
共晶组织中 α:45%, β:55%
\end{verbatim}

\textbf{Aha}:\textbf{共晶点的熔点 183°C,比纯 Pb(327°C)和纯 Sn(232°C)都低}。\textbf{两种金属混在一起,
熔点反而比任何一种纯金属都低}——\textbf{这违反直觉,但相图说得明明白白}。

\textbf{这就是为什么电子焊料用接近共晶的 Pb-Sn 成分}:\textbf{低熔点 = 低温焊接 = 不损伤元器件}。
\textbf{(现代无铅焊料用 Sn-Ag-Cu,原理相同——找共晶低熔点)}。

\subsection{相图从热力学"长"出来}

运行混溶间隙生成(连接 Ch5 公切线):

\begin{verbatim}
Ω=16000 J/mol, 临界温度 T_c=962K
温度K      左边界x    右边界x
914        0.310     0.690
760        0.138     0.862
606        0.056     0.944
452        0.016     0.984
\end{verbatim}

\textbf{Aha}:\textbf{把 Ch5 的公切线在每个温度做一遍,平衡成分点连起来,真的"长"出了相图的穹顶}——
\textbf{温度越低,混溶间隙越宽}。\textbf{这不是画出来的,是从自由能函数算出来的}。
\textbf{这正是 CALPHAD 的核心:相图 = 自由能 + 公切线 + 扫描温度}。

\subsection{相图预测凝固组织}

运行 40\%Sn 亚共晶合金的冷却路径:

\begin{verbatim}
1. 高温液相:40%Sn 均匀液体 L
2. 过液相线:开始析出初生 α 相(富Pb)
3. 接近183°C:初生α长大,剩余液体趋向共晶点 61.9%Sn
4. 共晶温度刚上方:初生α 51% + 共晶液体 49%
5. 共晶反应:剩余液体 → 共晶组织(α+β层片)
6. 室温组织:初生α(51%) + 共晶(49%)
\end{verbatim}

\textbf{Aha}:\textbf{相图不仅告诉你"平衡有什么相",还能预测"凝固后的组织长什么样"}——
\textbf{沿冷却路径走一遍,用杠杆定律算每步比例,就得到最终组织 = 初生 α + 共晶层片}。
\textbf{这把相图(Ch6)和组织(Ch4)直接连起来了}——\textbf{相图是组织的"预言书"}。

\subsection{怎么看见它:热分析与冷却曲线}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{相图上的相变温度,靠"热分析"(冷却曲线)测出来}。
\end{bluebox}

\textbf{原理}:\textbf{把合金熔化后缓慢冷却,记录温度随时间的变化}。\textbf{当发生相变(凝固、共晶反应),
会释放潜热,冷却曲线上出现"平台"或"拐点"}。

\begin{itemize}
\item \textbf{纯金属凝固}:冷却曲线出现\textbf{水平平台}(恒温凝固)
\item \textbf{固溶体凝固}:出现\textbf{两个拐点}(液相线、固相线温度)
\item \textbf{共晶反应}:出现\textbf{水平平台}(恒温三相反应,$F=0$)
\end{itemize}

\textbf{把不同成分合金的冷却曲线拐点温度,标到"成分-温度"图上,连起来就是相图}——
\textbf{这是相图最早的测定方法(19 世纪末至今)}。\textbf{现代用 DSC(Ch5)更精确}。
\textbf{能测什么}:液相线/固相线温度、共晶/包晶温度、相变潜热。
\textbf{局限}:冷却太快会偏离平衡(测到的不是平衡相图);微小相变热效应弱、难检测;
\textbf{慢扩散的固态相变可能完全测不到}。

\textbf{现代视角}:\textbf{今天的相图大多是 CALPHAD 计算 + 关键实验验证的结合}——
\textbf{纯实验测全相图代价太大,计算 + 少量实验校准是主流(Ch7)}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{合金设计}:查相图选成分,避开脆性相,获得想要的组织
\item \textbf{铸造}:用相图设计凝固路径,控制偏析和组织
\item \textbf{热处理}:Fe-C 相图是钢热处理的"圣经"(Ch11)
\item \textbf{焊接/钎焊}:用共晶低熔点设计焊料
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{CALPHAD}:用 $G(x,T)$ 数据库计算多元相图——\textbf{你的主场(Ch7)}
\item \textbf{高通量相图计算}:扫描成千上万种合金成分,预测相组成
\item \textbf{第一性原理相图}:DFT + 统计力学从头算相图(无需实验)
\item \textbf{相图 + 动力学(Ch12)}:相图给"终点",相场给"路径",合起来预测真实组织
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看相图}:本章手工画的二元相图,\textbf{在多元体系(5-6 元的真实合金)
根本画不出来——必须用 CALPHAD 计算}。\textbf{你的工作就是构建/优化 $G(x,T)$ 数据库,
让计算机算出可靠的多元相图}。\textbf{Ch7 我们正式进入 CALPHAD——本章是它的"手工版"前传}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么冬天撒盐化冰}:NaCl-H$_2$O 共晶 -21°C,盐水冰点远低于 0°C
\item \textbf{为什么钢能淬硬}:Fe-C 相图的奥氏体区 + 快冷(Ch11)
\item \textbf{为什么焊锡好用}:Pb-Sn 共晶低熔点
\item \textbf{为什么铝合金要时效}:固溶度随温度变(solvus 线),过饱和后析出强化
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:phase\_diagram.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{lever\_rule} & 杠杆定律算两相比例 \\
\texttt{isomorphous\_diagram} & 匀晶相图(Cu-Ni)液相线+固相线 \\
\texttt{eutectic\_diagram} & 共晶相图(Pb-Sn)真实数据 \\
\texttt{eutectic\_reaction} & 共晶反应 + 共晶组织相比例 \\
\texttt{miscibility\_gap} & 从自由能生成混溶间隙(连接 Ch5)\\
\texttt{cooling\_path\_eutectic} & 冷却路径追踪凝固组织 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 phase\_diagram.py}——\textbf{纯 numpy,真实相图数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(杠杆定律)} Cu-Ni 合金 35\%Ni,某温度下液相线 30\%Ni、固相线 50\%Ni。
固相分数多少?(用 \texttt{lever\_rule})温度降低时,固相是增多还是减少?

\item \textbf{(共晶)} 为什么共晶组织是"层片状"(α 和 β 交替)?
(提示:层片状缩短原子扩散距离——这是动力学,Ch9)

\item \textbf{(相律)} 用 Gibbs 相律解释:为什么二元共晶点是"恒温反应"($F=0$)?

\item \textbf{(冷却路径)} 用 \texttt{cooling\_path\_eutectic} 算 70\%Sn(过共晶)合金的组织。
和 40\%Sn(亚共晶)有什么不同?(提示:初生相变成 β)

\item \textbf{(平衡 vs 实际)} 为什么实际铸件常有"成分偏析"(芯部和边缘成分不同)?
相图假设的"平衡"为什么达不到?(提示:冷却太快,扩散来不及——埋 Ch8 伏笔)
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Callister, \textit{Materials Science and Engineering}(相图章)
\item \textbf{相变}:Porter \& Easterling, \textit{Phase Transformations in Metals and Alloys}
\item \textbf{相图集}:ASM \textit{Handbook Vol.3: Alloy Phase Diagrams}
\item \textbf{CALPHAD}:Saunders \& Miodownik, \textit{CALPHAD: A Comprehensive Guide}
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲三元相图的细节}(等温截面、liquidus 投影)——进阶,Ch7 略涉
\item \textbf{没讲 Fe-C 相图的完整解读}——留给 Ch11 热处理(它值得专门讲)
\item \textbf{没讲相变如何"发生"}(形核长大、扩散)——督脉 Ch8-9(静动对仗)
\item \textbf{没讲亚稳相图}(如马氏体)——Ch11 的"动力学战胜热力学"
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:相图是\textbf{成分-温度平面的"地图"},一眼查出\textbf{有哪些相、各相成分、各相比例}。\textbf{它是 Ch5 公切线法的产物}:每个温度做一次公切线,平衡点连成相界线。\textbf{读图三步}:看落在哪区 → 画等温线交相界得成分 → 杠杆定律算比例。\textbf{核心 Aha:共晶成分熔点最低}(Pb-Sn 183°C,焊料的原理);\textbf{把公切线在不同温度连起来,相图真的从热力学"长"出来};\textbf{相图能预测凝固组织}(冷却路径 + 杠杆 → 初生α + 共晶)。\textbf{怎么看见它:热分析冷却曲线,相变放潜热出现平台}。\textbf{Gibbs 相律 $F=C-P+2$ 决定相图几何}。\textbf{相图是"静"(平衡)的地图——但实际组织受动力学限制偏离平衡,这是督脉的主题}。\textbf{下一章}:相图的现代计算化——\textbf{CALPHAD 与计算热力学}。
\end{bluebox}

\begin{flushright}
\textit{第 6 章 · 相图:平衡的地图 · 完}
\end{flushright}
