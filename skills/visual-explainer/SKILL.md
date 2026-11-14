---
name: visual-explainer
description: How a lesson page is built. Use when building the page for a lesson, which is the default delivery of /continue - what the page shows and in what order, the widgets and colours, how it reacts to answers, the numbers it computes, how it saves answers or hands them back to chat, and how it is written, listed in course.json and published.
---

# Visual Explainer

Some principles are easier to see than to read: a matrix whose rows and columns mean different things, a vector that rotates, a probability that is a share of a grid. This skill builds the **lesson page**: one interactive page that carries a lesson from its opening to Show you've got it. The page is the default delivery. The learner gets the lesson in chat only by asking for `chat`, or when no page can be delivered. The page changes how a lesson is delivered. It does not change what is taught, the order, or how answers are judged.

Other skills own the rest:

- **lesson-flow** says when each part of the page is built, how answers are judged, and what is saved in `course.json` and when. Its section 2.7 "Page delivery" is the page's part of the lesson. Its section 3 gives the verdicts.
- **explaining** writes the content the page shows: the formats, the aha moment, the levels, worked examples, checks, Your turn and the step back.
- **course-model** owns `course.json`, the folder layout and the files list. Its `glossary.md` gives the words. Use them on the page as everywhere else.

This skill owns only the page: what it contains and in what order, its widgets and colours, how it reacts, the numbers it computes, how it saves or hands answers back, and how it is delivered.

## 1. Two ways to build the page

| The environment | The page |
|---|---|
| A published page can ask the model a question and save data the lesson can read back (in Claude artifacts: the `sample` and `db` capabilities) | **The whole lesson on the page** (section 2). The learner never copies anything into chat |
| The page can do neither, or only one of the two | **Three stages through chat** (section 3). The page hands answers back in plain-text blocks. Say which ability is missing |

lesson-flow 2.7 says when each is built and how what comes back is read.

## 2. The whole lesson on the page

The learner goes from the first question to the result of Show you've got it without leaving the page. All parts are built at once and follow each other on the page: the opening, Try first (with the puzzle in a Socratic course), Learn with its checks, Show you've got it, and the result.

**What the page shows**

- **It opens with why it matters and how we got here.** These are the first two steps, built from `design.context`. They show the real situation before the idea as something to operate: a timeline with what each approach solved and where it broke down, or a before and after. Names and dates appear only when certain. They give no answer to the lesson's questions. The first question comes after them.
- **One step on screen at a time.** The picture stays pinned at the top. Below it is one step, with one thing to do and one button. A progress line says "Step N of M". There are no stage tabs, no long scroll and no sections to hunt for. Each step's feedback appears in place, then Next.
- **Clear questions, true cases.** Each step asks one thing and says what form the answer takes. Each case is something really done. The page never invents a method in order to knock it down. It never states as fact something true only in its small example.
- **The tests end with their notes.** Try first and Show you've got it end with the two notes of lesson-flow 3.4. Every check and Your turn ends with the short word note.
- **Learn is built before the learner answers.** So it covers all the guiding questions and every success criterion. Where the teaching begins, the page quotes the learner's own Try first answer.

**How the page reacts**

