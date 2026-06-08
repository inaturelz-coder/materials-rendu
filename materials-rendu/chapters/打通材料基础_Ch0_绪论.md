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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 0}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 绪论:材料科学是什么}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 怎么读这本书}\\[0.5em]
{\color{primarycolor!60} Introduction: What Is Materials Science}
\vspace{2em}
```

> "石器时代、青铜时代、铁器时代、硅时代——人类的文明史,
> 就是一部材料史。每一次材料的突破,都重塑了世界。
> 但材料科学这门学问,常常让初学者头疼:晶体、相图、扩散、位错、
> 热处理……一堆名词,彼此孤立,记了就忘。这本书想做一件事:
> \textbf{给你一根线,把它们全串起来}。"

\vspace{1.5em}

\section{材料科学是什么}

\textbf{材料科学研究的核心问题只有一个}:\textbf{为什么这种材料有这样的性能?
怎么让它有我想要的性能?}

\textbf{从一块铁到一把锋利的刀,从沙子到芯片,从石墨到金刚石}——\textbf{材料科学
要回答的是:成分、加工、内部结构、最终性能,这四者之间到底是什么关系}。

\subsection{材料科学四面体}

\textbf{这门学科的"中心法则",可以画成一个四面体}:

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1,
  v/.style={circle,draw=primarycolor,fill=primarycolor!12,minimum size=1.2cm,font=\small\bfseries,align=center}]
  \node[v] (comp) at (-2.8,2.2) {成分};
  \node[v] (proc) at (2.8,2.2) {工艺};
  \node[v,fill=mergecolor!20,draw=mergecolor] (micro) at (0,0.8) {组织};
  \node[v] (prop) at (0,-2.0) {性能};
  \draw[->,gray,thick] (comp) -- (micro);
  \draw[->,gray,thick] (proc) -- (micro);
  \draw[->,mergecolor,line width=1.8pt] (micro) -- (prop);
  \draw[gray!40,dashed] (comp) -- (proc);
  \draw[gray!40,dashed] (comp) to[bend right=40] (prop);
  \draw[gray!40,dashed] (proc) to[bend left=40] (prop);
  \node[font=\scriptsize,mergecolor] at (1.9,-0.8) {组织决定性能};
  \node[font=\scriptsize,gray] at (0,2.5) {你放什么 + 你怎么做};
\end{tikzpicture}
\end{center}
```

\begin{itemize}
\item \textbf{成分(Composition)}:材料里有哪些元素,各多少
\item \textbf{工艺(Processing)}:怎么加工、热处理、成型
\item \textbf{组织(Microstructure)}:原子和相在空间里如何排布(显微镜下的样子)
\item \textbf{性能(Property)}:强度、导电、磁性、耐腐蚀……
\end{itemize}

\textbf{关键洞察}:\textbf{成分和工艺不直接决定性能,而是先共同决定"组织",组织再决定性能}。
\textbf{组织是中心枢纽}。\textbf{这就是为什么同样成分的钢,通过不同热处理(工艺),
能得到软硬天差地别的性能——因为工艺改变了组织}(这本书 Ch11 的高潮)。

\section{这本书的方法:一静一动}

\textbf{传统材料教材的最大问题是"知识零散"}:晶体结构、相图、扩散、位错、热处理……
\textbf{每一章都讲一堆,但章与章之间像孤岛,学生记不住、串不起}。

\textbf{这本书用一根线把它们穿起来}——\textbf{一静一动}:

\begin{center}
\begin{tikzpicture}[scale=1.0,
  s/.style={rectangle,draw=staticcolor,fill=staticcolor!12,rounded corners=2pt,minimum width=5cm,minimum height=0.9cm,font=\small,align=center},
  d/.style={rectangle,draw=dynamiccolor,fill=dynamiccolor!12,rounded corners=2pt,minimum width=5cm,minimum height=0.9cm,font=\small,align=center}]
  \node[s] at (0,1.2) {\textbf{静(任脉)}\\平衡热力学 + 晶体结构\\\scriptsize「平衡态是什么样」};
  \node[d] at (0,-0.5) {\textbf{动(督脉)}\\动力学 + 缺陷运动\\\scriptsize「怎么到达、为什么到不了」};
\end{tikzpicture}
\end{center}

\begin{itemize}
\item \textbf{静(任脉)}:\textbf{平衡态是什么样}。原子怎么排成晶体、有什么缺陷、形成什么组织、
热力学上"应该"形成什么相。\textbf{这是材料的"地图"——它告诉你终点在哪}。
\item \textbf{动(督脉)}:\textbf{怎么到达那个终点}。原子怎么扩散、相变怎么发生、位错怎么运动、
材料怎么从一个状态走到另一个。\textbf{这是材料的"路径"——它告诉你怎么走、走多快、能不能到}。
\end{itemize}

\textbf{为什么这根线管用}?——\textbf{因为它对应日常直觉}:\textbf{水往低处流(静:终点是最低处),
但流多快、走哪条沟,要看坡度和阻力(动:过程)}。\textbf{材料也一样:热力学告诉你"该去哪",
动力学告诉你"怎么去"}。

\begin{bluebox}
\textbf{有了这根线,每学一个新概念,你都可以问自己三个问题}:

\textbf{1. 它是"静"(平衡、结构)还是"动"(过程、演化)?}

\textbf{2. 它和对面那条脉的哪个概念"对仗"?}(比如:缺陷的几何 ↔ 缺陷的运动)

