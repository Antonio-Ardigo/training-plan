# Training Plan Plugin

Learn any subject, including hard ones (mathematics, physics, machine learning, engineering, finance), through a **course** of short lessons. Each lesson asks you to **try first**, teaches only what your attempt showed you need, and asks you to **show you've got it** on a new case. The hardest ideas of a subject, its **key ideas** ★, are taught through an aha moment and then level by level, with fully worked examples.

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

Installed this way, each command carries the plugin's name: `/training-plan:learn`, `/training-plan:continue`, and so on. The commands below are written in their short form.

To try the plugin from a local copy without installing it, start Claude Code with `claude --plugin-dir <path to this folder>`.

## Commands

| Command | Does |
|---|---|
| `/learn <goal> [level] [direct]` | Designs a course for your goal and writes it to a folder |
| `/continue [lesson] [level] [chat]` | Runs your next lesson, picks up an interrupted one where you stopped, or runs the lesson you name |
| `/practice <lesson or idea> [level]` | Three fresh, fully solved exercises, added to the lesson's practice book |
| `/progress [notes [words]]` | Where you stand across all your courses, or a list or search of your lesson notes |
| `/course` | Opens your course app, rebuilding it with the next lessons prepared |

Examples:

```
/learn Understand quantum measurement for one qubit, at master's level
/learn Cost estimation for EPC construction projects, high school, direct
/continue
/continue 6 advanced
/practice 3
/progress notes softmax
```

## How a course works

**Designing the course** (`/learn`)
1. Your goal is refined to at most 15 words, and the course gets one **level**: High school, Master's or Advanced. Say it in the goal, or you are asked once.
2. The course finds the subject's 3 to 5 **principles**, the **facts to know**, and **the story**: how things were before the key idea, the aha, and what it solved.
3. It writes the **lessons** in order: why it matters, one lesson per principle, concepts, tools, and a capstone. Each lesson knows which lessons it **needs** first.
4. It marks the hardest principles as **key ideas** ★ (usually one to three) and designs their teaching ahead: **the trap** (the confident wrong answer), **the aha** (the sentence that makes it click), a **picture**, and a solved example for each level.
5. It writes the **course overview** for you to read and edit. Your feedback can reshape the course.

**The method.** By default a course is **Socratic**: guiding questions lead you to state each idea yourself before it is confirmed. Add `direct` to the goal for a course that explains directly after Try first.

**Running a lesson** (`/continue`)

| Step | What happens |
|---|---|
| Open | Why the lesson matters and the real story behind it. No answer is given away |
| Try first | A real case, before any teaching. You can choose **Start from scratch**, or ask **What does this word mean?** |
| Learn | Only what your attempt showed you need, one item at a time, each followed by a **check**. A key idea starts with the aha moment and goes **level by level**, with a **Your turn** at each level and a **step back** if the method goes wrong |
| Show you've got it | A new case. If it does not pass, **another round** on what is still missing (at most two) |
| Close | The lesson is saved as done or for review, with your **lesson notes** and a **practice book** of solved exercises |

**The course app.** On claude.ai each course gets one interactive page: the course map with a **Continue** button, and each lesson one step per screen, with the subject's objects drawn from their real numbers (matrices, arrows, dots, bars, growth curves, tables, timelines, sliders). Your answers are marked on the page: checks by the page itself, with the worked solution replayed step by step after a wrong answer; Try first, guiding questions and Show you've got it by Claude, asked from the page. Every answer is saved. Typing `/continue` in chat brings your work into the course and prepares the next lessons. `/course` opens or rebuilds the app.

Add `chat` to learn in chat instead. Every step is saved as it happens, so an interrupted lesson resumes where you stopped.

**Every worked solution ends with a Check** that confirms the result a second way.

## Where your course lives

Each course has its own folder. One file, `course.json`, holds the whole course: its design, the state of every lesson, every answer you gave, the files and the history. Everything else is generated from it or listed in it, so nothing is stored twice.

```
<course>/
  course.json            the only source of truth
  overview.md            the course outline to read (never shows tests or solutions)
  lessons/
    03-soft-lookup/
      notes.md           lesson notes, when the lesson taught something
      practice.md        practice book: fully solved exercises, added to over time
      lesson.json        the lesson prepared for the course app
      page.html          a single lesson page, when the lesson was taught on one
  app/
    index.html           the course app (published as one page)
    local.html           the same app, to open in a browser
```

Your **progress** (lessons done, key ideas held, strengths, mistakes that recur) is computed from all your courses whenever you ask, so it is never out of date.

## Courses from version 3

Version 3 wrote a Markdown plan (`<topic>_training_plan.md`) with separate session files. The first time a command finds such a plan, it converts it into a course folder beside it, copies its files in, and leaves the old files untouched. The old command names still work for this version and point to the new ones: `/create-training-plan` and `/socratic-training-plan` → `/learn`, `/run-session` → `/continue`, `/worked-exercises` → `/practice`, `/training-status` and `/concept-library` → `/progress`, `/user-testing` → `/test-course`.

## Words used

The plugin uses plain words throughout. The full list, with the older names they replace, is in [`skills/course-model/glossary.md`](skills/course-model/glossary.md).

## Inside the plugin

Every rule lives in exactly one skill. Commands and agents point to skills; they never copy them.

| Skill | Owns |
|---|---|
| `course-model` | The course file: schema, folder layout, saving rules, glossary, conversion of old plans, and the helper tool `tools/course.py` |
| `course-design` | Designing a course from a goal, for both methods |
| `lesson-flow` | Running a lesson from Open to Close, with every variation (Socratic, key idea, start from scratch, page or chat, resuming, another round) |
| `explaining` | How explanations, worked examples, levels, checks, step back, go deeper, idea maps, lesson notes and practice books are written |
| `course-app` | The course app: the page template, building it, publishing it, and bringing your answers back into `course.json` |
| `lesson-content` | The format of a prepared lesson (`lesson.json`) and the widgets the app can draw |
| `visual-explainer` | How a single lesson page is built, when the app is not used |
| `progress` | The progress report and the notes search |
| `technical-training-manual` | Accessory: writes a step-by-step technical training manual as a PDF, in US corporate-manual style |

| Agent | Does |
|---|---|
| `tutor` | Routes any learning request to the skill that owns it |
| `term-helper` | Defines a word during a test without giving the answer away |
| `course-tester` | Developer tool: plays a learner through a course and checks every file (`/test-course`) |

**Checks.** `python3 tests/run_tests.py` validates the example course, converts three version-3 plans and checks the result, and fails if a prompt file uses the old storage or vocabulary. It runs on every pull request.

## Accessory skill: technical training manual

`technical-training-manual` writes a step-by-step technical training manual as a PDF, on any technical subject, in US corporate-manual style, with an explanation before and a worked example after every formula, rule or step, plus numbered procedures, NOTE and CAUTION callouts, a troubleshooting table, a quick-reference card and a glossary. Ask Claude for a manual or a technical note. Building the PDF needs Node.js (KaTeX, Playwright and pdf-lib), a Chromium browser, the Inter fonts and `pdftotext`; section 7 of the skill gives the details.

## Learning science

[PRINCIPLES.md](PRINCIPLES.md) explains the research behind trying first, teaching only what is missing, key ideas and worked examples.