- **Answers are checked where they are given.** The page's own code checks choices, values and operations on the picture. A written answer (the learner's statement of the idea, the open parts of a test) is sent to the model with the design's marking and success criteria as the rubric. The reply is a verdict (lesson-flow 3.1) and at most two or three sentences, shown in place. In a Socratic step the reply to a weak statement is one narrowing question. It never states the idea.
- **The model's feedback never gives the answer away.** The judging prompt tells the model to name what is right and ask one guiding question about what is missing. It never states the correct values and never writes a model answer, because the learner can try again. When a statement misses several points, the prompt says which one to ask about first.
- **A wrong answer never blocks.** The page reacts visibly to every answer. A wrong choice is marked and its feedback appears at once. The first wrong answer gets a hint that says what to look at or what to compute. From then on a button, "Show me the answer and go on", is always there. It marks the right answer, explains it and opens Next. A step that asks the learner to operate the picture (sliders, a drag) shows its hint from the start and offers to set a working state. A written answer judged not enough can always be passed with "Go on". An answer shown by the page is saved as shown, so the lesson counts it as something to work on (lesson-flow 2.7).
- **Progress toward a target is shown live.** A step whose target the learner reaches by operating the picture says how close they are at every moment ("2 of 3 nearest items are electronics, a little more Phones"), not only when they succeed.
- **Next always works and always moves forward.** On a finished step, Next looks ready and opens the step after it. On an unfinished step, Next looks waiting. Pressing it does not move: it says in one line what is still to do and brings up the way forward (the hint and "Show me the answer and go on"). A greyed-out button that does nothing is not allowed. Next never jumps backwards because another step looks unfinished.
- **Back.** Every step has a Back button. A finished step reopens with the learner's answer, its feedback and the picture as it was, and the learner may change the answer.
- **Contents.** A Contents button, always visible, opens the list of the lesson's steps with their state (done, next, locked). The learner can jump to any step already reached, and only to those. Below the list, the course's lessons, with this lesson marked.
- **Manual.** A Manual button, always visible, opens a reference the page writes as the lesson goes: the case; one section per finished step, stating what was found with the page's own numbers; the design's worked example; the learner's own statement and test answers with their feedback; the meaning of each word the lesson uses; the learner's notes. A section appears only when its step is finished, so the manual never gives an answer away. The page says how many sections are filled. The learner can save the manual as a file and copy its text.
- **Notes.** Each step has a small "My note for this step" box. Notes are saved and added to the manual.
- **Help without leaving.** A small "What does this word mean?" box asks the model for a definition under the term-helper's rules: the word only, no help with the exercise. A "Start from scratch" button on a test opens the full explanation (for a key idea, the levels from High school, with no trap named) on a case that is not the test's, then gives the test again. The page saves the choice as `start-from-scratch`.

**What the page saves**

- **Everything, after every step:** each answer, the number of tries, the written statements, the verdicts, and whether an answer was shown. The lesson copies this record into `state.attempts` when the learner comes back (lesson-flow 2.7).
- **Nothing is lost.** Save at every change of step and when the tab is hidden. Keep an instant copy in the browser as well as the shared record. On opening, use whichever is newer. Going back to a step never overwrites what its record says (for example, that its answer was shown).
- **The saved place.** On opening, the page reads the saved record before it shows any step or writes anything, then goes to the first unfinished step. Until the record is read, the page writes nothing: a freshly loaded page must never overwrite saved progress. If the record cannot be read within a few seconds, start from step 1 and say so.

**When Show you've got it fails**

The page never offers the same test again. A failed Show you've got it starts another round, and each round on the page counts as one of the two at most (lesson-flow 2.6).

1. The result screen names what to work on, item by item, each narrower than before.
2. The page reopens the teaching for those items only. A key idea goes back in at the first level not held.
3. The page gives a new case: different from Try first, from the failed case and from every case so far, at the same pass standard. New given values count as a new case only when they change the answer and the reasoning has to be done again. The page's own code computes every number in it.
4. The page writes the new case itself when it can: from the design's case family with new given values its code can compute, or by asking the model for a new case from the design and checking its numbers with its own code.
5. When the page cannot write a new case it can trust, it says so and sends the learner back to chat: "Write `/continue` in chat to go on with another round." The round then runs in chat.

The result screen also says the learner may stop instead and have the result recorded as it is. After the second round fails, the page offers no more rounds and shows the end screen. When a key idea's levels stopped short, the page gives Show you've got it at the level reached and offers no round (lesson-flow 2.1).

**The end screen** gives the result and one line: the lesson is saved, and writing `done` in chat records it and suggests the next lesson.

## 3. Three stages through chat