\textbf{3. 它怎么影响最终性能?}(回到四面体)

\textbf{一旦这根线在脑子里立起来,材料基础就从"背一堆孤立名词"变成"看一张有结构的网"}。
\end{bluebox}

\section{贯穿全书的四条线}

\textbf{除了"一静一动"这条主轴,这本书还有三条线贯穿始终}:

\subsection{主旋律:结构决定性能}

\textbf{材料科学最核心的命题}:\textbf{成分相同,结构不同,性能可以天差地别}。
\textbf{最震撼的例子是金刚石 vs 石墨}(Ch1):\textbf{都是纯碳,一个最硬、一个最软,
只因原子键合方式不同}。\textbf{这个命题在全书反复出现}:从晶体结构到相变,从热处理到失效。

\subsection{暗线一:多尺度计算}

\textbf{现代材料科学已经能用计算机"算"材料}。\textbf{这本书埋了一条计算暗线,贯穿三个尺度}:

\begin{center}
\begin{tikzpicture}[scale=0.95,
  b/.style={rectangle,draw=primarycolor,fill=primarycolor!8,rounded corners=2pt,minimum width=3.2cm,minimum height=0.85cm,font=\scriptsize,align=center}]
  \node[b] (a) at (0,0) {\textbf{原子尺度}\\DFT / MD / MLIP\\\scriptsize Ch14};
  \node[b] (m) at (4,0) {\textbf{微观尺度}\\CALPHAD / 相场\\\scriptsize Ch7 / Ch12};
  \node[b] (M) at (8,0) {\textbf{宏观尺度}\\有限元 FEM\\\scriptsize Ch13};
  \draw[->,mergecolor,thick] (a) -- (m);
  \draw[->,mergecolor,thick] (m) -- (M);
\end{tikzpicture}
\end{center}

\textbf{从电子(DFT)到组织(相场)到构件(FEM)}——\textbf{这是材料科学正在经历的"计算革命",
也是本书区别于传统教材的地方}。

\subsection{暗线二:怎么看见它}

\textbf{材料的结构肉眼看不见——怎么"看见"原子排列、晶粒、缺陷、相?}\textbf{这本书
不把表征手段堆在一章死记,而是让它"跟着内容走"}:\textbf{每一章讲完一个对象,
就有一节"怎么看见它",讲透对应的表征手段}(XRD、TEM、金相、DSC、EBSD、ARPES……)。
\textbf{最后用附录 C 系统总收口}。

\section{怎么读这本书}

\subsection{全书地图}

\textbf{15 章分三大部分}:

\begin{itemize}
\item \textbf{☯ 任脉·静(Ch1-7)}:原子 → 晶体 → 缺陷 → 组织 → 热力学 → 相图 → CALPHAD
\item \textbf{☯ 督脉·动(Ch8-12)}:扩散 → 相变动力学 → 位错塑性 → 热处理 → 相场
\item \textbf{☯ 任督交汇(Ch13-15)}:力学+FEM → 电磁热+DFT → 失效与寿命
\end{itemize}

\subsection{每章的结构(7 件套)}

\textbf{每一章都按同样的节奏展开,帮你建立稳定的阅读预期}:

\begin{longtable}{|l|p{0.62\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{节} & \textbf{作用} \\
\hline
1. 一句话本质 & 三句话记住这一章 \\
2. 教科书里你看到的 & 标准概念(和别的教材对接)\\
3. 但其实是什么意思 & 直觉、图像、深层理解 \\
4. 真正的数学 & 关键公式与推导 \\
5. 一个让人 Aha 的例子 & 真实数据 + 「怎么看见它」表征专节 \\
6. 这玩意儿现在在哪 & 工程应用 + 计算材料学现代视角 \\
7. 让代码告诉你 & 配套 Python 模块 + 思考题 + 延伸阅读 \\
\hline
\end{longtable}

\subsection{给不同读者的建议}

\begin{itemize}
\item \textbf{跨专业入门者(物理/化学/机械转材料)}:按顺序读,重点看 §1、§3、§5。
\textbf{§4 的数学可以先跳过,回头再补}。
\item \textbf{材料专业学生}:用"一静一动"重新组织你已学的零散知识。\textbf{特别注意四组静动对仗}。
\item \textbf{想动手的人}:每章配套代码可独立运行(纯 numpy/scipy),\textbf{跑一遍代码,
比读十遍公式管用}。
\item \textbf{对计算材料学感兴趣}:留意每章 §6 的"计算材料学视角"和两条计算暗线。
\end{itemize}

\subsection{配套代码}

\textbf{这本书每章配一个 Python 模块,用真实材料数据演示核心概念}。\textbf{它们不是玩具}:
\textbf{从晶体结构算密度(误差<0.3\%)、用焓熵算冰的熔点、模拟调幅分解、一维有限元……
都是真实可跑的}。\textbf{强烈建议边读边跑}。

\begin{bluebox}
\textbf{最后一句}:这本书不追求大而全(那是 Callister 千页教科书的事)。\textbf{它追求的是
"通"——让你理解材料科学的内在逻辑,把零散知识连成网}。\textbf{读完它,你再去读厚厚的
专业教材,会发现一切都有了位置}。\textbf{这就是"打通任督二脉"的意思}。

\vspace{0.3em}

\textbf{现在,让我们从最底层开始——单个原子的电子排布(Ch1)}。
\end{bluebox}

\begin{flushright}
\textit{第 0 章 · 绪论 · 完}
\end{flushright}
