---
name: create-training-plan
description: Create a customized training plan from a learning goal. Socratic by default (each concept reached through questions); add the word direct for direct explanation
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Skill
---

You are creating a customized training plan using the **Test-Teach-Test (TTT)** methodology.

The user wants to learn: **$ARGUMENTS**

## Step 0: Choose the Teaching Method

A plan teaches in one of two ways:

| Method | How a concept reaches the learner | Created when |
|--------|-----------------------------------|--------------|
| **Socratic** (the default) | Through a chain of questions, so that the learner states the idea before it is explained | The goal does not ask for direct explanation |
| **Direct explanation** | Test first, then the gaps are explained | The goal contains the word `direct`, or the learner asks for direct explanation or for "no Socratic" |

**Default: Socratic.** Do NOT follow the rest of this file. Hand the goal, unchanged, to this plugin's `socratic-training-plan` command: invoke it with the Skill tool (`training-plan:socratic-training-plan`; `socratic-training-plan` when the plugin is loaded without a prefix). If it cannot be invoked, find its file with Glob (`**/commands/socratic-training-plan.md`), Read it, and follow it in full with the same goal. Tell the learner in one line that the plan is Socratic and that `direct` in the goal gives direct explanation.

**Direct explanation.** Remove the word `direct` from the goal and continue with the steps below.

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

Compute the learner's progress as the course-model skill describes (`python3 <path>/course.py progress .` when Python is available; otherwise read every `*/course.json` below the current folder). A 3.x `learner_profile.md`, if present, counts too.

If any course exists, note:
- **Known strengths**: Topics the learner has mastered (passed Initial Test with zero gaps). If any relate to this new goal, plan harder initial tests for those sub-goals.
- **Gap patterns**: Recurring weaknesses. If any relate to this new goal, note them in the Teach Topics of relevant session blueprints so they get proactive coverage.

If there is no earlier course, proceed normally.

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
- In the `## Hard Core` table, give each reason as the criterion's name only: counter-intuitive, new abstraction, persistent misconception, load-bearing (for load-bearing you may add how many sub-goals depend on it). Do not describe the misconception or the insight there: the top of the plan must not give a test away.
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
- **Visual design**: how the principle is shown on an interactive page, for sessions run with visual delivery. Five parts, as the visual-explainer skill defines them: **Objects** (what is drawn, kept tiny, with exact values), **Colour roles** (one colour per role, at most three), **Steps** (the order in which the objects appear, one sentence each), **Your-turn inputs** (for each rung: what the learner enters, the right value, and the two most likely wrong values with what each reveals) and **Control** (the one thing the learner can change, and what it shows). Design it from the Picture and the solved exercises. It adds no teaching content of its own.
- **Worked Example (foundational)**: as in a Core Principle blueprint. Here it is also the smallest example of the Insight, and the solved exercise of the High school rung.
- **Level ladder**: one fully solved exercise for each level above High school, up to the Target level. In a High school plan there is no rung above the foundational worked example: keep the field and write "none: the foundational worked example is the only rung". Each is the same idea seen with that level's tools, not a harder calculation at the level below. Same format as the worked example: Given, every step with its "Why", Result, and a Check that confirms the result a second way.
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
- It is stored in `overview` (Step 4) and shown at the top of `overview.md`, so the learner sees the big picture before the details.

### Step 4: Write the Course

The course is stored as **one file**, `course.json`, in a folder named after the course, with a generated outline beside it. Read the **course-model** skill (Glob `**/skills/course-model/SKILL.md`) and its schema `course.schema.json` before writing: they define every field, the folder layout and the rules. Do not write a Markdown plan file.

1. **Choose the folder.** The course id is a short lowercase slug of the topic (`cost-estimation`, `transformer-attention`). If `<course-id>/course.json` already exists, do not overwrite it: ask whether to replace it or to keep both (keep both by adding a suffix such as `-2` to the new id).
2. **Write `<course-id>/course.json`** with the Write tool. Put what Steps 1 to 3.5 produced into these fields:

