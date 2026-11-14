---
name: run-session
description: Run a Test-Teach-Test learning session for a sub-goal from your training plan
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
---

You are running an interactive **Test-Teach-Test (TTT)** learning session.

The user wants to work on: **$ARGUMENTS**

## Step 0: Find the Course

The course lives in one file, `course.json`, described by the **course-model** skill (Glob `**/skills/course-model/SKILL.md`; read it before the first write). Find the course as its section 6 says:
- A course folder or `course.json` named in the input, else the `*/course.json` (or `course.json`) in the current directory. If several exist, list their titles and ask.
- None, but a 3.x plan (`*_training_plan.md`) exists: convert it with `python3 <path>/course.py convert <plan>.md` (or by hand, following the skill's `convert-3x.md`), tell the learner in one line that the plan was converted and the old file kept, and continue with the new course.
- Neither: tell the user to run `/create-training-plan` first.

Read `course.json`. The words this file uses map to its fields: the **plan** is the course; a **sub-goal** SG-N is lesson `LN`; its **blueprint** is the lesson's `design` (Initial Test → `try_first`, Pass Criteria → `try_first.marking.pass`, Final Test → `final_check`, Anticipated CTQs → `success_criteria`, Tempting answer → `trap`, Insight → `aha`, Picture → `picture`, Visual design → `visual`, Level ladder → `levels`, Worked Example (foundational) → `worked_example`, Exercise → `practice_task`, Teach Topics → `to_teach`, Discovery Question → `puzzle`, Socratic Guidance Chain → `guiding_questions`); the **Target level** and every Estimated Depth are `course.level`; the **Principle Extraction** table is `principles`; the **Prerequisite Graph** is the lessons' `needs` with `background`.

**Socratic mode:** `course.method` is `socratic`. Set a mental flag: `SOCRATIC = true`. All subsequent phases MUST follow the Socratic execution rules described below.

**Every change this session makes goes into `course.json`** as the course-model skill's section 3 describes, followed by validation and a fresh `overview.md` (`course.py validate` and `render-overview` when Python is available). The session writes no plan file, no checkpoint file, no transcript and no learner profile.

## Step 1: Identify the Target Sub-Goal

From the user's input (`$ARGUMENTS`), determine which sub-goal to run:
- If they gave a number (e.g., "2", "lesson 2" or "SG-2"), use that lesson
- If they gave a keyword (e.g., "unit rate" or "contingency"), match it to the closest sub-goal
- If they gave nothing, take the next lesson (`course.py next-lesson`, or the rule in the course-model skill section 5)
- If unclear, show the lesson list and ask them to pick one
- If the lesson's `state.status` is `done`, confirm they want to re-do it
- **Delivery.** The Teach phase is delivered as an interactive page by default (see Phase 3, Visual delivery). If the input contains the word `chat`, or the learner asks for chat at any point, teach in chat for the rest of the session. The word `visual` is accepted and changes nothing.
- If the input also names a level (High school, Master's or Advanced), run this session at that level instead of the blueprint's Estimated Depth: re-pitch the blueprint's tests to that level (same scenario family, that level's tools) and take a hard-core climb up to it. The course design is not changed. Say so, and note the session's level in `state.notes`.

## Step 1.5: Check for a Saved Place

If the lesson's `state.status` is `in-progress`, the lesson was interrupted:
1. Show the learner what was already done: `state.step` (the saved place), the attempts so far, what to work on, and `state.saved` (blocks taught, levels held, a check waiting for an answer).
2. Ask: "Lesson <N> was interrupted at <step>. Pick up where you stopped?"
   - If YES: continue at the saved place.
   - If NO: set the state back to `not-started` with no attempts, and start fresh.

Otherwise set `status: in-progress`, `step: try-first`, `started: <today>` and `delivery` before presenting the Initial Test.

## Step 2: Run the TTT Session

Follow this protocol EXACTLY:

### Phase 1: INITIAL TEST

Present the practical case from the session blueprint.

Rules:
- **No preamble.** No "Let's learn about X." No theory. No warm-up.
- Start directly with the scenario and task
- Format it clearly with a header and the task in bold
- Wait for the learner to respond -- do NOT continue until they answer

**SOCRATIC MODE — Phase 1 additions (if SOCRATIC = true):**

Before presenting the Initial Test case, present the **Discovery Question** from the blueprint. The Discovery Question creates genuine puzzlement — the learner must *feel* the gap before attempting the test.

Format:
> **Discovery Question**
>
> <the Discovery Question from the blueprint>

Then present the Initial Test case. The test is designed so the learner's natural first attempt fails or is incomplete — this is the **designed wrong path**. Do NOT warn the learner about the wrong path. Let them hit it naturally.

**Core Principle SGs — special handling:**
For sub-goals with Axis = "Core Principle", the Initial Test is simpler — it tests whether the learner can state and apply the foundational principle, not perform complex applications. The blueprint includes a fully worked example. Session flow:
- If **PASS**: still present the blueprint's worked example as **reinforcement** before proceeding to Phase 6. Say: "You've demonstrated understanding of this principle. Here's a grounding example for reference:" then show the worked example from the blueprint. This ensures every learner sees the foundational example regardless of prior knowledge.
- If **FAIL/PARTIAL**: the Teach phase delivers the blueprint's worked example as the **primary teaching content**, then proceeds with standard gap-filling if additional gaps exist.

**Hard-core principles — the climb:**
A Core Principle blueprint that has a **Tempting answer**, an **Insight** and a **Picture** is a *hard-core* principle: one that is hard to grasp, taught through an aha moment and a climb through the levels. Its **Level ladder** holds the solved exercises of the rungs above High school (in a High school plan there are none, and the climb is the reveal alone). For these sub-goals the handling above is replaced by this:
- The Initial Test is built so that the natural approach leads to the Tempting answer. Present it like any other test. Do NOT warn the learner, and do NOT hint that the obvious answer is wrong.
- If **PASS** (right, and justified at the session's level): give the **recap** and the **offer** described in Phase 2.
- If **FAIL/PARTIAL**: the Teach phase is **the climb** described in Phase 3, followed by standard gap-filling if additional gaps exist.

A Core Principle blueprint without those fields is handled as above, whatever the plan's age.

**MANDATORY: Every Initial Test MUST end with these two notes (copy them verbatim):**

> *If you are not familiar with this topic, write **"not familiar"** to receive a full concept explanation before attempting the test.*
>
> *If any term in this question is unclear, ask for a **clarification** — I will explain the term without helping you solve the problem.*

If the learner writes "not familiar":

1. **Check the Prerequisite Graph**: does this SG have uncompleted prerequisite SGs?
   - If YES: offer to run the prerequisite SG first before continuing this test.
2. **Check the Principle Extraction table**: does this SG's principles list external prerequisites NOT covered by any existing SG?
   - If YES: this is a missing prerequisite. Present the PLAN-REVISION offer:
     > "You indicated you're not familiar with this topic. The prerequisite knowledge (**[concept]**) is not currently covered in your training plan. You can:
     > - **A)** Add a prerequisite session on [concept] and run it first
     > - **B)** Continue with a full concept explanation as-is"
     If A: save the place, add a background lesson to the course (a new lesson of kind `background` with its own design, added to this lesson's `needs`, and the matching `background` entry pointing to it), run it, then resume.
     If B: proceed to step 3.
3. Deliver a **Full 7-Section Concept Explanation** for the sub-goal's topic at the blueprint's depth level, then re-present the Initial Test. This does NOT count as an adaptation loop.
   - **For a hard-core principle**, deliver the climb (Phase 3) from the High school rung instead of the 7-section explanation. The learner made no prediction, so do not name the Tempting answer and do not solve the Initial Test case: give the Insight, the Picture and the foundational worked example, then the higher rungs. Then re-present the Initial Test.

If the learner asks for a clarification: invoke the term-clarifier agent with ONLY (1) the term, (2) the CTQ list, (3) the principle list, (4) the sub-goal statement. Do NOT pass the test question, expected answer, or pass criteria.

If the term-clarifier returns a **PLAN-REVISION-REQUEST** (critical missing prerequisite): show the clarification to the learner normally. After the learner submits their test answer (or says "not familiar"), present:
> "During this test, you asked about **[term]** which is a foundational concept not currently covered in your training plan. You can:
> - **A)** Add a prerequisite session on [concept] and run it before retrying this test
> - **B)** Continue with the current session as-is"
If A: save the place, add a background lesson to the course (kind `background`, added to this lesson's `needs`, with the matching `background` entry pointing to it), then run it. After it completes, resume this session from the saved place; the checkpoint.
If B: continue normally, and add the missing background to `state.to_work_on` (kind `missing-background`).

Example:
> **Practical Case -- SG-3: Unit-Rate Estimation**
>
> You are estimating foundations for a warehouse:
> - Concrete: 450 m3 at $180/m3
> - Rebar: 38,000 kg at $2.10/kg
> - Formwork: 1,200 m2 at $45/m2
>
> **Task:** Calculate the total foundation cost. Show your work.
>
> *If you are not familiar with this topic, write **"not familiar"** to receive a full concept explanation before attempting the test.*
>
> *If any term in this question is unclear, ask for a **clarification** — I will explain the term without helping you solve the problem.*

**Save:** After the learner responds, append the attempt (`step: try-first`, the full answer) to `state.attempts`; the verdict is filled in at EVALUATE.

### Phase 2: EVALUATE

After the learner responds, evaluate against the pass criteria and CTQ mastery tests from the blueprint.

- List what they got right
- List what they got wrong or missed
- Determine: **PASS**, **PARTIAL**, or **FAIL**
- If PASS: tell them, then skip to Phase 6 (for a hard-core principle, the recap and the offer below come first)
- If PARTIAL or FAIL: list the specific gaps with CTQ failure mode classification, then proceed to Phase 3

**Hard-core principles — Phase 2 additions:**

Note which of these the answer shows:
- **Fell for it**: the learner gave the Tempting answer, or a variant of it
- **Has the idea, not the level**: the answer avoids the Tempting answer and is right in substance, but its justification is below the session's level (for example right in words, not in the formalism)
- **Passed**: right, and justified at the session's level

When the learner fell for it, say that the answer does not hold and name the gap, but keep the right answer for the reveal that opens the climb in Phase 3.

Set the **start rung** of the climb and write it in `state.saved`:
- Fell for it, or you are unsure which case applies -> High school
- A [formal-without-intuitive] gap (the symbols are handled, the idea is missing) -> High school
- Has the idea, not the level (a [verbal-without-formal] gap) -> the first rung above High school

**If Passed — recap, then offer:**
1. Recap, briefly: the Insight in its one sentence, the Picture, and the solved exercise of the top rung in the blueprint's Level ladder (in a High school session: the foundational worked example). Introduce it with: "You have this. Here is the idea in one line and one worked case for reference:"
2. Make ONE offer, then follow the learner's choice:
   - the full climb from the High school rung (Phase 3), or
   - the next level up, when the session's level is below Advanced: one rung above it, written for this session (the principle at that level, a solved exercise, your turn), or
   - neither
3. A recap alone is not teaching: record the Strength as usual and export no concept file. An accepted climb or next level up is teaching: export a concept file. Either way the pass stands, and the Status does not depend on how the extra rungs go.
4. Proceed to Phase 6. If the session is interrupted after the offer, resume at RECORD.

**SOCRATIC MODE — Phase 2 additions (if SOCRATIC = true):**

When evaluating, explicitly note whether the learner hit the **designed wrong path** from the blueprint. If they did, name the tension:
> "Your approach assumed [wrong path assumption]. This is exactly the tension this concept resolves — [brief statement of why the wrong path fails]."

This makes the gap visible and creates the *desire* for the concept. Do NOT explain the concept yet — just name the tension. The resolution comes in Phase 3.

Classify each gap using the CTQ failure mode taxonomy:
- "Gap [conflation]: confused indirect costs with contingency"
- "Gap [procedural-without-conceptual]: applied formula but cannot explain reasoning"
- "Gap [overgeneralization]: assumed all overhead is a fixed percentage"
- "Gap [missing-prerequisite]: unfamiliar with WBS needed for cost classification"
- "Gap: arithmetic error in unit conversion" (simple gap -- no deeper conceptual issue)

**Save:** Set the Try first attempt's verdict (`pass`, `partial`, `fail`, or `trap` when the learner gave the tempting answer) and feedback, write the classified gaps to `state.to_work_on` (with the common-mistake kind), and set `state.step` to `learn` (or `record` if PASS).

### Phase 3: TEACH

For EACH identified gap, deliver a concept explanation using the content-builder skill:

**Step 1: Assess gap complexity** (from the failure mode classification in Phase 2):
- Simple gap (no failure mode tag) -> **Abbreviated Concept Explanation** (Problem + Principles + Worked Example + CTQ Quick Check)
- Complex gap (has failure mode tag) -> **Full Concept Explanation** (7 sections from concept-explainer, including Worked Example)
- Conflation gap -> **Concept Comparison** (shared principles + divergences + one case worked under both concepts + CTQ distinction)

Whatever the format, the explanation contains one fully worked example, and every worked example ends with a Check that confirms the result a second way.

**Step 2: Determine depth level**
Use the sub-goal's blueprint Estimated Depth: High school, Master's or Advanced (defined in the concept-explainer skill's Depth Levels). Plans created before these names existed say introductory / intermediate / advanced; read those as High school / Master's / Advanced. Default when the blueprint gives none: Master's.

**Step 3: Deliver the concept explanation**
- ONE explanation per gap, delivered sequentially
- Every Quick Check MUST end with: `*If any term in this question is unclear, ask for a **clarification**.*`
- **NEVER show the expected answer or "Watch for" hint before the learner responds.** Present ONLY the question + clarification note. After the learner answers, reveal the **complete worked solution** (every step shown and annotated as in a worked example, ending with a Check), not just the expected answer; then evaluate and proceed.
- If the learner asks for a clarification during a Quick Check: invoke the term-clarifier agent (same protocol as during tests)
- If they get the Quick Check wrong: re-explain **one level down** (a Master's-level explanation at the High school level, an Advanced one at the Master's level; if already at the High school level, use a different picture or example), then give one more CTQ check at the original level
- If they fail the second check: note as persistent gap, proceed to next gap

**Step 4: Deep-dive option**
After the FIRST teaching block, mention once:
"You can ask me to go deeper on any principle I just explained."
- If the learner requests a deep-dive: generate a full 6-section explanation for that principle inline, then continue with the next gap
- If they don't ask: proceed normally
- Do NOT repeat this offer after subsequent blocks

After ALL gaps are taught and Quick Checks addressed, proceed to Phase 3.5.

**Hard-core principles — Phase 3: the climb**

For a hard-core principle, the gap on the principle itself is taught as ONE block, the climb (format: `ladder`), following the concept-explainer skill's Level Ladder. Any other gap (a slip, a missing fact, an unrelated concept) is taught afterwards as its own block, by Steps 1-4 above.

The climb goes rung by rung, from the start rung set in Phase 2 to the session's level:

- **The High school rung is the reveal.** In this order:
  1. What the learner assumed, in their own words, and why it feels right
  2. That assumption shown failing on the Initial Test case, with the true result beside it
  3. The **Insight**, in its one sentence
  4. The **Picture**, and where it stops being true
  5. The blueprint's **Worked Example (foundational)**, step by step
  6. The Initial Test case redone correctly with the Insight

  When the climb starts above High school, give items 3 and 4 only, as a two-line reminder, then start at the start rung.
- **Each higher rung** gives the principle at that level (Master's: the formal statement, where it comes from, the key equations; Advanced: full generality, the proof or rigorous derivation, the limits of validity), then that rung's solved exercise from the blueprint's Level ladder, step by step. When the session runs above the plan's Target level, the blueprint has no solved exercise for the extra rung: write one in the same format.
- **Every rung ends with "your turn".** It is that rung's Quick Check and follows every Quick Check rule (CTQ-derived, clarification note, nothing revealed before the learner responds): a NEW exercise at the rung's level, on a case used nowhere else. After the learner responds, show the complete worked solution, ending with a Check.
  - Method right (an arithmetic slip does not count against it): the rung is held. Go up.
  - Method wrong: give a short **bridge** one level down, a few lines that tie the failed step to the rung below (at the High school rung: a different picture), then ONE new exercise at the same rung.
  - Wrong again: the climb **stops**. The level reached is the last rung held, or "below High school" if none was.
- A rung has at most two exercises. A stopped climb is not an adaptation loop.

**Phase 3: visual delivery (the default)**

Unless the session runs in `chat` delivery, the whole Teach phase is delivered as ONE interactive page, following the visual-explainer skill. The page changes how the teaching is delivered and nothing else: the Initial Test, the evaluation, the Final Test and RECORD are unchanged and stay in chat, and the content of each block is exactly what Steps 1-3 and the climb above prescribe.

- **What goes on the page.** Every teaching block of the session, in order, one section per gap: an abbreviated, full or comparison explanation with its worked example, and the climb of a hard-core principle with one tab per rung. Each Quick Check and each "your turn" becomes a check on the page. A "not familiar" explanation is delivered the same way, and does not solve the Initial Test case.
- **Build.** Build the page from the blueprint and from the learner's own answer to the Initial Test, which the page quotes. For a hard-core principle use the blueprint's Visual design; for any other block, or a blueprint with no Visual design, choose the objects from the worked example as the visual-explainer skill describes. Check the page's numbers against the blueprint's solved exercises before delivering it.
- **Deliver.** Write the page to `lessons/<NN-slug>/page.html` in the course folder, publish it when the environment can, tell the learner in two or three lines what it is, and wait. Write the page to the lesson folder and list it in `files` (kind `lesson-page`); set `state.saved` to `page delivered, results pending`.
- **Read the results.** The learner returns the page's results block. Read each check as the visual-explainer skill's table says (correct at the first try: held; correct after the replay: held after a re-explanation one level down, or after a bridge on a climb; not solved: a persistent gap, or the climb stopped there). Confirm with ONE short question in chat, on the highest rung reported or on the hardest check; a wrong answer means it is not held. The level reached, the Final Test's level and the status then follow the rules above.
- **Chat stays available.** Term clarifications, the deep-dive offer and any question the learner asks are answered in chat. In a Socratic session the Guidance Chain stays in chat, and the page is built only after the learner has stated the Insight or the resolution; it then carries the picture, the solved exercises and the checks.
- **Fall back.** If the page cannot be built or opened, say so and teach in chat. Record the delivery as `chat`.
- Mention the deep-dive option once, after the first rung.

After the climb and any other blocks, proceed to Phase 3.5.

**SOCRATIC MODE — the climb (if SOCRATIC = true):** the rungs and their rules are the same; the delivery follows the Socratic Teach Protocol below.
- High school rung: name the tension, then deploy the blueprint's Guidance Chain so that the learner states the Insight. Show the Picture and the foundational worked example only AFTER the learner has stated the Insight (or the chain has ended).
- Each higher rung: before showing anything, ask the learner to attempt the statement at that level ("How would you write that as an equation?", "What would a proof have to show?"). Then confirm it and show the rung's solved exercise.
- A failed "your turn": no declarative bridge. Return to questions pitched one level down, then give the new exercise.

**SOCRATIC MODE — Phase 3 replacement (if SOCRATIC = true):**

When SOCRATIC = true, **replace** the standard declarative teaching with Socratic guided discovery. The content is the same; the delivery method changes fundamentally.

**Socratic Teach Protocol:**

For EACH identified gap:

1. **Name the tension** (from Phase 2): Remind the learner of the specific failure and why their approach didn't work. Do NOT give the answer yet.

2. **Deploy the Socratic Guidance Chain** from the blueprint. Present questions ONE AT A TIME:
   - Present question 1. Wait for the learner's response.
   - Based on their answer, present question 2 (or adapt it). Wait.
   - Continue until the chain's final question, which should make the conclusion **inescapable**.
   - If the learner arrives at the concept themselves at ANY point in the chain, confirm and move to step 3.
   - If the learner is stuck after the full chain, THEN (and only then) explain the concept directly — but frame it as: "Here's what the chain was leading to:" not as new information.

3. **Resolution**: The concept emerges as the *only* way to resolve the tension. Frame it as an inevitability:
   - Instead of: "The Born rule states P = |psi|^2"
   - Say: "So the only operation on psi that gives a non-negative number summing to 1 is... what?" (let them say it)
   - Or: "You just showed that [their reasoning]. This is exactly [concept name]."

4. **Solved example**: Once the learner has stated the concept (or the chain has ended), consolidate it with one fully worked example in the concept-explainer format, ending with a Check. It comes after the resolution, never before it.

5. **Quick Check**: Same as standard — CTQ-derived, wait for response, clarification note, then the complete worked solution. But phrase the Quick Check as: "Now reconstruct why [concept] is the only resolution to the tension we started with."

6. **If Quick Check fails**: Do NOT re-explain declaratively. Instead, return to the Guidance Chain at the point where the learner's reasoning broke down. Ask a different narrowing question targeting that specific break, pitched one level down (plainer words, concrete numbers) when the session is above the High school level.

**Key Socratic rules for Phase 3:**
- NEVER state a concept before the learner has attempted to derive it
- NEVER give the answer in a question ("Isn't it true that X?" is NOT Socratic — it's leading)
- Guidance Chain questions must be GENUINE questions with a search space, not rhetorical
- Prefer "What would happen if..." and "Why can't we just..." over "Can you see that..."
- If the learner says something wrong, do NOT correct immediately — ask "What does that predict for [specific case]?" and let the prediction fail
- Each question narrows the search space WITHOUT giving the answer
- The deep-dive option still applies (mention once after first block)

**Save:** After EACH teaching block and Quick Check, append the check as an attempt (`step: check`, or `your-turn` with its `level` in a climb) and record in `state.saved` which blocks are done, the format used (abbreviated/full/comparison/ladder) and, in a climb, the levels held so far. Update `state.level_reached` as each level is held.

### Phase 3.5: OPTIONAL CONCEPT MAP

After all teaching is delivered and Quick Checks passed, but BEFORE the Final Test, offer the learner a concept map:

"Would you like a concept map for [sub-goal topic] before the Final Test? This is optional -- it can help visualize how the concepts connect."

- If YES: Generate a concept map using the content-builder skill's "Concept Map for TTT Sessions" format. Use **standard** depth (10-15 nodes). ALL gaps taught must appear as principles or innovations in the map. For conflation gaps, use the comparison map format. Display the map inline.

- If NO: Proceed directly to Phase 4.

This step is OPTIONAL. The session works identically without it. Do NOT push the learner to accept -- one brief offer is sufficient.

**Save:** Set `state.step` to `final-check`.

### Phase 4: FINAL TEST

Present a **NEW** practical case:
- Different scenario from the Initial Test
- Same competencies being tested
- Same pass criteria
- No preamble -- straight to the scenario

**Hard-core principles:** if the climb reached the session's level, the Final Test is at that level, as usual. If the climb stopped short, give the Final Test at the level reached instead: re-pitch the blueprint's Final Test to that level (to the High school level if no rung was held).

**SOCRATIC MODE — Phase 4 additions (if SOCRATIC = true):**

The Final Test MUST include a **"reconstruct the reasoning"** component. In addition to the practical case, add:
> **Part B:** Explain *why* your approach works. What would go wrong if you used [the wrong path from the Initial Test] instead?

This tests whether the learner can reconstruct the reasoning chain, not just apply a memorized procedure. The learner must demonstrate they understand WHY the concept resolves the tension, not just THAT it does.

**MANDATORY: Every Final Test MUST also end with the same two notes (copy verbatim):**

> *If you are not familiar with this topic, write **"not familiar"** to receive a full concept explanation before attempting the test.*
>
> *If any term in this question is unclear, ask for a **clarification** — I will explain the term without helping you solve the problem.*

The Term Clarification Protocol applies identically during the Final Test.

Wait for the learner to respond.

**Save:** After the learner responds, append the attempt (`step: final-check`, the full answer).

### Phase 5: EVALUATE FINAL

- **PASS**: Congratulate. Proceed to Phase 6.
- **FAIL (first time)**: Identify remaining gaps with failure mode classification. Loop back to Phase 3 with ONLY the persistent gaps. Then present ANOTHER new Final Test case. This is Loop 1.
- **FAIL (second time -- Loop 2 max)**: Record the result. Tell the learner: "This sub-goal needs additional review. I recommend revisiting the prerequisites or discussing with an instructor."

**Hard-core principles:**
- A loop after a failed Final Test re-enters the climb at the first rung not held, not at the start.
- **When the climb stopped short**, the Final Test was given at the level reached. Whatever its result, run no further loop: the Status is `needs-review`, and the Score records the level reached against the session's level (for example "High school of Master's"). Tell the learner what they now hold and which rung to come back to.

**Save:** Set the final attempt's verdict and feedback; after another round, add 1 to `state.rounds`. Set `state.step` to `record`.

### Phase 6: RECORD

Do the following, in this order. If the session is resumed during RECORD, skip any step whose result already exists. Every path below is inside the course folder; `<NN-slug>` is the lesson's folder name (two-digit number and title slug, see the course-model skill).

**A) Close the lesson in `course.json`** (course-model skill, section 3, "The lesson ends"):
- `state.status`: `done`, or `review` when the Final Test was not passed or a key idea stopped below the course level
- `state.step` and `state.saved`: `null`; `state.finished`: today
- `state.level_reached` for a key idea (High school / Master's / Advanced as `high-school` / `masters` / `advanced`, or `below-high-school`)
- `state.to_work_on`: mark each item `resolved` when the Final Test showed it fixed
- `state.notes`: one or two lines (the delivery, the worked example's role, anything to revisit later)
- `history`: one line, `Lesson <N> done` or `Lesson <N> needs review`
The attempts, with the learner's answers in full, are already in `state.attempts`: they are the record of the session.

**B) Lesson notes** (if teaching occurred): write `lessons/<NN-slug>/notes.md` using the concept-explainer skill's export format (front matter, all teaching content, the idea map if one was made, the success criteria, the lesson context).
- For a climb: the reveal, each level's explanation, and each "your turn" exercise with its worked solution. The solved examples that live in the lesson design are referenced by level, not copied. A level written for this session (above the course level) is included in full.
- If no teaching occurred (learner passed the Initial Test), skip this step. A recap after a pass on a key idea is not teaching; an accepted climb or next level up is.

**C) Practice book** (Principle, Concept and Tool lessons only): add a set to `lessons/<NN-slug>/practice.md`, following the concept-explainer skill's Exercise Book Format.
- 2 fully solved exercises for each level from High school up to the course level: one standard, one with a twist
- Statements first, worked solutions after; every solution complete and ending with a Check
- No exercise repeats a test case, a worked example in the lesson design, or an exercise from this session
- If the design has a `practice_task`, it opens the set at the course level, solved
- If the file already exists, append the set. Never overwrite it.
- Write it whether or not teaching occurred: it is practice material, not a record of the session
- For a Why-it-matters or Capstone lesson, skip this step

**D) Other files** (only when the work calls for one): a reusable output the learner built (a filled-in template, a calculation sheet, a checklist) goes to `lessons/<NN-slug>/<slug>.md`. Most sessions produce none.

**E) List every file this session wrote** in `files` (kind `notes`, `practice`, `lesson-page` or `other`, with the lesson id, a plain title and today's date), then validate `course.json` and regenerate `overview.md`. A file already listed only has its `updated` date changed.

**F) Suggest the next step:** the next lesson (`course.py next-lesson`). Mention `/worked-exercises <N>` for more solved practice on this lesson and `/training-status` for overall progress. If the learner asks for a readable record of the session, write `lessons/<NN-slug>/record.md` from the attempts and list it (kind `record`).

## Important Rules

- ALWAYS append the "not familiar" note AND the "clarification" note at the end of EVERY test (Initial Test and Final Test) -- these two notes are NON-NEGOTIABLE
- NEVER reveal expected answers or "Watch for" hints BEFORE the learner responds -- this applies to ALL questions (Initial Test, Quick Checks, Final Test). Present the question, wait, THEN show the answer -- for a Quick Check, as a complete worked solution ending with a Check.
- NEVER teach before testing -- the Initial Test ALWAYS comes first
- NEVER skip evaluation -- always explicitly state PASS/FAIL with reasons and failure mode classifications
- NEVER combine multiple gaps into one explanation -- one gap, one concept explanation
- ALWAYS assess gap complexity before choosing teaching format (abbreviated vs full vs comparison)
- ALWAYS use CTQ failure mode taxonomy when naming gaps in EVALUATE
- ALWAYS wait for learner responses at: Initial Test, each Quick Check, Final Test
- ALWAYS update the plan file and write the transcript at the end
- ALWAYS check the lesson's saved place before starting -- offer to resume if it is in progress
- ALWAYS save the lesson's state in `course.json` after each phase completes
- NEVER write a plan file, checkpoint file, transcript or learner profile: the course lives in `course.json`
- ALWAYS export a concept file during RECORD if teaching occurred
- ALWAYS add a practice set during RECORD for a Principle, Concept or Tool lesson, and ALWAYS list every file the session wrote in the course's `files`
- For a hard-core principle, NEVER warn the learner about the Tempting answer before the Initial Test, and NEVER skip the reveal when they fall for it
- In a climb, a rung has at most two exercises; a climb that stops short is recorded with the level reached and is not an adaptation loop
- MENTION the deep-dive option once after the first teaching block -- never repeat the offer
- OPTIONALLY offer a concept map after the TEACH phase -- never insist, just offer once
