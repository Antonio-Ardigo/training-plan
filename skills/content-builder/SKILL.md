---
description: "Gap-targeted teaching content generation for training sessions. Use when generating teaching material during the Teach phase of a TTT session, when the user asks to explain a concept, teach me about a topic, what did I get wrong, fill a learning gap, when a gap involves distinguishing two concepts, or when the learner requests a deep-dive into a taught principle."
---

# Content Builder -- Domain Knowledge

Reference knowledge for generating targeted, gap-filling teaching content within TTT sessions. Delegates to the concept-explainer skill for the full explanation methodology and CTQ framework.

## Purpose

Generate a **concept explanation** for ONE specific learning gap. Not a lecture. Not a textbook chapter. Just enough to fill the gap so the learner can pass the next test -- but structured using principle-first pedagogy when the gap warrants it.

## Teaching Format

Each gap receives either an abbreviated or full concept explanation, determined by the Gap Complexity Assessment below.

### Abbreviated Concept Explanation (for simple gaps)

```markdown
---

**The Problem**
<1-2 sentences: why this gap matters, framed in the learner's context.
Not "this is important" but "without this, your estimates will systematically miss 15-25% of costs.">

**Core Principles**
<1-2 principles in plain language. Each: one clear statement + one concrete example.>

**Worked Example**
<Short but COMPLETE worked example: 2-4 steps, every step shown explicitly, annotated with
"Why" notes explaining reasoning. No intermediate steps skipped. Domain-appropriate format
(LaTeX for math, word-by-word for language, line-by-line for code, etc.).
See concept-explainer skill Section 3.5 for domain templates.>

**Quick Check** (CTQ: [source principle])
<CTQ-derived verification question>

*If any term in this question is unclear, ask for a **clarification**.*

⏸ **STOP HERE. Wait for the learner to respond.**
Then reveal the expected answer and evaluate. Do NOT write the expected answer in the teaching block.

---
```

### Full Concept Explanation (for complex gaps)

Deliver all 7 sections from the concept-explainer skill at the session's depth level:

1. **The Problem** -- What makes this concept necessary; framed in the learner's gap context
2. **Core Principles** (3-5) -- Foundational truths with statement + LaTeX (at intermediate+) + example
3. **Key Innovations** (2-4) -- Breakthroughs: who, what it solved, worked example
4. **Worked Example** -- FULLY DEVELOPED step-by-step example with every intermediate step shown, every algebraic/linguistic/logical transformation explicit, annotated with "Why" and "Note" at each step. See concept-explainer skill Section 3.5 for format and domain templates.
5. **Intuitive Formalization** -- Minimum math to make predictions
6. **CTQ Mapping** -- Mastery criteria table with failure modes
7. **Quick Check** (CTQ-derived) -- Verification question from the CTQ mastery test. Include clarification note. Do NOT write the expected answer — stop and wait for the learner to respond.

### Concept Comparison (for conflation gaps)

When the gap is classified as [conflation], use the concept-explainer skill's Concept Comparison Protocol instead:
1. What They Share -- shared principles table
2. Where They Diverge -- differences table
3. CTQ: The Critical Distinction -- specific mastery test for the A vs B distinction
4. Quick Check targeting the distinction

## Gap Complexity Assessment

Before generating content for each gap, assess complexity using the CTQ failure mode classification from the EVALUATE phase:

1. Does the gap match a CTQ failure mode? (conflation, overgeneralization, missing prerequisite, procedural-without-conceptual, verbal-without-formal, formal-without-intuitive)
2. Is the gap flagged as a persistent pattern in the learner profile? (2+ occurrences)
3. Does the gap involve a prerequisite the learner is missing?
4. Is the gap a conflation between two specific concepts?
5. Did the learner declare "not familiar" with the topic? (responded "not familiar", "I don't know this", "no background", or equivalent to the Initial Test)

**If condition 4 is true** -> Concept Comparison
**If condition 5 is true** -> Full Concept Explanation (the learner has no prior knowledge; deliver all 7 sections as a comprehensive introduction to the topic)
**If any of conditions 1-3 are true** -> Full Concept Explanation
**Otherwise** -> Abbreviated Concept Explanation

## Design Principles

### 1. One Gap, One Explanation

Each concept explanation addresses exactly ONE gap. If the learner has 3 gaps, produce 3 separate explanations delivered sequentially -- not one large combined lesson.

### 2. Practical Over Theoretical

- Lead with "The Problem" -- connect to the learner's actual gap and real-world consequences
- Exercises and examples should use concrete numbers, scenarios, and contexts
- Principles should be illustrated with vivid, specific examples before any formalization

### 3. Minimal and Sufficient

For **simple gaps**: abbreviated treatment (Problem + Principles + Quick Check). Similar length to the old teaching block.

