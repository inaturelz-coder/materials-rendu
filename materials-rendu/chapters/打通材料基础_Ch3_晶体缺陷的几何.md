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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 3}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 晶体缺陷的几何}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 完美晶体里的"不完美"}\\[0.5em]
{\color{primarycolor!60} The Geometry of Crystal Defects}
\vspace{2em}
```

> "上一章的晶体是完美的——原子整整齐齐排到无穷远。
> 但真实晶体没有完美的。\textbf{每立方厘米的金属里,有 $10^{12}$ 条位错、
> 无数空位、密密麻麻的晶界}。神奇的是——\textbf{正是这些"缺陷",
> 让金属能弯曲、能强化、能扩散}。这一章,我们爱上不完美。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的第三章}。前两章讲完美结构(原子、晶体),
这一章讲\textbf{真实晶体的"不完美"——缺陷的几何}。

\textbf{关键的静动对仗}:本章讲缺陷"\textbf{长什么样}"(静态几何);
\textbf{它们怎么"运动"——位错滑移、空位扩散——留给督脉 Ch10}。
\textbf{同一个位错,任脉看它的几何,督脉看它的运动}——\textbf{这正是"一静一动"主轴的精髓}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{真实晶体充满缺陷,而缺陷不是"瑕疵",是"功能"}。\textbf{按维度分四类}:

\textbf{0 维(点缺陷)}:空位、间隙原子、杂质原子——\textbf{决定扩散、导电、掺杂}。

\textbf{1 维(线缺陷)}:位错——\textbf{决定塑性和强度}。\textbf{金属能被锤打成型,全靠位错}。

\textbf{2 维(面缺陷)}:晶界、相界、孪晶界——\textbf{决定强度、腐蚀、晶粒长大}。

\textbf{3 维(体缺陷)}:孔洞、夹杂、第二相——\textbf{断裂和疲劳的起源}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{空位浓度从室温到熔点暴涨 $10^{12}$ 倍}(指数敏感于温度);
\textbf{位错越多金属越强}(重度冷加工 vs 退火,位错密度差 10 万倍,强度大增——反直觉!);
\textbf{晶粒越细越强}(Hall-Petch,100µm→1µm 强度 +38\%);
\textbf{TEM 用 $g\cdot b=0$ 判据能唯一定出位错的柏氏矢量}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{缺陷的维度分类}

\begin{longtable}{|l|p{0.3\textwidth}|l|p{0.22\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{维度} & \textbf{例子} & \textbf{尺度} & \textbf{主要影响} \\
\hline
0 维 点缺陷 & 空位/间隙/置换原子 & $\sim$0.1 nm & 扩散/电阻/掺杂 \\
1 维 线缺陷 & 刃位错/螺位错 & 长 µm 级 & 塑性/强度 \\
2 维 面缺陷 & 晶界/相界/孪晶/表面 & $\sim$nm 厚 & 强度/腐蚀 \\
3 维 体缺陷 & 孔洞/夹杂/第二相 & µm-mm & 断裂/疲劳 \\
\hline
\end{longtable}

\subsection{点缺陷}

\begin{itemize}
\item \textbf{空位(Vacancy)}:格点上少了一个原子。\textbf{平衡浓度由温度决定}(永远存在)
\item \textbf{自间隙(Interstitial)}:原子挤进格点间隙,能量很高(罕见)
\item \textbf{置换/间隙杂质}:外来原子占据格点 / 钻进间隙——\textbf{合金化与掺杂的基础}
\end{itemize}

\subsection{位错}

\begin{itemize}
\item \textbf{刃位错(Edge)}:多出半个原子面,\textbf{柏氏矢量 $\perp$ 位错线}
\item \textbf{螺位错(Screw)}:原子面螺旋上升,\textbf{柏氏矢量 $\parallel$ 位错线}
\item \textbf{柏氏矢量 $\vec{b}$}:描述位错引起的晶格畸变大小和方向——\textbf{位错的"身份证"}
\end{itemize}

\subsection{面缺陷}

\begin{itemize}
\item \textbf{晶界}:相邻晶粒取向不同,中间的过渡区。\textbf{小角度晶界 = 位错墙;大角度晶界 = 无序区}
\item \textbf{孪晶界}:镜像对称的特殊晶界,能量低
\item \textbf{相界}:不同相之间的界面
\item \textbf{表面}:晶体的终止,能量最高(原子有"悬键")
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么"缺陷越多金属越强"}(位错互相缠结,难以运动)
\item \textbf{空位浓度对温度有多敏感}(指数关系,熔点附近暴涨)
\item \textbf{TEM 怎么"数"位错、"测"柏氏矢量}(不是看一眼那么简单)
\item \textbf{为什么晶粒细化是"唯一免费的午餐"}(既增强又增韧)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{空位:为什么总是存在}

\textbf{你可能以为完美晶体能量最低}。错——\textbf{有少量空位时,自由能反而更低}。

\textbf{原因是熵}:制造一个空位要消耗能量(形成能 $Q_f$),但空位可以在 $N$ 个格点中任意分布,
\textbf{大大增加了组态熵}。自由能 $G = H - TS$ 中,\textbf{熵项 $-TS$ 让一定数量的空位成为平衡态}。

\textbf{平衡空位浓度}:
$$\frac{n_v}{N} = \exp\left(-\frac{Q_f}{k_B T}\right)$$

\textbf{这是 Arrhenius 形式}——\textbf{温度越高,空位指数暴涨}。\textbf{空位是扩散的"载体"(Ch8),
没有空位,原子无法在固体里搬家}——\textbf{所以这个公式是后面整个动力学的前提}。

\subsection{位错:金属为什么能弯曲}

\textbf{一个谜题}:理论计算,让一整层原子同时滑过另一层(完美晶体的剪切),
\textbf{需要的应力约是实测屈服强度的 1000 倍}。\textbf{金属为什么这么"软"}?

\textbf{答案是位错}。\textbf{位错让滑移"逐个原子"进行,而非"整层同时"}——
\textbf{就像移动一大块地毯:你不会整块拖(费力),而是推一个褶皱过去(省力)}。

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.5]
  % 完美晶格
  \foreach \x in {0,...,7} \foreach \y in {0,...,3}
    \fill[staticcolor!50] (\x,\y) circle (0.13);
  % 刃位错:上半多一列
  \foreach \y in {2,3} \fill[accentcolor!70] (3.5,\y) circle (0.15);
  \draw[accentcolor,thick] (3.5,1.6) -- (3.5,3.4);
  \node[font=\scriptsize,accentcolor] at (3.5,4.0) {多出半原子面};
  \node[font=\scriptsize,accentcolor] at (3.5,-0.8) {$\perp$ 刃位错};
  \node[font=\scriptsize,primarycolor] at (10,1.8) {地毯褶皱:};
  \node[font=\scriptsize,primarycolor] at (10,1.0) {推褶皱省力};
  \node[font=\scriptsize,primarycolor] at (10,0.2) {= 位错滑移};
\end{tikzpicture}
\end{center}
```

