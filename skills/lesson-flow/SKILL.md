---
name: lesson-flow
description: How a lesson runs, from finding the course and the lesson to closing it - Open, Try first, Judge, Learn, Checks, Show you've got it, Judge, Close - with the variations for the Socratic and Direct methods, key ideas, start from scratch, page or chat delivery, a named level, resuming and another round. Use when running, resuming or finishing a lesson, and for /continue.
---

# Lesson Flow

This skill owns how a lesson runs. Other skills own the rest:

- **course-model**: the data in `course.json` and how to save it (its section 3). Every "Save" line below is written the way that section says: read the whole file, change the fields named, write it back, validate, regenerate `overview.md`.
- **explaining**: how explanations, worked examples, the content of each level, lesson notes, practice books and idea maps are written.
- **visual-explainer**: how a lesson page is built.
- **term-helper** (agent): definitions for "what does this word mean?".

The lesson writes nothing outside the course folder and no other state file. Everything it remembers is in `course.json`.

## 1. The one flow

Every lesson runs the same eight steps in this order:

**Open → Try first → Judge → Learn → Checks → Show you've got it → Judge → Close**

Section 2 lists what changes for each method, kind of lesson and delivery. Section 3 says how answers are judged.

### Getting ready

1. **Find the course** as course-model section 6 says. A course folder or `course.json` named in the request wins. Otherwise look for `*/course.json` and `course.json` in the working folder; with several, list their titles and ask. With none but a version 3 course file (`*_training_plan.md`), convert it (course-model section 7), tell the learner in one line that it was converted and the old file kept, and go on with the new course. With neither, tell the learner to create a course first.
2. **Bring in the course app.** If `course.app_url` is set, first bring in what the learner did on the app since the last time (course-app skill, section 4): new answers, lessons started or closed, answers left `unmarked` (mark them now, section 3). Then choose the lesson with that state.
3. **Read the method** from `course.method` (`socratic` or `direct`) and the level from `course.level`.
4. **Choose the lesson** from the request:
   - a number ("2", "lesson 2"): that lesson;
   - words: the lesson whose title or goal matches best;
   - nothing: the next lesson (`python3 course.py next-lesson <course>/course.json`, or course-model section 5 by hand);
   - unclear: show the lesson list and ask.
