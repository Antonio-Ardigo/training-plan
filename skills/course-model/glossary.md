# Glossary

Words the learner sees, and the older words they replace. Use the words in the first column in everything the learner reads: chat, pages, overview, notes, practice books. The `course.json` field is given where one exists.

| Say | Meaning | Field | Replaces |
|---|---|---|---|
| **Course** | One learning goal and everything that teaches it | `course` | training plan |
| **Lesson 3** | One numbered step of the course, with its own tests | `lessons[]` | sub-goal, SG-3 |
| **Goal** | What the learner will be able to do, in at most 15 words | `course.goal` | SMART goal |
| **Level** | High school, Master's or Advanced: one per course | `course.level` | target level, estimated depth, depth |
| **Method** | Socratic (the learner reaches each idea through questions) or Direct (try first, then the gaps are explained) | `course.method` | pedagogical method |
| Lesson kinds: **Why it matters, Principle, Concept, Tool, Capstone, Background** | What a lesson is for | `lessons[].kind` | Motivation, Core Principle, Key Concept, Tools, Verification axes; prerequisite sub-goal |
| **Principle** | A foundational truth of the topic | `principles[]` | core principle |
| **Key idea** ★ | One of the hardest principles: counter-intuitive, new, or met with a mistaken belief. Taught through the trap, the aha moment and the levels | `key_idea` | hard core |
| **The trap** | The natural, confident, wrong answer the key idea's first test leads to | `design.trap` | tempting answer, designed wrong path |
| **The aha** | The one sentence that makes the idea click | `design.aha` | insight |
| **Picture** | One picture or analogy for the aha, and where it stops being true | `design.picture` | picture |
| **The aha moment** | The trap shown failing, then the aha, the picture and the first worked example | — | reveal |
| **Levels**, **level by level** | A key idea taught at High school, then up to the course level, each level with a solved example and a Your turn | `design.levels` | level ladder, rungs, climb |
| **Step back** | A short explanation one level down after a wrong Your turn or check | — | bridge, re-explain one level down |
| **Try first** | The test at the start of a lesson, before any teaching | `design.try_first` | initial test |
| **Learn** | The teaching part of a lesson, covering only what Try first showed | — | teach phase |
| **Check**, **Your turn** | A short question after an explanation / at each level | — | quick check, your turn |
| **Show you've got it** | The test at the end of a lesson, on a new case | `design.final_check` | final test |
| **Another round** | Teaching again after a failed Show you've got it (at most two) | `state.rounds` | adaptation loop |
| **What to work on** | What a test showed the learner does not yet have | `state.to_work_on` | gap |
| **Success criteria** | What the learner must be able to do, how it is tested, and the common mistake | `design.success_criteria` | CTQ |
| **Common mistakes**: mixing up two ideas, stretching a rule too far, missing background, steps without the why, words without the maths, maths without the picture | Kinds of mistake | `common_mistake.kind` | failure-mode tags (conflation, overgeneralization, missing-prerequisite, procedural-without-conceptual, verbal-without-formal, formal-without-intuitive) |
| **Worked example**, **Check** (of a solution) | A fully solved example; its last line confirms the result a second way | `worked_example` | foundational worked example |
| **Go deeper** | A fuller explanation the learner asks for | — | deep-dive |
| **Start from scratch** | The learner's choice to be taught before trying | verdict `start-from-scratch` | "not familiar" |
| **What does this word mean?** | A definition that does not give the answer away | — | clarification |
| **Add a background lesson** | Offer to add a lesson for missing background | kind `background` | plan revision, prerequisite sub-goal |
| **Course overview** | Why it matters, what you will learn, what you will be able to do | `overview` | VOC, motivation & course overview |
| **The story** | Before, the aha, what it solved | `story` | breakthrough |
| **Facts to know** | What must simply be known | `facts` | key facts |
| **Background** | Knowledge the course assumes | `background` | prerequisites |
| **Lesson design** | Everything prepared for a lesson. Never shown before the lesson | `design` | session blueprint |
| **Puzzle** | Socratic: the question that makes the learner feel the gap | `design.puzzle` | discovery question |
| **The clash**, **the way out** | Socratic: where the first attempt fails / the idea that resolves it | — | tension, resolution |
| **Guiding questions** | Socratic: three to six questions that lead to the idea | `design.guiding_questions` | Socratic guidance chain |
| **Explain it back** | Socratic: rebuild the reasoning in your own words at the end | `final_check.marking.explain_it_back` | reconstruct the reasoning |
| **Lesson page**, **course app** | Where lessons are taught; chat is the fallback | `delivery` | visual delivery, page |
| **Files** | Everything the course has written | `files` | artefacts register, artefacts |
| **Practice book** | A lesson's solved exercises, added to over time | kind `practice` | exercise book |
| **Lesson notes**, **Notes** | What a lesson taught / all of them | kind `notes` | concept file, concept library |
| **Idea map** | How the ideas of a lesson connect | — | concept map |
| **Your progress** | Computed across courses; not stored | — | learner profile, training status |
| **Saved place** | Where an unfinished lesson resumes | `state.step`, `state.saved` | checkpoint |
| **Lesson record** | A readable account of a lesson, written on request | kind `record` | session transcript |
| **Not started, In progress, Done, Review** | Lesson status | `state.status` | pending, complete, needs-review |
