---
description: "Learning goal decomposition into SMART sub-goals. Use when the user asks to create a training plan, break down a learning goal, decompose objectives, define sub-goals, structure a learning path from a high-level goal, or identify what sub-topics need to be learned for a given goal."
---

# Goal Decomposer — Domain Knowledge

Reference knowledge for decomposing a learning goal into structured, testable sub-goals using principle-first analysis.

## What This Skill Does

Takes a free-form learning goal and produces:

1. A **Principle Extraction** of the domain (3-5 core principles)
2. A refined **SMART Goal** (max 15 words)
3. **N sub-goals** decomposed across 5 axes, each mapped to principles
4. A **prerequisite graph** with hard dependencies
5. A suggested **sequence** derived from the prerequisite graph

---

## Core Principles vs Key Concepts

The decomposition distinguishes two tiers of knowledge:

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

### The Relationship

Core principles **generate** key concepts. Every key concept must trace back to at least one core principle. A single core principle may generate multiple key concepts. Core principles come first in the learning sequence because they provide the framework into which key concepts slot.

| Dimension | Core Principle | Key Concept |
|-----------|---------------|-------------|
| Abstraction | High — domain-level truth | Medium — specific, teachable idea |
| Scope | Broad — applies across the domain | Narrow — one testable competency |
| Stability | Rarely changes | May evolve with methods/tools |
| Testability | Testable via understanding/reasoning | Testable via practical case |
| Position in sequence | Early — sets the framework | After the principle(s) it depends on |
| Maps to in plan | Core Principle axis SG | Key Concept axis SG |

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
  - Is always **low difficulty / introductory depth**
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

Difficulty determines the **depth level** for the session blueprint:
- low → introductory
- medium → intermediate
- high → advanced

**Core Principle SGs are always low difficulty / introductory depth** — by definition they involve 1 principle, 0 prereq depth within the plan, and minimal formalism. This is a hard rule, not derived.

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

## SMART Goal
<15-word refined statement>

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle |
|---|------|----------|--------|-----------|-------|-----------|
| SG-1 | Motivation | <statement> | <domain> | low | intro | — |
| SG-2 | Core Principle | <statement> | <domain> | low | intro | <principle name> |
| SG-3 | Core Principle | <statement> | <domain> | low | intro | <principle name> |
| ... | ... | ... | ... | ... | ... | ... |
| SG-N-1 | Key Concept | <statement> | <domain> | <derived> | <derived> | <principle name> |
| ... | ... | ... | ... | ... | ... | ... |
| SG-N | Verification | <statement> | <domain> | high | adv | integrative |

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