5. **Read the extra words** of the request: `chat` (deliver in chat), a level name (High school, Master's or Advanced; see Level named in the command), `visual` or `graphic` (accepted; they change nothing).
6. **A lesson already done**: ask "Lesson <N> is done. Do it again?" On yes, start it like a new lesson. Earlier attempts stay in `attempts`; set `rounds` to 0.
7. **A lesson in progress** was interrupted: see Resuming an interrupted lesson (section 2.5).

### Step 1. Open

The lesson opens with why it matters and the real story behind it, before any question. It takes a minute or two.

1. **Why it matters**: what this lesson lets the learner do, and where it sits in the course. One or two sentences.
2. **How we got here**: the real situation the idea came out of. What people did before, where that broke down, who changed it and when. Names and dates only when certain.

Take both from the lesson's `design.context`, the course's `story` and its `overview`.

- The opening sets the scene and stops before the idea. It states no answer to the lesson's questions and solves no test case.
- It is true. No invented method, and no simplified history told as fact.
- A lesson with no `design.context` (an older course): write one from `story` and `overview`, save it in `design.context`, and tell the learner.
- On a page, the opening is the first two steps of the page: "Why this matters" and "How we got here", as something the learner can operate (a timeline, a before and after).

**Save** when the lesson starts: `status: in-progress`, `step: try-first`, `started`, `delivery` (`app` for a page, `chat` for chat).

### Step 2. Try first

Give the test from `design.try_first.question`, before any teaching.

- **Nothing before it.** The opening has set the scene. Add no theory, no hint and no warm-up.
- **A clear question.** Each part asks one thing and says in what form the answer is expected. Rewrite a design question that does not, keeping what it tests.
- **A true case.** If the case rests on an invented method, or on a statement that is false outside the toy example, replace it with the real case from the story. Note the change in `state.notes`.
- Start straight with the case. Give it a heading and put the task in bold.
- End with the two notes of section 3.4.
- Wait for the answer. Do nothing else until it comes.

During Try first the learner may ask what a word means (section 4.1) or choose to start from scratch (section 2, Start from scratch).

**Save** when the answer arrives and before it is judged: the answer in `saved`, so an interruption does not lose it.

### Step 3. Judge

Judge the answer against `try_first.marking.pass` and the lesson's `success_criteria`, as section 3 says.

- Say what was right and what was missed, and give the verdict plainly, with the reason.
- **Pass**: go to Close (see Passed Try first in section 2 for what comes first).
- **Partial or fail**: list each thing to work on, with its kind of common mistake, and go to Learn.
- **Trap**: say that the answer does not hold and name what to work on. Keep the right answer for Learn.

**Save**: one entry in `attempts` (step `try-first`, the answer in full, the verdict, one line of feedback, `source`); `to_work_on` with each item and its kind; `step: learn` (or `record` after a pass); `saved` with what Learn needs (the order of the blocks, and for a key idea the starting level).

### Step 4. Learn

Teach only what to work on, one thing at a time, in the order listed.

- Choose the format for each item as section 3.3 says. Write the content as the **explaining** skill says, at the lesson's level.
- One explanation per item. Never combine two items in one explanation.
- Every explanation, whatever its format, contains one fully worked example ending with a Check that confirms the result a second way.
- Each explanation is followed by its check (Step 5) before the next one starts.
- **Go deeper.** After the first explanation, say once: "You can ask me to go deeper on any idea I just explained." When the learner asks, give the fuller explanation (explaining skill), at most one per explanation, then return to the next item. Never repeat the offer.
- **Idea map.** When every item is taught and checked, offer once: "Would you like an idea map of this lesson before Show you've got it? It is optional: it shows how the ideas connect." On yes, make it as the explaining skill says, with every item taught on it (a side-by-side map after a side-by-side comparison). On no, go on. Never insist.

**Save** after each explanation and its check: `saved` with the items taught, the format of each, and for a key idea the levels held so far.

### Step 5. Checks

Each explanation ends with a short check built from the success criteria.

- End the check with: `*If a word in this question is unclear, ask **what does this word mean?***`
- Wait for the answer. Never show the expected answer, or a hint of the mistake to watch for, before it.
- After the answer, show the complete worked solution, every step with its why, ending with a Check. Then judge it.
- **Right**: go to the next item.
- **Wrong**: **step back**. Explain the point that failed one level down (a Master's explanation at High school level, an Advanced one at Master's level; at High school level, with a different picture or example). Then give one more check at the original level.
- **Wrong again**: the item stays unresolved in `to_work_on`. Go to the next item. Never loop on checks.

**Save** each check: one entry in `attempts` (step `check`, or `your-turn` with its `level` for a key idea, or `guiding-question` for a Socratic question); `step: check` while a check waits for its answer, then back to `learn`; `level_reached` as each level of a key idea is held. When the last item is done: `step: final-check`.

### Step 6. Show you've got it

Give the test from `design.final_check.question`: a new case, different from Try first, testing the same success criteria to the same pass standard.

- Straight to the case, with no preamble.
- The same rules as Try first: a clear question, a true case, the two notes of section 3.4, wait for the answer.
- "What does this word mean?" works here exactly as in Try first.

**Save** when the answer arrives: the answer in `saved`.

### Step 7. Judge again

Judge against `final_check.marking.pass` (and `explain_it_back` in a Socratic course), as section 3 says. After the answer, show the complete worked solution.

- **Pass**: go to Close.
- **Not passed**: name what is still to work on, with its kind, and start another round (section 2.6). After the second round, go to Close.

**Save**: one entry in `attempts` (step `final-check`); the items fixed marked `resolved`, new items added to `to_work_on`; `rounds` + 1 when another round starts; `step: record` when the lesson goes to Close.

### Step 8. Close

Close the lesson as section 5 says.

## 2. Variations

Each row changes only the cells it fills. An empty cell means the step runs as section 1 says.

| Variation | Open | Try first | Learn | Show you've got it | Close |
|---|---|---|---|---|---|
| **Socratic method** (`course.method: socratic`) | Then the puzzle (`design.puzzle`), headed **Puzzle**, before the test | The test is built so the natural first attempt fails (`try_first.marking.trap`). Never warn the learner | Each item is reached through guiding questions (2.2). At Judge, name the clash and keep the way out | Adds **Part B**, explain it back (2.2) | |
| **Direct method** (`course.method: direct`) | | | Each item is explained directly, in its format (3.3) | | |
| **Key idea** ★ (`key_idea: true`) | | The test is built so the natural answer is the trap. No warning and no hint that the obvious answer is wrong | The key idea itself is taught as one block: the aha moment, then level by level (2.1). Other items follow as their own blocks | At the course level, or at the level reached when the levels stopped short | `level_reached` is written. Stopped below the course level: `review` |
| **Start from scratch** (the learner asks to be taught first) | | Answered with the verdict `start-from-scratch`. Check `needs` and background first (2.3) | A full explanation of the lesson's topic with its check; a key idea from the High school level with no trap named. Then Try first again | | This counts as teaching: lesson notes are written |
| **Passed Try first** | | | Skipped. A principle lesson shows its worked example for reference. A key idea gives a recap and one offer (2.4) | Skipped | `done`. No lesson notes unless the learner took the offer of more |
| **Lesson kind why or capstone** | A why lesson's opening carries the whole story of the course | | | | No practice book |
| **Delivery: page** (default) | The page's first two steps | Stage 1 of the page; nothing on it teaches | Stage 2 of the page | Stage 3 of the page | The page is listed in `files` (kind `lesson-page`). Section 2.7 |
| **Delivery: chat** (`chat` in the request, the learner asks, or no page can be delivered) | In chat | In chat | In chat | In chat | `delivery: chat` |
| **Level named in the command** | Say the lesson runs at that level, and that the course design is unchanged | The design's test re-pitched to that level: same family of cases, that level's tools | Explanations at that level. A key idea goes up to that level; a level above the course level gets a worked example written now in the same format | Re-pitched to that level | `state.notes` names the level the lesson ran at |
| **Resuming an interrupted lesson** (`status: in-progress`) | Skipped when resumed | Continues at the saved place (2.5) | Items already taught are skipped. A key idea goes on at the level after the last one held | | Steps whose result already exists are skipped |
| **Another round after a failed final check** | | | Only the items still to work on. A key idea goes back in at the first level not held (2.6) | A new case each round. At most two rounds | `review` when the second round fails |

### 2.1 The key idea: the aha moment and level by level

A key idea has `design.trap`, `design.aha`, `design.picture`, a worked example (the High school level) and one solved example in `design.levels` for each level above High school up to the course level. The explaining skill writes the content of each level. This section runs it.

**Judging Try first.** Note which case the answer shows:

- **Fell for it**: the answer is the trap or a variant of it. Verdict `trap`.
- **Has the idea, below the level**: the answer avoids the trap and is right in substance, but its reasoning is below the lesson's level (right in words, missing the maths). Verdict `partial`, kind `words-without-maths`.
- **Passed**: right, and justified at the lesson's level. Verdict `pass`.

**Starting level**, written in `saved`:

- Fell for it, or unsure which case applies: High school.
- Handles the symbols but misses the idea (`maths-without-picture`): High school.
- Has the idea, below the level: the first level above High school.

**The aha moment is the High school level.** In this order:

1. What the learner assumed, in their own words, and why it feels right.
2. That assumption shown failing on the Try first case, with the true result beside it.
3. The aha, in its one sentence.
4. The picture, and where it stops being true.
5. The worked example, step by step.
6. The Try first case redone correctly with the aha.

When the levels start above High school, give items 3 and 4 only, as a two-line reminder, then start at the starting level. After start from scratch, leave out items 1, 2 and 6: the learner made no prediction, so name no trap and solve no part of the Try first case, which comes again afterwards.

**Each higher level** gives the idea at that level (Master's: the formal statement, where it comes from, the key equations; Advanced: full generality, the proof or derivation, the limits), then that level's solved example from `design.levels`, step by step.

**Every level ends with Your turn.** It is that level's check and follows every rule of Step 5: a new exercise at the level, on a case used nowhere else; the word note; no answer before the learner's; the complete worked solution after.

- **Method right** (an arithmetic slip does not count against it): the level is held. Write `level_reached` and go up.
- **Method wrong**: step back. A few lines, one level down, that tie the failed step to the level below (at High school, a different picture). Then one new exercise at the same level.
- **Wrong again**: stop. The level reached is the last level held, or `below-high-school` if none was.

A level has at most two exercises. Stopping is not another round. When the levels stopped short, Show you've got it is given at the level reached (re-pitched to High school if no level was held). Whatever its result, no round follows: the status is `review`, and the notes record the level reached against the lesson's level ("High school of Master's"). Tell the learner what they now hold and which level to come back to.

**In a Socratic course** the levels are the same and are reached through questions:

- High school level: name the clash, then use the guiding questions so that the learner states the aha. Show the picture and the worked example only after the learner has stated it, or the questions have run out.
- Each higher level: before showing anything, ask the learner to try the statement at that level ("How would you write that as an equation?", "What would a proof have to show?"). Then confirm it and show the level's solved example.
- A wrong Your turn: no direct step back. Go back to questions pitched one level down, then give the new exercise.

### 2.2 The Socratic method: guiding questions

The Socratic method keeps the eight steps and changes how Learn is delivered. The puzzle and Try first are where the learner meets the clash; the guiding questions are where they find the way out; Show you've got it tests it.

**At Judge**, say whether the answer took the designed wrong path (`try_first.marking.trap`). If it did, verdict `trap`, and name the clash: "Your answer assumed [X]. That is exactly the clash this lesson is about: [why it fails]." Do not give the way out yet.

**In Learn**, for each item:

1. **Recall the clash**: what failed and why. No answer yet.
2. **Ask the guiding questions** from `design.guiding_questions`, one at a time. Wait for each answer. Adapt the next question to it. Each question narrows the search without giving the answer, and the last one leaves only one conclusion. When the learner reaches the idea at any point, confirm it and go to 3. When the questions run out and the learner is still stuck, say "Here is where the questions were leading:" and state the idea.
3. **The way out**: the idea appears as the only way out of the clash. Let the learner say it ("So the only operation that gives this is...?"), or name what they found ("You just showed that [their reasoning]. That is [the idea].").
4. **The worked example** comes after the way out, never before it.
5. **The check** asks the learner to explain back: "Now explain back why [idea] is the only way out of the clash we started with." Then the complete worked solution.
6. **A failed check**: no direct explanation. Go back to the question where the reasoning broke, and ask a different narrowing question there, one level down (plainer words, concrete numbers) when the lesson is above High school.

How to ask:

- Never state an idea before the learner has tried to reach it.
- Never put the answer in the question. "Isn't it true that X?" and "Can you see that X?" are not guiding questions.
- Ask real questions with room to search: "What would happen if we tried your approach on [this case]?", "Why can't we just [simpler wrong method]?", "What have we not used yet?", "If your answer were right, what would follow for [this]?"
- A wrong answer is not corrected. Ask "What does that predict for [this case]?" and let the prediction fail.

**Show you've got it** adds:

> **Part B:** Explain why your approach works. What would go wrong if you used [the wrong path from Try first] instead?

Part B counts as much as Part A, against `final_check.marking.explain_it_back`. Part A right without Part B is `partial`.

**Another round** in a Socratic course: the first round uses new guiding questions aimed at what is still to work on, with no direct teaching. In the second round, if the learner is still stuck when the questions run out, give a short direct explanation, say "The questions were not enough here, so here is the idea explained directly.", and note it in `state.notes`.

### 2.3 Start from scratch

The learner writes "start from scratch", or says the same in other words ("I don't know this topic", "never learned this").

1. **Lessons it needs.** If a lesson in `needs` is not done, offer to do that lesson first.
2. **Missing background.** If a principle of this lesson needs background (`principles[].needs`, `background`) that no lesson teaches, offer:
   > "This lesson relies on **[background]**, which the course does not teach yet. You can:
   > - **A)** Add a background lesson on it and do that first
   > - **B)** Start this lesson from scratch now"

   On A, add a background lesson (section 4.2). On B, go to 3.
