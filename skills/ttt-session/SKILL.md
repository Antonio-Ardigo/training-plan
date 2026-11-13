---
description: "Test-Teach-Test session design and execution. Use when the user asks to run a session, start a learning session, test me on a topic, practice a skill, assess my knowledge, design a TTT learning cycle, or execute an adaptive test-teach-test loop for a sub-goal."
---

# TTT Session -- Domain Knowledge

Reference knowledge for designing and executing Test-Teach-Test learning sessions.

## Two Modes

This skill operates in two modes:

1. **Design mode** -- called during `/create-training-plan` to produce session blueprints
2. **Execute mode** -- called during `/run-session` to run the interactive TTT loop

---

## MODE 1: Design (Session Blueprints)

For each sub-goal, produce a session blueprint with this structure:

```markdown
### SG-<N>: <title>

**Initial Test**
- Case: <practical scenario description -- what the learner must do>
- Assesses: <specific competencies being tested>
- Pass criteria: <concrete, measurable threshold>

**Estimated Depth:** <High school/Master's/Advanced>

**Anticipated CTQs:**
| CTQ | Source | Mastery Test | Common Failure Mode |
|-----|--------|-------------|---------------------|
| <what the learner must understand> | <concept> | <verification task> | <likely failure pattern> |

**Teach Phase Plan** (activated only if Initial Test reveals gaps)
- Concepts to cover: <list of key ideas>
- Exercises: <2-3 graduated exercises>
- Known pitfalls: <common errors with CTQ failure mode classification>
  - [conflation]: <two concepts learners commonly confuse>
  - [procedural-without-conceptual]: <formulas applied without understanding>
  - [overgeneralization]: <rules applied beyond their domain>

**Final Test**
- Case: <different scenario, same competencies>
- Pass criteria: <same threshold as Initial Test>

**Adaptation Rules**
- If fails on <specific gap>: re-teach <specific content>
- Max loops: 2
```

### Blueprint Design Principles

1. **Initial Test cases must be practical and immediate** -- the learner receives a scenario and must act. No multiple-choice. No "explain the theory." Instead: "Here is a situation. Solve it."

2. **The Initial Test must be solvable** by someone who has the knowledge -- it's a diagnostic, not a trick question. A competent person should pass it in a few minutes.

3. **The Final Test must be a DIFFERENT scenario** testing the SAME competencies. If the Initial Test used Project A, the Final Test uses Project B. Same skills, new context -- this verifies transfer, not memorization.

4. **Pass criteria must be concrete**:
   - Good: "Identifies at least 8 of 10 cost categories"
   - Good: "Calculation within 5% of reference answer"
   - Bad: "Shows understanding" (not measurable)

5. **CTQ criteria supplement pass criteria** -- they define what specific understanding is required, not just what score threshold to meet. Each CTQ traces to a principle or innovation and has a concrete mastery test.

6. **Adaptation rules map specific gaps to specific content** -- not "if fails, re-teach everything" but "if fails on indirect costs, re-teach indirect costs specifically." Classify anticipated failures using CTQ failure mode taxonomy.

7. **Estimated Depth is the plan's Target level** -- it sets the pitch of the tests and the teaching, not their length:
   - High school: plain words, concrete numbers, minimal LaTeX
   - Master's: formal statements, full LaTeX, worked examples in symbols then numbers
   - Advanced: proofs, edge cases, competing formulations

   A sub-goal's difficulty decides how long the teaching is, never how deep. (In plans created before the Target level existed, depth followed difficulty; read their values one for one.)

---

## MODE 2: Execute (Interactive TTT Loop)

When running a session, follow this exact protocol:

### Phase 1: INITIAL TEST

Present the practical case from the session blueprint to the learner.

Rules:
- The session has opened with motivation and historical context (Phase 0 of `/run-session`): why the sub-goal matters and the real situation it came out of, with no answer given. After that: no theory, no hint, no warm-up
- Every question is clear (one thing asked, the form of the answer stated) and every case is real (never an invented method)
- Present the scenario and the task directly
- Ask the learner to respond
- Wait for the learner's response before proceeding
- ALWAYS include the "not familiar" note AND the "clarification" note at the end of every test (see below)

