---
name: course-design
description: How a course is designed from a learner's goal, in the Socratic method (the default) or the Direct method - goal, level, principles, facts to know, the story, lessons and their needs, key ideas, every lesson's design, the course overview and the checks before the course is shown. Use when creating a course from a goal, and when the learner asks to change a course's design, its overview or its list of key ideas.
---

# Course Design

This skill turns a learner's goal into a complete, valid `course.json`. It owns every rule about what a course contains and how each part is designed. Three other skills own the rest:

- **course-model** owns the file: folder layout, field names, the tool, validation. Field definitions are in its `course.schema.json`; this skill never restates them.
- **lesson-flow** owns how a lesson is run.
- **explaining** owns how an explanation is written, including what each level adds.

The course names and motivates. It does not teach. The only teaching it holds is the worked example of each principle lesson and the key-idea fields (the trap, the aha, the picture, the visual design and the levels). The story and the facts to know are orientation: state them, never teach from them.

## 1. The method

Choose the method first. It changes a few fields of every lesson. The design steps are the same for both.

| Method | How an idea reaches the learner | Used when | `course.method` |
|---|---|---|---|
| **Socratic** (default) | Through a puzzle and guiding questions, so that the learner states the idea before it is explained | The goal does not ask for Direct | `socratic` |
| **Direct** | Try first, then what to work on is explained | The goal contains the word `direct`, or the learner asks for direct explanation or for "no Socratic" | `direct` |

Remove the word `direct` from the goal before refining it. Tell the learner in one line which method the course uses, and that adding `direct` to the goal gives the Direct method.

A Socratic lesson follows one arc: the **puzzle** makes the learner feel the gap; the learner's first attempt meets **the clash**, a failure the design provokes on purpose; **the way out** is the idea, reached as the only thing that resolves the clash; **Show you've got it** asks the learner to rebuild the reasoning. Rows and bullets marked *Socratic only* below apply to Socratic courses alone.

## 2. Design steps

Do the steps in order. Each says which part of `course.json` it fills.

### Step 1. Refine the goal → `course.goal`, `course.goal_as_given`, `course.title`, `course.id`

- `goal_as_given` is the goal exactly as the learner typed it.
- `goal` is at most 15 words. It names the exact competency, implies an outcome someone can observe, has a realistic scope, matches what the learner wants, and includes a timeframe if the learner gave one.
- `id` is a short lowercase slug of the topic (`cost-estimation`, `transformer-attention`). The method and level go in their own fields, never in the id.

### Step 2. Choose the level → `course.level`

| Level | The course assumes | It takes the learner to |
|---|---|---|
| **High school** (`high-school`) | School mathematics; no earlier exposure to the topic | The idea in plain words, with pictures and concrete numbers |
| **Master's** (`masters`) | The field's standard tools and notation | The formal statement, where it comes from, and problem solving in symbols |
| **Advanced** (`advanced`) | The Master's level, mastered | Full generality: proofs, limits of validity, competing formulations |

- If the goal states a level ("at master's level", "for high-school students", "advanced"), use it.
- Otherwise ask once: "Which level should this course take you to: High school, Master's or Advanced?" Wait for the answer.
- If you cannot ask (a run with no learner present), use Master's and say so in the summary.
- The level is fixed for the course. The goal, every lesson, every test and every pass standard are written for it. Nothing above it goes into the course.

### Step 3. Read earlier progress → notes for Step 10 and the summary

Compute the learner's progress as course-model section 5 describes: `python3 <course-model>/tools/course.py progress .` when Python is available, otherwise read every `*/course.json` below the working folder. A `learner_profile.md` from version 3.x counts too. With no earlier course, skip this step.

Note three things for later steps:

| Found | Use |
|---|---|
| Strengths (lessons passed at Try first) related to this goal | Make Try first harder in the related lessons, and say so in their `to_teach` |
| Kinds of common mistake that recur (two or more lessons) related to this goal | In the related lessons' `to_teach`, add a check on that mistake even if Try first does not show it |
| Background (Step 8) that progress does not show the learner holds | A warning in the summary, and in that `background[].note` |

### Step 4. Principles → `principles[]`

Find the topic's **3 to 5 principles**: the foundational truths it rests on.

| | Principle | Concept (taught in a concept lesson) | Fact to know |
|---|---|---|---|
| What it is | A truth of the whole topic, stated without any technique or tool: the *why* | A specific idea that puts a principle to work: the *what* and *how* | Something the learner must simply know |
| Scope | Broad, rarely changes | One testable competency; may change with methods and tools | One value, definition or convention |
| Tested by | Reasoning | A practical case | Nothing on its own: tests use it |

