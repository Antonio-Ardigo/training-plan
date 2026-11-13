---
name: visual-explainer
description: Deliver the Teach phase of a training-plan session as an interactive page instead of chat text. This is the default delivery of /run-session, for every gap and for hard-core principles. Builds one page per session with live objects, colour by role, a check after each explanation, a climb through the levels for hard-core principles, and a results block the session reads back.
---

# Visual Explainer -- Domain Knowledge

Some principles are easier to see than to read: a matrix whose rows and columns mean different things, a vector that rotates, a probability that is a share of a grid. This skill turns the Teach phase of a session into one interactive page. It is the default delivery: the learner gets chat text only by asking for `chat`, or when no page can be delivered. It changes how the Teach phase is delivered. It does not change what is taught, the order, or how the session is judged.

`/run-session` holds the session flow. The concept-explainer skill's Level Ladder holds the content rules for the climb. This skill holds the rules for the page.

## Where the Page Sits in a Session

| Phase | Chat delivery | Visual delivery (default) |
|-------|---------------|-----------------|
| Initial Test | chat | **chat** (unchanged: the answer needs judging) |
| Evaluate | chat | chat |
| Teach: the climb | chat | **the page** |
| Teach: other gaps | chat | **the page**, one section per gap |
| Clarifications, deep-dive, questions | chat | chat |
| Final Test | chat | **chat** (unchanged) |
| Record | files | files, plus the page |

The tests stay in chat because they ask for written reasoning, and only the session can judge it. The page teaches and checks numeric or multiple-choice answers; it does not decide whether the learner has mastered the sub-goal.

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

In a **Socratic session** the page is built only after the learner has stated the Insight in chat. It then carries parts 4 to 7.

### Sections for other gaps

A gap that is not a hard-core principle gets a shorter section, with the same content the chat explanation would have (concept-explainer skill), in this order:

| Format | The section shows |
|--------|-------------------|
| Abbreviated | The problem in two sentences, the principle, the worked example drawn with live objects, one check |
| Full | The same, plus the key formula with each symbol tied to an object on the page, the conceptual map as a small diagram, one check per CTQ (at most three) |
| Comparison | The two concepts side by side on the same case, the cells where they differ outlined, one check that needs the distinction |
| "Not familiar" | The full explanation of the sub-goal's topic on a case that is NOT the Initial Test case, then one check per CTQ |

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
- One page per session. No external data and no libraries the page cannot work without. It must read on a phone (about 400 px wide) without sideways scrolling, in light and dark themes.
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
3. In chat, say in two or three lines what the page is, how long it takes, and that the results block comes back to chat. Then wait.
4. If no page can be delivered (no file access, or the learner cannot open one), say so and teach the climb in chat. Record the delivery as `chat`.

## Example

`examples/query-vs-key.html` is a complete page for one principle: in self-attention, the query and key matrices receive different gradients even when they start identical. Read it for the structure and the amount of text, not to copy its subject. It was built to stand alone, so it asks for a prediction itself; a page built in a session quotes the learner's answer to the Initial Test instead.

`examples/why-attention.html` is a page for a Motivation sub-goal with no formula: a "not familiar" explanation of why attention replaced recurrent reading, with three things to operate (distance, selection by content, cost) and three checks.

The Visual design of the first example, as a plan would hold it:

- **Objects**: 3 tokens in 2 dimensions. X (3×2), W_Q = W_K = [[1, 0.5], [−0.5, 1]], W_V, target T; the forward pass Q, K, S, P, O and the loss; the gradients dS, dQ, dK, dW_Q, dW_K.
- **Colour roles**: query purple, key teal, value ochre. Cell fill: blue negative, orange positive.
- **Steps**: setup → the learner's prediction → the two gradients side by side, differing cells outlined → dS read by rows (query) and by columns (key).
- **Your-turn inputs**: High school: read P[3,1] (0.23; 0.41 means the row and column were swapped). Master's: compute dK[2,1] (−0.39; −0.07 means dS was read along the row; −0.55 means the √d was dropped). Advanced: the factor on dW_K when W_Q is doubled and W_K halved (2; 0.5 is the factor on dW_Q).
- **Control**: a slider that runs 0 to 40 gradient steps and shows the two matrices and the distance between them.
