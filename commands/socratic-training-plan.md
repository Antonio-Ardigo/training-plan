---
name: socratic-training-plan
description: Create a Socratic training plan where each concept arises from a discovery question and the conclusion feels inevitable
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are creating a customized training plan using the **Test-Teach-Test (TTT)** methodology with **Socratic Discovery** pacing.

The user wants to learn: **$ARGUMENTS**

## Socratic Discovery Method

This command extends `/create-training-plan` with a Socratic layer. The key difference: every concept arises from a question the learner is already asking, and each conclusion feels **inevitable** — not delivered, but discovered.

Each session follows a **Question → Tension → Resolution → Test** arc:

1. **Discovery Question** — a scenario that creates genuine puzzlement. The learner must *feel* the gap before any concept is introduced.
2. **Tension** — the learner's natural first attempt fails or is incomplete. This failure is designed, not accidental.
3. **Resolution** — the concept emerges as the *only* way to resolve the tension. It is not presented as a fact to memorize but as an inevitability.
4. **Test** — the learner demonstrates they can reconstruct the reasoning, not just repeat the answer.

**Socratic Guidance Chains** are sequences of 3-6 questions the instructor asks if the learner is stuck. Each question narrows the search space without giving the answer. The chain is designed so that answering the last question makes the conclusion inescapable.

## Your Task

Generate a complete Socratic training plan by following these steps in order:

### Step 1: Refine the Goal

Take the user's input and refine it into a **SMART Goal** (max 15 words):
- Specific: names the exact competency
- Measurable: implies an observable outcome
- Achievable: realistic scope
- Relevant: aligned with the user's intent
- Time-bound: includes a timeframe if the user mentioned one

### Step 1.5: Check Learner Profile

Use Glob to look for `learner_profile.md` in the current directory.

If found, read it and note:
- **Known strengths**: Topics the learner has mastered (passed Initial Test with zero gaps). If any relate to this new goal, plan harder initial tests for those sub-goals.
- **Gap patterns**: Recurring weaknesses. If any relate to this new goal, note them in the Teach Topics of relevant session blueprints so they get proactive coverage.

If no profile exists, proceed normally. The profile will be created after the first /run-session.

Pass these notes forward to Step 3 (Design Session Blueprints) so the blueprints reflect what is already known about the learner.

### Step 1.75: Principle Extraction

Before decomposing, identify the domain's **3-5 core principles**. This ensures sub-goals are principle-anchored, not topic-guessed.

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <one clear sentence> | <LaTeX or "—"> | <concepts the learner must already know> |

Rules:
- Order from most fundamental to most derived
- Each principle should be independently testable
- The Prerequisites column feeds Step 2.5 (Prerequisite Tracing)
- If the domain has fewer than 3 principles, it may be too narrow

### Step 2: Decompose into Sub-Goals

Break the SMART goal into **N sub-goals** across 5 axes:

| Axis | Purpose | Count |
|------|---------|-------|
| Motivation | Why this matters | 1+ |
| Core Principle | Domain-level foundational truth. The "why." | 1 per principle from Step 1.75 (typically 3-5) |
| Key Concept | Operational knowledge that applies a core principle. The "what/how." | **As many as the domain requires** |
| Tools | Practical techniques/frameworks | 0+ (only if relevant) |
| Verification | Proof of mastery | 1+ |

Rules:
- **Each principle from Step 1.75 gets exactly ONE Core Principle sub-goal.** Core Principle SGs are always low difficulty / introductory depth. They test whether the learner can state and apply the foundational principle in a simple scenario.
- Key Concepts MUST expand -- each covers ONE testable idea
- **Each Key Concept sub-goal MUST map to at least one Core Principle SG.** If a sub-goal doesn't trace to a Core Principle SG, either the principle list is incomplete or the sub-goal is not load-bearing.
- Each sub-goal is a 15-word SMART statement
- Each sub-goal gets a domain label, difficulty, and depth level
- Difficulty is derived (not guessed): low = 1 principle + 0-1 prereq depth, medium = 2-3 principles + 2-3 prereq depth, high = 4+ principles or proofs/derivations required
- Depth level follows difficulty: low -> introductory, medium -> intermediate, high -> advanced
- Sequence: Motivation first -> Core Principles (dependency order) -> Key Concepts (dependency order) -> Tools -> Verification last
- Total: typically 7-15+ sub-goals depending on complexity

