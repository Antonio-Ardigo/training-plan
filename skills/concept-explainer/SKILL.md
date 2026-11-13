---
description: "Concept explanation methodology for TTT sessions. Use when generating teaching content during the Teach phase, when a learner requests a deep-dive into a taught principle, when gaps involve distinguishing two concepts (comparison), or when generating concept maps and CTQ mastery criteria."
---

# Concept Explainer -- Domain Knowledge

Reference knowledge for generating rich, principle-first concept explanations within TTT sessions. Replaces simple teaching blocks with structured concept breakdowns when appropriate, while preserving the gap-driven, one-at-a-time delivery model of TTT.

## Standalone Invocation Rule

When this skill is invoked directly (e.g., via `/training-plan:concept-explainer` or when a learner declares "not familiar" with a topic), ALWAYS deliver the **Full 7-Section Concept Explanation** at the Master's level (the default) or at the level the user names (High school, Master's or Advanced). NEVER use the abbreviated form for standalone invocations -- the abbreviated form is reserved exclusively for simple gaps within TTT session Teach phases. A standalone concept explanation must include all 7 sections: The Problem, Core Principles, Key Innovations, Worked Example, Intuitive Formalization, CTQ Mapping, and Conceptual Map.

## The 7-Section Concept Explanation Structure

Every concept explanation follows this structure (7 sections). Sections may be abbreviated or omitted based on the adaptive depth logic below, but the Worked Example (3.5) is ALWAYS included -- it is the core teaching artifact.

### Section 1: The Problem

What observation, need, or contradiction made this concept necessary?

- What was broken, paradoxical, or limiting?
- What did people try before, and why did it fail?
- What was at stake -- practical, theoretical, or both?

Write 1-3 paragraphs in plain language. The learner should feel the tension the concept resolves.

**Within TTT**: Frame the problem in terms of the learner's gap. "You got this wrong because [gap]. Here's why that matters..."

### Section 2: Core Principles (3-5 principles)

For each principle:

```markdown
### Principle N: [Name]
**Statement**: [One clear sentence]
**Formally**: $$[LaTeX equation]$$
**Example**: [Concrete, vivid illustration]
```

Order from most fundamental to most derived. At the High school level, omit the **Formally** line.

### Section 3: Key Innovations (2-4 innovations)

```markdown
### [Innovation Name] ([Person/Group], [Year/Era])
**What**: [What was introduced or discovered]
**Why it mattered**: [What problem it solved, what it unlocked]
**Example**: [Concrete worked illustration]
```

Order chronologically or by logical dependency.

### Section 3.5: Worked Example

A FULLY DEVELOPED example that walks through the concept from start to finish. Every intermediate step is shown and annotated. Nothing is skipped. Nothing is left as "exercise for the reader."

The worked example is the heart of the teaching block. It must be:
- **Complete**: every algebraic step, every matrix multiplication, every word transformation -- shown explicitly
- **Annotated**: each step has a note explaining WHY that step is taken, not just WHAT is done
- **Domain-appropriate**: the format adapts to the domain (see domain templates below)

```markdown
### Worked Example: [Title describing the specific scenario]

**Given**: [All input data, clearly stated with units]

**Step 1**: [Name of this step]
$$[LaTeX showing the operation]$$
> **Why**: [1-2 sentences explaining why this step is needed and what it accomplishes]
> **Note**: [Optional: gotcha, unit warning, common mistake at this step]

**Step 2**: [Name of this step]
$$[LaTeX showing the operation, with intermediate result]$$
> **Why**: [Explanation]

**Step 3**: [Continue until the final result]
$$[Final result with units]$$
> **Check**: [How to verify this result makes sense -- sanity check, order of magnitude, dimensional analysis]

**Result**: [Final answer, boxed or bold, with units and interpretation]
```

