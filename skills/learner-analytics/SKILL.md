---
description: "Learner profile management and cross-plan analytics. Use when updating the learner profile after a session, reading the profile to inform plan creation, generating training status reports, analyzing gap patterns, identifying learner strengths, or computing completion statistics across multiple training plans."
---

# Learner Analytics -- Domain Knowledge

Reference knowledge for managing the persistent learner profile and generating cross-plan analytics.

## Purpose

Maintain a `learner_profile.md` file that tracks the learner's progress across ALL training plans and sessions. This enables:

1. **Informed plan creation**: Known strengths get harder initial tests; known weaknesses get extra attention in teach phase planning
2. **Cross-plan pattern detection**: Recurring gaps are surfaced so the learner can address root causes
3. **Progress visibility**: Completion rates and history at a glance

## Profile File Location

`learner_profile.md` in the current working directory (same directory as training plans). This is a user artifact, not a plugin file.

## Profile Format

```markdown
# Learner Profile
Last updated: <date>

## Plans

| Plan | Topic | Created | Sub-Goals | Completed | Completion % |
|------|-------|---------|-----------|-----------|-------------|
| cost-estimation_training_plan.md | Cost Estimation | 2026-03-01 | 8 | 5 | 62% |
| python-data_training_plan.md | Python Data Analysis | 2026-03-02 | 6 | 6 | 100% |

## Strengths

Topics where the learner PASSED the Initial Test with zero gaps.

| Topic | Sub-Goal | Plan | Date |
|-------|----------|------|------|
| Unit conversion | SG-4 | cost-estimation | 2026-03-01 |
| Pandas basics | SG-2 | python-data | 2026-03-02 |

## Gap Patterns

Recurring weaknesses across multiple sessions or plans.

| Pattern | Occurrences | Plans Affected | Last Seen |
|---------|-------------|----------------|-----------|
| Confuses indirect costs with contingency | 3 | cost-estimation | 2026-03-01 |
| Off-by-one errors in indexing | 2 | python-data | 2026-03-02 |

## Session History

### 2026-03-01 -- cost-estimation SG-1
- Result: complete
- Initial Test: PARTIAL (2 gaps)
- Gaps: confused direct/indirect costs, missed contingency category
- Loops: 1
- Concept Map: no

### 2026-03-01 -- cost-estimation SG-2
- Result: complete
- Initial Test: PASS (0 gaps)
- Gaps: none
- Loops: 0
- Concept Map: no
```

## Update Rules

### After each /run-session RECORD phase:

1. **Read** `learner_profile.md` (create it if it does not exist, using the format above with empty tables)
2. **Update the Plans table**:
   - If this plan already has a row, update Completed count and Completion %
   - If this is the first session for a plan, add a new row
3. **Update Strengths**:
   - If the learner PASSED the Initial Test with zero gaps, add the topic to Strengths
   - Only add if not already listed
4. **Update Gap Patterns**:
   - For each gap identified in this session, check if a similar gap appears in existing patterns
   - "Similar" means the same conceptual deficit, even if worded differently (e.g., "confused direct/indirect costs" and "misclassified indirect costs as direct" are the same pattern)
   - If similar pattern exists: increment Occurrences, update Last Seen, add plan to Plans Affected if not already there
   - If new pattern: add a new row with Occurrences = 1
   - When in doubt about similarity, create a new pattern entry rather than merging
5. **Add a Session History entry** with date, plan, sub-goal, result, initial test result, gaps, loops, and concept map flag

### During /create-training-plan:

1. **Read** `learner_profile.md` if it exists
2. **Check Strengths** for topics related to the new goal
3. **Check Gap Patterns** for recurring weaknesses related to the new goal
4. **Inform the decomposition**:
   - For known strengths: note in the session blueprint that the Initial Test can be set at elevated difficulty
   - For known weaknesses: note in the Teach Topics that these areas need proactive coverage (include a Quick Check even if the learner does not fail on them in the Initial Test)
5. If no profile exists, proceed normally -- the profile will be created after the first /run-session

## Pattern Detection Heuristics

A gap becomes a "pattern" when:
- It appears in 2+ sessions (even within the same plan)
- OR it appears across 2+ different plans

When presenting patterns in /training-status:
- Sort by Occurrences (descending)
- Highlight patterns with 3+ occurrences as "persistent"
- Suggest remedial actions for persistent patterns

## Analytics Computations

For /training-status reports:

- **Overall completion %**: total completed sub-goals / total sub-goals across all plans
- **Plan completion %**: per-plan completed / total
- **Strength ratio**: sub-goals passed on initial test / total sub-goals attempted
- **Average loops**: mean adaptation loops per session
- **Gap persistence**: % of gaps that recur across sessions
