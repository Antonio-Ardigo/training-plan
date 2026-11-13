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
- **The depth level of every sub-goal is the plan's Target level.** Difficulty does not set depth: an easy sub-goal gets a shorter explanation, not a lower level.
- Write every sub-goal so that it can be achieved at the Target level. A sub-goal that needs formalism above the Target level is out of scope: leave it out, or restate it at the Target level.
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

### Step 2.75: Flag the Hard Core

Some core principles are much harder to grasp than the rest, and the course stands or falls on them. Flag them: each gets an explanation designed around an aha moment and is taught as a climb through the levels.

A core principle belongs to the **hard core** when it is hard to grasp in at least one of these ways:

| Criterion | The principle... |
|-----------|------------------|
| **Counter-intuitive** | contradicts what everyday experience or earlier study leads the learner to expect |
| **New abstraction** | cannot be stated without a representation the learner has not used before |
| **Persistent misconception** | runs into a well-known wrong idea that people keep even after being told the right one |

and it passes this gate:

> "Can I write the **tempting answer**: what a capable person who does not yet know this principle would confidently, and wrongly, answer to a concrete case?"

If you cannot write one, there is nothing to predict and fail, and the principle is not hard-core.

Rules:
- Usually 1-3 principles. When more qualify, keep the ones that the most later sub-goals depend on in the Prerequisite Graph. For those, add **load-bearing** to the reasons.
- Zero is allowed: a procedural or tool-centred topic may have no hard core. Say so rather than forcing one.
- Only core principles are flagged, never Key Concepts
- Hard core is about how hard the idea is to *grasp*. It is not Difficulty: a hard-core principle's sub-goal is still low difficulty (one principle, one simple scenario).

### Step 3: Design Session Blueprints

For each sub-goal, design a TTT session blueprint. Every test is written at the Target level: its scenario, its task and its pass criteria assume that level's tools (see the table in Step 1).

#### Standard blueprint (Key Concept, Tools, Motivation, Verification SGs):

- **Initial Test**: A practical case the learner must solve immediately (no theory first). Describe the scenario and the task.
- **Pass Criteria**: Concrete, measurable threshold (e.g., "identifies 8 of 10 categories", "calculation within 5%")
- **Estimated Depth**: the plan's Target level (High school / Master's / Advanced)
- **Principle**: Which principle(s) from Step 1.75 this sub-goal tests
- **Exercise**: A simple, concrete, self-contained hands-on exercise the learner can do to practice this concept. Should be completable in 5-10 minutes with clear instructions and expected outcome. Different from the Initial/Final Tests — this is a practice activity, not an assessment.
- **Anticipated CTQs**: 2-4 Critical-To-Quality criteria for this sub-goal. Each CTQ: what must be understood + mastery test + common failure mode (using CTQ failure mode taxonomy: conflation, overgeneralization, missing-prerequisite, procedural-without-conceptual, verbal-without-formal, formal-without-intuitive)
- **Teach Topics**: Key concepts, exercises, and known pitfalls with CTQ failure mode classification (e.g., "[conflation]: confusing indirect costs with contingency", "[procedural-without-conceptual]: applying formula without understanding boundary conditions")
- **Final Test**: A DIFFERENT practical case testing the same competencies

#### Core Principle blueprint (Core Principle SGs only):

Core Principle blueprints include a **fully worked example in the plan itself** — this, and the additions of a hard-core blueprint below, are the only exceptions to the "no teaching content in the plan" rule. The worked example grounds the abstract principle in concrete reality.

