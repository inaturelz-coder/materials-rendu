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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 2}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 原子键合与晶体结构}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 原子怎么周期性堆叠}\\[0.5em]
{\color{primarycolor!60} Atomic Bonding \& Crystal Structure}
\vspace{2em}
```

> "上一章我们看到原子靠键合连在一起。但金属里有 $10^{23}$ 个原子,
> 它们不是随便堆的——而是像橙子摆摊一样,\textbf{按完美的周期重复}。
> 为什么铁是体心立方而铜是面心立方?为什么同样的铁,
> 高温下会突然'换一种堆法'?这一章,我们进入\textbf{晶体}的世界。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的第二章}。上一章讲\textbf{单个原子}(电子排布、键合),
这一章讲\textbf{大量原子如何周期性堆叠成晶体}——\textbf{从"点"到"阵列"}。

\textbf{核心因果链推进}:电子排布 → 键合 →\,\textbf{晶体结构}\,→ 缺陷 → 组织 → 性能。
\textbf{这一章我们走到"晶体结构"这一环}——\textbf{它是后面所有结构概念(缺陷、相、组织)的几何舞台}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{晶体 = 原子在三维空间周期性重复排列}。\textbf{把原子近似成硬球,
它们倾向于尽量密堆}(能量最低)——\textbf{堆法只有有限几种,
每种堆法的"密度、配位数、密排面"都不同,直接决定材料的性质}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 晶体 = 晶格(周期骨架)+ 基元(每个格点上挂什么)}——14 种布拉菲晶格穷尽了所有周期方式。

\textbf{2. 金属主要三种堆法}:\textbf{FCC}(面心立方,如 Cu/Al)、\textbf{BCC}(体心立方,如 Fe/W)、\textbf{HCP}(六方密堆,如 Mg/Ti)。

\textbf{3. 堆得多密(堆垛因子 APF)+ 每个原子周围有几个邻居(配位数)→ 决定密度、塑性、滑移}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{仅凭"结构+原子量+原子半径",算出的金属密度与实测误差 $<0.3\%$}(W 钨 19.24 vs 19.25);
\textbf{FCC 和 HCP 都达到 0.74 的最密堆积}(开普勒 1611 年猜想,2014 年才严格证明);
\textbf{XRD 通过"哪些衍射峰在/不在",一眼区分 FCC 和 BCC}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{晶格、基元、晶胞}

\begin{itemize}
\item \textbf{晶格(Lattice)}:无限重复的\textbf{数学点阵},描述"周期性"本身
\item \textbf{基元(Basis)}:挂在每个格点上的\textbf{原子(团)}——晶体 = 晶格 + 基元
\item \textbf{晶胞(Unit Cell)}:能平移填满空间的\textbf{最小重复单元},用三条边长 $a,b,c$ 和三个夹角 $\alpha,\beta,\gamma$ 描述
\end{itemize}

\subsection{七大晶系与 14 种布拉菲晶格}

按晶胞的对称性,所有晶体归入\textbf{七大晶系}:立方、四方、正交、六方、三方、单斜、三斜。
\textbf{Bravais 证明:考虑格点的位置(简单/体心/面心/底心),
总共只有 14 种本质不同的周期排列方式}——\textbf{这是所有晶体的"周期字母表"}。

\subsection{三大金属结构}

\begin{longtable}{|l|l|l|l|l|}
\hline
\rowcolor{primarycolor!10}
\textbf{结构} & \textbf{原子/胞} & \textbf{配位数} & \textbf{APF} & \textbf{典型金属} \\
\hline
SC 简单立方 & 1 & 6 & 0.52 & Po(罕见)\\
BCC 体心立方 & 2 & 8 & 0.68 & Fe($\alpha$)/W/Cr/Mo \\
FCC 面心立方 & 4 & 12 & 0.74 & Cu/Al/Ni/Au/Ag \\
HCP 六方密堆 & 6 & 12 & 0.74 & Mg/Ti/Zn/Co \\
\hline
\end{longtable}

\subsection{晶向与晶面指数}

\begin{itemize}
\item \textbf{晶向}:用方括号 $[uvw]$ 表示(原点指向某格点的方向)
\item \textbf{晶面}:用\textbf{米勒指数(Miller indices)} $(hkl)$ 表示——\textbf{取晶面在三轴截距的倒数,化成最小整数比}
\item \textbf{族}:$\langle uvw\rangle$ 代表所有等价晶向,$\{hkl\}$ 代表所有等价晶面
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么 FCC 比 BCC 塑性好}(密排面/密排方向数量的差异)
\item \textbf{为什么铁会"变身"}(同素异构转变:$\alpha$-Fe BCC $\leftrightarrow$ $\gamma$-Fe FCC,炼钢的根本)
\item \textbf{XRD 衍射峰的"选择定则"从哪来}(晶胞内原子的相消干涉)
\item \textbf{为什么 HCP 的 $c/a$ 偏离理想值 1.633}(键合的方向性)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{密堆积:像摆橙子一样堆原子}

\textbf{把原子看成硬球,怎么堆最省空间}?——\textbf{这就是"摆水果摊"问题}。

\textbf{最密堆积}:先铺一层球(每个球周围 6 个),第二层球坐进第一层的"坑"里,第三层有两种选择:
\begin{itemize}
\item \textbf{ABAB 堆垛}→ \textbf{HCP}(六方密堆)
\item \textbf{ABCABC 堆垛}→ \textbf{FCC}(面心立方)
\end{itemize}

\textbf{两种都达到 APF = 0.74}——\textbf{这是硬球能达到的理论最大密度}。
\textbf{开普勒 1611 年猜测"没有比这更密的堆法"},\textbf{但严格数学证明直到 2014 年才完成(Hales)}——
\textbf{一个"显而易见"的事实,人类花了 400 年才证明}。

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62]
  % BCC
  \begin{scope}[shift={(0,0)}]
    \draw[primarycolor!60] (0,0,0) -- (2,0,0) -- (2,2,0) -- (0,2,0) -- cycle;
    \draw[primarycolor!60] (0,0,2) -- (2,0,2) -- (2,2,2) -- (0,2,2) -- cycle;
    \draw[primarycolor!60] (0,0,0) -- (0,0,2); \draw[primarycolor!60] (2,0,0) -- (2,0,2);
    \draw[primarycolor!60] (2,2,0) -- (2,2,2); \draw[primarycolor!60] (0,2,0) -- (0,2,2);
    \foreach \x/\y/\z in {0/0/0,2/0/0,2/2/0,0/2/0,0/0/2,2/0/2,2/2/2,0/2/2}
      \shade[ball color=staticcolor!60] (\x,\y,\z) circle (0.28);
    \shade[ball color=accentcolor!70] (1,1,1) circle (0.3);
    \node[font=\small\bfseries,primarycolor] at (1,-1,0) {BCC};
    \node[font=\scriptsize] at (1,-1.7,0) {体心 1 个};
  \end{scope}
  % FCC
  \begin{scope}[shift={(6,0)}]
    \draw[primarycolor!60] (0,0,0) -- (2,0,0) -- (2,2,0) -- (0,2,0) -- cycle;
    \draw[primarycolor!60] (0,0,2) -- (2,0,2) -- (2,2,2) -- (0,2,2) -- cycle;
    \draw[primarycolor!60] (0,0,0) -- (0,0,2); \draw[primarycolor!60] (2,0,0) -- (2,0,2);
    \draw[primarycolor!60] (2,2,0) -- (2,2,2); \draw[primarycolor!60] (0,2,0) -- (0,2,2);
    \foreach \x/\y/\z in {0/0/0,2/0/0,2/2/0,0/2/0,0/0/2,2/0/2,2/2/2,0/2/2}
      \shade[ball color=staticcolor!60] (\x,\y,\z) circle (0.28);
    \foreach \x/\y/\z in {1/1/0,1/1/2,1/0/1,1/2/1,0/1/1,2/1/1}
      \shade[ball color=goldcolor!80] (\x,\y,\z) circle (0.3);
    \node[font=\small\bfseries,primarycolor] at (1,-1,0) {FCC};
    \node[font=\scriptsize] at (1,-1.7,0) {面心 6 个半};
  \end{scope}
\end{tikzpicture}
\end{center}
```

