---
name: socratic-training-plan
description: Create a Socratic training plan where each concept arises from a discovery question and the conclusion feels inevitable
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Bash(python3:*)
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
- The Breakthrough is the real history. The Motivation sub-goal (SG-1) builds its questions and tests on that same history: they ask the learner to predict or explain what the earlier approaches really do, never to recite the story, and never on an invented substitute
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

### Step 2.75: Flag the Hard Core

Some core principles are much harder to grasp than the rest, and the course stands or falls on them. Flag them: each gets an aha designed around a failed prediction and is taught as a climb through the levels.

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

### Step 3: Design Socratic Session Blueprints

For each sub-goal, design a TTT session blueprint with Socratic extensions. Every Discovery Question, test and Guidance Chain is written at the Target level: it assumes that level's tools (see the table in Step 1).

#### Standard Socratic blueprint (Key Concept, Tools, Motivation, Verification SGs):

All fields from the standard blueprint PLUS Socratic extensions:

- **Context**: the session's opening, shown BEFORE the Discovery Question or the Initial Test. Two short parts. *Why it matters*: one or two sentences on what this sub-goal lets the learner do. *Historical context*: two to four sentences on the real situation this idea came out of: what was done before, where it broke down, who changed it and when (names and dates only when certain). It sets the scene and stops before the idea itself: it states no answer to the session's questions, and names no mechanism, formula or conclusion that its tests ask the learner to find. Write the Context after the tests, and check it against them.
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
- **Worked Example (foundational)**: A simple, fully worked example. 2-4 steps, concrete numbers, every step shown explicitly, annotated with "Why" notes, ending with a Check that confirms the result a second way. **Socratic framing:** each "Why" note should be phrased as an answer to a question the learner would naturally ask at that step.
- **Discovery Question**: The question that makes the learner *want* this principle. It should create a puzzle or tension that only this principle resolves.
- **Initial Test**: A simple scenario. **Socratic design:** include a "wrong path" — a plausible but incorrect approach that surfaces the key insight when it fails.
- **Pass Criteria**: Can state the principle in own words AND apply it AND explain why the alternative fails
- **Estimated Depth**: the plan's Target level
- **Socratic Guidance Chain**: 3-6 questions leading to the principle's discovery
- **Anticipated CTQs**: 1-2 CTQs focused on understanding the principle
- **Teach Topics**: The principle, boundary conditions, common misunderstandings. Include Socratic teaching notes.
- **Final Test**: A DIFFERENT simple scenario. Include a "reconstruct the reasoning" component.

#### Hard-core Socratic blueprint (the Core Principle SG of each principle flagged in Step 2.75):

A hard-core Socratic blueprint is a Core Principle Socratic blueprint with an aha design and a level ladder added. In a session, the learner predicts, the prediction fails, and the Guidance Chain leads the learner to the insight. Write the added parts as the concept-explainer skill's Level Ladder describes.

- **Principle**: as in a Core Principle Socratic blueprint
- **Tempting answer**: the natural, confident, wrong answer that the designed wrong path leads to, and why it feels right
- **Insight**: the one sentence the Guidance Chain leads the learner to say. It reframes the situation; it does not recite the formal statement.
- **Picture**: one picture or analogy that carries the Insight, and where it stops being true. In the session it is shown only after the learner has stated the Insight.
- **Visual design**: how the principle is shown on an interactive page, for sessions run with visual delivery. Five parts, as the visual-explainer skill defines them: **Objects** (what is drawn, kept tiny, with exact values), **Colour roles** (one colour per role, at most three), **Steps** (the order in which the objects appear, one sentence each), **Your-turn inputs** (for each rung: what the learner enters, the right value, and the two most likely wrong values with what each reveals) and **Control** (the one thing the learner can change, and what it shows). Design it from the Picture and the solved exercises, but every Your-turn input uses a NEW case: values used nowhere else in the plan, so that its answer is not already shown in a solved exercise. It adds no teaching content of its own. In a Socratic session the page is built only after the learner has stated the Insight.
- **Worked Example (foundational)**: as in a Core Principle Socratic blueprint. Here it is also the smallest example of the Insight, and the solved exercise of the High school rung.
- **Level ladder**: one fully solved exercise for each level above High school, up to the Target level. In a High school plan there is no rung above the foundational worked example: keep the field and write "none: the foundational worked example is the only rung". Each is the same idea seen with that level's tools, not a harder calculation at the level below. Same format as the worked example: Given, every step with its "Why", Result, and a Check that confirms the result a second way.
- **Discovery Question** and **Initial Test**: the designed wrong path IS the Tempting answer. Ask the learner to predict and to justify, at the Target level. Do not warn, and do not hint that the obvious answer is wrong.
- **Pass Criteria**: "Gives the right answer, not the tempting one, AND justifies it at the Target level AND explains why the tempting answer fails"
- **Estimated Depth**: the plan's Target level
- **Socratic Guidance Chain**: 3-6 questions that lead to the Insight
- **Anticipated CTQs**: at least one for each rung of the climb, from High school up to the Target level; name the rung in the Source column
- **Teach Topics**: the principle, its boundary conditions, and the misunderstandings that survive the Insight. Include Socratic teaching notes.
- **Final Test**: a DIFFERENT case at the Target level in which the same tempting reasoning is again available, with the "reconstruct the reasoning" component

