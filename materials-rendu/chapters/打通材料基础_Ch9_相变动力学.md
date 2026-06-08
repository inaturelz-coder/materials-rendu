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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 9}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 相变动力学:形核与长大}\\[0.3em]
{\color{dynamiccolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{dynamiccolor!85} 督脉 · 该不该变 vs 变多快}\\[0.5em]
{\color{primarycolor!60} Phase Transformation Kinetics: Nucleation \& Growth}
\vspace{2em}
```

> "相图(Ch6)说:这个钢冷下来'应该'变成珠光体。可现实里,
> 同一块钢,慢冷得到珠光体,快冷却得到完全不同的马氏体。
> \textbf{相图没骗你——它说的是'平衡',但现实有'时间'这个变量}。
> 相变要先\textbf{形核}(凭空造出一个新相的小核),再\textbf{长大}。
> 这一章,我们补上相图缺的那一维:\textbf{时间}。"

\vspace{2em}

\begin{bluebox}
\textbf{这是督脉(动)的第二章,也是 Ch5/Ch6 的"动态对仗"}。

\textbf{Ch5 热力学 + Ch6 相图(静)回答}:\textbf{该不该变?变成什么相?}(看自由能、看相图)。
\textbf{本章(动)回答}:\textbf{变多快?怎么变?能不能变得成?}(形核、长大、时间)。
\textbf{这正是全书"一静一动"主轴最核心的一次对照}——\textbf{热力学给"方向",
动力学给"路径和速率"}。\textbf{它也为 Ch11 热处理的高潮(马氏体之谜)埋下全部伏笔}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{相变 = 形核 + 长大}。\textbf{热力学说"该变"(自由能能降),但变不变得成,看动力学}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 形核要过"能垒"}:造一个新相的小核,体积降能量但表面升能量,
\textbf{小核会溶解,只有超过临界尺寸 $r^*$ 才能长大}。

\textbf{2. 形核率是一场竞争}:\textbf{高温驱动力小(难形核),低温扩散慢(原子跳不动),
中温最快}——\textbf{产生著名的 C 形曲线}。

\textbf{3. 总动力学是 S 形}:Avrami 方程 $f = 1 - e^{-kt^n}$——\textbf{开始慢(形核)、
中间快(长大)、末尾慢(碰撞)}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{过冷度越大,临界核越小}($r^* \propto 1/\Delta T$,300K 过冷只需 221 个原子);
\textbf{形核率峰值在中温(C 曲线鼻尖)};\textbf{TTT 曲线的鼻尖,正是"淬火要躲过的那个弯"——
躲过它就得到马氏体(Ch11 高潮)}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{相变的两步}

\begin{itemize}
\item \textbf{形核(Nucleation)}:在母相中形成一个新相的稳定小核——\textbf{要克服能垒}
\item \textbf{长大(Growth)}:核形成后,通过原子扩散(Ch8)不断长大
\end{itemize}

\subsection{形核的分类}

\begin{longtable}{|l|p{0.6\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{类型} & \textbf{说明} \\
\hline
均匀形核 & 在母相内部随机形核——\textbf{需要很大过冷度(能垒高)} \\
非均匀形核 & 在晶界、夹杂、表面等缺陷处形核——\textbf{能垒低,实际中占主导} \\
\hline
\end{longtable}

\subsection{动力学曲线}

\begin{itemize}
\item \textbf{TTT 曲线}(Time-Temperature-Transformation):等温转变图,\textbf{C 形}
\item \textbf{CCT 曲线}(Continuous Cooling Transformation):连续冷却转变图
\item \textbf{Avrami 方程}:$f = 1 - \exp(-kt^n)$,描述转变分数随时间的演化
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么形核率曲线是 C 形}(驱动力与扩散的竞争——本章核心)
\item \textbf{临界核到底是什么}(为什么有的核溶解、有的长大)
\item \textbf{Avrami 指数 $n$ 的物理含义}(它编码了形核和长大的机制)
\item \textbf{TTT 的"鼻尖"如何决定了淬火工艺}(为 Ch11 马氏体铺路)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{形核:一场能量的赌博}

\textbf{造一个新相的小核,有两笔账}:
\begin{itemize}
\item \textbf{体积项(赚)}:新相自由能更低,每造一点体积就赚 $-\frac{4}{3}\pi r^3 \Delta g_v$
\item \textbf{表面项(亏)}:新核和母相之间有界面,要付界面能 $+4\pi r^2 \gamma$
\end{itemize}

\textbf{小核时表面项($r^2$)占优——亏本,核会溶解}。\textbf{大核时体积项($r^3$)占优——赚,核会长大}。
\textbf{中间有个临界半径 $r^*$,对应能垒最高点(形核功 $\Delta G^*$)}。

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
  \draw[->,gray] (0,0) -- (5.5,0) node[right,font=\scriptsize]{核半径 $r$};
  \draw[->,gray] (0,-1.8) -- (0,2.2) node[above,font=\scriptsize]{$\Delta G$};
  % 表面项 +r^2
  \draw[staticcolor,dashed,domain=0:4,samples=50] plot (\x,{0.28*\x*\x});
  \node[staticcolor,font=\scriptsize] at (3.5,2.0) {表面项 $+r^2$};
  % 体积项 -r^3
  \draw[dynamiccolor,dashed,domain=0:4.2,samples=50] plot (\x,{-0.09*\x*\x*\x});
  \node[dynamiccolor,font=\scriptsize] at (4.3,-1.5) {体积项 $-r^3$};
  % 总和
  \draw[accentcolor,line width=1.2pt,domain=0:4.4,samples=60] plot (\x,{0.28*\x*\x-0.09*\x*\x*\x});
  % 峰值标记
  \draw[dotted] (2.07,0) -- (2.07,1.2);
  \fill[accentcolor] (2.07,1.2) circle (0.06);
  \node[accentcolor,font=\scriptsize] at (2.07,1.5) {$\Delta G^*$};
  \node[font=\scriptsize] at (2.07,-0.3) {$r^*$};
  \node[accentcolor,font=\scriptsize] at (3.9,0.3) {总 $\Delta G$};
\end{tikzpicture}
\end{center}
```

\textbf{临界核就是站在能垒顶上的核}:\textbf{再小一点就溶解,再大一点就长大}。
\textbf{形核的难点,就是靠热涨落"爬过"这个能垒 $\Delta G^*$}。

\subsection{过冷度:让临界核变小}

\textbf{驱动力 $\Delta g_v$ 正比于过冷度 $\Delta T$}(冷得越狠,新相越想形成)。\textbf{于是}:
$$r^* = \frac{2\gamma}{\Delta g_v} \propto \frac{1}{\Delta T}, \qquad \Delta G^* = \frac{16\pi\gamma^3}{3\Delta g_v^2} \propto \frac{1}{\Delta T^2}$$

\textbf{过冷度越大,临界核越小、形核功越低、越容易形核}。\textbf{这就是为什么液体要"过冷"才结晶}——
\textbf{刚到熔点时驱动力为零,临界核无穷大,根本造不出来}。\textbf{必须过冷到一定程度,
临界核小到热涨落能造出来}。

\subsection{C 曲线:驱动力与扩散的拔河}

\textbf{形核率 $I$ 由两个指数因子相乘}:
$$I = A \cdot \underbrace{\exp\left(-\frac{\Delta G^*}{k_B T}\right)}_{\text{热力学:形核功}} \cdot \underbrace{\exp\left(-\frac{Q_d}{k_B T}\right)}_{\text{动力学:扩散}}$$

\begin{itemize}
\item \textbf{高温(过冷小)}:$\Delta G^*$ 巨大(临界核大)→ 第一项趋于 0 → \textbf{形核慢}
\item \textbf{低温(过冷大)}:扩散冻结(原子跳不动)→ 第二项趋于 0 → \textbf{形核慢}
\item \textbf{中温}:两者折中 → \textbf{形核率最大}
\end{itemize}

\textbf{这场"拔河"产生了一个中温峰值——画在温度-时间图上,就是 C 形曲线的"鼻尖"}。
\textbf{这是本章最深刻的洞察,也是整个热处理工艺的物理基础}。

\subsection{长大与碰撞:S 形曲线}

\textbf{核形成后靠扩散长大}。\textbf{但随着新相越来越多,它们开始互相"碰撞",长大停止}。
\textbf{整个过程的转变分数随时间呈 S 形}:\textbf{开始慢(忙着形核)→ 中间快(大量长大)→
末尾慢(互相碰撞,没地方长)}。\textbf{Avrami 方程 $f = 1 - e^{-kt^n}$ 精确描述了这条 S 曲线}。

\section{4. 真正的数学}

\subsection{形核的能量}

$$\Delta G(r) = -\frac{4}{3}\pi r^3 \Delta g_v + 4\pi r^2 \gamma$$

求极值 $\mathrm{d}\Delta G/\mathrm{d}r = 0$:
$$r^* = \frac{2\gamma}{\Delta g_v}, \qquad \Delta G^* = \frac{16\pi\gamma^3}{3(\Delta g_v)^2}$$

\textbf{$r^*$ 是临界半径,$\Delta G^*$ 是形核功(能垒高度)}。

\subsection{形核率}

$$I = A \exp\left(-\frac{\Delta G^*}{k_B T}\right)\exp\left(-\frac{Q_d}{k_B T}\right)$$

\textbf{第一个指数随 $T$ 降低而增大(过冷大、$\Delta G^*$ 小),第二个随 $T$ 降低而减小(扩散慢)}——
\textbf{两者竞争给出中温峰值}。

\subsection{Avrami(JMAK)方程}

$$f = 1 - \exp(-k t^n)$$

\textbf{$n$ 是 Avrami 指数(1$\sim$4),编码形核和长大的几何与机制}:
\begin{itemize}
\item \textbf{$n=1$}:界面控制的片状长大;\textbf{$n=2.5$}:扩散控制 + 持续形核;\textbf{$n=4$}:均匀形核 + 三维长大
\end{itemize}

\textbf{从实验 $f$-$t$ 曲线拟合 $n$,能反推相变机制}——\textbf{动力学的"指纹"}。

\subsection{长大速率}

\textbf{扩散控制的长大}:界面推进速度 $\propto \sqrt{D/t}$,长大尺寸 $\propto \sqrt{Dt}$(又是 Ch8 的 $\sqrt{Dt}$)。
\textbf{这把形核(本章)和扩散(Ch8)缝在了一起}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:过冷度越大,临界核越小}

