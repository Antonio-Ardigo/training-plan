---
name: course
description: Open your course app - the page with your course map and lessons - building or rebuilding it, bringing in what you did there, and preparing the next lessons.
argument-hint: [course folder]
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Skill
  - Bash(python3:*)
---

The learner asked for their course app: **$ARGUMENTS**

1. Find the course as the **course-model** skill says (section 6), converting a version 3 plan if that is all there is.
2. If `course.app_url` is set, bring in the learner's work first (**course-app** skill, section 4).
3. Make sure the next two lessons the learner can take are prepared (**lesson-content** skill), then build and publish the app (**course-app** skill, sections 2 and 3).
4. Give the link, say which lessons are ready, and say that `/continue` in chat brings their work back and prepares more.
