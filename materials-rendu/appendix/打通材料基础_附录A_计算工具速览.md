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
{\fontsize{48}{48}\selectfont\bfseries\color{goldcolor!60} A}
\end{flushright}
\vspace{-0.3em}
\noindent{\color{primarycolor}\Huge\bfseries 附录 A:计算材料学工具速览}\\[0.3em]
{\color{mergecolor}\rule{\textwidth}{2pt}}\\[1em]
{\large\itshape\color{mergecolor} 多尺度计算暗线 · 工具与入门路径}\\[0.5em]
{\color{primarycolor!60} Computational Materials Science: A Toolbox Overview}
\vspace{2em}
```

> "全书埋了一条『多尺度计算』暗线:原子(DFT)→ 微观(CALPHAD/相场)→
> 宏观(FEM)。这个附录把这条线上的\textbf{真实工具}收口——每个尺度有哪些
> 主流软件、它们算什么、怎么入门。这是给想真正动手做计算材料学的人的地图。"

\vspace{1.5em}

\section{多尺度计算的全景}

\textbf{材料现象跨越十几个数量级的尺度——从电子(Å)到构件(m)}。\textbf{没有单一方法能通吃,
不同尺度用不同工具,再设法"打通"}:

\begin{longtable}{|l|l|p{0.34\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{尺度} & \textbf{方法} & \textbf{算什么} \\
\hline
电子/原子(Å-nm) & DFT、MD、MLIP & 电子结构、键合、能量、扩散 \\
微观(nm-µm) & CALPHAD、相场、位错动力学 & 相平衡、组织演化、塑性 \\
介观(µm-mm) & 晶体塑性、元胞自动机 & 多晶变形、晶粒长大 \\
宏观(mm-m) & 有限元(FEM) & 构件应力、变形、温度场 \\
\hline
\end{longtable}

\textbf{贯穿尺度的纽带}:\textbf{低尺度算出的参数,喂给高尺度}。\textbf{DFT 算形成能 → CALPHAD;
DFT 算界面能 → 相场;DFT 算弹性常数 → FEM;CALPHAD 算自由能 → 相场}。\textbf{这就是 ICME
(集成计算材料工程)的核心思想}。

\section{原子尺度:DFT / MD / MLIP}(Ch1/Ch14)

\subsection{第一性原理(DFT)}
\textbf{算什么}:电子结构、能带、带隙、磁矩、形成能、弹性常数、声子、缺陷能、界面能。
\textbf{主流软件}:
\begin{itemize}
\item \textbf{VASP}:商业,工业/学术标准,赝势平面波,功能全
\item \textbf{Quantum ESPRESSO}:开源,平面波,适合学习
\item \textbf{ABINIT / CASTEP / WIEN2k}:各有侧重(全电子、特定功能)
\end{itemize}
\textbf{入门路径}:先懂 Kohn-Sham 方程(Ch14)→ 跑一个简单体系(如硅的能带)→ 学收敛测试
(k 点、截断能)→ 算实际性质。\textbf{推荐书}:Sholl \& Steckel《DFT: A Practical Introduction》。

\subsection{分子动力学(MD)}
\textbf{算什么}:原子运动、扩散系数、热输运、热膨胀、相变、力学(大变形)。
\textbf{主流软件}:\textbf{LAMMPS}(开源,最流行)、GROMACS(生物分子)。
\textbf{关键}:需要"势函数"(描述原子间作用)——经验势快但不准,DFT 准但慢。

\subsection{机器学习势(MLIP)}
\textbf{算什么}:用神经网络拟合 DFT 数据,兼具 \textbf{DFT 精度 + MD 速度}——百万原子、纳秒尺度。
\textbf{主流框架}:\textbf{NequIP、Allegro、MACE}(等变图神经网络);\textbf{通用势 MACE-MP、CHGNet、M3GNet}
(跨元素体系,开箱即用)。\textbf{这是当代计算材料学最热的前沿}——让第一性原理"放大"到介观。

\section{微观尺度:CALPHAD / 相场}(Ch7/Ch12)

\subsection{CALPHAD(计算热力学)}
\textbf{算什么}:多元相图、相平衡、相分数 vs 温度、凝固路径、热力学驱动力。
\textbf{主流软件}:
\begin{itemize}
\item \textbf{Thermo-Calc}:商业,工业标准,功能最全,含动力学模块 DICTRA
\item \textbf{Pandat}:商业,自动相图计算
\item \textbf{FactSage}:冶金/陶瓷/氧化物强
\item \textbf{pycalphad}:开源 Python,可编程,适合学习和科研
\item \textbf{OpenCALPHAD}:开源
\end{itemize}
\textbf{数据格式}:TDB(热力学数据库文件),SGTE 纯元素数据。
\textbf{入门路径}:懂自由能 + 公切线(Ch5)→ 装 pycalphad → 算一个二元相图 → 学 TDB 文件结构。

\subsection{相场(Phase-Field)}
\textbf{算什么}:微观组织演化——枝晶、晶粒长大、析出、调幅分解、马氏体。
\textbf{主流软件}:
\begin{itemize}
\item \textbf{MOOSE}:开源,多物理场框架(含相场模块 MARMOT),功能强
\item \textbf{PRISMS-PF}:开源,高性能,GPU 支持
\item \textbf{FiPy}:开源 Python,适合学习
\item \textbf{MICRESS / OpenPhase}:专业相场软件
\end{itemize}
\textbf{入门路径}:懂 Cahn-Hilliard / Allen-Cahn(Ch12)→ 装 FiPy → 跑一维调幅分解 → 学耦合 CALPHAD 自由能。

\section{宏观尺度:有限元(FEM)}(Ch13)

\textbf{算什么}:构件应力/应变、变形、温度场、热处理畸变、裂纹扩展。
\textbf{主流软件}:
\begin{itemize}
\item \textbf{ABAQUS}:商业,工业标准,非线性强
\item \textbf{ANSYS / COMSOL}:商业,多物理场
\item \textbf{FEniCS / deal.II}:开源,可编程
\item \textbf{DAMASK}:开源,晶体塑性有限元(CPFEM,接 Ch10 位错塑性)
\end{itemize}
\textbf{入门路径}:懂刚度矩阵组装(Ch13)→ 学一个商业软件的建模流程,或用 FEniCS 写简单问题。

\section{选型建议:我该学哪个}

\begin{longtable}{|p{0.32\textwidth}|p{0.58\textwidth}|}
\hline
\rowcolor{primarycolor!10}
\textbf{你的目标} & \textbf{建议起点} \\
\hline
做相图/相平衡(本书 Ch6/7)& pycalphad(开源易学)→ Thermo-Calc(工业)\\
做组织演化模拟(Ch12)& FiPy(学习)→ MOOSE/PRISMS-PF(科研)\\
算电子结构/磁性(Ch14)& Quantum ESPRESSO(开源)→ VASP \\
做大尺度原子模拟 & LAMMPS + MLIP(MACE/NequIP)\\
算构件力学(Ch13)& 商业 FEM(ABAQUS/ANSYS)或 FEniCS \\
ICME 全链条 & Thermo-Calc + 相场 + FEM 组合 \\
\hline
\end{longtable}

\begin{bluebox}
\textbf{给初学者的话}:\textbf{先用开源工具(pycalphad、FiPy、Quantum ESPRESSO、LAMMPS)
把原理跑通,理解每个尺度在算什么};\textbf{需要工业级精度和功能时,再上商业软件}。
\textbf{本书每章的配套 Python 代码,就是这些专业工具的"极简教学版"}——\textbf{先用它们理解原理,
再去碰真家伙}。\textbf{记住:工具是手段,理解物理才是目的——garbage in, garbage out,
不懂原理的计算只会产出垃圾}。
\end{bluebox}

\begin{flushright}
\textit{附录 A · 计算材料学工具速览 · 完}
\end{flushright}
