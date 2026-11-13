---
name: visual-explainer
description: Deliver a whole training-plan session as an interactive page instead of chat text. This is the default delivery of /run-session. Builds one page per session in three stages (the opening question and Initial Test, the teaching with the Socratic chain on the picture, the Final Test) with live objects, colour by role, a check after each explanation, a climb through the levels for hard-core principles, and answers and results blocks the session reads back.
---

# Visual Explainer -- Domain Knowledge

Some principles are easier to see than to read: a matrix whose rows and columns mean different things, a vector that rotates, a probability that is a share of a grid. This skill turns a session into one interactive page, from the opening question to the Final Test. It is the default delivery: the learner gets chat text only by asking for `chat`, or when no page can be delivered. It changes how the session is delivered. It does not change what is taught, the order, or how the session is judged.

`/run-session` holds the session flow. The concept-explainer skill's Level Ladder holds the content rules for the climb. This skill holds the rules for the page.

## Where the Page Sits in a Session

| Phase | Chat delivery | Visual delivery (default) |
|-------|---------------|-----------------|
| Discovery Question, Initial Test | chat | **the page, stage 1**: the picture, the question, the test, answer boxes |
| Evaluate | chat | chat, in a few lines |
| Teach: Socratic Guidance Chain | chat | **the page, stage 2**: one question at a time on the picture |
| Teach: the climb | chat | **the page, stage 2** |
| Teach: other gaps | chat | **the page, stage 2**, one section per gap |
| Clarifications, deep-dive, questions | chat | chat |
| Final Test | chat | **the page, stage 3** |
| Record | files | files, plus the page |

The page shows, asks, checks and saves. It checks numeric and multiple-choice answers itself, and has written reasoning judged in place against the blueprint's pass criteria. The session confirms the result from the saved record when the learner returns.

### The whole session on the page (no copying)

The learner should be able to go from the first question to the result of the Final Test without leaving the page and without copying anything into chat. Build the page this way whenever the environment lets a published page (a) ask the model a question and (b) save data the session can read back (in Claude artifacts: the `sample` and `db` capabilities).

