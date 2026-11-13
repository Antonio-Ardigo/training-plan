---
name: worked-exercises
description: Get a fresh set of fully solved exercises for a sub-goal or concept, at High school, Master's or Advanced level
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are producing a set of **fully solved exercises** for practice.

The user asked for: **$ARGUMENTS**

## Step 1: Work Out What, and at Which Level

From `$ARGUMENTS`:
- **What**: a sub-goal ("SG-3", "3") or a concept in words ("change of basis", "contingency")
- **Level** (optional): if the input contains a level name (High school, Master's or Advanced, in any capitalisation, with or without the apostrophe), that is the level

Use Glob to find `*_training_plan.md` in the current directory and read it. If several match, ask which one to use.

- **A sub-goal number, or words that match a sub-goal**: work from that sub-goal's blueprint (its principle, its CTQs, its Estimated Depth). Default level: the sub-goal's Estimated Depth.
- **A concept that matches no sub-goal, or no plan at all**: work from the concept as stated. Default level: the plan's Target level, or Master's when there is no plan.
- If the request is too vague to choose a concept, ask what the exercises should be about.

## Step 2: Check Before Showing Solutions

If the request maps to a sub-goal whose Status is still `pending`, say so before going on: these exercises come with full solutions, and reading them first makes that sub-goal's Initial Test less informative. Offer to run `/run-session SG-<N>` first, and continue with the exercises if the learner prefers them now.

## Step 3: Write the Set

If the sub-goal already has an exercise book, `<topic>_artefact_SG<N>_exercises.md`, read it so that nothing is repeated.

Write an on-request set following the concept-explainer skill's **Exercise Book Format**:
- 3 exercises at the chosen level, graded from standard to demanding
- Each with a complete worked solution: every step shown and annotated, ending with a Check that confirms the result a second way
- None repeating a case already used: the sub-goal's Initial Test or Final Test, a solved exercise in the plan, or an exercise already in the book
- Pitched as the level defines (concept-explainer skill, Depth Levels): High school in plain words and concrete numbers; Master's in the field's notation, symbols first and then numbers; Advanced in full generality, with proofs or derivations and edge cases
- SI units, unless the learner or the domain requires otherwise

Never invent a value you are not sure of: mark it `(verify)`.

## Step 4: Save and Register

**With a sub-goal:** append the set to `<topic>_artefact_SG<N>_exercises.md`. Create the file if it does not exist; never overwrite an earlier set. If the file is new and the plan has an Artefacts Register, add a row for it with the Edit tool:

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| Exercise book: SG-<N> | deliverable | SG-<N> | <topic>_artefact_SG<N>_exercises.md | current |

**With no plan, or no matching sub-goal:** write the set to `exercises-<concept-in-kebab-case>.md` in the current directory, appending if it exists.

## Step 5: Present the Exercises

Show the three exercise statements, and only the statements. Then say where the file is and that the worked solutions are in it, and offer both ways to continue:
- The learner sends an attempt, and you check it against the worked solution, then show that solution in full
- The learner asks for the solutions, and you show them in full

Do not show a solution in the same message as its exercise.

## Important

- Every exercise is solved in full. A final answer alone is not a solution.
- Every solution ends with a Check
- These exercises are practice, not assessment: nothing here changes a sub-goal's Status or Score, and nothing is written to the learner profile
- Do not reuse a test case from the plan: the tests must stay unseen
