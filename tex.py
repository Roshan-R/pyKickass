intro = r"""%%% Template originaly created by Karol Kozio0x00C5 (mail@karol-koziol.net) and modified for ShareLaTeX use

\documentclass[14pt, letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[a4paper, total={6in, 8in}]{geometry}
\usepackage{listings}
\usepackage{enumitem}
\usepackage{graphicx}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{xcolor}
\usepackage{algorithm}
\usepackage{algorithmic}
\renewcommand\familydefault{\sfdefault}
\usepackage{tgheros}

\usepackage{amsmath,amssymb,amsthm,textcomp}
\usepackage{enumerate}
\usepackage{multicol}
\usepackage{tikz}
\usepackage{titlesec}
\usepackage{geometry}
\geometry{left=25mm,right=25mm,%
bindingoffset=0mm, top=20mm,bottom=20mm}


\linespread{1.3}

\newcommand{\linia}{\rule{\linewidth}{0.5pt}}

% custom theorems if needed
\newtheoremstyle{mytheor}
    {1ex}{1ex}{\normalfont}{0pt}{\scshape}{.}{1ex}
    {{\thmname{#1 }}{\thmnumber{#2}}{\thmnote{ (#3)}}}

\theoremstyle{mytheor}
\newtheorem{defi}{Definition}


% custom footers and headers
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{}
\chead{}
\rhead{}
\lfoot{\textbf{--TITLE--} }
\cfoot{}
\rfoot{Page \thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
%

% code listing settings
\usepackage{listings}
\lstset{
    language=C,
    basicstyle=\ttfamily\small,
    aboveskip={1.0\baselineskip},
    belowskip={1.0\baselineskip},
    columns=fixed,
    extendedchars=true,
    breaklines=true,
    tabsize=4,
    prebreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\hookleftarrow}},
    frame=lines,
    showtabs=false,
    showspaces=false,
    showstringspaces=false,
    keywordstyle=\color[rgb]{0.627,0.126,0.941},
    commentstyle=\color[rgb]{0.133,0.545,0.133},
    stringstyle=\color[rgb]{01,0,0},
    numbers=left,
    numberstyle=\small,
    stepnumber=1,
    numbersep=10pt,
    captionpos=t,
    escapeinside={\%*}{*)}
}

%%%----------%%%----------%%%----------%%%----------%%%

\begin{document}


\end{titlepage}

%%% -- Title page -- %%%
\begin{titlepage}
	\begin{center}
	\fontsize{14pt}{14pt} \selectfont {College of Engineering Trivandrum}\\
	\vspace*{0.8cm}
	\vspace*{1.5cm}	
	\fontsize{18pt}{1cm}\selectfont\textbf{{--TITLE--}}\\
	\vspace*{0.8cm}
	\vspace*{1.5cm}
	\includegraphics[width=2in]{cet.jpg}\\
	\vspace*{2.5cm}
	\fontsize{14pt}{14pt} \selectfont{--NAME--}\\
	\vspace{0.2cm}
	\fontsize{14pt}{14pt} \selectfont{S3 CSE Roll No:..}\\
	\vspace*{0.2cm}
	\fontsize{14pt}{14pt} \selectfont{TVE19CS..}\\
	\vspace*{2cm}
	\fontsize{18pt}{1cm}\selectfont {Department Of Computer Science}\\
	\vspace{0.5cm}
		\fontsize{18pt}{18pt}\selectfont{November 24, 2020}
\end{center}
\end{titlepage}
"""

first = r"""
\includegraphics[width=0.5in]{cet.jpg}
\hfill
  \textbf{ \huge{\underline{--TITLE--}}}
"""

section = r"""

\section{Experiment --NUMBER-- }

\subsection{Aim}
--AIM--

\subsection{Algorithm}
\hline 
\vspace{0.1cm}
\hspace{0.2 cm}Algorithm --NUMBER--:--AIM--
\vspace{0.1cm}
\hline
\begin{verbatim}
--ALGORITHM--
\end{verbatim}
\newpage

\subsection{Code}
\begin{lstlisting}[label={list:first}]
--CODE--
\end{lstlisting}

\subsection{Sample output}
\includegraphics[scale=0.5]{pics/--OUTPUT--.png}
%use output here if output is imagg else include in main code

\newpage
"""

end = r"""

\end{document}
"""