运行配套模块 \texttt{phase\_kinetics.py}:

\begin{verbatim}
过冷度对临界核的影响(Cu,γ=0.2 J/m²):
过冷度ΔT(K)   r*(nm)    核内原子数
10           25.87     5958357
50            5.17       47667
100           2.59        5958
200           1.29         745
300           0.86         221
→ 过冷度越大,临界核越小(r* ∝ 1/ΔT)
\end{verbatim}

\textbf{Aha}:\textbf{过冷 10K 时,临界核要近 600 万个原子——靠热涨落根本造不出来};
\textbf{过冷 300K 时,临界核只要 221 个原子——容易多了}。\textbf{这定量解释了
"为什么液体能过冷"}:\textbf{在熔点附近驱动力太小,临界核大到不可能形成,
必须冷到足够低,临界核才小到热涨落能够造出}。

\subsection{C 曲线:形核率的中温峰值}

\begin{verbatim}
温度°C   过冷度   形核率(相对)
927      158     7.09e-26   ← 高温:驱动力小,形核慢
727      358     4.93e+18
627      458     1.87e+22
527      558     3.05e+23   ← 中温:峰值!(C曲线鼻尖)
427      658     2.50e+23   ← 低温:扩散变慢,开始下降
\end{verbatim}

\textbf{Aha}:\textbf{形核率不是温度越低越快,而是在中温(527°C)达到峰值}。\textbf{高温端
驱动力不足,低温端扩散冻结——中间最快}。\textbf{这个峰值,画在温度-时间坐标上
就是 C 形曲线的"鼻尖"}。\textbf{整个热处理工艺,都是围绕"鼻尖"做文章}。