**Socratic framing rule:** Each sub-goal statement should be phrased as a *discovery* (e.g., "Discover why outcomes must be labeled by orthogonal vectors") rather than a passive reception (e.g., "Learn about orthogonal vectors").

### Step 2.5: Prerequisite Tracing

Build a prerequisite graph from the principles in Step 1.75:

```
<Goal> (core)
  requires:
    <External Prerequisite> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle 1> (principle) → SG-X
      led to:
        <Principle 2> (principle) → SG-Y
```

Rules:
- **`requires`** = knowledge OUTSIDE this plan (external prerequisites). The learner must already know these.
- **`rests on`** = principles WITHIN this plan. These become hard sub-goal dependencies.
- **`led to`** = derived relationships. If Principle 2 builds on Principle 1, SG-Y depends on SG-X.
- If a `requires` prerequisite is NOT in the learner profile as a known strength, flag it as a WARNING in the plan.
- Every dependency in the Sequence must trace to a graph edge -- no intuited dependencies.

### Step 3: Design Socratic Session Blueprints

For each sub-goal, design a TTT session blueprint with Socratic extensions.

#### Standard Socratic blueprint (Key Concept, Tools, Motivation, Verification SGs):

All fields from the standard blueprint PLUS Socratic extensions:

- **Discovery Question**: A scenario that creates genuine puzzlement *before* any theory. The question should make the learner *want* the concept — they should feel the gap. Design the question so that the learner's natural first attempt fails or is incomplete, creating tension that the concept resolves.
- **Initial Test**: A practical case the learner must solve immediately (no theory first). **Socratic design principle:** the test should be structured so that attempting it naturally surfaces the key tension — the learner's first instinct leads to a partial or incorrect answer, and the gap between their attempt and the correct answer reveals exactly what concept is needed.
- **Pass Criteria**: Concrete, measurable threshold
- **Estimated Depth**: introductory / intermediate / advanced (derived from sub-goal difficulty)
- **Principle**: Which principle(s) from Step 1.75 this sub-goal tests
- **Socratic Guidance Chain**: 3-6 progressively narrowing questions for when the learner is stuck. Each question:
  - Does NOT give the answer
  - Narrows the search space
  - Builds on the previous question
  - The final question makes the conclusion inescapable
- **Anticipated CTQs**: 2-4 Critical-To-Quality criteria with failure modes
- **Teach Topics**: Key concepts, exercises, and known pitfalls with CTQ failure mode tags. **Socratic teaching note:** during the Teach phase, prefer leading questions over declarations. Instead of "The Born rule states P = |psi|^2", use "What operation on psi would give a non-negative number that sums to 1?"
- **Final Test**: A DIFFERENT practical case testing the same competencies. **Socratic design principle:** the final test should require the learner to *reconstruct the reasoning*, not just apply a formula. Include at least one part that asks "why" or "what would happen if."

#### Core Principle Socratic blueprint (Core Principle SGs only):

All fields from the standard Core Principle blueprint PLUS Socratic extensions:

- **Principle**: The principle name and statement from Step 1.75
- **Worked Example (foundational)**: A simple, fully worked example. 2-4 steps, concrete numbers, every step shown explicitly, annotated with "Why" notes. **Socratic framing:** each "Why" note should be phrased as an answer to a question the learner would naturally ask at that step.
- **Discovery Question**: The question that makes the learner *want* this principle. It should create a puzzle or tension that only this principle resolves.
- **Initial Test**: A simple scenario. **Socratic design:** include a "wrong path" — a plausible but incorrect approach that surfaces the key insight when it fails.
- **Pass Criteria**: Can state the principle in own words AND apply it AND explain why the alternative fails
- **Estimated Depth**: Always introductory
- **Socratic Guidance Chain**: 3-6 questions leading to the principle's discovery
- **Anticipated CTQs**: 1-2 CTQs focused on understanding the principle
- **Teach Topics**: The principle, boundary conditions, common misunderstandings. Include Socratic teaching notes.
- **Final Test**: A DIFFERENT simple scenario. Include a "reconstruct the reasoning" component.

If the learner profile indicated strengths or gap patterns relevant to a sub-goal, note them in the blueprint:
- **Profile note (strength):** "Learner has prior mastery in [topic] -- set Initial Test at elevated difficulty"
- **Profile note (gap pattern):** "Learner has recurring gap in [pattern] -- include proactive Quick Check in Teach Topics even if not identified in Initial Test"

### Step 4: Write the Plan File

