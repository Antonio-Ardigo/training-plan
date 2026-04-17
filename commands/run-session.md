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

## Step 0: Find the Training Plan

Use Glob to find `*_training_plan.md` or `*-socratic_training_plan.md` in the current directory. Read the file. If no plan exists, tell the user to run `/create-training-plan` or `/socratic-training-plan` first.

**Detect Socratic mode:** If the plan filename ends with `-socratic_training_plan.md` OR the plan contains a `## Pedagogical Method: Socratic Discovery` section, this is a **Socratic plan**. All subsequent phases MUST follow the Socratic execution rules described below. Set a mental flag: `SOCRATIC = true`.

## Step 1: Identify the Target Sub-Goal

From the user's input (`$ARGUMENTS`), determine which sub-goal to run:
- If they gave a number (e.g., "SG-2" or "2"), use that sub-goal
- If they gave a keyword (e.g., "unit rate" or "contingency"), match it to the closest sub-goal
- If unclear, show the sub-goals table and ask them to pick one
- If the sub-goal is already marked "complete", confirm they want to re-do it

## Step 1.5: Check for Existing Checkpoint

Use Glob to look for `<topic>_checkpoint_SG<N>.md` in the current directory (where `<topic>` and `<N>` match the current plan and sub-goal).

If a checkpoint file exists:
1. Read it
2. Show the learner a summary of what was already completed:
   - Which phases were finished
   - The current phase marker
   - Key results so far (initial test result, gaps found, teach blocks delivered)
3. Ask: "A previous session for this sub-goal was interrupted at [phase name]. Resume from where you left off?"
   - If YES: skip to the next phase after the checkpoint marker
   - If NO: delete the checkpoint file and start the session fresh

If no checkpoint exists, proceed normally.

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
     If A: save checkpoint, add prerequisite SG to plan (update Sub-Goals, Prerequisite Graph, Sequence), run it, then resume.
     If B: proceed to step 3.
3. Deliver a **Full 7-Section Concept Explanation** for the sub-goal's topic at the blueprint's depth level, then re-present the Initial Test. This does NOT count as an adaptation loop.

If the learner asks for a clarification: invoke the term-clarifier agent with ONLY (1) the term, (2) the CTQ list, (3) the principle list, (4) the sub-goal statement. Do NOT pass the test question, expected answer, or pass criteria.

If the term-clarifier returns a **PLAN-REVISION-REQUEST** (critical missing prerequisite): show the clarification to the learner normally. After the learner submits their test answer (or says "not familiar"), present:
> "During this test, you asked about **[term]** which is a foundational concept not currently covered in your training plan. You can:
> - **A)** Add a prerequisite session on [concept] and run it before retrying this test
> - **B)** Continue with the current session as-is"
If A: save checkpoint, add the prerequisite sub-goal to the plan (update Sub-Goals table, Prerequisite Graph, and Sequence), then run the new prerequisite session. After it completes, resume this session from the checkpoint.
If B: continue normally, note the gap in the learner profile.

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

**Checkpoint:** After the learner responds, write `<topic>_checkpoint_SG<N>.md` with the initial test case and learner response. Set `## Current Phase: EVALUATE`.

### Phase 2: EVALUATE

After the learner responds, evaluate against the pass criteria and CTQ mastery tests from the blueprint.

- List what they got right
- List what they got wrong or missed
- Determine: **PASS**, **PARTIAL**, or **FAIL**
- If PASS: tell them, then skip to Phase 6
- If PARTIAL or FAIL: list the specific gaps with CTQ failure mode classification, then proceed to Phase 3

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

**Checkpoint:** Update `<topic>_checkpoint_SG<N>.md` with evaluation results and classified gap list. Set `## Current Phase: TEACH` (or `RECORD` if PASS).

### Phase 3: TEACH

For EACH identified gap, deliver a concept explanation using the content-builder skill:

**Step 1: Assess gap complexity** (from the failure mode classification in Phase 2):
- Simple gap (no failure mode tag) -> **Abbreviated Concept Explanation** (Problem + Principles + Worked Example + CTQ Quick Check)
- Complex gap (has failure mode tag) -> **Full Concept Explanation** (7 sections from concept-explainer, including Worked Example)
- Conflation gap -> **Concept Comparison** (shared principles + divergences + CTQ distinction)