\subsection{为什么 FCC 比 BCC 塑性好}

\textbf{金属塑性变形靠"滑移"——原子面沿密排方向滑动}。\textbf{滑移系 = 密排面 × 密排面上的密排方向}。

\begin{itemize}
\item \textbf{FCC}:密排面 $\{111\}$ 有 4 个,每个面上密排方向 $\langle 110\rangle$ 有 3 个 → \textbf{12 个滑移系}
\item \textbf{BCC}:没有真正的密排面,滑移系虽多但不密排,\textbf{需要更大力气启动}
\item \textbf{HCP}:只有 1 个基面 $(0001)$,密排方向 3 个 → \textbf{只有 3 个滑移系,所以脆}
\end{itemize}

\textbf{这就是为什么}:\textbf{铜铝(FCC)能拉成丝、压成箔;镁钛(HCP)难加工、易开裂}。
\textbf{结构(堆垛)直接决定了性能(塑性)}——\textbf{本书主旋律的又一次现身}。

\subsection{铁的"变身术":同素异构转变}

\textbf{同一种元素,不同温度下可以有不同晶体结构}——叫\textbf{同素异构(allotropy)}。
\textbf{铁是最重要的例子}:

\begin{itemize}
\item \textbf{室温 $\sim$912°C}:$\alpha$-Fe,\textbf{BCC}(铁素体)
\item \textbf{912$\sim$1394°C}:$\gamma$-Fe,\textbf{FCC}(奥氏体)
\item \textbf{1394$\sim$1538°C}:$\delta$-Fe,\textbf{BCC}(再次)
\end{itemize}

