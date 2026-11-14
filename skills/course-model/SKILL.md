---
name: course-model
description: The data model of a course - course.json, the only place where a course's design and state live - with its folder layout, rules, the plain-word glossary, conversion of 3.x training plans, and the derived views (overview.md, next lesson, progress). Use whenever a command creates, reads or changes a course, records a lesson, adds a file, reports progress, or finds an old *_training_plan.md.
---

# Course Model

A **course** is one learning goal, taught in numbered **lessons**. Everything about it lives in one file, `course.json`. Every other file is either generated from it or listed in it. Nothing is stored twice.

The schema is `course.schema.json` in this skill's folder. It is authoritative for field names and allowed values. This file gives the rules the schema cannot express. The words the learner sees are in `glossary.md`.

## 1. Folder layout

One folder per course, named after the course id, inside the folder where the learner works:

```
<course-id>/
  course.json            the only source of truth
  overview.md            generated outline for reading; never edited by hand
  lessons/
    03-soft-lookup/      <number, two digits>-<title as a slug>
      notes.md           lesson notes, written when a lesson teaches something
      practice.md        practice book: fully solved exercises, appended to
      page.html          the lesson page, when a lesson was taught on a page
      record.md          a readable lesson record, written only on request
  app/index.html         the course app (from version 4.1)
```

- The course id is a lowercase slug of the topic (`transformer-attention`). Every path in `course.json` is relative to the course folder.
- A file in the folder that is not in `files` is not part of the course. A file in `files` must exist.
- There are no checkpoint files, no progress log, no file register and no learner profile file. Their content is in `course.json` (`state`, `history`, `files`) or is computed (progress).

## 2. The helper tool

`tools/course.py` (Python 3, standard library only) does the exact work. Use it whenever `python3` is available; find it with Glob (`**/course-model/tools/course.py`).

| Command | Does |
|---|---|
| `python3 course.py validate <course>/course.json --files` | Checks the schema and every rule in section 4. Run it after every change |
| `python3 course.py render-overview <course>/course.json` | Rewrites `overview.md` |
| `python3 course.py next-lesson <course>/course.json` | The lesson to do next: resume, next, review, or course complete |
| `python3 course.py progress [folder]` | Report over every course found below the folder |
| `python3 course.py convert <plan>.md` | Converts a 3.x plan into a course folder, copying its files |

Without Python, do the same work by hand, following this file and the schema exactly.

## 3. Writing `course.json`

- **Read before you write.** Read the whole file, change only the fields the step owns, write the whole file back as UTF-8 JSON with two-space indentation. Never keep a second copy of a field anywhere else.
- **After every write:** validate, then regenerate `overview.md`. A failed validation is fixed before anything else happens.
- **Dates** are `YYYY-MM-DD`. Every change a learner would care about adds one line to `history` (`Lesson 3 done`, `Course created`, `Lesson 2 converted from 3.x`).
- **Text** is Markdown. Mathematics uses `$...$` and `$$...$$`.
- **Answers stay hidden.** `overview.md` and anything else shown before a lesson never contains `try_first`, `final_check`, marking guides, worked examples, levels or the trap. The overview generator leaves them out by construction.

### Who writes which part

| Part | Written when | Written by |
|---|---|---|
| `course`, `overview`, `story`, `principles`, `facts`, `background`, every lesson's `design` | The course is designed | the course-creation command |
| `overview.learner_notes`, design changes the learner asks for | The learner edits the course | the command handling the request, then the re-check of the design rules |
| a lesson's `state` | Each step of a lesson | the session command, at each step |
| `files` | A file is written or removed | whoever writes the file, in the same change |
| `history` | Any of the above | whoever made the change |

### Lesson state, step by step

`state.status` is `not-started`, `in-progress`, `done` or `review`. While a lesson is in progress, `state.step` is the saved place, and `state.saved` holds whatever is needed to resume (blocks taught so far, the level being climbed, a check waiting for an answer). This replaces checkpoint files.

