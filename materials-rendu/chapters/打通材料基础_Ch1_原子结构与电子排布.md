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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 1}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 原子结构与电子排布}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 一切材料性质的最底层}\\[0.5em]
{\color{primarycolor!60} Atomic Structure \& Electron Configuration}
\vspace{2em}
```

> "为什么金子是金色的,铜是红色的?为什么钻石硬、石墨软,
> 但它们都是纯碳?为什么铁有磁性,铝没有?
> 这些问题的答案,\textbf{全都藏在原子的电子排布里}。
> 这一章,我们从材料世界的最底层——\textbf{单个原子}——开始。"

\vspace{2em}

\begin{bluebox}
\textbf{这是全书的地基章}。无论你想理解\textbf{结构}(晶体怎么堆)、
\textbf{性能}(为什么导电/磁性/坚硬)、还是\textbf{工艺}(为什么这样加工),
\textbf{所有材料问题,最终都能追溯到原子的电子排布}。

\textbf{材料科学的核心因果链}:\textbf{电子排布 → 键合方式 → 晶体结构 → 微观组织 → 宏观性能}。
本章打通这条链的\textbf{第一环}——\textbf{从电子排布到键合}。后面所有章节,都是这条链的延伸。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{材料 = 大量原子按某种方式键合在一起}。\textbf{原子怎么键合,
取决于它最外层的电子(价电子)}——\textbf{而价电子的行为,由电子排布决定}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. 电子住在"能级"里}——不是绕着核乱飞,而是占据确定的能量轨道(量子化)。

\textbf{2. 最外层电子(价电子)决定一切}——\textbf{化学性质、键合方式、导电与否,全看价电子}。

\textbf{3. 电负性差决定键合类型}——差大了是\textbf{离子键}(NaCl),差小了是\textbf{共价键}(金刚石)或\textbf{金属键}(铜)。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{同样是纯碳,金刚石和石墨硬度天差地别}——\textbf{只因键合方式不同};
\textbf{Li 到 Ne 原子半径缩小 77\%}——\textbf{只因核电荷增加};
\textbf{Fe 的磁性来自 3d 轨道的 6 个电子}——\textbf{一切都能从电子排布读出}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{原子的组成}

\textbf{原子 = 原子核(质子 + 中子)+ 核外电子}。
\begin{itemize}
\item \textbf{质子}:带正电,数目 = 原子序数 $Z$,决定"是什么元素"
\item \textbf{中子}:不带电,改变中子数 = 同位素
\item \textbf{电子}:带负电,质量约为质子的 1/1836,\textbf{决定化学和材料性质}
\end{itemize}

\textbf{关键比例}:原子核直径约 $10^{-15}$ m,原子直径约 $10^{-10}$ m——\textbf{核只占原子体积的 $10^{-15}$}。
\textbf{原子内部 99.9999...\% 是"空的"}——\textbf{但电子云让原子表现得像个实心球}。

\subsection{四个量子数}

电子的状态由\textbf{四个量子数}完全描述:

\begin{longtable}{|l|l|p{0.45\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{量子数} & \textbf{符号} & \textbf{含义} \\
\hline
主量子数 & $n$ & 能级(第几层),$n = 1, 2, 3, \ldots$ \\
角量子数 & $l$ & 轨道形状(s/p/d/f),$l = 0 \ldots n-1$ \\
磁量子数 & $m_l$ & 轨道空间取向,$m_l = -l \ldots +l$ \\
自旋量子数 & $m_s$ & 电子自旋,$\pm 1/2$ \\
\hline
\end{longtable}

\textbf{三大填充规则}:
\begin{itemize}
\item \textbf{泡利不相容原理}:一个轨道最多 2 个电子(自旋相反)
\item \textbf{能量最低原理}:电子先填能量低的轨道
\item \textbf{洪特规则}:同能量轨道,电子先单独占据(自旋平行)
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么填充顺序是 4s 在 3d 之前}(Madelung 规则的物理根源)
\item \textbf{电子排布如何直接预测一个材料是金属、半导体还是绝缘体}
\item \textbf{为什么过渡金属(Fe/Co/Ni)有磁性,而碱金属没有}
\item \textbf{电负性这个"软"概念,如何定量预测键合类型}
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{电子为什么不掉进核里}

经典物理预言:\textbf{带负电的电子绕带正电的核转,会辐射能量、螺旋掉进核里}——
\textbf{原子应该在 $10^{-11}$ 秒内崩溃}。但现实是原子稳定存在了 138 亿年。

\textbf{量子力学的答案}:\textbf{电子只能待在确定的能级上}(能量量子化),
\textbf{最低能级(基态)就是"坑底"——电子无处可掉}。

\textbf{类氢原子能级公式}(玻尔模型):
$$E_n = -\frac{13.6 \, Z^2}{n^2} \text{ eV}$$

\textbf{基态 $n=1$ 能量 $-13.6$ eV 是最低点}——\textbf{要把电子拿走(电离)需要 13.6 eV}。
\textbf{这与氢原子电离能的实测值完全一致}。

\subsection{Madelung 规则:为什么 4s 先于 3d}

\textbf{填充顺序不是简单的 $n$ 从小到大},而是按 \textbf{$(n+l)$ 排序}:

\begin{center}
1s → 2s → 2p → 3s → 3p → \textbf{4s} → \textbf{3d} → 4p → 5s → 4d → ...
\end{center}

\textbf{为什么 4s($n+l=4$)排在 3d($n+l=5$)前面}?——
\textbf{4s 电子虽然主量子数大,但它的轨道能"钻"到内层附近,感受到更强的核吸引,所以能量反而更低}。
\textbf{这个"轨道穿透效应"是过渡金属一切特殊性质的根源}。

\subsection{价电子:材料性质的"决策者"}

\textbf{原子的化学和材料行为,几乎只由最外层电子(价电子)决定}:

\begin{itemize}
\item \textbf{Na(3s$^1$)}:1 个价电子,容易丢掉 → \textbf{活泼金属,+1 价}
\item \textbf{Cl(3s$^2$3p$^5$)}:差 1 个填满,容易抢电子 → \textbf{活泼非金属,-1 价}
\item \textbf{Ne(3s$^2$3p$^6$)}:最外层填满,极稳定 → \textbf{惰性气体,不反应}
\item \textbf{C(2s$^2$2p$^2$)}:4 个价电子,既不易丢也不易抢 → \textbf{爱共享,成共价键}
\end{itemize}

\textbf{周期表的"族"(纵列)本质是"价电子数相同"}——\textbf{所以同族元素性质相似}。

\subsection{三种主要键合}

\textbf{原子结合成材料,主要靠三种"强键"}:

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9,
  a/.style={circle,draw=primarycolor,fill=primarycolor!12,minimum size=0.7cm,font=\scriptsize},
  ap/.style={circle,draw=accentcolor,fill=accentcolor!15,minimum size=0.7cm,font=\scriptsize},
  am/.style={circle,draw=goldcolor,fill=goldcolor!25,minimum size=0.7cm,font=\scriptsize}]
  % 离子键
  \node[a] (na) at (0,0) {Na$^+$};
  \node[ap] (cl) at (1.1,0) {Cl$^-$};
  \node[font=\scriptsize,primarycolor] at (0.55,-0.8) {离子键};
  \node[font=\tiny] at (0.55,-1.2) {(转移)};
  % 共价键
  \node[a] (c1) at (3.3,0) {C};
  \node[a] (c2) at (4.4,0) {C};
  \draw[line width=1.5pt,goldcolor] (c1) -- (c2);
  \node[font=\scriptsize,primarycolor] at (3.85,-0.8) {共价键};
  \node[font=\tiny] at (3.85,-1.2) {(共享)};
  % 金属键
  \node[am] (m1) at (6.3,0.3) {+};
  \node[am] (m2) at (7.2,0.3) {+};
  \node[am] (m3) at (6.75,-0.4) {+};
  \node[font=\tiny,accentcolor] at (6.4,0) {e$^-$};
  \node[font=\tiny,accentcolor] at (7.0,-0.1) {e$^-$};
  \node[font=\scriptsize,primarycolor] at (6.75,-0.9) {金属键};
  \node[font=\tiny] at (6.75,-1.3) {(电子海)};
\end{tikzpicture}
\end{center}
```

