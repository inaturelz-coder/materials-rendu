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
{\fontsize{56}{56}\selectfont\bfseries\color{goldcolor!60} 4}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 微观组织:从缺陷到组织}\\[0.3em]
{\color{goldcolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{primarycolor!75} 连接结构与性能的桥}\\[0.5em]
{\color{primarycolor!60} Microstructure: From Defects to Organization}
\vspace{2em}
```

> "原子、晶体、缺陷——前三章讲的都是'微观'。性能——是'宏观'。
> 中间隔着一道鸿沟。\textbf{填这道鸿沟的,就是'微观组织'}:
> 晶粒怎么排、第二相怎么分布、相界怎么织成网。
> \textbf{材料工程师天天打交道的不是原子,而是组织}——
> 一张金相照片,藏着材料的全部身世。"

\vspace{2em}

\begin{bluebox}
\textbf{这是任脉(静)的第四章,也是全书一个枢纽}。前三章(原子→晶体→缺陷)
讲的是\textbf{微观结构};这一章讲\textbf{这些结构在空间里如何组织起来——微观组织}。

\textbf{为什么单设一章}:材料科学的核心是\textbf{"成分-工艺-组织-性能"四面体}。
\textbf{组织是中心顶点}——\textbf{成分和工艺通过"组织"来决定性能}。\textbf{不懂组织,
就抓不住材料科学的命门}。\textbf{这一章把"组织"这个顶点讲实、讲到可定量}。
\end{bluebox}

\section{1. 一句话本质}

\begin{bluebox}
\textbf{微观组织 = 晶粒、相、缺陷在空间里的排布方式}。\textbf{它的尺度介于
"原子"(0.1 nm)和"宏观构件"(mm-m)之间}——\textbf{是肉眼看不见、但显微镜能看见的那一层}。

\vspace{0.3em}

\textbf{材料科学的核心方程(四面体)}:\textbf{成分 + 工艺 → 组织 → 性能}。
\textbf{成分和工艺不直接决定性能,而是先决定"组织",组织再决定性能}。

\vspace{0.3em}

\textbf{组织可以定量}:\textbf{晶粒尺寸}(ASTM 等级)、\textbf{相比例}(杠杆定律)、
\textbf{第二相体积分数}(体视学)、\textbf{组织取向}(织构)——\textbf{这些定量参数直接进入性能公式}。

\vspace{0.3em}

\textbf{实测核心 Aha}:\textbf{同样的成分,只改组织(工艺),屈服强度能差 83\%}
(粗晶无第二相 52 MPa → 超细晶 + 15\% 第二相 96 MPa);
\textbf{切开一个 2D 截面,竟能推断 3D 组织}(Delesse 原理:面积分数 = 体积分数)。
\end{bluebox}

\section{2. 教科书里你看到的}

\subsection{材料科学四面体}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0,
  v/.style={circle,draw=primarycolor,fill=primarycolor!12,minimum size=1.1cm,font=\small\bfseries,align=center}]
  \node[v] (comp) at (-2.5,2) {成分};
  \node[v] (proc) at (2.5,2) {工艺};
  \node[v,fill=mergecolor!20,draw=mergecolor] (micro) at (0,0.5) {组织};
  \node[v] (prop) at (0,-1.8) {性能};
  \draw[->,gray,thick] (comp) -- (micro);
  \draw[->,gray,thick] (proc) -- (micro);
  \draw[->,mergecolor,line width=1.5pt] (micro) -- (prop);
  \draw[gray!40,dashed] (comp) -- (proc);
  \draw[gray!40,dashed] (comp) -- (prop);
  \draw[gray!40,dashed] (proc) -- (prop);
  \node[font=\scriptsize,mergecolor] at (1.7,-0.7) {组织决定性能};
\end{tikzpicture}
\end{center}
```

\textbf{这是材料科学的"中心法则"}:\textbf{成分(你放了什么元素)+ 工艺(你怎么加工热处理)
→ 共同决定组织 → 组织决定性能}。\textbf{改变任一顶点,沿着箭头传播,最终改变性能}。

\subsection{组织的层次}

\begin{longtable}{|l|l|p{0.4\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{组织单元} & \textbf{尺度} & \textbf{影响} \\
\hline
晶粒 & µm-mm & 强度(Hall-Petch)、各向同性 \\
晶界网络 & nm 厚 & 强度、腐蚀、断裂路径 \\
第二相/析出物 & nm-µm & 析出强化、韧性 \\
共晶/共析层片 & µm & 层片间距决定强度 \\
马氏体板条/孪晶 & nm-µm & 高强度(钢的淬火组织)\\
织构(取向分布) & — & 各向异性(深冲性能)\\
\hline
\end{longtable}

\subsection{定量金相的基本量}

\begin{itemize}
\item \textbf{晶粒度}:ASTM 等级 $G$,$N = 2^{G-1}$ 个晶粒/in²(100×)
\item \textbf{相比例}:各相的体积分数(杠杆定律算,体视学测)
\item \textbf{晶粒尺寸}:截线法、面积法测量
\item \textbf{相间距}:共晶层片间距、析出相平均间距
\end{itemize}

\subsection{教科书不讲的事}

\begin{itemize}
\item \textbf{为什么 2D 截面能推 3D 组织}(Delesse 原理的深刻性)
\item \textbf{为什么同成分能有完全不同的组织}(组织是工艺的产物,不只是成分)
\item \textbf{组织参数如何定量进入性能公式}(不是定性"细晶好",而是算出 MPa)
\item \textbf{为什么金相制样是门"手艺"}(磨抛腐蚀的每一步都影响你看到什么)
\end{itemize}

\section{3. 但其实是什么意思}

\subsection{组织:材料的"身世照片"}

\textbf{一块金属的组织,记录了它的全部加工历史}。\textbf{看一张金相照片,有经验的人能读出}:

\begin{itemize}
\item \textbf{晶粒大小}→ 经历过什么温度、保温多久(晶粒长大动力学)
\item \textbf{晶粒形状}→ 是铸态(柱状晶)、变形态(纤维状)还是再结晶(等轴晶)
\item \textbf{第二相形态}→ 冷却快慢(片状珠光体 vs 球状珠光体)
\item \textbf{有无马氏体}→ 是否淬过火
\end{itemize}

\textbf{组织是"成分 + 工艺"的指纹}——\textbf{这就是为什么失效分析第一步永远是"切开看组织"}。

\subsection{同样的成分,不同的组织}

\textbf{这是材料科学最反直觉、也最强大的地方}:\textbf{成分完全相同的钢,
通过不同热处理,可以得到强度差几倍的组织}。

\textbf{以共析钢(0.8\% C)为例}:
\begin{itemize}
\item \textbf{缓冷}→ 粗珠光体(软,$\sim$200 HB)
\item \textbf{较快冷}→ 细珠光体(中等)
\item \textbf{更快冷}→ 贝氏体(较硬)
\item \textbf{淬火}→ 马氏体(极硬,$\sim$700 HB)
\end{itemize}

\textbf{同一块钢,硬度能差 3 倍以上}——\textbf{差别全在组织,而组织由工艺(冷速)决定}。
\textbf{这就是热处理的威力(Ch11 详讲),也是"组织决定性能"最有力的证据}。

\subsection{杠杆定律:组织里有多少各相}

\textbf{两相组织里,每种相占多少}?——\textbf{杠杆定律}给出答案。
在两相区,合金成分 $c_0$ 介于 $\alpha$ 相成分 $c_\alpha$ 和 $\beta$ 相成分 $c_\beta$ 之间:

$$f_\alpha = \frac{c_\beta - c_0}{c_\beta - c_\alpha}, \quad f_\beta = \frac{c_0 - c_\alpha}{c_\beta - c_\alpha}$$

\textbf{像一个杠杆}:成分点是支点,两端是两相成分,\textbf{相分数与"对臂长度"成正比}。
\textbf{这把"成分"(相图)和"组织"(相比例)直接连起来}——\textbf{是 Ch6 相图的核心工具,本章先用起来}。

\subsection{体视学:2D 看 3D 的魔法}

\textbf{我们只能切开材料看一个 2D 截面,但材料是 3D 的}。\textbf{怎么从截面推断三维组织}?

\textbf{Delesse 原理(1847)}:\textbf{在随机截面上,某相的面积分数 = 它的三维体积分数}。
$$A_A = V_V$$

\textbf{这个看似简单的等式极其深刻}——\textbf{它让我们用一张照片(2D)定量推断整块材料(3D)}。
\textbf{现代体视学(stereology)在此基础上,还能从 2D 推断 3D 的表面积、晶粒尺寸分布、连通性}。
\textbf{你拍一张金相照,就能定量整块材料的组织}。

\section{4. 真正的数学}

\subsection{ASTM 晶粒度}

$$N = 2^{G-1} \text{ 个晶粒/in}^2 \text{ (在 100× 下)}$$

\textbf{$G$ 越大,晶粒越小、越细}。换算到实际尺寸:$G=7$ 约对应 32 µm,$G=10$ 约 11 µm。
\textbf{工业钢材常控制在 $G=7$-$9$(细晶,兼顾强度与韧性)}。

\subsection{组织-性能的定量模型}

把组织参数代入性能公式(以屈服强度为例):
$$\sigma_y = \sigma_0 + \underbrace{\frac{k_y}{\sqrt{d}}}_{\text{Hall-Petch}} + \underbrace{k_p \cdot f}_{\text{第二相}}$$

其中 $d$ 晶粒尺寸,$f$ 第二相体积分数。\textbf{这是"组织 → 性能"的定量桥梁}——
\textbf{给定组织参数,算出强度}。\textbf{下一节的 Aha 用它做组织设计}。

\subsection{截线法测晶粒尺寸}

\textbf{在金相照片上画一条已知长度 $L$ 的线,数它穿过的晶界数 $P$}:
$$\bar{\ell} = \frac{L}{P} \quad(\text{平均截距}), \quad d \approx 1.5\,\bar{\ell}$$

\textbf{简单、快速、标准化}——\textbf{这是定量金相最常用的测量方法}。

\section{5. 一个让人 "Aha" 的例子}

\subsection{核心 Aha:同成分,改组织,强度差 83\%}

运行配套模块 \texttt{microstructure.py} 的组织设计:

\begin{verbatim}
组织设计              晶粒µm   第二相   强度MPa
粗晶+无第二相          100     0.00      52
细晶+无第二相           10     0.00      57
粗晶+10%第二相         100     0.10      72
细晶+10%第二相          10     0.10      77
超细晶+15%第二相         2     0.15      96
\end{verbatim}

\textbf{Aha}:\textbf{成分完全没变,只通过工艺改变组织(晶粒尺寸 + 第二相),
屈服强度从 52 提升到 96 MPa,提升 83\%}。\textbf{这就是"组织决定性能"的定量证明}——
\textbf{材料工程师的核心工作,就是通过控制工艺来设计组织,从而获得想要的性能}。

\textbf{这也解释了为什么"成分相同"的钢价格能差很多}——\textbf{贵的不是成分,是组织控制(工艺)}。

\subsection{2D 推 3D:Delesse 原理}

\begin{verbatim}
照片上测得面积分数 0.05 → 三维体积分数 0.05
照片上测得面积分数 0.15 → 三维体积分数 0.15
照片上测得面积分数 0.30 → 三维体积分数 0.30
\end{verbatim}

\textbf{Aha}:\textbf{你切开材料,在显微镜下测出某个相占了照片的 15\% 面积,
就能断定它在整块材料里占 15\% 体积}。\textbf{一张 2D 照片,定量了 3D 组织}——
\textbf{这是定量金相的理论基石,一个 1847 年的地质学发现,至今支撑着材料表征}。

\subsection{怎么看见它:金相显微镜与定量金相}

\begin{bluebox}
\textbf{怎么看见它}。\textbf{这一章的对象是微观组织——最经典的工具是
光学金相显微镜(OM)和扫描电镜(SEM)}。
\end{bluebox}

\textbf{金相制样四步(每步都是手艺)}:
\begin{itemize}
\item \textbf{切割}:取样,避免过热改变组织
\item \textbf{镶嵌 + 磨抛}:从粗砂纸到 0.05 µm 抛光,得到镜面
\item \textbf{腐蚀}:用化学试剂(如硝酸酒精)\textbf{选择性腐蚀晶界和不同相}——\textbf{这是关键!不腐蚀就只是个镜面,看不见组织}
\item \textbf{观察}:OM(放大 50-1000×)看晶粒、相;SEM(放大到几万×)看更细的析出物
\end{itemize}

\textbf{为什么腐蚀能"显示"组织}:\textbf{晶界原子能量高、不同相化学活性不同,腐蚀速率不同}——
\textbf{腐蚀后高低不平,光线散射不同,就显出衬度}。\textbf{所以你看到的"组织",
是腐蚀"雕刻"出来的}。

\textbf{定量金相能测什么}:晶粒尺寸(截线法)、相体积分数(Delesse)、第二相尺寸分布、
晶粒形状、织构。\textbf{现代有图像分析软件 + EBSD(电子背散射衍射)自动测晶粒取向}。
\textbf{局限}:OM 分辨率受光波长限制($\sim$0.2 µm,看不清纳米组织,要靠 SEM/TEM);
\textbf{制样假象}(磨抛划痕、腐蚀过度)会误导;\textbf{2D 截面的统计代表性需足够取样}。

\textbf{这就是"怎么看见组织"的真相}——\textbf{从切样到腐蚀,每一步都决定你看到什么;
看到之后,还要用体视学定量,才是科学,不是"看图说话"}。

\section{6. 这玩意儿现在在哪}

\subsection{在材料工程中}

\begin{itemize}
\item \textbf{失效分析}:零件断了,第一步永远是切开看组织——\textbf{组织藏着失效原因}
\item \textbf{质量控制}:钢材出厂要测晶粒度等级,确保达标
\item \textbf{工艺开发}:调整热处理参数,目标是获得特定组织
\item \textbf{逆向工程}:看竞品组织,反推它的成分和工艺
\end{itemize}

\subsection{在计算材料学中(本书的现代视角)}

\begin{itemize}
\item \textbf{相场法(Ch12)}:\textbf{直接模拟组织演化}——晶粒长大、枝晶生长、析出——\textbf{是计算"组织"的主力}
\item \textbf{ICME(集成计算材料工程)}:把"成分-工艺-组织-性能"全链条用计算串起来——\textbf{四面体的计算化}
\item \textbf{机器学习}:从组织图像预测性能,或反过来设计目标组织
\item \textbf{数字孪生}:用 3D 重构(连续切片 + EBSD)建立真实组织的数字模型
\end{itemize}

\begin{bluebox}
\textbf{计算材料学怎么看组织}:你做相场模拟(Ch12),模拟的输出就是\textbf{微观组织演化}——
\textbf{从初始态长出晶粒、析出第二相}。\textbf{本章的"组织定量参数"(晶粒尺寸、相分数),
正是相场模拟的输出量,也是连接到性能预测(Ch13)的输入}。\textbf{组织是 ICME 全链条的中枢}。
\end{bluebox}

\subsection{在日常材料中}

\begin{itemize}
\item \textbf{大马士革钢的花纹}:就是宏观可见的组织(碳化物的层状分布)
\item \textbf{为什么铸铁脆}:片状石墨(组织)割裂基体,成为裂纹源
\item \textbf{为什么焊缝是薄弱处}:焊接热影响区组织粗大、不均匀
\item \textbf{金属的"疲劳寿命"}:取决于组织里的夹杂、孔洞(疲劳裂纹源)
\end{itemize}

\section{7. 让代码告诉你}

\subsection{配套模块:microstructure.py}

\begin{longtable}{|l|p{0.55\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{函数} & \textbf{演示什么} \\
\hline
\texttt{astm\_grain\_size} & ASTM 晶粒度等级 ↔ 晶粒尺寸 \\
\texttt{lever\_rule} & 杠杆定律算两相比例 \\
\texttt{delesse\_principle} & 体视学:2D 面积分数 = 3D 体积分数 \\
\texttt{intercept\_method} & 截线法测晶粒尺寸 \\
\texttt{strength\_from\_microstructure} & 组织参数 → 屈服强度 \\
\texttt{microstructure\_design} & 组织设计:同成分强度差 83\% \\
\hline
\end{longtable}

\textbf{运行}:\texttt{python3 microstructure.py}——\textbf{纯 numpy,真实组织数据}。

\subsection{思考题}

\begin{enumerate}
\item \textbf{(晶粒度)} 用 \texttt{astm\_grain\_size} 算 ASTM G=6 和 G=9 的晶粒尺寸。
若要求强度提升,该选哪个?用 Hall-Petch 估算强度差。

\item \textbf{(杠杆定律)} Pb-Sn 焊料含 40\% Sn,刚低于共晶温度时,
$\alpha$ 相占多少?β 相占多少?(用 \texttt{lever\_rule})

\item \textbf{(体视学)} 为什么 Delesse 原理要求截面"随机"?
如果材料有强烈织构(取向排列),会怎样?

\item \textbf{(组织设计)} 你要设计一个强度 80 MPa 的合金,
有"细化晶粒"和"增加第二相"两条路,各有什么代价?(提示:第二相过多会降韧)

\item \textbf{(综合)} 为什么说"组织是成分和工艺的指纹"?
举一个例子:同成分的钢,缓冷和淬火得到什么不同组织?
\end{enumerate}

\subsection{延伸阅读}

\begin{itemize}
\item \textbf{经典教材}:Callister, \textit{Materials Science and Engineering}(组织相关章节)
\item \textbf{金相}:Vander Voort, \textit{Metallography: Principles and Practice}
\item \textbf{体视学}:Underwood, \textit{Quantitative Stereology}
\item \textbf{组织-性能}:Bhadeshia \& Honeycombe, \textit{Steels: Microstructure and Properties}
\end{itemize}

\subsection{这一章没讲什么}

\begin{itemize}
\item \textbf{没讲组织怎么"形成"}(形核长大、相变动力学)——留给督脉 Ch8-9
\item \textbf{没讲具体合金的组织}(珠光体、贝氏体细节)——Ch11 热处理展开
\item \textbf{没讲织构的定量}(取向分布函数 ODF)——进阶话题
\item \textbf{没讲 3D 组织重构}(FIB 连续切片、X 射线断层)——留给附录 C
\end{itemize}

\begin{bluebox}
\textbf{本章小结}:微观组织 = 晶粒、相、缺陷在空间的排布,\textbf{尺度介于原子和宏观之间}。\textbf{材料科学四面体:成分 + 工艺 → 组织 → 性能}——\textbf{组织是中心顶点,成分和工艺通过组织决定性能}。\textbf{组织可定量}:ASTM 晶粒度、杠杆定律算相比例、Delesse 原理(2D 面积分数 = 3D 体积分数)。\textbf{核心 Aha:同成分只改组织,强度差 83\%}——组织是工艺的产物,不只是成分。\textbf{怎么看见它:金相显微镜,关键是腐蚀"雕刻"出组织,再用截线法/体视学定量——不是"看图说话"}。\textbf{组织是连接结构(前三章)与性能(后面交汇)的桥,也是计算材料学 ICME 的中枢}。\textbf{下一章}:组织为什么会变——\textbf{热力学:材料为什么变}。
\end{bluebox}

\begin{flushright}
\textit{第 4 章 · 微观组织:从缺陷到组织 · 完}
\end{flushright}
