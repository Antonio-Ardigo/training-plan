---
name: training-status
description: Show learning progress across all courses -- completion, strengths, recurring mistakes and what to do next
allowed_tools:
  - Read
  - Glob
  - Bash(python3:*)
---

You are generating a learning analytics summary across the learner's courses.

## Step 1: Compute Progress

Progress is not stored: it is computed from every course, as the **course-model** skill (Glob `**/skills/course-model/SKILL.md`, section 5) describes. When `python3` is available, run `python3 <path>/course.py progress .` and use its output. Otherwise read every `*/course.json` below the current directory and count the same things by hand.

A 3.x plan (`*_training_plan.md`) with no course yet is converted first (course-model skill, section 7), so that it counts. If there is no course at all, tell the user: "No course found. Create one with /create-training-plan."

## Step 2: Read Each Course

For each course, from `course.json`: lessons done of total and in review; key ideas done; the last activity (latest `finished` date or `history` entry); the next lesson; each lesson's `state.attempts` (Try first verdicts, rounds) and `state.to_work_on` (kinds of common mistake).

## Step 3: Generate the Report

Present the analytics summary in this format:

```markdown
# Training Status

## Overview
- Courses: <N> (<N complete>, <N in progress>)
- Lessons: <done>/<total> (<percentage>%)
- Lessons done: <N>
- Average extra rounds per lesson: <N>
- Strength ratio: <N>% (passed Try first with nothing to work on)

## Courses

| Course | Status | Progress | Last activity |
|------|--------|----------|-------------|
| <name> | <in-progress/complete> | <N/M> (<pct>%) | <date> |

## Strengths (passed Try first with nothing to work on)

| Topic | Lesson | Course | Date |
|-------|----------|------|------|
| ... | ... | ... | ... |

<If no strengths: "No topics mastered on first attempt yet.">

## Recurring mistakes

| Kind of mistake | Occurrences | Persistence | Courses |
|---------|-------------|-------------|-------|
| <pattern> | <N> | <persistent/occasional> | <list> |

<If no patterns: "No recurring gap patterns detected yet.">
<Mark patterns with 3+ occurrences as "persistent">

## Recommendations

<Based on the data, provide 2-3 actionable recommendations:
- Which lesson to take next (the course's next lesson)
- Which gap patterns to address proactively
- Whether to revisit any lesson in review>
```

## Step 4: Present to User

Display the report inline (do NOT save it to a file -- it is a live view, not an artifact). Offer the user to:
- Run `/run-session <N>` for the recommended next lesson
- Re-run a lesson in review