Rules:
- No test reuses the case of a solved exercise in the plan, and the solved exercises do not reuse each other's case
- Once a hard-core blueprint is written, re-read that principle's Breakthrough row (Step 1.9). If it states the Tempting answer or the test case, rewrite it at the level of history or practice: the top of the plan must not give the test away.

If the learner profile indicated strengths or gap patterns relevant to a sub-goal, note them in the blueprint:
- **Profile note (strength):** "Learner has prior mastery in [topic] -- set Initial Test at elevated difficulty"
- **Profile note (gap pattern):** "Learner has recurring gap in [pattern] -- include proactive Quick Check in Teach Topics even if not identified in Initial Test"

**Key facts in tests:** when a test or exercise depends on a fact, that fact must be in the Key Facts table from Step 1.8. If it is missing, add it.

**Test quality rules** (every Discovery Question, test, check and Guidance Chain question):
- **A clear question.** Each question asks one thing, says plainly what is asked, and says in what form the answer is expected (a number, a choice, one sentence). A reader who knows the answer must be able to tell that it answers the question. No question depends on guessing what the author had in mind.
- **A true case.** A case is built on something that really was done or really is done: a method that was in use, a real system's behaviour, a real engineering decision. Never invent a method nobody uses in order to knock it down. Every statement the case makes must be true outside the toy example; when a toy simplifies, say what was simplified.
- **The Motivation sub-goal uses the real history.** Its questions and tests are built on the actual problem the topic solved, as the Breakthrough tells it, with the earlier approaches named as they were. Its questions ask the learner to predict or explain what those real approaches do, not to recite the story.

**Every blueprint, of every kind, starts with a `Context` field** (defined above), written before its other fields.

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
- It is stored in `overview` (Step 4) and shown at the top of `overview.md`, so the learner sees the big picture before the details.

### Step 4: Write the Course

The course is stored as **one file**, `course.json`, in a folder named after the course, with a generated outline beside it. Before writing, load the **course-model** skill (the Skill tool, `training-plan:course-model`; or Read `**/skills/course-model/SKILL.md`) and get its two reference files: `example-course.json` (a complete, valid three-lesson course) and `course.schema.json` (every field and allowed value). Read them from the skill's folder, or print them with `python3 <skill folder>/tools/course.py example` and `... schema` when reading the folder is not allowed. **Use exactly the field names and nesting of `example-course.json`; never invent a field or rename one.** Do not write a Markdown plan file.

1. **Choose the folder.** The course id is a short lowercase slug of the topic (`cost-estimation`, `transformer-attention`). If `<course-id>/course.json` already exists, do not overwrite it: ask whether to replace it or to keep both (keep both by adding a suffix such as `-2` to the new id).
2. **Write `<course-id>/course.json`** with the Write tool. Put what Steps 1 to 3.5 produced into these fields:

| What you designed | Field in `course.json` |
|---|---|
| The learner's goal as typed / the refined goal (Step 1) | `course.goal_as_given` / `course.goal` |
| The level (Step 1) | `course.level`: `high-school`, `masters` or `advanced` |
| The method | `course.method`: `socratic` |
| Delivery | `course.delivery`: `app` (lessons on a page), or `chat` if the learner asked for chat |
| The overview (Step 3.5) | `overview`: `why_it_matters`, `what_you_will_learn`, `principles_and_facts`, `you_will_be_able_to` |
| The breakthrough (Step 1.9) | `story`: `before`, `the_aha`, `what_it_solved`, and one `by_principle` row per principle |
| Principle extraction (Step 1.75) | `principles[]`: `P1`... with name, statement, formal, needs |
| The hard core (Step 2.75) | `key_idea: true` and `why_hard` on those principles |
| Key facts (Step 1.8) | `facts[]`: `F1`... with `used_in` lesson ids and `verify` for values to check |
| External prerequisites (Step 2.5) | `background[]` |
| Sub-goals, in order (Step 2) | `lessons[]`: `L1`, `L2`... numbered in the recommended order, with `kind` (Motivation → `why`, Core Principle → `principle`, Key Concept → `concept`, Tools → `tool`, Verification → `capstone`), title, goal, area, difficulty, principles, `needs` (the lessons each one depends on, from the prerequisite graph), `key_idea` |
| Each blueprint (Step 3) | that lesson's `design`: Initial Test and Pass Criteria → `try_first.question` and `try_first.marking.pass`; Final Test → `final_check`; Anticipated CTQs → `success_criteria` (the failure-mode tag becomes `common_mistake.kind`: conflation → `mixing-up`, overgeneralization → `overstretching`, missing-prerequisite → `missing-background`, procedural-without-conceptual → `steps-without-why`, verbal-without-formal → `words-without-maths`, formal-without-intuitive → `maths-without-picture`); Exercise → `practice_task`; Teach Topics → `to_teach`; the `Context` (why it matters, historical context) → `context`; the principle → `principle_statement`; the worked example → `worked_example` (`given`, `steps` with `do` and `why`, `result`, `check`); the Discovery Question → `puzzle`; the Socratic Guidance Chain → `guiding_questions`; the reconstruct-the-reasoning part of the Final Test → `final_check.marking.explain_it_back`; the designed wrong path → `try_first.marking.trap` |
| Each hard-core blueprint | also `trap` (the tempting answer, also copied to `try_first.marking.trap`), `aha` (the insight), `picture`, `visual` (objects, colour_roles, steps, your_turn, control) and `levels` (one `{level, example}` per level above High school up to the course level) |
| Every lesson's state | `{"status": "not-started", "attempts": []}` |
| Files | `files[]`: one row for `overview.md` (kind `overview`) |
| History | `history[]`: `{"at": "<today>", "event": "Course created"}` |

3. **Validate and render.** Run the course-model tool with Bash: `python3 <skill folder>/tools/course.py validate <course-id>/course.json --files`. Fix every error it reports and run it again until it prints `OK`. Then run `python3 <skill folder>/tools/course.py render-overview <course-id>/course.json`. Only if Bash or Python is unavailable: compare every field name in your file with `example-course.json` and the schema, check the rules in section 4 of the course-model skill yourself, write `overview.md` as its section 5 describes, and tell the learner that the course was checked by hand. The overview never contains tests, marking guides or worked solutions.

### Step 4.5: Check the Required Elements

Confirm each row below in `course.json`. Where a row fails, fix the file and validate again.

| Element | Present when |
|---------|--------------|
| Core principles identification | Every principle has exactly one lesson of kind `principle`, and every principle lesson names a principle |
| Key facts identification | `facts` has at least one entry, and every `used_in` names an existing lesson |
| Motivation | `overview` has its four parts filled in, Lesson 1 is of kind `why` and is built on the real history, and every lesson has a `design.context` (why it matters, historical context) that gives no answer away |
| Test quality | Every question asks one thing and says what form the answer takes; every case is something really done, with no invented method to knock down |
| Context gives nothing away | Read each lesson's `design.context` against its own puzzle, Try first and final check: the context names the problem and the history, and states none of the answers (no mechanism, formula, number or conclusion the tests ask the learner to find) |
| Novel cases | No Your-turn input, exercise or test reuses a case whose answer is worked out elsewhere in the course |
| Breakthrough | `story` has `before`, `the_aha` and `what_it_solved`, and one `by_principle` row per principle |
| Method | `course.method` is `socratic`, and every lesson has `try_first` and `final_check`, and every lesson has a `puzzle` and 3 to 6 `guiding_questions` |
| Levels | `course.level` is set, and every test and pass standard is written for that level |
| Hard core | At least one principle has `key_idea: true` unless no principle passed the gate (then say so). Every key-idea lesson has `trap`, `aha`, `picture`, `visual`, a worked example and the right `levels` for the course level, each example ending with a `check`. No other lesson has these fields. No test reuses a worked example's case |

