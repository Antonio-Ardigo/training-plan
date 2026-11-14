# Training Plan: Transformer Attention — Queries, Keys, Values and Their Gradients
Generated: 2026-11-13 | Status: in-progress | Target level: Master's

## Learning Goal
Understand the attention mechanism of transformers: scaled dot-product self-attention, the roles of the query, key and value matrices, and how training differentiates the query and key matrices through their gradients, at master's level. Do not ask me questions: use Master's as the target level and accept your own overview and hard-core list.

## SMART Goal
Derive and compute scaled dot-product self-attention, explaining Q, K, V roles and query–key gradient differentiation.

## Pedagogical Method: Test-Teach-Test

Each session follows a **Test → Teach → Test** cycle:

1. **Test** — a practical case comes first, with no theory beforehand. Attempt it cold: the attempt shows what is already known and exactly where the gaps are.
2. **Teach** — only the gaps the test revealed are taught, one at a time and principle-first. Each explanation ends with a Quick Check.
3. **Test** — a different practical case confirms the learning transfers. If gaps remain, the cycle repeats on those gaps only (at most twice).

**Teaching style: direct explanation.** A Socratic version of a plan, in which each concept is reached through a chain of questions instead of being explained, is created with `/socratic-training-plan` in a separate folder.

## Motivation & Course Overview (VOC)
> _Editable by the learner. This is the course's bird's-eye view and
> voice-of-customer anchor. If you change anything here, tell me — your
> feedback may restructure the plan (re-decomposition of sub-goals)._

**Why this matters:** Attention is the one operation that every modern language, vision and protein model is built from. Anyone who initialises, debugs, compresses or interprets a transformer is making claims about what its query, key and value matrices do and how they learn, and those claims are only as good as the algebra behind them.

**Bird's-eye view of the course:** The course starts from attention as a differentiable lookup (a weighted average of values), adds the one numerical safeguard it needs (the $\sqrt{d_k}$ scaling), and then separates the head into its two jobs: deciding where to look (queries and keys) and deciding what to carry (values). From there it goes backwards through the head: first the gradient that reaches each attention score, then the gradients that reach the query and key matrices, which is where the two matrices stop being interchangeable. Key-concept sessions turn each principle into working skill (matrix-form forward pass, saturation, asymmetry and rank, the value gradient, symmetry breaking at initialisation, a conserved quantity of training), a tools session checks the hand-derived gradients numerically, and a capstone puts everything together on one small head.

**Core principles & key facts:**
- *Soft lookup:* each token's output is a weighted average of all tokens' value vectors; the weights are a softmax over query–key dot products.
- *Variance scaling:* dot products grow with the key dimension, so they are divided by $\sqrt{d_k}$ to keep the softmax responsive.
- *Role separation:* queries and keys together decide where attention goes; the value matrix alone decides what is transported.
- *Softmax competition gradient:* a score's gradient depends on how that key's value compares with the current output, and the gradients along one query's row cancel.
- *Query–key gradient duality:* each of the two matrices is updated using the other one, and they read the table of score gradients from opposite sides.
- *Facts relied on:* the formula $\mathrm{softmax}(QK^\top/\sqrt{d_k})\,V$ with a row-wise softmax; this plan's shape convention ($q_i = W_Q x_i$); the original base configuration ($d_\text{model}=512$, 8 heads, $d_k=64$); the unit-variance assumption behind the scaling.

**What you'll be able to do on completion:**
- Compute a self-attention head by hand and in matrix form, with every shape correct.
- Say, for any claim about "what the query matrix encodes", whether it is a property of the head or of an arbitrary choice of coordinates.
- Derive $\partial L/\partial W_Q$, $\partial L/\partial W_K$ and $\partial L/\partial W_V$ from a loss on the head's output, and verify them numerically.
- Predict from the gradients what an initialisation scheme (equal, zero, tied) does to the first training steps of a head.
- Explain why a saturated head stops learning where to look while it keeps learning what to carry.
- Complete the capstone: forward pass, all three gradients, one update step and a written interpretation for a small head.

## Breakthrough
> _The story behind the topic: what the situation was before the key
> intuition, and what the topic solved._

**Before the intuition:** Sequence models read text one token at a time and carried everything they knew in a single running state; early translation systems even squeezed a whole sentence into one fixed vector. Information from far back had to survive every step in between, and long sentences came out worse.

**The intuition:** Let each position look directly at every other position and take a weighted mix of what it finds there, with the weights computed from the content itself. Attention was introduced this way for translation by Bahdanau, Cho and Bengio (2014), and in 2017 Vaswani and colleagues showed that it could be the whole architecture.

**What it solved:** Any two positions became one step apart, whatever their distance, and all positions could be processed in parallel. That made training on very large corpora practical and is the basis of today's large models.

| Principle | Before the intuition | What it solved |
|-----------|----------------------|----------------|
| Soft lookup | Retrieval meant picking one item (a hard choice that gradients cannot pass through) or reading a fixed window. | A lookup that is smooth in its inputs, so "where to read" can be learned by gradient descent. |
| Variance scaling | Plain dot-product attention was observed to train worse than the older additive form as the vectors got wider. | One constant keeps the scores in the same numerical range at any width, so the cheap dot-product form could be used everywhere. |
| Role separation | The first attention models scored each pair of positions with one small network fed both states, so asking, offering and delivering were mixed in one function. | Three plain linear maps with distinct jobs, cheap enough to run as matrix products and to replicate over many heads. |
| Softmax competition gradient | Attention weights were read as given "importance" numbers, with no account of what makes one go up or down in training. | A local rule that says which scores training pushes up and which it pushes down. |
| Query–key gradient duality | The names "query" and "key" were role labels attached by the designer, with no account of what learning signal each matrix actually receives. | Explicit gradients for both matrices, from which initialisation choices and stalled heads can be diagnosed. |

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| Soft lookup | Each output is a weighted average of the value vectors, with weights given by a softmax over query–key similarity scores. | $o_i=\sum_j \alpha_{ij}v_j,\quad \alpha_{ij}=\mathrm{softmax}_j(s_{ij}),\quad s_{ij}=q_i^\top k_j/\sqrt{d_k}$ | Dot product; softmax; convex combination |
| Variance scaling | The dot product of two $d_k$-dimensional vectors with independent unit-variance components has variance $d_k$, so dividing by $\sqrt{d_k}$ keeps the scores at unit variance and the softmax out of saturation. | $\mathrm{Var}(q^\top k)=d_k \;\Rightarrow\; \mathrm{Var}(q^\top k/\sqrt{d_k})=1$ | Variance of a sum of independent variables; softmax |
| Role separation | The attention pattern depends on $W_Q$ and $W_K$ only through the product $W_Q^\top W_K$, while $W_V$ alone determines what is carried along that pattern. | $s_{ij}=x_i^\top W_Q^\top W_K\,x_j/\sqrt{d_k},\quad v_j=W_Vx_j$ | Matrix product, transpose, inverse; bilinear forms |
| Softmax competition gradient | The loss gradient on a score is the attention weight times how much that key's value differs from the current output along the output's error signal; along each query's row these gradients sum to zero. | $g_{ij}=\dfrac{\partial L}{\partial s_{ij}}=\alpha_{ij}\,(v_j-o_i)^\top\delta_i,\quad \delta_i=\dfrac{\partial L}{\partial o_i},\quad \sum_j g_{ij}=0$ | Chain rule; derivative of softmax |
| Query–key gradient duality | The query matrix is updated with keys weighted along each query's row of score gradients, and the key matrix with queries weighted along each key's column, so each gradient is built from the other matrix and sees the score gradients from the opposite side. | $\dfrac{\partial L}{\partial W_Q}=\dfrac{1}{\sqrt{d_k}}W_KM^\top,\quad \dfrac{\partial L}{\partial W_K}=\dfrac{1}{\sqrt{d_k}}W_QM,\quad M=X^\top GX=\sum_{i,j}g_{ij}\,x_ix_j^\top$ | Matrix chain rule ($y=Wx \Rightarrow \partial L/\partial W=(\partial L/\partial y)\,x^\top$); outer products; gradient descent |

## Hard Core
> _The principles that are hardest to grasp. Each is taught through an aha
> moment and a climb through the levels, with a solved exercise at every rung.
> If this list looks wrong to you, tell me which principle to add or remove._

| Principle | Why it is hard | Taught in |
|-----------|----------------|-----------|
| Role separation | persistent misconception, load-bearing (4 sub-goals depend on it) | SG-4 |
| Query–key gradient duality | counter-intuitive, load-bearing (4 sub-goals depend on it) | SG-6 |