**Rules for worked examples:**
- NEVER skip intermediate steps. If a step involves expanding $(a+b)^2$, write $a^2 + 2ab + b^2$ explicitly.
- NEVER write "it can be shown that" or "after simplification" -- show the simplification.
- Every variable must be defined on first use with its units.
- The "Why" annotation explains the REASONING, not just restates the math in words.
- The "Note" annotation flags traps: unit mismatches, sign conventions, boundary conditions.
- ALWAYS end with a **Check** that confirms the result a second way: units or dimensions, a limiting or special case, substituting the result back, an independent method, or an order-of-magnitude estimate. A line that only restates the result is not a Check. This applies to every worked example and to every worked solution of an exercise.
- At the High school level: use concrete numbers throughout, minimize symbols.
- At the Master's level: start with symbols, substitute numbers, show both.
- At the Advanced level: prove each step, show alternative approaches, discuss edge cases.

#### Domain Templates

**Mathematics / Physics / Engineering:**
Show every algebraic manipulation, every matrix operation, every integral evaluation. Use LaTeX for all expressions. Annotate each transformation.

```markdown
**Step 2**: Multiply the matrices
$$\mathbf{A}\mathbf{B} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$

Row 1: $1 \times 5 + 2 \times 6 = 5 + 12 = 17$
Row 2: $3 \times 5 + 4 \times 6 = 15 + 24 = 39$

$$\mathbf{A}\mathbf{B} = \begin{pmatrix} 17 \\ 39 \end{pmatrix}$$

> **Why**: Matrix-vector multiplication gives us the transformed coordinates. Each row of $\mathbf{A}$ acts as a weight vector that linearly combines the input components.
> **Note**: Row-by-column, NOT element-wise. A common error is multiplying corresponding elements (Hadamard product), which is a different operation.
```

**Language Learning / Translation:**
Show word-by-word breakdown, morphological analysis, grammatical annotations, then natural translation.

```markdown
**Step 1**: Word-by-word analysis
| Original | Root | Grammar | Literal meaning |
|----------|------|---------|-----------------|
| Il | -- | definite article, masc. sing. | the |
| ragazzo | ragazzo | noun, masc. sing. | boy |
| mangia | mangiare | verb, 3rd pers. sing., presente indicativo | eats |
| la | -- | definite article, fem. sing. | the |
| mela | mela | noun, fem. sing. | apple |

> **Why**: Italian word order here is SVO (Subject-Verb-Object), same as English. The article agrees in gender with its noun: "il" (masc.) for "ragazzo", "la" (fem.) for "mela".
> **Note**: "Mangia" alone tells you the subject is he/she/it -- Italian often drops the pronoun entirely ("Mangia la mela" = "[He] eats the apple").

**Step 2**: Structural translation
Il ragazzo | mangia | la mela
The boy    | eats   | the apple

**Result**: "The boy eats the apple."
```

**Cost Engineering / Business:**
Show every line item, every subtotal, every percentage application with the base it applies to. Use SI/ISO units throughout (kg, m, m2, m3, t for tonnes).

```markdown
**Step 1**: Calculate direct costs
| Item | Quantity | Unit | Rate | Cost |
|------|----------|------|------|------|
| Concrete | 450 | m3 | $180/m3 | $81,000 |
| Rebar | 38.0 | t | $2,100/t | $79,800 |
| Formwork | 1,200 | m2 | $45/m2 | $54,000 |
| **Direct subtotal** | | | | **$214,800** |

> **Why**: Each line is Quantity x Unit Rate. Units must cancel: m3 x $/m3 = $.
> **Note**: Verify that your rate card units match your quantity takeoff units. Rebar may come in kg or tonnes (1 t = 1,000 kg) -- always confirm which unit the rate card uses and convert if necessary.

**Step 2**: Add indirect costs (itemized, NOT a percentage)
| Item | Basis | Cost |
|------|-------|------|
| Site security | 6 months x $4,500/month | $27,000 |
| Builder's risk insurance | 0.8% of direct costs | $1,718 |
| Mob/demob | lump sum | $35,000 |
| **Indirect subtotal** | | **$63,718** |

> **Why**: Indirects are project-wide costs not traceable to a single scope item. Each must be estimated individually -- never use a blanket percentage.
> **Note**: Insurance is calculated on direct costs ($214,800 x 0.008 = $1,718), not on the total. Applying it to the total including itself creates a circular reference.
```