\begin{itemize}
\item \textbf{离子键}:电负性差大,电子\textbf{完全转移}(Na 给 Cl)→ 正负离子静电吸引。\textbf{硬、脆、绝缘、高熔点}(NaCl, MgO)
\item \textbf{共价键}:电负性差小,电子\textbf{共享}→ 方向性强。\textbf{极硬、高熔点、多为绝缘或半导体}(金刚石, Si)
\item \textbf{金属键}:价电子\textbf{脱离原子,形成"电子海"}→ 正离子泡在自由电子里。\textbf{导电、导热、可塑、有金属光泽}(Cu, Fe, Al)
\end{itemize}

\textbf{还有两种"弱键"}:\textbf{范德华力}(分子间,如石墨层间、塑料)和\textbf{氢键}(水、DNA、尼龙)——
\textbf{弱键解释了为什么石墨软、为什么冰会浮}。

\section{4. 真正的数学}

\subsection{薛定谔方程与原子轨道}

电子的精确行为由\textbf{薛定谔方程}描述:
$$\hat{H}\psi = E\psi, \quad \hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(r)$$

对氢原子,$V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$(库仑势),\textbf{解出来的 $\psi$ 就是"原子轨道"}——
\textbf{s 轨道球形,p 轨道哑铃形,d 轨道四瓣形}。\textbf{$|\psi|^2$ 是电子出现的概率密度}。