When the page cannot ask the model or cannot save, it is built in three stages. lesson-flow 2.7 says when each stage is built and what the lesson does with what comes back. The page is one file, delivered again at the same address as each stage is added. Earlier stages stay on the page, collapsed.

| Stage | Contains | Must not contain |
|---|---|---|
| 1. Opening | Why it matters and how we got here; the picture with the given values as live objects; the puzzle (Socratic course); Try first, one answer box per part; the two notes; the answers block | Any hint, expected answer, named trap, or part of the picture the test asks the learner to work out |
| 2. Learn | The sections of section 4; the results block | The answer to a check before the learner submits |
| 3. Show you've got it | The same picture with the new case's values; the test, one answer box per part, Part B (explain it back) in a Socratic course; the two notes; the answers block | Anything from stage 2 left open beside the test: collapse it |

After a failed Show you've got it, another round adds a new Learn stage for what is still to work on and a new stage 3 with a new case. The page never shows the same test again.

**One picture for the lesson.** All three stages are drawn on the same picture (`design.visual`, or the one the page draws for the lesson), with the part in use lit and the rest dimmed or covered. A test's given values are placed on the picture where they belong.

**The answers block** is plain text with a Copy button:

```
LESSON ANSWERS
Lesson <N>: <title> | <Try first / Show you've got it>
(a) <the learner's text>
(b) <the learner's text>
```

A learner who chooses start from scratch or asks what a word means does so in chat.

**The results block** ends stage 2. It is plain text with a Copy button:

```
LESSON PAGE RESULTS
Lesson <N>: <title>
<Level or check name>: <correct, N tries | not solved, N tries | not attempted>[, worked solution replayed]
(one line per level of a key idea, and one per check of any other section)
Level reached: <key idea only: the highest level solved with every level below it solved, or "none">
Stated idea: <Socratic course: the learner's own statement of the idea>
Q<n>: <Socratic course: the answer to guiding question n>, <N> tries
```

lesson-flow 2.7 says how the lesson reads both blocks.

## 4. What Learn contains

Learn has one section for each item to work on. The table below is the section for a key idea ★. The sections for other items follow it. Build every part from the lesson design. Every part has a source. Do not invent teaching content the design does not hold.

| Part of the page | Source | Rule |
|---|---|---|
| 1. The setup | `design.visual.objects` | The objects on screen, with their real numbers. Small enough to read at a glance. They appear in the order of `design.visual.steps` |
| 2. What you predicted | The learner's Try first answer | Quoted, with why it feels right. No second prediction is asked: Try first was the prediction |
| 3. The trap shown failing, then the aha | `design.trap`, `design.aha` | The learner's assumption shown failing on the Try first case, with the true result beside it. Then the aha, in its one sentence, set apart |
| 4. The picture | `design.picture`, `design.visual.colour_roles` | The picture drawn with the page's own objects. Say where it stops being true |
| 5. The levels | `design.worked_example`, `design.levels`, `design.visual.your_turn` | One tab per level, from the starting level to the lesson's level. Each tab: the level's solved example, then Your turn |
| 6. The control | `design.visual.control` | One thing the learner can change, and what to watch when they do |
| 7. Back to the lesson | -- | The results block and a Copy button, or, with the whole lesson on the page, the next step |

After start from scratch, leave out part 2 and the failing assumption in part 3: give the aha, the picture and the levels, and do not solve the Try first case.

When the levels start above High school, the page still shows parts 3 and 4 in short form, and the tabs start at the starting level.

In a **Socratic course** Learn opens with the guiding questions on the picture. Parts 4 to 7 stay closed until the learner has written the aha in their own words.

- Parts 2 and 3 come first, without the aha: the quoted prediction and its failure are the clash.
- One question on screen at a time, beside the part of the picture it is about. The next appears only after an answer.
- Each question is put as something to do wherever it allows: a value to enter, an object to move, a cell to pick, a choice among answers a learner would really give. An open question gets a text box.
- A wrong answer is not corrected. The page shows what that answer predicts on the picture, lets the prediction fail, and asks again. No question states the idea or contains its own answer.
- After the last question, a text box: "Say the idea in your own words." Submitting it opens parts 4 to 7. The statement and the answer to each question are saved, or go into the results block.

