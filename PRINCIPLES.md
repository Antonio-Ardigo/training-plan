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
| **Fluency Illusion** | Learner feels they understand from reading but cannot apply | Initial Test exposes this immediately -- no reading happens before testing |
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