3. **Teach from scratch.** Give the full explanation of the lesson's topic at the lesson's level, on a case that is not the Try first case, with its check. A key idea gets its levels from High school instead (2.1, without the trap). Then give Try first again.

This is not another round. **Save**: an entry in `attempts` with the verdict `start-from-scratch`, and `to_work_on` with the topic, kind `missing-background`.

### 2.4 Passed Try first

- **A principle lesson**: say "You have shown you have this principle. Here is a worked example for reference:" and show `design.worked_example`. Then Close.
- **A key idea**:
  1. Recap: "You have this. Here is the idea in one line and one worked example for reference:", then the aha, the picture, and the solved example of the top level in `design.levels` (at High school level: the worked example).
  2. Make one offer and follow the learner's choice: all the levels from High school; or the next level up, when the lesson is below Advanced (the idea at that level, a solved example written now, a Your turn); or neither.
  3. A recap alone is not teaching: no lesson notes. An accepted offer is teaching: lesson notes are written. The pass stands either way, and the status does not depend on how the extra levels go.
  4. Then Close. A lesson interrupted after the offer resumes at Close.

### 2.5 Resuming an interrupted lesson

1. Show what was done: the saved place (`state.step`), the attempts so far, what to work on, and `state.saved` (items taught, levels held, a check or page stage waiting for an answer).
2. Ask: "Lesson <N> stopped at <step>. Pick up where you left off?"
   - **Yes**: continue at the saved place. Skip the items already taught; a key idea goes on at the level after the last one held; at Close, skip every step whose result exists.
   - **No**: set the lesson back to `not-started` with no attempts and no saved place, and start fresh.

