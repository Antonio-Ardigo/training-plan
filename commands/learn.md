---
name: learn
description: Create a course for a learning goal. Socratic by default (you reach each idea through questions); add "direct" for direct explanation. Name a level (high school, master's, advanced) or you will be asked once.
argument-hint: <goal> [high school | master's | advanced] [direct]
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Skill
  - Bash(python3:*)
---

The learner wants to learn: **$ARGUMENTS**

Design and write the course by following the **course-design** skill from start to end (load it with the Skill tool, `training-plan:course-design`, or Read `**/skills/course-design/SKILL.md`). It uses the **course-model** skill for the file and the **progress** skill for what the learner already knows.

- The method is Socratic unless the goal contains the word `direct` or the learner asks for direct explanation.
- The level is the one named in the goal; otherwise ask once (High school, Master's or Advanced). In a run where you cannot ask, use Master's and say so.
- Never overwrite an existing course without asking.

End with the summary the course-design skill describes and the next step: `/continue` starts Lesson 1.
