# Principles: Why Try First, Learn, Show You've Got It

## The core idea

Most teaching explains first and tests after. This plugin turns that round. Each lesson starts with **Try first**: a real case the learner attempts before any explanation. The attempt shows what the learner already holds and what is missing. **Learn** then teaches only what is missing, one item at a time. **Show you've got it** checks, on a new case, that the learning carries over. The result is faster learning, stronger memory and clear evidence of what was learned.

## What the research says

### 1. Trying to recall builds memory (the testing effect)

Pulling something out of memory strengthens it far more than reading it again. Try first makes the learner recall and apply before any teaching; even a failed attempt makes the teaching that follows work better.

**In a lesson:** Try first, the checks after each explanation and Show you've got it give at least three recalls per lesson.

*Roediger & Karpicke (2006). Test-enhanced learning.*

### 2. Effort helps (desirable difficulty)

Learning that takes effort lasts longer than learning that feels easy. Reading theory fluently feels productive but sticks poorly. Struggling with a real case feels harder and sticks.

**In a lesson:** the case comes before the theory, on purpose.

*Bjork (1994). Memory and metamemory considerations in the training of human beings.*

### 3. Learn the way you will be tested (transfer-appropriate processing)

People perform best when they learned in the same way they are tested. Both tests of a lesson are real cases, and Show you've got it uses a different case from Try first, so it measures transfer, not memory of one example.

### 4. Teach only what is missing

Teaching what the learner already knows wastes time and attention. Judging Try first names exactly **what to work on**; Learn gives one explanation for each item and nothing else.

### 5. Recall again, spaced out

Recalling the same idea several times, with other activity in between, strengthens it more than recalling it several times in a row. In a lesson, Try first, each check and Show you've got it are separated by new material; another round adds one more recall.

## Five learning risks

These risks come from research on learning while working with AI assistants (DrCatHicks, learning-opportunities).

| Risk | What happens | How the lesson guards against it |
|---|---|---|
| **Plausible but wrong** | The learner produces answers that sound right and are not | Judging names what to work on, with the kind of common mistake; a check follows every explanation |
| **Fluency illusion** | Reading feels like understanding, but the learner cannot apply it | Try first exposes it at once: nothing is taught before the lesson's test, and no test uses a case the course has already solved |
| **Cramming** | Fast learning, fast forgetting | Lessons spread the practice; another round adds spacing inside a lesson |
| **Not knowing what you know** | The learner misjudges their own understanding | The pass standard decides, not the learner's feeling |
| **Passive review** | Re-reading instead of recalling | Every step asks the learner to produce something: solve a case, answer a check, solve a new case |

## Design decisions that follow

- **No theory before Try first.** Explaining first would remove the useful difficulty and the recall. A short opening says why the lesson matters and where the idea came from, and gives no answer away.
- **A check after each explanation.** Each check is a recall that fixes what was just taught.
- **A new case in Show you've got it.** The same case would test memory; a new one tests transfer.
- **At most two more rounds.** After two, the missing piece is usually background the lesson cannot supply, and marking the lesson for review helps more than repeating it.
- **One item, one explanation.** Merging several missing items into one explanation makes them interfere; one at a time lets each settle.

## What every course contains, and why

1. **Principles.** A learner who holds the principles can rebuild the details; one who holds only details cannot. The three to five principles are found before any lesson is written, and every lesson traces back to one.
2. **Facts to know.** Principles are reasoned from; facts are simply known. Listing them separates what to memorise from what to understand, and keeps a test of reasoning from failing on a missing constant.
3. **Why it matters.** People put effort into what they can see the use of. A course opens with why the topic matters and what the learner will be able to do. *Hulleman & Harackiewicz (2009). Promoting interest and performance in high school science classes.*
4. **The story.** An idea is easier to grasp and remember as the answer to a real problem. A course records what the situation was before the key idea, the aha, and what it solved.
5. **A stated method.** In the Direct method, the lesson explains after Try first. In the Socratic method (the default), guiding questions lead the learner to state the idea themselves, on the same Try first → Learn → Show you've got it cycle. What learners work out, they remember better than what they are told. *Slamecka & Graf (1978). The generation effect.*

## Teaching the key ideas ★

Some principles resist being told. They contradict intuition, need a new abstraction, or meet a mistaken belief that survives correction; once grasped, they change how the rest of the subject looks. A course marks these as **key ideas** and designs their teaching in advance. *Meyer & Land (2003). Threshold concepts and troublesome knowledge.*

| Design decision | Why |
|---|---|
| **The trap first, then the aha moment** | An explanation lands when the learner has just met the problem it solves. Try first is built so that the natural answer fails, and the teaching starts from the learner's own answer. |
| **One aha, one picture, the smallest example** | An aha is a new way of seeing, and it fits in a sentence. One picture carries it; its limit is stated so it does not become the next mistaken belief. |
| **Level by level, from High school up** | Concrete first, formal next, general last. Each level keeps what the level below got right and adds one layer. |
| **A solved example, then Your turn, at each level** | Studying a worked example and then solving a similar problem builds skill better than solving unaided, most of all for a newcomer. |
| **A wrong method: step back one level** | When the formalism has outrun the intuition, repeating the formalism does not help. |
| **Every solution ends with a Check** | A wrong solution shown with confidence teaches the wrong thing. A second route to the result catches it. |

*Kapur (2008). Productive failure. Schwartz & Bransford (1998). A time for telling. Fyfe, McNeil, Son & Goldstone (2014). Concreteness fading in mathematics and science instruction. Sweller & Cooper (1985). The use of worked examples as a substitute for problem solving in learning algebra.*

## Try first, even though the course holds solutions

A course holds more than tests: an overview, the story, facts to know and, for key ideas, solved examples. Trying first still works, because:

- What the learner reads before a lesson (`overview.md`) names and motivates; it never shows a test, a marking guide, a solution or a trap.
- No test is built on a case the course has already solved.
- A learner who reads the lesson design ahead loses the surprise, not the measurement: Try first still shows whether they can apply the idea to a new case.