- Order principles from the most fundamental to the most derived. Number them `P1`, `P2` ...
- Each has a short `name`, a one-sentence `statement`, a `formal` statement in LaTeX where one exists, and `needs`: the background knowledge it relies on (Step 8).
- Each must be testable on its own.
- Fewer than 3 principles means the goal may be too narrow. Say so to the learner.
- Every concept traces back to at least one principle. One principle may give rise to several concepts.

### Step 5. Facts to know → `facts[]`

A fact to know cannot be worked out from the principles, yet the principles cannot be applied without it: a definition, a constant, a conversion factor, a convention, a threshold or standard value, a classification, a name or a date.

- For each principle ask: "What must the learner already know as a fact to apply this?" Then add any fact the practical cases need that no principle covers.
- One fact per entry, stated exactly, with its value and SI unit where it has one. Number them `F1`, `F2` ...
- `why_it_matters` says what breaks without the fact. It never says why the fact is true.
- A fact is never a principle in disguise (leave out anything a principle in this course yields), never background (that goes in the principle's `needs`), never vocabulary (lessons define their terms) and never a concept (concepts get lessons).
- Tests use facts. They never ask the learner to recite one. Facts get no lesson of their own.
- Usually 4 to 10. Never pad the list.
- Never guess a value. Set `verify: true` on any number, date or name you are not certain of, so the learner checks it against a source.
- `used_in` is filled in Step 14, once the lessons exist.

### Step 6. The story → `story`

A principle is easier to grasp and remember as the answer to a problem. The story tells that problem.

- For the whole topic: `before` (what people did or believed, and where it broke down), `the_aha` (the idea that changed the picture, in plain words), `what_it_solved` (what became possible). One or two sentences each.
- `by_principle`: one entry per principle, with its id, `before` (the earlier view or practice it replaced, and how that failed) and `what_it_solved`. The principle's statement is its aha, so the entry adds only the before and the after.
- It is the real history. Name people and dates only when you are certain of them; otherwise describe the change without names.
- A topic with no single historical moment (a practical skill, a tool, a procedure): `before` is how the work is done without this knowledge, and where that breaks down.
- A story, not a lesson: no derivations, formulas or worked steps.
- The story is never reused as a test case.
- *Socratic only:* the story names *what* was found. It never tells the reasoning that leads there and never describes a lesson's designed wrong path.

### Step 7. Lessons → `lessons[]`: `kind`, `title`, `goal`, `area`, `difficulty`, `principles`, `key_idea`

| Kind | What it is for | How many | Where |
|---|---|---|---|
| `why` (Why it matters) | Why the topic matters, built on the real history in the story | 1, sometimes 2 | First |
| `principle` | One principle, stated and applied in one simple case | Exactly 1 per principle | After the why lesson, in principle order |
| `concept` | One concept that puts a principle to work | As many as the topic needs, often 2 to 8 or more | After the principle lessons they rest on |
| `tool` | A technique, framework, piece of software or instrument | 0 to 3, only when the goal involves tools | After the concepts they serve |
| `capstone` | Proof of mastery, combining several lessons | 1, sometimes 2 | Last |

A course usually has 7 to 15 lessons or more. The kind `background` is added only later, when the learner asks for it (section 6).

Rules for every lesson:

- `goal` is at most 15 words, names one competency with an outcome someone can observe, and is clearly part of the course goal. "Understand cost estimation" is too vague; "Learn everything about piping, structural and electrical estimation" is too broad and must be split.
- *Socratic only:* phrase each `goal` as a discovery ("Discover why ..."), never as passive learning ("Learn about ...").
- One testable idea per lesson. A concept with independent parts is split.
- **Testability check:** "Can I design a practical case that a competent person could solve, and that would fail if this lesson's knowledge were missing?" If not, the lesson is too vague, too broad or not testable on its own: refine or split it.
- `principles` lists the principles the lesson tests. A principle lesson names exactly its own principle. Every concept lesson names at least one principle that has a principle lesson; if it cannot, the principle list is incomplete or the lesson is not needed. The why lesson may name none; the capstone names the principles it combines.
- `area` is a short label for the part of the field the lesson belongs to.
- `difficulty` is derived, never guessed. It says how much a lesson combines:

| | `low` | `medium` | `high` |
|---|---|---|---|
| Principles involved | 1 | 2 to 3 | 4 or more |
| Depth of the chain of needs | 0 to 1 | 2 to 3 | 4 or more |
| Mathematics | None or little | Standard notation | Proofs, derivations |

- A principle lesson is always `low`: one principle, one simple case. This is a fixed rule.
- Difficulty never sets the level. Every lesson is at the course level: an easy lesson gets a shorter explanation, never a lower level. A lesson that needs mathematics above the course level is out of scope: leave it out, or restate it at the course level.
- Number lessons `L1`, `L2` ... in the order Step 8 gives.

### Step 8. Needs between lessons and background → `lessons[].needs`, `background[]`

Build the principle graph, then read the needs off it. Every need traces to an edge of the graph; never add a need from intuition.

| Edge | Meaning | Becomes |
|---|---|---|
| A principle **relies on** outside knowledge | Knowledge the course assumes and does not teach (from `principles[].needs`) | An entry in `background[]` |
| A lesson **rests on** a principle of this course | The lesson cannot be learnt before that principle | The lesson needs that principle's lesson |
| Principle B **follows from** principle A | B builds on A | B's principle lesson needs A's |

Then order the lessons: the why lesson first; principle lessons in the order of the graph; each concept lesson after the principle lessons it rests on; tools after the concepts they serve; the capstone last, needing every earlier lesson it combines. Two lessons with no edge between them may be taken in either order.

### Step 9. Key ideas → `principles[].key_idea`, `principles[].why_hard`, `lessons[].key_idea`

A key idea ★ is a principle much harder to grasp than the rest. It is taught through the trap, the aha moment and the levels (Step 11). A principle is a key idea when it meets at least one criterion:

| Criterion | The principle ... |
|---|---|
| **Counter-intuitive** | contradicts what everyday experience or earlier study leads the learner to expect |
| **New abstraction** | cannot be stated without a representation the learner has not used before |
| **Persistent misconception** | runs into a well-known wrong idea that people keep even after being told the right one |

**and** it passes the gate: *"Can I write the trap: what a capable person who does not yet know this principle would confidently, and wrongly, answer to a concrete case?"* With no trap there is nothing to predict and see fail, so the principle is not a key idea.

- Usually 1 to 3. When more qualify, keep the ones that the most later lessons need in the graph, and add **load-bearing** to their reasons.
- Zero is allowed for a procedural or tool-centred topic. Say so plainly; never force one.
- Only principles can be key ideas, never concepts.
- A key idea is about how hard an idea is to grasp. Difficulty is about how much a lesson combines. A key idea's principle lesson stays `low`.
- `why_hard` gives the reasons as criterion names only: counter-intuitive, new abstraction, persistent misconception, load-bearing (with load-bearing you may add how many lessons need it). It never describes the misconception, the trap or the aha: the overview shows this field, and it must not give a test away.
- Set `key_idea: true` on the principle and on its principle lesson.

### Step 10. Design each lesson → `lessons[].design`

Design every lesson; none is left without a design. Every test is written at the course level: its case, its task and its pass standard assume that level's tools. Use the notes from Step 3.

| Field | Lessons | What it holds |
|---|---|---|
| `context` | All | The lesson's opening, shown before any question. *Why it matters*: one or two sentences on what the lesson lets the learner do. *How we got here*: two to four sentences on the real situation the idea came out of: what was done before, where it broke down, who changed it and when (names and dates only when certain). It stops before the idea: it states no answer to the lesson's tests and names no mechanism, formula, number or conclusion they ask the learner to find. Write it after the tests and check it against them |
| `principle_statement` | Principle | The principle's name and statement |
| `puzzle` | *Socratic only*, all | See Step 12. `null` in a Direct course |
| `try_first` | All | `question`: a practical case the learner solves at once, with no theory first. `marking.pass`: a concrete, measurable standard ("identifies 8 of 10 categories", "within 5%"), with the right values |
| `try_first.marking.trap` | Key idea; *Socratic only*, every lesson that has one | The wrong answer the test is built to provoke. For a key idea, a copy of `design.trap`. Otherwise `null` |
| `guiding_questions` | *Socratic only*, all | 3 to 6 questions (Step 12). Empty in a Direct course |
| `worked_example` | Principle (required), key idea | A fully solved example in the simplest case that makes the principle visible: `given`; 2 to 4 `steps`, each with `do` and `why`, every step shown, concrete numbers; `result`; `check`, which confirms the result a second way. *Socratic only:* phrase each `why` as the answer to a question the learner would ask at that step. Other lessons: `null` |
| `practice_task` | All | A short, concrete, self-contained exercise the learner can do in 5 to 10 minutes, with clear instructions and the expected outcome. It is practice, not a test, and differs from both tests |
| `success_criteria` | All | 2 to 4 entries (1 or 2 for a principle lesson; for a key idea, at least one per level from High school up to the course level, the level named in `from`). Each has `what` must be understood, `from` (the principle or part it comes from), `how_tested`, and `common_mistake` with its `kind`: `mixing-up`, `overstretching`, `missing-background`, `steps-without-why`, `words-without-maths` or `maths-without-picture` |
| `to_teach` | All | What the lesson teaches if Try first shows it is needed: the concepts and the known pitfalls, each tagged with its common-mistake kind, and what to teach again when that mistake appears. Principle lesson: the principle, its limits and the usual misunderstandings. Key idea: the misunderstandings that survive the aha. Notes from Step 3. *Socratic only:* a teaching note that prefers a leading question to a statement ("What operation on ψ gives a non-negative number that sums to 1?" rather than "The Born rule states P = \|ψ\|²") |
| `final_check` | All | `question`: a different case that tests the same competencies. `marking.pass`: the Try first standard applied to the new case. *Socratic only:* the question has at least one part that asks "why" or "what would happen if", and `marking.explain_it_back` says what the learner must rebuild. Direct: `explain_it_back` is `null` |

What each kind's tests ask:

| Lesson | Try first asks | Pass standard | Show you've got it |
|---|---|---|---|
| Why it matters | To predict or explain what the earlier approaches in the story really do, never to recite the story | As the table above | A new case built on the same real history |
| Principle | To state the principle in own words and apply it to one simple case; simpler than concept tests | States it and applies it correctly. *Socratic:* and explains why the designed wrong path fails | A different simple case for the same principle |
| Key idea | To predict and justify, in a case at the course level where the natural approach leads to the trap. No warning and no hint that the obvious answer is wrong | Gives the right answer, not the trap, and justifies it at the course level. *Socratic:* and explains why the trap fails | A different case at the course level where the same trap is again available |
| Concept, tool, capstone | To solve a practical case. *Socratic:* the first instinct leads to a partial or wrong answer, and the gap shows exactly which idea is needed | As the table above | A different case, same competencies |

### Step 11. Design each key idea → `design.trap`, `aha`, `picture`, `visual`, `worked_example`, `levels`

A key-idea lesson is a principle lesson with these fields added. No other lesson has them. In a lesson the learner predicts, the prediction fails, and the explanation starts from that failure (lesson-flow runs it; explaining writes each level).

| Field | Rule |
|---|---|
| `trap` | The natural, confident, wrong answer to Try first, and why it feels right. It is the answer a capable person gives before knowing the principle. *Socratic:* it is also the designed wrong path that the puzzle and Try first lead to. Copy it into `try_first.marking.trap` |
| `aha` | One sentence that makes the idea click. It reframes the situation and does not recite the formal statement. Test it by reading it alone: it should make the failure look obvious in hindsight. *Socratic:* it is the sentence the guiding questions lead the learner to say |
| `picture` | One picture or analogy that carries the aha, concrete and familiar at High school level, and where it stops being true. An unstated limit becomes the next misconception |
| `worked_example` | The High school level's example, and the smallest example of the aha: remove everything not needed to see it |
| `levels` | One solved example for each level above High school, up to the course level: none for a High school course, `masters` for a Master's course, `masters` then `advanced` for an Advanced course. Each shows the same idea with that level's tools, never a harder calculation at the level below. Same parts as a worked example, ending with a `check` |
| `visual` | How the key idea is shown on a lesson page, in five parts. `objects`: what is drawn, kept tiny, with exact values. `colour_roles`: one colour per role, at most three. `steps`: the order in which objects appear, one sentence each. `your_turn`: for each level, what the learner enters, the right value, and the two most likely wrong values with what each reveals. `control`: the one thing the learner can change, and what it shows. Design it from the picture and the solved examples. It adds no teaching of its own. Every Your turn uses a new case, with values used nowhere else in the course |

After writing a key idea, re-read its `story.by_principle` entry. If it states the trap or the test case, rewrite it at the level of history or practice.

### Step 12. *Socratic only:* puzzle and guiding questions → `design.puzzle`, `design.guiding_questions`

- **Puzzle.** A case that creates real puzzlement before any theory. It makes the learner want the idea: the natural first attempt fails or falls short, and that clash is what the idea resolves. Never "What do you know about X?". In a principle lesson, the puzzle is one only this principle resolves. In a key-idea lesson, the designed wrong path is the trap.
- **Designed wrong path.** Try first contains a plausible, wrong approach whose failure brings out the idea. Write it in `try_first.marking.trap`. It is required in principle and key-idea lessons and used wherever a lesson has one.
- **Guiding questions.** 3 to 6 questions for when the learner is stuck. Each gives no answer, narrows the search, and builds on the one before. The last makes the conclusion inescapable. In a key-idea lesson they lead to the aha.
- **Explain it back.** Show you've got it asks the learner to rebuild the reasoning; `final_check.marking.explain_it_back` names what must be rebuilt.
- The overview and the story name what is discovered. They never spoil a puzzle.

### Step 13. Test quality → every puzzle, test, guiding question, Your turn and practice task

| Rule | Means |
|---|---|
| One clear question | It asks one thing, says plainly what is asked, and says what form the answer takes (a number, a choice, one sentence). A reader who knows the answer can tell that it answers the question. Nothing depends on guessing what the author meant |
| A true case | The case is built on something really done: a method that was in use, a real system's behaviour, a real engineering decision. Never invent a method nobody uses in order to knock it down. Every statement in the case is true outside the toy example; when a toy simplifies, say what was simplified |
| The real history | The why lesson's puzzle and tests use the actual problem the topic solved, as the story tells it, with the earlier approaches named as they were |
| New cases | No test, Your turn or practice task reuses a case whose answer is worked out elsewhere in the course. Solved examples do not reuse each other's case |
| Facts are listed | When a test or exercise relies on a fact, that fact is in `facts`. If it is missing, add it |

### Step 14. Facts' use and the course overview → `facts[].used_in`, `overview`

First fill each fact's `used_in` with the lessons whose tests or exercises rely on it. Drop any fact no lesson uses.

Then write the course overview. It comes last so that it matches the lessons.

| Field | Content |
|---|---|
| `why_it_matters` | 1 to 3 sentences on the real-world stakes |
| `what_you_will_learn` | 2 to 4 sentences on what the course covers end to end and how the lessons connect into one arc |
| `principles_and_facts` | A plain-words digest of the principles and the most load-bearing facts to know |
| `you_will_be_able_to` | Concrete abilities, tied to the course goal and the capstone |

- The overview is for the whole course. It is separate from Lesson 1, which stays a lesson with its own tests.
- It informs. It holds no test, no theory and no teaching.
- The learner may edit it (section 6).

## 3. Writing and validating the file

1. Load the **course-model** skill. Read `example-course.json` and `course.schema.json` in its folder. If the folder cannot be read, print them with `python3 <course-model>/tools/course.py example` and `... schema`. Find the tool with Glob (`**/course-model/tools/course.py`).
2. Choose the folder `<course-id>/`. If `<course-id>/course.json` already exists, never overwrite it without asking. Ask whether to replace it or keep both; to keep both, add a suffix to the new id (`-2`, or the level: `-hs`, `-msc`, `-adv`).
3. Write `<course-id>/course.json` with the shape of `example-course.json` (course-model section 3). Use its field names and nesting exactly. Never invent, rename or add a field. Also set:
   - `course.method` (section 1), `course.created` (today), `course.delivery`: `app`, or `chat` if the learner asked for chat.
   - every lesson's `state` as a not-started lesson, copied from the example;
   - Direct: `puzzle: null`, `guiding_questions: []`, `explain_it_back: null`;
   - `files`: one entry for `overview.md`, kind `overview`;
   - `history`: one entry, `Course created`, dated today.
   Do not write any Markdown version of the course.
4. Run `python3 <course-model>/tools/course.py validate <course-id>/course.json --files`. Fix every error and run it again until it prints `OK`. Read the warnings: a warning about a missing design part is fixed now.
5. Run `python3 <course-model>/tools/course.py render-overview <course-id>/course.json`.
6. Without Bash or Python: compare every field name with the example and the schema, check course-model section 4 by hand, write `overview.md` as course-model section 5 describes, and tell the learner the course was checked by hand. The overview never contains a test, a marking guide or a solution.

## 4. The required-elements check

A course that fails a row is incomplete. Check every row in `course.json`; fix the file, validate again, and report the result to the learner in one line per row.

| Element | Holds when |
|---|---|
| Principles | 3 to 5 principles. Each has exactly one lesson of kind `principle`, and every principle lesson names its principle |
| Lessons trace to principles | Every concept lesson names at least one principle; every `needs` entry follows the principle graph |
| Facts to know | `facts` has at least one entry, every `used_in` names an existing lesson, and every fact is used |
| Course overview | `overview` has its four parts filled in |
| Why it matters | Lesson 1 is of kind `why` and is built on the real history in `story` |
| Context gives nothing away | Every lesson has a `design.context`. Read against the lesson's puzzle, Try first and Show you've got it, it names the problem and the history and states none of the answers |
| The story | `story` has `before`, `the_aha` and `what_it_solved`, and one `by_principle` entry per principle, none stating a trap or a test case |
| Method | `course.method` is set; every lesson has `try_first` and `final_check`. Socratic: every lesson has a `puzzle`, 3 to 6 `guiding_questions` and `final_check.marking.explain_it_back`. Direct: `puzzle` is `null` and `guiding_questions` empty |
| Level | `course.level` is set, and every test and pass standard is written for it |
| Key ideas | At least one principle has `key_idea: true`, unless none passed the gate (then say so). Every key-idea lesson has `trap`, `aha`, `picture`, `visual`, a `worked_example` and the right `levels` for the course level, each example ending with a `check`. No other lesson has these fields. `why_hard` holds criterion names only |
| Test quality | Every question asks one thing and states the form of the answer; every case is something really done, with no invented method to knock down |
| New cases | No test, Your turn or practice task reuses a case whose answer is worked out elsewhere in the course |
| Valid | `course.py validate` prints `OK` and `overview.md` is regenerated |

## 5. What to tell the learner

After the course is written and checked, show:

- the course goal;
- the level, and if it was not stated and you could not ask, that Master's was assumed and the course can be created again at another level;
- the method in one or two sentences (Socratic: puzzle, clash, way out, explain it back; Direct: Try first, Learn, Show you've got it);
- the course overview, with an invitation to edit it: edits are welcome, and feedback on it may restructure the course;
- the story: before, the aha, what it solved;
- the principles, as a short table;
- the key ideas ★ and their reasons, and that each is taught through the trap, the aha moment and the levels. Ask the learner to confirm the list or change it;
- the facts to know: how many, and which are marked to verify against a source;
- the lessons, as a table (number, kind, title, goal);
- any background warnings from Step 3;
- what earlier progress changed in the design, if anything;
- the result of the required-elements check, one line per element;
- where the course is: `<course-id>/course.json`, with the readable outline in `<course-id>/overview.md`;
- the lesson to start with, and how to start it (`/run-session 1`).

Never show a trap, a test, a marking guide or a solution here.

## 6. Changes the learner asks for afterwards

Every change ends the same way: validate until `OK`, render the overview, re-run the required-elements check, and add one `history` line.

| The learner ... | Do |
|---|---|
| Edits the course overview or gives feedback on it | Store the request in `overview.learner_notes`. Check whether the lessons still match the stated scope and outcomes. If they no longer do, offer to restructure the course with the steps above; never restructure without asking. A restructure updates the lessons and their needs, the story entries and the key ideas if the principles changed, the facts' `used_in`, and the overview digest |
| Adds a key idea | Apply the gate (Step 9). If a trap can be written, set `key_idea` and `why_hard`, add the key-idea fields (Step 11) to its principle lesson, and rebuild Try first and Show you've got it on the trap (Socratic: the puzzle and the guiding questions too). If not, say why the principle cannot be taught that way |
| Removes a key idea | Set `key_idea: false` and `why_hard: null` on the principle and its lesson. Remove `trap`, `aha`, `picture`, `visual` and `levels` (set them to `null` or `[]`), and clear `try_first.marking.trap` in a Direct course. Restore the principle lesson's tests (Step 10; Socratic: a designed wrong path of its own). Keep the worked example. No restructure is needed |
| Wants another level or method | Create the course again with that level or method, in a new folder, as section 3 step 2 describes |

---

**Older names.** Courses before version 3.10 used other words: training plan (course), sub-goal (lesson), blueprint (lesson design), hard core (key ideas), tempting answer (the trap), insight (the aha), breakthrough (the story), VOC (course overview), CTQ (success criteria), Initial and Final Test (Try first, Show you've got it), discovery question (puzzle), guidance chain (guiding questions), rung (level). The full table is course-model's `glossary.md`.