**Computer Science / Programming:**
Show every line of logic, every variable state change, every iteration of a loop.

```markdown
**Step 1**: Initialize variables
```
array = [3, 1, 4, 1, 5]
n = 5
swapped = True
```
> **Why**: Bubble sort needs a flag to know when to stop. If no swaps occur in a full pass, the array is sorted.

**Step 2**: First pass (i = 0)
```
Compare array[0]=3 and array[1]=1 --> 3 > 1, SWAP --> [1, 3, 4, 1, 5]
Compare array[1]=3 and array[2]=4 --> 3 < 4, no swap
Compare array[2]=4 and array[3]=1 --> 4 > 1, SWAP --> [1, 3, 1, 4, 5]
Compare array[3]=4 and array[4]=5 --> 4 < 5, no swap
```
> **Why**: Each pass "bubbles" the largest unsorted element to its correct position. After pass 1, the last element (5) is guaranteed in place.
> **Note**: We made 2 swaps, so swapped=True and we need another pass.
```

### Section 4: Intuitive Formalization

NOT the most general form -- minimum math needed to make predictions.

```markdown
### Starting Point
[The simplest mathematical statement, with all terms defined]

### Building Up
[Step-by-step development, each step grounded in earlier examples]

### Key Equations
| Name | Equation | What it tells you |
|------|----------|-------------------|
| [name] | $[LaTeX]$ | [plain-language meaning] |
```

At the High school level, this section is a brief paragraph with minimal notation.

### Section 5: CTQ Mapping

```markdown
| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| [specific understanding] | Principle N / Innovation N | [question or task] | [failure pattern] |
```

See the CTQ Derivation Method and Failure Mode Taxonomy below for how to populate this table.

### Section 6: Conceptual Map

Markdown nested-list visualization of the concept's structure. See the Concept Map Format section below.

---

## Depth Levels

There are three levels. A level says who the explanation is for: it sets the notation, the rigor and the kind of solved exercise.

| Level | Assumes | Explanation | Solved exercise |
|-------|---------|-------------|-----------------|
| **High school** | School mathematics; no earlier exposure to the topic | Plain words, one picture or analogy, concrete numbers; every symbol explained on first use | Concrete numbers throughout, every step shown |
| **Master's** | The field's standard tools and notation | The formal statement, where it comes from, the key equations | Symbols first, then numbers; every step with its reason |
| **Advanced** | The Master's level, mastered | Full generality: a proof or rigorous derivation, the limits of validity, competing formulations | A proof, a derivation or a non-standard case, with edge cases checked |

How each section of an explanation scales with the level:

| Level | Math | Principles | Worked Example | Innovations | CTQ |
|-------|------|-----------|---------------|------------|-----|
| **High school** | Minimal notation, intuition-first | 3, plain-language only | Concrete numbers throughout, all steps shown, plain-language annotations | 2, brief | Short table (2-3 rows) |
| **Master's** | Full LaTeX throughout | 3-5 with LaTeX | Symbols + numbers, all steps with LaTeX, "Why" and "Note" annotations | 2-4 with worked examples | Full table with mastery tests |
| **Advanced** | Proofs, edge cases, competing forms | 5 with derivations | Multiple approaches shown, edge cases explored, proof annotations | 4 with detailed proofs | Advanced failure modes + edge cases |

Within a TTT session, the level is the sub-goal's `Estimated Depth` in the plan. With no plan to read it from, the default is **Master's**.