### 2.6 Another round, at most twice

After a failed Show you've got it:

- **Round 1**: teach again, narrower: only the items still to work on, by the rules of Learn and Checks. Then a new Show you've got it case, different from every case so far, at the same pass standard.
- **Round 2**: the same once more, if round 1 failed.
- **After round 2 fails**: no more rounds. Say: "Lesson <N> needs more work. Come back to it after going over its background again, or with someone who can help in person." The status is `review`.

A key idea goes back in at the first level not held. A key idea whose levels stopped short gets no round (2.1). Start from scratch and a step back are not rounds.

### 2.7 Page delivery

By default the learner works on one lesson page from the first minute to the last. The **visual-explainer** skill builds the page. This section says when it is built, what comes back and how it is read. Chat carries only what the page cannot do: judging written answers, word definitions, go deeper, and the few lines that hand the learner back to the page.

**The course app (the default where pages can be published).** When a published page can ask Claude and save data the lesson can read back, the lesson runs in the **course app** (course-app skill): one page for the whole course, where each lesson was prepared in advance as a `lesson.json` (lesson-content skill). `/continue` then does not run the lesson in chat: it brings in the learner's work (Getting ready, step 2), makes sure the next two lessons are prepared, rebuilds and republishes the app, and gives the link with the lesson to open. Everything this skill says about each step still holds; the prepared lesson must follow it, and the app saves each answer as an attempt.

