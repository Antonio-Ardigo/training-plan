# Converting a 3.x Training Plan

`tools/course.py convert` implements this table. Use it by hand only when Python is not available.

## Plan sections

| 3.x plan | `course.json` |
|---|---|
| File name `<topic>_training_plan.md` / `<topic>-socratic_training_plan.md` | `course.id` = topic slug; `course.method` = `socratic` for the second form or a `## Pedagogical Method: Socratic Discovery` section, else `direct` |
| `# Training Plan: <title>` | `course.title` |
| `Generated: <date>` | `course.created` |
| `Target level:` (or, in plans before 3.0, the first Estimated Depth: introductory / intermediate / advanced) | `course.level`: `high-school` / `masters` / `advanced` |
| `## Learning Goal` | `course.goal_as_given` |
| `## SMART Goal` | `course.goal` |
| `## Motivation & Course Overview (VOC)`: Why this matters / Bird's-eye view / Core principles & key facts / What you'll be able to do | `overview.why_it_matters` / `what_you_will_learn` / `principles_and_facts` / `you_will_be_able_to` |
| `## Breakthrough`: Before the intuition / The intuition / What it solved, and the per-principle table | `story.before` / `the_aha` / `what_it_solved` / `by_principle` |
| `## Principle Extraction` rows | `principles[]`: name, statement, formal, needs (the Prerequisites cell) |
| `## Hard Core` rows | `principles[].key_idea: true` and `why_hard` |
| `## Key Facts` rows (`(verify)` marks) | `facts[]` with `used_in` renumbered, `verify` |
| `## Prerequisite Graph`, `requires:` lines | `background[]` |
| `## Sequence` (free text: needs, depends on, after, arrows) | `lessons[].needs`; a lesson with none found needs the principle lessons of its principles |
| `## Sub-Goals` rows: Axis, Sub-Goal, Domain, Difficulty, Principle, Status | `lessons[]`: `kind` (Motivation→`why`, Core Principle→`principle`, Key Concept→`concept`, Tools→`tool`, Verification→`capstone`), `goal`, `area`, `difficulty`, `principles`, `state.status` (pending→`not-started`, complete→`done`, needs-review→`review`) |
| `## Artefacts Register` | `files[]`, after copying (below) |
| `## Progress Log` entries | `state` of the lesson: `finished`, `status`, `attempts` (Initial and Final Test, `source: converted`), `to_work_on` (Gaps found), `level_reached`, `delivery`, `rounds` (Loops), `notes` |

## Blueprint fields (`### SG-N: <title>`)

| 3.x field | `lessons[].design` |
|---|---|
| title | `lessons[].title` |
| Context (why it matters, historical context; plans from 3.8) | `context` |
| Principle | `principle_statement` |
| Discovery Question | `puzzle` |
| Initial Test + Pass Criteria | `try_first.question`, `try_first.marking.pass` |
| Socratic Guidance Chain | `guiding_questions` |
| Tempting answer | `trap`, also `try_first.marking.trap` (key ideas only) |
| Insight | `aha` |
| Picture | `picture` |
| Visual design (Objects, Colour roles, Steps, Your-turn inputs, Control) | `visual` (`objects`, `colour_roles`, `steps`, `your_turn`, `control`) |
| Worked Example (foundational): Given, Step n, Why, Result, Check | `worked_example` (`given`, `steps[{do, why}]`, `result`, `check`) |
| Level ladder: Master's / Advanced solved exercise | `levels[{level, example}]` |
| Exercise | `practice_task` |
| Anticipated CTQs: CTQ, Source, Mastery Test, Common Failure Mode | `success_criteria[{what, from, how_tested, common_mistake{kind, text}}]` |
| Teach Topics | `to_teach` |
| Final Test | `final_check.question`; `final_check.marking.pass` asks for the same standard on the new case, without copying Try first's values (lesson-flow works out the right values of the new case when it marks); a Socratic course adds `explain_it_back` |
| Estimated Depth | dropped: the course has one level |

Failure-mode tags become common-mistake kinds: conflation → `mixing-up`, overgeneralization → `overstretching`, missing-prerequisite → `missing-background`, procedural-without-conceptual → `steps-without-why`, verbal-without-formal → `words-without-maths`, formal-without-intuitive → `maths-without-picture`. A mistake written in another form keeps its text with `kind: null`.

## Files (copied, never moved)

| 3.x file | Course file |
|---|---|
| `<topic>_session_SG<N>.md` | `lessons/NN-slug/record.md` (`record`) |
| `concept-<domain>-<topic>.md` | `lessons/NN-slug/notes.md` (`notes`) |
| `<topic>_artefact_SG<N>_exercises.md` | `lessons/NN-slug/practice.md` (`practice`) |
| `<topic>_visual_SG<N>.html` | `lessons/NN-slug/page.html` (`lesson-page`) |
| other `<topic>_artefact_SG<N>_<slug>.md` | `lessons/NN-slug/<same name>` (`other`) |
| `<topic>_checkpoint_SG<N>.md` | not copied: the lesson becomes `in-progress`, `step` from its Current Phase, the checkpoint text in `saved` |
| `learner_profile.md` | not copied: progress is computed |
| the plan itself | listed as `old-plan`, left where it is |