## Key Facts
> _What this course relies on you simply knowing. Values marked `(verify)`
> should be checked against a source before you rely on them._

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | Scaled dot-product attention is $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})\,V$, with the softmax taken **row-wise**: row $i$ belongs to query $i$ and sums to 1 over the keys $j$. | With a column-wise softmax every later result (weights, row sums of gradients) comes out wrong. | SG-2, SG-5, SG-7, SG-10, SG-14 |
| KF-2 | Convention of this plan: the rows of $X\in\mathbb{R}^{n\times d}$ are the tokens $x_i^\top$; $q_i=W_Qx_i$, $k_j=W_Kx_j$, $v_j=W_Vx_j$ with $W_Q,W_K\in\mathbb{R}^{d_k\times d}$ and $W_V\in\mathbb{R}^{d_v\times d}$; hence $Q=XW_Q^\top$, $K=XW_K^\top$, $V=XW_V^\top$. No biases. | Other texts write $Q=XW_Q$; mixing the two conventions transposes every gradient formula. | SG-4, SG-6, SG-7, SG-9, SG-10, SG-11, SG-12, SG-13, SG-14 |
| KF-3 | The base model of "Attention Is All You Need" (Vaswani et al., 2017) uses $d_\text{model}=512$, $h=8$ heads and $d_k=d_v=d_\text{model}/h=64$. | Realistic orders of magnitude for scores, ranks and shapes cannot be estimated without it. | SG-3, SG-7, SG-8, SG-9 |
| KF-4 | The $\sqrt{d_k}$ argument assumes that the components of $q$ and $k$ are independent with mean 0 and variance 1. | Without the assumption the variance $d_k$ does not follow, and the argument is misapplied to trained heads where it need not hold. | SG-3, SG-8 |
| KF-5 | Gradient layout: $\partial L/\partial W$ has the same shape as $W$, with entry $(a,b)$ equal to $\partial L/\partial W_{ab}$; $G$ denotes the $n\times n$ matrix of $g_{ij}=\partial L/\partial s_{ij}$ (row = query, column = key). | With the other layout the formulas for $W_Q$ and $W_K$ swap their transposes. | SG-5, SG-6, SG-10, SG-11, SG-12, SG-13, SG-14 |
| KF-6 | In **self**-attention $Q$, $K$ and $V$ are all computed from the same input $X$; in cross-attention $Q$ comes from one sequence and $K$, $V$ from another. | Arguments about symmetry between queries and keys only make sense in the self-attention case. | SG-1, SG-6, SG-9, SG-11 |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | Explain, for a concrete long-range task, what self-attention offers over recurrence and its cost. | Sequence modelling | low | MSc | — | complete | Page checks 3/3, chat test waived |
| SG-2 | Core Principle | State the soft-lookup principle and compute one attention output as a weighted average of values. | Attention forward pass | low | MSc | Soft lookup | pending | - |
| SG-3 | Core Principle | State why scores are divided by $\sqrt{d_k}$ and quantify the effect on one softmax. | Numerical conditioning | low | MSc | Variance scaling | pending | - |
| SG-4 | Core Principle | State which function of $W_Q$, $W_K$ sets the pattern and apply it to one head. | Head parametrisation | low | MSc | Role separation | pending | - |
| SG-5 | Core Principle | State the score-gradient rule and compute the score gradients of one query. | Backpropagation | low | MSc | Softmax competition gradient | pending | - |
| SG-6 | Core Principle | State the query and key gradient formulas and apply them to one small head. | Backpropagation | low | MSc | Query–key gradient duality | complete | Final Test PASS, 0 loops; level reached Master's of Master's |
| SG-7 | Key Concept | Compute a full self-attention head in matrix form, giving every intermediate shape correctly. | Attention forward pass | medium | MSc | Soft lookup, Variance scaling | pending | - |
| SG-8 | Key Concept | Quantify how score scale drives softmax saturation and shrinks the score gradients. | Numerical conditioning | medium | MSc | Variance scaling, Softmax competition gradient | pending | - |
| SG-9 | Key Concept | Show what separate query and key matrices can express that a tied matrix cannot. | Head parametrisation | medium | MSc | Role separation | pending | - |
| SG-10 | Key Concept | Derive the value-matrix gradient and contrast its path with the score-gradient path. | Backpropagation | medium | MSc | Soft lookup, Softmax competition gradient | pending | - |
| SG-11 | Key Concept | Predict from the gradient formulas the first training step under equal, zero and tied initialisations. | Training dynamics | high | MSc | Softmax competition gradient, Query–key gradient duality | pending | - |
| SG-12 | Key Concept | Derive the quantity that gradient flow conserves between $W_Q$ and $W_K$ and use it. | Training dynamics | high | MSc | Role separation, Query–key gradient duality | pending | - |
| SG-13 | Tools | Verify hand-derived attention gradients numerically with finite differences to relative error below $10^{-5}$. | Numerical verification | medium | MSc | Query–key gradient duality | pending | - |
| SG-14 | Verification | For one small head, compute forward pass, all gradients, one update, and interpret each matrix's role. | Integration | high | MSc | All five | pending | - |

_Depth is the plan's Target level in every row: HS = High school, MSc = Master's, Adv = Advanced._

## Prerequisite Graph

```
Transformer attention: Q, K, V roles and query–key gradients (core)
  requires:
    Linear algebra: matrix product, transpose, inverse, rank, outer product (prerequisite) ← CHECK learner profile
    Multivariable calculus: chain rule, gradient of a scalar w.r.t. a matrix (prerequisite) ← CHECK learner profile
    Probability: mean and variance of a sum of independent variables (prerequisite) ← CHECK learner profile
    Softmax function and its derivative (prerequisite) ← CHECK learner profile
    Gradient descent and backpropagation in a feed-forward network (prerequisite) ← CHECK learner profile
    NumPy or PyTorch at the level of writing a 30-line script (prerequisite, SG-13 only) ← CHECK learner profile
  rests on:
    Soft lookup (principle) → SG-2
      led to:
        Variance scaling (principle) → SG-3
        Role separation (principle) → SG-4
        Softmax competition gradient (principle) → SG-5
          led to:
            Query–key gradient duality (principle, also rests on Role separation) → SG-6
```

> **WARNING — prerequisites not confirmed.** No `learner_profile.md` exists, so none of the six `requires` items is confirmed as a known strength. If an Initial Test fails because of one of them rather than because of attention itself, the session will flag it as a missing prerequisite.

## Sequence
- **SG-1** first (Motivation; no dependency).
- **SG-2** next: Soft lookup is the root of the graph.
- **SG-3**, **SG-4**, **SG-5** each depend on SG-2 only (three `led to` edges from Soft lookup) and may be taken in any order; the listed order is recommended.
- **SG-6** depends on SG-5 (`led to`) and SG-4 (`also rests on`).
- **SG-7** depends on SG-2 and SG-3. **SG-8** depends on SG-3 and SG-5. **SG-9** depends on SG-4. **SG-10** depends on SG-2 and SG-5.
- **SG-11** depends on SG-5 and SG-6. **SG-12** depends on SG-4 and SG-6.
- **SG-13** (Tools) depends on SG-6; taking SG-10 first lets it check all three gradients.
- **SG-14** (Verification) last; it draws on all five principles.

## Session Blueprints
> _Session designs. Run a sub-goal's session before reading its blueprint: the
> tests work best unseen. The solved exercises are there to study afterwards._

### SG-1: Why attention
- **Initial Test:** A team builds a code-completion model. In a C file, `buf = malloc(n)` appears at token 40 and `free(` must be completed with `buf` at token 640. They are choosing between a 2-layer LSTM and a stack of self-attention layers. Task: explain (a) how many computation steps separate the two tokens in each design, for the forward signal and for the gradient; (b) how each design decides *which* earlier token is relevant; (c) what the attention design costs in exchange, and what it needs that the LSTM gets for free.
- **Pass Criteria:** Names at least 3 of these 4, each with a correct reason: constant path length versus about 600 recurrent steps; content-based selection (the weights depend on what the tokens are, not where they are); cost that grows as $n^2$ in sequence length; no built-in notion of order, so position information must be added.
- **Estimated Depth:** Master's
- **Principle:** —
- **Exercise:** Take the sentence "The keys that the manager left on the desk are missing." Mark the verb "are" and the word it must agree with. Count the tokens between them, then write two sentences: how a recurrent model gets the information across, and how an attention layer does. Expected outcome: 7 intervening tokens; "many updates of one state" versus "one weighted read".
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Attention shortens the path between any two positions to one step | Path length | Give the number of steps between tokens 40 and 640 in each design | overgeneralization: "attention has no long-range problem at all", ignoring cost and context limits |
  | Selection is by content, not by position | Content-based addressing | Explain why moving `malloc` 100 tokens earlier does not change how it is found | conflation: confusing attention weights with positional proximity |
  | The benefit is paid for with quadratic cost and loss of order | Trade-offs | State the cost of doubling the sequence length | verbal-without-formal: says "expensive" without the $n^2$ scaling |
- **Teach Topics:** Path length for signal and gradient in recurrent versus attention layers; content-based addressing; parallelism over positions; the $n\times n$ score table and its cost; why order must be injected separately; self- versus cross-attention (KF-6). Pitfalls: [overgeneralization] treating attention as free of long-range limits; [conflation] attention weight versus positional distance.
- **Final Test:** A hospital summarisation model must connect "penicillin" in a discharge prescription with "allergic to beta-lactams" written 2,000 tokens earlier in the admission note. Compare a recurrent encoder with a self-attention encoder on the same three points (path, selection, cost), and say what happens to the attention cost if the note doubles in length.

### SG-2: Soft lookup
- **Principle:** Soft lookup — each output is a weighted average of the value vectors, with weights given by a softmax over query–key similarity scores.
- **Worked Example (foundational):**
  **Given:** One query and three keys with $d_k=4$: $q=(1,1,1,1)$, $k_1=(1,1,1,1)$, $k_2=(1,1,0,0)$, $k_3=(1,-1,0,0)$. Values $v_1=(10,0)$, $v_2=(0,10)$, $v_3=(10,10)$.
  **Step 1:** Scores: $q^\top k_1=4$, $q^\top k_2=2$, $q^\top k_3=0$; divide by $\sqrt{4}=2$ to get $s=(2,1,0)$.
  > **Why:** The score measures how well each key matches the query; the division is the scaling of KF-1.
  **Step 2:** Softmax: $e^2=7.389$, $e^1=2.718$, $e^0=1$, sum $=11.107$, so $\alpha=(0.665,\,0.245,\,0.090)$.
  > **Why:** The softmax turns scores into positive weights that sum to 1, so the result is an average and not a sum.
  **Step 3:** Output: $o=0.665\,(10,0)+0.245\,(0,10)+0.090\,(10,10)=(7.55,\,3.35)$.
  > **Why:** The query never sees the keys' content directly; it receives the values, mixed in proportion to the weights.
  **Result:** $o=(7.55,\,3.35)$: mostly $v_1$, the value whose key matched best, with a share of the others.
  > **Check:** The weights sum to $0.665+0.245+0.090=1.000$. Second way: the first component receives 10 from $v_1$ and $v_3$ only, so $o_1=10\,(\alpha_1+\alpha_3)=7.55$; likewise $o_2=10\,(\alpha_2+\alpha_3)=3.35$. Both components lie between 0 and 10, as an average must.