- **One step on screen at a time.** The picture stays pinned at the top; below it is a single step with one thing to do and one button. A progress line says "Step N of M". No stage tabs, no long scroll, no sections to hunt for. Each step's feedback appears in place, then a Next button.
- **Answers are checked where they are given.** Choices, values and operations on the picture are checked by the page's own code. Written answers (the learner's statement of the idea, the open parts of a test) are sent to the model from the page with the blueprint's pass criteria as the rubric; the reply is a verdict plus at most two or three sentences, shown in place. In a Socratic step the reply to a weak statement is one narrowing question, never the idea itself.
- **Everything is saved by the page**, after every step: each answer, the number of tries, the written statements and the verdicts. The session reads this record when the learner comes back; nothing is pasted.
- **It opens with motivation and history.** The first two steps are "Why this matters" and "How we got here": the real situation before the idea, as something to operate (a timeline with what each approach solved and where it broke down, or a before and after), with names and dates only when certain. They give no answer to the session's questions. The first question comes after them.
- **Clear questions, true cases.** Each step asks one thing and says what form the answer takes. Each case is something really done; the page never invents a method in order to knock it down, and never states as fact something true only in its toy example.
- **All three stages are built at once** and follow each other on the page: the opening question and Initial Test, the discovery and consolidation, the Final Test with its result. After a failed Final Test the page offers it again (at most twice) on the same page. Because the teaching cannot be built from an answer not yet given, it covers the blueprint's whole Guidance Chain and every anticipated CTQ; the learner's own Initial Test answer is quoted by the page where the teaching begins.
- **A wrong answer never blocks.** The page reacts visibly to every answer: a wrong choice is marked and its feedback appears at once. The first wrong answer gets a hint that says what to look at or what to compute. From then on a button, "Show me the answer and go on", is always there: it marks the right answer, explains it, and opens Next. An operation step (sliders, a drag) shows its hint from the start and offers to set a working state. A written answer that is judged insufficient can always be passed with "Go on". A shown answer is saved as shown, so the session knows it was not found unaided and treats it as a gap, not as a pass.
- **Going back.** Every step has a Back button. A finished step reopens with the learner's answer, its feedback and the picture as it was, and the learner may change the answer. A step that is not finished keeps Next disabled.
- **Contents.** A Contents button, always visible, opens an index of the session's steps with their state (done, next, locked) and lets the learner jump to any step already reached. Below it, the course's sub-goals with this session marked, so the learner sees where the session sits in the course.
- **Manual.** A Manual button, always visible, opens a reference document the page writes from the session: the case, one section per finished step stating what was found with the page's own numbers, the specification and worked example, the learner's own statement and test answers with their feedback, a glossary of the session's terms, and the learner's notes. A section appears only when its step is finished, so the manual never gives an answer away; the page says how many sections are filled. The learner can save it as a file and copy its text.
- **Notes.** Each step has a small "My note for this step" box. Notes are saved and are added to the manual.
- **Pick up where you stopped.** On opening, the page reads the saved record BEFORE it shows any step or writes anything, then goes to the first unfinished step. Until the record has been read, the page writes nothing: a freshly loaded page must never overwrite saved progress. If the record cannot be read within a few seconds, start from step 1 and say so.
- **Next always moves forward.** Next is enabled only when the current step is finished and always opens the step after it; it never jumps backwards because another step looks unfinished. Only Contents limits a jump to the steps already reached.
- **Help without leaving.** A small "A word is unclear?" box asks the model for a term clarification under the term-clarifier's rules (the term only, no help with the exercise). A "not familiar" button on a test opens the full explanation on a case that is not the test's.
- **The end screen** gives the result and one line: the session is saved, and writing `done` in chat records it and proposes the next session.
- **The session's part.** When the learner returns, read the saved record, confirm or correct the page's verdicts against the pass criteria (the session's judgement is final), and go to RECORD. Do not ask the learner to repeat anything the record holds.
- **Fall back** to the staged page with answers and results blocks, described next, only when the page cannot ask the model or cannot save. Say which is missing.

### The three stages (fall-back: answers come back through chat)

The page is one file, delivered again at the same address as each stage is added. Earlier stages stay on the page, collapsed.

| Stage | Contains | Must not contain |
|-------|----------|------------------|
| 1. Opening | Why it matters and the historical context; the picture with the given values as live objects; the Discovery Question (Socratic plans); the Initial Test, one answer box per part; the "not familiar" and "clarification" notes; the answers block | Any hint, expected answer, named wrong path, or part of the picture the test asks the learner to work out |
| 2. Teach | The sections described below; the results block | The answer to a check before the learner submits |
| 3. Final Test | The same picture with the new case's values; the Final Test, one answer box per part, Part B in a Socratic session; the two notes; the answers block | Anything from stage 2 left open beside the test: collapse it |

**One picture for the session.** When the plan has a course diagram, or the blueprint a `Diagram focus` line, all three stages are drawn on that diagram with the named part lit and the rest dimmed or covered. A test's given values are placed on the diagram where they belong.

**The answers block** is plain text with a Copy button, like the results block:

```
SESSION ANSWERS
Sub-goal: SG-<N> <title> | <Initial Test / Final Test>
(a) <the learner's text>
(b) <the learner's text>
```

A learner who writes "not familiar" or asks for a clarification does so in chat.

## What the Page Contains

A session's page holds one section for each teaching block. The table below is the section for a hard-core climb. The sections for other gaps follow it.

Build the page from the blueprint. Every part below has a source; do not invent teaching content the blueprint does not hold.

| Part of the page | Source | Rule |
|------------------|--------|------|
| 1. The setup | Visual design: Objects | The objects on screen, with their real numbers. Small enough to read at a glance. |
| 2. What you predicted | The learner's answer to the Initial Test | Quoted, with why it feels right. No second prediction is asked: the Initial Test was the prediction. |
| 3. The reveal | Tempting answer, Insight | The learner's assumption shown failing on the Initial Test case, with the true result beside it. Then the Insight, in its one sentence, set apart. |
| 4. The picture | Picture, Visual design: Colour roles | The Picture drawn with the page's own objects. State where it stops being true. |
| 5. The climb | Worked Example (foundational), Level ladder | One tab per rung, from the start rung to the session's level. Each tab: the rung's solved exercise, then "your turn". |
| 6. The control | Visual design: Control | One thing the learner can change, and what to watch when they do. |
| 7. Back to your session | -- | The results block and a Copy button. |

When the learner declared "not familiar", leave out parts 2 and 3's failing assumption, as the climb does: give the Insight, the Picture and the rungs, and do not solve the Initial Test case.

When the climb starts above High school, the page still shows parts 3 and 4 in short form, and the tabs start at the start rung.

In a **Socratic session** stage 2 opens with the Guidance Chain on the picture, and parts 4 to 7 stay closed until the learner has written the Insight in their own words:

- One question on screen at a time, beside the part of the picture it is about. The next appears only after an answer.
- Each question is put as something to do wherever it allows: a value to enter, an object to move, a cell to pick, a choice among answers a learner would really give. An open question gets a text box.
- A wrong answer is not corrected. The page shows what that answer predicts on the picture, lets the prediction fail, and asks again. No question states the concept or contains its own answer.
- After the last question, a text box: "Say the idea in your own words." Submitting it opens parts 4 to 7. The text goes into the results block as `Stated idea: <text>`, with one line per chain question (`Q<n>: <answer>, <N> tries`), and is judged in chat.
- Parts 2 and 3 (the quoted prediction and its failure) are shown before the chain, without the Insight: they are the tension.

### Sections for other gaps

A gap that is not a hard-core principle gets a shorter section, with the same content the chat explanation would have (concept-explainer skill), in this order:

| Format | The section shows |
|--------|-------------------|
| Abbreviated | The problem in two sentences, the principle, the worked example drawn with live objects, one check |
| Full | The same, plus the key formula with each symbol tied to an object on the page, the conceptual map as a small diagram, one check per CTQ (at most three) |
| Comparison | The two concepts side by side on the same case, the cells where they differ outlined, one check that needs the distinction |
| "Not familiar" | The full explanation of the sub-goal's topic on a case that is NOT the Initial Test case, then one check per CTQ |

In a Socratic session each of these sections also opens with its Guidance Chain, by the rules above, and the worked example and checks open after the learner's own statement.

The blueprint has no Visual design for these. Choose the objects from the block's worked example, with the table "Which widget for which field" below, and keep to one control per section. A Motivation sub-goal has no formula: show the before and the after of the topic as two things the learner can operate and compare.

## The Visual Design Field

A hard-core blueprint carries a `Visual design` with five parts. When a plan has none (it was created before the field existed), derive one from the Picture and the solved exercises, and tell the learner the page was designed during the session.

- **Objects**: what is drawn, with its size and exact values. Keep it tiny: 3 tokens in 2 dimensions, one qubit, a 10 by 10 grid of cases, five cash flows.
- **Colour roles**: one colour for each role an object plays (for example query, key, value). At most three.
- **Steps**: the order in which the objects appear or change, each with the one sentence that goes with it.
- **Your-turn inputs**: for each rung, what the learner types or picks, the right value, and the two most likely wrong values with what each one reveals.
- **Control**: the one slider, toggle or drag the learner can use, and what it shows.

### Which widget for which field

| Subject | Objects | Typical control |
|---------|---------|-----------------|
| Linear algebra, machine learning | Small matrices as heatmaps, cell by cell | Run more steps; change one entry |
| Quantum mechanics, geometry | An arrow on a circle or sphere, with its projections | Rotate the arrow or the measuring axis |
| Probability, statistics | A grid of dots, one per case, coloured by outcome | Change the base rate |
| Calculus, physics | A curve with a movable point and its tangent or area | Drag the point |
| Finance | A cash-flow timeline with bars | Change the rate |
| Cost estimation, planning | A breakdown table that sorts and sums; a schedule bar | Change one quantity or rate |
| Law, procedures | A timeline or decision path with the rule at each branch | Change one fact of the case |

A subject with no natural picture gets a page with a worked table and step-by-step replay, not decoration.

## Rules for the Page

**Numbers**
- Every number on the page is computed by the page's code from the given values. Never type a result in by hand.
- Before delivery, run the page's computation once outside the page and compare it with the blueprint's solved exercises. Check a gradient or a derivative against a finite difference. A page that disagrees with the blueprint is not delivered: fix the page, or correct the blueprint and say so. Where no code can be run, recompute each solved exercise by hand from the page's values.
- The solved exercise on the page uses the numbers on the page. When the blueprint's exercise uses other numbers, keep its method and steps and recompute.
- Rounded numbers must still add up as shown: display enough decimals for the steps to reproduce by hand.

**Colour**
- Colour by role marks whose object it is (a border or label). Colour by value marks the number (the cell fill). Never use the same hues for both.
- Values use a diverging scale around zero, two hues plus neutral, readable without colour (the number is always printed in the cell).
- Mark the cells an explanation talks about with an outline, not with colour alone.

**Interaction**
- Hovering, tapping or focusing a cell shows the formula that produced it, with numbers, and outlines the cells it came from.
- Each "your turn" takes one answer. Right: show the complete worked solution, ending with a Check. Wrong: name what the wrong value reveals when it is one of the anticipated ones, then replay the solved exercise one step at a time, each step outlining its cells; the learner may then try again.
- The answer to a "your turn" is never visible before the learner submits. Where the page shows a full matrix, ask for a value the learner must compute or locate by reasoning, and say plainly when the page's own display is the check.
- One control, not a dashboard.

**Form**
- One page per session, in three stages. No external data and no libraries the page cannot work without. It must read on a phone (about 400 px wide) without sideways scrolling, in light and dark themes.
- Short sentences beside the objects. The page is not a chat explanation pasted into boxes: if a paragraph needs more than three sentences, it belongs in chat.
- Progress is remembered in the browser as a convenience only. The results block is what counts.

## The Results Block

The page ends with a plain-text block the learner copies into chat:

```
VISUAL SESSION RESULTS
Sub-goal: SG-<N> <title>
<Level or check name>: <correct, N tries | not solved, N tries | not attempted>[, worked solution replayed]
(one line per rung of a climb, and one per check of any other section)
Level reached: <for a climb only: the highest rung solved with every rung below it solved, or "none">
```

The session reads it as the record of the climb:

| On the page | In the session |
|-------------|----------------|
| Correct, 1 try | Rung held |
| Correct after the solution was replayed | Rung held after a bridge |
| Not solved | Rung not held: the climb stopped here |
| Not attempted | Ask the learner whether to continue on the page or in chat |

For a check outside a climb, read "rung held" as "Quick Check passed", "held after a bridge" as "passed after the re-explanation one level down", and "not solved" as a persistent gap.

The block is the learner's own report, so confirm it with one short question in chat on the highest rung reported ("In one sentence: why does the key read the column?"). A wrong answer there means that rung is not held. If the learner cannot copy the block, ask what they reached and use the same question.

## Delivering the Page

1. Write the page to `<topic>_visual_SG<N>.html` in the working folder.
2. If the environment has a tool that publishes a page and returns a link, publish with it and follow that tool's page rules. Otherwise write a complete HTML document and tell the learner to open the file in a browser.
3. In chat, say in two or three lines what the stage is, how long it takes, and that the answers block or the results block comes back to chat. Then wait.
4. After each stage is read, add the next stage to the same file and deliver it again at the same address.
5. If no page can be delivered (no file access, or the learner cannot open one), say so and run that phase in chat. Record the delivery as `chat`.

## Example

`examples/query-vs-key.html` is a complete page for one principle: in self-attention, the query and key matrices receive different gradients even when they start identical. Read it for the structure and the amount of text, not to copy its subject. It was built to stand alone, so it asks for a prediction itself and shows only the Teach stage; a page built in a session has the three stages and quotes the learner's answer to the Initial Test.

`examples/why-attention.html` is a page for a Motivation sub-goal with no formula: a "not familiar" explanation of why attention replaced recurrent reading, with three things to operate (distance, selection by content, cost) and three checks.

The Visual design of the first example, as a plan would hold it:

- **Objects**: 3 tokens in 2 dimensions. X (3×2), W_Q = W_K = [[1, 0.5], [−0.5, 1]], W_V, target T; the forward pass Q, K, S, P, O and the loss; the gradients dS, dQ, dK, dW_Q, dW_K.
- **Colour roles**: query purple, key teal, value ochre. Cell fill: blue negative, orange positive.
- **Steps**: setup → the learner's prediction → the two gradients side by side, differing cells outlined → dS read by rows (query) and by columns (key).
- **Your-turn inputs**: High school: read P[3,1] (0.23; 0.41 means the row and column were swapped). Master's: compute dK[2,1] (−0.39; −0.07 means dS was read along the row; −0.55 means the √d was dropped). Advanced: the factor on dW_K when W_Q is doubled and W_K halved (2; 0.5 is the factor on dW_Q).
- **Control**: a slider that runs 0 to 40 gradient steps and shows the two matrices and the distance between them.