**The whole lesson on one page** (when the app cannot be used but a single page can ask and save): build all three stages at once (visual-explainer: "the whole lesson on the page").

- Because the teaching is built before the learner answers, it covers all the guiding questions and every success criterion. The page quotes the learner's Try first answer where the teaching begins.
- The page checks answers in place and saves every answer, the number of tries, the written statements and the verdicts.
- An answer the learner asked the page to show ("Show me the answer and go on") is saved as shown. It is judged `skipped` and counts as something to work on.
- A retry of Show you've got it offered by the page counts as one of the two rounds.
- The learner comes back to chat at the end and writes `done`. Read the saved record, confirm or correct each verdict against the design's marking (the lesson's judgement is final), and go to Close. Never ask the learner to repeat anything the record holds.

**Three stages through chat** (when the page can neither ask nor save):

| Stage | Built when | The page shows | What comes back |
|---|---|---|---|
| 1. Opening | At the start, before anything else | Why it matters and how we got here, the lesson's picture, the puzzle (Socratic), Try first with one answer box per part, the two notes | The answers block |
| 2. Learn | After Try first is judged | One section per item to work on. Socratic: the guiding questions on the picture, the learner's own statement of the idea, then the picture, worked example and checks. A key idea: one tab per level | The results block |
| 3. Show you've got it | After the results block is read and confirmed | The same picture with the new case, one answer box per part (and Part B in a Socratic course), the two notes | The answers block |