\textbf{这就是为什么金属能锻造、能拉丝、能冲压}——\textbf{位错让塑性变形以极低的应力发生}。
\textbf{没有位错,金属会像玻璃一样脆}。\textbf{(位错怎么"动",是 Ch10 的核心——本章只讲它的几何)}。

\subsection{反直觉:缺陷越多越强}

\textbf{既然位错让金属变软,那位错越多应该越软}?——\textbf{恰恰相反}。

\textbf{当位错很多时,它们互相缠结、互相阻挡,反而难以运动}——\textbf{金属变硬变强}。
\textbf{这就是"加工硬化"(冷加工)}:\textbf{反复锤打 → 位错暴增 → 互相钉扎 → 越打越硬}。

\textbf{Taylor 关系}量化了这点:$\Delta\tau = \alpha G b \sqrt{\rho}$——\textbf{强度增量正比于位错密度的平方根}。

\subsection{晶界:好缺陷}

\textbf{晶界阻挡位错运动}——位错冲到晶界就被挡住,\textbf{晶粒越细、晶界越多、位错越难穿越 → 越强}。

\textbf{Hall-Petch 关系}:$\sigma_y = \sigma_0 + k_y / \sqrt{d}$,\textbf{晶粒尺寸 $d$ 越小,强度越高}。

