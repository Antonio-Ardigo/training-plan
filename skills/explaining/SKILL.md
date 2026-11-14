---
name: explaining
description: How things are explained and written down in a lesson. Use when writing any explanation (short, full, side by side, or a key idea level by level), a worked example, a check or Your turn and its solution, a step back, go deeper, the success criteria and common mistakes, an idea map, the lesson notes or the practice book. Also use when the learner asks to have something explained outside a lesson.
---

# Explaining

This skill owns how things are explained and written down during a lesson: the formats, the levels, worked examples, checks, success criteria, common mistakes, go deeper, the idea map, the lesson notes and the practice book.

Other skills own the rest:
- **lesson-flow** says when each thing happens in a lesson, what is judged and what is saved in `course.json`.
- **visual-explainer** builds the lesson page. A page shows the same content as this skill defines.
- **course-model** owns `course.json`, the folder layout and the paths. Its `glossary.md` gives the words to use.

Use the glossary words in everything the learner reads.

## Files in this folder

| File | Holds |
|---|---|
| `formats.md` | The four formats and their sections, the aha moment, the levels of a key idea, the recap, and worked examples by subject |
| `idea-map.md` | The idea map: format, node kinds, link labels, built from `course.json` |
| `lesson-notes.md` | The lesson notes, `lessons/<NN-slug>/notes.md` |
| `practice-book.md` | The practice book, `lessons/<NN-slug>/practice.md` |

## 1. Levels

A course has one level: High school, Master's or Advanced (`course.level`: `high-school`, `masters`, `advanced`). The level says who an explanation is for. It sets the notation, the rigour and the kind of worked example. Difficulty does not set the level: an easy lesson gets a shorter explanation at the same level. With no course to read it from, the level is Master's.

| Level | Assumes | How it explains | Worked example | Maths |
|---|---|---|---|---|
| **High school** | School mathematics. No earlier contact with the topic | Plain words, one picture or analogy, concrete numbers. Every symbol explained on first use | Concrete numbers throughout. Every step shown, with a plain-words Why | Minimal notation. The idea first |
| **Master's** | The field's standard tools and notation | The formal statement, where it comes from, the key equations, and how it contains the High school picture | Symbols first, then numbers. Every step with its Why | LaTeX throughout |
| **Advanced** | The Master's level, held | Full generality: a proof or rigorous derivation, the limits of validity, competing formulations, and what the Master's statement assumed without saying | A proof, a derivation or a non-standard case, with edge cases checked and other routes shown | LaTeX, proofs, edge cases |

Write level names in full: High school, Master's, Advanced. Never shorten High school to "high", which is a difficulty value.

## 2. Choosing the format

Each item in **what to work on** gets its own explanation, in one of four formats (`formats.md`). Never combine two items in one explanation. Decide in this order:

| Situation | Format |
|---|---|
| A key idea ★, and what to work on is the key idea itself (also after start from scratch) | **Level by level** |
| The common mistake is mixing up two ideas | **Side by side** |
| The learner chose start from scratch | **Full** |
| Any other common mistake kind, a kind that recurs in two or more lessons (Your progress), or missing background | **Full** |
| Anything else: a slip, a missing fact, a narrow point | **Short** |

Outside a lesson, a request to explain something gets the full format at the level the learner names, Master's by default. The short format is used only inside a lesson.

Keep each explanation as short as the item allows. Start from the learner's own answer and what it costs them. Show a concrete example before any formal statement.

In a Socratic course the content is the same. The learner reaches the idea through the guiding questions first, and the worked example comes after the learner has stated the idea. lesson-flow gives the order.

## 3. Worked examples

A worked example solves one case completely. Every explanation in every format has one. Its parts match `worked_example` in `course.json`: title, given, steps (each a `do` and a `why`), result, check.

```markdown
### Worked example: <the case, in a few words>

**Given:** <all the data, with units>

**Step 1:** <what is done, with the working>
$$<the operation and its intermediate result>$$
> **Why:** <why this step is taken and what it achieves>
> **Watch out:** <optional: a unit trap, a sign, a boundary case, a common mistake at this step>

**Step 2:** ...

**Result:** <the answer, with units and what it means>

**Check:** <the result confirmed a second way>
```

Rules:
- Show every step. Never write "it can be shown that" or "after simplification": show it. Expanding $(a+b)^2$ means writing $a^2 + 2ab + b^2$.
- Define every variable on first use, with its units.
- The Why gives the reasoning. It does not repeat the step in words.
- The **Check** comes last and confirms the result a second way: units, a limiting or special case, putting the result back in, another method, or an order-of-magnitude estimate. A line that only restates the result is not a Check.
- These rules apply to every worked example and to every solution shown after a check, a Your turn or a practice exercise. A final answer alone is never a solution.
- The format adapts to the subject: `formats.md` has the layouts for maths and science, languages, costs and business, and programming.

## 4. Checks and Your turn

A **Check** ends every explanation. **Your turn** is the check at each level of a key idea. Both follow the same rules.

```markdown
**Check** (<the success criterion it tests>)
<the question, with all data and the form of the answer expected>

*If a word in this question is unclear, ask what it means.*
```

- The question comes from a success criterion: its `how_tested`, or a new question written to test its `what`.
- It tests understanding, not recall: "When would you use X?", not "What is the definition of X?".
- It is a new case. It never repeats Try first, Show you've got it, a worked example or an earlier exercise.
- In a Socratic course, the check asks the learner to rebuild why the idea is the only way out of the clash they met.
- The expected answer and the mistake to watch for are kept by the teacher. They are never written in the explanation and never shown before the learner answers.
- After the answer, show the complete worked solution in the format of section 3, ending with its Check. When the check asks for an explanation, the solution is the full chain of reasoning, step by step.
- Judge the method. An arithmetic slip with the right method is not a wrong method.
- When the learner asks what a word means, the term-helper agent answers without giving the answer away.