\textbf{这个 BCC$\leftrightarrow$FCC 的转变是整个炼钢工艺的根基}:
\textbf{FCC 奥氏体能溶解大量碳,BCC 铁素体几乎不溶碳}——\textbf{加热溶碳、淬火冻住,就得到马氏体}。
\textbf{(这是后面 Ch11 热处理的核心,本章先埋下伏笔)}。

\section{4. 真正的数学}

\subsection{堆垛因子的计算}

\textbf{堆垛因子} $\text{APF} = \dfrac{n \cdot \frac{4}{3}\pi r^3}{a^3}$,其中 $n$ 是每胞原子数,$r$ 原子半径,$a$ 晶格常数。

\textbf{关键是 $r$ 与 $a$ 的几何关系}(原子沿哪个方向相切):
\begin{itemize}
\item \textbf{BCC}:原子沿\textbf{体对角线}相切,$4r = \sqrt{3}\,a$ → $\text{APF} = \dfrac{\sqrt{3}\pi}{8} = 0.68$
\item \textbf{FCC}:原子沿\textbf{面对角线}相切,$4r = \sqrt{2}\,a$ → $\text{APF} = \dfrac{\sqrt{2}\pi}{6} = 0.74$
\end{itemize}

\subsection{理论密度}

$$\rho = \frac{n \cdot M}{V_{\text{cell}} \cdot N_A} = \frac{n \cdot M}{a^3 \cdot N_A}$$

其中 $M$ 是原子量,$N_A$ 阿伏伽德罗常数。\textbf{这个公式把"原子尺度"和"宏观密度"直接连起来}——
\textbf{下一节的 Aha 会用它精确算出金属密度}。

\subsection{立方晶系晶面间距}

$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

\textbf{晶面间距 $d$ 是 XRD 的核心量}——\textbf{衍射角直接由它决定}。

\subsection{布拉格定律}

$$n\lambda = 2d\sin\theta$$

\textbf{X 射线只在满足布拉格条件的角度才相长干涉、出现衍射峰}。\textbf{测出 $\theta$ → 反推 $d$ → 反推晶格常数 $a$}——
\textbf{这就是 XRD 测晶体结构的全部数学}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:从结构算密度,误差不到 0.3\%}

运行配套模块 \texttt{crystal\_structure.py}:

\begin{verbatim}
金属        结构   a(nm)    理论ρ   实测ρ   误差
---------------------------------------------------
Al 铝       FCC   0.4047   2.70    2.70   0.1%
Cu 铜       FCC   0.3615   8.94    8.96   0.3%
Fe 铁(α)    BCC   0.2866   7.88    7.87   0.1%
W 钨        BCC   0.3166  19.24   19.25   0.1%
Ni 镍       FCC   0.3524   8.91    8.90   0.1%
Cr 铬       BCC   0.2884   7.20    7.19   0.1%
\end{verbatim}