| What you designed | Field in `course.json` |
|---|---|
| The learner's goal as typed / the refined goal (Step 1) | `course.goal_as_given` / `course.goal` |
| The level (Step 1) | `course.level`: `high-school`, `masters` or `advanced` |
| The method | `course.method`: `direct` |
| Delivery | `course.delivery`: `app` (lessons on a page), or `chat` if the learner asked for chat |
| The overview (Step 3.5) | `overview`: `why_it_matters`, `what_you_will_learn`, `principles_and_facts`, `you_will_be_able_to` |
| The breakthrough (Step 1.9) | `story`: `before`, `the_aha`, `what_it_solved`, and one `by_principle` row per principle |
| Principle extraction (Step 1.75) | `principles[]`: `P1`... with name, statement, formal, needs |
| The hard core (Step 2.75) | `key_idea: true` and `why_hard` on those principles |
| Key facts (Step 1.8) | `facts[]`: `F1`... with `used_in` lesson ids and `verify` for values to check |
| External prerequisites (Step 2.5) | `background[]` |
| Sub-goals, in order (Step 2) | `lessons[]`: `L1`, `L2`... numbered in the recommended order, with `kind` (Motivation → `why`, Core Principle → `principle`, Key Concept → `concept`, Tools → `tool`, Verification → `capstone`), title, goal, area, difficulty, principles, `needs` (the lessons each one depends on, from the prerequisite graph), `key_idea` |
| Each blueprint (Step 3) | that lesson's `design`: Initial Test and Pass Criteria → `try_first.question` and `try_first.marking.pass`; Final Test → `final_check`; Anticipated CTQs → `success_criteria` (the failure-mode tag becomes `common_mistake.kind`: conflation → `mixing-up`, overgeneralization → `overstretching`, missing-prerequisite → `missing-background`, procedural-without-conceptual → `steps-without-why`, verbal-without-formal → `words-without-maths`, formal-without-intuitive → `maths-without-picture`); Exercise → `practice_task`; Teach Topics → `to_teach`; the principle → `principle_statement`; the worked example → `worked_example` (`given`, `steps` with `do` and `why`, `result`, `check`) |
| Each hard-core blueprint | also `trap` (the tempting answer, also copied to `try_first.marking.trap`), `aha` (the insight), `picture`, `visual` (objects, colour_roles, steps, your_turn, control) and `levels` (one `{level, example}` per level above High school up to the course level) |
| Every lesson's state | `{"status": "not-started", "attempts": []}` |
| Files | `files[]`: one row for `overview.md` (kind `overview`) |
| History | `history[]`: `{"at": "<today>", "event": "Course created"}` |

3. **Validate and render.** If `python3` is available, run the course-model tool: `python3 <path>/course.py validate <course-id>/course.json --files`, fix every error it reports and run it again until it passes, then `python3 <path>/course.py render-overview <course-id>/course.json`. Without Python, check the rules in section 4 of the course-model skill yourself and write `overview.md` as its section 5 describes. The overview never contains tests, marking guides or worked solutions.

### Step 4.5: Check the Required Elements

Confirm each row below in `course.json`. Where a row fails, fix the file and validate again.

| Element | Present when |
|---------|--------------|
| Core principles identification | Every principle has exactly one lesson of kind `principle`, and every principle lesson names a principle |
| Key facts identification | `facts` has at least one entry, and every `used_in` names an existing lesson |
| Motivation | `overview` has its four parts filled in, and Lesson 1 is of kind `why` |
| Breakthrough | `story` has `before`, `the_aha` and `what_it_solved`, and one `by_principle` row per principle |
| Method | `course.method` is `direct`, and every lesson has `try_first` and `final_check` |
| Levels | `course.level` is set, and every test and pass standard is written for that level |
| Hard core | At least one principle has `key_idea: true` unless no principle passed the gate (then say so). Every key-idea lesson has `trap`, `aha`, `picture`, `visual`, a worked example and the right `levels` for the course level, each example ending with a `check`. No other lesson has these fields. No test reuses a worked example's case |

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
- Where the course is: `<course-id>/course.json`, with the readable outline in `<course-id>/overview.md`
- Remind the user to run `/run-session 1` (or the number of the suggested lesson) to start learning

**VOC feedback → restructure rule:** If the learner revises the Motivation & Course Overview (or gives feedback on it), re-evaluate whether the current sub-goal decomposition still matches the stated scope and outcomes. If it no longer matches, **offer to re-decompose (restructure) the plan** using the normal decomposition rules — update the Sub-Goals table, Prerequisite Graph, and Sequence, the Breakthrough and Hard Core rows if the principles changed, and the Key Facts `Used in` column — then refresh the VOC digest so it stays consistent with the revised plan and re-run the check in Step 4.5.

**Hard-core list → blueprint rule:** If the learner asks to add a principle to the Hard Core, apply the gate from Step 2.75. If a tempting answer can be written, add the hard-core fields to that principle's Core Principle blueprint, rebuild its tests on the Tempting answer, and add the row to `## Hard Core`; if not, say why the principle cannot be taught that way. If the learner asks to remove one, remove its Tempting answer, Insight, Picture, Visual design and Level ladder, restore the standard Core Principle tests, and remove the row. No re-decomposition is needed. Re-run the check in Step 4.5.

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example, and hard-core blueprints, which also hold the aha design (Tempting answer, Insight, Picture, Visual design) and the Level ladder's solved exercises
- The plan names and motivates; it does not explain or derive. The Breakthrough section and the Key Facts table are orientation: state them, never teach from them.
- Do NOT skip the required-elements check (Step 4.5): a plan missing one of its required elements is incomplete
- The Target level is fixed for the plan: every sub-goal, test and pass criterion is written for it, and nothing above it is written into the plan
- Do NOT overwrite an existing course without asking (Step 4)
- Do NOT skip the session blueprint for any sub-goal
- Practical cases must be realistic scenarios, not abstract questions
- The course id should be a short kebab-case slug derived from the goal (e.g., `cost-estimation`, `python-data-analysis`)
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