**Step 2: Determine depth level**
Use the sub-goal's blueprint Estimated Depth. Default: intermediate.

**Step 3: Deliver the concept explanation**
- ONE explanation per gap, delivered sequentially
- Every Quick Check MUST end with: `*If any term in this question is unclear, ask for a **clarification**.*`
- **NEVER show the expected answer or "Watch for" hint before the learner responds.** Present ONLY the question + clarification note. After the learner answers, reveal the expected answer, evaluate, and proceed.
- If the learner asks for a clarification during a Quick Check: invoke the term-clarifier agent (same protocol as during tests)
- If they get the Quick Check wrong: re-explain using a different angle, give one more CTQ check
- If they fail the second check: note as persistent gap, proceed to next gap

**Step 4: Deep-dive option**
After the FIRST teaching block, mention once:
"You can ask me to go deeper on any principle I just explained."
- If the learner requests a deep-dive: generate a full 6-section explanation for that principle inline, then continue with the next gap
- If they don't ask: proceed normally
- Do NOT repeat this offer after subsequent blocks

After ALL gaps are taught and Quick Checks addressed, proceed to Phase 3.5.

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

4. **Quick Check**: Same as standard — CTQ-derived, wait for response, clarification note. But phrase the Quick Check as: "Now reconstruct why [concept] is the only resolution to the tension we started with."

5. **If Quick Check fails**: Do NOT re-explain declaratively. Instead, return to the Guidance Chain at the point where the learner's reasoning broke down. Ask a different narrowing question targeting that specific break.

**Key Socratic rules for Phase 3:**
- NEVER state a concept before the learner has attempted to derive it
- NEVER give the answer in a question ("Isn't it true that X?" is NOT Socratic — it's leading)
- Guidance Chain questions must be GENUINE questions with a search space, not rhetorical
- Prefer "What would happen if..." and "Why can't we just..." over "Can you see that..."
- If the learner says something wrong, do NOT correct immediately — ask "What does that predict for [specific case]?" and let the prediction fail
- Each question narrows the search space WITHOUT giving the answer
- The deep-dive option still applies (mention once after first block)

**Checkpoint:** After EACH teaching block and Quick Check, update `<topic>_checkpoint_SG<N>.md` with the completed block (including format used: abbreviated/full/comparison). Update `## Current Phase: TEACH (Gap N of M completed)`. After the final block, set `## Current Phase: CONCEPT_MAP_OFFER`.

### Phase 3.5: OPTIONAL CONCEPT MAP

After all teaching is delivered and Quick Checks passed, but BEFORE the Final Test, offer the learner a concept map:

"Would you like a concept map for [sub-goal topic] before the Final Test? This is optional -- it can help visualize how the concepts connect."

- If YES: Generate a concept map using the content-builder skill's "Concept Map for TTT Sessions" format. Use **standard** depth (10-15 nodes). ALL gaps taught must appear as principles or innovations in the map. For conflation gaps, use the comparison map format. Display the map inline.

- If NO: Proceed directly to Phase 4.

This step is OPTIONAL. The session works identically without it. Do NOT push the learner to accept -- one brief offer is sufficient.

**Checkpoint:** Update checkpoint. Set `## Current Phase: FINAL_TEST`. If a concept map was generated, include it in the checkpoint.

### Phase 4: FINAL TEST

Present a **NEW** practical case:
- Different scenario from the Initial Test
- Same competencies being tested
- Same pass criteria
- No preamble -- straight to the scenario

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

**Checkpoint:** After the learner responds, update checkpoint with final test case and response. Set `## Current Phase: EVALUATE_FINAL`.

### Phase 5: EVALUATE FINAL

- **PASS**: Congratulate. Proceed to Phase 6.
- **FAIL (first time)**: Identify remaining gaps with failure mode classification. Loop back to Phase 3 with ONLY the persistent gaps. Then present ANOTHER new Final Test case. This is Loop 1.
- **FAIL (second time -- Loop 2 max)**: Record the result. Tell the learner: "This sub-goal needs additional review. I recommend revisiting the prerequisites or discussing with an instructor."

**Checkpoint:** Update checkpoint with final evaluation. Set `## Current Phase: RECORD`.

### Phase 6: RECORD

Do six things:

**A) Update the training plan file** using the Edit tool:
- Change the sub-goal's Status from "pending" to "complete" (or "needs-review")
- Update the Score column
- Add a Progress Log entry:

