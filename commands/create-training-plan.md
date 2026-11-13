---
name: create-training-plan
description: Create a customized training plan from a learning goal using Test-Teach-Test methodology
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are creating a customized training plan using the **Test-Teach-Test (TTT)** methodology.

The user wants to learn: **$ARGUMENTS**

## Your Task

Generate a complete training plan by following these steps in order:

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

### Step 3: Design Session Blueprints

For each sub-goal, design a TTT session blueprint.

#### Standard blueprint (Key Concept, Tools, Motivation, Verification SGs):

- **Initial Test**: A practical case the learner must solve immediately (no theory first). Describe the scenario and the task.
- **Pass Criteria**: Concrete, measurable threshold (e.g., "identifies 8 of 10 categories", "calculation within 5%")
- **Estimated Depth**: introductory / intermediate / advanced (derived from sub-goal difficulty)
- **Principle**: Which principle(s) from Step 1.75 this sub-goal tests
- **Exercise**: A simple, concrete, self-contained hands-on exercise the learner can do to practice this concept. Should be completable in 5-10 minutes with clear instructions and expected outcome. Different from the Initial/Final Tests — this is a practice activity, not an assessment.
- **Anticipated CTQs**: 2-4 Critical-To-Quality criteria for this sub-goal. Each CTQ: what must be understood + mastery test + common failure mode (using CTQ failure mode taxonomy: conflation, overgeneralization, missing-prerequisite, procedural-without-conceptual, verbal-without-formal, formal-without-intuitive)
- **Teach Topics**: Key concepts, exercises, and known pitfalls with CTQ failure mode classification (e.g., "[conflation]: confusing indirect costs with contingency", "[procedural-without-conceptual]: applying formula without understanding boundary conditions")
- **Final Test**: A DIFFERENT practical case testing the same competencies

#### Core Principle blueprint (Core Principle SGs only):

Core Principle blueprints include a **fully worked example in the plan itself** — this is the one exception to the "no teaching content in the plan" rule. The worked example grounds the abstract principle in concrete reality.

- **Principle**: The principle name and statement from Step 1.75
- **Worked Example (foundational)**: A simple, fully worked example demonstrating the principle in the most basic scenario. 2-4 steps, concrete numbers, every step shown explicitly, annotated with "Why" notes explaining reasoning. This is the simplest possible scenario that makes the principle visible — not a complex application.
- **Initial Test**: A simple scenario testing whether the learner can STATE the principle in their own words AND APPLY it to a basic case. Simpler than Key Concept tests.
- **Pass Criteria**: "Can state the principle in own words AND apply it to a basic scenario correctly"
- **Estimated Depth**: Always introductory
- **Exercise**: A simple, concrete, self-contained hands-on exercise the learner can do to practice this principle. Should be completable in 5-10 minutes. Different from the Initial/Final Tests — this is a practice activity, not an assessment.
- **Anticipated CTQs**: 1-2 CTQs focused on understanding the principle, not applying advanced techniques
- **Teach Topics**: The principle itself, its boundary conditions, common misunderstandings
- **Final Test**: A DIFFERENT simple scenario testing the same principle

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
- This is a plan-level overview, **distinct from the SG-1 Motivation session blueprint** (which stays a TTT test on "why this matters").
- Keep it informative — **not** teaching content, no test, no theory.
- It goes near the top of the plan file (see Step 4 template), so the learner sees the big picture before the details.

### Step 4: Write the Plan File

Use the Write tool to create `<topic>_training_plan.md` in the current directory. Use this exact format:

```markdown
# Training Plan: <Title>
Generated: <date> | Status: in-progress

## Learning Goal
<User's original input>

## SMART Goal
<15-word refined statement>

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
| SG-1 | Motivation | <statement> | <domain> | low | intro | — | pending | - |
| SG-2 | Core Principle | <statement> | <domain> | low | intro | <principle> | pending | - |
| SG-3 | Core Principle | <statement> | <domain> | low | intro | <principle> | pending | - |
| ... | Core Principle | ... | ... | low | intro | ... | ... | ... |
| SG-N | Key Concept | <statement> | <domain> | <low/med/high> | <intro/inter/adv> | <principle> | pending | - |
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
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** introductory
- **Principle:** —
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags>
- **Final Test:** <different case, same competencies>

### SG-2: <Core Principle short title>
- **Principle:** <principle name> — <principle statement>
- **Worked Example (foundational):**
  **Given:** <simplest possible scenario with concrete numbers>
  **Step 1:** <operation>
  > **Why:** <reasoning>
  **Step 2:** <operation>
  > **Why:** <reasoning>
  **Result:** <answer with units and interpretation>
- **Initial Test:** <simple scenario testing principle understanding>
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** introductory
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <principle> | <verification task> | <failure pattern> |
- **Teach Topics:** <the principle, boundary conditions, common misunderstandings>
- **Final Test:** <different simple scenario testing same principle>

### SG-N: <Key Concept short title>
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** <introductory/intermediate/advanced>
- **Principle:** <principle name>
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags>
- **Final Test:** <different case, same competencies>

(repeat for every sub-goal — Core Principle SGs include the Worked Example field, others do not)

## Artefacts Register
> _Visible anchor for every artefact this course produces. Seeded at plan
> creation and updated as sessions run — each artefact is reusable context._

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| <plan title> | plan | — | <topic>_training_plan.md | current |

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
| Method | `## Pedagogical Method: Test-Teach-Test` is present with its three steps and its teaching-style line, and every blueprint has an Initial Test and a Final Test |

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The teaching method: Test-Teach-Test with direct explanation
- The Motivation & Course Overview (VOC) — and **invite the learner to review and edit it**. State that edits are welcome and that feedback on it may **restructure the course**.
- The Breakthrough: before the intuition, the intuition, what it solved
- The principle extraction table
- The key facts: how many there are, and which are marked `(verify)` for the learner to confirm against a source
- The sub-goals table
- Any prerequisite warnings (external prerequisites not confirmed in learner profile)
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan (if profile existed)
- The result of the required-elements check (Step 4.5), one line per element
- Remind the user to run `/run-session SG-<N>` to start learning

**VOC feedback → restructure rule:** If the learner revises the Motivation & Course Overview (or gives feedback on it), re-evaluate whether the current sub-goal decomposition still matches the stated scope and outcomes. If it no longer matches, **offer to re-decompose (restructure) the plan** using the normal decomposition rules — update the Sub-Goals table, Prerequisite Graph, and Sequence, the Breakthrough rows if the principles changed, and the Key Facts `Used in` column — then refresh the VOC digest so it stays consistent with the revised plan and re-run the check in Step 4.5.

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example
- The plan names and motivates; it does not explain or derive. The Breakthrough section and the Key Facts table are orientation: state them, never teach from them.
- Do NOT skip the required-elements check (Step 4.5): a plan missing one of the five elements is incomplete
- Do NOT skip the session blueprint for any sub-goal
- Practical cases must be realistic scenarios, not abstract questions
- The `<topic>` in the filename should be a short kebab-case slug derived from the goal (e.g., `cost-estimation`, `python-data-analysis`)
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
