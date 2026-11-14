# Formats

Four formats: short, full, side by side, and level by level for a key idea. `SKILL.md` section 2 says which one to use. Every format contains one complete worked example (`SKILL.md` section 3) and ends with Key terms and a Check (`SKILL.md` section 4). The section lists below are the only ones.

## Short

For a narrow item: a slip, a missing fact, one point.

1. **The problem.** One or two sentences: why this matters, in the learner's own case. Say what it costs ("without this, the estimate misses 15 to 25% of the cost"), not that it is important.
2. **Principles.** One or two, in plain words. Each is one clear statement and one concrete example.
3. **Worked example.** Two to four steps, complete, each with its Why.
4. **Key terms.**
5. **Check.**

## Full

For a mistaken picture, a common mistake other than mixing up two ideas, missing background, start from scratch, go deeper, and any explanation asked for outside a lesson.

1. **The problem.** One to three paragraphs. What observation, need or contradiction made the idea necessary, what was tried before and why it failed, what was at stake. In a lesson, frame it in the learner's answer: "Your answer assumed... Here is why that matters."
2. **Principles.** Three to five, from the most basic to the most derived:
   ```markdown
   #### <Principle name>
   **Statement:** <one sentence>
   **Formally:** $$<equation>$$        (Master's and Advanced only)
   **Example:** <a concrete case>
   ```
3. **Key innovations.** Two to four, in the order they came or the order they depend on each other:
   ```markdown
   #### <Innovation> (<who>, <when>)
   **What:** <what was introduced or found>
   **Why it mattered:** <what it solved, what it made possible>
   **Example:** <a concrete case>
   ```
4. **Worked example.** Fully developed.
5. **The maths.** The least maths needed to make predictions, not the most general form: the starting point with every term defined, then each step built on the examples, then a table `Name | Equation | What it tells you`. At High school, one short paragraph with minimal notation.
6. **Success criteria.** The table from `SKILL.md` section 7.
7. **Key terms.**
8. **Check.**

How the full format scales with the level:

| Level | Principles | Key innovations | Worked example | Success criteria |
|---|---|---|---|---|
| High school | 3, plain words, no Formally line | 2, brief | Concrete numbers, plain-words Why | 2 or 3 rows |
| Master's | 3 to 5, with LaTeX | 2 to 4, each with an example | Symbols then numbers, Why and Watch out | Every principle covered |
| Advanced | 5, with derivations | 4, with proofs | Several routes, edge cases | Edge cases included |

## Side by side

For mixing up two ideas.

```markdown
## <Idea A> and <Idea B>

### What they share
| Shared principle | In <A> | In <B> |
|---|---|---|

### Where they differ
| | <A> | <B> |
|---|---|---|
| Starting assumption | | |
| Where it works best | | |
| When to use it | | |

### One case, both ideas
<One concrete case worked under A, then under B, in the worked-example format, so that the difference shows in the result. Ends with a Check.>

### The distinction
| What you can do | How it is tested | Common mistake |
|---|---|---|
| Tell <A> from <B> in <context> | <test> | Mixing up two ideas: <the confusion> |

**Key terms**

**Check** (the distinction)
<a question that only the distinction answers>
```

## Key terms

Every format has one Key terms table, just before the Check. Level by level has one for the whole key idea.

```markdown
**Key terms**
| Term | Meaning | First used in |
|---|---|---|
| <term> | <one sentence> | <Principle 2 / Worked example, step 1 / ...> |
```

- List every subject word the explanation uses, not only new ones, in the order they first appear.
- Each meaning stands on its own: a reader understands it without the explanation.
- Use the term's proper name. Give a common synonym in brackets: "Self-adjoint (also: Hermitian, in finite dimensions)".
- Give the notation for a mathematical term: "Conjugate transpose: $A^*$ or $A^\dagger$".

## Level by level (a key idea)

A key idea ★ is hard to grasp: it goes against intuition, needs an abstraction the learner has not used, or meets a mistaken belief that survives being told. Its lesson design holds the trap, the aha, the picture, a worked example (the High school level) and one solved example per level above High school (`design.levels`). It is taught level by level. This replaces the full format for that idea.

**Shape.**
1. **The aha moment**, which is the High school level.
2. **One level for each level above High school**, up to the course level (none in a High school course).
3. **Close**: one Key terms table for the whole key idea, and the success criteria with at least one row per level.

Every level has three parts: the idea at that level, one solved example, and Your turn (a new exercise the learner attempts, then its complete worked solution).

### The aha moment

The aha comes from a prediction that fails, so it starts from the learner's own answer. In this order:

| Part | Content | Rule |
|---|---|---|
| 1. The trap | What the learner assumed, in their words, and why it feels right | Take it seriously. The trap is tempting for a reason |
| 2. The trap shown failing | The assumption applied to the Try first case, with the true result beside it | Concrete and checkable, with numbers. Never "the theory says so" |
| 3. The aha | The one sentence from `design.aha` | One sentence. It changes how the case looks. It does not recite the formal statement |
| 4. The picture | `design.picture` | One picture. Say where it stops being true |
| 5. The first worked example | `design.worked_example` | The smallest case in which the aha is visible, in concrete numbers |
| 6. The case redone | The Try first case solved with the aha | The case that failed now works |

After start from scratch the learner made no prediction. Leave out parts 1, 2 and 6. Do not name the trap and do not solve the Try first case: it comes again.

When the levels start above High school, give parts 3 and 4 as a two-line reminder, then start at that level. lesson-flow sets the starting level.

### The levels

| Level | The idea at this level | Its solved example |
|---|---|---|
| High school | Plain words, the picture, concrete numbers | `design.worked_example` |
| Master's | The formal statement in standard notation, where it comes from, the key equations, and how it contains the High school picture | `design.levels` (masters): symbols first, then numbers |
| Advanced | Full generality: the proof or rigorous derivation, the limits of validity, competing formulations, what the Master's statement assumed without saying | `design.levels` (advanced): a proof, a derivation or a non-standard case, edge cases checked |

Rules:
- Each level says what it adds to the level below. It never says the level below was wrong.
- Solved examples follow the worked-example format, with their Check.
- A lesson taught above the course level has no solved example for the extra level in the design. Write one in the same format.
- Your turn is a new case at the level's own level, used nowhere else in the course.
- After a wrong method, step back one level (`SKILL.md` section 5). A level has at most two exercises.
- In a Socratic course the learner reaches the aha through the guiding questions. The picture and the solved examples come only after the learner has stated the idea. At each higher level the learner first attempts the statement ("How would you write that as an equation?", "What would a proof have to show?"); then it is confirmed and the solved example follows.

The trap, the aha, the picture and the solved examples are written when the course is designed, by the course-design skill (Step 11). A solved example written here, for a level above the course level, follows the same rule: the same idea seen with that level's tools, never a harder calculation at the level below.

## Recap (a key idea held at Try first)

When the learner passes Try first on a key idea, give a short recap: the aha in its one sentence, the picture, and the solved example of the course level (`design.levels` for its level, or `design.worked_example` in a High school course). Open it with: "You have this. Here is the idea in one line and one worked case for reference." A recap is not teaching.

## Worked examples by subject

**Maths, physics, engineering.** Every algebraic step, matrix product and integral shown, in LaTeX, each with its Why.

```markdown
**Step 2:** Multiply the matrix by the vector
$$\mathbf{A}\mathbf{b} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$
Row 1: $1 \times 5 + 2 \times 6 = 17$. Row 2: $3 \times 5 + 4 \times 6 = 39$.
$$\mathbf{A}\mathbf{b} = \begin{pmatrix} 17 \\ 39 \end{pmatrix}$$
> **Why:** Each row of $\mathbf{A}$ weights the components of $\mathbf{b}$ and adds them.
> **Watch out:** Row by column. Multiplying matching entries is a different operation.
```

**Languages and translation.** A word-by-word table, then the structure, then the natural translation.

```markdown
**Step 1:** Word by word
| Original | Root | Grammar | Literal meaning |
|---|---|---|---|
| Il | | article, masculine singular | the |
| ragazzo | ragazzo | noun, masculine singular | boy |
| mangia | mangiare | verb, 3rd person singular, present | eats |
| la | | article, feminine singular | the |
| mela | mela | noun, feminine singular | apple |
> **Why:** The article agrees in gender with its noun: "il ragazzo", "la mela".
> **Watch out:** "Mangia" alone already says he, she or it. Italian often drops the pronoun.

**Result:** "The boy eats the apple."
```

**Costs and business.** Every line item, every subtotal, and every percentage with the base it applies to. SI units.

```markdown
**Step 1:** Direct costs
| Item | Quantity | Unit | Rate | Cost |
|---|---|---|---|---|
| Concrete | 450 | m³ | $180/m³ | $81,000 |
| Rebar | 38.0 | t | $2,100/t | $79,800 |
| **Direct subtotal** | | | | **$160,800** |
> **Why:** Each line is quantity times rate. The units cancel: m³ × $/m³ = $.
> **Watch out:** Check that the rate's unit matches the quantity's unit. Rebar comes in kg or t.
```

**Programming.** Every line of logic, every change of a variable, every pass of a loop.

```markdown
**Step 2:** First pass
Compare 3 and 1: 3 > 1, swap: [1, 3, 4, 1, 5]
Compare 3 and 4: no swap
Compare 4 and 1: 4 > 1, swap: [1, 3, 1, 4, 5]
Compare 4 and 5: no swap
> **Why:** Each pass moves the largest unsorted value to its place.
> **Watch out:** Two swaps happened, so another pass is needed.
```
