# Exercise Book: SG-6 — Query–key gradient duality
Plan: transformer-attention_training_plan.md | Target level: Master's

> Try each exercise before reading its solution. In every set, the worked solutions follow the exercises.

## Set 2026-11-13 — after the session

### High school: exercises

**HS-1.** Two tokens have identical queries and keys: $q_1=k_1=(1,1)$ and $q_2=k_2=(1,-1)$. The gradients of the loss with respect to the dot products $q_i^\top k_j$ are $\hat G=\begin{pmatrix}0&0\\2&-2\end{pmatrix}$ (row = asking token, column = asked token). The learning rate is $\eta=0.1$. Find the four gradients $\partial L/\partial q_1$, $\partial L/\partial q_2$, $\partial L/\partial k_1$, $\partial L/\partial k_2$ and the four vectors after one step of gradient descent.

**HS-2.** *(Twist: the table is symmetric.)* $q_1=k_1=(1,0)$, $q_2=k_2=(0,1)$ and $\hat G=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, with $\eta=0.5$. Are the queries and keys still equal, pair by pair, after one step? Say what this shows about the cause of the separation seen in HS-1.

### High school: worked solutions

**HS-1.**
**Given:** $q_1=k_1=(1,1)$, $q_2=k_2=(1,-1)$, $\hat G=\begin{pmatrix}0&0\\2&-2\end{pmatrix}$, $\eta=0.1$.
**Step 1:** Queries read rows.
$\partial L/\partial q_1=0\cdot k_1+0\cdot k_2=(0,0)$
$\partial L/\partial q_2=2\,k_1-2\,k_2=(2,2)-(2,-2)=(0,4)$
> **Why:** $q_2$ appears only in the dot products of row 2, each time multiplied by a key.

**Step 2:** Keys read columns.
$\partial L/\partial k_1=0\cdot q_1+2\,q_2=(2,-2)$
$\partial L/\partial k_2=0\cdot q_1-2\,q_2=(-2,2)$
> **Why:** $k_j$ appears only in the dot products of column $j$, each time multiplied by a query.

**Step 3:** Update, new = old $-\ \eta\,\cdot$ gradient.
$q_1=(1,1)$; $q_2=(1,-1)-(0,0.4)=(1,-1.4)$
$k_1=(1,1)-(0.2,-0.2)=(0.8,1.2)$; $k_2=(1,-1)-(-0.2,0.2)=(1.2,-1.2)$
**Result:** The queries are $\{(1,1),(1,-1.4)\}$ and the keys $\{(0.8,1.2),(1.2,-1.2)\}$: no pair is equal any more. Token 1 asked nothing that mattered (its row is zero), yet its key moved, because token 2 asked about it.
> **Check:** new dot products. $q_2^\top k_1=0.8-1.68=-0.88$ (down from 0, as $\hat g_{21}=2>0$ wants); $q_2^\top k_2=1.2+1.68=2.88$ (up from 2, as $\hat g_{22}<0$ wants); $q_1^\top k_1=0.8+1.2=2$ and $q_1^\top k_2=1.2-1.2=0$ (unchanged, row 1 is zero). Second way, to first order: $\Delta(q_2^\top k_1)\approx-\eta\,[(0,4)\cdot(1,1)+(1,-1)\cdot(2,-2)]=-0.1\cdot8=-0.8$; the remaining $-0.08$ is the second-order term $\eta^2\,(0,4)\cdot(2,-2)=-0.08$.

**HS-2.**
**Given:** $q_1=k_1=(1,0)$, $q_2=k_2=(0,1)$, $\hat G=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, $\eta=0.5$.
**Step 1:** Rows: $\partial L/\partial q_1=k_1-k_2=(1,-1)$; $\partial L/\partial q_2=-k_1+k_2=(-1,1)$.
> **Why:** queries read rows.

**Step 2:** Columns: $\partial L/\partial k_1=q_1-q_2=(1,-1)$; $\partial L/\partial k_2=-q_1+q_2=(-1,1)$.
> **Why:** keys read columns. Here column $j$ holds the same numbers as row $j$, and queries equal keys, so each column read equals the matching row read.

**Step 3:** Update: $q_1=k_1=(1,0)-0.5\,(1,-1)=(0.5,0.5)$; $q_2=k_2=(0,1)-0.5\,(-1,1)=(0.5,0.5)$.
**Result:** Yes, the pairs stay equal. The separation in HS-1 came from the asymmetry of the table and from nothing else. A real head does not promise a symmetric table: the softmax fixes each row sum at zero and leaves the rest free.
> **Check:** in matrix form the query gradients are the rows of $\hat GK$ and the key gradients the rows of $\hat G^\top Q$. With $Q=K=I$ these are $\hat G$ and $\hat G^\top$, equal exactly when $\hat G$ is symmetric, which it is here.

### Master's: exercises

