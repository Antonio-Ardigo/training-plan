---
name: progress
description: Report where the learner stands across all their courses - lessons done, key ideas held, strengths, recurring mistakes and what to do next - list or search their lesson notes, and supply that history when a new course is designed. Use for /progress, for "how am I doing", for finding an earlier lesson's notes, and when course-design asks what the learner already knows.
---

# Progress

Progress is **computed, never stored**. Every fact it uses is already in the courses' `course.json` files (course-model skill): lesson status, attempts and verdicts, what to work on with its kind of common mistake, level reached, extra rounds, history. There is no profile file to keep up to date, so the report can never lag behind the courses.

## 1. Compute

For a course with an app (`course.app_url`), first bring in what the learner did there (course-app skill, section 4), so the report includes it.

Run `python3 <course-model folder>/tools/course.py progress <folder>` from the folder the learner works in. It finds every `course.json` up to three folders down and returns:

| Field | Meaning |
|---|---|
| `summary` | courses, courses complete, lessons done of total, average extra rounds per finished lesson, strength ratio (lessons passed at Try first, of lessons finished) |
| `courses[]` | per course: title, level, done / total, in review, key ideas done of total, last activity, next lesson |
| `passed_first_time` | strengths: lessons passed at Try first and done |
| `all_mistakes` | each kind of common mistake, with the lessons where it appeared |
| `recurring_mistakes` | kinds that appeared in two or more lessons |
| `persistent_mistakes` | kinds that appeared in three or more lessons |
| `to_work_on` | every item still on a lesson's list, resolved or not, with its course and lesson |

Without Python, read every `*/course.json` and count the same things by hand. A 3.x plan with no course yet is converted first (course-model section 7), so that it counts.

Two items of `to_work_on` describe the **same weakness** when they name the same missing understanding, even in different words ("confused direct and indirect costs", "put an indirect cost under direct"). When in doubt, keep them apart.

## 2. Report (for `/progress`)

Show it in chat; do not save it to a file.

```markdown
# Your progress

- Courses: <N> (<N> complete) · Lessons: <done>/<total> (<pct>%)
- Strength ratio: <pct>% of finished lessons passed at Try first
- Extra rounds: <average> per finished lesson

## Courses
| Course | Level | Done | Key ideas ★ | Last activity | Next |
|---|---|---|---|---|---|

## Strengths
| Lesson | Course |
(or: "No lesson passed at Try first yet.")

## Recurring mistakes
| Kind of mistake | Lessons | Persistent? |
(three or more lessons: persistent. Or: "No mistake has recurred yet.")

## What to do next
Two or three concrete suggestions: the next lesson of the course in progress; a lesson in review; for a persistent mistake, which lesson to revisit and what to look for.
```

End by offering `/continue` for the suggested lesson, and `/practice <lesson>` for a lesson in review.

## 3. Notes (`/progress notes [words]`)

Every lesson that taught something has lesson notes, `lessons/<NN-slug>/notes.md`, listed in its course's `files` with kind `notes`.

- **No words:** list the notes of every course: course, lesson number and title, date.
- **With words:** search the notes for them (Grep over the course folders) and list the matching lessons with the line that matched. Offer to open one.
- **Two lessons are related** when the learner asks how one idea leads to another: read both notes and the courses' `needs` and principles, and show the path of lessons between them in order. Nothing is written.

## 4. Use it when designing a course

The course-design skill asks for progress before it writes lessons. Pass it:
- **Strengths** related to the new goal: those lessons' Try first can be harder.
- **Recurring mistakes** related to the new goal: add them to the matching lessons' `to_teach`, so they are taught even if Try first does not show them, with a check on each.

If there is no earlier course, say nothing about it.
