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

### Step 1: Refine the Goal and Set the Target Level

Take the user's input and refine it into a **SMART Goal** (max 15 words):
- Specific: names the exact competency
- Measurable: implies an observable outcome
- Achievable: realistic scope
- Relevant: aligned with the user's intent
- Time-bound: includes a timeframe if the user mentioned one

Then set the plan's **Target level**: the level the whole course is pitched at.

| Level | The course assumes | It takes the learner to |
|-------|--------------------|-------------------------|
| **High school** | School mathematics; no earlier exposure to the topic | The idea in plain words, with pictures and concrete numbers |
| **Master's** | The field's standard tools and notation | The formal statement, where it comes from, and problem solving in symbols |
| **Advanced** | The Master's level, mastered | Full generality: proofs, limits of validity, competing formulations |

- If the user's input states a level (for example "at master's level", "for high-school students", "advanced"), use it
- Otherwise ask once, "Which level should this course take you to: High school, Master's or Advanced?", and wait for the answer
- If you cannot ask (a non-interactive run), use Master's and say so in the Step 5 summary
- The Target level is fixed for the plan. Write the SMART Goal, every sub-goal, every test and every pass criterion for that level.

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

### Step 1.8: Key Facts Identification

Identify the domain's **key facts**: the specific things the learner must simply *know*. A principle is reasoned from. A key fact cannot be worked out from the principles, yet they cannot be applied without it: a definition, a constant, a conversion factor, a convention, a threshold or standard value, a classification, a name or a date.

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | <one fact, with its value and unit> | <what goes wrong without it> | <filled in at Step 3.5> |

Rules:
- For each principle from Step 1.75 ask: "What must the learner already know as a fact to apply this?" Then add any fact the practical cases need that no principle covers.
- One fact per row, stated exactly, with its value and SI unit where it has one
- "Why it matters" says what breaks without the fact, never why the fact is true
- A key fact is **not** a principle in disguise (if it can be worked out from a principle in this plan, leave it out), **not** a prerequisite (those go in the Prerequisites column of Step 1.75), **not** vocabulary (terms are defined in each session's Key Terms table), and **not** a Key Concept (those get sub-goals)
- Key facts are what tests *use*, not what tests ask the learner to recite. They get no sub-goal and no axis of their own.
- Typically 4-10. Never pad the list: a short honest list beats a long one.
- Never guess a value. If you are not certain of a number, date or name, mark the fact `(verify)` so the learner checks it against a source.

### Step 1.9: Breakthrough

Capture the topic's **breakthrough**: what the situation was *before* the key intuition, and what the topic *solved*. A concept is easier to understand and remember as the answer to a problem than as a free-standing statement.

Write it at two levels.

**The topic as a whole**, in three short parts (one or two sentences each):
- **Before the intuition:** what people did or believed, and where it broke down.
- **The intuition:** the insight that changed the picture, in plain language.
- **What it solved:** what became possible that was not possible before.

**Each core principle**, one row per principle from Step 1.75, using the exact principle names. The principle's Statement is its intuition, so the table only adds the before and the after:

| Principle | Before the intuition | What it solved |
|-----------|----------------------|----------------|
| <principle name> | <the earlier view or practice this principle replaced, and how it failed> | <what this principle made possible> |

Rules:
- One or two sentences per part and per cell
- If the topic has no single historical moment (a practical skill, a tool, a procedure), "before" is how the work is done *without* this knowledge and where that breaks down
- Tell a story, not a lesson: no derivations, no formulas, no worked steps. Those belong to the sessions.
- Name people and dates only when you are certain of them; otherwise describe the shift without attribution
- Do not reuse the Breakthrough story as a test case: the SG-1 Motivation tests must use different cases
- The Breakthrough names *what* was found. It does not narrate the reasoning that leads there and never describes a blueprint's designed wrong path: finding the *how* is the learner's work in the sessions.

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
- **Each principle from Step 1.75 gets exactly ONE Core Principle sub-goal.** Core Principle SGs are always low difficulty: one principle, one simple scenario. They test whether the learner can state and apply the foundational principle.
- Key Concepts MUST expand -- each covers ONE testable idea
- **Each Key Concept sub-goal MUST map to at least one Core Principle SG.** If a sub-goal doesn't trace to a Core Principle SG, either the principle list is incomplete or the sub-goal is not load-bearing.
- Each sub-goal is a 15-word SMART statement
- Each sub-goal gets a domain label, difficulty, and depth level
- Difficulty is derived (not guessed): low = 1 principle + 0-1 prereq depth, medium = 2-3 principles + 2-3 prereq depth, high = 4+ principles or proofs/derivations required
- **The depth level of every sub-goal is the plan's Target level.** Difficulty does not set depth: an easy sub-goal gets a shorter session, not a lower level.
- Write every sub-goal so that it can be achieved at the Target level. A sub-goal that needs formalism above the Target level is out of scope: leave it out, or restate it at the Target level.
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

For each sub-goal, design a TTT session blueprint with Socratic extensions. Every Discovery Question, test and Guidance Chain is written at the Target level: it assumes that level's tools (see the table in Step 1).

#### Standard Socratic blueprint (Key Concept, Tools, Motivation, Verification SGs):

All fields from the standard blueprint PLUS Socratic extensions:

- **Discovery Question**: A scenario that creates genuine puzzlement *before* any theory. The question should make the learner *want* the concept — they should feel the gap. Design the question so that the learner's natural first attempt fails or is incomplete, creating tension that the concept resolves.
- **Initial Test**: A practical case the learner must solve immediately (no theory first). **Socratic design principle:** the test should be structured so that attempting it naturally surfaces the key tension — the learner's first instinct leads to a partial or incorrect answer, and the gap between their attempt and the correct answer reveals exactly what concept is needed.
- **Pass Criteria**: Concrete, measurable threshold
- **Estimated Depth**: the plan's Target level (High school / Master's / Advanced)
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
- **Estimated Depth**: the plan's Target level
- **Socratic Guidance Chain**: 3-6 questions leading to the principle's discovery
- **Anticipated CTQs**: 1-2 CTQs focused on understanding the principle
- **Teach Topics**: The principle, boundary conditions, common misunderstandings. Include Socratic teaching notes.
- **Final Test**: A DIFFERENT simple scenario. Include a "reconstruct the reasoning" component.