- **Initial Test:** In the sentence "river bank flooded", the token "bank" issues a query. Its scaled scores against the three tokens (river, bank, flooded) are $s=(\ln 4,\ 0,\ \ln 3)$, and the value vectors are $v_\text{river}=(8,0)$, $v_\text{bank}=(0,0)$, $v_\text{flooded}=(0,8)$. (a) Compute the output for "bank". (b) State in your own words what kind of quantity the output is. (c) What does the output tend to if the score for "river" grows without bound?
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly (weights $(0.5, 0.125, 0.375)$, output $(4,3)$, limit $v_\text{river}$).
- **Estimated Depth:** Master's
- **Exercise:** With scores $s=(0,0,\ln 2)$ and scalar values $v=(1,5,9)$, compute the weights and the output, then say between which two numbers the output must lie whatever the scores are. Expected outcome: $\alpha=(0.25,0.25,0.5)$, $o=6$, always between 1 and 9.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The output is a convex combination of values, not of keys | Soft lookup | Given keys and values that differ, say which vectors appear in the output | conflation: averaging the keys, or treating key and value as the same vector |
  | The weights come from a softmax over the keys for one query | Soft lookup | Compute the weights for a 3-key case and check they sum to 1 | procedural-without-conceptual: computes the softmax without seeing that it makes the output an average |
- **Teach Topics:** The three steps score → softmax → average; hard lookup as the limit of large score gaps; the output stays inside the convex hull of the values; the row-wise softmax (KF-1). Pitfalls: [conflation] key versus value; [overgeneralization] "the output is the best-matching value" (true only in the saturated limit).
- **Final Test:** In "she paid the bill", the token "paid" has scaled scores $s=(\ln 2,\ 0,\ 0,\ \ln 5)$ against (she, paid, the, bill), with scalar values $v=(9,\ 0,\ 0,\ 18)$. Compute the output, state the principle in one sentence, and say what the output becomes if all four scores are equal.

### SG-3: Variance scaling
- **Principle:** Variance scaling — the dot product of two $d_k$-dimensional vectors with independent unit-variance components has variance $d_k$, so dividing by $\sqrt{d_k}$ keeps the scores at unit variance and the softmax out of saturation.
- **Worked Example (foundational):**
  **Given:** Queries and keys whose components are independent and equal to $+1$ or $-1$ with probability ½ each (mean 0, variance 1). Compare $d_k=4$ with $d_k=64$, for two keys whose raw scores differ by one standard deviation.
  **Step 1:** Each product $q_ak_a$ is $\pm1$ with mean 0 and variance 1. The dot product is a sum of $d_k$ such independent terms, so its variance is $d_k$: standard deviation 2 for $d_k=4$ and 8 for $d_k=64$.
  > **Why:** Variances of independent terms add; this is the whole reason the scores grow with the dimension.
  **Step 2:** Without scaling, at $d_k=64$ a one-standard-deviation gap is 8, and two keys get weights $1/(1+e^{-8})=0.9997$ and $0.0003$.
  > **Why:** The softmax responds to differences of scores, so a larger spread means a harder choice.
  **Step 3:** With scaling, the gap is $8/\sqrt{64}=1$ and the weights are $1/(1+e^{-1})=0.731$ and $0.269$, the same as for $d_k=4$ ($2/\sqrt4=1$).
  > **Why:** Dividing by the standard deviation of the scores makes their spread independent of the width of the head.
  **Result:** Scaling by $\sqrt{d_k}$ turns a nearly one-hot choice ($0.9997$) into a graded one ($0.731$), at any $d_k$.
  > **Check:** Enumerate $d_k=2$ exactly: the dot product is the sum of two independent $\pm1$ terms, so it equals $-2, 0, +2$ with probabilities ¼, ½, ¼. Its variance is $¼\cdot4+½\cdot0+¼\cdot4=2=d_k$.
- **Initial Test:** An engineer widens a head from $d_k=64$ to $d_k=256$ and removes the division by $\sqrt{d_k}$ "because it is just a constant". At initialisation the components of queries and keys are independent with mean 0 and variance 1. (a) What is the standard deviation of the scores now? (b) For two keys whose scores differ by one standard deviation, what weights does the softmax give? (c) State the principle the engineer has broken and what symptom you expect in training.
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly (standard deviation 16; weights about $1-10^{-7}$ and $10^{-7}$; near one-hot attention at initialisation with very small gradients to the scores).
- **Estimated Depth:** Master's
- **Exercise:** For $d_k=16$ and $d_k=100$, write down the standard deviation of the raw dot product and of the scaled score under KF-4, then compute the larger of two softmax weights for a one-standard-deviation gap, with and without scaling. Expected outcome: raw 4 and 10, scaled 1 and 1; unscaled weights $0.982$ and $0.99995$; scaled $0.731$ in both cases.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The spread of the dot product grows as $\sqrt{d_k}$, not as $d_k$ | Variance scaling | Give the standard deviation of the raw score for $d_k=256$ | conflation: variance versus standard deviation, leading to division by $d_k$ |
  | The scaling exists to keep the softmax responsive, under stated assumptions | Variance scaling | Name the assumption (KF-4) and say when it may fail | overgeneralization: "scores always have unit variance in a trained model" |
- **Teach Topics:** Variance of a sum of independent products; why the softmax cares about score differences; saturation in words (the detailed gradient effect is SG-8); the assumptions of KF-4 and their limits after training; the base configuration $d_k=64$ (KF-3). Pitfalls: [conflation] $d_k$ versus $\sqrt{d_k}$; [procedural-without-conceptual] treating the constant as cosmetic.
- **Final Test:** A new library divides the dot products by $d_k$ instead of $\sqrt{d_k}$, with $d_k=16$ and the assumptions of KF-4. (a) What is the standard deviation of the scores? (b) What weights do two keys one standard deviation apart receive? (c) State the principle and describe what the head's output looks like at initialisation.

### SG-4: Role separation
- **Principle:** Role separation — the attention pattern depends on $W_Q$ and $W_K$ only through the product $W_Q^\top W_K$, while $W_V$ alone determines what is carried along that pattern.
- **Tempting answer:** "The two checkpoints have different query matrices and different key matrices, so their queries ask for different things and the heads attend differently." It feels right because the names suggest that a query vector has a meaning of its own ("what this token is looking for") that can be read off the vector, the way a database query can be read on its own.
- **Insight:** A query is never looked at on its own, only through its dot product with a key, so the only real thing is the pairing; the coordinates in between are a private code the two matrices share.
- **Picture:** A lock and its key. Re-cut both to a new matching profile and the door opens exactly as before; re-cut only one and it does not. An observer comparing two keys from two such doors learns nothing about the doors. Where it stops being true: a real key opens one lock or none, while a query scores every key by degree; and the picture is about the function the head computes, not about training, where the two matrices are separate parameters that the optimiser treats separately.
- **Visual design:**
  - **Objects:** Two tokens $x_1=(1,0)$, $x_2=(0,1)$; the grids $W_Q=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $W_K=\begin{pmatrix}0&2\\2&0\end{pmatrix}$; the product grid $W_Q^\top W_K$; a $2\times2$ table of raw scores $q_i^\top k_j$ (here $\begin{pmatrix}0&2\\2&0\end{pmatrix}$).
  - **Colour roles:** blue = query side ($W_Q$, $q_i$); orange = key side ($W_K$, $k_j$); green = what does not change (product grid, score table).
  - **Steps:** (1) The two tokens and the two matrices appear. (2) The queries and keys are computed and drawn as arrows. (3) The score table fills in from the dot products. (4) $W_Q$ is doubled and $W_K$ halved; the arrows change, the score table does not. (5) The product grid appears and is shown to be the same before and after. (6) Master's rung: the scaling is replaced by a general invertible $R$ acting as $W_Q\to RW_Q$, $W_K\to R^{-\top}W_K$.
  - **Your-turn inputs:** *High school rung:* enter the raw score $q_1^\top k_2$ after $W_Q$ is doubled and $W_K$ halved. Right: 2. Wrong 4: only the query's change was applied (the key's compensating change was forgotten). Wrong 1: only the key's change was applied. *Master's rung* (the solved exercise below): enter entry $(2,1)$ of $W_Q'^\top W_K'$. Right: 3. Wrong 7: $R$ was applied to both matrices instead of $R$ and $R^{-\top}$. Wrong 0: entry $(1,2)$ was read instead of $(2,1)$, an index or transpose slip.
  - **Control:** One slider for a factor $c$ applied to $W_Q$, with a switch "compensate in $W_K$". With the switch on, the score table stays fixed for every $c$; with it off, the scores scale with $c$. It shows that only matched changes leave the head unchanged.
- **Worked Example (foundational):**
  **Given:** Tokens $x_1=(1,0)$, $x_2=(0,1)$. Head A: $W_Q=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, $W_K=\begin{pmatrix}0&2\\2&0\end{pmatrix}$. Head B: $W_Q'=2W_Q$, $W_K'=\tfrac12W_K$. Compare the raw scores $q_1^\top k_j$ of token 1 (the common factor $1/\sqrt{d_k}$ is the same for both heads).
  **Step 1:** Head A: $q_1=W_Qx_1=(1,0)$, $k_1=W_Kx_1=(0,2)$, $k_2=W_Kx_2=(2,0)$, so the scores are $q_1^\top k_1=0$ and $q_1^\top k_2=2$.
  > **Why:** The score is the only place where the query and the keys are used.
  **Step 2:** Head B: $q_1'=(2,0)$, $k_1'=(0,1)$, $k_2'=(1,0)$, so the scores are $0$ and $2$ again.
  > **Why:** Doubling one factor of a product and halving the other leaves the product unchanged.
  **Result:** The two heads have different queries and different keys and exactly the same scores, hence the same attention weights.
  > **Check:** Compute the product directly: $W_Q^\top W_K=\begin{pmatrix}0&2\\2&0\end{pmatrix}$ and $W_Q'^\top W_K'=(2W_Q)^\top(\tfrac12W_K)=\begin{pmatrix}0&2\\2&0\end{pmatrix}$. Entry $(1,2)$ is the score of token 1 against token 2, which is 2 in both heads.