\subsection{TTT 鼻尖与淬火}

\begin{verbatim}
温度°C    转变开始时间(相对)
927       ∞(太慢)
627       5.34e+07
527       3.28e+06   ← 鼻尖:转变最快
427       4.00e+06
327       4.98e+07
\end{verbatim}

\textbf{Aha}:\textbf{TTT 曲线在中温有个"鼻尖"(转变最快的温度)}。\textbf{如果冷却足够快,
"躲过"这个鼻尖,扩散型相变(珠光体)来不及发生}——\textbf{原子被冻在原地,
被迫发生无扩散的切变相变,得到马氏体}。\textbf{这就是淬火的全部秘密,
也是 Ch11 全书高潮"马氏体之谜"的核心}。\textbf{热力学(相图)说该得珠光体,
动力学(躲过鼻尖)让你得到马氏体——动力学战胜了热力学}。

\subsection{怎么看见它:膨胀法与金相+电阻}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{相变动力学(转变了多少、多快)主要靠"原位"测量——
膨胀法、电阻法,配合金相验证组织}。
\end{bluebox}

\textbf{相变常伴随体积、电阻、磁性的变化,这些是动力学的"探针"}:

\begin{itemize}
\item \textbf{膨胀法(dilatometry)}:相变时体积变化(如奥氏体 FCC → 铁素体 BCC 体积膨胀)——\textbf{测试样长度随温度/时间变化,捕捉相变开始和结束}
\item \textbf{电阻法}:不同相电阻率不同,\textbf{原位测电阻随时间变化,得到转变分数-时间曲线}(可拟合 Avrami)
\item \textbf{差示扫描量热(DSC,Ch5)}:相变放/吸热,测相变焓和速率
\item \textbf{淬火 + 金相(Ch4)}:在不同时间淬火"冻住"组织,金相测各时刻转变分数——\textbf{直接构建 TTT 曲线}
\end{itemize}

