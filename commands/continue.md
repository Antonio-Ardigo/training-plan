---
name: continue
description: Run the next lesson of your course, pick up an interrupted one where you stopped, or run the lesson you name. Lessons are taught on a page by default; add "chat" for chat.
argument-hint: [lesson number] [level] [chat]
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Skill
  - Bash(python3:*)
---

The learner asked for: **$ARGUMENTS**

Run the lesson by following the **lesson-flow** skill from start to end (load it with the Skill tool, `training-plan:lesson-flow`, or Read `**/skills/lesson-flow/SKILL.md`). It finds the course (converting a plan from version 3 if that is all there is), chooses the lesson, saves every step in `course.json` as the **course-model** skill says, and uses the **explaining**, **visual-explainer** skills and the **term-helper** agent where it says so.

- If the course has an app (`course.app_url`), lesson-flow first brings in what the learner did there, then keeps the next two lessons prepared and republishes the app (**course-app** and **lesson-content** skills); the learner continues on the app's link.
- No lesson named: the next lesson (an interrupted lesson first).
- A number: that lesson. A level name (High school, Master's, Advanced): this lesson at that level, without changing the course.
- `chat`: teach in chat instead of on a page.