If the learner profile indicated strengths or gap patterns relevant to a sub-goal, note them in the blueprint:
- **Profile note (strength):** "Learner has prior mastery in [topic] -- set Initial Test at elevated difficulty"
- **Profile note (gap pattern):** "Learner has recurring gap in [pattern] -- include proactive Quick Check in Teach Topics even if not identified in Initial Test"

**Key facts in tests:** when a test or exercise depends on a fact, that fact must be in the Key Facts table from Step 1.8. If it is missing, add it.

### Step 3.5: Compose the Motivation / VOC Overview

**First complete the Key Facts table** (the sub-goals now exist): fill each fact's `Used in` column with the sub-goals whose tests or exercises rely on it, and drop any fact that no sub-goal uses.

After decomposition and blueprint design (so the digest and outcomes are accurate), compose a plan-level **Motivation & Course Overview (VOC)** — a bird's-eye view that anchors the whole course. This is the "voice of customer" section: informative, plain-language, and **editable by the learner**.

Write four parts:
- **Why this matters:** 1-3 sentences on real-world stakes and relevance.
- **Bird's-eye view of the course:** 2-4 sentences on what the course covers end to end and how the sub-goals connect into one arc.
- **Core principles & key facts:** a plain-language digest of the 3-5 core principles from the Principle Extraction table (Step 1.75) and the most load-bearing facts from the Key Facts table (Step 1.8).
- **What you'll be able to do on completion:** a bulleted list of concrete capabilities tied to the SMART Goal and the Verification sub-goal(s).

Rules:
- This is a plan-level overview, **distinct from the SG-1 Motivation session blueprint** (which stays a Socratic TTT session on "why this matters").
- Keep it informative — **not** teaching content, no test, no theory. (The overview names *what* is discovered; it does not spoil the Discovery Questions.)
- It goes near the top of the plan file (see Step 4 template), so the learner sees the big picture before the details.

### Step 4: Write the Plan File

First use Glob to check whether `<topic>-socratic_training_plan.md` already exists in the current directory. If it does, do not overwrite it: ask the learner whether to replace it or to keep both. To keep both (and whenever you cannot ask), put the level in the name, `<topic>-hs`, `<topic>-msc` or `<topic>-adv`, and use that as the `<topic>` of this plan.

Use the Write tool to create `<topic>-socratic_training_plan.md` in the current directory. Use this exact format:

```markdown
# Training Plan: <Title> (Socratic)
Generated: <date> | Status: in-progress | Target level: <High school/Master's/Advanced>

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

**The arc is a form of Test-Teach-Test.** Attempt each test cold, before reading its blueprint:

| Test-Teach-Test | In this plan |
|-----------------|--------------|
| Test | Discovery Question and Initial Test: the first attempt meets the **tension** |
| Teach | Socratic Guidance Chain: the **resolution** is derived through questions, not explained |
| Test | Final Test, including its "reconstruct the reasoning" part |

## Motivation & Course Overview (VOC)
> _Editable by the learner. This is the course's bird's-eye view and
> voice-of-customer anchor. If you change anything here, tell me — your
> feedback may restructure the plan (re-decomposition of sub-goals)._

**Why this matters:** <1-3 sentences — real-world stakes and relevance>

**Bird's-eye view of the course:** <2-4 sentences — what the course covers
end to end and how the sub-goals connect into one arc>

**Core principles & key facts:** <plain-language digest of the 3-5 core
principles from Principle Extraction and the most load-bearing facts from Key Facts>

**What you'll be able to do on completion:** <bulleted concrete capabilities
tied to the SMART Goal and the Verification sub-goal(s)>

## Breakthrough
> _The story behind the topic: what the situation was before the key
> intuition, and what the topic solved._

**Before the intuition:** <1-2 sentences — what people did or believed, and where it broke down>

**The intuition:** <1-2 sentences — the insight that changed the picture, in plain language>

**What it solved:** <1-2 sentences — what became possible that was not possible before>

| Principle | Before the intuition | What it solved |
|-----------|----------------------|----------------|
| <principle name> | <the earlier view or practice it replaced, and how it failed> | <what it made possible> |

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| <name> | <sentence> | <LaTeX or —> | <prior knowledge> |

## Key Facts
> _What this course relies on you simply knowing. Values marked `(verify)`
> should be checked against a source before you rely on them._

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | <one fact, with its value and unit> | <what goes wrong without it> | SG-<N>, ... |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | Discover <statement> | <domain> | low | <HS/MSc/Adv> | — | pending | - |
| SG-2 | Core Principle | Discover <statement> | <domain> | low | <HS/MSc/Adv> | <principle> | pending | - |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

_Depth is the plan's Target level in every row: HS = High school, MSc = Master's, Adv = Advanced._

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
- **Estimated Depth:** <Target level>
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
- **Estimated Depth:** <Target level>
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
- **Estimated Depth:** <Target level>
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

## Artefacts Register
> _Visible anchor for every artefact this course produces. Seeded at plan
> creation and updated as sessions run — each artefact is reusable context._

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| <plan title> | plan | — | <topic>-socratic_training_plan.md | current |

## Progress Log
(updated by /run-session)
```

Seed the **Artefacts Register** with the plan file itself. If a `learner_profile.md`
exists in the directory, add a row for it too (`profile` type). Session artefacts
(transcripts, concept files, and any deliverables) are appended by `/run-session`
during its RECORD phase.

### Step 4.5: Check the Required Elements

Read back the file you just wrote, from the top through the Sub-Goals table, plus the blueprint headings and their field names. Confirm each row below. Where a row fails, fix the file with the Edit tool and check that row again.

| Element | Present when |
|---------|--------------|
| Core principles identification | Every row of `## Principle Extraction` has exactly one Core Principle row in `## Sub-Goals`, and every Core Principle row names a principle from that table |
| Key facts identification | `## Key Facts` has at least one row, and every `Used in` cell names sub-goals that exist |
| Motivation | `## Motivation & Course Overview (VOC)` has its four parts filled in, and SG-1 is on the Motivation axis |
| Breakthrough | `## Breakthrough` has its three labelled parts filled in and one table row for each principle in `## Principle Extraction` |
| Method | `## Pedagogical Method: Socratic Discovery` is present with its four-step arc and its Test-Teach-Test table, and every blueprint has a Discovery Question, an Initial Test, a Socratic Guidance Chain and a Final Test |
| Levels | The header line has a `Target level:` of High school, Master's or Advanced, and every Depth cell and every Estimated Depth is that level |

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The Target level (if it was not stated and you could not ask, say that Master's was assumed and that the plan can be created again at another level)
- The Socratic method explanation (Question → Tension → Resolution → Test) and how it maps onto Test-Teach-Test
- The Motivation & Course Overview (VOC) — and **invite the learner to review and edit it**. State that edits are welcome and that feedback on it may **restructure the course**.
- The Breakthrough: before the intuition, the intuition, what it solved
- The principle extraction table
- The key facts: how many there are, and which are marked `(verify)` for the learner to confirm against a source
- The sub-goals table (note the "Discover" framing)
- Any prerequisite warnings
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan
- The result of the required-elements check (Step 4.5), one line per element
- Remind the user to run `/run-session SG-<N>` to start learning

**VOC feedback → restructure rule:** If the learner revises the Motivation & Course Overview (or gives feedback on it), re-evaluate whether the current sub-goal decomposition still matches the stated scope and outcomes. If it no longer matches, **offer to re-decompose (restructure) the plan** using the normal decomposition rules — update the Sub-Goals table, Prerequisite Graph, and Sequence, the Breakthrough rows if the principles changed, and the Key Facts `Used in` column — then refresh the VOC digest so it stays consistent with the revised plan and re-run the check in Step 4.5.

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example
- The plan names and motivates; it does not explain or derive. The Breakthrough section and the Key Facts table are orientation: state them, never teach from them.
- Do NOT skip the required-elements check (Step 4.5): a plan missing one of its required elements is incomplete
- The Target level is fixed for the plan: every sub-goal, test and pass criterion is written for it, and nothing above it is written into the plan
- Do NOT overwrite an existing plan file without asking (Step 4)
- Do NOT skip the session blueprint for any sub-goal
- Every blueprint MUST include a Discovery Question and a Socratic Guidance Chain
- Discovery Questions must create genuine tension — not just ask "what do you know about X?"
- Socratic Guidance Chains must narrow progressively — the last question should make the answer inescapable
- Initial Tests should have a designed "wrong path" that reveals the concept's necessity
- Final Tests must include a "reconstruct the reasoning" or "explain why" component
- The `<topic>` in the filename should be a short kebab-case slug with `-socratic` suffix
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