\textbf{晶粒细化是材料强化里唯一"既增强又增韧"的方法}——\textbf{其它强化(固溶、位错、第二相)都会牺牲韧性,
唯独细化晶粒两者兼得}。\textbf{所以叫"免费的午餐"}。

\section{4. 真正的数学}

\subsection{平衡空位浓度的热力学推导}

引入 $n$ 个空位,焓变 $\Delta H = n Q_f$,组态熵 $\Delta S = k_B \ln\binom{N}{n}$。
用 Stirling 近似最小化 $G = nQ_f - T\Delta S$,得:
$$\frac{n_v}{N} = \exp\left(-\frac{Q_f}{k_B T}\right)$$

\textbf{这是熵驱动"不完美"的经典案例}——\textbf{完美不是平衡,有缺陷才是}。

\subsection{Taylor 强化关系}

$$\Delta\tau = \alpha G b \sqrt{\rho}$$

其中 $G$ 剪切模量,$b$ 柏氏矢量模,$\rho$ 位错密度,$\alpha\approx 0.3$-$0.6$。
\textbf{位错密度从 $10^{10}$(退火)到 $10^{15}$(重度冷加工),$\sqrt{\rho}$ 增大 $\sim$300 倍}。

\subsection{Hall-Petch 关系}

$$\sigma_y = \sigma_0 + \frac{k_y}{\sqrt{d}}$$

\textbf{物理图像}:位错在晶粒内塞积(pile-up),在晶界前形成应力集中。
\textbf{晶粒越小,塞积位错数越少,应力集中越弱,需要更大外力才能让相邻晶粒屈服}。

\subsection{TEM 衍射衬度的 g·b 判据}

\textbf{位错在 TEM 明场像里是黑线}——因为它畸变的晶格改变了局部衍射条件。
\textbf{但当衍射矢量 $\vec{g}$ 垂直于柏氏矢量 $\vec{b}$ 时}:
$$\vec{g}\cdot\vec{b} = 0 \quad\Rightarrow\quad \text{位错不可见}$$

\textbf{物理}:$\vec{g}\cdot\vec{b}=0$ 意味着位错没有扰动这组衍射面,衬度消失。
\textbf{反过来用}:换不同的 $\vec{g}$ 观察位错何时消失,\textbf{就能反推未知位错的 $\vec{b}$}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:缺陷越多,金属越强}

运行配套模块 \texttt{crystal\_defects.py}:

\begin{verbatim}
状态          位错密度(/m²)    强度增量(MPa)
充分退火        1e10            0.6
轻度冷加工      1e12            5.8
中度冷加工      1e14           57.6
重度冷加工      1e15          182.1
\end{verbatim}

\textbf{Aha}:\textbf{位错是"缺陷",但位错越多金属越强}——\textbf{重度冷加工的位错密度是退火态的 10 万倍,
强度增量从 0.6 暴增到 182 MPa}。\textbf{这彻底颠覆了"缺陷=瑕疵"的直觉}。

\textbf{这就是为什么}:\textbf{反复弯折铁丝会越来越硬(加工硬化),最后断裂};\textbf{冷轧钢板比热轧的强};
\textbf{铁匠"千锤百炼"——每一锤都在增加位错}。\textbf{缺陷的几何(位错密度),直接决定了性能(强度)}。

\subsection{空位浓度:对温度的指数敏感}

