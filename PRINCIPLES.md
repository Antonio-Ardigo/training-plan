# Principles -- Why Test-Teach-Test Works

## The Core Insight

TTT inverts the traditional lecture-then-test model. By testing first, the learner's actual knowledge state is measured before any instruction is delivered. Teaching is then gap-driven -- only what the learner doesn't already know gets taught. This produces faster learning, stronger retention, and immediate evidence of mastery.

## Cognitive Science Foundations

### 1. The Testing Effect (Retrieval Practice)

Attempting to retrieve information from memory strengthens that memory far more than re-reading or passive review. The Initial Test forces the learner to retrieve and apply knowledge before any teaching occurs -- even a failed attempt improves subsequent learning.

**How TTT uses it:** Initial Test, Quick Checks, and Final Test create 3+ retrieval events per session. Each retrieval strengthens the memory trace.

*Reference: Roediger & Karpicke (2006). Test-enhanced learning.*

### 2. Desirable Difficulty

Learning that requires effort produces stronger, more durable memories than learning that feels easy. Fluent reading of theory feels productive but encodes weakly. Struggling with a practical case feels harder but encodes deeply.

**How TTT uses it:** The practical-first approach is deliberately harder than reading theory first. The learner confronts difficulty immediately, which triggers deeper cognitive processing.

*Reference: Bjork (1994). Memory and metamemory considerations in the training of human beings.*

### 3. Transfer-Appropriate Processing

Performance is best when the conditions of learning match the conditions of assessment. If you will be tested with practical cases, you should learn through practical cases.

**How TTT uses it:** Both the Initial Test and Final Test are practical cases -- the learner practices in the same mode they will be assessed. The Final Test uses a different scenario to verify transfer, not memorization.

### 4. Gap-Driven Teaching

Instruction is most effective when it targets specific deficits rather than covering material uniformly. Teaching what the learner already knows wastes time and attention. Teaching only what is missing is both faster and more engaging.

**How TTT uses it:** The EVALUATE phase identifies named, specific gaps. The TEACH phase delivers one teaching block per gap. Nothing more, nothing less.

### 5. Spaced Retrieval Practice

Retrieving the same knowledge at multiple points -- separated by intervening activity -- strengthens retention more than massed practice. Each retrieval event in a TTT session is separated by new information (teaching blocks, new scenarios).

**How TTT uses it:** The learner retrieves knowledge at the Initial Test, at each Quick Check during teaching, and again at the Final Test. Adaptation loops add further spaced retrieval.

## Five Learning Risks and How TTT Addresses Them

These risks are identified in research on developer learning during AI-assisted coding (DrCatHicks, learning-opportunities).

| Risk | Description | How TTT Mitigates |
|------|-------------|-------------------|
| **Generation Effect Gaps** | Learner generates plausible but wrong answers without feedback | EVALUATE phase explicitly names gaps; Quick Checks catch remaining errors after each teaching block |
| **Fluency Illusion** | Learner feels they understand from reading but cannot apply | Initial Test exposes this immediately -- nothing is taught in a session before its test, and no test uses a case the plan has already solved |
| **Spacing Effect** | Cramming produces fast forgetting | Multiple sub-goals spread practice; adaptation loops add spacing within sessions |
| **Metacognitive Blindness** | Learner cannot accurately judge what they know | Pass criteria provide an objective measure -- the criteria decide, not the learner's self-assessment |
| **Reduced Retrieval Practice** | Passive review instead of active recall | Every phase requires active production: solve a case, answer Quick Checks, solve another case |

## Design Implications

These principles explain specific TTT design decisions:

- **No preamble before Initial Test**: Presenting theory first would eliminate desirable difficulty and bypass the testing effect. The test must come first.
- **Quick Checks after each teaching block**: Each Quick Check is a retrieval event that strengthens the just-taught concept. Skipping them loses a critical learning opportunity.
- **Different scenario in Final Test**: Same scenario would test memorization. Different scenario tests transfer -- the learner must apply the concept in a new context.
- **Maximum 2 adaptation loops**: Diminishing returns after 2 loops indicate the gap may require prerequisite knowledge the session cannot provide. Flagging for review is more productive than infinite retry.
- **One gap, one teaching block**: Combining gaps into a single explanation creates interference. Sequential, focused blocks let each concept consolidate before the next is introduced.

## Plan Design Principles

The sections above explain how a *session* runs. These explain what every *plan* contains, and why. Plan creation checks for all five after writing the file.

**1. Core principles identification.** A learner who holds the principles can rebuild the details; one who holds only the details cannot. So the 3-5 core principles are identified before any sub-goal is written, and every sub-goal traces back to one.

**2. Key facts identification.** Principles are reasoned from; facts are simply known. Listing the few facts a course relies on tells the learner what to memorise and what to understand, and keeps a test of reasoning from failing on a missing constant.

**3. Motivation.** People put effort into what they can see the use of. A plan opens with why the topic matters and what the learner will be able to do, before any detail.

*Reference: Hulleman & Harackiewicz (2009). Promoting interest and performance in high school science classes.*

**4. Breakthrough.** A concept is easier to understand and remember as the answer to a problem than as a free-standing statement. A plan records what the situation was before the key intuition, and what the topic solved.

**5. Test-Teach-Test, by explanation or by discovery.** Every plan states its method. A standard plan explains after the test; a Socratic plan leads the learner to derive the concept, on the same test-teach-test cycle. What a learner works out is remembered better than what they are told.

*Reference: Slamecka & Graf (1978). The generation effect: Delineation of a phenomenon.*

## Teaching the Hard Core

Some principles resist being told. They contradict intuition, need a new abstraction, or run into a misconception that survives correction, and once grasped they change how the rest of the subject looks. A plan flags these principles and designs their explanation before the session.

*Reference: Meyer & Land (2003). Threshold concepts and troublesome knowledge.*

| Design decision | Why |
|-----------------|-----|
| **Predict, fail, then reveal** | An explanation lands when the learner has just met the problem it solves. A test built so that the natural approach fails creates that moment, and the explanation starts from the learner's own answer. |
| **One insight, one picture, the smallest example** | An aha is a reframing, and a reframing fits in a sentence. One picture carries it; the picture's limit is stated so that it does not become the next misconception. |
| **A climb from High school to the plan's level** | Concrete first, formal second, general last. Each rung keeps what the rung below got right and adds one layer. |
| **A solved example, then "your turn", at every rung** | Studying a worked example and then solving a similar problem builds skill better than solving problems unaided, most of all for a learner new to the material. |
| **A failed rung drops one level** | When the formalism has outrun the intuition, repeating the formalism does not help. |
| **Every solution ends with a Check** | A wrong solution presented with confidence teaches the wrong thing. A second route to the result catches it. |

*References: Kapur (2008). Productive failure. Schwartz & Bransford (1998). A time for telling. Fyfe, McNeil, Son & Goldstone (2014). Concreteness fading in mathematics and science instruction. Sweller & Cooper (1985). The use of worked examples as a substitute for problem solving in learning algebra.*

## Test First, Even With Solutions in the Plan

A plan holds more than a list of tests: an overview, a breakthrough story, key facts and, for hard-core principles, solved exercises. The test-first rule still holds, for three reasons:

- The top of a plan names and motivates; it does not explain, and it never states the tempting answer to a test.
- No test is built on a case the plan has already solved.
- A note above the blueprints asks the learner to run a session before reading its blueprint. A learner who reads ahead loses the surprise, not the measurement: the test still shows whether they can apply the idea to a new case.