## 5. Step back

After a wrong method on a check or a Your turn, step back one level:

| The explanation was at | Step back to |
|---|---|
| Advanced | Master's |
| Master's | High school: plain words, a picture, concrete numbers |
| High school | High school, with a different picture or example |

A step back is a few lines that tie the step that failed to what the learner already holds. It is not a second explanation. Then give one new check (or one new Your turn) at the original level. A level has at most two exercises: the Your turn and this one. lesson-flow says what happens after a second wrong answer.

In a Socratic course the step back is made of questions pitched one level down. It returns to the guiding question where the reasoning broke.

## 6. Common mistakes

Every item in what to work on is named with the common mistake it shows, where one applies (`common_mistake.kind`).

| Common mistake | Field value | How to recognise it | How to teach against it |
|---|---|---|---|
| **Mixing up two ideas** | `mixing-up` | Uses one idea where a related one applies, or treats the two as one | The side by side format: what they share, where they differ, one case worked under both |
| **Stretching a rule too far** | `overstretching` | Applies a rule outside the cases where it holds | Teach the boundary: one case where the rule holds, one where it fails, and the condition that separates them |
| **Missing background** | `missing-background` | Cannot start, or asks about a word the lesson assumes | Teach the background first, briefly, then the lesson's idea. lesson-flow offers to add a background lesson |
| **Steps without the why** | `steps-without-why` | Follows the steps but cannot say why they work or when they fail | The principles and the why before the how. Every step's Why carries the reasoning |
| **Words without the maths** | `words-without-maths` | Describes the idea correctly but cannot write the equation or produce the number | The formal statement, built from the learner's own sentence. A worked example with symbols first, then numbers |
| **Maths without the picture** | `maths-without-picture` | Handles the symbols but cannot say what a result means | The picture, concrete numbers, and the meaning of every result in words |

## 7. Success criteria

Success criteria (`design.success_criteria`) say what the learner must be able to do to hold a lesson. Each has four parts: **what** the learner can do, **from** (the principle or level it comes from), **how it is tested**, and the **common mistake** (kind and one line). The course-design skill writes them into the lesson design. Use the design's criteria. Write new ones only for what the design does not cover (a full explanation of a background point, a go deeper, an explanation outside a lesson), by these rules:

- Each one is checkable. "Can work out the entropy of a simple system from its number of microstates" is a success criterion. "Understand entropy" is not.
- Trace them from the principles ("Energy is conserved" gives "Can track energy across heat, work and internal energy in a closed system") and from the key innovations ("Earned value" gives "Can compute CPI and SPI from earned value, planned value and actual cost").
- For each one, name the most likely common mistake (section 6).
- A key idea has at least one success criterion per level.

In an explanation the success criteria appear as a table:

```markdown
| What you can do | From | How it is tested | Common mistake |
|---|---|---|---|
| <what> | <principle or level> | <how tested> | <kind>: <one line> |
```

## 8. Go deeper

The learner may ask to go deeper on a principle just explained.

- Write the full format for that one principle, at the lesson's level. Frame The problem inside the explanation it came from: "Within <idea>, <this principle> matters because...".
- Offer it once, after the first explanation of the lesson. Never repeat the offer.
- One go deeper per explanation. A go deeper may raise a principle the learner then asks to go deeper on.
- It goes into the lesson notes.

## 9. Writing style

- Short, plain, declarative sentences in the active voice. Glossary words only.
- **Maths.** LaTeX from Master's up: `$...$` inline, `$$...$$` on its own line, `$x$` for a variable in a sentence. Usual notation: vectors `$\mathbf{v}$`, matrices `\begin{pmatrix}...\end{pmatrix}`, derivatives `$\frac{\partial f}{\partial x}$`, sums `$\sum_{i=1}^{n}$`, probability `$P(A \mid B)$`, norms `$\lVert x \rVert$`. At High school, minimal notation, and every symbol explained in words on first use.
- **Units.** SI and ISO units: kg and t (1 t = 1,000 kg), m, mm, km, m², m³, L, N, kN, Pa, kPa, MPa, °C (K in thermodynamics). Currency in $ or the learner's currency. Imperial units only when the learner asks or the field requires them (feet in US aviation). Write the unit beside every number in a calculation.
- **True values.** Never invent a value you are not sure of. Mark it `(verify)`.
- **Higher levels add.** A higher level says what it adds to the level below. It never tells the learner the lower level was wrong: the lower level was a correct view of a special case.
- **Nothing given away early.** No explanation, map or file shown before a test contains its answer.

## 10. Older names

Plugin versions before 4 used other words. Read them as: concept explainer and content builder, this skill; CTQ, success criteria; failure-mode tags (conflation, overgeneralization, missing prerequisite, procedural without conceptual, verbal without formal, formal without intuitive), the six common mistakes in that order; quick check, Check; abbreviated / full / comparison / ladder, short / full / side by side / level by level; hard core, key idea; insight, the aha; reveal, the aha moment; rung and climb, levels; bridge, step back; deep-dive, go deeper; gap, what to work on; concept map, idea map; concept file and concept library, lesson notes and notes; exercise book, practice book; sub-goal and SG-N, Lesson N; plan, course; introductory / intermediate / advanced, High school / Master's / Advanced.
