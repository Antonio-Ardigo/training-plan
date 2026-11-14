---
name: test-course
description: Developer tool - create a course, play a learner through it and write a test report; or "inspect" to check the courses already in this folder.
argument-hint: <goal> | inspect
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Skill
  - Bash(python3:*)
---

Run the plugin test for: **$ARGUMENTS**

Use the **course-tester** agent and follow its instructions exactly: `inspect` (or `inspect-only`) checks the courses already in this folder; anything else is a goal for a full test. The report is written to `test-report_<course-id>_<date>.md`.