\textbf{能量本征值}:
$$E_n = -\frac{m e^4}{8\epsilon_0^2 h^2} \cdot \frac{Z^2}{n^2} = -13.6 \cdot \frac{Z^2}{n^2} \text{ eV}$$

\textbf{这个 $-13.6$ eV 是从基本物理常数算出来的}——\textbf{量子力学最早的辉煌胜利之一}。

\subsection{屏蔽与有效核电荷}

\textbf{多电子原子里,内层电子"挡住"了部分核电荷}。外层电子感受到的不是全部 $Z$,而是\textbf{有效核电荷} $Z_{\text{eff}}$:
$$Z_{\text{eff}} = Z - \sigma$$
其中 $\sigma$ 是\textbf{屏蔽常数}(Slater 规则可估算)。

\textbf{这解释了周期性}:\textbf{同周期从左到右,$Z$ 增加但屏蔽几乎不变,$Z_{\text{eff}}$ 上升}→
\textbf{电子被拉得更紧 → 原子半径收缩、电离能升高}。

\subsection{电负性的定量}

\textbf{Pauling 电负性}衡量原子\textbf{吸引电子的能力}。键的\textbf{离子性百分比}:
$$\text{离子性} = \left(1 - e^{-0.25(\Delta\chi)^2}\right) \times 100\%$$

其中 $\Delta\chi$ 是两原子电负性之差。\textbf{$\Delta\chi > 1.7$ 通常算离子键,$< 0.4$ 算共价/金属键}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:同样是碳,金刚石和石墨为什么天差地别}

\textbf{金刚石和石墨都是纯碳(都是 C,2s$^2$2p$^2$)}——\textbf{成分完全一样}。
但:

\begin{longtable}{|l|l|l|}
\hline
\rowcolor{primarycolor!10}
\textbf{性质} & \textbf{金刚石} & \textbf{石墨} \\
\hline
硬度 & 最硬(莫氏 10) & 极软(莫氏 1-2,能写字) \\
导电 & 绝缘体 & 良导体(沿层方向) \\
外观 & 透明 & 黑色不透明 \\
用途 & 钻头/珠宝 & 铅笔芯/润滑剂/电极 \\
\hline
\end{longtable}