- **Principle**: The principle name and statement from Step 1.75
- **Worked Example (foundational)**: A simple, fully worked example demonstrating the principle in the most basic scenario. 2-4 steps, concrete numbers, every step shown explicitly, annotated with "Why" notes explaining reasoning, ending with a Check that confirms the result a second way. This is the simplest possible scenario that makes the principle visible — not a complex application.
- **Initial Test**: A simple scenario testing whether the learner can STATE the principle in their own words AND APPLY it to a basic case. Simpler than Key Concept tests.
- **Pass Criteria**: "Can state the principle in own words AND apply it to a basic scenario correctly"
- **Estimated Depth**: the plan's Target level
- **Exercise**: A simple, concrete, self-contained hands-on exercise the learner can do to practice this principle. Should be completable in 5-10 minutes. Different from the Initial/Final Tests — this is a practice activity, not an assessment.
- **Anticipated CTQs**: 1-2 CTQs focused on understanding the principle, not applying advanced techniques
- **Teach Topics**: The principle itself, its boundary conditions, common misunderstandings
- **Final Test**: A DIFFERENT simple scenario testing the same principle

#### Hard-core blueprint (the Core Principle SG of each principle flagged in Step 2.75):

A hard-core blueprint is a Core Principle blueprint with an aha design and a level ladder added. In a session, the learner predicts, the prediction fails, and the explanation starts from that failure. Write the added parts as the concept-explainer skill's Level Ladder describes.

- **Principle**: as in a Core Principle blueprint
- **Tempting answer**: the natural, confident, wrong answer to the Initial Test, and why it feels right
- **Insight**: the one sentence that makes it click. It reframes the situation; it does not recite the formal statement.
- **Picture**: one picture or analogy that carries the Insight, and where it stops being true
- **Worked Example (foundational)**: as in a Core Principle blueprint. Here it is also the smallest example of the Insight, and the solved exercise of the High school rung.
- **Level ladder**: one fully solved exercise for each level above High school, up to the Target level (none when the Target level is High school). Each is the same idea seen with that level's tools, not a harder calculation at the level below. Same format as the worked example: Given, every step with its "Why", Result, and a Check that confirms the result a second way.
- **Initial Test**: a practical case at the Target level in which the natural approach leads to the Tempting answer. Ask the learner to predict and to justify. Do not warn, and do not hint that the obvious answer is wrong.
- **Pass Criteria**: "Gives the right answer, not the tempting one, AND justifies it at the Target level"
- **Estimated Depth**: the plan's Target level
- **Exercise**: as in a Core Principle blueprint
- **Anticipated CTQs**: at least one for each rung of the climb, from High school up to the Target level; name the rung in the Source column
- **Teach Topics**: the principle, its boundary conditions, and the misunderstandings that survive the Insight
- **Final Test**: a DIFFERENT practical case at the Target level in which the same tempting reasoning is again available

Rules:
- No test reuses the case of a solved exercise in the plan, and the solved exercises do not reuse each other's case
- Once a hard-core blueprint is written, re-read that principle's Breakthrough row (Step 1.9). If it states the Tempting answer or the test case, rewrite it at the level of history or practice: the top of the plan must not give the test away.

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

First use Glob to check whether `<topic>_training_plan.md` already exists in the current directory. If it does, do not overwrite it: ask the learner whether to replace it or to keep both. To keep both (and whenever you cannot ask), put the level in the name, `<topic>-hs`, `<topic>-msc` or `<topic>-adv`, and use that as the `<topic>` of this plan.

Use the Write tool to create `<topic>_training_plan.md` in the current directory. Use this exact format:

```markdown
# Training Plan: <Title>
Generated: <date> | Status: in-progress | Target level: <High school/Master's/Advanced>

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

## Hard Core
> _The principles that are hardest to grasp. Each is taught through an aha
> moment and a climb through the levels, with a solved exercise at every rung.
> If this list looks wrong to you, tell me which principle to add or remove._

| Principle | Why it is hard | Taught in |
|-----------|----------------|-----------|
| <principle name> | <counter-intuitive / new abstraction / persistent misconception / load-bearing> | SG-<N> |

(If no principle qualifies, write "No principle in this plan is hard-core." in place of the table.)

## Key Facts
> _What this course relies on you simply knowing. Values marked `(verify)`
> should be checked against a source before you rely on them._

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | <one fact, with its value and unit> | <what goes wrong without it> | SG-<N>, ... |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | <statement> | <domain> | low | <HS/MSc/Adv> | — | pending | - |
| SG-2 | Core Principle | <statement> | <domain> | low | <HS/MSc/Adv> | <principle> | pending | - |
| SG-3 | Core Principle | <statement> | <domain> | low | <HS/MSc/Adv> | <principle> | pending | - |
| ... | Core Principle | ... | ... | low | <HS/MSc/Adv> | ... | ... | ... |
| SG-N | Key Concept | <statement> | <domain> | <low/med/high> | <HS/MSc/Adv> | <principle> | pending | - |
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
> _Session designs. Run a sub-goal's session before reading its blueprint: the
> tests work best unseen. The solved exercises are there to study afterwards._

### SG-1: <Motivation short title>
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** <Target level>
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
  > **Check:** <the result confirmed a second way>
- **Initial Test:** <simple scenario testing principle understanding>
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** <Target level>
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <principle> | <verification task> | <failure pattern> |
- **Teach Topics:** <the principle, boundary conditions, common misunderstandings>
- **Final Test:** <different simple scenario testing same principle>

### SG-3: <Hard-core principle short title>
- **Principle:** <principle name> — <principle statement>
- **Tempting answer:** <the natural, confident, wrong answer to the Initial Test, and why it feels right>
- **Insight:** <the one sentence that makes it click>
- **Picture:** <one picture or analogy, and where it stops being true>
- **Worked Example (foundational):**
  **Given:** <the smallest case in which the Insight is visible, with concrete numbers>
  **Step 1:** <operation>
  > **Why:** <reasoning>
  **Step 2:** <operation>
  > **Why:** <reasoning>
  **Result:** <answer with units and interpretation>
  > **Check:** <the result confirmed a second way>
- **Level ladder:** <one solved exercise for each level above High school, up to the Target level>
  **Master's solved exercise** (not in a High school plan)
  **Given:** <the same idea, in the field's notation>
  **Step 1:** <operation>
  > **Why:** <reasoning>
  **Result:** <answer with interpretation>
  > **Check:** <the result confirmed a second way>
  **Advanced solved exercise** (only in an Advanced plan)
  **Given:** <the same idea in full generality: a proof, a derivation or a non-standard case>
  **Step 1:** <operation>
  > **Why:** <reasoning>
  **Result:** <answer with interpretation>
  > **Check:** <the result confirmed a second way>
- **Initial Test:** <practical case in which the natural approach leads to the Tempting answer: predict and justify>
- **Pass Criteria:** Gives the right answer, not the tempting one, AND justifies it at the Target level
- **Estimated Depth:** <Target level>
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood at this rung> | <principle>, <level> rung | <verification task> | <failure pattern> |
- **Teach Topics:** <the principle, boundary conditions, the misunderstandings that survive the Insight>
- **Final Test:** <different case in which the same tempting reasoning is again available>

### SG-N: <Key Concept short title>
- **Initial Test:** <practical case description>
- **Pass Criteria:** <measurable threshold>
- **Estimated Depth:** <Target level>
- **Principle:** <principle name>
- **Exercise:** <simple hands-on exercise, 5-10 min, concrete and self-contained>
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | <what must be understood> | <concept> | <verification task> | <failure pattern> |
- **Teach Topics:** <concepts, exercises, pitfalls with CTQ failure mode tags>
- **Final Test:** <different case, same competencies>

(repeat for every sub-goal — Core Principle SGs include the Worked Example field, others do not; only the principles listed in `## Hard Core` use the hard-core form)

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

Read back the file you just wrote: from the top through the Sub-Goals table, the blueprint headings and their field names, and each hard-core blueprint in full. Confirm each row below. Where a row fails, fix the file with the Edit tool and check that row again.