\textbf{Aha}:\textbf{仅凭"晶体结构 + 原子量 + 原子半径"三个数,
就能算出金属的宏观密度,误差不到 0.3\%}。\textbf{这是"原子尺度 → 宏观性质"最干净的一次贯通}——
\textbf{你测一块金属有多重,本质是在数它每个晶胞里塞了多少原子}。

\textbf{为什么 W(钨)密度高达 19.25}?——\textbf{原子量大(183.8)+ BCC 堆得紧 + 半径小}。
\textbf{所以钨用来做穿甲弹芯、灯丝、配重块}——\textbf{它的"重"直接写在晶体结构里}。

\subsection{怎么看见它:XRD 与布拉格定律}

\begin{bluebox}
\textbf{怎么看见它}(本书贯穿全书的表征专节)。\textbf{这一章的对象是晶体结构——
看它的主力工具是 X 射线衍射(XRD)}。
\end{bluebox}

\textbf{原理}:X 射线波长($\sim$0.15 nm)和原子间距($\sim$0.2-0.4 nm)\textbf{同数量级},
\textbf{晶体就像一个三维光栅}。X 射线打上去,\textbf{只在满足布拉格定律 $n\lambda = 2d\sin\theta$ 的角度相长干涉},
形成尖锐衍射峰。

运行模块算铝(FCC, $a=0.4049$ nm)的 XRD 谱:

\begin{verbatim}
晶面      d(nm)    2θ(度)     ← Cu Kα 波长 0.15406 nm
(111)    0.2338   38.48
(002)    0.2024   44.73
(022)    0.1432   65.11
(113)    0.1221   78.24
\end{verbatim}

\textbf{Aha}:\textbf{铝的 (111) 峰在 38.48°——这是真实 XRD 谱图上铝的第一个峰的标准位置}。
\textbf{测出峰的角度,反推 $d$,反推 $a$}——\textbf{XRD 就是这样"看见"肉眼看不见的原子排列的}。

\textbf{能测什么}:晶体结构类型、晶格常数(精度可达 0.0001 nm)、物相组成(每种物相有指纹谱)、
晶粒尺寸(峰宽,Scherrer 公式)、残余应力(峰移)、织构(峰强分布)。
\textbf{局限}:对非晶态(玻璃)只有"馒头峰";对微量相($<$几 \%)不敏感;轻元素散射弱。

\subsection{为什么有些衍射峰"消失"了——选择定则}

运行模块的选择定则分析:

\begin{verbatim}
FCC 允许的衍射: (111) (002) (022) (113) (222) (133)
BCC 允许的衍射: (011) (002) (112) (022) (013) (222)
→ FCC 看不到 (100)(110),BCC 看不到 (100)(111)
\end{verbatim}

\textbf{Aha}:\textbf{晶胞里"额外"的原子(BCC 的体心、FCC 的面心),
它们散射的 X 射线波会和角顶原子的波相消干涉,让某些本该出现的峰"消失"}。
\textbf{FCC 要求 $h,k,l$ 全奇或全偶;BCC 要求 $h+k+l$ 为偶数}。