\textbf{差别全在键合方式}:
\begin{itemize}
\item \textbf{金刚石}:每个 C 与 4 个 C 形成\textbf{sp$^3$ 共价键},构成\textbf{三维网络}——\textbf{4 个价电子全用于成键,没有自由电子 → 绝缘 + 极硬}
\item \textbf{石墨}:每个 C 与 3 个 C 形成\textbf{sp$^2$ 共价键},构成\textbf{二维平面层},\textbf{第 4 个电子离域 → 层内导电};\textbf{层与层之间只有弱范德华力 → 容易滑动 → 软}
\end{itemize}

\begin{bluebox}
\textbf{这就是材料科学的核心命题}:\textbf{成分相同,结构不同,性能天差地别}。
\textbf{金刚石 vs 石墨——是"结构决定性能"最震撼的例子}。
\textbf{这个命题贯穿整本书}:从晶体结构到相变,从加工到失效,我们反复看到它。
\end{bluebox}

\subsection{用代码验证:键合判据}

运行配套模块 \texttt{atomic\_structure.py} 的键合分析:

\begin{verbatim}
材料            ΔEN    离子性%   类型
--------------------------------------------
NaCl 食盐       2.23   71.2%    离子键
MgO 氧化镁      2.13   67.8%    离子键
SiC 碳化硅      0.65   10.0%    极性共价键
Al2O3 刚玉      1.83   56.7%    离子键
金刚石 C-C      0.00    0.0%    共价键
Si-Si 硅        0.00    0.0%    共价键
\end{verbatim}

\textbf{Aha}:\textbf{仅凭电负性差,就能预测一个化合物是离子型还是共价型}——
\textbf{进而预测它脆不脆、导不导电、熔点高不高}。
\textbf{NaCl(71\% 离子性)→ 脆、绝缘、溶于水};\textbf{SiC(10\% 离子性)→ 硬、半导体、耐高温}。

\subsection{周期性:原子半径的收缩}

运行模块的周期性分析:

\begin{verbatim}
第二周期原子半径(pm):
  Li:167 Be:112 B:87 C:67 N:56 O:48 F:42 Ne:38
→ Li→Ne 半径缩小 77%
\end{verbatim}

\textbf{Aha}:\textbf{从 Li 到 Ne,电子都填在第二层,但核电荷从 3 涨到 10}——
\textbf{核把电子拉得越来越紧,原子越来越小}。\textbf{这个"周期性收缩"直接决定了
原子在晶体里怎么堆、堆多密}——\textbf{是后面晶体结构章节的基础}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料设计中}

\begin{itemize}
\item \textbf{合金设计}:Hume-Rothery 规则——\textbf{原子半径差 < 15\% 才容易固溶}(直接用本章的原子半径)
\item \textbf{半导体掺杂}:往 Si(4 价)里掺 P(5 价,多 1 电子)或 B(3 价,少 1 电子)——\textbf{n 型/p 型半导体的根源是价电子数}
\item \textbf{高熵合金}:5 种以上元素混合,\textbf{电负性差和原子半径差决定能否形成单相固溶体}
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\textbf{今天,电子结构可以直接用计算机算出来}:

\begin{itemize}
\item \textbf{密度泛函理论(DFT)}:解薛定谔方程的工程化版本,\textbf{算出任意材料的电子结构、能量、键合}——\textbf{现代材料计算的主力}
\item \textbf{Materials Project / AFLOW}:在线材料数据库,\textbf{几十万种材料的 DFT 计算结果免费查}
\item \textbf{机器学习势函数}:用神经网络拟合 DFT 能量,\textbf{快 $10^3-10^6$ 倍}(NequIP, MACE)
\item \textbf{CALPHAD}:用热力学模型描述相图,\textbf{Gibbs 自由能的最底层就是电子结合能}
\end{itemize}