**Level names.** Write them in full: High school, Master's, Advanced. Plan tables may abbreviate them to HS, MSc, Adv. Never shorten "High school" to "high": that is a difficulty value. Plans created before these names existed say `introductory` / `intermediate` / `advanced` (`intro` / `inter` / `adv` in tables); read those as High school / Master's / Advanced.

---

## Adaptive Teaching: When to Use What

### Abbreviated Concept Explanation (for simple gaps)

When a gap is narrow, concrete, and does not involve deep conceptual misunderstanding:

```markdown
---

**The Problem**
<1-2 sentences: why this gap matters, framed in the learner's context>

**Core Principles**
<1-2 principles, plain language, no LaTeX>

**Worked Example**
<Short but COMPLETE worked example: 2-4 steps, every step shown, annotated with "Why" notes. No steps skipped. Domain-appropriate format.>

**Quick Check** (CTQ: [source principle])
<CTQ-derived verification question>
(Expected answer: <answer>)
(Watch for: <failure mode>)

---
```

Even in abbreviated form, the worked example must be COMPLETE -- every intermediate step shown and annotated. It is just shorter (fewer steps, simpler scenario) than in the full form.

### Full Concept Explanation (for complex gaps)

When a gap involves conceptual confusion, wrong mental models, or multi-layered misunderstanding, deliver all 6 sections at the appropriate depth level.

### Concept Comparison (for conflation gaps)

When the gap involves confusing two related concepts, use the comparison format (see Concept Comparison Protocol below) instead of a standard explanation.

### Level Ladder (for hard-core principles)

When the sub-goal is a hard-core principle and the gap is on the principle itself, use the Level Ladder (see The Level Ladder below) instead of a standard explanation, whatever the gap's failure mode.

### Decision Criteria

A gap on a **hard-core principle** itself always gets the Level Ladder. A sub-goal is a hard-core principle when its plan blueprint has a Tempting answer, an Insight and a Picture.

A gap is **complex** if ANY of these apply:

1. The gap matches a CTQ failure mode pattern (conflation, overgeneralization, missing prerequisite, procedural-without-conceptual)
2. The gap is flagged as a persistent pattern in the learner profile (2+ occurrences)
3. The gap involves a prerequisite the learner is missing
4. The gap was a "verbal-without-formal" or "formal-without-intuitive" failure

A gap is a **conflation** specifically if the learner confused two related but distinct concepts.

Otherwise, the gap is **simple** -- use the abbreviated form.

---

## The Level Ladder (hard-core principles)

A hard-core principle is one that is hard to grasp: it contradicts intuition, needs an abstraction the learner has not used before, or runs into a misconception that survives being told. Its plan blueprint carries a **Tempting answer**, an **Insight**, a **Picture**, a foundational worked example and a **Level ladder** of solved exercises. In a session it is taught as a climb through the levels, which takes the place of the Full Concept Explanation for that principle.

### Shape

1. **The reveal**, which is the High school rung
2. **One rung for each level above High school**, up to the session's level (none in a High school session: the climb is then the reveal alone)
3. **Close**: one Key Terms table for the whole climb, and a CTQ Mapping table with at least one row per rung

Every rung has the same three parts: the principle at that level, one solved exercise, and "your turn" (an exercise the learner attempts, followed by its complete worked solution).

### The reveal

The aha comes from a prediction that fails, so the reveal starts from the learner's own answer. In this order:

| Step | Content | Rule |
|------|---------|------|
| 1. The assumption | What the learner assumed, in their own words, and why it feels right | Take it seriously: the tempting answer is tempting for a reason |
| 2. The failure | The assumption applied to the test case, with the true result beside it | Concrete and checkable, with numbers. Never "this is wrong because the theory says so". |
| 3. The Insight | The one sentence from the blueprint | One sentence. It reframes the situation; it does not recite the principle's formal statement. |
| 4. The Picture | The blueprint's picture or analogy | One picture, not three. Say where it stops being true. |
| 5. The smallest example | The blueprint's foundational worked example | The minimal case in which the Insight is visible, in concrete numbers |
| 6. The payoff | The test case redone with the Insight | The case that failed now works |