**MSc-1.** *(The plan's Exercise for SG-6.)* With $d=d_k=2$, $X=I$, $W_Q=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $W_K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $G=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$, compute $\sqrt2\,\partial L/\partial W_Q$ and $\sqrt2\,\partial L/\partial W_K$ from the formulas, then recompute the first one as $\sum_i\big(\sum_jg_{ij}k_j\big)x_i^\top$.

**MSc-2.** *(Twist: the tokens are not the identity, so $M\neq G$.)* A head has $d=2$, $d_k=1$, tokens $x_1=(1,0)$, $x_2=(1,1)$ and equal matrices $W_Q=W_K=\begin{pmatrix}1&-1\end{pmatrix}$. The score gradients are $G=\begin{pmatrix}0.2&-0.2\\-0.4&0.4\end{pmatrix}$. Compute $\partial L/\partial W_Q$ and $\partial L/\partial W_K$.

### Master's: worked solutions

**MSc-1.**
**Given:** as stated; $X=I$ so $M=X^\top GX=G$.
**Step 1:** $\sqrt2\,\partial L/\partial W_Q=W_KM^\top$ with $M^\top=\begin{pmatrix}1&0\\-1&0\end{pmatrix}$:
Row 1: $(0\cdot1+1\cdot(-1),\ 0\cdot0+1\cdot0)=(-1,0)$. Row 2: $(1\cdot1+0\cdot(-1),\ 0)=(1,0)$.
$$W_KG^\top=\begin{pmatrix}-1&0\\1&0\end{pmatrix}$$
> **Why:** the query gradient is built from the key matrix and reads the table transposed.

**Step 2:** $\sqrt2\,\partial L/\partial W_K=W_QM$:
Row 1: $1\cdot(1,-1)+0=(1,-1)$. Row 2: $0+2\cdot(0,0)=(0,0)$.
$$W_QG=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$$
> **Why:** the key gradient is built from the query matrix and reads the table as it stands.

**Result:** $\partial L/\partial W_Q=\tfrac1{\sqrt2}\begin{pmatrix}-1&0\\1&0\end{pmatrix}$ and $\partial L/\partial W_K=\tfrac1{\sqrt2}\begin{pmatrix}1&-1\\0&0\end{pmatrix}$.
> **Check:** per token. $k_1=W_Kx_1=(0,1)$, $k_2=W_Kx_2=(1,0)$. For $i=1$: $\sum_jg_{1j}k_j=(0,1)-(1,0)=(-1,1)$; for $i=2$: zero. Then $(-1,1)^\top x_1^\top=\begin{pmatrix}-1&0\\1&0\end{pmatrix}$, the matrix of Step 1.

**MSc-2.**
**Given:** $X=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ (rows are tokens), $W_Q=W_K=(1\ \ -1)$, $G$ as stated, $\sqrt{d_k}=1$.
**Step 1:** $M=X^\top GX$.
$GX$: row 1 $=(0.2\cdot1-0.2\cdot1,\ -0.2\cdot1)=(0,-0.2)$; row 2 $=(-0.4+0.4,\ 0.4)=(0,0.4)$.
$X^\top(GX)$ with $X^\top=\begin{pmatrix}1&1\\0&1\end{pmatrix}$: row 1 $=(0+0,\ -0.2+0.4)=(0,0.2)$; row 2 $=(0,0.4)$.
$$M=\begin{pmatrix}0&0.2\\0&0.4\end{pmatrix}$$
> **Why:** the formulas contain $M$, not $G$. They are the same only when $X=I$.
> **Note:** the trap is to use $G$ directly: $W_KG^\top=(0.4,-0.8)$, which is wrong here.

**Step 2:** $\partial L/\partial W_Q=W_KM^\top=(1\ \ -1)\begin{pmatrix}0&0\\0.2&0.4\end{pmatrix}=(-0.2,\ -0.4)$.
**Step 3:** $\partial L/\partial W_K=W_QM=(1\ \ -1)\begin{pmatrix}0&0.2\\0&0.4\end{pmatrix}=(0,\ -0.2)$.
> **Why:** same matrix on the left in both, $M^\top$ against $M$ on the right.

**Result:** $\partial L/\partial W_Q=(-0.2,-0.4)$ and $\partial L/\partial W_K=(0,-0.2)$: equal matrices, different gradients, and here the query matrix gets the larger one.
> **Check:** per token. $q_1=k_1=1$, $q_2=k_2=1-1=0$. Rows: $\partial L/\partial q_1=0.2\cdot1-0.2\cdot0=0.2$, $\partial L/\partial q_2=-0.4$. So $\partial L/\partial W_Q=0.2\,x_1^\top-0.4\,x_2^\top=(0.2,0)-(0.4,0.4)=(-0.2,-0.4)$. Columns: $\partial L/\partial k_1=0.2\cdot1-0.4\cdot0=0.2$, $\partial L/\partial k_2=-0.2$. So $\partial L/\partial W_K=0.2\,x_1^\top-0.2\,x_2^\top=(0,-0.2)$. Both agree.