| Moment | Write |
|---|---|
| The lesson starts | `status: in-progress`, `step: try-first`, `started`, `delivery` |
| An answer is judged (Try first, a check, a guiding question, Your turn, Show you've got it) | append to `attempts`: date, step, level (for a Your turn), the question if it is not the design's own, the learner's answer in full, the verdict, one line of feedback, `source` (`chat` or `app`) |
| The evaluation finds what to work on | `to_work_on` entries, with the kind of common mistake where one applies |
| Each move to the next step | `step`, and `saved` with what the next step needs |
| A key idea's levels | `level_reached` as each level is held |
| Another round after a failed final check | `rounds` + 1 (at most 2) |
| The lesson ends | `status: done` or `review`, `step: null`, `saved: null`, `finished`, `to_work_on[].resolved`, `notes` (one or two lines), one `history` line, files written listed in `files` |

`review` means the lesson ended without the final check passed, or a key idea stopped below the course level.

### Files

Add each file to `files` when it is written: `path`, `kind` (`overview`, `lesson-content`, `lesson-page`, `notes`, `practice`, `record`, `app`, `old-plan`, `other`), `lesson`, a plain `title` and `updated`. Update `updated` when it changes. A practice book is one file per lesson and is appended to, never replaced.

## 4. Rules beyond the schema

`validate` checks all of these. Errors must be fixed; warnings are reported to the learner only if they affect them.

- Lessons are numbered 1, 2, 3 in order, with ids `L1`, `L2` ... matching the number. Principles are `P1` ..., facts `F1` ....
- `needs` names existing lessons, never the lesson itself, and never forms a circle.
- Each principle is taught by exactly one lesson of kind `principle`. A key-idea lesson teaches a principle marked `key_idea`.
- A principle lesson has a worked example. Every worked example ends with a `check`: the result confirmed a second way.
- A key-idea lesson has `trap`, `aha`, `picture`, a worked example (the High school level) and exactly one example in `levels` for each level above High school up to the course level: none for a High school course, `masters` for a Master's course, `masters` then `advanced` for an Advanced course. It should have a `visual`. Other lessons have none of these fields.
- In a Socratic course every lesson has a `puzzle` and 3 to 6 `guiding_questions`.
- Every lesson has at least one success criterion. Every fact is used in at least one lesson.
- A lesson that is `done` or `review` has a `finished` date; a key idea that is `done` has `level_reached`.

## 5. Derived views

**Next lesson.** In this order: the lesson in progress (resume it); the first lesson not started whose `needs` are all done; the first lesson in review; the first lesson not started, saying which of its needs are not done; otherwise the course is complete.

**Progress** (replaces the learner profile). Computed on request from every `course.json` below the working folder: per course, lessons done of total, lessons in review, key ideas done, last activity, next lesson; across courses, the kinds of common mistake that recur (two or more lessons), and lessons passed at Try first (strengths). Nothing is stored.

**Overview.** `overview.md` shows the course, level and method, the overview, the story, the principles (key ideas marked ★ with why they are hard), facts to know, background, the lesson list with status and level reached, and the files. It never shows tests or solutions.

## 6. Finding the course

1. If the learner names a course folder or a `course.json`, use it.
2. Otherwise look for `*/course.json` and `course.json` in the working folder. One found: use it. Several: list their titles and ask.
3. None found, but a 3.x plan (`*_training_plan.md`) exists: convert it (section 7), tell the learner in one line, and continue with the new course.

## 7. Converting a 3.x plan

Run `course.py convert <plan>.md`. It creates `<course-id>/` beside the plan, writes `course.json` and `overview.md`, and **copies** the plan's transcripts, concept files, exercise books and pages into the lesson folders. The old plan and its files are never changed or deleted; the course lists the plan as `old-plan`. A plan already converted (a course whose `converted_from` names it) is not converted again.

What each part of a 3.x plan becomes is listed in `convert-3x.md`. Without Python, follow that table by hand.

After converting, validate. Warnings that come from the old format (a key idea without a visual design, a worked example without a Check) are normal: the lesson designs the missing part when it is taught.