If the learner made no prediction (they said "not familiar"), leave out steps 1, 2 and 6: do not name the Tempting answer and do not solve the test case, which will be presented again.

### The rungs

| Rung | The principle at this level | Its solved exercise |
|------|-----------------------------|---------------------|
| **High school** | Plain words, the Picture, concrete numbers | The foundational worked example |
| **Master's** | The formal statement in standard notation, where it comes from, the key equations, and how it contains the High school picture | Symbols first, then numbers |
| **Advanced** | Full generality: the proof or rigorous derivation, the limits of validity, competing formulations, and what the Master's statement assumed without saying | A proof, a derivation or a non-standard case, with edge cases checked |

Rules:
- Each rung says what it adds to the rung below. A higher rung never tells the learner that the lower one was wrong: the lower rung was a correct view of a special case.
- The solved exercise of a rung comes from the blueprint's Level ladder. Solved exercises follow Section 3.5, including the Check.
- "Your turn" is the rung's Quick Check: a new case at the rung's level, never one used in the plan. Its complete worked solution is shown after the learner responds.
- A failed "your turn" is judged on method: an arithmetic slip does not fail a rung.
- The **bridge** after a failed "your turn" is a few lines, pitched one level down, that connect the step that failed to what the learner already holds. It is not a second explanation of the rung. At the High school rung, the bridge is a different picture.
- In a Socratic session the same content is reached through questions: the Insight through the Guidance Chain, each higher statement by asking the learner to attempt it first. The Picture and the solved exercises come only after the learner has stated the idea.

### Writing the aha parts (when designing a plan)

- **Tempting answer**: the answer a capable person gives *before* knowing the principle, with the reason it feels right. If you cannot write one, the principle is not hard-core.
- **Insight**: test it by reading it alone. It should make the failure look obvious in hindsight.
- **Picture**: concrete and familiar at the High school level. State its limit: every analogy breaks somewhere, and an unstated limit becomes the next misconception.
- **Foundational worked example**: remove everything that is not needed to see the Insight.
- **Solved exercises for the higher rungs**: each one is the same idea seen with that level's tools, not a harder calculation at the level below.

---

## Units Convention