| Element | Present when |
|---------|--------------|
| Core principles identification | Every row of `## Principle Extraction` has exactly one Core Principle row in `## Sub-Goals`, and every Core Principle row names a principle from that table |
| Key facts identification | `## Key Facts` has at least one row, and every `Used in` cell names sub-goals that exist |
| Motivation | `## Motivation & Course Overview (VOC)` has its four parts filled in, and SG-1 is on the Motivation axis |
| Breakthrough | `## Breakthrough` has its three labelled parts filled in and one table row for each principle in `## Principle Extraction` |
| Method | `## Pedagogical Method: Test-Teach-Test` is present with its three steps and its teaching-style line, and every blueprint has an Initial Test and a Final Test |
| Levels | The header line has a `Target level:` of High school, Master's or Advanced, and every Depth cell and every Estimated Depth is that level |
| Hard core | `## Hard Core` is present. Every principle it lists has, in its Core Principle blueprint, a Tempting answer, an Insight, a Picture, a foundational worked example and one solved exercise for each level above High school up to the Target level, each ending with a Check. No other blueprint has those fields. No test reuses a solved exercise's case. |

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The Target level (if it was not stated and you could not ask, say that Master's was assumed and that the plan can be created again at another level)
- The teaching method: Test-Teach-Test with direct explanation
- The Motivation & Course Overview (VOC) — and **invite the learner to review and edit it**. State that edits are welcome and that feedback on it may **restructure the course**.
- The Breakthrough: before the intuition, the intuition, what it solved
- The principle extraction table
- The hard core: which principles were flagged and why, and that each will be taught through an aha moment and a climb through the levels. **Ask the learner to confirm the list or change it.**
- The key facts: how many there are, and which are marked `(verify)` for the learner to confirm against a source
- The sub-goals table
- Any prerequisite warnings (external prerequisites not confirmed in learner profile)
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan (if profile existed)
- The result of the required-elements check (Step 4.5), one line per element
- Remind the user to run `/run-session SG-<N>` to start learning

**VOC feedback → restructure rule:** If the learner revises the Motivation & Course Overview (or gives feedback on it), re-evaluate whether the current sub-goal decomposition still matches the stated scope and outcomes. If it no longer matches, **offer to re-decompose (restructure) the plan** using the normal decomposition rules — update the Sub-Goals table, Prerequisite Graph, and Sequence, the Breakthrough and Hard Core rows if the principles changed, and the Key Facts `Used in` column — then refresh the VOC digest so it stays consistent with the revised plan and re-run the check in Step 4.5.

**Hard-core list → blueprint rule:** If the learner asks to add a principle to the Hard Core, apply the gate from Step 2.75. If a tempting answer can be written, add the hard-core fields to that principle's Core Principle blueprint, rebuild its tests on the Tempting answer, and add the row to `## Hard Core`; if not, say why the principle cannot be taught that way. If the learner asks to remove one, remove its Tempting answer, Insight, Picture and Level ladder, restore the standard Core Principle tests, and remove the row. No re-decomposition is needed. Re-run the check in Step 4.5.

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example, and hard-core blueprints, which also hold the aha design (Tempting answer, Insight, Picture) and the Level ladder's solved exercises
- The plan names and motivates; it does not explain or derive. The Breakthrough section and the Key Facts table are orientation: state them, never teach from them.
- Do NOT skip the required-elements check (Step 4.5): a plan missing one of its required elements is incomplete
- The Target level is fixed for the plan: every sub-goal, test and pass criterion is written for it, and nothing above it is written into the plan
- Do NOT overwrite an existing plan file without asking (Step 4)
- Do NOT skip the session blueprint for any sub-goal
- Practical cases must be realistic scenarios, not abstract questions
- The `<topic>` in the filename should be a short kebab-case slug derived from the goal (e.g., `cost-estimation`, `python-data-analysis`)
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