### Sections for other items

An item that is not a key idea gets a shorter section, with the same content as the explanation in chat (explaining skill), in this order:

| Format | The section shows |
|---|---|
| Short | The problem in two sentences, the principle, the worked example drawn with live objects, one check |
| Full | The same, plus the key formula with each symbol tied to an object on the page, how the principles connect as a small diagram, one check per success criterion (at most three) |
| Side by side | The two ideas on the same case, the cells where they differ outlined, one check that needs the difference |
| Start from scratch | The full explanation of the lesson's topic on a case that is not the Try first case, then one check per success criterion |

In a Socratic course each of these sections also opens with its guiding questions, by the rules above. The worked example and the checks open after the learner's own statement.

These items have no `design.visual`. Choose the objects from the item's worked example, with the table "Which widget for which field" below, and keep to one control per section. A Why it matters lesson has no formula: show the before and the after of the topic as two things the learner can operate and compare.

## 5. The `design.visual` field

A key idea's design carries `design.visual` with five parts:

- **`objects`**: what is drawn, with its size and exact values. Keep it tiny: 3 tokens in 2 dimensions, one qubit, a 10 by 10 grid of cases, five cash flows.
- **`colour_roles`**: one colour for each role an object plays (for example query, key, value). At most three.
- **`steps`**: the order in which the objects appear or change, each with the one sentence that goes with it.
- **`your_turn`**: for each level, what the learner types or picks, the right value, and the two most likely wrong values with what each one shows.
- **`control`**: the one slider, toggle or drag the learner can use, and what it shows.

When a key idea has no `design.visual` (an older course), derive one from `design.picture` and the solved examples, save it in `design.visual`, and tell the learner the page was designed during the lesson.

### Which widget for which field

| Subject | Objects | Typical control |
|---|---|---|
| Linear algebra, machine learning | Small matrices as heatmaps, cell by cell | Run more steps; change one entry |
| Quantum mechanics, geometry | An arrow on a circle or sphere, with its projections | Rotate the arrow or the measuring axis |
| Probability, statistics | A grid of dots, one per case, coloured by outcome | Change the base rate |
| Calculus, physics | A curve with a movable point and its tangent or area | Drag the point |
| Finance | A cash-flow timeline with bars | Change the rate |
| Cost estimation, scheduling | A breakdown table that sorts and sums; a schedule bar | Change one quantity or rate |
| Law, procedures | A timeline or decision path with the rule at each branch | Change one fact of the case |

A subject with no natural picture gets a worked table and a step-by-step replay, never decoration.

## 6. Rules for the page

**Numbers**
- The page's code computes every number on the page from the given values. Never type a result in by hand.
- Before delivery, run the page's computation once outside the page and compare it with the design's solved examples (`design.worked_example`, `design.levels`). Check a gradient or a derivative against a finite difference. A page that disagrees with the design is not delivered: fix the page, or correct the design and say so. Where no code can be run, recompute each solved example by hand from the page's values.
- The solved example on the page uses the numbers on the page. When the design's example uses other numbers, keep its method and steps and recompute.
- Rounded numbers must still add up as shown: show enough decimals for the steps to work by hand.

**Colour**
- Colour by role marks whose object it is (a border or label). Colour by value marks the number (the cell fill). Never use the same hues for both.
- Values use a diverging scale around zero: two hues plus neutral, readable without colour (the number is always printed in the cell).
- Mark the cells an explanation talks about with an outline, never with colour alone.

**Interaction**
- Hovering, tapping or focusing a cell shows the formula that produced it, with numbers, and outlines the cells it came from.
- Each Your turn takes one answer. Right: show the complete worked solution, ending with a Check. Wrong: when the wrong value is one listed in `design.visual.your_turn`, name what it shows. Then replay the solved example one step at a time, each step outlining its cells. This replay is the page's step back. The learner may then try again.
- The answer to a Your turn is never visible before the learner submits. Where the page shows a full matrix, ask for a value the learner must compute or find by reasoning, and say plainly when the page's own display is the check.
- One control, never a dashboard.