- Stage 1 shows nothing that teaches: no hint, no expected answer, no named trap, no part of the picture the test asks the learner to work out.
- The page is written to `lessons/<NN-slug>/page.html`, listed in `files` (kind `lesson-page`), published when the environment can, and delivered again at the same address after each stage.
- In chat, say in two or three lines what the stage is and what comes back. Then wait. **Save** `saved: stage <N> delivered, answers pending`.
- The learner may write "start from scratch", ask what a word means, or answer any stage directly in chat.

**Reading what comes back.**

- An **answers block** is judged exactly like a chat answer (Step 3, Step 7), in a few lines of chat.
- A **results block** is read line by line:

| On the page | In the lesson |
|---|---|
| Correct at the first try | Check passed; a level held |
| Correct after the solution was replayed | Passed after a step back; a level held after a step back |
| Not solved | Still to work on; a key idea's levels stopped here |
| Not attempted | Ask whether to continue on the page or in chat |

- Judge the learner's own statement of the idea (Socratic) in chat.
- Confirm with one short question in chat on the highest level reported, or on the hardest check. A wrong answer means that level or check is not held. A learner who cannot copy the block is asked what they reached, then the same question.
- Every answer read from a page goes into `attempts` with `source: app`.

**Falling back.** If the page cannot be built or opened, say so, run that part in chat and save `delivery: chat`.

## 3. Judging answers

### 3.1 Verdicts

| Verdict | When |
|---|---|
| `pass` | The answer meets the marking's pass standard (and, in a Socratic Show you've got it, explain it back as well). A Your turn passes when the method is right, even with an arithmetic slip |
| `partial` | Some of the standard is met. A Socratic Part A right without Part B is partial |
| `fail` | The main point is missing or wrong |
| `trap` | The answer is the design's trap (`try_first.marking.trap`) or a variant of it |
| `skipped` | The learner gave no answer, or asked the page to show it |
| `start-from-scratch` | The learner chose to be taught before trying |

Each judged answer gets one line of feedback and one entry in `attempts`, with the learner's answer in full.

### 3.2 Common mistakes

Name each thing to work on with the kind of common mistake it shows, using the lesson's `success_criteria[].common_mistake` as the first guide:

| Kind | Field value | The learner |
|---|---|---|
| Mixing up two ideas | `mixing-up` | treats two related ideas as one |
| Stretching a rule too far | `overstretching` | uses a rule beyond where it holds |
| Missing background | `missing-background` | lacks knowledge the lesson assumes |
| Steps without the why | `steps-without-why` | runs the method and cannot say why it works |
| Words without the maths | `words-without-maths` | says it right and cannot write it formally |
| Maths without the picture | `maths-without-picture` | handles the symbols and misses the idea |

A plain slip (an arithmetic error, a wrong unit) has no kind (`kind: null`).

### 3.3 Choosing the teaching format

Choose the format for each thing to work on before teaching it:

| Thing to work on | Format |
|---|---|
| A slip with no kind | **Short**: the problem, the principle, a worked example, a check |
| Any kind except mixing up, or a kind that recurs in two or more lessons of the course (from their `to_work_on`) | **Full** explanation |
| Mixing up two ideas | **Side-by-side comparison**: what they share, where they differ, one case worked under both, a check that needs the difference |
| The key idea itself | **Levels**: the aha moment, then level by level (2.1), whatever its kind |

The explaining skill writes each format. Every format has one fully worked example ending with a Check.

### 3.4 The two notes every test ends with

Try first and Show you've got it always end with these two notes, word for word:

> *If this is new to you, write **start from scratch** and you will be taught it before you try.*
>
> *If a word in this question is unclear, ask **what does this word mean?** I will explain the word without helping you solve the problem.*

Every check and Your turn ends with the second note in short form: `*If a word in this question is unclear, ask **what does this word mean?***`

### 3.5 Answers hidden before, solutions shown after

- Never show an expected answer, a hint of the mistake to watch for, or the trap before the learner has answered. This holds for Try first, every guiding question, check, Your turn and Show you've got it, on a page and in chat.
- After the learner answers a check, a Your turn or Show you've got it, show the complete worked solution: every step with its why, ending with a Check. The bare expected answer is never enough.
- The Try first solution is given in Learn: in the aha moment for a key idea, after the way out in a Socratic course, inside the explanation otherwise.

## 4. Words and background

### 4.1 What does this word mean?

When the learner asks what a word means, during any question, call the **term-helper** agent with only:

1. the word;
2. the lesson's success criteria;
3. the course's principles;
4. the lesson's goal.

Never pass the question, the marking, the trap, `to_teach` or any worked example.

The term-helper answers in one of three ways:

- **The word is what the test checks**: it declines and suggests "start from scratch" if the learner lacks the background.
- **A context word**: a short definition with an example from another setting.
- **Missing background**: a definition, plus a note to the lesson. A minor note needs nothing more. A note that the word belongs to an earlier lesson not yet done means: at Judge, suggest doing that lesson first. A critical note, background no lesson teaches, means: offer a background lesson (4.2).

Show the definition and let the learner go on with the question. Several words may be asked about, one at a time. A word asked about is not a mistake and gets no verdict.

After the learner has answered the question (or chosen to start from scratch) following a critical note, offer:

> "You asked about **[word]**. It is background this course does not teach yet. You can:
> - **A)** Add a background lesson on it and do that first, then come back to this test
> - **B)** Carry on with this lesson as it is"

On A, add a background lesson (4.2). On B, carry on, and add the background to `to_work_on` with kind `missing-background`.

### 4.2 Add a background lesson

1. Save the place of the current lesson (`step`, `saved`).
2. Add a new lesson of kind `background`, with the next free number and its own full design, written by the rules the course was designed with.
3. Add the new lesson to the current lesson's `needs`.
4. Point the matching `background` entry's `lesson` at the new lesson, adding the entry if there is none.
5. Add a `history` line (`Lesson <M> added: background for Lesson <N>`), validate and regenerate the overview.
6. Run the new lesson through the whole flow. Then resume the current lesson at its saved place.

## 5. Close

Do these in order. When a lesson is resumed at Close, skip each step whose result already exists. Paths are inside the course folder; `<NN-slug>` is the lesson's folder (two-digit number and title slug).

