# Lesson notes

The lesson notes are a lesson's teaching, written down for the learner to keep: `lessons/<NN-slug>/notes.md` in the course folder. lesson-flow says when they are written and lists them in `files` (kind `notes`). This file says what is in them.

## Front matter

```yaml
---
title: "Lesson <N>: <lesson title>"
course: <course id>
lesson: L<N>
kind: <why | principle | concept | tool | capstone | background>
level: <High school | Master's | Advanced>
date: <YYYY-MM-DD>
tags: [<subject>, <topic>, <lesson title as a slug>]
---
```

`level` is the level the lesson was taught at. It differs from the course level only when the learner asked for a different level.

## Contents

In this order:

1. **The lesson.** The goal, the result of Try first in one line, and what to work on, each with its common mistake.
2. **The explanations**, one section per item worked on, in the order taught, each in the format it was delivered in:
   - **Short, full, side by side:** every section of the format (`formats.md`), with its Key terms, its Check and the complete worked solution shown after the learner answered.
   - **Level by level:** the aha moment (as taught: after start from scratch, without the trap and the Try first case), then for each level taught: the idea at that level, its solved example, and each Your turn with its complete worked solution. Note any step back in one or two lines.
   - **Recap only:** none. A recap after passing Try first is not teaching, and no notes are written.
3. **Go deeper**, each in full, under the explanation it came from.
4. **Idea map**, if one was made.
5. **Success criteria**: one table for the lesson, every criterion taught (`SKILL.md` section 7).
6. **Key terms**: one table merging the tables of all explanations, each term once, in order of first use.

## Rules

- A worked example or solved example taken from the lesson design (`design.worked_example`, `design.levels`) is named with its title, its level and its result, and is not copied. Everything written during the lesson, including a solved example for a level above the course level, is written in full.
- The notes never contain Try first, Show you've got it or their marking guides.
- When a lesson is taught again (another round, or the lesson redone later), add a dated section at the end. Never rewrite an earlier section.
- The writing style rules of `SKILL.md` section 9 apply.