### Step 5: Confirm to the User

After writing the file, present a summary:
- The SMART goal
- The Target level (if it was not stated and you could not ask, say that Master's was assumed and that the plan can be created again at another level)
- The Socratic method explanation (Question → Tension → Resolution → Test) and how it maps onto Test-Teach-Test
- The Motivation & Course Overview (VOC) — and **invite the learner to review and edit it**. State that edits are welcome and that feedback on it may **restructure the course**.
- The Breakthrough: before the intuition, the intuition, what it solved
- The principle extraction table
- The hard core: which principles were flagged and why, and that each will be taught through an aha moment and a climb through the levels. **Ask the learner to confirm the list or change it.**
- The key facts: how many there are, and which are marked `(verify)` for the learner to confirm against a source
- The sub-goals table (note the "Discover" framing)
- Any prerequisite warnings
- The suggested starting sub-goal
- Any learner profile notes that influenced the plan
- The result of the required-elements check (Step 4.5), one line per element
- Where the course is: `<course-id>/course.json`, with the readable outline in `<course-id>/overview.md`
- Remind the user to run `/run-session 1` (or the number of the suggested lesson) to start learning

**VOC feedback → restructure rule:** If the learner revises the Motivation & Course Overview (or gives feedback on it), re-evaluate whether the current sub-goal decomposition still matches the stated scope and outcomes. If it no longer matches, **offer to re-decompose (restructure) the plan** using the normal decomposition rules — update the Sub-Goals table, Prerequisite Graph, and Sequence, the Breakthrough and Hard Core rows if the principles changed, and the Key Facts `Used in` column — then refresh the VOC digest so it stays consistent with the revised plan and re-run the check in Step 4.5.

**Hard-core list → blueprint rule:** If the learner asks to add a principle to the Hard Core, apply the gate from Step 2.75. If a tempting answer can be written, add the hard-core fields to that principle's Core Principle blueprint, rebuild its Discovery Question and tests on the Tempting answer, and add the row to `## Hard Core`; if not, say why the principle cannot be taught that way. If the learner asks to remove one, remove its Tempting answer, Insight, Picture, Visual design and Level ladder, restore the standard Core Principle tests, and remove the row. No re-decomposition is needed. Re-run the check in Step 4.5.

## Important

- Do NOT include theory or teaching content in the plan -- that happens during `/run-session` -- EXCEPT for Core Principle SG blueprints, which MUST include a simple fully worked example, and hard-core blueprints, which also hold the aha design (Tempting answer, Insight, Picture, Visual design) and the Level ladder's solved exercises
- The plan names and motivates; it does not explain or derive. The Breakthrough section and the Key Facts table are orientation: state them, never teach from them.
- Do NOT skip the required-elements check (Step 4.5): a plan missing one of its required elements is incomplete
- The Target level is fixed for the plan: every sub-goal, test and pass criterion is written for it, and nothing above it is written into the plan
- Do NOT overwrite an existing course without asking (Step 4)
- Do NOT skip the session blueprint for any sub-goal
- Every blueprint MUST include a Discovery Question and a Socratic Guidance Chain
- Cases must be real: built on something that was or is really done, never on an invented method. Every question must be clear: one thing asked, the form of the answer stated
- Discovery Questions must create genuine tension — not just ask "what do you know about X?"
- Socratic Guidance Chains must narrow progressively — the last question should make the answer inescapable
- Initial Tests should have a designed "wrong path" that reveals the concept's necessity
- Final Tests must include a "reconstruct the reasoning" or "explain why" component
- The course id should be a short kebab-case slug derived from the goal (e.g., `bayes-medical-tests`); the method is recorded in `course.method`, not in the name
- Every sub-goal dependency must trace to the prerequisite graph -- no intuited dependencies