\textbf{这有巨大实用价值}:\textbf{拿到一块未知金属,看 XRD 谱图里"哪些峰在、哪些缺席",
立刻就能判断它是 FCC 还是 BCC}——\textbf{不用任何其它信息}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{相鉴定}:XRD 是材料实验室最常用的设备,\textbf{拿到样品先打个 XRD 看是什么相}
\item \textbf{钢铁热处理}:奥氏体(FCC)$\to$ 马氏体(体心四方)的结构转变是淬火强化的核心
\item \textbf{钛合金}:$\alpha$(HCP)/ $\beta$(BCC)两相比例决定钛合金性能——航空发动机关键
\item \textbf{半导体}:Si 是金刚石结构(两套 FCC 套构),晶向 $(100)/(111)$ 决定芯片切割方向
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{DFT 预测晶体结构}:给定成分,算哪种结构能量最低——\textbf{第一性原理预测稳定相}
\item \textbf{晶体结构数据库}:ICSD、Materials Project 收录几十万种晶体结构
\item \textbf{结构搜索算法}:USPEX、CALYPSO 用进化算法\textbf{搜索未知的新晶体结构}
\item \textbf{机器学习}:从成分预测晶体结构类型,加速新材料发现
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看晶体结构}:今天给一个化学式(比如某个新合金),
\textbf{DFT 能算出它最可能是 FCC 还是 BCC,晶格常数多少,稳不稳定}——
\textbf{从 Bragg 用 X 射线"测"结构,到用计算机"预测"结构,这是材料科学的范式跃迁}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么金箔能打到极薄}:Au 是 FCC,12 个滑移系,极易塑性变形
\item \textbf{为什么镁合金轮毂轻但脆}:Mg 是 HCP,滑移系少,轻(密度小)但延展性差
\item \textbf{为什么钻石和石墨都是碳却天差地别}(回应 Ch1):金刚石是金刚石立方结构,石墨是层状六方
\item \textbf{雪花为什么六角形}:冰的晶体结构是六方,宏观对称性直接来自原子排列对称性
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:crystal\_structure.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{packing\_factor} & FCC/BCC/SC 堆垛因子的几何推导 \\
\texttt{theoretical\_density} & 从结构 + 原子量算密度 \\
\texttt{density\_comparison} & 6 种金属理论 vs 实测密度(误差 $<0.3\%$)\\
\texttt{d\_spacing\_cubic} & 立方晶系晶面间距 \\
\texttt{bragg\_angle} & 布拉格定律算衍射角 \\
\texttt{xrd\_pattern} & 模拟 XRD 衍射峰位置 \\
\texttt{allowed\_reflections} & FCC/BCC 选择定则 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 crystal\_structure.py}——\textbf{纯 numpy,真实数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(密度)} 用 \texttt{theoretical\_density} 算金(Au, FCC, 原子量 197, 半径 0.144 nm)的密度,
与实测 19.32 g/cm³ 对比。为什么金和钨密度接近但结构不同?

\item \textbf{(XRD)} 用 \texttt{xrd\_pattern} 算 $\alpha$-Fe(BCC, $a=0.2866$ nm)的衍射谱。
它的第一个峰 (110) 在多少度?和铝的 (111) 比哪个角度小?

\item \textbf{(选择定则)} 为什么 FCC 的第一个峰是 (111) 而不是 (100)?
从晶胞内原子散射相消的角度解释。

\item \textbf{(滑移系)} 查资料:为什么 HCP 金属(Mg/Ti)在室温脆,但加热后塑性变好?
(提示:温度激活了非基面滑移系)

\item \textbf{(同素异构)} 铁从 BCC($\alpha$)变到 FCC($\gamma$)时,体积是膨胀还是收缩?
用两种结构的 APF 估算。(提示:FCC 更密)
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Callister, \textit{Materials Science and Engineering}(第 3 章晶体结构)
\item \textbf{晶体学}:Cullity, \textit{Elements of X-Ray Diffraction}(XRD 圣经)
\item \textbf{固体物理}:Kittel, \textit{Introduction to Solid State Physics}(第 1-2 章)
\item \textbf{在线工具}:Materials Project / VESTA(晶体结构可视化软件)
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲倒易点阵}(XRD 的更深数学框架)——固体物理课展开
\item \textbf{没讲准晶}(2011 诺奖,打破"周期"才是晶体的旧定义)——进阶话题
\item \textbf{没讲复杂晶体结构}(钙钛矿、尖晶石等)——后面具体材料章涉及
\item \textbf{没讲电子衍射/中子衍射}——留给附录 C 表征速览
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:晶体 = 晶格 + 基元,\textbf{14 种布拉菲晶格穷尽周期排列}。金属主要三种堆法:\textbf{FCC}(0.74,12 配位,塑性好)、\textbf{BCC}(0.68,8 配位)、\textbf{HCP}(0.74,但滑移系少而脆)。\textbf{核心 Aha:仅凭结构+原子量+半径,算金属密度误差$<0.3\%$}——原子尺度直通宏观。\textbf{怎么看见它:XRD 用布拉格定律 $n\lambda=2d\sin\theta$,通过衍射峰位置反推结构,通过选择定则区分 FCC/BCC}。\textbf{结构决定性能再现:FCC 滑移系多所以铜铝能拉丝,HCP 滑移系少所以镁钛脆}。\textbf{伏笔:铁的 BCC$\leftrightarrow$FCC 同素异构转变,是后面炼钢与热处理的根基}。\textbf{下一章}:完美晶体里的"不完美"——\textbf{晶体缺陷的几何}。
\end{bluebox}

\begin{flushright}
\textit{第 2 章 · 原子键合与晶体结构 · 完}
\end{flushright}
