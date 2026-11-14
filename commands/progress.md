---
name: progress
description: Where you stand across all your courses - lessons done, key ideas held, strengths, recurring mistakes, and what to do next. Add "notes" (and words to search for) to list or search your lesson notes.
argument-hint: [notes [words]]
allowed_tools:
  - Read
  - Glob
  - Grep
  - Skill
  - Bash(python3:*)
---

Show the learner's progress by following the **progress** skill (load it with the Skill tool, `training-plan:progress`, or Read `**/skills/progress/SKILL.md`): compute it from every `course.json` in the current folder and below, and show the report it describes. If the input starts with `notes`, list or search the lesson notes instead (progress skill, section 3). Nothing is saved.

The learner asked for: **$ARGUMENTS**

If there is no course yet, say so and suggest `/learn <goal>`.