- **Level ladder:**
  **Master's solved exercise**
  **Given:** $W_Q=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $W_K=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, and the invertible matrix $R=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Define $W_Q'=RW_Q$ and $W_K'=R^{-\top}W_K$. Show that the two heads compute the same scores for every input, and find the scores between the one-hot tokens.
  **Step 1:** Write the score as a bilinear form: $q_i^\top k_j=(W_Qx_i)^\top(W_Kx_j)=x_i^\top A\,x_j$ with $A=W_Q^\top W_K$.
  > **Why:** This isolates everything the score knows about the two matrices in the single matrix $A$.
  **Step 2:** Transform: $A'=(RW_Q)^\top(R^{-\top}W_K)=W_Q^\top R^\top R^{-\top}W_K=W_Q^\top W_K=A$.
  > **Why:** $R^\top R^{-\top}=I$ for every invertible $R$, so a whole $d_k\times d_k$ family of different $(W_Q,W_K)$ pairs gives one and the same head.
  **Step 3:** Numbers: $A=\begin{pmatrix}1&0\\2&1\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}=\begin{pmatrix}1&0\\3&1\end{pmatrix}$. With $R^{-\top}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}$: $W_Q'=\begin{pmatrix}1&3\\0&1\end{pmatrix}$, $W_K'=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, and $A'=W_Q'^\top W_K'=\begin{pmatrix}1&0\\3&1\end{pmatrix}$.
  > **Why:** The concrete matrices look unrelated; only the product reveals that they are the same head.
  **Result:** $A'=A$. For one-hot tokens the raw scores are the entries of $A$: token 2 scores 3 against token 1, while token 1 scores 0 against token 2. What the head "looks for" is a property of $A$, not of $W_Q$ or $W_K$ separately.
  > **Check:** Take $x=(1,1)$ as both query and key token. Through $A$: $x^\top Ax=1+0+3+1=5$. Through head 1: $q=W_Qx=(3,1)$, $k=W_Kx=(1,2)$, $q^\top k=5$. Through head 2: $q'=W_Q'x=(4,1)$, $k'=W_K'x=(1,1)$, $q'^\top k'=5$.
- **Initial Test:** Two fine-tuning runs of the same head ($d=3$, $d_k=2$) end with these weights. Checkpoint A: $W_Q=\begin{pmatrix}1&0&1\\0&1&0\end{pmatrix}$, $W_K=\begin{pmatrix}0&1&0\\1&0&1\end{pmatrix}$. Checkpoint B: $W_Q=\begin{pmatrix}0&-1&0\\1&0&1\end{pmatrix}$, $W_K=\begin{pmatrix}-1&0&-1\\0&1&0\end{pmatrix}$. Both have the same $W_V$. A colleague plots the query vectors of the two checkpoints for the same sentence and asks you how the attention patterns of the two heads differ. Predict the difference in attention weights on an arbitrary input, and justify your prediction.
- **Pass Criteria:** Gives the right answer, not the tempting one, AND justifies it at the Target level (the weights are identical for every input, because $W_Q^\top W_K$ is the same matrix in both checkpoints, shown by computing it or by exhibiting the transformation that links them).
- **Estimated Depth:** Master's
- **Exercise:** Take $W_Q=\begin{pmatrix}2&0\\0&1\end{pmatrix}$ and $W_K=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Build a second pair with $R=\begin{pmatrix}3&0\\0&1\end{pmatrix}$, compute $W_Q^\top W_K$ for both pairs, and state how many free numbers $R$ has for a head with $d_k=64$. Expected outcome: both products equal $\begin{pmatrix}2&2\\0&1\end{pmatrix}$; $64^2=4096$ free numbers.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | A matched rescaling of queries and keys leaves every score unchanged | Role separation, High school rung | Predict a score after $W_Q$ is tripled and $W_K$ divided by 3 | overgeneralization: "larger queries mean sharper attention" without looking at the keys |
  | Scores are a bilinear form in the tokens with matrix $W_Q^\top W_K$, invariant under $W_Q\to RW_Q$, $W_K\to R^{-\top}W_K$ | Role separation, Master's rung | Given two weight pairs, decide whether they are the same head | formal-without-intuitive: can verify $A'=A$ but still interprets single query coordinates |
  | $W_V$ is outside this invariance and sets what is transported | Role separation, Master's rung | Say what changes in the output if $W_V$ is doubled and $W_Q$, $W_K$ are kept | conflation: attributing content to keys instead of values |
- **Teach Topics:** The score as a bilinear form; the family of equivalent $(W_Q,W_K)$ pairs; what is and is not meaningful to interpret (the product, not single coordinates); the separate job of $W_V$; boundary: an unmatched change does alter the head, and the equivalence concerns the computed function, not how the two matrices move in training. Misunderstandings that survive the Insight: [formal-without-intuitive] accepting the algebra yet still reading meaning into one query coordinate; [overgeneralization] concluding that $W_Q$ and $W_K$ are interchangeable (they are not: swapping them changes $A$ into $A^\top$).
- **Final Test:** A checkpoint loader has a bug: it swaps the two rows of $W_Q$ and, by the same code path, the two rows of $W_K$, for a head with $W_Q=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $W_K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. A teammate says the head is now corrupted because "every query vector has changed". (a) Predict the effect on the attention weights and justify it. (b) A second bug swaps the rows of $W_Q$ only. Predict the effect now, and give the raw score of token $x_1=(1,0)$ against token $x_2=(0,1)$ before and after.

### SG-5: Softmax competition gradient
- **Principle:** Softmax competition gradient — the loss gradient on a score is the attention weight times how much that key's value differs from the current output along the output's error signal; along each query's row these gradients sum to zero.
- **Worked Example (foundational):**
  **Given:** One query, two keys with equal scores, so $\alpha=(0.5,0.5)$. Scalar values $v_1=4$, $v_2=0$, so $o=2$. Loss $L=\tfrac12(o-t)^2$ with target $t=4$.
  **Step 1:** Error signal at the output: $\delta=\partial L/\partial o=o-t=-2$.
  > **Why:** Every gradient further back is this number multiplied by a local sensitivity.
  **Step 2:** Score gradients: $g_1=\alpha_1(v_1-o)\,\delta=0.5\cdot(4-2)\cdot(-2)=-2$ and $g_2=\alpha_2(v_2-o)\,\delta=0.5\cdot(0-2)\cdot(-2)=+2$.
  > **Why:** Raising a score moves the output towards that key's value, so what counts is the value *relative to the current output*, not the value itself.
  **Step 3:** Gradient descent lowers the loss by moving against the gradient: $s_1$ goes up, $s_2$ goes down.
  > **Why:** Key 1 holds the value the target wants; the two scores compete for one unit of attention.
  **Result:** $g=(-2,+2)$, summing to zero: attention shifts towards key 1 and away from key 2 by the same amount.
  > **Check:** Directly: $o=4\sigma(s_1-s_2)$ with $\sigma$ the logistic function, so $\partial o/\partial s_1=4\sigma(1-\sigma)=4\cdot0.25=1$ at equal scores, and $\partial L/\partial s_1=\delta\cdot1=-2$. It agrees with Step 2.
- **Initial Test:** A query has scaled scores $(\ln 2,\ 0,\ 0)$ over three keys with scalar values $v=(6,\ 2,\ -2)$. The loss reports $\delta=\partial L/\partial o=+1$ (the output is too high). (a) Compute the three score gradients. (b) Which scores will gradient descent raise? (c) State the rule you used in one sentence, and say what the three gradients add up to and why.
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly ($o=3$; $g=(1.5,\ -0.25,\ -1.25)$; scores 2 and 3 rise, score 1 falls; sum zero because the weights of one query always sum to 1).
- **Estimated Depth:** Master's
- **Exercise:** With $\alpha=(0.5,0.5)$, $v=(10,2)$ and $\delta=-1$, compute $o$ and both score gradients, then repeat with $\alpha=(0.9,0.1)$. Expected outcome: $o=6$, $g=(-2,+2)$; then $o=9.2$, $g=(-0.72,+0.72)$, smaller because the weights are less even.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The gradient uses $v_j-o_i$, the value relative to the current output | Softmax competition gradient | Find a key with large weight and zero score gradient | conflation: using $v_j$ alone, or equating high weight with high gradient |
  | The gradients of one query's scores sum to zero | Softmax competition gradient | Check the row sum in a 3-key case and explain it | procedural-without-conceptual: computes the entries but cannot say why they cancel |
- **Teach Topics:** The softmax derivative $\partial\alpha_j/\partial s_l=\alpha_j(\mathbb{1}[j=l]-\alpha_l)$; assembling $g_{ij}$; the sign convention of gradient descent; row sums zero, column sums in general not; the matrix $G$ of KF-5. Pitfalls: [conflation] weight versus gradient; [verbal-without-formal] "it attends more to useful tokens" with no formula for "useful".
- **Final Test:** A query has weights $\alpha=(0.5,\ 0.25,\ 0.25)$ over keys with two-dimensional values $v_1=(2,0)$, $v_2=(0,4)$, $v_3=(4,4)$, and the error signal is $\delta=(1,0)$. Compute the output and the three score gradients, say which scores gradient descent raises, and explain why the key with the largest weight gets the gradient it gets.