\begin{verbatim}
温度            空位浓度       每多少原子有1个空位
27°C  (300K)    7.6e-16       1 / 1.3e15
527°C (800K)    2.1e-6        1 / 4.7e5
1083°C(1356K)   4.5e-4        1 / 2200      ← 铜熔点
\end{verbatim}

\textbf{Aha}:\textbf{室温下铜里几乎没有空位($10^{15}$ 个原子才 1 个),
熔点附近每 2200 个原子就有 1 个空位}——\textbf{浓度暴涨了 12 个数量级}。
\textbf{这种指数敏感性正是 Arrhenius 行为}——\textbf{它解释了为什么扩散、相变、蠕变都强烈依赖温度(后面督脉反复出现)}。

\subsection{怎么看见它:TEM 与 g·b 判据}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{这一章的对象是缺陷——XRD(Ch2)只能给"平均"信息,
看单个位错要靠透射电镜(TEM)}。
\end{bluebox}

\textbf{原理}:TEM 用高能电子束(200-300 kV)穿透极薄样品($<$100 nm)。\textbf{位错周围畸变的晶格
改变局部衍射条件,在像上形成黑色衬度}——\textbf{这叫衍射衬度成像}。

\textbf{但位错不是随便都能看见}。运行模块的 $g\cdot b$ 分析:

\begin{verbatim}
实验:位错在 g=(200) 下可见,在 g=(111) 下不可见
候选 b      (200)·b   (111)·b   符合观察?
[110]         2         2
[1-10]        2         0       ★ 是它!
[101]         2         2
[011]         0         2
\end{verbatim}

\textbf{Aha}:\textbf{当 $g\cdot b = 0$ 时位错"消失"}。\textbf{用两个不同的衍射矢量 $g$ 观察,
看位错在哪个 $g$ 下消失,就能唯一确定它的柏氏矢量 $b$}——\textbf{这里定出 $b = \frac{1}{2}[1\bar{1}0]$}。

\textbf{能测什么}:位错类型(刃/螺)、柏氏矢量、位错密度、滑移系、位错与第二相的交互;
还能看晶界结构、纳米析出相、孪晶。\textbf{TEM 分辨率达 0.1 nm,能直接"看见"原子列}。
\textbf{局限}:样品要减薄到电子可穿透(制样难、耗时)、视场极小($\sim$µm)、电子束可能损伤样品、
\textbf{只能看"局部",代表性需谨慎}。

\textbf{这就是"怎么看见缺陷"的真相}——\textbf{不是显微镜下一看就有,而是要懂衍射、选对 $g$、做不可见判据}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{加工硬化}:冷轧、拉拔、喷丸——\textbf{主动引入位错来强化}
\item \textbf{晶粒细化}:控轧控冷、严重塑性变形(ECAP)——\textbf{Hall-Petch 强化}
\item \textbf{半导体掺杂}:往 Si 里掺入 ppm 级杂质(点缺陷)——\textbf{整个电子工业的基础}
\item \textbf{固溶强化}:置换原子(如不锈钢的 Cr/Ni)畸变晶格,阻碍位错
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{分子动力学(MD)}:模拟位错的形核、运动、与晶界交互——\textbf{百万原子尺度}
\item \textbf{位错动力学(DDD)}:把位错当线缺陷直接模拟,\textbf{算加工硬化曲线}
\item \textbf{DFT 算缺陷能}:空位形成能、晶界能、层错能——\textbf{第一性原理给出本章的 $Q_f$}
\item \textbf{相场法}:模拟晶粒长大、孔洞演化(Ch12)
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看缺陷}:本章的空位形成能 $Q_f$、位错的柏氏矢量、晶界能,
\textbf{今天都能用 DFT/MD 从第一性原理算出来}。\textbf{你做相场模拟(后面 Ch12),
模拟的就是缺陷(晶界、相界)的演化}——\textbf{缺陷的几何(本章)是缺陷动力学(督脉)的输入}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么回形针反复弯折会断}:加工硬化 + 位错塞积 → 局部脆化 → 断裂
\item \textbf{为什么金属疲劳}:循环载荷下位错往复运动,在表面萌生裂纹(Ch15)
\item \textbf{为什么不锈钢比纯铁强}:Cr/Ni 置换原子的固溶强化
\item \textbf{为什么纳米材料超强}:晶粒小到纳米级,Hall-Petch 强化到极致(但太小会反转)
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:crystal\_defects.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{vacancy\_concentration} & 平衡空位浓度的 Arrhenius 行为 \\
\texttt{taylor\_strengthening} & 位错密度 → 强度增量 \\
\texttt{hall\_petch} & 晶粒尺寸 → 屈服强度 \\
\texttt{gb\_invisibility} & TEM 的 $g\cdot b$ 不可见判据 \\
\texttt{burgers\_vector\_analysis} & 用两个 $g$ 反推柏氏矢量 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 crystal\_defects.py}——\textbf{纯 numpy,真实物理数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(空位)} 铝的空位形成能 $Q_f\approx 0.67$ eV,比铜低。
用 \texttt{vacancy\_concentration} 算铝在 300K 和 900K 的空位浓度,
为什么铝比铜更"容易"产生空位?