For **complex gaps**: the full 7-section treatment IS the minimum needed -- the gap is deep enough that shortcuts would leave misunderstandings intact. But even here, each section should be concise and targeted.

### 4. Error-Focused with CTQ Failure Modes

The CTQ failure mode taxonomy enriches error identification:
- **Conflation**: the learner confused two distinct concepts -> use Comparison format
- **Overgeneralization**: applied a rule beyond its domain -> teach the boundary conditions
- **Missing prerequisite**: lacks foundation -> teach the prerequisite first, then the target concept
- **Procedural without conceptual**: can follow steps but not explain why -> emphasize principles and "why" before "how"
- **Verbal without formal**: describes correctly but cannot formalize -> emphasize the LaTeX / formal expression
- **Formal without intuitive**: manipulates symbols but cannot interpret results -> emphasize concrete examples and physical meaning

### 5. CTQ-Enhanced Quick Checks

Quick Checks are derived from CTQ mastery tests:
- The question comes from the CTQ table's "Mastery Test" column
- Must test understanding, not recall: "When would you use X?" not "What is the definition of X?"
- Every Quick Check MUST end with: `*If any term in this question is unclear, ask for a **clarification**.*`
- **CRITICAL: Do NOT write the expected answer or "Watch for" hint in the teaching block.** The Quick Check output contains ONLY the question + clarification note. Stop there and wait for the learner. You know the answer internally — reveal it only AFTER the learner responds.

## Example: Abbreviated Concept Explanation

Gap [simple]: "Learner miscalculated unit cost by using wrong units."

```markdown
---

**The Problem**
Your rebar cost was off by a factor of 1,000 because your quantity was in kg but your rate was in $/t. Unit mismatches are the most common arithmetic error in cost estimation -- they don't look wrong until the total is wildly off.

**Core Principles**

**Dimensional consistency**: Every multiplication must have compatible units. If your quantity is in kg and your rate is in $/t, you need a conversion factor (1 t = 1,000 kg) before multiplying.

**Unit-label tracking**: Write units next to every number in your calculation. If the units don't cancel to produce $, something is wrong.

**Worked Example**

**Given**: Rebar quantity = 38,000 kg. Rate card = $2,100/t.

**Step 1**: Identify the unit mismatch
Quantity is in **kg**, rate is in **$/t** (tonnes). These cannot be multiplied directly.
> **Why**: kg x $/t does not cancel to $. You'd get kg-$/t, which is meaningless.

**Step 2**: Convert quantity to match the rate's unit
$$1 \text{ t} = 1{,}000 \text{ kg}$$
$$38{,}000 \text{ kg} \div 1{,}000 \text{ kg/t} = 38.0 \text{ t}$$
> **Why**: We convert the quantity to tonnes so the multiplication will produce $.
> **Note**: Divide by 1,000 (NOT multiply). A common error: 38,000 x 1,000 = 38,000,000 -- obviously wrong but easy to type.

**Step 3**: Multiply converted quantity by rate
$$38.0 \text{ t} \times \$2{,}100/\text{t} = \$79{,}800$$
> **Check**: The wrong answer (no conversion) would be 38,000 x $2,100 = $79,800,000 -- absurdly high for rebar on one foundation. Sanity check confirms our answer is in the right order of magnitude.

**Result**: **$79,800**

**Quick Check** (CTQ: dimensional consistency)
Your quantity is 38,000 kg of rebar. The rate card says $2,100/t. What is the correct rebar cost?

*If any term in this question is unclear, ask for a **clarification**.*

⏸ **Wait for the learner to respond before revealing the answer.**

---
```

## Example: Full Concept Explanation

Gap [conflation]: "Learner confused indirect costs with contingency."