Use the Write tool to create `<topic>-socratic_training_plan.md` in the current directory. Use this exact format:

```markdown
# Training Plan: <Title> (Socratic)
Generated: <date> | Status: in-progress

## Learning Goal
<User's original input>

## SMART Goal
<15-word refined statement>

## Pedagogical Method: Socratic Discovery

Each session follows a **Question → Tension → Resolution → Test** arc:

1. **Discovery Question** — a scenario that creates genuine puzzlement. The learner must *feel* the gap before any concept is introduced.
2. **Tension** — the learner's natural first attempt fails or is incomplete. This is designed, not accidental.
3. **Resolution** — the concept emerges as the *only* way to resolve the tension. It is not presented as a fact to memorize but as an inevitability.
4. **Test** — the learner demonstrates they can reconstruct the reasoning, not just repeat the answer.

**Socratic Guidance Chains** are provided in each blueprint: sequences of 3-6 questions the instructor asks if the learner is stuck. Each question narrows the search space without giving the answer. The chain is designed so that answering the last question makes the conclusion inescapable.

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <sentence> | <LaTeX or —> | <prior knowledge> |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | Discover <statement> | <domain> | low | intro | — | pending | - |
| SG-2 | Core Principle | Discover <statement> | <domain> | low | intro | <principle> | pending | - |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Prerequisite Graph

<Goal> (core)
  requires:
    <External> (prerequisite) ← CHECK learner profile
  rests on:
    <Principle> (principle) → SG-X
      led to:
        <Principle> (principle) → SG-Y

## Sequence
<dependency notes derived from prerequisite graph>

## Session Blueprints

### SG-1: <Motivation short title>
- **Discovery Question:** <puzzlement-creating scenario>
- **Initial Test:** <practical case with designed tension>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** introductory
- **Principle:** —
- **Socratic Guidance Chain (if stuck):**
  1. <narrowing question>
  2. <narrowing question>
  3. <narrowing question — conclusion becomes inescapable>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags + Socratic teaching notes>
- **Final Test:** <different case with "reconstruct the reasoning" component>

### SG-2: <Core Principle short title>
- **Principle:** <principle name> — <principle statement>
- **Worked Example (foundational):**
  **Given:** <simplest possible scenario>
  **Step 1:** <operation>
  > **Why:** <answer to the question the learner would naturally ask>
  **Step 2:** <operation>
  > **Why:** <answer to natural question>
  **Result:** <answer with interpretation — stated as an inevitability>
- **Discovery Question:** <puzzle that only this principle resolves>
- **Initial Test:** <simple scenario with a "wrong path" that reveals the insight when it fails>
- **Pass Criteria:** Can state the principle in own words AND apply it AND explain why the alternative fails
- **Estimated Depth:** introductory
- **Socratic Guidance Chain (if stuck):**
  1. <narrowing question>
  2. <narrowing question>
  3. <narrowing question>
  4. <conclusion becomes inescapable>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <principle> | <verification task> | <failure pattern> |
- **Teach Topics:** <the principle, boundary conditions, Socratic teaching notes>
- **Final Test:** <different scenario with "reconstruct the reasoning" component>

### SG-N: <Key Concept short title>
- **Discovery Question:** <puzzlement-creating scenario>
- **Initial Test:** <practical case with designed tension>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** <introductory/intermediate/advanced>
- **Principle:** <principle name>
- **Socratic Guidance Chain (if stuck):**
  1. <narrowing question>
  2. <narrowing question>
  3. <narrowing question>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags + Socratic teaching notes>
- **Final Test:** <different case with "reconstruct the reasoning" component>

(repeat for every sub-goal)

## Progress Log
(updated by /run-session)
```

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The principle extraction table
- The sub-goals table (note the "Discover" framing)
- The Socratic method explanation (Question → Tension → Resolution → Test)
- Any prerequisite warnings
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan
- Remind the user to run `/run-session SG-<N>` to start learning

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example
- Do NOT skip the session blueprint for any sub-goal
- Every blueprint MUST include a Discovery Question and a Socratic Guidance Chain
- Discovery Questions must create genuine tension — not just ask "what do you know about X?"
- Socratic Guidance Chains must narrow progressively — the last question should make the answer inescapable
- Initial Tests should have a designed "wrong path" that reveals the concept's necessity
- Final Tests must include a "reconstruct the reasoning" or "explain why" component
- The `<topic>` in the filename should be a short kebab-case slug with `-socratic` suffix
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