1. **Status.** `done` when Show you've got it passed (or Try first passed). `review` when Show you've got it was not passed after the rounds, or a key idea stopped below the lesson's level.
2. **Level reached.** For a key idea: `level_reached` is the highest level held (`high-school`, `masters`, `advanced`, or `below-high-school`).
3. **The rest of the state.** `step: null`, `saved: null`, `finished: <today>`, each `to_work_on` item marked `resolved` when the last test showed it fixed, `notes` in one or two lines (the delivery, the worked example's role, the level the lesson ran at if named, anything to come back to). Add one `history` line: `Lesson <N> done` or `Lesson <N> needs review`. The attempts already hold every answer in full.
4. **Lesson notes**, when the lesson taught something (including start from scratch and an accepted offer after a pass): write `lessons/<NN-slug>/notes.md` in the format the **explaining** skill gives. It holds everything taught, the idea map if one was made, any go deeper, the success criteria and the lesson's opening. For a key idea: the aha moment, each level's explanation, and each Your turn with its worked solution. Worked examples that live in the design are referred to by level, not copied; a level written during the lesson is included in full. No notes after a pass with a recap alone.
5. **Practice book**, for lessons of kind `principle`, `concept`, `tool` and `background` (not `why` or `capstone`): add a set to `lessons/<NN-slug>/practice.md` in the format the **explaining** skill gives. Two fully solved exercises for each level from High school up to the course level, one standard and one with a twist; statements first, worked solutions after, each ending with a Check. No exercise repeats a test case, a worked example of the design or an exercise of this lesson. A `practice_task` in the design opens the set at the course level, solved. Append to an existing book; never replace it. Write the set whether or not the lesson taught anything.
6. **Other files**, only when the work calls for one: a reusable piece the learner built (a filled-in template, a calculation sheet, a checklist) goes to `lessons/<NN-slug>/<slug>.md`. Most lessons have none.
7. **Files list.** List every file the lesson wrote in `files` (kind `notes`, `practice`, `lesson-page` or `other`, with the lesson id, a plain title and today's date). A file already listed only gets a new `updated` date.
8. **Validate and render.** `python3 course.py validate <course>/course.json --files`, then `render-overview`. Fix any error before going on.
9. **Next.** Suggest the next lesson (`python3 course.py next-lesson <course>/course.json`). Mention `/practice <N>` for more solved exercises on this lesson and `/progress` for progress across courses. If the learner asks for a readable record of the lesson, write `lessons/<NN-slug>/record.md` from the attempts and list it (kind `record`).

## 6. Rules

- ALWAYS open with why it matters and how we got here, giving no answer away, then Try first before any teaching.
- ALWAYS end Try first and Show you've got it with the two notes of section 3.4, and every check and Your turn with the short word note.
- NEVER show an expected answer, a hint of the mistake to watch for or the trap before the learner answers. ALWAYS show the complete worked solution, ending with a Check, after a check, a Your turn or Show you've got it.
- ALWAYS wait for the learner's answer at Try first, each guiding question, each check, each Your turn and Show you've got it.
- NEVER give a question that asks two things at once or hides the form of the answer, and NEVER a case built on an invented method. Fix it first.
- ALWAYS judge explicitly: the verdict, its reason, and each thing to work on with its kind of common mistake.
- ALWAYS choose the format before teaching. One thing to work on, one explanation, one check, at a time. NEVER combine items.
- ALWAYS teach the key idea itself level by level. NEVER warn the learner about the trap before Try first, and NEVER skip the aha moment when they fall for it.
- A level has at most two exercises. Levels that stop short are recorded with the level reached and are not another round.
- At most two rounds after a failed Show you've got it. Each round has a new case.
- In a Socratic course, NEVER state an idea before the learner has tried to reach it, NEVER put the answer in a question, and NEVER correct a wrong answer directly: let its prediction fail.
- Offer go deeper once, after the first explanation. Offer the idea map once, after Learn. NEVER insist on either.
- Unless the lesson runs in chat, ALWAYS deliver the puzzle and Try first on the page, never as chat text.
- ALWAYS check the saved place before starting, and offer to resume a lesson in progress.
- ALWAYS save each step in `course.json` as course-model section 3 says, then validate and regenerate the overview.
- NEVER write any state outside `course.json`, and no file the course does not list.
- ALWAYS close the lesson: status, notes when something was taught, a practice set for the kinds that get one, every file listed.
- ALWAYS use the words of the course-model glossary in everything the learner reads.

## Older names

Earlier versions used other words for the same things: session or TTT session (lesson), sub-goal or SG-N (Lesson N), blueprint (lesson design), Initial Test / Teach / Final Test (Try first / Learn / Show you've got it), Quick Check (check), CTQ (success criteria), gap (what to work on), failure-mode tags (common mistakes), hard core (key idea), tempting answer (the trap), insight (the aha), reveal (the aha moment), climb, ladder and rungs (levels), bridge (step back), adaptation loop (another round), deep-dive (go deeper), "not familiar" (start from scratch), clarification and the term-clarifier agent (what does this word mean? and the term-helper agent), plan revision (add a background lesson), Discovery Question (puzzle), Socratic Guidance Chain (guiding questions), tension and resolution (the clash and the way out), reconstruct the reasoning (explain it back), checkpoint (saved place), transcript (attempts, or a lesson record on request), learner profile (your progress), concept file (lesson notes), exercise book (practice book), concept map (idea map), training plan (course).
