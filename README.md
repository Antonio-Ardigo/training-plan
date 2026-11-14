# Training Plan Plugin

Generate customized learning paths using **Test-Teach-Test (TTT)** methodology with integrated concept-builder pedagogy. Built for difficult subjects: the hardest principles of a topic get an explanation designed around an aha moment, taught at three levels, with fully worked exercises.

## Install

In Claude Code, add this repository as a marketplace and install the plugin from it:

```
/plugin marketplace add Antonio-Ardigo/training-plan
/plugin install training-plan@training-plan
```

On Claude Code 2.1.275 or later this works in one step:

```
/plugin install training-plan --marketplace Antonio-Ardigo/training-plan
```

Installed this way, each command carries the plugin's name: `/training-plan:create-training-plan`, `/training-plan:run-session`, and so on. The commands below are written in their short form.

To try the plugin from a local copy without installing it, start Claude Code with `claude --plugin-dir <path to this folder>`.

## How It Works

0. **Defaults:** plans are Socratic (you reach each concept through questions) and sessions are graphic from start to finish: the opening question, both tests and the teaching all run on one interactive page. Add `direct` when creating a plan for direct explanation, and `chat` when running a session for chat text
1. You provide a learning goal and a **target level**: High school, Master's or Advanced (the plugin asks if you do not say)
2. The plugin identifies the domain's **core principles** and **key facts**, records the topic's **breakthrough** (what the situation was before the key intuition, and what the topic solved), flags the **hard core** (the principles that are hardest to grasp), and decomposes the goal into testable sub-goals with CTQ mastery criteria, all written for your level. It also writes a plan-level **Motivation & Course Overview (VOC)** — a bird's-eye view of the course, its core principles and key facts, and what you'll be able to do on completion. You can edit this overview, and your feedback on it can restructure the plan. You can also change the hard-core list.
3. For each sub-goal, you run a TTT session:
   - **Test** -- face a practical case immediately (no theory first)
   - **Teach** -- get principle-first concept explanations for your gaps (adaptive: abbreviated for simple gaps, full 7-section with LaTeX, Worked Examples, and CTQ for complex gaps, comparison for conflation, a climb through the levels for hard-core principles, delivered on an interactive page by default)
   - **Test** -- prove mastery with a new case
4. Every explanation pairs a solved example with an exercise you attempt and then see solved in full
5. Each lesson that teaches writes **lesson notes**, and each lesson adds fully solved exercises to its **practice book**
6. Every step is saved in the course -- if interrupted, you resume where you stopped
7. Your progress, strengths and recurring mistakes are computed across all your courses
8. A concept library tracks your learning artifacts across all sessions
9. Every file a course writes is listed in its `course.json` and in the generated `overview.md`

## What Every Plan Includes

Every plan, standard or Socratic, carries five elements, each in a fixed place. Plan creation checks for them after writing the file.

| Element | What it gives the learner | Where it lives in the plan |
|---------|---------------------------|----------------------------|
| **Core principles identification** | The 3-5 foundational truths of the domain, identified before any sub-goal is written | `Principle Extraction`, plus one Core Principle sub-goal per principle |
| **Key facts identification** | What must simply be known (definitions, constants, conventions), each tied to the sub-goals that use it | `Key Facts` |
| **Motivation** | Why the topic matters and where the course leads | `Motivation & Course Overview (VOC)`, plus the Motivation sub-goal |
| **Breakthrough** | What the situation was before the key intuition, and what the topic solved | `Breakthrough` |
| **Test-Teach-Test / Socratic** | How every session runs: motivation and historical context, then test, teach only the gaps, test again, by direct explanation or by Socratic discovery | `Pedagogical Method`, plus the tests in every blueprint |

## Levels and the Hard Core

**Three levels.** A plan is pitched at one target level, fixed when it is created. The goal, every sub-goal and every test are written for it.

| Level | Assumes | Explains with |
|-------|---------|---------------|
| **High school** | School mathematics, no earlier exposure to the topic | Plain words, a picture, concrete numbers |
| **Master's** | The field's standard tools and notation | The formal statement, where it comes from, symbols then numbers |
| **Advanced** | The Master's level, mastered | Full generality: proofs, limits of validity, competing formulations |

**The hard core.** Some principles are much harder to grasp than the rest: they are counter-intuitive, need a new abstraction, or run into a misconception that survives being told. The plan flags them (usually 1-3, and you can change the list) and designs their explanation ahead of the session:

1. **Predict.** The test is built so that the natural approach gives a confident wrong answer.
2. **Reveal.** The explanation starts from that failure: the insight in one sentence, one picture, and the smallest example that shows it.
3. **Climb.** The principle is then taught rung by rung, from High school up to the plan's level. Each rung has a solved exercise and ends with "your turn". A failed rung gets a short bridge one level down, and the session records the level reached.

A learner who passes the test outright gets a short recap and the offer of the full climb or the next level up.

**Graphic delivery (the default).** Every session runs on one interactive page instead of chat text, in three stages: the Discovery Question and Initial Test, the teaching, and the Final Test. The page shows the subject's objects drawn with their real numbers (matrices as coloured grids, an arrow you rotate, a grid of cases), coloured by role, with a check after each explanation that replays the worked solution step by step after a wrong answer. A hard-core principle gets its climb on the page, one tab per level, from the `Visual design` the plan wrote for it. In a Socratic plan the chain of questions runs on the page too, one question at a time on the picture, and the explanation opens only after you have written the idea in your own words. When a plan has a course diagram, every stage is drawn on it. You go through the whole session on the page, one step at a time, without copying anything into chat: your answers are checked where you give them and saved by the page. You can go back to any finished step, open a Contents index, write a note on any step, and open a Manual that the page writes as you go and that you can save as a file. At the end you write `done` in chat and the session is recorded. To learn from chat text instead, add `chat` (`/run-session SG-3 chat`) or ask for chat during the session.

**Fully worked exercises** come four ways: in every explanation; inside the plan, for each hard-core principle; in an exercise book written after each session; and on demand with `/worked-exercises`. Every solution ends with a check that confirms the result a second way.

## Commands

### `/create-training-plan <learning goal> [direct]`

Creates a full training plan at your target level, with sub-goals, session blueprints and CTQ criteria. **The plan is Socratic by default**: each session follows a **Question -> Tension -> Resolution -> Test** arc, a Socratic form of Test-Teach-Test, in which you reach each concept through a short chain of questions before it is explained. Add the word `direct` to get a plan that explains the gaps directly after the first test.

State the level in the goal, or the command asks once. If a learner profile exists, it informs the plan design (harder tests for known strengths, proactive coverage for known weaknesses). An existing plan of the same name is never overwritten without asking.

Example:
```
/create-training-plan Understand quantum measurement for one qubit, at master's level
/create-training-plan I want to learn cost estimation for EPC construction projects, direct
```

### `/socratic-training-plan <learning goal>`

The Socratic plan itself, which `/create-training-plan` hands over to by default. It uses the same goal decomposition as a direct plan (SMART goal, target level, principle extraction, key facts, breakthrough, hard core, 5-axis decomposition, prerequisite graph) with a **Socratic Discovery** layer: blueprints include Discovery Questions, designed "wrong paths," Socratic Guidance Chains (3-6 progressively narrowing questions), and "reconstruct the reasoning" final tests.

Example:
```
/socratic-training-plan Derive quantum mechanics from experimental spectra
```

### `/run-session <sub-goal> [level] [chat]`

Runs an interactive TTT session for one sub-goal. Teaches using concept-builder methodology (Problem, Principles, Innovations, Worked Example, Formalization, CTQ, Conceptual Map), and teaches hard-core principles as a climb through the levels. Saves checkpoints after each phase. On completion it exports a concept file, adds solved exercises to the sub-goal's exercise book, and registers what it wrote in the plan's Artefacts Register. Name a level to run one session at a different level from the plan's without changing the plan. The Teach phase arrives as an interactive page by default; add `chat` to get chat text instead.

Example:
```
/run-session SG-2
/run-session unit-rate estimation
/run-session SG-3 advanced
/run-session SG-3 chat
```

### `/worked-exercises <sub-goal or concept> [level]`