**Form**
- One page per lesson. No external data, and no library the page cannot work without. It reads on a phone (about 400 px wide) without sideways scrolling, in light and dark themes.
- Short sentences beside the objects. The page is not a chat explanation pasted into boxes: a paragraph that needs more than three sentences belongs in chat.
- The glossary words throughout.
- Progress kept in the browser is a convenience only. The saved record, or the results block, is what counts.

## 7. Delivering the page

1. Write the page to `lessons/<NN-slug>/page.html` in the course folder. List it in `files` with kind `lesson-page`, the lesson id, a plain title and today's date. A page already listed only gets a new `updated` date.
2. If the environment has a tool that publishes a page and returns a link, publish with it and follow that tool's page rules. Otherwise write a complete HTML document and tell the learner to open the file in a browser.
3. In chat, say in two or three lines what the page or the stage is, how long it takes, and what comes back to chat (`done`, or the answers block or results block). Then wait.
4. With three stages, add each new stage to the same file and deliver it again at the same address.
5. If no page can be delivered (no file access, or the learner cannot open one), say so. The lesson runs that part in chat (lesson-flow 2.7, Falling back).

## 8. Examples

`examples/query-vs-key.html` is a complete Learn section for one key idea: in self-attention, the query and key matrices get different gradients even when they start identical. It shows the setup, the prediction, the aha moment, the picture, one tab per level with a solved example and Your turn, the control, and the results block. Read it for the structure and the amount of text. Do not copy its subject. It was built to stand alone, before version 4. So it asks for its own prediction, shows only Learn. A page built in a lesson has all the parts, quotes the learner's Try first answer, and uses the blocks of section 3.

`examples/why-attention.html` is a page for a Why it matters lesson with no formula: a start-from-scratch explanation of why attention replaced recurrent reading. It has three things to operate (how far information travels, how the right word is found by its content, what it costs) and three checks.

The `design.visual` of the first example, as `course.json` would hold it:

- **`objects`**: 3 tokens in 2 dimensions. X (3×2), W_Q = W_K = [[1, 0.5], [−0.5, 1]], W_V, target T; the forward pass Q, K, S, P, O and the loss; the gradients dS, dQ, dK, dW_Q, dW_K.
- **`colour_roles`**: query purple, key teal, value ochre. Cell fill: blue negative, orange positive.
- **`steps`**: the setup, then the learner's prediction, then the two gradients side by side with the differing cells outlined, then dS read by rows (query) and by columns (key).
- **`your_turn`**: High school: read P[3,1] (0.23; 0.41 means the row and column were swapped). Master's: compute dK[2,1] (−0.39; −0.07 means dS was read along the row; −0.55 means the √d was dropped). Advanced: the factor on dW_K when W_Q is doubled and W_K halved (2; 0.5 is the factor on dW_Q).
- **`control`**: a slider that runs 0 to 40 gradient steps and shows the two matrices and the distance between them.

## Older names

Earlier versions used other words: session (lesson), sub-goal and SG (Lesson N), blueprint (lesson design), hard core or hard-core (key idea), tempting answer (the trap), insight (the aha), reveal (the aha moment), rung and climb (levels), bridge (step back), gap (what to work on), Initial Test and Final Test (Try first and Show you've got it), Quick Check (check), CTQ (success criteria), Discovery Question (puzzle), Guidance Chain (guiding questions), tension and resolution (the clash and the way out), reconstruct the reasoning (explain it back), "not familiar" (start from scratch), clarification (what does this word mean?), checkpoint (saved place), transcript (attempts), learner profile (your progress), concept file (lesson notes), exercise book (practice book), plan (course), Estimated Depth (level), artefact (file).
