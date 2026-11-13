---
description: "Learning goal decomposition into SMART sub-goals. Use when the user asks to create a training plan, break down a learning goal, decompose objectives, define sub-goals, structure a learning path from a high-level goal, or identify what sub-topics need to be learned for a given goal."
---

# Goal Decomposer — Domain Knowledge

Reference knowledge for decomposing a learning goal into structured, testable sub-goals using principle-first analysis.

## What This Skill Does

Takes a free-form learning goal and produces:

1. A **Principle Extraction** of the domain (3-5 core principles)
2. A **Key Facts** table — what the learner must simply know, each fact tied to the sub-goals that use it
3. A **Breakthrough** — the situation before the key intuition and what the topic solved, for the topic and for each principle
4. A refined **SMART Goal** (max 15 words)
5. A plan-level **Motivation & Course Overview (VOC)** — a learner-editable bird's-eye view (why it matters, course arc, digest of core principles and key facts, completion outcomes)
6. **N sub-goals** decomposed across 5 axes, each mapped to principles and written for the plan's **Target level** (High school, Master's or Advanced)
7. A **prerequisite graph** with hard dependencies
8. A **Hard Core** list — the core principles that are hardest to grasp, which get an aha design and a climb through the levels
9. A suggested **sequence** derived from the prerequisite graph

---

## Core Principles, Key Concepts and Key Facts

The decomposition distinguishes three kinds of knowledge:

### Core Principles

Domain-level foundational truths — abstract, general, and transferable. A core principle can be stated without reference to any specific technique, tool, or procedure. It is the **"why"** behind the domain. Core principles rarely change; they are the load-bearing axioms.

- High abstraction, broad scope
- Applies across the entire domain regardless of method or tooling
- Independently testable via reasoning, not just procedure
- Example (cost engineering): *"Every project cost is either traceable to a specific scope item or necessary for the project as a whole"*
- Example (quantum computing): *"A quantum state exists in superposition until measured"*

### Key Concepts

Specific, teachable ideas that **operationalize** core principles. They are more concrete, narrower in scope, and often domain-specific applications or decompositions of a core principle. A key concept is the **"what"** and **"how"** the learner needs to master.

- Medium abstraction, narrow scope
- One testable competency per concept
- May evolve with methods and tools
- Example (cost engineering): *"Unit-rate estimation: multiply quantity takeoff by unit rate to get direct cost"*
- Example (quantum computing): *"The Bloch sphere representation of a single qubit"*

### Key Facts

Specific things the learner must simply **know**. A key fact cannot be worked out from the core principles, yet neither the principles nor the key concepts can be applied without it: a definition, a constant, a conversion factor, a convention, a threshold or standard value, a classification, a name or a date.

- No abstraction: a fact is stated, not reasoned
- Checkable against a source; an uncertain value is marked `(verify)`, never guessed
- Load-bearing: at least one sub-goal's test relies on it
- What tests *use*, not what tests ask the learner to recite: key facts get no sub-goal and no axis
- Example (cost engineering): *"1 t = 1,000 kg"*; *"AACE estimate classes run from Class 5 (least project definition) to Class 1 (most)"*
- Example (quantum computing): *"The two computational basis states of a qubit are written $|0\rangle$ and $|1\rangle$"*