\begin{bluebox}
\textbf{贯穿全书的现代视角}:每一章我们都会问——\textbf{"这件事,计算材料学怎么看?"}
\textbf{本章的电子排布、键合能},今天都能用 \textbf{DFT 精确算出}——
\textbf{从"经验规律"到"第一性原理预测",这是材料科学正在发生的革命}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么金子不生锈}:金的电子排布让它\textbf{化学惰性}——价电子不易失去
\item \textbf{为什么铜线导电}:金属键的\textbf{自由电子海}——施加电场,电子定向移动
\item \textbf{为什么玻璃透明}:无自由电子 + 带隙大于可见光能量——\textbf{光子穿过不被吸收}
\item \textbf{为什么铁磁、铝不磁}:Fe 的 \textbf{3d 轨道未成对电子}产生磁矩——铝没有
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:atomic\_structure.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{hydrogen\_energy\_level} & 类氢能级 $-13.6 Z^2/n^2$ + 玻尔半径 \\
\texttt{hydrogen\_spectrum} & Balmer 系谱线(656/486/434 nm 真实值)\\
\texttt{madelung\_order} & 自动生成轨道填充顺序 \\
\texttt{electron\_configuration} & 任意元素的电子排布(Fe = 3d$^6$)\\
\texttt{periodicity\_analysis} & 原子半径/电离能的周期性 \\
\texttt{bond\_type} & 电负性差 → 离子性百分比 → 键合类型 \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 atomic\_structure.py}——\textbf{纯 numpy,真实数据,无需联网}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(电子排布)} 用 \texttt{electron\_configuration} 查 Cu(Z=29)的排布。
它的实际排布是 3d$^{10}$4s$^1$ 而非 3d$^9$4s$^2$——\textbf{为什么?}(提示:全充满更稳定)

\item \textbf{(键合)} 用 \texttt{bond\_type} 算 GaAs(Ga=31, As=33)。它是什么键?
为什么 GaAs 是重要的半导体材料?

\item \textbf{(周期性)} 为什么第一电离能在 Be→B、N→O 处出现"反常下降"?
(提示:洪特规则 + 轨道半满/全满的稳定性)

\item \textbf{(综合)} 查 Mg(12)和 O(8)的电负性差,预测 MgO 的键型;
再查它的实际熔点(2852°C)——\textbf{为什么这么高?}

\item \textbf{(联动 DFT)} 上 Materials Project 网站,查一个你感兴趣的材料,
看它的电子态密度(DOS)图——\textbf{带隙为 0 是金属,带隙大是绝缘体}。
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Callister, \textit{Materials Science and Engineering}(材料科学圣经,第 2 章)
\item \textbf{深入物理}:Kittel, \textit{Introduction to Solid State Physics}
\item \textbf{化学键}:Pauling, \textit{The Nature of the Chemical Bond}(电负性概念的原始来源)
\item \textbf{计算视角}:Materials Project(materialsproject.org)免费查 DFT 数据
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲能带理论}(为什么有的材料导电有的不导电)——留给"电子性质"章节
\item \textbf{没讲杂化轨道的细节}(sp/sp$^2$/sp$^3$ 怎么形成)——化学课更深入
\item \textbf{没讲相对论效应}(为什么金是金色的、汞是液体)——进阶话题
\item \textbf{没讲原子核物理}(放射性、同位素应用)——本书聚焦电子
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:材料科学的因果链从\textbf{电子排布}开始。\textbf{四个量子数 + 三大填充规则}决定每个原子的电子排布;\textbf{最外层价电子}决定原子的化学和材料行为;\textbf{电负性差}决定三种键合(离子/共价/金属)中的哪一种。\textbf{核心 Aha:金刚石 vs 石墨——成分相同,键合不同,性能天差地别}——这就是贯穿全书的命题"\textbf{结构决定性能}"。\textbf{现代视角}:今天 DFT 能从第一性原理精确算出本章的一切,材料科学正从"经验"走向"预测"。\textbf{下一章}:原子如何周期性地堆叠成\textbf{晶体结构}。
\end{bluebox}

\begin{flushright}
\textit{第 1 章 · 原子结构与电子排布 · 完}
\end{flushright}