```markdown
---

## Indirect Costs vs Contingency

### 1. The Problem

Your estimate lumped "miscellaneous 15%" at the bottom without distinguishing indirect costs from contingency. These are fundamentally different categories: one covers KNOWN costs you can itemize, the other covers UNKNOWN risks you cannot. Mixing them means you cannot defend your estimate in a review, and you will either double-count or miss real costs.

### 2. Core Principles

#### Principle 1: Direct vs Indirect Classification
**Statement**: Every project cost is either traceable to a specific scope item (direct) or necessary for the project but not tied to one item (indirect).
**Example**: Steel for Tank T-101 is direct. Site security fencing is indirect -- it serves the whole project, not one deliverable.

#### Principle 2: Contingency as Risk Reserve
**Statement**: Contingency covers the cost impact of identified risks that may or may not occur. It is probability-weighted, not a line item.
**Example**: "30% chance the soil needs extra piling" = contingency of 0.30 x $200k = $60k. This is NOT an indirect cost -- it may never be spent.

#### Principle 3: Estimating Traceability
**Statement**: If you can point to the item on a drawing or schedule, it is direct. If it serves the whole project, it is indirect. If it depends on a risk event, it is contingency.

### 3. Key Innovations

#### AACE Classification System (AACE International, 1990s)
**What**: Standardized cost breakdown into direct, indirect, contingency, and escalation categories.
**Why it mattered**: Before this, estimators used ad-hoc categories, making estimates incomparable across projects and companies.

### 3.5. Worked Example: Building a Cost Estimate with Correct Classification

**Given**: A small tank farm project with the following costs to classify and total.

**Step 1**: Identify and sum direct costs
| Item | Quantity | Unit | Rate | Cost |
|------|----------|------|------|------|
| Carbon steel plate | 85 | t | $3,200/t | $272,000 |
| Welding labour | 2,400 | h | $65/h | $156,000 |
| Foundation concrete | 120 | m3 | $180/m3 | $21,600 |
| Piping (installed) | 350 | m | $420/m | $147,000 |
| **Direct subtotal** | | | | **$596,600** |

> **Why**: Each of these items is traceable to a specific scope item on the drawings. Steel is for Tank T-101/T-102, welding is for those tanks, concrete is for their foundations, piping connects them.
> **Note**: "Traceable to a drawing" is the key test. If you can point to it on a P&ID, GA, or structural drawing, it is direct.

**Step 2**: Identify and sum indirect costs (itemized)
| Item | Basis | Cost |
|------|-------|------|
| Site security | 8 months x $4,500/month | $36,000 |
| Builder's risk insurance | 0.8% of $596,600 | $4,773 |
| Mob/demob | lump sum | $45,000 |
| Construction management | 8 months x $18,000/month | $144,000 |
| **Indirect subtotal** | | **$229,773** |

> **Why**: None of these serve a single scope item -- they serve the whole project. Security protects the entire site, insurance covers all direct works, mob/demob moves the crew.
> **Note**: Insurance base is direct costs only ($596,600), NOT direct + indirect. The base must exclude the items being calculated -- otherwise you get a circular reference.

**Step 3**: Calculate contingency via risk analysis (NOT a blanket %)
| Risk Event | Probability | Impact | Contingency |
|-----------|------------|--------|-------------|
| Soil bearing capacity below design | 25% | $80,000 (extra piling) | $20,000 |
| Steel price escalation >10% | 30% | $40,000 (price delta) | $12,000 |
| Schedule delay due to permits | 15% | $54,000 (extended indirects) | $8,100 |
| **Contingency total** | | | **$40,100** |

> **Why**: Each contingency line is probability x impact for an identified risk. This is NOT "add 15% to cover unknowns" -- it is a quantified reserve for specific risks that may or may not occur.
> **Note**: A blanket "15% contingency" on this project would be $123,956 -- three times the risk-based number. Blanket percentages either overcharge or underprotect.

**Step 4**: Assemble the total estimate
$$\text{Total} = \$596{,}600 + \$229{,}773 + \$40{,}100 = \$866{,}473$$
> **Check**: Indirects are 38.5% of directs (typical range for small projects: 30-50%). Contingency is 4.6% of base (direct + indirect) -- reasonable for a well-defined scope with few unknowns.

**Result**: **$866,473** (Direct: $596,600 + Indirect: $229,773 + Contingency: $40,100)

### 4. Intuitive Formalization

$$\text{Total Estimate} = \sum \text{Direct}_i + \sum \text{Indirect}_j + \text{Contingency} + \text{Escalation}$$

| Component | Formula | What it covers |
|-----------|---------|----------------|
| Direct costs | $\sum Q_i \times R_i$ | Scope-specific items (quantity x rate) |
| Indirect costs | Itemized list | Project-wide costs (camp, insurance, mob/demob) |
| Contingency | $\sum P_k \times I_k$ | Probability-weighted risk impacts |

### 5. CTQ Mapping

| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| Can classify any cost line as direct, indirect, or contingency | Principle 1 + 2 | "Freight for equipment X" -- which category? | Conflation: calling freight "indirect" when it's direct to that equipment |
| Can explain why contingency is not a percentage add-on | Principle 2 | Why is "add 15% contingency" a bad practice? | Procedural: applies % without risk analysis |

### What They Share

| Shared Principle | Indirect Costs | Contingency |
|-----------------|----------------|-------------|
| Both are non-scope-specific costs | Yes -- project-wide, not item-specific | Yes -- risk-driven, not item-specific |
| Both appear below the direct cost subtotal | Yes | Yes |

### Where They Diverge

| Dimension | Indirect Costs | Contingency |
|-----------|---------------|-------------|
| Nature | KNOWN and quantifiable | UNCERTAIN and probability-weighted |
| Can you itemize it? | Yes -- security, insurance, camp, etc. | No -- it is a reserve for risk events |
| When is it spent? | Always -- these costs will occur | Maybe -- only if the risk event occurs |
| How to estimate | Bottom-up: list and price each item | Risk analysis: probability x impact |

**Quick Check** (CTQ: classification)
Your estimate includes "builder's risk insurance: $45,000" and "possible soil remediation if contamination found: $120,000." Which is indirect and which is contingency, and why?

*If any term in this question is unclear, ask for a **clarification**.*

⏸ **Wait for the learner to respond before revealing the answer.**

---
```

