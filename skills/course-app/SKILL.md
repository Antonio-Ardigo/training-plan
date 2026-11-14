---
name: course-app
description: The course app - one interactive page per course that shows the course map and runs the prepared lessons step by step, marks answers by asking Claude from the page, and saves every answer - with how to build it, publish it, and bring what the learner did back into course.json. Use when /learn or /continue delivers lessons on a page (the default), when /course is run, and whenever the learner has used the app since the last sync.
---

# Course App

The learner's interface is **one page per course**. It shows the course (map, progress, the story) and runs each **prepared** lesson one step per screen: Open, Try first, Learn, Checks, Show you've got it, then a clear **Next lesson**. `course.json` stays the only source of truth: the page reads a copy of it, saves the learner's answers in its own store, and Claude brings those answers back into `course.json` at the next `/continue`.

| Part | Where |
|---|---|
| The page template | `app.html` in this folder (renderer, widgets, marking, saving) |
| Prepared lessons | `lessons/<NN-slug>/lesson.json`, format in the **lesson-content** skill |
| The built page | `app/index.html` (to publish) and `app/local.html` (to open in a browser), made by `course.py build-app` |
| The learner's answers | The page's store (collection `activity`, one document per event; collection `place`, the saved place per lesson), and the browser's own storage as a fallback |

## 1. What the page does

- **Home:** course title, level and method, lessons done, the lesson list (status, key ideas ★, what each needs), a large button for the next lesson, why it matters and the story. A lesson that is not prepared says: type `/continue` in chat.
- **A lesson:** the steps of `lesson.json` in order, with Back and Next, a progress bar and the saved place. Try first and Show you've got it have one answer box per part, the two notes, and (Try first only) **Start from scratch**.
- **Marking.** Checks and Your turn are marked by the page itself from `answer`, `tolerance` and `wrong`; a wrong answer shows what it reveals and replays the solution step by step, then allows one more try. Try first, guiding questions and Show you've got it are marked by **Claude from the page** (`sample` capability), with the marking guide read from the course data and never shown. Try first's feedback never gives the answer, because teaching follows; the verdict chooses the path (`learn.passed` after a pass, `learn.not_passed` otherwise).
- **Without marking by Claude** (the learner declined, or the page is opened outside claude.ai): every answer is saved as `unmarked`, the lesson goes on to the teaching, and the answers are marked in chat at the next `/continue`.
- **Show you've got it failed:** the page does not repeat the test. It records `final-failed` and sends the learner to `/continue`, which runs another round with a new case (lesson-flow 2.6).
- **Events saved:** `lesson-start`; `answer` (step, level, question, answer, verdict, feedback, what to work on); `lesson-end` (status, level reached) after a passed Show you've got it; `final-failed`.

## 2. Build

1. Prepare the lessons that are due (lesson-content section 5): at least the next two lessons the learner can take. Check each with `python3 <course-model>/tools/course.py check-lesson <file>`.
2. Run `python3 <course-model>/tools/course.py build-app <course>/course.json`. It embeds `course.json` and every prepared lesson into a copy of `app.html`, writes `app/index.html` and `app/local.html`, and lists both in `files` (kind `app`).
3. Validate `course.json` and regenerate `overview.md` (course-model section 3).

## 3. Publish

When a tool that publishes pages is available (on claude.ai: the Artifact tool):
- Publish `app/index.html` with the capabilities `{"db": {}, "sample": {}, "user": {}}` and a one-word icon such as `book` the first time; later, publish the same file to the same link without restating capabilities. A page whose capabilities are declared gets one functional check after its first publish: one read of the `activity` collection.
- Save the link in `course.app_url`, regenerate `overview.md`, and give the learner the link with two lines: what is prepared, and that `/continue` in chat brings their work back and prepares more.
- The page and its store are private to the learner unless they share it.

Without a publishing tool: tell the learner to open `app/local.html` in a browser. Their answers stay in that browser; marking by Claude is not available there, so the lessons run in chat (`/continue` delivers them in chat) and the local page is for reading and the widgets.

## 4. Sync: bring the learner's work into `course.json`

Do this at the start of every `/continue` and `/progress` when `course.app_url` is set:
1. Read the page's `activity` collection (on claude.ai: the `ArtifactData` tool, action `list` with the artifact's url, `query.limit` 1000, and `out_dir` to save the documents as files when there are many) and write the documents, as one JSON list, to a temporary file. Either shape works: the events themselves, or the `{id, data, version}` records the read returns.
2. Run `python3 <course-model>/tools/course.py merge-activity <course>/course.json <file>`. It appends every new answer to its lesson's `attempts` (once: the event id is kept), adds what to work on, starts and closes lessons, sets the level reached, and regenerates `overview.md`. Running it twice changes nothing.
3. It reports `unmarked` answers: mark each now, as lesson-flow section 3 says, and write the verdict into that attempt. It reports `closed` lessons: write their lesson notes and practice book (lesson-flow, Close) if the app did not.
4. A lesson the app left `in-progress` with `step: learn` after `final-failed` continues in chat or on the page with another round.

## 5. Rules

- `course.json` is the truth. The page's store is an inbox: never read the learner's progress from anywhere else.
- Never put a marking guide, a pass standard or a trap on screen. They live in the embedded course data and are only sent to Claude for marking.
- Rebuild and republish after any change to `course.json` or to a prepared lesson, so the page never shows an old course.
