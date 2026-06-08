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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 8}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 扩散:原子怎么搬家}\\[0.3em]
{\color{dynamiccolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{dynamiccolor!85} 督脉开篇 · 从"静"到"动"}\\[0.5em]
{\color{primarycolor!60} Diffusion: How Atoms Move}
\vspace{2em}
```

> "任脉七章告诉我们材料的'平衡态'——相图说该形成什么相。
> 但有个问题被我们一直回避:材料\textbf{怎么}从一个状态'走'到另一个?
> 钢里的碳怎么跑到表面?合金怎么均匀化?答案是\textbf{扩散}——
> 原子借助空位,一步一步地跳。\textbf{这是'动'的起点,
> 整个督脉从这里展开}。"

\vspace{2em}

\begin{bluebox}
\textbf{这是督脉(动)的开篇,全书从"静"转"动"的转折点}。

\textbf{任脉(静)回答"平衡态是什么样"};\textbf{督脉(动)回答"怎么到达、多久到、走哪条路"}。
\textbf{扩散是一切动力学过程的基础}:\textbf{相变(Ch9)、位错攀移(Ch10)、热处理(Ch11)、
蠕变、烧结、渗碳——全靠原子扩散}。\textbf{它直接承接 Ch3 的空位}:
\textbf{扩散需要空位作"载体",原子才能跳}。\textbf{懂了扩散,才算踏进"动"的门}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{扩散 = 原子在固体里的随机跳跃,宏观表现为"从浓处流向稀处"}。
\textbf{原子不会凭空移动——它需要旁边有个空位(Ch3),才能跳过去}。

\vspace{0.3em}

\textbf{三句话记住这一章}:

\textbf{1. Fick 定律}:扩散通量正比于浓度梯度($J = -D\,\partial C/\partial x$);
浓度随时间的变化由扩散方程描述。

\textbf{2. 扩散系数 $D$ 对温度指数敏感}:$D = D_0 e^{-Q/RT}$(Arrhenius)——\textbf{高温扩散快得多}。

\textbf{3. 扩散距离 $\sim \sqrt{Dt}$}:\textbf{要扩散到 2 倍深,需要 4 倍时间}(平方根定律)。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{钢渗碳 10 小时,碳的浓度分布是一条误差函数曲线,渗碳层 0.89 mm}
(齿轮表面硬、芯部韧);\textbf{温度从 727 到 1127°C,扩散系数暴增 162 倍};
\textbf{扩散激活能 = 空位形成能 + 迁移能——直接连接 Ch3 的空位浓度}。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{Fick 两定律}

\begin{itemize}
\item \textbf{Fick 第一定律(稳态)}:$J = -D\dfrac{\partial C}{\partial x}$——\textbf{通量正比于浓度梯度}(负号:从高到低)
\item \textbf{Fick 第二定律(非稳态)}:$\dfrac{\partial C}{\partial t} = D\dfrac{\partial^2 C}{\partial x^2}$——\textbf{浓度随时间的演化}
\end{itemize}

\subsection{扩散机制}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{机制} & \textbf{说明} \\
\hline
空位机制 & 原子跳进相邻空位(置换原子、自扩散)——\textbf{需要空位} \\
间隙机制 & 小原子(C、N、H)在间隙位跳跃——\textbf{快,不需空位} \\
晶界/表面扩散 & 沿缺陷的快速通道——\textbf{比体扩散快几个数量级} \\
\hline
\end{longtable}

\subsection{扩散系数的 Arrhenius 形式}

$$D = D_0 \exp\left(-\frac{Q}{RT}\right)$$

\textbf{$D_0$ 是指前因子,$Q$ 是激活能}。\textbf{在 $\ln D$ vs $1/T$ 图上是直线,斜率给出 $Q$}。

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{扩散激活能为什么 = 空位形成能 + 迁移能}(连接 Ch3)
\item \textbf{为什么扩散距离是 $\sqrt{t}$ 而不是 $t$}(随机行走的统计本质)
\item \textbf{Kirkendall 效应如何证明了空位机制}(标记物移动 + 孔洞)
\item \textbf{扩散方程和热传导、相场方程是同一个方程}(为 Ch12 铺垫)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{扩散是"喝醉的原子"随机走}

\textbf{微观上,扩散不是原子"知道"要往稀处走}。\textbf{每个原子只是随机地、无方向地跳}——
\textbf{但因为浓处原子多、跳出来的多,宏观上就表现为"从浓流向稀"}。

\textbf{这是随机行走(random walk)}。\textbf{随机行走的关键结论}:\textbf{$N$ 步之后,
平均位移正比于 $\sqrt{N}$,不是 $N$}。\textbf{这就是为什么扩散距离 $\sim\sqrt{Dt}$}——
\textbf{原子走得磕磕绊绊,进三步退两步,效率低}。

\subsection{为什么需要空位:连接 Ch3}

\textbf{置换原子要扩散,必须旁边有空位才能跳过去}。\textbf{所以扩散分两步}:
\begin{enumerate}
\item \textbf{形成空位}:需要能量 $Q_f$(Ch3 讲过,空位浓度 $\propto e^{-Q_f/kT}$)
\item \textbf{原子跳进空位}:需要越过能垒 $Q_m$(迁移能)
\end{enumerate}

\textbf{所以扩散激活能 $Q = Q_f + Q_m$}——\textbf{这就是 Arrhenius 里那个 $Q$ 的物理来源}。
\textbf{Ch3 的空位浓度,在这里变成了扩散的"前提"}——\textbf{静(空位的存在)驱动动(扩散)}。

\textbf{间隙原子(碳、氮)例外}:\textbf{它们小,直接在间隙位跳,不需要空位}——\textbf{所以扩散快得多}。
\textbf{这就是钢能"渗碳"(碳快速渗入)但"渗铁"几乎不可能的原因}。

\subsection{Arrhenius:为什么高温扩散快}

\textbf{$D = D_0 e^{-Q/RT}$ 的指数形式意味着扩散对温度极度敏感}。\textbf{温度升高,
两件事同时变快}:\textbf{空位更多(Ch3)+ 原子跳得更勤}。\textbf{两个指数相乘,
扩散系数暴涨}。

\textbf{这就是为什么所有扩散控制的工艺都要加热}:\textbf{渗碳要 900°C+、退火要高温、
烧结要接近熔点}。\textbf{室温下原子几乎不动(铁器埋千年成分基本不变),
高温下原子活蹦乱跳}。

\subsection{根号Dt:扩散的标度律}

\textbf{扩散距离 $x \sim \sqrt{Dt}$ 是一条深刻的标度律}。\textbf{它意味着}:
\begin{itemize}
\item \textbf{扩散初期快,后期慢}(梯度变平缓)
\item \textbf{要扩散到 2 倍深度,需要 4 倍时间}
\item \textbf{要扩散到 10 倍深度,需要 100 倍时间}
\end{itemize}

\textbf{这解释了很多现象}:\textbf{为什么渗碳层做厚很费时间、为什么大铸件均匀化要很久、
为什么纳米材料(扩散距离短)烧结快}。

\section{4. 真正的数学}

\subsection{Fick 第二定律的推导}

\textbf{质量守恒 + Fick 第一定律}:
$$\frac{\partial C}{\partial t} = -\frac{\partial J}{\partial x} = \frac{\partial}{\partial x}\left(D\frac{\partial C}{\partial x}\right) = D\frac{\partial^2 C}{\partial x^2}$$
(末步假设 $D$ 不随位置变)。\textbf{这就是扩散方程——和热传导方程、相场方程同一个数学形式}。

\subsection{误差函数解(半无限固体)}

\textbf{表面浓度恒定 $C_s$、初始浓度 $C_0$ 的半无限固体(渗碳)},解为:
$$\frac{C(x,t) - C_s}{C_0 - C_s} = \mathrm{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

\textbf{$\mathrm{erf}$ 是误差函数}。\textbf{注意特征长度 $2\sqrt{Dt}$——又是 $\sqrt{Dt}$ 标度}。

\subsection{随机行走与 根号Dt}

\textbf{原子每跳一步长 $a$,跳 $N$ 次}。\textbf{随机行走的均方位移}:
$$\langle x^2 \rangle = N a^2 \quad\Rightarrow\quad \sqrt{\langle x^2\rangle} = a\sqrt{N} \sim \sqrt{Dt}$$

\textbf{因为 $D \sim a^2 \Gamma$($\Gamma$ 跳跃频率),$N = \Gamma t$}。\textbf{$\sqrt{Dt}$ 的根源
就是随机行走的统计}。

\subsection{扩散系数的微观表达}

$$D = D_0 \exp\left(-\frac{Q_f + Q_m}{RT}\right)$$

\textbf{$Q_f$ 空位形成能(Ch3),$Q_m$ 迁移能}。\textbf{对间隙扩散,无 $Q_f$ 项(不需要空位),
所以 $Q$ 小、扩散快}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:钢渗碳的误差函数曲线}

运行配套模块 \texttt{diffusion.py}:

\begin{verbatim}
齿轮表面渗碳:927°C,表面碳1.0%,基体0.2%
扩散系数 D = 8.318e-12 m²/s
深度(mm)   碳浓度(%)
0.0        1.000
0.2        0.837
0.5        0.615
1.0        0.357
2.0        0.208
→ 渗碳10小时,碳降到0.4%的深度 = 0.89 mm
\end{verbatim}

\textbf{Aha}:\textbf{齿轮渗碳,碳从表面往里的浓度分布,精确地是一条误差函数曲线}。
\textbf{表面高碳(硬、耐磨),芯部低碳(韧、抗冲击)——这正是齿轮想要的}:
\textbf{硬壳 + 韧芯}。\textbf{Fick 第二定律 + 误差函数,定量预测了渗碳层深度}——
\textbf{热处理工程师就是用这个公式设计渗碳工艺的}。

\subsection{Arrhenius:温度的指数威力}

\begin{verbatim}
碳在 γ-Fe 中扩散系数:
727°C:  4.28e-13 m²/s
927°C:  8.32e-12 m²/s
1127°C: 6.92e-11 m²/s
→ 727→1127°C,扩散系数增大 162 倍
\end{verbatim}

\textbf{Aha}:\textbf{温度从 727 升到 1127°C(才 400 度),扩散系数暴增 162 倍}。
\textbf{这就是 Arrhenius 指数的威力}——\textbf{扩散对温度极度敏感}。\textbf{所以渗碳、退火、
烧结都要高温:不是为了"熔化",而是为了让原子"跑得动"}。

\subsection{根号 t 标度律}

\begin{verbatim}
时间(h)   √t    扩散距离(mm)
1        1.00   0.173
4        2.00   0.346
9        3.00   0.519
16       4.00   0.692
25       5.00   0.865
\end{verbatim}

\textbf{Aha}:\textbf{扩散距离严格正比于 $\sqrt{t}$}——\textbf{时间变 4 倍(1→4h),距离才变 2 倍}。
\textbf{这个平方根定律支配所有扩散控制过程}:\textbf{渗碳层加厚一倍要 4 倍时间,
大铸件均匀化极其耗时,而纳米尺度扩散瞬间完成}(为什么纳米材料烧结快、易长大)。

\subsection{怎么看见它:扩散偶与浓度剖面}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{扩散的"证据"靠测浓度剖面——经典方法是"扩散偶"实验}。
\end{bluebox}

\textbf{扩散偶(diffusion couple)}:\textbf{把两块不同成分(或不同材料)的金属紧密贴合,
高温保温,让原子互相扩散},然后\textbf{切开,沿界面测成分剖面}。

\begin{itemize}
\item \textbf{EPMA(电子探针)/ SEM-EDS}:沿扩散方向逐点测成分——\textbf{得到浓度-距离曲线}
\item \textbf{拟合误差函数}:从浓度剖面反推扩散系数 $D$(Boltzmann-Matano 法)
\item \textbf{Kirkendall 标记}:在界面放惰性标记物(如 Mo 丝),\textbf{看它移动}——证明两种原子扩散速率不同
\end{itemize}

\textbf{Kirkendall 效应的历史意义}:\textbf{1947 年 Kirkendall 发现扩散偶里的标记物会移动,
还产生孔洞}——\textbf{证明了"空位机制"(原子借空位跳,净空位流导致界面移动),
推翻了当时"原子直接换位"的旧理论}。\textbf{能测什么}:互扩散系数、本征扩散系数、
扩散激活能(测不同温度的 $D$,Arrhenius 拟合)。\textbf{局限}:需要高温长时间实验、
成分剖面测量精度要求高、晶界扩散会干扰体扩散测量。

\textbf{现代视角}:\textbf{DICTRA(基于 CALPHAD 的扩散模拟)把热力学(Ch7)和动力学结合,
计算多元扩散}——\textbf{你的 CALPHAD 工作可以延伸到动力学数据库}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{表面硬化}:渗碳、渗氮——表面硬芯部韧
\item \textbf{均匀化退火}:消除铸件的成分偏析(Ch6 埋的伏笔)
\item \textbf{烧结}:粉末冶金、陶瓷致密化靠扩散
\item \textbf{半导体掺杂}:杂质扩散进硅(虽然现在多用离子注入)
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{DICTRA}:CALPHAD + 扩散,算多元扩散问题
\item \textbf{相场(Ch12)}:扩散方程是相场模拟的核心组成
\item \textbf{第一性原理算扩散}:DFT + 过渡态理论(NEB)算迁移能 $Q_m$
\item \textbf{分子动力学(Ch14)}:直接模拟原子跳跃,算扩散系数
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看扩散}:本章的扩散方程,\textbf{是相场模拟(Ch12)的数学核心};
\textbf{扩散系数 $D$ 可以用 DFT + NEB 从第一性原理算出迁移能,或用 MD 直接模拟}。
\textbf{DICTRA 把 CALPHAD(Ch7,热力学)和扩散(动力学)结合}——\textbf{热力学给"驱动力",
扩散给"速率"}。\textbf{这正是"一静一动"的具体结合:CALPHAD(静)+ 扩散(动)= 完整的演化预测}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{为什么铁器埋千年成分基本不变}:室温扩散极慢($\sqrt{Dt}$,$D$ 极小)
\item \textbf{为什么炒菜放盐会均匀}:液体中扩散 + 对流
\item \textbf{为什么旧电子产品焊点会失效}:金属间化合物层随时间扩散长大
\item \textbf{为什么食物冷冻保鲜}:低温抑制扩散(化学反应、微生物代谢都慢)
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:diffusion.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{carburizing} & 钢渗碳的误差函数解 \\
\texttt{case\_depth} & 渗碳层深度计算 \\
\texttt{diffusion\_coefficient} & Arrhenius $D = D_0 e^{-Q/RT}$ \\
\texttt{scaling\_demo} & 扩散距离 $\sqrt{Dt}$ 标度律 \\
\texttt{vacancy\_diffusion\_link} & 空位机制(连接 Ch3)\\
\texttt{solve\_diffusion\_1d} & 有限差分数值解(为 Ch12 铺垫)\\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 diffusion.py}——\textbf{numpy + scipy,真实扩散数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(渗碳)} 用 \texttt{case\_depth} 算:要把渗碳层从 0.89 mm 加深到 1.78 mm(2 倍),
需要多少小时?(提示:$\sqrt{t}$ 定律,答案是 40h 不是 20h)

\item \textbf{(Arrhenius)} 为什么间隙扩散(碳)比置换扩散(铁自扩散)快得多?
从激活能 $Q = Q_f + Q_m$ 的角度解释。

\item \textbf{(标度律)} 一个铸件均匀化需要原子扩散 1 cm。
若实验室小样品只需扩散 1 mm,时间差多少倍?

\item \textbf{(Kirkendall)} 为什么 Kirkendall 标记物移动 + 孔洞,
证明了空位机制而非"原子直接换位"?

\item \textbf{(数值解)} 用 \texttt{solve\_diffusion\_1d},为什么时间步长 $dt$ 必须
小于 $dx^2/(2D)$?(提示:显式格式的稳定性——这是 Ch12 相场也要面对的问题)
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Shewmon, \textit{Diffusion in Solids}(扩散圣经)
\item \textbf{材料基础}:Callister, \textit{Materials Science and Engineering}(扩散章)
\item \textbf{相变中的扩散}:Porter \& Easterling, \textit{Phase Transformations}
\item \textbf{计算工具}:DICTRA(Thermo-Calc 的扩散模块)
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲多元扩散}(扩散矩阵、上坡扩散)——DICTRA 展开
\item \textbf{没讲晶界/位错的快速扩散通道细节}——进阶话题
\item \textbf{没讲离子晶体的扩散}(缺陷化学、Kröger-Vink)——陶瓷专题
\item \textbf{没讲扩散驱动的具体相变}(怎么形核长大)——下一章 Ch9
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:扩散 = 原子借空位的随机跳跃,宏观表现为从浓流向稀。\textbf{Fick 定律}:通量正比于浓度梯度,浓度演化由扩散方程描述。\textbf{扩散系数 $D = D_0 e^{-Q/RT}$ 对温度指数敏感}(727→1127°C 增大 162 倍)。\textbf{扩散距离 $\sim\sqrt{Dt}$}(2 倍深要 4 倍时间)。\textbf{核心 Aha:钢渗碳的误差函数曲线}(表面硬芯部韧);\textbf{扩散激活能 = 空位形成能 + 迁移能,直接连接 Ch3}。\textbf{怎么看见它:扩散偶 + 浓度剖面,Kirkendall 效应证明了空位机制}。\textbf{扩散方程 = 相场方程(Ch12)= 热传导方程,同一个数学}。\textbf{这是督脉"动"的起点——材料如何走向平衡。下一章}:扩散驱动的相变怎么发生——\textbf{相变动力学:形核与长大}。
\end{bluebox}

\begin{flushright}
\textit{第 8 章 · 扩散:原子怎么搬家 · 督脉开篇 · 完}
\end{flushright}