## Key Terms Appendix

Every teaching block (abbreviated or full) MUST end with a **Key Terms** table before the Quick Check. This table defines every domain-specific term introduced or used in the explanation.

```markdown
**Key Terms**
| Term | Definition | First appears |
|------|-----------|---------------|
| <term> | <one-sentence definition> | <Principle N / Worked Example / etc.> |
```

### Rules

- Include ALL domain terms used in the teaching block, not just new ones
- Definitions must be self-contained — a reader should understand each term without reading the full explanation
- Use the term's formal name (e.g., "Hermitian matrix" not "that kind of matrix")
- If a term has a common synonym, note it: "Self-adjoint (also: Hermitian in finite dimensions)"
- For mathematical terms, include the LaTeX notation: "Conjugate transpose: $A^*$ or $A^\dagger$"
- Order terms by first appearance in the teaching block, not alphabetically
- The Key Terms table is included in the concept file export

### Example

```markdown
**Key Terms**
| Term | Definition | First appears |
|------|-----------|---------------|
| Direct cost | A cost traceable to a specific scope item on a drawing or schedule | Principle 1 |
| Indirect cost | A project-wide cost not tied to one deliverable (e.g., site security, insurance) | Principle 1 |
| Contingency | A probability-weighted reserve for identified risk events that may or may not occur | Principle 2 |
| Mob/demob | Mobilization and demobilization — the cost of moving crew and equipment to and from site | Worked Example Step 2 |
| Builder's risk insurance | Insurance covering damage to works under construction; base is typically direct costs only | Worked Example Step 2 |
```

---

## When the Quick Check Fails

After the learner responds to the Quick Check, reveal the expected answer and the "Watch for" failure mode. Then evaluate:

- **Correct**: Acknowledge, proceed to next gap or Phase 3.5
- **Incorrect**: Follow the re-teach protocol below

If the learner answers the Quick Check incorrectly:

1. Do NOT move to the next teaching block
2. Re-explain the specific point they got wrong, using a DIFFERENT angle or example
3. Give one more CTQ-derived Quick Check on the same concept
4. If they pass the second check, proceed
5. If they fail again, note it as a persistent gap and proceed (don't loop on Quick Checks)

---

## Concept Map for TTT Sessions

After all teaching blocks are delivered and Quick Checks passed, generate a concept map during Phase 3.5.

### Format

Use the concept-explainer skill's full Concept Map Format:
- All node types: (core), (principle), (innovation), (application), (prerequisite), (shared)
- All relationship labels: `rests on`, `requires`, `led to`, `enables`, `generalizes`, `is a special case of`, `contrasts with`, `equivalent to`

### Design Rules for TTT Context

1. Default depth: **standard** (10-15 nodes)
2. The (core) node is the sub-goal's topic, NOT the entire training plan topic
3. ALL gaps taught MUST appear as principles or innovations in the map
4. Nest innovations under their parent principle using `led to`
5. Add 2-4 applications connecting concepts to practical use
6. Add 1-3 prerequisites for context
7. Keep descriptions to one line each
8. Do NOT include "Where to Go Next" suggestions -- the next step is the Final Test

### For Conflation Gaps

If the session included a comparison, use the comparison map format (three-section: Shared Foundation, Concept A, Concept B).

---

## Concept File Export

Every Teach phase generates a concept file, written during the RECORD phase (Phase 6).

- **Filename**: `concept-<domain>-<topic>.md` (kebab-case)
- **Content**: YAML frontmatter + all teaching blocks + concept map + aggregated CTQ table + session context
- **Format**: See concept-explainer skill's Concept File Export Format

The concept file is a persistent learning artifact. It can be browsed via `/concept-library`.

---

## In-Session Deep-Dive

If the learner asks for deeper explanation of a principle after a teaching block:

1. Identify the principle to expand (from the most recent teaching block or concept map)
2. Generate a full 6-section explanation for that principle using the concept-explainer skill's Deep-Dive Protocol
3. Deliver it inline -- the deep-dive does NOT interrupt the session flow
4. Return to the next gap (or Phase 3.5 if all gaps are done)

Rules:
- Mention the deep-dive option once after the first teaching block
- Only one deep-dive per teaching block (prevent rabbit holes)
- Include the deep-dive content in the session transcript and concept file