Produces three fresh, fully solved exercises at the level you name (default: the sub-goal's level) and adds them to the exercise book. You see the statements first; the solutions follow when you send an attempt or ask for them.

Example:
```
/worked-exercises SG-3
/worked-exercises change of basis advanced
```

### `/training-status`

Shows your cross-plan learning analytics: completion rates, strengths, recurring gap patterns, and recommendations for what to study next.

### `/concept-library [list|search|path|link]`

Manage concept files generated during sessions: browse your library, search by keyword, build learning paths between concepts, or link related concept files.

Example:
```
/concept-library list
/concept-library search "indirect costs"
/concept-library path "cost classification" "earned value"
```

### `/user-testing <learning goal>` or `/user-testing inspect`

A developer tool. It creates a plan, simulates a learner through the sessions and checks every artefact against the plugin's own rules, or inspects the files already in the folder.

## Accessory Skill: Technical Training Manual

`technical-training-manual` writes a step-by-step technical training manual as a PDF, on any technical subject, in US corporate-manual style. The manual gives an explanation before and a worked example after every formula, rule or step. It also includes numbered procedures, NOTE and CAUTION callouts, a troubleshooting table, a quick-reference card and a glossary.

The skill works on its own: ask Claude for a manual, a training document or a technical note. It is not part of the Test-Teach-Test flow, but it pairs well with it, for example to turn a finished course into a printable manual.

Building the PDF needs Node.js (KaTeX, Playwright and pdf-lib), a Chromium browser, the Inter fonts and `pdftotext`. Section 7 of the skill gives the details.

## Architecture

- **3 agents**: `training-planner` (orchestrator), `term-clarifier` (defines a term during a test without leaking the answer), `user-testing` (QA)
- **9 skills**: `course-model` (the course data file: schema, rules, glossary, conversion of old plans), `goal-decomposer`, `ttt-session`, `content-builder`, `concept-explainer`, `visual-explainer` (the interactive page that delivers the Teach phase), `concept-map`, `learner-analytics`, and the accessory skill `technical-training-manual`
- **7 commands**: `/create-training-plan`, `/socratic-training-plan`, `/run-session`, `/worked-exercises`, `/training-status`, `/concept-library`, `/user-testing`

## Output Files

Each course lives in its own folder. One file, `course.json`, holds the whole course: its design, the state of every lesson, the list of files and the history. Everything else is generated from it or listed in it, so no fact is stored twice. The format is defined by the `course-model` skill (`skills/course-model/`: schema, rules, glossary and a helper tool).

```
<course-id>/
  course.json            the only source of truth
  overview.md            generated outline for reading (never shows tests or solutions)
  lessons/
    03-soft-lookup/
      notes.md           lesson notes, when the lesson taught something
      practice.md        practice book: fully solved exercises, added to over time
      page.html          the lesson page, when the lesson was taught on a page
```

There are no checkpoint files (an interrupted lesson's saved place is in `course.json`), no transcripts (every answer is kept in the lesson's attempts; a readable record is written on request), no separate register and no learner profile (`/training-status` computes progress from all courses).

**Plans from version 3.4 and earlier** (`<topic>_training_plan.md` and its files) are converted the first time a command finds them: the course folder is created beside the plan, the plan's transcripts, concept files, exercise books and pages are copied into it, and the old files are left untouched. `python3 skills/course-model/tools/course.py convert <plan>.md` does the same by hand.

## Concept-Builder Methodology

The Teach phase uses a principle-first approach adapted from the concept-builder methodology:

1. **The Problem** -- why the gap matters (framed in learner's context)
2. **Core Principles** -- foundational truths (with LaTeX at the Master's level and above)
3. **Key Innovations** -- breakthroughs and techniques
3.5. **Worked Example** -- fully developed step-by-step example with every intermediate step shown and annotated, ending with a check of the result (always included)
4. **Intuitive Formalization** -- minimum math needed for prediction
5. **CTQ Mapping** -- mastery criteria with failure mode awareness
6. **Conceptual Map** -- visual structure of learned concepts

Teaching is **adaptive**: simple gaps get abbreviated treatment (Problem + Principles + Worked Example + Quick Check), complex gaps get the full 7-section explanation, conflation gaps get a side-by-side comparison, and a gap on a hard-core principle gets the climb through the levels. After every Quick Check the learner sees the complete worked solution. A failed Quick Check is re-explained one level down.

During a session, learners can request a **deep-dive** into any taught principle for a full expanded explanation.

## Plans From Earlier Versions

Plans created before version 3.0 still run. Sessions read their depth names (introductory / intermediate / advanced) as High school / Master's / Advanced, and a plan without hard-core blueprints is taught as before. Such plans lack the newer sections (method, breakthrough, hard core, key facts), which `/user-testing inspect` reports as missing. A hard-core blueprint written before version 3.2 has no `Visual design`; the session designs the page from the blueprint's Picture and solved exercises.

## Learning Science

See [PRINCIPLES.md](PRINCIPLES.md) for the cognitive science behind TTT, how this plugin addresses common learning risks (testing effect, desirable difficulty, fluency illusion, metacognitive blindness), and the reasons behind what every plan contains and how the hard core is taught.
