---
name: practice
description: Three fresh, fully solved exercises for a lesson or an idea, at the level you choose, added to the lesson's practice book.
argument-hint: <lesson number or idea> [high school | master's | advanced]
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Skill
  - Bash(python3:*)
---

The learner asked for practice on: **$ARGUMENTS**

## 1. What, and at which level

- **A lesson** (a number, or words that match a lesson's title or goal): work from that lesson's design in `course.json` (its principles, success criteria, worked example). Find the course as the **course-model** skill says (section 6).
- **An idea that matches no lesson, or no course**: work from the idea as stated.
- **Level**: the one named, otherwise the course level, otherwise Master's.
- Too vague to choose an idea: ask what the exercises should be about.

## 2. Before showing solutions

If the lesson is **not started**, say so first: these exercises come with full solutions, and reading them makes the lesson's Try first less telling. Offer to run the lesson first with `/continue <N>`. Go on only if the learner still wants the exercises.

## 3. Write the set

Write an **on-request set of three** as the **explaining** skill's practice-book rules describe: graded from standard to demanding, each with a complete worked solution ending with a Check, none repeating a test, a worked example of the lesson design or an exercise already in the book, pitched at the chosen level. Mark any value you are not sure of `(verify)`.

## 4. Save

- **With a lesson:** append the set to `lessons/<NN-slug>/practice.md` in the course folder (never overwrite earlier sets), list it in `files` (kind `practice`) or update its date, add a `history` line, validate `course.json` and regenerate `overview.md` (course-model section 3). Do not change the lesson's status.
- **Without a course:** write `practice-<idea-slug>.md` in the current folder, appending if it exists.

## 5. Show

Show the three statements only, say where the file is, and offer two ways on: the learner sends an attempt and you check it against the worked solution, then show that solution in full; or the learner asks for the solutions and you show them in full. Never show a solution in the same message as its exercise.