Example opening:
> **Practical Case -- SG-3: Unit-Rate Estimation**
>
> You have the following quantities for a warehouse foundation:
> - Concrete: 450 m3
> - Rebar: 38,000 kg
> - Formwork: 1,200 m2
>
> Unit rates: Concrete $180/m3, Rebar $2.10/kg, Formwork $45/m2
>
> **Task:** Calculate the total foundation cost. Show your work.
>
> *If you are not familiar with this topic, write **"not familiar"** to receive a full concept explanation before attempting the test.*
>
> *If any term in this question is unclear, ask for a **clarification** — I will explain the term without helping you solve the problem.*

Both notes MUST appear at the end of every Initial Test AND Final Test presentation:
- The "not familiar" note gives learners an honest opt-in to receive the full concept explainer before attempting a topic they have no background in.
- The "clarification" note enables the Term Clarification Protocol (see below) — preventing false negatives from terminology confusion.

### Term Clarification Protocol

When the learner asks about a term during a test phase (Initial Test or Final Test), invoke the **term-clarifier** agent. Pass it:
1. The term the learner asked about
2. The Anticipated CTQs for this sub-goal (from the blueprint)
3. The Principle Extraction table (from the training plan)
4. The sub-goal statement

Do NOT pass: the test question, the expected answer, the pass criteria, or the teach topics. The term-clarifier agent is firewalled from the answer.

The term-clarifier will return one of three responses:
- **Category A (tested knowledge)**: Declines to clarify; suggests "not familiar" if the learner lacks background
- **Category B (context vocabulary)**: Provides a generic definition with an example from a different context
- **Category C (missing prerequisite)**: Provides a definition and flags a session note for the Teach phase

After the clarification, resume the test. The learner continues their attempt. Clarifications do not count as gaps or failures — they are purely informational.

**Rules for clarifications:**
- Multiple clarifications are allowed during a single test
- Each clarification is for ONE term at a time
- Clarifications are logged in the session transcript
- Category C clarifications are noted in the evaluation as potential prerequisite gaps

**Handling PLAN-REVISION-REQUEST:**

If the term-clarifier returns a PLAN-REVISION-REQUEST (critical missing prerequisite), the session must:

1. Show the clarification to the learner normally
2. After the learner submits their test answer (or says "not familiar"), present the plan revision offer:
   > "During this test, you asked about **[term]** which is a foundational concept not currently covered in your training plan. I recommend adding a prerequisite session before continuing. You can:
   > - **A)** Add a prerequisite session on [concept] and run it before retrying this test
   > - **B)** Continue with the current session as-is"
3. If the learner chooses A: save a checkpoint, add the prerequisite sub-goal to the plan (update the Sub-Goals table, Prerequisite Graph, and Sequence), then run the new prerequisite session. After it completes, resume the current session from the checkpoint.
4. If the learner chooses B: continue normally. The gap is noted in the learner profile for future reference.

### Phase 2: EVALUATE

After the learner responds, evaluate against the pass criteria and CTQ mastery tests:

- **PASS** (meets or exceeds criteria): Skip to Phase 6 (RECORD). Sub-goal complete. (For a hard-core principle, give the recap and the offer first; see Hard-Core Principles below.)
- **PARTIAL** (some gaps identified): Proceed to Phase 3. List specific gaps with failure mode classification.
- **FAIL** (major gaps): Proceed to Phase 3. List all gaps with failure mode classification.
- **NOT FAMILIAR**: If the learner writes "not familiar" (or equivalent: "I don't know this topic", "no background", "never learned this"):
  1. **Check Prerequisite Graph**: does this SG have uncompleted prerequisite SGs? If YES, offer to run the prerequisite SG first.
  2. **Check Principle Extraction table**: does this SG's principles list external prerequisites NOT covered by any existing SG? If YES, present the PLAN-REVISION offer:
     > "You indicated you're not familiar with this topic. The prerequisite knowledge (**[concept]**) is not currently covered in your training plan. You can:
     > - **A)** Add a prerequisite session on [concept] and run it first
     > - **B)** Continue with a full concept explanation as-is"
     If A: save checkpoint, add prerequisite SG, run it, then resume. If B: proceed to step 3.
  3. Treat as a single complex gap with failure mode `[missing-prerequisite]`. Deliver the **Full 7-Section Concept Explanation** for the sub-goal's topic at the blueprint's depth level. After the full explanation and Quick Check, proceed to the Initial Test again (the learner now attempts it with the knowledge gained). This does NOT count as an adaptation loop.

When identifying gaps, classify each using the CTQ failure mode taxonomy:
- "Gap [conflation]: confused indirect costs with contingency"
- "Gap [procedural-without-conceptual]: applied the formula correctly but cannot explain why it works"
- "Gap [overgeneralization]: assumed all overhead is a fixed percentage"
- "Gap [missing-prerequisite]: unfamiliar with WBS structure needed for cost classification"

Simple gaps that don't match a failure mode pattern:
- "Gap: arithmetic error in unit conversion" (simple, no deeper conceptual issue)

### Phase 3: TEACH

For each identified gap, generate a concept explanation using the `content-builder` skill:

1. **Assess gap complexity** (from the failure mode classification in Phase 2):
   - Simple gap (no failure mode) -> Abbreviated Concept Explanation (Problem + Principles + Worked Example + Quick Check)
   - Complex gap (has failure mode) -> Full Concept Explanation (7 sections including Worked Example)
   - Conflation gap -> Concept Comparison

2. **Select depth level** from the blueprint's Estimated Depth: High school, Master's or Advanced (older plans say introductory / intermediate / advanced; read them one for one). Default: Master's.

3. **Deliver the concept explanation**:
   - ONE explanation per gap, delivered sequentially
   - Whatever the format (abbreviated, full or comparison), the explanation contains one fully worked example ending with a Check
   - After each Quick Check (CTQ-derived), wait for the learner's answer, then reveal the complete worked solution
   - If Quick Check fails: re-explain one level down (a different picture if already at the High school level), give one more CTQ check at the original level
   - If second check fails: note as persistent gap, proceed

4. **After the first teaching block**, mention once:
   "You can ask me to go deeper on any principle I just explained."
   If the learner requests a deep-dive: generate it inline using the concept-explainer skill's Deep-Dive Protocol, then continue.

5. After ALL gaps are taught, proceed to Phase 3.5

Rules:
- Deliver ONE explanation at a time
- Every Quick Check MUST end with: `*If any term in this question is unclear, ask for a **clarification**.*`
- **NEVER show expected answers or "Watch for" hints before the learner responds to a Quick Check.** Present the question + clarification note, wait for the learner's answer, THEN reveal the complete worked solution (every step shown and annotated, ending with a Check that confirms the result a second way) and evaluate.
- If the learner asks for a clarification during a Quick Check: invoke the term-clarifier agent (same protocol as during tests)
- Wait for the learner to complete the Quick Check before moving to the next
- If the Quick Check fails, re-explain that specific point one level down before moving on: a Master's-level block at the High school level, an Advanced block at the Master's level, a High school block with a different picture or example
- After ALL gaps are taught, proceed to Phase 3.5

### Phase 3.5: OPTIONAL CONCEPT MAP

After all teaching is delivered, optionally offer a concept map:

- Use **standard** depth (10-15 nodes)
- ALL gaps taught must appear as principles or innovations in the map
- For conflation gaps, use the comparison map format (three-section)
- See the content-builder skill's "Concept Map for TTT Sessions" for format details
- This is a brief offer -- proceed to Phase 4 regardless of answer

### Phase 4: FINAL TEST

Present a NEW practical case testing the same competencies:

- Different scenario from the Initial Test (different project, different numbers, different context)
- Same competencies being assessed
- Same pass criteria
- Same format (practical, immediate, no preamble)
- MUST include both the "not familiar" and "clarification" notes at the end (same as Initial Test)
- The Term Clarification Protocol applies identically during the Final Test

### Phase 5: EVALUATE FINAL

Evaluate the Final Test response:

- **PASS**: Proceed to Phase 6. Sub-goal complete.
- **FAIL (Loop 1)**: Identify remaining gaps with failure mode classification. Loop back to Phase 3 with NARROWER focus -- only re-teach the specific gaps that persist. Then present ANOTHER new Final Test case.
- **FAIL (Loop 2)**: This is the maximum. Record the result and flag: "Sub-goal needs additional review. Recommend revisiting prerequisites or seeking instructor support."

### Phase 6: RECORD

In this order: update the training plan file, write the session transcript, update the learner profile, export the concept file, write the exercise book, write any other deliverable, register every artefact, delete the checkpoint, and suggest the next step. `/run-session` Phase 6 gives the detail of each step. If a session is resumed during RECORD, steps whose result already exists are skipped.

**Exercise book:** for a Core Principle, Key Concept or Tools sub-goal, add a session set to `<topic>_artefact_SG<N>_exercises.md`: 2 fully solved exercises for each level from High school up to the sub-goal's Estimated Depth, in the concept-explainer skill's Exercise Book Format. Append if the file exists; never overwrite it. Motivation and Verification sub-goals have no exercise book.

**Other deliverable artefacts (as required):** if the sub-goal work naturally yielded a reusable output — a filled-in template, a worked calculation sheet, a checklist, or a reference the learner built — write it to disk as `<topic>_artefact_SG<N>_<slug>.md`. Not every session produces one; create it only when the work genuinely calls for it.

**Register every artefact:** for each artefact this session wrote (transcript, concept file, exercise book, and any other deliverable), append a row to the plan file's **Artefacts Register** via the `Edit` tool. If `learner_profile.md` is not listed yet (the first session of a plan creates it), add a row for it as well, with type `profile`:

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| <name> | transcript / concept-file / deliverable | SG-<N> | <relative path> | current |

The Artefacts Register is the course's visible anchor — it must stay authoritative, so registration is mandatory whenever an artefact is produced.

---

## Hard-Core Principles: the Climb

A Core Principle blueprint that has a Tempting answer, an Insight and a Picture is a *hard-core* principle: one that is hard to grasp, taught through an aha moment and a climb through the levels. Its Level ladder holds the solved exercises of the rungs above High school; in a High school plan there are none. `/run-session` holds the full flow and the concept-explainer skill's Level Ladder holds the content rules. In short:

- **Test**: the Initial Test is built so that the natural approach gives the Tempting answer. No warning, no hint.
- **Pass** (right, and justified at the session's level): a recap (the Insight, the Picture, the top rung's solved exercise), then one offer: the full climb, or the next level up.
- **Not passed**: the climb, taught as one block (format `ladder`), from the start rung the answer shows (fell for it, or unsure: High school) to the session's level. The High school rung is the reveal. Every rung ends with "your turn", which is that rung's Quick Check. A method failure gets a short bridge one level down and one new exercise; a second failure stops the climb.
- **Final Test**: at the session's level, or at the level reached when the climb stopped short. A stopped climb is recorded as `needs-review` with the level reached and uses no adaptation loop. A loop after a failed Final Test re-enters the climb at the first rung not held.
- **"Not familiar"**: the climb from High school with no Tempting answer named, then the Initial Test again.
- **Graphic delivery (the default)**: the whole session is delivered on one interactive page built by the visual-explainer skill, in three stages: the Discovery Question and Initial Test, the Teach phase (one section per gap, and the climb of a hard-core principle with one tab per rung, from the blueprint's Visual design), and the Final Test. The learner goes through the whole session on the page, one step at a time, without copying anything into chat: answers are checked in place and saved by the page, and the session reads the record and confirms it when the learner writes `done`. Where a page can neither ask the model nor save, the learner returns an answers block after each test and a results block after the Teach stage. The page is written to `<topic>_visual_SG<N>.html` and registered. `/run-session SG-N chat`, or asking for chat, switches the session to chat text; so does a page that cannot be delivered.
- **Socratic plans**: the same rungs, reached through questions. The Insight comes from the Guidance Chain, which in graphic delivery runs on the page, one question at a time on the picture; the Picture and the solved exercises open only after the learner has stated the idea.

A Core Principle blueprint without those fields is handled as before: its worked example is shown as reinforcement on a pass, and as the primary teaching content otherwise.

---

## Socratic Execution Mode

When running a session from a Socratic training plan, the TTT protocol keeps its three steps and changes how they are delivered. The **Question -> Tension -> Resolution -> Test** arc is a Socratic form of **Test -> Teach -> Test**: the Discovery Question and Initial Test are the first Test (where the tension appears), the Guidance Chain is the Teach (where the resolution is derived, not explained), and the Final Test is the second Test.

### Detection

At Step 0, when reading the training plan, the method heading decides the mode:
- `## Pedagogical Method: Socratic Discovery` means a Socratic plan: set `SOCRATIC = true` and apply the modifications below to every phase
- `## Pedagogical Method: Test-Teach-Test` means a standard plan, even though that section mentions the Socratic command
- No method heading (plans created before the section existed): fall back to the file name. A name ending in `-socratic_training_plan.md` is a Socratic plan.

### Phase 1 Modification: Discovery Question Before Initial Test

Before presenting the Initial Test, present the blueprint's **Discovery Question**. This creates genuine puzzlement — the learner must *feel* the gap.

The Initial Test is designed with a **wrong path** — a plausible but incorrect approach. Do NOT warn the learner. Let them hit the wrong path naturally. The tension between their attempt and the correct answer is the pedagogical engine.

### Phase 2 Modification: Name the Tension

When evaluating, explicitly identify whether the learner hit the designed wrong path:
> "Your approach assumed [wrong path]. This is exactly the tension: [why the wrong path fails]."

Name the tension but do NOT explain the resolution. The learner should now *want* the concept.

### Phase 3 Modification: Socratic Guided Discovery (replaces declarative teaching)

**This is the most critical change.** Instead of declaring concepts, guide the learner to discover them.

For each gap:

1. **Remind of the tension**: What failed and why.

2. **Deploy the Socratic Guidance Chain** from the blueprint (3-6 questions). Present ONE question at a time:
   - Wait for the learner's response to each question
   - Each question narrows the search space without giving the answer
   - The final question makes the conclusion inescapable
   - If the learner derives the concept at any point, confirm immediately and skip remaining chain questions
   - If the learner is stuck after the full chain, explain — but frame as "Here's what the chain was leading to:" not as new information

3. **Resolution as inevitability**: The concept emerges as the ONLY way to resolve the tension.
   - Frame conclusions as questions: "So the only operation that gives a non-negative number summing to 1 is...?"
   - Or: "You just showed that [their reasoning]. This is exactly [concept name]."
   - NEVER state a concept before the learner has attempted to derive it

4. **Solved example**: once the learner has stated the concept, consolidate it with one fully worked example ending with a Check. It comes after the resolution, never before it.

5. **Quick Check**: Phrase as reconstruction: "Reconstruct why [concept] is the only resolution to the tension." After the learner responds, reveal the complete worked solution.

6. **On Quick Check failure**: Do NOT re-explain declaratively. Return to the Guidance Chain at the break point. Ask a different narrowing question, pitched one level down when the session is above the High school level.

**Anti-patterns (NEVER do these in Socratic mode):**
- "The answer is X because Y" (declarative — the learner should derive X)
- "Isn't it true that X?" (leading, not Socratic — gives the answer in the question)
- "Can you see that X?" (rhetorical — not a genuine question)
- Correcting a wrong answer immediately (instead: "What does that predict for [specific case]?" — let the prediction fail)
- Explaining before the learner has struggled (the struggle IS the learning)

**Genuine Socratic questions:**
- "What would happen if we tried [their approach] on [edge case]?"
- "Why can't we just [simpler but wrong method]?"
- "What constraint have we not used yet?"
- "If [their answer] were correct, what would that imply about [consequence]?"

### Phase 4 Modification: Reconstruct the Reasoning

The Final Test adds a **Part B**:
> "Explain *why* your approach works. What would go wrong if you used [wrong path from Initial Test] instead?"

This tests reconstruction of reasoning, not just procedural application.

### Phase 5 Modification: Evaluate Reconstruction

When evaluating the Final Test in Socratic mode, Part B is weighted equally with Part A. A learner who gets Part A correct but cannot explain why (Part B) receives a PARTIAL, not a PASS.

### Adaptation Loop in Socratic Mode

If the learner fails the Final Test in Socratic mode:
- Loop 1: Re-deploy a MODIFIED Guidance Chain (different questions targeting the persistent gap). Do NOT fall back to declarative teaching.
- Loop 2 (max): If still failing after two Socratic loops, THEN deliver a brief declarative explanation as last resort, flagging: "Socratic derivation was not sufficient for this gap — direct explanation provided."

---

## Adaptation Loop Summary

```text
Loop 0 (normal):  Initial Test -> Teach -> Final Test -> PASS
Loop 1 (retry):   Initial Test -> Teach -> Final Test -> FAIL -> Re-teach (narrower) -> Final Test 2 -> PASS
Loop 2 (max):     Initial Test -> Teach -> Final Test -> FAIL -> Re-teach -> Final Test 2 -> FAIL -> FLAG
```

Maximum 2 adaptation loops per sub-goal. After 2 failures, do not loop again -- record the result and recommend review.

---

## Checkpoint File Format

When a session is interrupted, the checkpoint file preserves progress so the session can be resumed.

Filename: `<topic>_checkpoint_SG<N>.md`

```markdown
# Session Checkpoint: SG-<N> -- <title>
Started: <date>

## Current Phase: <INITIAL_TEST|EVALUATE|TEACH|CONCEPT_MAP_OFFER|FINAL_TEST|EVALUATE_FINAL|RECORD>
<!-- For TEACH phase, also note: Gap <X> of <Y> completed. During a climb: Rung <level> completed -->

## Initial Test
**Case:** <what was presented>
**Learner response:** <what they said>

## Evaluation
**Result:** <PASS/PARTIAL/FAIL>
**Gaps identified:** <list with failure mode classifications>
**Start rung:** <hard-core principles only: the rung where the climb starts>

## Teach Phase
### Gap: <name> [<failure mode>]
**Format:** <abbreviated/full/comparison/ladder>
**Content:** <summary of what was taught>
**Quick Check:** <question> -> Learner: <answer> -> <correct/incorrect>
**Rungs:** <for a climb only, one line per rung completed: <level> -- your turn: <question> -> Learner: <answer> -> <held/bridge/not held>>
**Deep-dive:** <if requested, summary of expanded principle>

(repeat for each gap completed so far)

## Concept Map
(if generated during Phase 3.5)

## Final Test
**Case:** <what was presented>
**Learner response:** <what they said>

## Final Evaluation
**Result:** <PASS/FAIL>
```

Sections are populated incrementally as phases complete. Sections below the current phase marker are absent or empty.

## Resume Protocol

When resuming from a checkpoint:

1. Read the checkpoint file
2. Show the learner a brief summary of completed phases
3. Ask if they want to resume or start fresh
4. If resuming, skip to the phase AFTER the `## Current Phase` marker
5. For TEACH phase resume: skip already-delivered gaps (listed in checkpoint) and continue from the next undelivered gap. In a climb, continue at the rung after the last one completed.
6. When the session completes normally, delete the checkpoint and write the final transcript as usual
