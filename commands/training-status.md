---
name: training-status
description: Show cross-plan learning analytics -- completion rates, strengths, gap patterns, and session history
allowed_tools:
  - Read
  - Glob
---

You are generating a learning analytics summary from the learner's profile.

## Step 1: Read the Profile

Use Glob to find `learner_profile.md` in the current directory. If it does not exist, tell the user: "No learner profile found. Complete at least one /run-session to create your profile."

## Step 2: Read All Training Plans

Use Glob to find all `*_training_plan.md` files. Read each one to get current sub-goal statuses (the profile may be slightly behind if the user edited plans manually).

## Step 3: Generate the Report

Present the analytics summary in this format:

```markdown
# Training Status

## Overview
- Plans: <N> (<N complete>, <N in-progress>)
- Sub-goals: <completed>/<total> (<percentage>%)
- Sessions completed: <N>
- Average loops per session: <N>
- Strength ratio: <N>% (passed Initial Test with zero gaps)

## Plans

| Plan | Status | Progress | Last Session |
|------|--------|----------|-------------|
| <name> | <in-progress/complete> | <N/M> (<pct>%) | <date> |

## Strengths (passed Initial Test with zero gaps)

| Topic | Sub-Goal | Plan | Date |
|-------|----------|------|------|
| ... | ... | ... | ... |

<If no strengths: "No topics mastered on first attempt yet.">

## Gap Patterns

| Pattern | Occurrences | Persistence | Plans |
|---------|-------------|-------------|-------|
| <pattern> | <N> | <persistent/occasional> | <list> |

<If no patterns: "No recurring gap patterns detected yet.">
<Mark patterns with 3+ occurrences as "persistent">

## Recommendations

<Based on the data, provide 2-3 actionable recommendations:
- Which sub-goal to tackle next (the next pending one in sequence)
- Which gap patterns to address proactively
- Whether to revisit any "needs-review" sub-goals>
```

## Step 4: Present to User

Display the report inline (do NOT save it to a file -- it is a live view, not an artifact). Offer the user to:
- Run `/run-session SG-<N>` for the recommended next sub-goal
- Re-run a specific "needs-review" session