A key fact is **not** a principle in disguise (if it follows from a principle in the plan, the principle carries it), **not** a prerequisite (those go in the Prerequisites column of the Principle Extraction table), **not** vocabulary (terms are defined in each session's Key Terms table), and **not** a key concept.

### The Relationship

Core principles **generate** key concepts. Every key concept must trace back to at least one core principle. A single core principle may generate multiple key concepts. Core principles come first in the learning sequence because they provide the framework into which key concepts slot. Key facts are the fixed points that both rely on.

| Dimension | Core Principle | Key Concept | Key Fact |
|-----------|---------------|-------------|----------|
| Abstraction | High — domain-level truth | Medium — specific, teachable idea | None — one stated item |
| Scope | Broad — applies across the domain | Narrow — one testable competency | A single value, definition or convention |
| Stability | Rarely changes | May evolve with methods/tools | Fixed by definition, measurement or standard |
| Testability | Testable via understanding/reasoning | Testable via practical case | Not tested by itself — used inside practical cases |
| Position in sequence | Early — sets the framework | After the principle(s) it depends on | Wherever a sub-goal first relies on it |
| Maps to in plan | Core Principle axis SG | Key Concept axis SG | A row in the Key Facts table |

---

## Step 0: Principle Extraction

Before decomposing into sub-goals, identify the domain's **3-5 core principles**. This ensures sub-goals are principle-anchored, not topic-guessed.

For each principle, state:

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <one clear sentence> | <LaTeX or "—" if non-mathematical> | <concepts the learner must already know> |

### Rules

- Order from most fundamental to most derived
- Each principle should be independently testable
- The Prerequisites column feeds Step 4 (Prerequisite Tracing)
- If the domain has fewer than 3 principles, it may be too narrow — consider whether the goal should be a sub-goal of a larger plan

### Key Facts Identification

Right after the principles, list the key facts (see the definition above):

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | <one fact, with its value and SI unit> | <what goes wrong without it> | <sub-goals that rely on it> |

- For each principle ask: "What must the learner already know as a fact to apply this?" Then add any fact the practical cases need that no principle covers.
- "Why it matters" says what breaks without the fact, never why the fact is true
- `Used in` is filled once the sub-goals exist (after Step 5); a fact that no sub-goal uses is dropped
- Typically 4-10. Never pad the list.

### Breakthrough

Then capture the breakthrough: what the situation was **before** the key intuition, and what the topic **solved**.

- For the topic as a whole, three short parts: *Before the intuition* (what people did or believed, and where it broke down), *The intuition* (the insight, in plain language), *What it solved* (what became possible)
- For each principle, one table row with the exact principle name: `Principle | Before the intuition | What it solved`
- One or two sentences per part and per cell. A story, not a lesson: no derivations, formulas or worked steps.
- With no historical moment (a practical skill, a tool), "before" is how the work is done without this knowledge and where that breaks down
- Name people and dates only when certain of them
- The Breakthrough story is never reused as a test case

---

## Step 1: The 5 Decomposition Axes

| Axis | Purpose | Typical Count | Position in Sequence |
|------|---------|---------------|---------------------|
| **Motivation** | Why this matters. Engagement, relevance, real-world impact. | 1 (sometimes 2) | First — sets context |
| **Core Principle** | Domain-level foundational truth. Abstract, transferable, the "why." | 1 per principle from Step 0 (typically 3-5) | After Motivation — sets the framework |
| **Key Concept** | Operational knowledge that applies a core principle. The "what/how." | **As many as the domain requires** (2-8+) | After Core Principles — bulk of learning |
| **Tools** | Practical techniques, frameworks, software, resources. | 0-3 (only if tooling is relevant) | After concepts that require them |
| **Verification** | Integrative proof of mastery. Combines multiple concepts. | 1-2 | Last — capstone |

### Critical Rule: Sub-Goal Expansion

The axes are **decomposition directions**, NOT fixed slots. Specifically:

- **Core Principles get exactly ONE sub-goal per principle** from Step 0. Each Core Principle SG:
  - Is always **low difficulty**: one principle, one simple scenario
  - Tests whether the learner can STATE and APPLY the principle in a simple scenario
  - MUST include a **simple, fully worked example** in its session blueprint — this is the one exception to the "no teaching content in the plan" rule. The worked example grounds the abstract principle in concrete reality (2-4 steps, concrete numbers, annotated with "Why" notes, simplest possible scenario).
- **Key Concepts MUST expand** into as many sub-goals as the domain requires. A simple goal may have 2 Key Concept sub-goals; a complex goal may have 8+.
- Each Key Concept sub-goal covers **one testable idea** — if a concept has multiple independent parts, split it.
- **Each Key Concept sub-goal MUST map to at least one Core Principle SG** (not just to the principle table). If a Key Concept sub-goal doesn't trace to a Core Principle SG, either the principle list is incomplete or the sub-goal is not load-bearing.
- Motivation and Verification typically have 1 sub-goal each, but can have more.
- Tools sub-goals exist ONLY if the goal involves specific tooling (software, frameworks, instruments).

---

## Step 2: SMART Statement Format

Each sub-goal is expressed as a 15-word SMART statement:

- **Specific**: names the exact competency
- **Measurable**: implies an observable outcome
- **Achievable**: scoped to one learning unit
- **Relevant**: clearly connected to the main goal
- **Time-bound**: implicitly — each is a single TTT session

### Examples

Good: `"Identify and classify all cost components in an EPC project estimate accurately"`
Good: `"Apply unit-rate estimation to civil quantities with less than 5% calculation error"`
Bad: `"Understand cost estimation"` (too vague, not measurable)
Bad: `"Learn everything about piping, structural, and electrical estimation"` (too broad — split into separate sub-goals)

---

## Step 3: Difficulty Calibration

Assign difficulty to each sub-goal using these **derived criteria**, not intuition:

| Criterion | Low | Medium | High |
|-----------|-----|--------|------|
| Principles involved | 1 | 2-3 | 4+ |
| Prerequisite chain depth | 0-1 | 2-3 | 4+ |
| Math/formalism required | None or minimal | Standard notation | Proofs, derivations |

Difficulty describes how much a sub-goal combines. It does **not** set the depth level. The **depth level of every sub-goal is the plan's Target level**:

- **High school** — school mathematics, no earlier exposure to the topic
- **Master's** — the field's standard tools and notation
- **Advanced** — the Master's level, mastered

The Target level is set once, when the plan is created, and is fixed for the plan. An easy sub-goal gets a shorter explanation, not a lower level.

Write each sub-goal so that it can be achieved at the Target level. A sub-goal that needs formalism above the Target level is out of scope for the plan: leave it out, or restate it at the Target level.

**Core Principle SGs are always low difficulty** — by definition they involve 1 principle, 0 prereq depth within the plan, and one simple scenario. This is a hard rule, not derived.

---

## Step 4: Prerequisite Tracing

Build a prerequisite graph using the concept map relationship types. The principles from Step 0 and their Prerequisites column are the source.

```markdown
<Goal> (core)
  requires:
    <External Prerequisite 1> (prerequisite) ← CHECK learner profile
    <External Prerequisite 2> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle 1> (principle) → SG-X
      led to:
        <Principle 2> (principle) → SG-Y
    <Principle 3> (principle) → SG-Z
```

### Rules

- **`requires`** links point to knowledge OUTSIDE this training plan. These are external prerequisites — the learner must already know them or they need their own sub-goals.
- **`rests on`** links point to principles WITHIN this plan. These become hard sub-goal dependencies.
- **`led to`** links show derived relationships — if Principle 2 was derived from Principle 1, SG-Y depends on SG-X.
- If a `requires` prerequisite is NOT in the learner profile as a known strength, flag it: "WARNING: Learner may lack prerequisite [X]. Consider adding a prerequisite sub-goal or verifying during session."
- The prerequisite graph replaces intuited dependencies — every dependency in the Sequence must trace to a graph edge.

### Flagging the Hard Core

With the graph in hand, flag the **hard core**: the core principles that are much harder to grasp than the rest. They get an explanation designed around an aha moment and are taught as a climb through the levels.

A core principle belongs to the hard core when it is hard to grasp in at least one of these ways:

| Criterion | The principle... |
|-----------|------------------|
| **Counter-intuitive** | contradicts what everyday experience or earlier study leads the learner to expect |
| **New abstraction** | cannot be stated without a representation the learner has not used before |
| **Persistent misconception** | runs into a well-known wrong idea that people keep even after being told the right one |

and it passes the gate: *"Can I write the tempting answer — what a capable person who does not yet know this principle would confidently, and wrongly, answer to a concrete case?"* Without a tempting answer there is nothing to predict and fail, and the principle is not hard-core. This gate works like the Testability Check in Step 6.

- Usually 1-3 principles. When more qualify, keep the ones that the most sub-goals depend on in the graph (**load-bearing**).
- Zero is allowed for a procedural or tool-centred topic. Say so rather than forcing one.
- Only core principles are flagged, never key concepts
- In the plan's Hard Core table the reasons are criterion names only (counter-intuitive, new abstraction, persistent misconception, load-bearing). The misconception and the insight are never described there: the top of the plan must not give a test away.
- Hard core is about how hard an idea is to *grasp*; Difficulty (Step 3) is about how much a sub-goal combines. A hard-core principle's sub-goal is still low difficulty.
- Examples: *"A quantum state exists in superposition until measured"* is hard-core (counter-intuitive; the tempting answer treats the state as an unknown but definite value). *"Every project cost is either traceable to a specific scope item or necessary for the project as a whole"* is not: nothing about it resists being told.

---

## Step 5: Sequencing Rules

Sequence sub-goals using the prerequisite graph:

1. **Motivation first** — always. Brief, but sets the "why."
2. **Core Principles after Motivation** — ordered by principle dependency (if Principle B `rests on` Principle A, the Core Principle SG for A comes before B). These set the foundational framework.
3. **Key Concepts after Core Principles** — ordered by prerequisite graph. Each Key Concept SG comes after the Core Principle SG(s) it depends on. This is a hard constraint derived from the graph, not a guess.
4. **Independent concepts can be parallel** — if two sub-goals have no graph edge between them, they can run in parallel.
5. **Tools after the concepts they serve** — don't teach the tool before the learner understands what it does.
6. **Verification last** — it integrates everything. Always depends on all prior sub-goals.

---

## Step 6: Testability Check

Before finalizing, verify each sub-goal passes this check:

> "Can I design a practical case (scenario, exercise, or problem) that a competent person could solve, and that would FAIL if the specific knowledge in this sub-goal is missing?"

Additionally, verify the sub-goal traces to at least one principle from Step 0. If it doesn't, the sub-goal may be too vague or the principle list is incomplete.

If yes → good sub-goal.
If no → too vague, too broad, or not independently testable. Refine or split.

---

## Output Format

When decomposing a goal, produce this structure:

```markdown
## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <sentence> | <LaTeX or —> | <prior knowledge> |

## Key Facts

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | <one fact, with its value and unit> | <what goes wrong without it> | SG-<N>, ... |

## SMART Goal
<15-word refined statement>

## Motivation & Course Overview (VOC)
> _Editable by the learner. Bird's-eye view and voice-of-customer anchor;
> feedback on it may restructure the plan._

**Why this matters:** <1-3 sentences — real-world stakes and relevance>

**Bird's-eye view of the course:** <2-4 sentences — end-to-end scope and how the sub-goals connect>

**Core principles & key facts:** <plain-language digest of the Principle Extraction table and the most load-bearing facts from Key Facts>

**What you'll be able to do on completion:** <concrete capabilities tied to the SMART Goal and Verification sub-goal(s)>

## Breakthrough

**Before the intuition:** <1-2 sentences — what people did or believed, and where it broke down>

**The intuition:** <1-2 sentences — the insight that changed the picture, in plain language>

**What it solved:** <1-2 sentences — what became possible that was not possible before>

| Principle | Before the intuition | What it solved |
|-----------|----------------------|----------------|
| <principle name> | <the earlier view or practice it replaced, and how it failed> | <what it made possible> |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle |
|---|------|----------|--------|-----------|-------|-----------|
| SG-1 | Motivation | <statement> | <domain> | low | <HS/MSc/Adv> | — |
| SG-2 | Core Principle | <statement> | <domain> | low | <HS/MSc/Adv> | <principle name> |
| SG-3 | Core Principle | <statement> | <domain> | low | <HS/MSc/Adv> | <principle name> |
| ... | ... | ... | ... | ... | ... | ... |
| SG-N-1 | Key Concept | <statement> | <domain> | <derived> | <HS/MSc/Adv> | <principle name> |
| ... | ... | ... | ... | ... | ... | ... |
| SG-N | Verification | <statement> | <domain> | high | <HS/MSc/Adv> | integrative |

_Depth is the plan's Target level in every row: HS = High school, MSc = Master's, Adv = Advanced._

## Hard Core

| Principle | Why it is hard | Taught in |
|-----------|----------------|-----------|
| <principle name> | <counter-intuitive / new abstraction / persistent misconception / load-bearing> | SG-<N> |

## Prerequisite Graph

<Goal> (core)
  requires:
    <External> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle> (principle) → SG-X
      led to:
        <Principle> (principle) → SG-Y

## Sequence
- SG-1 has no prerequisites
- SG-2 requires SG-1 (graph: rests on)
- SG-3 requires SG-2 (graph: led to)
- ...
- SG-N requires all previous sub-goals
```