\textbf{TTT 曲线的实验构建}:\textbf{把样品快速加热到奥氏体区,再快速降到某等温温度,保温不同时间后淬火,
金相看转变了多少}——\textbf{重复多个温度和时间,连成 C 形曲线}。\textbf{能测什么}:相变开始/结束时间、
转变分数、Avrami 指数(反推机制)、临界冷却速率。\textbf{局限}:快速相变(如马氏体)难以原位捕捉;
膨胀/电阻信号需要组织标定;\textbf{形核是统计事件,小样品涨落大}。

\textbf{现代视角}:\textbf{原位同步辐射 XRD / 中子衍射能实时追踪相变(毫秒级时间分辨),
直接看各相的演化}——\textbf{把"事后金相"升级为"实时电影"}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{钢的热处理}:TTT/CCT 曲线是制定淬火、退火、正火工艺的依据(Ch11)
\item \textbf{时效硬化}:铝合金、镍基合金的析出强化靠控制形核长大
\item \textbf{铸造凝固}:形核率决定晶粒大小(加形核剂细化晶粒)
\item \textbf{非晶合金(金属玻璃)}:冷却快到"完全躲过"形核——无晶体形成
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{相场法(Ch12)}:直接模拟形核、长大、组织演化——\textbf{动力学的主力工具}
\item \textbf{CALPHAD + 动力学}:CALPHAD(Ch7)给驱动力 $\Delta g_v$,动力学算速率——\textbf{静驱动动}
\item \textbf{形核理论的第一性原理}:DFT 算界面能 $\gamma$,MD 模拟形核事件
\item \textbf{机器学习}:从成分预测 TTT 曲线、临界冷却速率
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看相变动力学}:本章的形核驱动力 $\Delta g_v$,\textbf{正是 CALPHAD(Ch7)
计算的输出};\textbf{界面能 $\gamma$ 可由 DFT 算}。\textbf{有了这些,相场模拟(Ch12)
能直接"播放"形核长大的全过程}。\textbf{这是"一静一动"的完整闭环:CALPHAD(静)给驱动力,
相场(动)算演化}——\textbf{你做的相图/相场工作,正处在这个闭环的核心}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么蜂蜜会结晶}:糖过饱和后形核长大(加热溶解 = 逆过程)
\item \textbf{为什么冰淇淋要快速冷冻}:慢冻冰晶长大变粗糙,快冻冰晶细腻
\item \textbf{为什么暖宝宝能放热}:醋酸钠过饱和液,按一下触发形核,瞬间结晶放热
\item \textbf{为什么玻璃不结晶}:冷却太快,完全躲过形核(过冷液体冻结成非晶)
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:phase\_kinetics.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{nucleation\_energy} & 形核总自由能(体积项 vs 表面项)\\
\texttt{critical\_nucleus} & 临界半径 $r^*$ 和形核功 $\Delta G^*$ \\
\texttt{undercooling\_effect} & 过冷度对临界核的影响 \\
\texttt{nucleation\_rate} & 形核率的 C 曲线(驱动力 vs 扩散)\\
\texttt{avrami} & Avrami 方程的 S 形曲线 \\
\texttt{ttt\_curve} & TTT 曲线(C 形)的生成 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 phase\_kinetics.py}——\textbf{纯 numpy,真实形核数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(临界核)} 用 \texttt{undercooling\_effect} 算:过冷度从 100K 增加到 200K,
临界核体积变成原来的几分之一?(提示:$r^* \propto 1/\Delta T$,体积 $\propto 1/\Delta T^3$)