### SG-6: Query–key gradient duality
- **Principle:** Query–key gradient duality — the query matrix is updated with keys weighted along each query's row of score gradients, and the key matrix with queries weighted along each key's column, so each gradient is built from the other matrix and sees the score gradients from the opposite side.
- **Tempting answer:** "Yes, they stay equal. Queries and keys are computed from the same tokens and enter the score through a dot product, which is symmetric, so with equal starting matrices the two gradients are equal at every step and the head is the same as one with a single tied matrix." It feels right because every visible ingredient (the same input $X$, two linear maps of the same shape, a commutative product) is symmetric under exchanging the two matrices.
- **Insight:** The dot product is symmetric but the softmax is not: every query chooses among the keys and no key chooses among the queries, so the asker and the asked receive different sums of the same numbers.
- **Picture:** A square spreadsheet of score gradients, one row per asking token and one column per asked token. The query of token $i$ is corrected by reading **row** $i$ across (its own verdicts on everyone it asked); the key of token $j$ is corrected by reading **column** $j$ down (everyone's verdicts on it). Every row adds up to zero; the columns do not. Where it stops being true: the picture suggests the two matrices use different information, but both use the whole table; and it leaves out that each correction is expressed in the *other* matrix's current vectors.
- **Visual design:**
  - **Objects:** A $2\times2$ table $\hat G=\begin{pmatrix}-1&+1\\0&0\end{pmatrix}$ (gradients with respect to the raw dot products); four arrows in the plane, $q_1=k_1=(1,0)$ and $q_2=k_2=(0,1)$, drawn in coincident pairs; a small readout of the four dot products.
  - **Colour roles:** blue = queries and row reads; orange = keys and column reads; grey = the gradient table itself.
  - **Steps:** (1) The coincident query and key arrows appear. (2) The table $\hat G$ appears. (3) Row 1 lights up and builds the correction to $q_1$ as a weighted sum of keys. (4) Row 2 lights up: zero correction to $q_2$. (5) Column 1 lights up and builds the correction to $k_1$ as a weighted sum of queries; then column 2 for $k_2$. (6) One step is taken and the pairs of arrows separate. (7) Master's rung: the per-vector reads are collected into $W_KM^\top$ and $W_QM$.
  - **Your-turn inputs:** *High school rung:* enter $\partial L/\partial k_2$. Right: $(1,0)$. Wrong $(0,0)$: row 2 was read instead of column 2 (the key was treated as a query). Wrong $(-1,1)$: the gradient of $q_1$ was copied "by symmetry". *Master's rung* (the solved exercise below): enter $\partial L/\partial W_Q$. Right: $(0,\ 0)$. Wrong $(0.5,\ -0.5)$: the key gradient was assumed to hold for the query too. Wrong $(0.25,\ -0.25)$: a single row of $G$ was used instead of the product $W_KM^\top$.
  - **Control:** One slider that blends the table from $\hat G$ towards its symmetric part $\tfrac12(\hat G+\hat G^\top)$. As the table becomes symmetric the two sets of updated arrows come back together; it shows that the separation is caused by the asymmetry of the table and by nothing else.
- **Worked Example (foundational):**
  **Given:** Two tokens whose queries and keys start identical: $q_1=k_1=(1,0)$, $q_2=k_2=(0,1)$. The gradients of the loss with respect to the raw dot products $q_i^\top k_j$ are $\hat G=\begin{pmatrix}-1&+1\\0&0\end{pmatrix}$ (token 1 should attend more to itself and less to token 2; token 2 is already right). Learning rate $\eta=0.1$.
  **Step 1:** Queries read rows: $\partial L/\partial q_1=\hat g_{11}k_1+\hat g_{12}k_2=-(1,0)+(0,1)=(-1,1)$ and $\partial L/\partial q_2=(0,0)$.
  > **Why:** $q_1$ appears only in the dot products of row 1, each time multiplied by a key, so its gradient is a sum of keys weighted by row 1.
  **Step 2:** Keys read columns: $\partial L/\partial k_1=\hat g_{11}q_1+\hat g_{21}q_2=(-1,0)$ and $\partial L/\partial k_2=\hat g_{12}q_1+\hat g_{22}q_2=(1,0)$.
  > **Why:** $k_j$ appears only in the dot products of column $j$, each time multiplied by a query.
  **Step 3:** Update: $q_1=(1.1,-0.1)$, $q_2=(0,1)$; $k_1=(1.1,0)$, $k_2=(-0.1,1)$.
  > **Why:** Subtracting $\eta$ times each gradient is one step of gradient descent.
  **Result:** After one step the queries $\{(1.1,-0.1),(0,1)\}$ and the keys $\{(1.1,0),(-0.1,1)\}$ are no longer equal, although they started equal and the dot product treats them alike.
  > **Check:** The new dot products are $q_1^\top k_1=1.21$ (up from 1, as wanted), $q_1^\top k_2=-0.21$ (down from 0, as wanted), $q_2^\top k_1=0$ and $q_2^\top k_2=1$ (unchanged, as wanted). Second way, to first order: $\Delta(q_1^\top k_1)\approx-\eta\,\hat g_{11}(\lVert k_1\rVert^2+\lVert q_1\rVert^2)=+0.2$, which matches $0.21$ up to the second-order term $0.01$.
- **Level ladder:**
  **Master's solved exercise**
  **Given:** A head with $d=2$, $d_k=1$, $d_v=2$ and tokens $X=I$ (so $x_1=(1,0)$, $x_2=(0,1)$). Equal starting matrices $W_Q=W_K=\begin{pmatrix}1&1\end{pmatrix}$, and $W_V=I$. Loss $L=\sum_i\tfrac12\lVert o_i-t_i\rVert^2$ with $t_1=t_2=(0,1)$: both tokens should output the content of token 2. Find $\partial L/\partial W_Q$ and $\partial L/\partial W_K$.
  **Step 1:** Forward pass: $q_i=1$ and $k_j=1$ for both tokens, so every score is $1$, every weight is $\alpha_{ij}=\tfrac12$, and $o_1=o_2=(0.5,0.5)$. The loss is $0.5$.
  > **Why:** With identical keys the head cannot yet tell the tokens apart, so it averages them.
  **Step 2:** Score gradients: $\delta_i=o_i-t_i=(0.5,-0.5)$; $v_1-o_i=(0.5,-0.5)$ and $v_2-o_i=(-0.5,0.5)$, so $g_{i1}=\tfrac12\cdot0.5=0.25$ and $g_{i2}=\tfrac12\cdot(-0.5)=-0.25$: $G=\begin{pmatrix}0.25&-0.25\\0.25&-0.25\end{pmatrix}$.
  > **Why:** This is the rule of SG-5. Each row sums to zero; the columns sum to $0.5$ and $-0.5$, so $G$ is not symmetric.
  **Step 3:** General formulas. From $q_i=W_Qx_i$: $\partial L/\partial W_Q=\sum_i(\partial L/\partial q_i)\,x_i^\top$ with $\partial L/\partial q_i=\tfrac1{\sqrt{d_k}}\sum_jg_{ij}k_j$, which gives $\tfrac1{\sqrt{d_k}}W_KM^\top$ with $M=X^\top GX$. In the same way $\partial L/\partial W_K=\tfrac1{\sqrt{d_k}}W_QM$.
  > **Why:** The query gradient contains $W_K$ and the transpose of $M$; the key gradient contains $W_Q$ and $M$ itself. Exchanging the roles of the two matrices exchanges rows and columns of the table.
  **Step 4:** Numbers ($\sqrt{d_k}=1$, $M=G$ because $X=I$): $\partial L/\partial W_Q=\begin{pmatrix}1&1\end{pmatrix}G^\top=\begin{pmatrix}0&0\end{pmatrix}$ and $\partial L/\partial W_K=\begin{pmatrix}1&1\end{pmatrix}G=\begin{pmatrix}0.5&-0.5\end{pmatrix}$.
  > **Why:** $W_KM^\top$ adds up each row of $G$ (zero), while $W_QM$ adds up each column (not zero).
  **Result:** From identical starting matrices, the key matrix receives the gradient $(0.5,-0.5)$ and the query matrix receives exactly zero. With $\eta=1$ the step gives $W_K=(0.5,\ 1.5)$ and $W_Q=(1,\ 1)$: token 2's key now scores higher for every query, each token puts weight $0.731$ on token 2, and the loss falls from $0.5$ to $0.145$.
  > **Check:** Perturb directly. Adding $\varepsilon$ to the second entry of $W_K$ gives scores $s_{i2}=1+\varepsilon$, weights $\alpha_{i2}\approx\tfrac12+\tfrac\varepsilon4$, outputs $(\tfrac12-\tfrac\varepsilon4,\ \tfrac12+\tfrac\varepsilon4)$ and $L=2(\tfrac12-\tfrac\varepsilon4)^2$, so $dL/d\varepsilon=-0.5$ at $\varepsilon=0$: it agrees. Adding $\varepsilon$ to the first entry of $W_Q$ makes $q_1=1+\varepsilon$ and both scores of row 1 equal to $1+\varepsilon$; the weights stay $\tfrac12$ and $L$ does not change: gradient 0, in agreement.
- **Initial Test:** To save a random seed, a teammate initialises the two matrices of an untied self-attention head to the same matrix, $W_Q=W_K=W_0$, and trains with plain gradient descent. Their note says the head has separate parameters for queries and keys. (a) Predict whether $W_Q=W_K$ still holds after 1,000 steps, and justify the prediction with the gradients of the first step, written in terms of $W_0$, $X$ and the score-gradient matrix $G$. (b) For $d=d_k=2$, $W_0=I$, $X=I$ and $G=\begin{pmatrix}0.2&-0.2\\-0.1&0.1\end{pmatrix}$ at the first step, give both gradients.
- **Pass Criteria:** Gives the right answer, not the tempting one, AND justifies it at the Target level (the matrices separate at the first step; $\partial L/\partial W_Q=\tfrac1{\sqrt2}G^\top$ and $\partial L/\partial W_K=\tfrac1{\sqrt2}G$ here; they would coincide only if $X^\top GX$ were symmetric, which the row-wise softmax does not provide).
- **Estimated Depth:** Master's
- **Exercise:** With $d=d_k=2$, $X=I$, $W_Q=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $W_K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $G=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$, compute $\sqrt2\,\partial L/\partial W_Q$ and $\sqrt2\,\partial L/\partial W_K$ from the formulas, then recompute the first one as $\sum_i(\sum_jg_{ij}k_j)x_i^\top$. Expected outcome: $W_KG^\top=\begin{pmatrix}-1&0\\1&0\end{pmatrix}$, $W_QG=\begin{pmatrix}1&-1\\0&0\end{pmatrix}$, and the per-token sum reproduces the first matrix.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | A query's gradient is a row-weighted sum of keys; a key's gradient is a column-weighted sum of queries | Query–key gradient duality, High school rung | From a $2\times2$ table and four vectors, compute one query gradient and one key gradient | conflation: reading a row for a key, or copying the query's gradient to the key |
  | $\partial L/\partial W_Q=\tfrac1{\sqrt{d_k}}W_KM^\top$ and $\partial L/\partial W_K=\tfrac1{\sqrt{d_k}}W_QM$ with $M=X^\top GX$ | Query–key gradient duality, Master's rung | Derive both formulas from $q_i=W_Qx_i$, $k_j=W_Kx_j$ and apply them to given matrices | procedural-without-conceptual: applies the formulas but cannot say where the transpose comes from |
  | The two gradients differ because $G$ is not symmetric, and $G$ is not symmetric because the softmax normalises over keys only | Query–key gradient duality, Master's rung | Explain why equal matrices do not stay equal, naming the source of the asymmetry | formal-without-intuitive: shows $M\ne M^\top$ numerically without linking it to the row-wise softmax |
- **Teach Topics:** Per-vector gradients (rows for queries, columns for keys); collecting them into $W_KM^\top$ and $W_QM$; each gradient is proportional to the other matrix; the source of the asymmetry of $G$; boundary conditions: the formulas are for a single head without biases under the convention of KF-2, and the "same input" premise is specific to self-attention (KF-6). Misunderstandings that survive the Insight: [overgeneralization] "the query matrix always gets the smaller gradient" (a feature of one example, not of the principle); [conflation] the asymmetry of $G$ with an asymmetry of the data.
- **Final Test:** A classifier reads its prediction from the last token only, so only $\delta_3\neq0$ and only the last row of $G$ is non-zero: with three tokens $x_1=(1,0)$, $x_2=(0,1)$, $x_3=(1,1)$, $d=d_k=2$ and $W_Q=W_K=I$, the last row of $G$ is $(0.3,\ -0.1,\ -0.2)$. A reviewer writes: "the two matrices are equal and play symmetric parts in the score, so they receive the same gradient; we can tie them at no cost". (a) Predict whether the two gradients are equal and justify it. (b) Compute both gradients. (c) Say which tokens each gradient is built from.

### SG-7: Matrix-form forward pass
- **Initial Test:** A head has $d=2$, $d_k=2$, $d_v=1$ with $W_Q=\sqrt2\,I$, $W_K=I$, $W_V=\begin{pmatrix}1&-1\end{pmatrix}$, and receives three tokens $X=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$. (a) Compute $Q$, $K$, $V$, the score matrix $S$, the attention matrix and the output, to three decimals. (b) For the base configuration of KF-3 and a sequence of $n=128$ tokens, give the shapes of $Q$, $K$, $V$, $S$ and the output of one head.
- **Pass Criteria:** $S=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$; attention rows $(0.422,0.155,0.422)$, $(0.155,0.422,0.422)$, $(0.212,0.212,0.576)$; output $(0.267,\ -0.267,\ 0)$, all within $\pm0.005$; and all five shapes correct ($128\times64$ three times, $128\times128$, $128\times64$).
- **Estimated Depth:** Master's
- **Principle:** Soft lookup, Variance scaling
- **Exercise:** For $X=I_2$, $W_Q=W_K=I_2$, $W_V=\begin{pmatrix}3&0\\0&5\end{pmatrix}$, write out $S$, the attention matrix and the output by hand. Expected outcome: $S=I/\sqrt2$; each token puts $0.670$ on itself and $0.330$ on the other; output rows $(2.01,\ 1.65)$ and $(0.99,\ 3.35)$.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | $S=QK^\top/\sqrt{d_k}$ is $n\times n$ with rows indexed by queries | Matrix form | Say what entry $(3,1)$ of $S$ means | conflation: rows and columns of $S$ exchanged, or a column-wise softmax |
  | Shapes follow from $Q=XW_Q^\top$ etc. under KF-2 | Matrix form | Give all shapes for given $n,d,d_k,d_v$ | missing-prerequisite: matrix shape bookkeeping |
  | The matrix form is the per-token rule applied to all tokens at once | Soft lookup | Recover one output row from the per-token formula | procedural-without-conceptual: multiplies matrices without linking them to the weighted average |
- **Teach Topics:** From per-token to matrix form; shape bookkeeping; which axis the softmax runs over; where $\sqrt{d_k}$ sits; the output as attention matrix times $V$. Pitfalls: [conflation] query axis versus key axis; [missing-prerequisite] transposes under the convention of KF-2.
- **Final Test:** A head has $d=2$, $d_k=4$, $d_v=2$, tokens $X=I_2$, $W_Q=\begin{pmatrix}1&0\\0&1\\1&0\\0&1\end{pmatrix}$, $W_K=\begin{pmatrix}0&1\\1&0\\0&1\\1&0\end{pmatrix}$, $W_V=I_2$. Compute $S$, the attention matrix and the output, describe in one sentence what the head does, and give the shape of $S$ for a batch of 16 sequences of 50 tokens.

### SG-8: Saturation and vanishing score gradients
- **Initial Test:** A training log shows a head whose attention rows are almost one-hot from the first step, and whose $W_Q$ and $W_K$ barely move while $W_V$ trains normally. The head has $d_k=64$ (KF-3) and the code omits the $\sqrt{d_k}$ division. For a query with two keys and score gap $\Delta$: (a) express the sensitivity of the larger weight to its score in terms of that weight; (b) evaluate it for $\Delta=8$ (unscaled) and $\Delta=1$ (scaled) and give the ratio; (c) explain the log, including why $W_V$ is unaffected.
- **Pass Criteria:** Gives $\partial\alpha/\partial s=\alpha(1-\alpha)$; values about $3.4\times10^{-4}$ and $0.197$, ratio about 590 (each within 10%); and links the stalled matrices to the factor $\alpha_{ij}(v_j-o_i)$ in the score gradient, which the path to $W_V$ does not contain.
- **Estimated Depth:** Master's
- **Principle:** Variance scaling, Softmax competition gradient
- **Exercise:** Tabulate $\alpha$ and $\alpha(1-\alpha)$ for two keys with gaps $\Delta=0,2,4,8$. Expected outcome: $\alpha=0.5,\ 0.881,\ 0.982,\ 0.9997$ and $\alpha(1-\alpha)=0.25,\ 0.105,\ 0.018,\ 0.0003$.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Score gradients carry a factor that vanishes when a row is one-hot | Softmax competition gradient | Show $g_{ij}\to0$ for every $j$ in a saturated row | verbal-without-formal: "the softmax saturates" with no expression for the gradient |
  | The size of the gap is set by score scale, hence by $d_k$ and the scaling | Variance scaling | Predict the typical gap with and without scaling for a given $d_k$ | conflation: sharp attention (a trained property) with saturation at initialisation |
  | The effect is specific to the path through the scores | Both | Say which of $W_Q$, $W_K$, $W_V$ stall and why | overgeneralization: "all gradients vanish" |
- **Teach Topics:** The two-key case as a logistic function; the factor $\alpha(1-\alpha)$ and its general form in $g_{ij}$; why both the dominant key ($v_j\approx o_i$) and the others ($\alpha_{ij}\approx0$) get near-zero gradient; temperature as the same knob; limits of KF-4 in trained heads. Pitfalls: [overgeneralization] to the value path; [conflation] learned sharpness versus initial saturation.
- **Final Test:** A colleague adds a learnable temperature $\tau$, with scores divided by $\tau$, and initialises $\tau=0.05$ on a head that already uses the $\sqrt{d_k}$ scaling under KF-4. For two keys one standard deviation apart, compute the larger weight and the sensitivity factor, compare them with $\tau=1$, and predict what the first thousand steps of training look like for $W_Q$, $W_K$ and $W_V$.

### SG-9: What separate queries and keys can express
- **Initial Test:** In "the animal was tired because it slept badly", a head should make "it" attend strongly to "animal", while "animal" should not attend to "it". To halve the parameters, a teammate ties the matrices, $W_Q=W_K=W$. (a) Write the score matrix of the tied head and state its two structural properties. (b) Prove or refute: a tied head can make token 1 score token 2 higher than itself *and* token 2 score token 1 higher than itself. (c) For the base configuration (KF-3), give the maximum rank of the matrix that sets the scores in an untied head, and compare it with $d_\text{model}$.
- **Pass Criteria:** All three: (a) $S=XW^\top WX^\top/\sqrt{d_k}$ is symmetric and positive semi-definite; (b) refuted with a valid argument ($s_{12}\le\sqrt{s_{11}s_{22}}\le\max(s_{11},s_{22})$ by Cauchy–Schwarz); (c) rank at most 64, against 512.
- **Estimated Depth:** Master's
- **Principle:** Role separation
- **Exercise:** For one-hot tokens and $W_Q=I$, $W_K=\begin{pmatrix}0&0\\3&0\end{pmatrix}$, write $W_Q^\top W_K$ and read off the four raw scores; then say what swapping the two matrices does to the scores. Expected outcome: only the score of token 2 against token 1 is non-zero (3); after the swap the score matrix is transposed, so token 1 scores token 2 instead.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Scores are directional when $W_Q^\top W_K$ is not symmetric | Bilinear form | Build a $2\times2$ example with $s_{12}\ne s_{21}$ | conflation: asymmetric scores versus asymmetric attention weights (the softmax alone already makes the weights asymmetric) |
  | Tying forces a symmetric positive semi-definite form, which bounds off-diagonal scores | Tied head | Prove the bound $s_{ij}\le\max(s_{ii},s_{jj})$ | formal-without-intuitive: proves the bound without stating what a tied head cannot do |
  | The form has rank at most $d_k$ | Low rank | Give the rank bound for given $d$, $d_k$ and say what it restricts | overgeneralization: "a head can implement any pairwise relation between tokens" |
- **Teach Topics:** The matrix $A=W_Q^\top W_K$ and its symmetric and antisymmetric parts; the tied case as a Gram matrix; the Cauchy–Schwarz bound and its meaning; rank at most $d_k$ and the subspaces the head reads; swapping the matrices transposes $A$; self- versus cross-attention (KF-6). Pitfalls: [conflation] asymmetry of scores versus asymmetry of weights; [overgeneralization] of expressive power.
- **Final Test:** A head is meant to implement "every closing bracket attends to its opening bracket, and opening brackets attend only to themselves". With one-hot tokens for "(" and ")" and $d_k=2$, give a pair $(W_Q,W_K)$ whose raw scores do this, show that no tied head can, and state what happens to the behaviour if the two matrices are exchanged.

### SG-10: The value gradient and its path
- **Initial Test:** A head with $X=I_2$ and $W_V=I_2$ currently has attention matrix $\begin{pmatrix}0.5&0.5\\0.1&0.9\end{pmatrix}$ and receives the error signals $\delta_1=(1,0)$ and $\delta_2=(0,-1)$. (a) Derive a formula for $\partial L/\partial W_V$ in terms of the error signals, the attention matrix and $X$. (b) Evaluate it. (c) Compute $G$. (d) Compare the two paths: which of the two gradients would survive if the second row of the attention matrix became $(0,1)$?
- **Pass Criteria:** Formula $\partial L/\partial W_V=\sum_j(\sum_i\alpha_{ij}\delta_i)x_j^\top=\Delta^\top\!\mathcal{A}X$ (with $\Delta$ the matrix of rows $\delta_i^\top$ and $\mathcal{A}$ the attention matrix); value $\begin{pmatrix}0.5&0.5\\-0.1&-0.9\end{pmatrix}$; $G=\begin{pmatrix}0.25&-0.25\\0.09&-0.09\end{pmatrix}$; and the statement that row 2 of $G$ vanishes in the limit while the value gradient does not.
- **Estimated Depth:** Master's
- **Principle:** Soft lookup, Softmax competition gradient
- **Exercise:** With attention matrix $\begin{pmatrix}1&0\\0.5&0.5\end{pmatrix}$, $X=I_2$, $\delta_1=(2,0)$, $\delta_2=(0,2)$, compute $\partial L/\partial v_1$, $\partial L/\partial v_2$ and $\partial L/\partial W_V$. Expected outcome: $\partial L/\partial v_1=(2,1)$, $\partial L/\partial v_2=(0,1)$, $\partial L/\partial W_V=\begin{pmatrix}2&0\\1&1\end{pmatrix}$.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | A value's gradient is the attention-weighted sum of the error signals of the tokens that read it | Value path | Compute $\partial L/\partial v_j$ from a given attention column | conflation: summing along a row instead of a column |
  | The value path is linear in the weights and has no softmax derivative | Path comparison | Say which gradient survives one-hot attention | overgeneralization: carrying the saturation argument over to $W_V$ |
  | Both paths start from the same $\delta_i$ | Backpropagation | Draw the two branches from $o_i$ back to $W_V$ and to $S$ | procedural-without-conceptual: two formulas with no common origin |
- **Teach Topics:** The output as a product of attention matrix and $V$; the two branches of the chain rule; assembling $\Delta^\top\!\mathcal{A}X$; the contrast with $G$ under saturation; what "what to carry" means in gradient terms. Pitfalls: [conflation] row versus column sums of the attention matrix; [overgeneralization] of vanishing gradients.
- **Final Test:** A head attends uniformly over $n=4$ tokens (all weights ¼) and only $\delta_1\ne0$. Give $\partial L/\partial W_V$ in terms of $\delta_1$ and the tokens, state what feature of the input it depends on, and explain what $W_V$ learns in a head whose queries and keys are frozen at zero.

### SG-11: The first step under equal, zero and tied initialisations
- **Initial Test:** Three initialisation proposals are on the table for a new self-attention head: (i) $W_Q=0$ with $W_K$ random, "for stability"; (ii) $W_Q=W_K=0$; (iii) one tied matrix $W$ used for both, random. For each: (a) give $\partial L/\partial W_Q$ and $\partial L/\partial W_K$ at the first step, in terms of $M$; (b) say which matrices move at the first step and what the attention pattern is at that moment; (c) say whether the head can ever learn where to look. For (iii), derive the gradient of the single matrix $W$.
- **Pass Criteria:** At least 5 of 6 correct: (i) $\partial L/\partial W_K=0$, $\partial L/\partial W_Q=W_KM^\top/\sqrt{d_k}\neq0$ in general, uniform attention, only $W_Q$ moves first and the head then learns; (ii) both gradients zero at every step, the pattern stays uniform, only $W_V$ learns; (iii) $\partial L/\partial W=W(M+M^\top)/\sqrt{d_k}$, driven by the symmetric part of $M$ only.
- **Estimated Depth:** Master's
- **Principle:** Softmax competition gradient, Query–key gradient duality
- **Exercise:** For $W_Q=W_K=W$, write $\partial L/\partial W_Q-\partial L/\partial W_K$ in terms of $M$, then evaluate it for $W=I$, $d_k=2$ and $M=\begin{pmatrix}0.4&-0.4\\0.2&-0.2\end{pmatrix}$. Expected outcome: $W(M^\top-M)/\sqrt{d_k}=\tfrac1{\sqrt2}\begin{pmatrix}0&0.6\\-0.6&0\end{pmatrix}$, an antisymmetric matrix.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Each gradient is proportional to the other matrix, so a zero matrix blocks its partner | Duality | Predict which matrix moves when one of the two is zero | conflation: "a zero matrix has zero gradient" (it is the partner's gradient that is zero) |
  | Equal untied matrices separate through the antisymmetric part of $M$ | Symmetry breaking | Express the difference of the gradients for equal matrices | formal-without-intuitive: writes $M^\top-M$ without tying it to the row-sum property of $G$ |
  | A tied matrix sees only the symmetric part of $M$ | Tied gradient | Derive the gradient of $W$ in the tied head | procedural-without-conceptual: forgets that $W$ appears twice in the score |
  | Both matrices at zero is a stationary point for the pattern, not for the head | Saddle | Say what still learns in case (ii) | overgeneralization: "the head is dead" |
- **Teach Topics:** Reading the two formulas as "each needs the other"; the difference $W(M^\top-M)/\sqrt{d_k}$; why $G$ symmetric would require zero column sums; the tied head and the product rule; the zero–zero saddle and what breaks it; link to common practice (small random initialisation of both). Pitfalls: [conflation] whose gradient vanishes; [overgeneralization] from one example to all initialisations.
- **Final Test:** A paper proposes "mirror initialisation", $W_K=-W_Q$, claiming it starts each token attending away from itself and trains like any other scheme. For a head with $W_Q=W_0$, $W_K=-W_0$: give both first-step gradients in terms of $W_0$ and $M$, state the condition under which the relation $W_K=-W_Q$ would survive the step, decide whether it does in general, and describe the starting attention pattern for one-hot tokens with $W_0=I$.

### SG-12: What gradient flow conserves between queries and keys
- **Initial Test:** A training run uses plain gradient descent with a very small learning rate and no weight decay. At initialisation the Frobenius norms of one head's matrices are $\lVert W_Q\rVert_F=3.0$ and $\lVert W_K\rVert_F=4.0$. Later the log shows $\lVert W_Q\rVert_F=5.0$. (a) Using the gradient formulas, compute $\tfrac{d}{dt}\big(W_QW_Q^\top\big)$ and $\tfrac{d}{dt}\big(W_KW_K^\top\big)$ under gradient flow and compare them. (b) Predict $\lVert W_K\rVert_F$ at the later time. (c) Relate the conserved quantity to the family of equivalent heads of SG-4. (d) Name two common training choices under which the prediction fails.
- **Pass Criteria:** Shows that both derivatives equal $-\tfrac1{\sqrt{d_k}}\big(W_KM^\top W_Q^\top+W_QMW_K^\top\big)$, hence $W_QW_Q^\top-W_KW_K^\top$ is constant; predicts $\lVert W_K\rVert_F=\sqrt{32}\approx5.66$ (within 2%); links the conservation to the freedom $W_Q\to RW_Q$, $W_K\to R^{-\top}W_K$; and names two of: finite or large learning rate, weight decay, adaptive optimisers such as Adam.
- **Estimated Depth:** Master's
- **Principle:** Role separation, Query–key gradient duality
- **Exercise:** For $d_k=1$, $W_Q=W_K=(1,\ 1)$, $\partial L/\partial W_Q=(0,\ 0)$ and $\partial L/\partial W_K=(0.5,\ -0.5)$, compute $W_K\cdot\partial L/\partial W_K$ and $W_Q\cdot\partial L/\partial W_Q$; then take one step with $\eta=1$ and compute $\lVert W_Q\rVert^2-\lVert W_K\rVert^2$ before and after. Expected outcome: both inner products are 0, so the difference is conserved to first order; after the finite step it moves from $0$ to $-0.5$, which equals $-\eta^2\lVert\partial L/\partial W_K\rVert^2$, a second-order effect.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | $W_QW_Q^\top-W_KW_K^\top$ is constant under gradient flow | Conservation | Carry out the two-line derivation from the gradient formulas | procedural-without-conceptual: derives it without being able to use it on norms |
  | The conservation is the training-time counterpart of the head's reparametrisation freedom | Role separation | Explain why the loss cannot push along directions that leave $W_Q^\top W_K$ unchanged | formal-without-intuitive: treats the result as an isolated identity |
  | It is exact only for gradient flow | Limits of validity | Compute the second-order violation for one finite step | overgeneralization: applying it to Adam or to runs with weight decay |
- **Teach Topics:** Gradient flow as the small-step limit; the derivation; the trace as a statement about norms; meaning: the two matrices grow together and differ in direction, not in overall size, beyond their initial imbalance; connection to the equivalent-heads family; limits of validity. Pitfalls: [overgeneralization] to other optimisers; [conflation] "conserved difference of Gram matrices" with "equal matrices".
- **Final Test:** Two heads are initialised with the same product $W_Q^\top W_K$ but different balance: head A has $\lVert W_Q\rVert_F=\lVert W_K\rVert_F=2$; head B has $\lVert W_Q\rVert_F=20$ and $\lVert W_K\rVert_F=0.2$. Both are trained by gradient flow. Compare the sizes of the first-step gradients of the two matrices in each head using the duality formulas, state what stays constant in each head during training, and predict which head's function changes faster at the start and through which matrix.

### SG-13: Numerical gradient checking
- **Initial Test:** You have derived $\partial L/\partial W_Q$, $\partial L/\partial W_K$ and $\partial L/\partial W_V$ for a single head with loss $L=\tfrac12\lVert O-T\rVert_F^2$. Write a script (NumPy or PyTorch, about 30 lines) that draws random $X$, $T$ and weights with $n=4$, $d=3$, $d_k=2$, $d_v=3$, computes the three analytic gradients from your formulas, and checks each against central finite differences. Report the maximum relative error for each matrix, and say how you chose the step size.
- **Pass Criteria:** The script runs; all three relative errors are below $10^{-5}$ in double precision; the step size is justified (truncation error against round-off, a value near $10^{-5}$–$10^{-6}$); and the comparison is done entry by entry or with a relative norm, not by eye.
- **Estimated Depth:** Master's
- **Principle:** Query–key gradient duality
- **Exercise:** For the scalar function $f(s)=1/(1+e^{-s})$ at $s=1$, compute the central difference with $h=10^{-1}$, $10^{-5}$ and $10^{-12}$ and compare each with $f(1)\,(1-f(1))=0.19661$. Expected outcome: the middle step agrees to about 10 digits; the large step shows truncation error in the fourth decimal (about $0.19655$); the tiny step shows round-off noise.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | A central difference approximates one entry of the gradient to second order in the step | Finite differences | Write the central-difference formula for entry $(a,b)$ of $W_Q$ | missing-prerequisite: forward differences or single precision giving false alarms |
  | The check compares against the stated layout and convention | KF-2, KF-5 | Detect a transposed gradient with the script | conflation: a transpose error mistaken for a wrong derivation |
  | A passing check on equal matrices needs care | Duality | Explain why testing with $W_Q=W_K$ and a symmetric-looking setup can hide an exchanged formula, and choose a better test | overgeneralization: "it passed once, so the formula is right" |
- **Teach Topics:** Central differences and their error; choosing the step; relative error; testing with generic random inputs so that $M\ne M^\top$; the same check with automatic differentiation (`requires_grad`, `.backward()`); reading a failure (transpose, missing $1/\sqrt{d_k}$, wrong softmax axis). Pitfalls: [conflation] convention error versus derivation error; [overgeneralization] from one passing test.
- **Final Test:** A colleague's implementation of the three gradients passes their own check but training diverges. Their check uses $n=2$, $X=I$, $W_Q=W_K=I$ and only the output of token 1 in the loss. Explain what such a check can fail to detect, design a check that would catch an exchange of $M$ and $M^\top$ and a missing $1/\sqrt{d_k}$, run it on your own script with each bug planted in turn, and report the relative errors you observe.

### SG-14: Capstone — one head, end to end
- **Initial Test:** A head has $d=2$, $d_k=1$, $d_v=1$, tokens $x_1=(1,0)$, $x_2=(0,1)$, weights $W_Q=(1,\ 0)$, $W_K=(0,\ \ln 3)$, $W_V=(2,\ 6)$, and loss $L=\tfrac12(o_1-6)^2$ on the output of token 1 only. (a) Compute scores, attention weights and outputs. (b) Compute $G$, then $\partial L/\partial W_Q$, $\partial L/\partial W_K$ and $\partial L/\partial W_V$. (c) Take one gradient step with $\eta=0.5$ and recompute $o_1$ and $L$. (d) Explain in a short paragraph what each of the three updates did, which of them changed *where* token 1 looks and which changed *what* it receives, and why the query and key updates are not the same matrix. (e) Give a second pair $(W_Q',W_K')$ that defines the same head, and say whether it would receive the same updates.
- **Pass Criteria:** At least 4 of the 5 parts correct, with (b) among them: numerical results within 2% (forward: $\alpha_1=(0.25,0.75)$, $o_1=5$; $G$ with first row $(0.75,-0.75)$ and second row zero; $\partial L/\partial W_Q=(-0.75\ln3,\ 0)$, $\partial L/\partial W_K=(0.75,\ -0.75)$, $\partial L/\partial W_V=(-0.25,\ -0.75)$); the loss is lower after the step; the explanation separates the pattern (queries and keys) from the content (values) and attributes the difference of the two gradients to rows versus columns of $G$ and to each gradient containing the other matrix; (e) a valid rescaled pair with the statement that its updates differ.
- **Estimated Depth:** Master's
- **Principle:** Soft lookup, Variance scaling, Role separation, Softmax competition gradient, Query–key gradient duality
- **Exercise:** Before the session, write on one page, from memory, the forward formula, the score-gradient rule, the three weight gradients and the conserved quantity, each with the shape of every symbol. Then check the page against your notes from SG-2 to SG-12. Expected outcome: six formulas with consistent shapes under KF-2 and KF-5.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The whole chain from tokens to weight gradients can be executed without a reference | All principles | Complete parts (a)–(c) by hand | procedural-without-conceptual: correct numbers with no interpretation |
  | "Where" and "what" are learned through different paths | Role separation, value path | Attribute each update to the pattern or to the content | conflation: crediting the value update with a change of pattern |
  | The query and key matrices are distinguished by their gradients, not by the score formula | Query–key gradient duality | Explain part (d) with reference to $G$ | verbal-without-formal: "queries ask and keys answer" with no gradient argument |
  | Equivalent heads are the same function but not the same training trajectory | Role separation, conservation | Answer part (e) | overgeneralization: "same function, so same updates" |
- **Teach Topics:** Assembling the full pipeline; a checklist for shapes and conventions; interpreting each gradient; common end-to-end slips. Pitfalls: [conflation] pattern versus content; [verbal-without-formal] role labels in place of gradient arguments; [overgeneralization] from function equivalence to training equivalence.
- **Final Test:** A head has $d=2$, $d_k=1$, $d_v=1$, tokens $x_1=(1,0)$, $x_2=(0,1)$, weights $W_Q=(0,\ 1)$, $W_K=(\ln 4,\ 0)$, $W_V=(10,\ 0)$, and loss $L=\tfrac12(o_2-2)^2$ on the output of token 2 only. Carry out the same five parts: forward pass; $G$ and the three weight gradients; one step with $\eta=0.1$ and the new loss; a written interpretation of the three updates; and an equivalent pair $(W_Q',W_K')$ with a statement on whether its updates coincide with the original ones.

## Artefacts Register
> _Visible anchor for every artefact this course produces. Seeded at plan
> creation and updated as sessions run — each artefact is reusable context._

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| Transformer Attention — Queries, Keys, Values and Their Gradients | plan | — | transformer-attention_training_plan.md | current |
| Session transcript SG-6 | transcript | SG-6 | transformer-attention_session_SG6.md | current |
| Concept report: query–key gradient duality | concept-file | SG-6 | concept-machine-learning-query-key-gradient-duality.md | current |
| Exercise book SG-6 | deliverable | SG-6 | transformer-attention_artefact_SG6_exercises.md | current |
| Interactive page: rows and columns of G | visual | SG-6 | transformer-attention_visual_SG6.html | current |
| Interactive page: why attention | visual | SG-1 | transformer-attention_visual_SG1.html | current |
| Learner profile | profile | — | learner_profile.md | current |

## Progress Log
(updated by /run-session)

### SG-6 -- Completed 2026-11-13
- Initial Test: FAIL (fell for the Tempting answer: predicted W_Q = W_K persists and gave G/√2 for both gradients; the key gradient was right, the query gradient was not)
- Gaps found: [conflation] the query gradient taken to be the key gradient (row read and column read of G treated as the same), from the symmetry of the dot product
- Teach Phase: 1 explanation delivered (0 abbreviated, 0 full, 0 comparison, 1 ladder), start rung High school
- Final Test: PASS (not equal, justified through M ≠ Mᵀ; both gradients correct; tokens behind each gradient identified; rank-1 structure noted)
- Loops: 0
- Level reached: Master's (session level: Master's)
- Delivery: visual (transformer-attention_visual_SG6.html)
- Concept Map: not generated
- Concept File: concept-machine-learning-query-key-gradient-duality.md
- Exercise Book: transformer-attention_artefact_SG6_exercises.md
- Worked Example: delivered as teaching
- Notes: High school rung held at the first try; Master's rung held after one replay (2 tries), confirmed in chat with a correct explanation of the M / Mᵀ swap. SG-6 was run before its prerequisites SG-4 and SG-5; no prerequisite gap showed. The page was delivered as a local file (hosted publishing was not approved) and its numbers were checked by hand, not by machine.


### SG-1 -- Completed 2026-11-13
- Initial Test: not attempted ("not familiar" with C and LSTM; both terms clarified)
- Gaps found: prerequisite outside the plan (recurrent networks); the learner chose to continue
- Teach Phase: 1 explanation delivered ("not familiar"), on an interactive page
- Final Test: not taken (waived at the learner's request; completion rests on the page checks)
- Loops: 0
- Delivery: visual (transformer-attention_visual_SG1.html)
- Page checks: path length correct at try 1; cost correct at try 3; found by content correct at try 1
- Concept Map: not generated
- Concept File: none
- Exercise Book: none (Motivation sub-goal)
- Notes: Cost scaling (n squared) took three tries and was not confirmed in chat: revisit it in SG-7. The page gave no visible next step; the learner took its checks to be the test.