All examples and worked examples use **SI / ISO units** by default:
- Mass: kg, t (metric tonnes, 1 t = 1,000 kg)
- Length: m, mm, km
- Area: m2
- Volume: m3, L
- Force: N, kN
- Pressure: Pa, kPa, MPa
- Temperature: C (or K for thermodynamics)
- Currency: $ (or the learner's currency)

Never use imperial units (lb, ft, in, gal, F) unless the learner explicitly requests them or the domain requires them (e.g., US aviation uses feet).

## LaTeX Conventions

All mathematical expressions use LaTeX notation:

- Inline: `$...$`
- Display (centered, separate line): `$$...$$`
- Variables in prose: `$x$`, `$\theta$`, `$\mathbf{v}$`

**Standard notation reference:**

| Category | Notation |
|----------|----------|
| Vectors | `$\mathbf{v}$`, `$\vec{x}$` |
| Matrices | `$\mathbf{A}$`, `\begin{pmatrix}...\end{pmatrix}` |
| Partial derivatives | `$\frac{\partial f}{\partial x}$` |
| Integrals | `$\int_a^b f(x)\,dx$` |
| Summations | `$\sum_{i=1}^{n}$` |
| Greek letters | `$\alpha$`, `$\beta$`, `$\theta$`, `$\lambda$` |
| Set notation | `$\in$`, `$\subset$`, `$\cup$`, `$\cap$` |
| Probability | `$P(A|B)$`, `$\mathbb{E}[X]$` |
| Norms | `$\|x\|$`, `$\|A\|_F$` |

At the High school level, use minimal notation and explain every symbol on first use.

---

## CTQ Derivation Method

CTQ (Critical-To-Quality) criteria define what the learner MUST understand to claim mastery. They are verifiable -- not topics to study, but criteria to meet.

**Good CTQ**: "Can derive the relationship between entropy and the number of microstates"
**Bad CTQ**: "Understand entropy" (too vague, not verifiable)

### Step 1: Trace from Principles

| Principle | -> | CTQ |
|-----------|-----|-----|
| Energy is conserved | -> | Can track energy transformations across heat, work, and internal energy in a closed system |
| Direct vs indirect costs | -> | Can classify any project cost line item as direct or indirect with justification |

### Step 2: Trace from Innovations

| Innovation | -> | CTQ |
|-----------|-----|-----|
| Boltzmann's $S = k_B \ln W$ | -> | Can calculate entropy from microstate counting for a simple system |
| Earned Value Method | -> | Can compute CPI and SPI from BCWP, BCWS, and ACWP |

### Step 3: Identify Failure Modes

For each CTQ, identify the most likely way a learner will fail it. See the Failure Mode Taxonomy below.

---

## CTQ Failure Mode Taxonomy

| Failure Pattern | Description | Example |
|----------------|-------------|---------|
| **Conflation** | Mixing up two related but distinct concepts | Confusing indirect costs with contingency |
| **Overgeneralization** | Applying a principle beyond its valid domain | Assuming all nested loops are $O(n^k)$ |
| **Missing prerequisite** | Lacking foundational understanding needed for this concept | Cannot classify costs because unfamiliar with WBS |
| **Procedural without conceptual** | Can follow steps but cannot explain why they work | Applies the formula correctly but cannot explain when it breaks |
| **Verbal without formal** | Can describe in words but cannot write the equation | Explains entropy conceptually but cannot write $S = k_B \ln W$ |
| **Formal without intuitive** | Can manipulate symbols but cannot explain what results mean | Solves the integral but cannot interpret the physical meaning |

When identifying gaps in the EVALUATE phase, classify each gap using this taxonomy:
- "Gap [conflation]: confused indirect costs with contingency"
- "Gap [procedural-without-conceptual]: applied formula correctly but cannot explain why it works"

---

## CTQ-Enhanced Quick Check Design

Quick Checks are now derived from CTQ mastery tests:

```markdown
**Quick Check** (CTQ: [source principle or innovation])
[Question from the CTQ's Mastery Test column]
(Expected answer: [answer])
(Watch for: [failure mode pattern from CTQ table])
```

The Quick Check question comes directly from the CTQ table's "Mastery Test" column. The "Watch for" line alerts the evaluator to the most likely failure mode for this specific check.

The "Expected answer" and "Watch for" lines are the evaluator's notes: they are never shown before the learner responds. **After the learner responds, reveal a complete worked solution, not just the expected answer**: every step shown and annotated as in a worked example (Section 3.5), ending with a Check. When the Quick Check asks for an explanation rather than a calculation, the worked solution is the full chain of reasoning, step by step.

---

## Concept Comparison Protocol

Triggered when a gap is classified as **conflation** -- the learner confused two related but distinct concepts.

### Format

```markdown
---

## [Concept A] vs [Concept B]

### What They Share
| Shared Principle | In [Concept A] | In [Concept B] |
|-----------------|----------------|----------------|
| [principle] | [how it manifests] | [how it manifests] |

### Where They Diverge
| Dimension | [Concept A] | [Concept B] |
|-----------|-------------|-------------|
| Core assumption | [what A assumes] | [what B assumes] |
| Primary strength | [where A excels] | [where B excels] |
| Typical use case | [when to use A] | [when to use B] |

### Worked Example: One Case, Both Concepts
[One concrete case worked step by step under [Concept A] and then under [Concept B], in the Section 3.5 format, so that the difference shows up in the result. Ends with a Check.]

### CTQ: The Critical Distinction
| CTQ | Mastery Test | Failure Mode |
|-----|-------------|-------------|
| Can distinguish [A] from [B] in [context] | [specific test] | Conflation: [specific confusion] |

**Quick Check** (CTQ: distinction)
[Question that specifically tests the A vs B distinction]
(Expected answer: [answer])
(Watch for: conflation -- [specific confusion to watch for])

---
```

### When to Use

Use instead of a standard teaching block when:
- The gap is classified as [conflation]
- The learner explicitly confused two specific concepts
- The evaluation identified "confused X with Y" as a gap

---

## Deep-Dive Protocol

During a TTT session, the learner may request deeper explanation of a principle just taught.

### How It Works

1. Identify the principle or innovation to expand (from the most recent teaching block or concept map)
2. Generate a full 6-section explanation for that specific principle, at the session's depth level
3. Frame Section 1 (The Problem) in context of the parent concept: "Within [parent concept], [this principle] matters because..."
4. Deliver the deep-dive inline -- it does NOT interrupt the session
5. After the deep-dive, return to the TTT flow (next gap, or Phase 3.5 if all gaps done)

### Rules

- Deep-dives are offered, never forced: mention the option once after the first teaching block
- Only one deep-dive per teaching block (prevent rabbit holes)
- The deep-dive is included in the session transcript and concept file
- Deep-dives can chain: a deep-dive may reveal new principles the learner can further explore

---

## Concept Map Format

### Node Types

| Type | Meaning | Usage |
|------|---------|-------|
| **(core)** | Central concept being mapped | Exactly one per map |
| **(principle)** | Foundational truth or constraint | The 3-5 load-bearing ideas |
| **(innovation)** | Conceptual breakthrough or key contribution | Creative leaps that built the concept |
| **(application)** | Practical use or derived concept | Where theory meets reality |
| **(prerequisite)** | Required prior knowledge | What you need before this concept |
| **(shared)** | Common to both concepts in a comparison | Only used in comparison maps |

### Relationship Labels

| Label | Meaning | Direction |
|-------|---------|-----------|
| `rests on` | Built on these principles | core -> principle |
| `requires` | Needs these prerequisites | core -> prerequisite |
| `led to` | Produced these innovations | principle -> innovation |
| `enables` | Enables these applications | innovation -> application |
| `generalizes` | Generalization of the child | parent -> child |
| `is a special case of` | Specialization | child -> parent |
| `contrasts with` | In tension or opposition | sibling <-> sibling |
| `equivalent to` | Different formulations of same idea | sibling <-> sibling |

### Structure

```markdown
## Concept Map: [Topic]

- **[Topic]** (core): [one-line description]
  - requires:
    - **[Prerequisite]** (prerequisite): [description]
  - rests on:
    - **[Principle 1]** (principle): [description]
      - led to:
        - **[Innovation A]** (innovation): [description]
          - enables:
            - **[Application X]** (application): [description]
    - **[Principle 2]** (principle): [description]
  - enables:
    - **[Application Y]** (application): [description]
```

### Design Rules

1. Start from the core concept at the top level
2. Group children by relationship type: `requires` first, then `rests on`, then `enables`
3. Every principle and innovation from the teaching blocks MUST appear in the map
4. Nest innovations under their parent principle using `led to`
5. Add 2-4 applications showing practical impact
6. Add 1-3 prerequisites for context
7. Keep descriptions to one line

### Depth Scaling

| Depth | Total Nodes | Levels | Include |
|-------|------------|--------|---------|
| shallow | 5-8 | 2 | Core + immediate principles/innovations |
| standard | 10-15 | 3 | + applications + some prerequisites |
| deep | 15-25 | 4 | + cross-connections + secondary applications + all prerequisites |

Default for TTT sessions: **standard** (10-15 nodes).

### Comparison Maps

For conflation gaps, use a three-section map:

```markdown
- **Shared Foundation**
  - **[Shared Principle]** (shared): [description]
- **[Concept A]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[A-only Principle]** (principle): [description]
- **[Concept B]** (core): [description]
  - rests on:
    - **[Shared Principle]** (shared): see above
    - **[B-only Principle]** (principle): [description]
```

---

## Concept File Export Format

Every Teach phase that delivers content generates a concept file during the RECORD phase.

### Filename

`concept-<domain>-<topic>.md` in kebab-case.
- Example: `concept-cost-engineering-direct-vs-indirect-costs.md`
- Example: `concept-physics-entropy.md`

### YAML Frontmatter

```yaml
---
title: "Concept Report: [Topic]"
domain: [domain in kebab-case]
date: [YYYY-MM-DD]
type: ttt-session
session: SG-[N]
plan: [training plan filename]
level: [High school / Master's / Advanced]
tags: [domain, topic, sub-goal-title]
---
```

The `type: ttt-session` field distinguishes files generated during TTT from standalone `/explain` files.

### Content

The file contains:
1. All teaching blocks delivered during Phase 3 (abbreviated or full)
2. The concept map from Phase 3.5 (if generated)
3. The CTQ table aggregated from all teaching blocks
4. A "Session Context" section noting the plan, sub-goal, initial test result, and gaps found

### Compatibility

These files are structurally compatible with concept-builder's `/library` command. If concept-builder is also installed, its `/library list`, `/library search`, and `/library path` commands will find and index these files.

---

## Exercise Book Format

An exercise book is a file of fully solved exercises for one sub-goal. `/run-session` adds a set to it at the end of a session, and `/worked-exercises` adds a set on request.

### Filename

`<topic>_artefact_SG<N>_exercises.md`, next to the plan. It is a deliverable artefact and is listed in the plan's Artefacts Register with type `deliverable`.

For a concept that belongs to no plan: `exercises-<concept-in-kebab-case>.md`.

### Layout

The file is append-only: each write adds one dated set at the end and never rewrites an earlier set. Inside a set, the exercises of a level come first and their worked solutions after, so the learner can attempt before reading.

```markdown
# Exercise Book: SG-<N> — <sub-goal title>
Plan: <plan filename> | Target level: <level>

> Try each exercise before reading its solution. In every set, the worked solutions follow the exercises.

## Set <date> — <after the session / on request>

### High school: exercises
**HS-1.** <statement, with all data and units>
**HS-2.** <statement — with a twist: what differs from HS-1>

### High school: worked solutions
**HS-1.**
**Given:** <data>
**Step 1:** <operation>
> **Why:** <reasoning>
**Result:** <answer with units and interpretation>
> **Check:** <the result confirmed a second way>

**HS-2.** <same format>

### Master's: exercises
**MSc-1.** ...
```

### Rules

- **A session set** holds 2 exercises for each level from High school up to the sub-goal's `Estimated Depth` (in current plans, the Target level): one standard, and one with a twist (a changed condition, an extra step, or a trap the standard one does not have).
- **An on-request set** holds 3 exercises at the one level asked for, graded from standard to demanding.
- Label exercises by level and number them through the whole file: HS-1, HS-2, MSc-1, Adv-1, continuing from the last number already used for that level.
- Every solution is a complete worked solution in the Section 3.5 format, ending with a Check. A final answer alone is not a solution.
- No exercise repeats a case already used: the sub-goal's Initial Test and Final Test, a solved exercise in the plan, an exercise from the session, or an exercise already in the book.
- If the sub-goal's blueprint has an `Exercise`, it opens the first session set as the first exercise at the sub-goal's own level, with its worked solution. It counts as one of the two for that level.
- Exercise books are written for Core Principle, Key Concept and Tools sub-goals. Motivation and Verification sub-goals have none.
- Never invent a value you are not sure of: mark it `(verify)`.