\item \textbf{(位错)} 为什么 Taylor 关系里是 $\sqrt{\rho}$ 而不是 $\rho$?
(提示:位错间距正比于 $1/\sqrt{\rho}$)

\item \textbf{(Hall-Petch)} 晶粒细化到几纳米时,Hall-Petch 会"反转"(越细越软)。
查资料,为什么?(提示:晶界滑移开始主导)

\item \textbf{(TEM)} 如果一个位错在 $g=(200)$ 和 $g=(020)$ 下都可见,
但在 $g=(002)$ 下不可见,它的柏氏矢量可能是什么方向?

\item \textbf{(综合)} 为什么"既要强又要韧"很难?列出四种强化方式,
说明哪些会牺牲韧性,为什么只有晶粒细化不牺牲。
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Callister, \textit{Materials Science and Engineering}(第 4-5 章缺陷)
\item \textbf{位错}:Hull \& Bacon, \textit{Introduction to Dislocations}(位错圣经)
\item \textbf{TEM}:Williams \& Carter, \textit{Transmission Electron Microscopy}
\item \textbf{强化机制}:Courtney, \textit{Mechanical Behavior of Materials}
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲位错怎么运动}(滑移、攀移、增殖)——留给督脉 Ch10(静动对仗)
\item \textbf{没讲位错反应与缠结的细节}——位错专著展开
\item \textbf{没讲点缺陷簇、级联损伤}(辐照材料)——核材料专题
\item \textbf{没讲晶界的具体结构}(CSL、晶界工程)——进阶话题
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:真实晶体充满缺陷,\textbf{按维度分四类}:点(空位/杂质)、线(位错)、面(晶界)、体(孔洞/夹杂)。\textbf{缺陷不是瑕疵是功能}:空位驱动扩散,位错带来塑性,晶界提供强化。\textbf{核心 Aha:缺陷越多金属越强}(位错密度差 10 万倍,强度大增)——彻底颠覆"缺陷=瑕疵"的直觉。\textbf{空位浓度对温度指数敏感}(室温到熔点暴涨 $10^{12}$ 倍),是扩散的前提。\textbf{Hall-Petch:晶粒细化是唯一"既增强又增韧"的方法}。\textbf{怎么看见它:TEM 衍射衬度 + $g\cdot b=0$ 判据,能唯一定出位错的柏氏矢量——表征不是"看一眼",是懂衍射、选 $g$、做判据}。\textbf{静动对仗:本章讲缺陷的几何(静),它们的运动留给 Ch10(动)}。\textbf{下一章}:缺陷与相在空间的排布——\textbf{微观组织}。
\end{bluebox}

\begin{flushright}
\textit{第 3 章 · 晶体缺陷的几何 · 完}
\end{flushright}