```markdown
### SG-<N> -- <Completed/Needs Review> <date>
- Initial Test: <PASS/PARTIAL/FAIL> (<details>)
- Gaps found: <list with failure mode tags, or "none">
- Teach Phase: <N explanations delivered (N abbreviated, N full, N comparison), or "skipped -- no gaps">
- Final Test: <PASS/FAIL> (<details>)
- Loops: <0/1/2>
- Concept Map: <generated (standard/deep) / not generated>
- Concept File: <filename or "none">
- Worked Example: <delivered as reinforcement / delivered as teaching / N/A (not a Core Principle SG)>
- Notes: <brief observations>
```

**B) Write a session transcript** to `<topic>_session_SG<N>.md`:

```markdown
# Session Transcript: SG-<N> -- <title>
Date: <date>

## Initial Test
**Case:** <what was presented>
**Learner response:** <what they said>
**Evaluation:** <PASS/PARTIAL/FAIL>
**Gaps identified:** <list with failure mode classifications>

## Teach Phase
### Gap: <name> [<failure mode>]
**Format:** <abbreviated/full/comparison>
**Content:** <summary of what was taught -- for full explanations, summarize the 6 sections>
**Quick Check:** <question> -> Learner: <answer> -> <correct/incorrect>
**Deep-dive:** <if requested, summary of expanded principle>

(repeat for each gap)

## Concept Map
(if generated -- otherwise omit this section entirely)

## Final Test
**Case:** <what was presented>
**Learner response:** <what they said>
**Evaluation:** <PASS/FAIL>

## Result
Status: <complete/needs-review>
Loops: <0/1/2>
```

**C) Delete the checkpoint file.** The session is complete and the final transcript supersedes the checkpoint. Remove `<topic>_checkpoint_SG<N>.md`.

**D) Update the learner profile.** Read `learner_profile.md` from the current directory (create it if it does not exist). Update according to the learner-analytics skill's Update Rules:
1. Update or add the plan row in the Plans table
2. If Initial Test was PASS with zero gaps, add to Strengths
3. For each gap found, update Gap Patterns (increment existing or add new, noting failure mode)
4. Add a Session History entry

**E) Export concept file** (if teaching occurred):
Write a concept file to the current directory using the concept-explainer skill's export format.
- Filename: `concept-<domain>-<sg-topic>.md` (kebab-case)
- Contains: YAML frontmatter (type: ttt-session, session, plan, level, tags) + all teaching content + concept map (if generated) + aggregated CTQ table + session context
- If no teaching occurred (learner passed Initial Test), skip this step

**F) Suggest next step:** Tell the learner which sub-goal to run next (the next pending one in sequence). Mention `/training-status` for overall progress and `/concept-library` to browse saved concept files.

## Important Rules

- ALWAYS append the "not familiar" note AND the "clarification" note at the end of EVERY test (Initial Test and Final Test) -- these two notes are NON-NEGOTIABLE
- NEVER reveal expected answers or "Watch for" hints BEFORE the learner responds -- this applies to ALL questions (Initial Test, Quick Checks, Final Test). Present the question, wait, THEN show the answer.
- NEVER teach before testing -- the Initial Test ALWAYS comes first
- NEVER skip evaluation -- always explicitly state PASS/FAIL with reasons and failure mode classifications
- NEVER combine multiple gaps into one explanation -- one gap, one concept explanation
- ALWAYS assess gap complexity before choosing teaching format (abbreviated vs full vs comparison)
- ALWAYS use CTQ failure mode taxonomy when naming gaps in EVALUATE
- ALWAYS wait for learner responses at: Initial Test, each Quick Check, Final Test
- ALWAYS update the plan file and write the transcript at the end
- ALWAYS check for an existing checkpoint file before starting -- offer to resume if one exists
- ALWAYS write/update the checkpoint after each phase completes
- ALWAYS delete the checkpoint file after a successful RECORD phase
- ALWAYS update the learner profile during RECORD
- ALWAYS export a concept file during RECORD if teaching occurred
- MENTION the deep-dive option once after the first teaching block -- never repeat the offer
- OPTIONALLY offer a concept map after the TEACH phase -- never insist, just offer once
