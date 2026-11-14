# Session Transcript: SG-6 -- Query–key gradient duality
Date: 2026-11-13

## Initial Test
**Case:** A teammate initialises an untied self-attention head with $W_Q=W_K=W_0$ and trains with plain gradient descent. (a) Predict whether $W_Q=W_K$ still holds after 1,000 steps, justified with the first-step gradients in terms of $W_0$, $X$, $G$. (b) For $d=d_k=2$, $W_0=I$, $X=I$, $G=\begin{pmatrix}0.2&-0.2\\-0.1&0.1\end{pmatrix}$, give both gradients.

**Learner response:** (a) Yes, equality holds: the score $x_i^\top W_Q^\top W_Kx_j/\sqrt{d_k}$ is symmetric in the two matrices, so both get the same first-step gradient $\tfrac1{\sqrt{d_k}}W_0X^\top GX$, and identical updates keep them identical. (b) Both gradients are $G/\sqrt2\approx\begin{pmatrix}0.141&-0.141\\-0.071&0.071\end{pmatrix}$.

**Evaluation:** FAIL (fell for the Tempting answer). Right: the key gradient $G/\sqrt2$, the $\sqrt{d_k}$ factor, $M=X^\top GX$. Wrong: the prediction, and the query gradient (it is $G^\top/\sqrt2$).

**Gaps identified:**
- Gap [conflation]: the query gradient was taken to be the key gradient (row read and column read of $G$ treated as the same) on the strength of the dot product's symmetry; the asymmetry of $G$ was missed.

## Teach Phase
### Gap: query gradient vs key gradient [conflation]
**Format:** ladder (start rung: High school; rungs: High school, Master's)
**Delivery:** visual: transformer-attention_visual_SG6.html. Results block returned:

```
VISUAL SESSION RESULTS
Principle: Query–key gradient duality
High school: correct, 1 try
Master's: correct, 2 tries, worked solution replayed
Level reached: Master's
```

**Content:** The reveal quoted the learner's prediction and showed it failing on the Initial Test case: $\partial L/\partial W_K=G/\sqrt2$ as answered, but $\partial L/\partial W_Q=G^\top/\sqrt2$, so the matrices separate at step 1. Then the Insight (the dot product is symmetric but the softmax is not), the Picture (a spreadsheet of score gradients: queries read rows, keys read columns; rows sum to zero, columns do not) with its limit, the foundational worked example (plan, SG-6), the Master's formal statement with the plan's Master's solved exercise, and a slider blending $\hat G$ towards its symmetric part.

**Rungs:**
- High school -- your turn: $q_1=k_1=(2,0)$, $q_2=k_2=(1,1)$, $\hat G=\begin{pmatrix}0.5&-0.5\\-1&1\end{pmatrix}$; find $\partial L/\partial k_2$ -> Learner: correct at the first try [$(0,1)$] -> held
- Master's -- your turn: $d=2$, $d_k=1$, $X=I$, $W_Q=W_K=(2\ \ 1)$, $G=\begin{pmatrix}0.3&-0.3\\-0.1&0.1\end{pmatrix}$; find $\partial L/\partial W_Q$ -> Learner: correct at the second try after the solved exercise was replayed [$(0.3,-0.1)$] -> held after a bridge

**Quick Check (confirmation of the top rung, in chat):** Why does $\partial L/\partial W_Q$ contain $M^\top$ while $\partial L/\partial W_K$ contains $M$, and why is $M$ not symmetric in general? -> Learner: each $g_{ij}$ pushes $W_K$ along $q_ix_j^\top$ and $W_Q$ along $k_jx_i^\top$, so the token roles are swapped; $M$ is symmetric only if $G$ is, and each row of $G$ comes from a separate softmax over keys; the tie breaks at the first step -> correct (refinement given: the exact condition is on $X^\top GX$).

**Deep-dive:** offered once; not requested.

## Final Test
**Case:** Classifier reading the last token only; $x_1=(1,0)$, $x_2=(0,1)$, $x_3=(1,1)$, $d=d_k=2$, $W_Q=W_K=I$, last row of $G$ is $(0.3,-0.1,-0.2)$, other rows zero. Reviewer claims equal gradients and free tying. (a) Predict and justify. (b) Compute both gradients. (c) Say which tokens each gradient is built from.

**Learner response:** (a) Not equal: $\partial L/\partial W_K=\tfrac1{\sqrt{d_k}}W_QM$, $\partial L/\partial W_Q=\tfrac1{\sqrt{d_k}}W_KM^\top$, equal only if $M$ is symmetric, which it is not; tying is not free. (b) $M=x_3(0.1,-0.3)=\begin{pmatrix}0.1&-0.3\\0.1&-0.3\end{pmatrix}$; $\partial L/\partial W_K=M/\sqrt2\approx\begin{pmatrix}0.071&-0.212\\0.071&-0.212\end{pmatrix}$; $\partial L/\partial W_Q=M^\top/\sqrt2\approx\begin{pmatrix}0.071&0.071\\-0.212&-0.212\end{pmatrix}$. (c) $\partial L/\partial W_Q=\tfrac1{\sqrt2}(\sum_jg_{3j}k_j)x_3^\top$: input side the single query token $x_3$, output direction the $G$-weighted mix of keys; $\partial L/\partial W_K=\tfrac1{\sqrt2}q_3(\sum_jg_{3j}x_j)^\top$: input side all three key tokens, output direction $q_3$. Both rank 1, transposes of each other.

**Evaluation:** PASS

## Result
Status: complete
Loops: 0
Level reached: Master's (session level: Master's)