\item \textbf{(非均匀形核)} 为什么实际形核几乎总在晶界、夹杂处发生?
从"降低形核功 $\Delta G^*$"的角度解释。

\item \textbf{(C 曲线)} 用 \texttt{nucleation\_rate},为什么形核率在中温最大?
如果某材料扩散激活能很低(原子很灵活),鼻尖会往高温还是低温移?

\item \textbf{(Avrami)} 测得某相变 $f$-$t$ 数据拟合出 $n=4$,
这暗示什么形核长大机制?(提示:均匀形核 + 三维长大)

\item \textbf{(淬火)} 为什么"躲过 TTT 鼻尖"就能得到马氏体?
临界冷却速率和鼻尖位置什么关系?(Ch11 会详解)
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Porter \& Easterling, \textit{Phase Transformations in Metals and Alloys}(相变圣经)
\item \textbf{形核理论}:Christian, \textit{The Theory of Transformations in Metals and Alloys}
\item \textbf{钢的相变}:Bhadeshia, \textit{Bainite in Steels}
\item \textbf{计算工具}:相场软件(MOOSE、FiPy、PRISMS-PF)
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲无扩散相变(马氏体)的细节}——留给 Ch11 高潮
\item \textbf{没讲调幅分解(spinodal,无需形核)}——Ch5 提过,Ch12 相场展开
\item \textbf{没讲具体的 CCT 曲线读法}——Ch11 结合钢的热处理
\item \textbf{没讲形核的涨落理论细节}——统计物理专题
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:相变 = \textbf{形核 + 长大}。\textbf{形核要过能垒}:体积项(降能)vs 表面项(升能),只有超过临界半径 $r^*$ 才能长大,能垒高度是形核功 $\Delta G^*$。\textbf{过冷度越大,临界核越小}($r^*\propto 1/\Delta T$)。\textbf{核心 Aha:形核率是"驱动力 vs 扩散"的竞争,中温最快}——产生 C 形曲线的"鼻尖"。\textbf{总动力学是 S 形}(Avrami $f=1-e^{-kt^n}$)。\textbf{怎么看见它:膨胀法/电阻法原位测,金相构建 TTT 曲线,同步辐射实时追踪}。\textbf{静动对仗:Ch5/Ch6(热力学+相图)说"该不该变",本章说"变多快"——热力学给方向,动力学给路径}。\textbf{TTT 的鼻尖是 Ch11 马氏体之谜的钥匙:躲过它,动力学就战胜了热力学}。\textbf{下一章}:另一种"动"——缺陷的运动,\textbf{位错与塑性}(对仗 Ch3)。
\end{bluebox}

\begin{flushright}
\textit{第 9 章 · 相变动力学:形核与长大 · 完}
\end{flushright}
