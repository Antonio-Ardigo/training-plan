---
name: lesson-content
description: The format of lesson.json - one lesson prepared for the course app - and the catalogue of widgets the app can draw. Use when preparing lessons for the app (/learn and /continue prepare the next two), or when changing what a lesson shows on the page.
---

# Lesson Content

The course app (skill **course-app**) runs lessons that were **prepared** in advance. Each prepared lesson is one file, `lessons/<NN-slug>/lesson.json`, listed in `files` with kind `lesson-content`. It holds what the page shows and asks, step by step. It is written from the lesson's `design` in `course.json` and follows lesson-flow exactly: the app only plays it.

The app draws every number from the values in this file: never write a computed result as text that the widget could compute, and never write a number you have not checked (`python3` where available).

## 1. The file

```json
{
  "schema": "lesson/1",
  "lesson": "L4",
  "prepared": "2026-11-14",
  "open":  [ step, ... ],
  "try_first": { "prompt": "...", "parts": [ part, ... ] },
  "learn": { "not_passed": [ step, ... ], "passed": [ step, ... ] },
  "final": { "prompt": "...", "parts": [ part, ... ] }
}
```

| Part | What it holds | Rule (lesson-flow step) |
|---|---|---|
| `open` | Why it matters, then how we got here, from `design.context`; one `text` step each, a widget where it helps (a timeline, a before and after) | Open. No answer given away |
| `try_first` | The lesson's `design.try_first.question` (and the puzzle first, in a Socratic course), split into parts the learner answers | Try first. The two notes are added by the app |
| `learn.not_passed` | What is taught after a trap, a fail, a partial or Start from scratch: in a Socratic course the guiding questions; for a key idea the aha moment and each level with its worked example and Your turn; otherwise the explanation of each success criterion in the format explaining chooses, with its check | Learn and Checks |
| `learn.passed` | The short recap after a pass: the aha in one sentence, the picture, one worked example | Passed Try first |
| `final` | `design.final_check.question`, in parts; a Socratic course adds an "explain it back" part | Show you've got it |

The marking guides stay in `course.json`: the app reads them from there and sends them, with the learner's answer, to Claude for marking. They are never shown on screen.

## 2. Steps

One step is one screen. Every step may carry `"widgets": [ widget, ... ]`, drawn above its text.

| `kind` | Fields | The app |
|---|---|---|
| `text` | `title`, `md`, `level` (optional: `high-school`, `masters`, `advanced`) | Shows the text and widgets. A `level` tag shows as "Level: Master's" |
| `worked` | `title`, `example` (a worked example: `given`, `steps[{do, why}]`, `result`, `check`), `level` | Shows Given, then one step at a time on "Next step", then Result and Check |
| `guiding` | `prompt`, `aim` (what the answer should reach; never shown before the answer), `hint` | Socratic guiding question: the learner answers, Claude says whether it moves toward the aim, a hint after a wrong turn, never the answer itself |
| `check` | `prompt`, `answer` (number or text), `tolerance` (numbers), `choices` (optional list), `wrong` (`[{value, says}]`: likely wrong answers and what each reveals), `solution` (a worked example), `level`, `your_turn` (true at a key idea's level) | Marked on the page: right shows the full solution; a listed wrong answer shows what it reveals; any wrong answer replays the solution step by step (the step back) and allows one more try |

Text is Markdown: paragraphs, `**bold**`, `*italic*`, lists with `- `, inline code, and mathematics between `$...$` or `$$...$$`.

## 3. Parts of a test

```json
{ "id": "a", "ask": "How many euros of interest are added at the end of year 3? (a number)", "form": "number" }
```

`form` is `number`, `text` (a sentence or two) or `choice` (with `choices`). Each part asks one thing and says what form the answer takes (course-design, test quality).

## 4. Widgets

Every widget has `type` and may have `title` and `note`. Colours follow **roles**: `a`, `b`, `c` (at most three, as `design.visual.colour_roles` assigns them) and `neutral`. Values show a diverging blue to orange scale where a widget shades cells.

| `type` | Fields | Draws |
|---|---|---|
| `matrix` | `rows` (numbers), `role`, `row_labels`, `col_labels`, `highlight` (`[[r,c],...]`) | A grid of cells shaded by value, numbers printed; tapping a cell shows its row and column |
| `vectors` | `vectors` (`[{x, y, label, role}]`), `shadow` (`{of, on}`: indexes; draws the projection), `range` (`[xmin, xmax, ymin, ymax]`) | Arrows from the origin on a grid, with labels; the shadow drawn as a dashed drop line and a coloured segment |
| `dots` | `groups` (`[{count, label, role}]`), `cols` | One dot per case, coloured by group, with counts |
| `bars` | `items` (`[{label, value, role}]`), `unit` | Horizontal bars to scale, values printed |
| `lines` | `series` (`[{label, role, values}]`), `x` (labels or numbers), `x_label`, `y_label` | A line chart to scale, one line per series, the last value marked |
| `table` | `head`, `rows`, `highlight` (`[[r,c],...]`) | A table; highlighted cells outlined |
| `timeline` | `events` (`[{when, what}]`) | Events in order on a line |
| `slider` | `label`, `min`, `max`, `step`, `value`, `drives` | One control. `drives` is one object or a list: `{"widget": 0, "target": "series.0.values", "length": 6, "expr": "1000*Math.pow(1+v/100,i)"}`. `widget` is the index of a widget in the same step, `target` the path of the values it replaces, `expr` an arithmetic expression in `v` (the slider value) and `i` (the position, 0 to length − 1) |

Use the widget that fits the field (visual-explainer, section 5): matrices for linear algebra and machine learning, vectors for geometry and quantum states, dots for probability, lines and bars for growth and finance, tables for cost and planning, a timeline for history and procedures.

## 5. Preparing lessons

- `/learn` prepares Lessons 1 and 2; `/continue` keeps two lessons prepared ahead of the learner. A lesson is prepared once; re-prepare it only when its design changes.
- Write `lesson.json`, list it in `files`, then rebuild the app (course-app skill). Check each number in a widget, a check's `answer` and every worked example by computing it.
- `python3 <course-model>/tools/course.py check-lesson <course>/lessons/<NN-slug>/lesson.json` checks the shape of the file.
