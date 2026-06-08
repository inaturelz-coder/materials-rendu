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
{\fontsize{48}{48}\selectfont\bfseries\color{goldcolor!60} C}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 附录 C:材料表征手段速览}\\[0.3em]
{\color{mergecolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{mergecolor} 怎么看见它 · 系统总收口}\\[0.5em]
{\color{primarycolor!60} Materials Characterization: A Systematic Overview}
\vspace{2em}
```

> "全书每一章都有一节『怎么看见它』,讲透了那一章对象对应的表征手段。
> 这个附录把它们\textbf{系统地收口}——按『探测什么信号』归类,
> 配一张『分辨率-视场』定位图,让你一眼看清:看原子用什么,看晶粒用什么,
> 看成分用什么。这是全书表征暗线的总图。"

\vspace{1.5em}

\section{表征的核心逻辑:用什么"探针"测什么"信号"}

\textbf{所有表征手段,本质都是}:\textbf{用某种"探针"(X 射线、电子、离子、光)
打到材料上,接收返回的"信号"(衍射、成像、能谱),反推材料的结构或成分}。

\textbf{按探针和信号分五大类}:

\begin{longtable}{|l|p{0.32\textwidth}|p{0.32\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{类别} & \textbf{探测什么} & \textbf{代表手段} \\
\hline
衍射类 & 晶体结构、晶格常数、物相 & XRD、电子衍射、中子衍射 \\
成像类 & 形貌、组织、缺陷 & OM、SEM、TEM、AFM \\
谱学类 & 成分、化学态、电子结构 & EDS、EELS、XPS、ARPES \\
取向类 & 晶粒取向、织构、应变 & EBSD \\
原子级/三维 & 单原子、三维重构 & APT、3D-XRD、原子分辨 TEM \\
\hline
\end{longtable}

\section{按尺度选工具:分辨率-视场定位图}

\textbf{选表征手段的第一原则:看你要看多大尺度的东西}。\textbf{分辨率越高,视场越小}
(看得越细,看到的范围越小)——\textbf{这是表征的基本权衡}。

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0,
  m/.style={rectangle,draw=staticcolor,fill=staticcolor!10,rounded corners=2pt,font=\scriptsize,align=center,minimum height=0.7cm}]
  % 横轴:分辨率(从粗到细,左到右)
  \draw[->,gray,thick] (-0.3,0) -- (10,0) node[right,font=\scriptsize]{分辨率(越右越细)};
  \node[font=\scriptsize,gray] at (1,-0.4) {mm};
  \node[font=\scriptsize,gray] at (3.5,-0.4) {µm};
  \node[font=\scriptsize,gray] at (6,-0.4) {nm};
  \node[font=\scriptsize,gray] at (8.5,-0.4) {原子(Å)};
  % 各手段定位
  \node[m] at (1.2,1.0) {肉眼/卡尺};
  \node[m] at (2.5,1.9) {光学显微镜 OM};
  \node[m] at (4.3,1.0) {SEM};
  \node[m] at (4.3,2.6) {EBSD};
  \node[m] at (6.3,1.9) {TEM};
  \node[m] at (8.3,1.0) {原子分辨 TEM};
  \node[m] at (8.3,2.6) {APT 原子探针};
  \node[m] at (6.3,3.3) {XRD(平均)};
  \node[font=\scriptsize,staticcolor] at (5,4.0) {\textbf{看得越细(右),视场越小}};
\end{tikzpicture}
\end{center}
```

\section{衍射类:看晶体结构}

\subsection{X 射线衍射(XRD)}(Ch2)
\textbf{原理}:X 射线波长($\sim$0.15 nm)与原子间距同量级,晶体像三维光栅,
满足布拉格定律 $n\lambda=2d\sin\theta$ 处出现衍射峰。
\textbf{测什么}:晶体结构类型、晶格常数(精度 0.0001 nm)、物相组成、晶粒尺寸(峰宽)、
残余应力(峰移)、织构。\textbf{局限}:对非晶只有"馒头峰";微量相($<$几\%)不敏感;
是"平均"信息(不是单个晶粒)。

\subsection{电子衍射 / 中子衍射}
\textbf{电子衍射}(在 TEM 中):局部微区的晶体结构,可分析单个晶粒、纳米相。
\textbf{中子衍射}:穿透力强(测块体),对轻元素(H、Li)和磁结构敏感——XRD 的互补。

\section{成像类:看形貌与组织}

\subsection{光学显微镜(OM / 金相)}(Ch4)
\textbf{原理}:可见光成像,放大 50-1000×。\textbf{关键是腐蚀}——化学试剂选择性腐蚀晶界
和不同相,产生衬度。\textbf{测什么}:晶粒尺寸、相分布、组织类型(珠光体/马氏体等)。
\textbf{局限}:分辨率受光波长限($\sim$0.2 µm),看不清纳米组织。

\subsection{扫描电镜(SEM)}
\textbf{原理}:电子束扫描表面,接收二次电子(形貌)或背散射电子(成分衬度)。
\textbf{放大几万倍,景深大}。\textbf{测什么}:表面形貌、断口分析(Ch15)、第二相、配 EDS 测成分。

\subsection{透射电镜(TEM)}(Ch3)
\textbf{原理}:高能电子($>$100 kV)穿透极薄样品。\textbf{衍射衬度成像看位错}
(g·b=0 不可见判据,Ch3),分辨率达原子级。\textbf{测什么}:位错(类型、柏氏矢量、密度)、
纳米相、晶界结构、原子排列。\textbf{局限}:制样难(要减薄到电子可穿透)、视场极小、可能束损伤。

\subsection{原子力显微镜(AFM)}
\textbf{原理}:探针扫描表面,测原子间力。\textbf{测什么}:表面形貌(纳米级高度分辨)、
粗糙度、薄膜表面——不需要导电样品。

\section{谱学类:看成分与电子结构}

\subsection{能谱(EDS / EELS)}
\textbf{EDS}(配 SEM/TEM):测特征 X 射线,给出元素成分(快速、半定量)。
\textbf{EELS}(配 TEM):测电子能量损失,对轻元素、化学态、电子结构敏感。

\subsection{X 射线光电子能谱(XPS)}
\textbf{测表面($\sim$nm)的元素组成 + 化学态}(氧化态、键合)——表面分析、腐蚀研究。

\subsection{角分辨光电子能谱(ARPES)}(Ch14)
\textbf{直接"拍"出能带结构}——电子的能量-动量关系。\textbf{验证 DFT 算的能带}。

\subsection{电子探针(EPMA)}(Ch6/Ch8)
\textbf{高精度定量成分分析}——测相成分(对照 CALPHAD)、扩散偶浓度剖面(测扩散系数)。

\section{取向类:看晶粒取向与应变}

\subsection{电子背散射衍射(EBSD)}(Ch4/Ch10)
\textbf{原理}(在 SEM 中):测每个点的晶体取向。\textbf{测什么}:晶粒取向分布(织构)、
晶界类型、几何必需位错(GND)密度、塑性应变分布。\textbf{是连接组织(Ch4)和塑性(Ch10)的利器}。

\section{原子级 / 三维:看单原子与立体组织}

\subsection{原子探针层析(APT)}
\textbf{原理}:逐个原子蒸发 + 飞行时间质谱。\textbf{三维重构 + 单原子成分}——
看析出相、晶界偏析的原子级分布。\textbf{材料表征的"终极分辨"}。

\subsection{三维表征(3D-XRD / FIB 连续切片)}
\textbf{3D-XRD / 同步辐射断层}:无损追踪体内晶粒演化。
\textbf{FIB 连续切片 + EBSD}:逐层切 + 成像,重构真实三维组织(作相场 Ch12 的输入/验证)。

\subsection{原位与同步辐射}
\textbf{原位(in-situ)}:边加载/加热/通电边观察——把"事后快照"升级成"实时电影"。
\textbf{同步辐射}:超高亮度 X 射线,实现毫秒级时间分辨、微米级空间分辨的实时追踪。

\section{速查表:看什么用什么}

\begin{longtable}{|p{0.3\textwidth}|p{0.6\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{你想看} & \textbf{首选手段} \\
\hline
晶体结构/物相 & XRD(块体平均)、电子衍射(微区)\\
晶格常数 & XRD(高精度)\\
晶粒尺寸/组织 & OM 金相(µm)、SEM(细)、EBSD(取向)\\
位错 & TEM(g·b 判据)\\
成分(整体)& XRF、EDS \\
成分(微区/相)& EPMA、TEM-EDS \\
成分(表面/化学态)& XPS \\
成分(原子级三维)& APT \\
晶粒取向/织构 & EBSD、XRD 极图 \\
能带/电子结构 & ARPES(实验)、DFT(计算)\\
磁性 & VSM/SQUID 磁强计、XMCD \\
相变(动力学)& 膨胀法、电阻法、DSC、原位 XRD \\
断口/失效 & SEM 断口分析、无损检测(NDT)\\
三维组织 & FIB 切片+EBSD、3D-XRD \\
\hline
\end{longtable}

\begin{bluebox}
\textbf{表征的黄金法则}:\textbf{没有"最好"的手段,只有"最合适"的手段}。\textbf{先问三个问题}:
\textbf{(1) 我要看多大尺度?}(选分辨率)\textbf{(2) 我要看结构、成分还是性能?}(选信号类型)
\textbf{(3) 块体平均还是局部单点?}(选视场)。\textbf{实际研究常需多种手段交叉验证}——
\textbf{比如验证一个 CALPHAD 算的相图,要用 DSC(相变温度)+ EPMA(相成分)+ 金相(相比例)+ XRD(物相)}。
\end{bluebox}

\begin{flushright}
\textit{附录 C · 材料表征手段速览 · 完}
\end{flushright}
