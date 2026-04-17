---
name: user-testing
description: Run autonomous QA/UX test of the training-plan plugin -- creates plan, simulates learner sessions, produces compliance and effectiveness report
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

You are running an **autonomous QA/UX test** of the training-plan plugin.

The user wants to test: **$ARGUMENTS**

## Determine Mode

Parse `$ARGUMENTS`:

- If the argument is `inspect` or `inspect-only`: run **Inspect Mode** (Phase 3 only)
- Otherwise: treat the argument as a learning goal and run **Full Test Mode** (Phases 1 + 2 + 3)

---

## Full Test Mode

Execute all three phases sequentially. The user-testing agent's instructions define the complete protocol for each phase.

### Phase 1: Plan Creation

Create a training plan for the provided goal following the EXACT methodology from `/create-training-plan`:

1. Refine to SMART Goal (max 15 words)
2. Check for existing `learner_profile.md`
3. Principle Extraction (3-5 principles)
4. Decompose into sub-goals (4 axes: Motivation, Key Concepts, Tools, Verification)
5. Prerequisite Tracing (requires/rests on/led to)
6. Design Session Blueprints (Initial Test, Pass Criteria, CTQs, Teach Topics, Final Test)
7. Write `<topic>_training_plan.md`

### Phase 2: Learner Simulation

For each sub-goal, simulate a full TTT session playing both system and learner roles.

Assign performance profiles to ensure all code paths are exercised:

- **ZERO-GAP**: Perfect answer, no gaps (tests strength detection)
- **PARTIAL**: 2 gaps with specific failure modes (tests gap classification + targeted teaching)
- **NOT-FAMILIAR**: Learner says "not familiar" (tests full 7-section explanation path)
- **FAIL-LOOP**: 3+ gaps, fails Final Test, Loop 1 succeeds (tests adaptation loop)
- **CLARIFICATION**: Learner asks term clarification (tests safe definition without answer leak)
- **CLEAN-PASS**: Passes directly (tests standard completion)

For each session, write:
- Session transcript (`<topic>_session_SG<N>.md`)
- Update plan file (status, Progress Log)
- Update learner profile (strengths, gaps, history)
- Export concept file if teaching occurred

### Phase 3: Inspection & Report

Read ALL artifacts in the current directory and run the full checklist:

1. **Spec Compliance** -- plan structure, sub-goals table, principle mapping, difficulty derivation, sequencing, prerequisite graph, session blueprints, CTQ taxonomy
2. **Transcript Protocol** -- practical-first, explicit evaluation, gap classification, one-gap-one-teach, format matching, different final test, valid loop count
3. **Adaptive Personalization** -- profile-to-plan adaptation (strengths/gaps influence blueprints), session-to-teaching adaptation (correct format per failure mode)
4. **Effectiveness Metrics** -- per-session learning gain, gap resolution rate, recurring failure modes, loop frequency, strength accumulation
5. **Learner Profile Consistency** -- existence, plans table, strengths, gap patterns, session history
6. **Concept Files** -- frontmatter, naming, session linkage
7. **Cross-Artifact Consistency** -- statuses match transcripts, progress log matches, no orphaned checkpoints

Write the report to `qa-report_<topic>_<date>.md`.

---

## Inspect Mode

Use Glob to find all relevant files:
- `*_training_plan.md`
- `*_session_SG*.md`
- `learner_profile.md`
- `concept-*.md`
- `*_checkpoint_SG*.md`

If no training plan files are found, tell the user there is nothing to inspect.

Otherwise, run Phase 3 (Inspection & Report) on the existing files. Write the report.

---

## After the Report

Present a brief summary to the user:
- Overall compliance percentage
- Critical violations count
- Effectiveness score (gap resolution rate)
- Top 3 recommendations
- Path to the full report file
