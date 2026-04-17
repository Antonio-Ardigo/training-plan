# Training Plan Plugin

Generate customized learning paths using **Test-Teach-Test (TTT)** methodology with integrated concept-builder pedagogy.

## How It Works

1. You provide a learning goal
2. The plugin decomposes it into testable sub-goals with CTQ mastery criteria
3. For each sub-goal, you run a TTT session:
   - **Test** -- face a practical case immediately (no theory first)
   - **Teach** -- get principle-first concept explanations for your gaps (adaptive: abbreviated for simple gaps, full 7-section with LaTeX, Worked Examples, and CTQ for complex gaps, comparison for conflation)
   - **Test** -- prove mastery with a new case
4. Each Teach phase generates a concept file documenting what was taught
5. Sessions save checkpoints -- if interrupted, resume from where you left off
6. A learner profile tracks your progress, strengths, and gap patterns across all plans
7. A concept library tracks your learning artifacts across all sessions

## Commands

### `/create-training-plan <learning goal>`

Creates a full training plan with sub-goals, session blueprints, CTQ criteria, and depth levels. If a learner profile exists, it informs the plan design (harder tests for known strengths, proactive coverage for known weaknesses).

Example:
```
/create-training-plan I want to learn cost estimation for EPC construction projects
```

### `/socratic-training-plan <learning goal>`

Creates a Socratic training plan using the same goal decomposition structure as `/create-training-plan` (SMART goal, principle extraction, 5-axis decomposition, prerequisite graph) with a **Socratic Discovery** layer. Each session follows a **Question -> Tension -> Resolution -> Test** arc where concepts emerge as inevitable discoveries rather than delivered facts. Blueprints include Discovery Questions, designed "wrong paths," Socratic Guidance Chains (3-6 progressively narrowing questions), and "reconstruct the reasoning" final tests.

Example:
```
/socratic-training-plan Derive quantum mechanics from experimental spectra
```

### `/run-session <sub-goal>`

Runs an interactive TTT session for one sub-goal. Teaches using concept-builder methodology (Problem, Principles, Innovations, Worked Example, Formalization, CTQ, Conceptual Map). Saves checkpoints after each phase. Exports a concept file on completion.

Example:
```
/run-session SG-2
/run-session unit-rate estimation
```

### `/training-status`

Shows your cross-plan learning analytics: completion rates, strengths, recurring gap patterns, and recommendations for what to study next.

### `/concept-library [list|search|path|link]`

Manage concept files generated during sessions: browse your library, search by keyword, build learning paths between concepts, or link related concept files.

Example:
```
/concept-library list
/concept-library search "indirect costs"
/concept-library path "cost classification" "earned value"
```

## Architecture

- **1 agent**: `training-planner` (orchestrator)
- **5 skills**: `goal-decomposer`, `ttt-session`, `content-builder`, `concept-explainer`, `learner-analytics`
- **5 commands**: `/create-training-plan`, `/socratic-training-plan`, `/run-session`, `/training-status`, `/concept-library`

## Output Files

| File | Content |
|------|---------|
| `<topic>_training_plan.md` | Plan + progress tracking |
| `<topic>-socratic_training_plan.md` | Socratic plan + progress tracking |
| `<topic>_session_SG<N>.md` | Session transcript per sub-goal |
| `<topic>_checkpoint_SG<N>.md` | In-progress session checkpoint (deleted on completion) |
| `learner_profile.md` | Persistent learner profile across all plans |
| `concept-<domain>-<topic>.md` | Concept file from Teach phase (per session with gaps) |

## Concept-Builder Methodology

The Teach phase uses a principle-first approach adapted from the concept-builder methodology:

1. **The Problem** -- why the gap matters (framed in learner's context)
2. **Core Principles** -- foundational truths (with LaTeX at intermediate+ levels)
3. **Key Innovations** -- breakthroughs and techniques
3.5. **Worked Example** -- fully developed step-by-step example with every intermediate step shown and annotated (always included)
4. **Intuitive Formalization** -- minimum math needed for prediction
5. **CTQ Mapping** -- mastery criteria with failure mode awareness
6. **Conceptual Map** -- visual structure of learned concepts

Teaching is **adaptive**: simple gaps get abbreviated treatment (Problem + Principles + Worked Example + Quick Check), complex gaps get the full 7-section explanation, and conflation gaps get a side-by-side comparison.

During a session, learners can request a **deep-dive** into any taught principle for a full expanded explanation.

## Learning Science

See [PRINCIPLES.md](PRINCIPLES.md) for the cognitive science behind TTT and how this plugin addresses common learning risks (testing effect, desirable difficulty, fluency illusion, metacognitive blindness).
