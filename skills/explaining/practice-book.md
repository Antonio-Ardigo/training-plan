# Practice book

A practice book is a lesson's fully solved exercises: `lessons/<NN-slug>/practice.md` in the course folder, listed in `files` with kind `practice`. Without a course, or for an idea no lesson covers, it is `exercises-<idea-as-a-slug>.md` in the working folder.

Principle, Concept, Tool and Background lessons have a practice book. Why it matters and Capstone lessons have none. lesson-flow says when a set is added at the end of a lesson. The worked-exercises command adds a set on request.

## Two kinds of set

| Set | Holds |
|---|---|
| **Lesson set**, added at the end of a lesson | Two exercises for each level from High school up to the course level: one standard, one with a twist (a changed condition, an extra step, or a trap the standard one does not have) |
| **On-request set** | Three exercises at the one level asked for, from standard to demanding |

If the lesson design has a `practice_task`, it opens the first lesson set as the first exercise at the course level, with its solution. It counts as one of the two for that level.

## Layout

The file is append-only. Each write adds one dated set at the end and never changes an earlier set. In a set, each level's statements come first and their solutions after, so the learner can try before reading.

```markdown
# Practice book: Lesson <N>, <lesson title>
Course: <course title> | Level: <course level>

> Try each exercise before you read its solution. In every set, the solutions follow the exercises.

## Set <YYYY-MM-DD>, <after the lesson | on request>

### High school: exercises
**HS-1.** <statement, with all data and units>
**HS-2.** <statement, with the twist>

### High school: solutions
**HS-1.**
**Given:** <data>
**Step 1:** <working>
> **Why:** <reasoning>
**Result:** <answer, with units and meaning>
**Check:** <the result confirmed a second way>

**HS-2.** <same format>

### Master's: exercises
**MSc-1.** ...
```

## Rules

- Label exercises by level: HS-1, MSc-1, Adv-1. Number them through the whole file, continuing from the last number used at that level.
- Every solution is a complete worked solution in the worked-example format (`SKILL.md` section 3) and ends with a Check. A final answer alone is not a solution.
- Pitch each exercise as its level explains (`SKILL.md` section 1): High school in plain words and concrete numbers, Master's in the field's notation with symbols first, Advanced in full generality with proofs or derivations and edge cases.
- Read the book before writing. No exercise repeats Try first, Show you've got it, a worked example or solved example in the lesson design, a check or Your turn from a lesson, or an exercise already in the book.
- Never invent a value you are not sure of. Mark it `(verify)`.
