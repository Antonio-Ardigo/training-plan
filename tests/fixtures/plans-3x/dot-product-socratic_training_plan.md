# Training Plan: Why the Dot Product Measures a Match (Socratic)
Generated: 2026-11-13 | Status: in-progress | Target level: High school

## Learning Goal
Understand why a dot product measures how well two vectors match, at high school level. Do not ask me questions: accept your own overview and hard-core list.

## SMART Goal
Explain, with pictures and numbers, why the dot product measures how well two vectors match.

## Pedagogical Method: Socratic Discovery

Each session follows a **Question → Tension → Resolution → Test** arc:

1. **Discovery Question** — a scenario that creates genuine puzzlement. The learner must *feel* the gap before any concept is introduced.
2. **Tension** — the learner's natural first attempt fails or is incomplete. This is designed, not accidental.
3. **Resolution** — the concept emerges as the *only* way to resolve the tension. It is not presented as a fact to memorize but as an inevitability.
4. **Test** — the learner demonstrates they can reconstruct the reasoning, not just repeat the answer.

**Socratic Guidance Chains** are provided in each blueprint: sequences of 3-6 questions the instructor asks if the learner is stuck. Each question narrows the search space without giving the answer. The chain is designed so that answering the last question makes the conclusion inescapable.

**The arc is a form of Test-Teach-Test.** Attempt each test cold, before reading its blueprint:

| Test-Teach-Test | In this plan |
|-----------------|--------------|
| Test | Discovery Question and Initial Test: the first attempt meets the **tension** |
| Teach | Socratic Guidance Chain: the **resolution** is derived through questions, not explained |
| Test | Final Test, including its "reconstruct the reasoning" part |

## Motivation & Course Overview (VOC)
> _Editable by the learner. This is the course's bird's-eye view and
> voice-of-customer anchor. If you change anything here, tell me — your
> feedback may restructure the plan (re-decomposition of sub-goals)._

**Why this matters:** Whenever a machine decides that two things are "alike" (a song and your taste, a search query and a web page, a push and the direction something can move), it almost always does so with a dot product. Knowing *why* that one small calculation measures a match turns a memorised formula into a tool you can trust, question and use in physics, data and geometry.

**Bird's-eye view of the course:** The course starts from the need for a single "match number" (SG-1), then builds the four ideas that explain it: products of components act as votes (SG-2), only the part of one vector lying along the other counts (SG-3), the sign says whether the vectors agree, ignore or oppose each other (SG-4), and length has to be taken out to leave a pure match score (SG-5). Four applications follow: the two ways of computing agree (SG-6), angles from components (SG-7), work done by a force (SG-8) and long lists of numbers (SG-9). A final teach-back (SG-10) puts everything into one explanation.

**Core principles & key facts:** Four principles carry the course. *Multiply-and-add scoring*: each pair of components casts a vote, and the votes are added. *The shadow*: the dot product sees only the part of one vector that lies along the other. *Sign and zero*: positive, zero and negative results mean agreeing, perpendicular and opposing directions. *Length versus direction*: the raw number mixes size with alignment, and dividing by both lengths leaves a score between −1 and 1. The facts you rely on are few: the component formula itself, the fact that the result is one number, how the angle between vectors is measured, five cosine values, the name "cosine similarity", the length of a list of numbers, and the definition of work.

**What you'll be able to do on completion:**
- Compute a dot product from components and say what each term contributes
- Draw the shadow picture and read the dot product from it
- Tell from the sign alone whether two vectors agree, are perpendicular or oppose each other
- Separate "how big" from "how aligned" and compute a match score between −1 and 1
- Find the angle between two vectors from their components
- Use the dot product for work done by a force and for comparing lists of ratings
- Explain to a classmate, with one sketch and concrete numbers, why the dot product measures a match

## Breakthrough
> _The story behind the topic: what the situation was before the key
> intuition, and what the topic solved._

**Before the intuition:** To compare two directions, people drew them and measured the angle, or worked through triangle trigonometry case by case. That is slow, needs a picture, and cannot be done at all for lists of more than three numbers.

**The intuition:** One simple piece of arithmetic on the components, multiply in pairs and add, already contains the geometry: it says how much of one vector lies along the other.

**What it solved:** "How alike are these two?" became a calculation that needs no drawing and works for any number of components. Physics got a one-line rule for the useful part of a force, and computing got a way to compare texts, songs and images by the million.

| Principle | Before the intuition | What it solved |
|-----------|----------------------|----------------|
| Multiply-and-add scoring | Lists were compared by eye or by ad-hoc rules, which gave no single number and broke down as the lists grew. | One rule gives one number for any two lists of the same length. |
| The shadow | The effect of a slanted push or pull was found by drawing triangles for each new situation. | The "useful part" of any vector along any direction became a single reusable idea. |
| Sign and zero | Checking for a right angle, or for opposing directions, needed a protractor or a diagram. | A glance at the sign of one number answers the question, with no drawing. |
| Length versus direction | Comparisons of direction were disturbed by how large the things being compared happened to be. | Size and alignment could be separated, giving a fair score on a fixed scale. |

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| Multiply-and-add scoring | Multiply the two vectors component by component and add: each product is a vote, positive when the components agree in sign, negative when they disagree, zero when either is zero. | $a\cdot b = a_1b_1 + a_2b_2$ | Coordinates in the plane; multiplying signed numbers |
| The shadow | The dot product equals the length of one vector's shadow on the other's line, multiplied by the other's length: only the part lying along the other vector counts. | $a\cdot b = (\text{shadow of } a \text{ on } b)\times\lvert b\rvert$ | Right angles and perpendicular lines; Pythagoras' theorem |
| Sign and zero | The dot product is positive when the angle between the vectors is under 90°, zero at exactly 90°, and negative beyond 90°. | $a\cdot b = \lvert a\rvert\,\lvert b\rvert\cos\theta$ | Cosine of an angle, including angles between 90° and 180° |
| Length versus direction | The dot product mixes how long the vectors are with how well their directions agree; dividing by both lengths leaves a pure match score from −1 to 1. | $\cos\theta = \dfrac{a\cdot b}{\lvert a\rvert\,\lvert b\rvert}$ | Length of a vector from its components; division and ratios |

## Hard Core
> _The principles that are hardest to grasp. Each is taught through an aha
> moment and a climb through the levels, with a solved exercise at every rung.
> If this list looks wrong to you, tell me which principle to add or remove._

| Principle | Why it is hard | Taught in |
|-----------|----------------|-----------|
| The shadow | counter-intuitive, new abstraction, load-bearing (SG-4, SG-5, SG-6, SG-8 and SG-10 depend on it) | SG-3 |
| Length versus direction | persistent misconception | SG-5 |

## Key Facts
> _What this course relies on you simply knowing. Values marked `(verify)`
> should be checked against a source before you rely on them._

| # | Key Fact | Why it matters | Used in |
|---|----------|----------------|---------|
| KF-1 | The dot product of $(a_1, a_2)$ and $(b_1, b_2)$ is defined as $a_1b_1 + a_2b_2$; longer lists add one product per extra component. | Without the definition no score can be computed. | SG-2, SG-6, SG-7, SG-9, SG-10 |
| KF-2 | The result of a dot product is a single number, not a vector. | Treating the result as an arrow makes "bigger" and "positive or negative" meaningless. | SG-2, SG-3 |
| KF-3 | The angle between two vectors is measured with their tails together and lies between 0° and 180°. | With another convention the sign rule gives the wrong reading. | SG-4, SG-7 |
| KF-4 | cos 0° = 1, cos 60° = 0.5, cos 90° = 0, cos 120° = −0.5, cos 180° = −1. | Without these landmarks a match score cannot be read as "same, partly, unrelated, opposite". | SG-4, SG-7, SG-8 |
| KF-5 | The length of a vector with any number of components is the square root of the sum of its squared components. | Without it the size cannot be taken out of a list with more than two numbers. | SG-5, SG-7, SG-9, SG-10 |
| KF-6 | The score $a\cdot b$ divided by both lengths is called the cosine similarity. | It is the name under which the idea appears in data and computing. | SG-5, SG-9, SG-10 |
| KF-7 | Work is the force along the direction of motion multiplied by the distance moved; 1 joule = 1 newton × 1 metre. | Without the definition and unit the physics case cannot be stated or checked. | SG-8 |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | Discover why one number that scores a match between two lists is worth having. | Motivation | low | HS | — | pending | - |
| SG-2 | Core Principle | Discover why multiplying components in pairs and adding rewards agreement and punishes disagreement. | Arithmetic of vectors | low | HS | Multiply-and-add scoring | pending | - |
| SG-3 | Core Principle | Discover that the dot product counts only the part of one vector along the other. | Geometry of vectors | low | HS | The shadow | pending | - |
| SG-4 | Core Principle | Discover what a positive, a zero and a negative dot product say about two directions. | Geometry of vectors | low | HS | Sign and zero | pending | - |
| SG-5 | Core Principle | Discover why a dot product must be divided by both lengths to compare directions fairly. | Geometry of vectors | low | HS | Length versus direction | pending | - |
| SG-6 | Key Concept | Discover why the component rule and the shadow picture always give the same number. | Linking arithmetic and geometry | medium | HS | Multiply-and-add scoring; The shadow | pending | - |
| SG-7 | Key Concept | Discover how to find the angle between two vectors from their components alone. | Angles | medium | HS | Sign and zero; Length versus direction | pending | - |
| SG-8 | Key Concept | Discover why the work done by a slanted force is a dot product. | Physics application | medium | HS | The shadow; Sign and zero | pending | - |
| SG-9 | Key Concept | Discover that match scoring works unchanged for lists of four or more numbers. | Data application | medium | HS | Multiply-and-add scoring; Length versus direction | pending | - |
| SG-10 | Verification | Explain to a classmate, with a sketch and numbers, why the dot product measures a match. | Teach-back | medium | HS | All four | pending | - |

_Depth is the plan's Target level in every row: HS = High school, MSc = Master's, Adv = Advanced._

## Prerequisite Graph

```
Why the dot product measures a match (core)
  requires:
    Coordinates in the plane and arithmetic with signed numbers (prerequisite) ← CHECK learner profile
    Right angles, perpendicular lines and Pythagoras' theorem (prerequisite) ← CHECK learner profile
    Cosine of an angle, including angles from 90° to 180° (prerequisite) ← CHECK learner profile
    Use of a calculator for square roots and inverse cosine (prerequisite) ← CHECK learner profile
  rests on:
    Multiply-and-add scoring (principle) → SG-2
      led to:
        The shadow (principle) → SG-3
          led to:
            Sign and zero (principle) → SG-4
              led to:
                Length versus direction (principle) → SG-5
```

**WARNING:** no learner profile exists, so none of the four external prerequisites is confirmed. The one most likely to be missing at school level is the cosine of angles between 90° and 180°; SG-4 is designed so that it can be reached through the shadow picture if that is the case.

## Sequence
- SG-1 first: it has no dependencies and creates the need for a match number.
- SG-2 → SG-3 → SG-4 → SG-5 follow the `led to` chain of the graph: the shadow reuses components (SG-2), the sign rule reads the shadow (SG-3), and removing length presupposes knowing what the sign and size mean (SG-4).
- SG-6 needs SG-2 and SG-3 (its two principles).
- SG-7 needs SG-4 and SG-5.
- SG-8 needs SG-3 and SG-4.
- SG-9 needs SG-2 and SG-5.
- SG-10 last: it needs all four principles, hence SG-2 to SG-5, and draws on SG-6 to SG-9.
- Suggested order: SG-1, SG-2, SG-3, SG-4, SG-5, SG-6, SG-7, SG-8, SG-9, SG-10.

## Session Blueprints
> _Session designs. Run a sub-goal's session before reading its blueprint: the
> questions and tests work best unseen. The solved exercises are there to study afterwards._

### SG-1: Why a match number is worth having
- **Discovery Question:** You and two friends rate three kinds of film from −2 (hate) to +2 (love), in the order action, comedy, horror. You: (2, 1, −2). Ana: (2, 2, −1). Ben: (−2, 1, 2). Who should choose tonight's film for you? Now the hard part: describe a rule a computer could follow to answer the same question for 1,000 friends, giving one number per friend.
- **Initial Test:** A music app stores your taste as (pop, rock, jazz) = (2, −1, 0): you love pop, mildly dislike rock and do not care about jazz. Three songs are described the same way: A = (2, −1, 2), B = (−2, 1, 0), C = (1, 0, 2). Invent a rule that turns "your taste and one song" into a single number, apply it to the three songs, and rank them. Then name one situation outside music where the same rule would be useful. (Designed tension: counting equal entries, or adding up differences, either ignores how strong a preference is or lets jazz, which you do not care about, change the result.)
- **Pass Criteria:** The rule gives one number per song and has all three properties: it rises when you and the song agree, it falls when you disagree, and jazz does not affect it. Ranking is A, then C, then B. One sensible use outside music is named.
- **Estimated Depth:** High school
- **Principle:** —
- **Socratic Guidance Chain (if stuck):**
  1. Ana and Ben each give exactly one rating identical to yours. Does "count the identical ratings" separate them? What does it miss?
  2. For one category, you say +2. Which should score higher: a friend who says +2 or one who says +1? And a friend who says −2?
  3. Song A and song C differ a lot in jazz. Should that change their scores for you? What must your rule do with a category where your own rating is 0?
  4. You need one operation on two numbers that is large when both are large with the same sign, negative when the signs differ, and zero when either is zero. Which operation does that?
  5. Once every category has its own small score, how do you turn them into one number?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | A match needs to be one number so that many candidates can be ranked | Motivation | Rank three candidates and say why a table of differences would not do | verbal-without-formal: describes "similar" without producing a number |
  | A good rule rewards agreement, punishes opposition and ignores what you do not care about | Motivation | List the three properties and test a proposed rule against each | overgeneralization: accepts any rule that happens to rank this one case correctly |
  | The same need appears outside this one example | Motivation | Name a second domain and say what the two lists are | procedural-without-conceptual: can score songs but cannot say what else is a "list" |
- **Teach Topics:** The need for a single ranking number; the three properties a match rule must have; examples of lists (taste profiles, forces, directions, word counts). Pitfalls: [overgeneralization] "any rule that ranks these three songs correctly is good"; [conflation] "similar" taken to mean "equal entry by entry". Socratic teaching note: do not name the dot product in this session; ask "what would your rule do if…" until the learner's own rule has the three properties.
- **Final Test:** A garden app describes a garden as (sun, wetness, wind) = (2, −1, 0) and three plants by what they like: X = (2, −2, 1), Y = (−1, 2, 2), Z = (1, 1, −2). Give each plant one number and rank them. Then explain why you chose your rule: what would go wrong with "count the entries that have the same sign", and what would happen to the ranking if the garden's wind value were ignored altogether? (Expected with a multiply-and-add rule: X = 6, Z = 1, Y = −4; wind already contributes nothing.)

### SG-2: Votes that add up
- **Principle:** Multiply-and-add scoring — Multiply the two vectors component by component and add: each product is a vote, positive when the components agree in sign, negative when they disagree, zero when either is zero.
- **Worked Example (foundational):**
  **Given:** a = (3, 2) and b = (4, −1). Find a·b and say what each term means.
  **Step 1:** Multiply the first components: 3 × 4 = 12.
  > **Why:** "Why multiply and not add?" Because a product is large only when *both* numbers are large and of the same sign. Both first components are positive: a vote of +12 for "these match".
  **Step 2:** Multiply the second components: 2 × (−1) = −2.
  > **Why:** "What does the minus sign say?" The two second components point opposite ways, so this pair votes against the match, but weakly, because both numbers are small.
  **Step 3:** Add the votes: 12 + (−2) = 10.
  > **Why:** "Why add?" Each component has had its say; one number is needed, and adding lets a strong agreement outweigh a weak disagreement.
  **Result:** a·b = 10, a single positive number: on balance the two vectors agree, mostly because of their first components.
  > **Check:** Swap the order: b·a = 4 × 3 + (−1) × 2 = 12 − 2 = 10. The same votes are cast, so the score cannot depend on who is called a and who b.
- **Discovery Question:** You need one operation on two numbers that gives a large positive result when both are large with the same sign (including both negative), a negative result when their signs differ, and nothing when either is zero. Adding fails the second test, subtracting fails the first. What is left?
- **Initial Test:** Two students mark how strongly they agree (+) or disagree (−) with two statements. Priya: (2, −3). Quentin: (1, −2). Compute one number for how well their opinions match and say what each part of your calculation means. A classmate adds each pair instead of multiplying and gets 3 + (−5) = −2, "so they disagree". Who is right, and why? (Wrong path: adding pairs; it reports a mismatch for two people who are on the same side of both statements.)
- **Pass Criteria:** Can state the principle in own words AND apply it (score 2 + 6 = 8) AND explain why the alternative fails (adding cannot tell "both negative" from "disagree").
- **Estimated Depth:** High school
- **Socratic Guidance Chain (if stuck):**
  1. On statement 2 both students are against. Should that count for or against their match?
  2. What does adding −3 and −2 give? Does its sign fit your answer to question 1?
  3. What does multiplying −3 by −2 give? And if one of them had been +2 instead?
  4. If Quentin had no opinion (0) on a statement, what should that statement contribute? Which operation gives that?
  5. You now have one number per statement. How do you get a single score, and what is it here?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Each product is a vote whose sign shows agreement and whose size shows strength | Multiply-and-add scoring | Given a·b written out, say which component helps most and which hurts | procedural-without-conceptual: computes the total but cannot interpret a single term |
  | The result is one number, and the order of the vectors does not matter | Multiply-and-add scoring | Compute a·b and b·a and explain why they agree | conflation: writes the answer as a vector of products, (12, −2) |
- **Teach Topics:** The principle; a zero component silences its vote; the two lists must have the same number of components, in the same order. Misunderstandings: [conflation] dot product confused with multiplying entry by entry and stopping there; [overgeneralization] "a positive score means every component agrees". Socratic teaching note: ask "which sign should this pair contribute?" before any multiplication is done.
- **Final Test:** Rosa: (−1, 4). Sam: (3, 2). Compute their match score. Then reconstruct the reasoning: on which statement do they disagree, and how does the calculation show it? What would the score become if Sam had no opinion on statement 1, and why does it go up? (Expected: −3 + 8 = 5; with Sam = (0, 2) it becomes 8.)

### SG-3: Only the part along the other counts
- **Principle:** The shadow — The dot product equals the length of one vector's shadow on the other's line, multiplied by the other's length: only the part lying along the other vector counts.
- **Tempting answer:** "The stronger pull gives the bigger dot product." In the Initial Test this ranks the pulls R, Q, P by strength (6, 5, 4). It feels right because a longer vector is "more" of everything, and because in everyday life pulling harder always seems to help.
- **Insight:** The dot product sees only the part of one vector that lies along the other; whatever points sideways is invisible to it.
- **Picture:** Light shines straight down onto the line of b, at right angles to it. Vector a casts a shadow on that line, and the dot product is the shadow's length times the length of b. Where it stops being true: a real shadow is never negative, but when a leans backwards its shadow falls behind the tail and has to be counted as negative; and a real shadow depends on where the sun is, whereas here the light is always at right angles to b.
- **Visual design:**
  - **Objects:** a grid with origin O; vector b = (2, 0) on a faint line extended both ways; vector a = (3, 4) from the same tail; a dashed drop line from (3, 4) to (3, 0); the shadow segment from (0, 0) to (3, 0); one read-out "a·b = shadow × length of b".
  - **Colour roles:** blue = vector a; orange = vector b and its line; green = the shadow and every number derived from it.
  - **Steps:** (1) b appears on its line. (2) a appears from the same tail. (3) The drop line falls from the tip of a at right angles to b's line. (4) The shadow lights up in green with its length. (5) The read-out multiplies the shadow by the length of b.
  - **Your-turn inputs (High school rung):** shadow of a on b's line: right value 3; wrong value 5 (the full length of a was used, so the sideways part was not discarded); wrong value 4 (the sideways part was taken instead of the part along b). Then a·b: right value 6; wrong value 10 (the two lengths were multiplied, so direction was ignored); wrong value 3 (the shadow was not multiplied by the length of b).
  - **Control:** the learner drags the tip of a. Moving it straight up or down leaves the shadow and the dot product unchanged; moving it parallel to b changes both.
- **Worked Example (foundational):**
  **Given:** a = (3, 4), which has length 5, and b = (2, 0), which lies along the x-axis and has length 2. Find a·b from a drawing.
  **Step 1:** Draw both vectors from the same point and drop a line from the tip of a, at right angles, onto the line of b. It lands at (3, 0).
  > **Why:** "Why at right angles?" Because that splits a into a part along b and a part sideways to b with nothing left over: (3, 4) = (3, 0) + (0, 4).
  **Step 2:** Read the shadow: the segment from (0, 0) to (3, 0) has length 3.
  > **Why:** "What happened to the 4?" It points straight across b. It has no part along b at all, so it has nothing to contribute.
  **Step 3:** Multiply the shadow by the length of b: 3 × 2 = 6.
  > **Why:** "Why multiply by the length of b?" The shadow says how much of a goes b's way; b's own length says how much b there is to match with.
  **Result:** a·b = 6. The length of a, which is 5, never entered the calculation: only its 3 units along b did.
  > **Check:** By components: 3 × 2 + 4 × 0 = 6. And replacing a by (3, −7), which has the same shadow, gives 3 × 2 + (−7) × 0 = 6 again.
- **Level ladder:** none: the foundational worked example is the only rung.
- **Discovery Question:** A heavy drawer can only slide straight in and out. You push it three times with exactly the same strength: straight in, at a slant, and flat against its side. Predict how far it moves each time, and say what number you would give each push to describe how much it achieved.
- **Initial Test:** A cart stands on straight rails that run east; the rail direction is r = (1, 0). Three ropes pull on it: P = (4, 0), with strength 4; Q = (4, 3), with strength 5; R = (0, 6), with strength 6. Predict the order of the three dot products r·P, r·Q and r·R, from largest to smallest, and justify your prediction. Then compute them.
- **Pass Criteria:** Gives the right answer, not the tempting one (r·P = r·Q = 4 and r·R = 0), AND justifies it at High school level (only the part of each pull along the rails counts) AND explains why the tempting answer fails (strength spent sideways moves nothing along the rails).
- **Estimated Depth:** High school
- **Socratic Guidance Chain (if stuck):**
  1. The cart can move only along the rails. Rope R pulls straight north with strength 6. How far east does the cart go?
  2. So how much did R's strength of 6 contribute to r·R? What does that say about judging by length alone?
  3. Split Q = (4, 3) into a pull east and a pull north. What are the two pieces?
  4. Which of the two pieces can the rails "feel", and what does the other piece achieve?
  5. Compare Q's eastward piece with P. What must r·Q be, compared with r·P?
  6. Say in one sentence which part of a vector the dot product counts.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Only the part of a along b enters a·b; the sideways part contributes nothing | The shadow, High school rung | Change the sideways part of a and predict the new dot product | overgeneralization: "longer vector, larger dot product" |
  | The dot product is the shadow multiplied by the length of the other vector, not the shadow alone | The shadow, High school rung | Given a shadow of 3 on a vector of length 2, state the dot product | conflation: dot product confused with the shadow itself |
  | Either vector may be the one that casts the shadow; the product is the same | The shadow, High school rung | For a = (3, 4), b = (2, 0), find b's shadow on a (1.2) and check 1.2 × 5 = 6 | formal-without-intuitive: accepts a·b = b·a but cannot see it in the picture |
- **Teach Topics:** The principle; splitting a vector into a part along and a part across another; the shadow counted as negative when it falls behind the tail (taken up in SG-4); the symmetry of the picture. Misunderstandings that survive the Insight: [conflation] "the dot product *is* the shadow" (true only when the other vector has length 1); [overgeneralization] "sideways parts reduce the score" (they add nothing, they do not subtract). Socratic teaching note: keep asking "which part of this pull can the rails feel?"; show the Picture only after the learner has stated the Insight.
- **Final Test:** A conveyor belt carries crates north; its direction is d = (0, 2). Three workers push a crate: A = (0, 3), B = (4, 3), C = (5, 0). Predict the order of d·A, d·B and d·C, justify it, then compute. Reconstruct the reasoning: B pushes with strength 5 and A with strength 3; explain what B's extra strength buys. What would happen to d·B if B's sideways part doubled, giving (8, 3)? (Expected: d·A = d·B = 6, d·C = 0; with (8, 3) still 6.)

### SG-4: What the sign says
- **Principle:** Sign and zero — The dot product is positive when the angle between the vectors is under 90°, zero at exactly 90°, and negative beyond 90°.
- **Worked Example (foundational):**
  **Given:** a = (0, 3) points north. Three partners: b₁ = (2, 2), b₂ = (4, 0), b₃ = (2, −2). Find each dot product with a and read its sign.
  **Step 1:** a·b₁ = 0 × 2 + 3 × 2 = 6, positive.
  > **Why:** "What does positive mean here?" b₁ points north-east, 45° from a. It leans a's way, so part of it lies along a.
  **Step 2:** a·b₂ = 0 × 4 + 3 × 0 = 0.
  > **Why:** "How can two vectors that are not zero give zero?" b₂ points due east, at 90° to a. None of it lies along a, however long it is.
  **Step 3:** a·b₃ = 0 × 2 + 3 × (−2) = −6, negative.
  > **Why:** "What does a negative match mean?" b₃ points south-east, 135° from a. Its part along a's line points against a.
  **Result:** 6, 0 and −6: lean with, stand across, lean against. The sign alone sorts the three cases.
  > **Check:** By shadows on the north line: b₁ reaches 2 north, so 2 × 3 = 6; b₂ reaches 0 north, so 0; b₃ reaches 2 south, counted as −2, so −2 × 3 = −6.
- **Discovery Question:** Two vectors each have length 100. Can their dot product be zero? Can it be negative? If it can, what would a negative "match" mean?
- **Initial Test:** A cyclist rides along d = (3, 1). Three winds blow during the ride: w₁ = (2, 2), w₂ = (−1, 3), w₃ = (−2, −1). Without measuring any angle, decide for each wind whether it helps, hinders or does neither, and explain how you know. (Wrong path: judging by strength, where w₂ is the strongest wind, or by one component, where w₂ "has a +3 in it"; both suggest w₂ matters most, yet d·w₂ = 0.)
- **Pass Criteria:** Can state the principle in own words AND apply it (d·w₁ = 8 helps, d·w₂ = 0 neither, d·w₃ = −7 hinders) AND explain why the alternative fails (strength or a single component says nothing about the direction relative to d).
- **Estimated Depth:** High school
- **Socratic Guidance Chain (if stuck):**
  1. Draw d and w₁ from the same point. Does w₁'s shadow on d's line fall ahead of the tail or behind it?
  2. Do the same for w₃. Where does its shadow fall, and what sign would you give it?
  3. Swing a wind slowly from "ahead" to "behind". The score goes from positive to negative. What value must it pass through on the way?
  4. At what angle to d is the shadow just a single point?
  5. So what does a dot product of exactly zero tell you about two directions? What does d·w₂ come to?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The sign of a·b says whether the angle is under, at, or over 90° | Sign and zero | Given three dot products, classify the angles without drawing | formal-without-intuitive: knows cos is negative past 90° but cannot say what "negative match" means |
  | Zero means perpendicular, not "small" or "one vector is tiny" | Sign and zero | Produce a vector with dot product zero against a given one | conflation: zero score read as "weak vectors" |
- **Teach Topics:** The principle; the signed shadow; the three landmark cases 0°, 90° and 180° with their cosines (KF-4); the angle measured tail to tail (KF-3). Boundary: a zero vector gives zero with everything and has no direction to compare. Misunderstandings: [conflation] negative taken as "error" instead of "opposed"; [missing-prerequisite] cosine not known beyond 90°, in which case stay with the shadow falling behind the tail. Socratic teaching note: let the learner swing a pencil from "with" to "against" and say where the score must cross zero.
- **Final Test:** A ship steers s = (2, 5). Three currents act on it: c₁ = (5, −2), c₂ = (−1, −3), c₃ = (1, 1). Classify each as helping, hindering or neither. Reconstruct the reasoning: c₁ is the strongest current, with strength about 5.4, and yet it scores as it does; explain why, using the shadow. Then give a current of your own, different from c₁, with the same score against s. (Expected: s·c₁ = 0, s·c₂ = −17, s·c₃ = 7; for example (−5, 2) or (10, −4).)

### SG-5: Taking the size out
- **Principle:** Length versus direction — The dot product mixes how long the vectors are with how well their directions agree; dividing by both lengths leaves a pure match score from −1 to 1.
- **Tempting answer:** "The song with the larger dot product is the better match." In the Initial Test that picks song B, 48 against 24. It feels right because the dot product has just been presented as *the* match number, and a bigger score normally means a better result.
- **Insight:** A dot product is "how long" times "how aligned", so before it can say how aligned two vectors are, the lengths have to be taken out.
- **Picture:** A volume knob. Turning a song up does not make it a different song, yet its dot product with your taste grows with the volume. Dividing by the lengths sets every song to the same volume before comparing. Where it stops being true: sometimes size is exactly what you want (a stronger push really does more work, SG-8), and then the raw dot product is the right number; and a vector of length zero has no direction, so it cannot be divided.
- **Visual design:**
  - **Objects:** a grid with a reference vector r = (0, 5); candidates c₁ = (0, 2) and c₂ = (6, 8); a circle of radius 1 round the origin with the length-1 copies of each vector; two read-outs per candidate, "raw" and "match".
  - **Colour roles:** blue = the reference; orange = the candidates; green = the length-1 copies and the match scores.
  - **Steps:** (1) r appears. (2) c₁ and c₂ appear with their raw dot products. (3) The radius-1 circle appears. (4) Each vector shrinks or stretches to the circle. (5) The match scores are read from the length-1 copies.
  - **Your-turn inputs (High school rung):** raw r·c₂: right value 40; wrong value 50 (the two lengths were multiplied, so direction was ignored); wrong value 30 (the 5 was paired with the 6, so the components were mismatched). Then the match score of c₂: right value 0.8; wrong value 4 (divided by the length of c₂ only, so the reference's size is still in); wrong value 40 (not divided at all, so size and alignment are still mixed).
  - **Control:** a slider stretches c₂ along its own direction. The raw dot product grows with it; the match score stays at 0.8.
- **Worked Example (foundational):**
  **Given:** A reference r = (0, 5) and two candidates, c₁ = (0, 2) and c₂ = (6, 8). Which candidate points more nearly the way r does?
  **Step 1:** Raw dot products: r·c₁ = 0 × 0 + 5 × 2 = 10 and r·c₂ = 0 × 6 + 5 × 8 = 40.
  > **Why:** "Is that the answer, then: c₂, by four to one?" Not yet. c₁ points exactly along r, and c₂ visibly leans away. Something other than direction is inflating c₂'s score.
  **Step 2:** Lengths: r has length 5, c₁ has length 2, c₂ has length √(36 + 64) = 10.
  > **Why:** "Why lengths?" They are the "something else". c₂ is five times as long as c₁, and every unit of length multiplies the score.
  **Step 3:** Divide each raw score by both lengths: c₁: 10 ÷ (5 × 2) = 1. c₂: 40 ÷ (5 × 10) = 0.8.
  > **Why:** "Why by both?" The score grows with the length of either vector, so both have to be removed to leave direction alone.
  **Result:** Match scores 1 and 0.8: c₁ is perfectly aligned with r, c₂ is well but not perfectly aligned. The raw order was the wrong way round.
  > **Check:** Shrink everything to length 1 first: r becomes (0, 1), c₁ becomes (0, 1), c₂ becomes (0.6, 0.8). Their dot products are 1 and 0.8, the same scores.
- **Level ladder:** none: the foundational worked example is the only rung.
- **Discovery Question:** A machine compares recordings with a stored "hello" by taking a dot product. One recording is the same "hello", whispered. Another is a different word, shouted. Predict which gets the higher score, justify it, and say what the machine should conclude.
- **Initial Test:** A music app stores your taste as t = (4, 3), in the order (beat, melody). It scores each song by its dot product with t. Song A = (3, 4). Song B = (12, 0). Compute both scores. Which song matches your taste better? Justify your answer.
- **Pass Criteria:** Gives the right answer, not the tempting one (A: raw 24 but match 0.96; B: raw 48 but match 0.8, so A matches better), AND justifies it at High school level (divides by the lengths 5, 5 and 12, or compares length-1 copies) AND explains why the tempting answer fails (B's score is large because B is long, not because it is aligned).
- **Estimated Depth:** High school
- **Socratic Guidance Chain (if stuck):**
  1. Play song A twice as loud: (6, 8). What happens to its dot product with t?
  2. Is it a different song now? Has its direction changed?
  3. So the dot product responds to two different things. Name them.
  4. A has length 5 and B has length 12. When two packets of different size are compared in a shop, what is done to make the comparison fair?
  5. Bring t, A and B all to length 1. What are the two scores now, and which is larger?
  6. Say in one sentence what has to be done to a dot product before it can be read as "how well the directions match".
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The raw dot product grows with the length of either vector, with no change of direction | Length versus direction, High school rung | Double one vector and predict the new dot product and the new match score | overgeneralization: "bigger dot product, better match" |
  | Dividing by both lengths gives a score from −1 to 1 that depends on direction only | Length versus direction, High school rung | Compute the match score of two given vectors and say what 1, 0 and −1 would mean | procedural-without-conceptual: divides correctly but cannot say why by both lengths |
- **Teach Topics:** The principle; length of a vector (KF-5); the name cosine similarity (KF-6); the fixed scale from −1 to 1; when the raw dot product is the right tool and when the match score is. Misunderstandings that survive the Insight: [overgeneralization] "always divide by the lengths" (not when size matters, as with work); [conflation] match score of 0.8 read as "80% the same" or as an angle of 80°. Socratic teaching note: return to "is it a different song when it is louder?" whenever the learner reaches for the raw number; show the Picture only after the Insight has been stated.
- **Final Test:** A cook's ideal sauce has the flavour profile p = (6, 8), in the order (sweet, sour). Sauce X = (8, 6). Concentrate Y = (0, 15). Using dot products with p, decide which has the flavour balance closer to the ideal, and justify it. Reconstruct the reasoning: explain where Y's raw score comes from. What happens to Y's raw score and to its match score if Y is diluted to (0, 5), and why? (Expected: X raw 96, match 0.96; Y raw 120, match 0.8; diluted Y raw 40, match still 0.8.)

### SG-6: Two routes, one number
- **Discovery Question:** One recipe says "multiply the components in pairs and add". Another says "take the shadow and multiply by the length". One uses only arithmetic, the other only a drawing. Why should two such different recipes ever give the same number, let alone always?
- **Initial Test:** A wind blows due east, w = (10, 0). A road runs along b = (4, 3). How much of the wind blows along the road? Find it twice: once from a scale drawing or trigonometry, once using components only. Then explain why the two answers had to agree. (Designed tension: many learners treat the two recipes as two different "dot products", or believe the component rule works only when a vector lies on an axis.)
- **Pass Criteria:** Both routes give 8 (drawing within ±0.2): by components w·b = 40 and 40 ÷ 5 = 8; by trigonometry 10 × 0.8 = 8. The explanation says that a vector can be split into its x-part and y-part and that the shadows of the parts add up to the shadow of the whole.
- **Estimated Depth:** High school
- **Principle:** Multiply-and-add scoring; The shadow
- **Socratic Guidance Chain (if stuck):**
  1. What is the shadow of any vector (a₁, a₂) on the x-axis? On the y-axis? Where have you seen those two numbers before?
  2. Split b = (4, 3) into (4, 0) + (0, 3). Using the shadow picture, what is w·(4, 0)? And w·(0, 3)?
  3. Walk along (4, 0) and then along (0, 3): you arrive at the tip of b. How does the shadow of the whole walk on w's line relate to the shadows of its two legs?
  4. So what exactly are a₁b₁ and a₂b₂, in the language of shadows, and what does adding them give?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The component rule and the shadow picture are one quantity seen two ways | Linking the two principles | Compute one dot product by both routes and get the same number | conflation: believes there are two different dot products |
  | Shadows of parts add up to the shadow of the whole | The shadow | Split a vector into two pieces and show the dot products add | procedural-without-conceptual: verifies with numbers but cannot say why it must work |
  | The dot product does not depend on how the axes are placed | Linking the two principles | Say what happens to a·b when both vectors are turned by the same angle | overgeneralization: "components changed, so the dot product changed" |
- **Teach Topics:** Splitting a vector along the axes; shadows add; the component rule as "shadow on each axis, scaled, then added"; turning both vectors together leaves the dot product alone. Pitfalls: [conflation] two formulas taken for two quantities; [formal-without-intuitive] can use both but sees no link. Socratic teaching note: ask for each product a₁b₁ "whose shadow on whose line is this?" before asking for the sum.
- **Final Test:** a = (12, 5), which has length 13, and b = (3, 0). Find a·b three ways: by components, as a's shadow on b times b's length, and as b's shadow on a times a's length. Reconstruct the reasoning: explain why the three had to agree. What would happen to the components and to the dot product if both vectors were turned through the same angle? (Expected: 36 each time; shadows 12 and 36/13 ≈ 2.77; components change, dot product does not.)

### SG-7: The angle from the components
- **Discovery Question:** Two straight paths leave a hut, one towards (1, 3) and one towards (2, 1). Neither lies along an axis and you have no protractor. Everything you know about the paths is those four numbers. Is the angle between them hidden in the numbers, and if so, where?
- **Initial Test:** For the two paths A = (1, 3) and B = (2, 1), find the angle between them, in degrees, using only the components and a calculator. Show each step and say what each step is for. (Designed tension: the dot product alone, 5, is not the angle and not its cosine; the first attempt usually stops there or divides by only one length.)
- **Pass Criteria:** Angle 45° (±1°), from 5 ÷ (√10 × √5) ≈ 0.707, with the lengths found correctly and a stated reason for dividing by both of them.
- **Estimated Depth:** High school
- **Principle:** Sign and zero; Length versus direction
- **Socratic Guidance Chain (if stuck):**
  1. A·B is 5. Is it positive, zero or negative, and what does that already tell you about the angle?
  2. If path B were three times as long, would the angle change? Would A·B change?
  3. So what must be removed from 5 before it says anything about the angle alone? What are the two lengths?
  4. After dividing you have a number between −1 and 1. Which property of an angle takes exactly those values, being 1 at 0° and 0 at 90°?
  5. Which calculator key takes you back from that number to the angle?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The match score is the cosine of the angle between the vectors | Length versus direction | Turn a match score of 0.5 and of −1 into angles | conflation: match score read as the angle itself or as a percentage |
  | Both lengths must be divided out before using inverse cosine | Length versus direction | Find an angle from components with all steps shown | procedural-without-conceptual: omits a length or cannot say why it is needed |
  | The sign of the dot product predicts acute or obtuse before any calculation | Sign and zero | Predict the kind of angle, then confirm it | formal-without-intuitive: computes 98° without noticing the minus sign announced it |
- **Teach Topics:** From dot product to match score to angle; landmark cosines (KF-4); the angle lies between 0° and 180° (KF-3); calculator in degree mode. Pitfalls: [conflation] cosine and angle mixed up; [procedural-without-conceptual] formula applied with one length missing. Socratic teaching note: always ask for the sign-based prediction before any calculation.
- **Final Test:** Two search beams leave a lighthouse along A = (3, 1) and B = (−1, 2). Before calculating, predict whether the angle between them is acute, right or obtuse, and say how you know. Then find it. Reconstruct the reasoning: why are the lengths divided out? What happens to the angle if B is tripled to (−3, 6), and which numbers in your calculation change? (Expected: A·B = −1, so obtuse; −1 ÷ (√10 × √5) ≈ −0.141, about 98°; tripling B triples the dot product and B's length, the angle is unchanged.)

### SG-8: Work as a dot product
- **Discovery Question:** You pull a wheeled suitcase through an airport with the handle slanting upwards. Your arm pulls with a certain strength, yet part of that pull only lifts the case slightly and moves it nowhere. How much of your effort is actually moving the suitcase forward, and what would you multiply by what to measure it?
- **Initial Test:** You pull a suitcase with a force of 20 N along a handle that makes 60° with the floor, and walk 10 m in a straight line. How much work does your pull do on the suitcase? Show how you got it and explain it with a sketch. (Designed tension: the natural first attempt is 20 × 10 = 200 J, which counts the whole pull.)
- **Pass Criteria:** Work = 100 J (within 5%), from the forward part of the force, 20 × 0.5 = 10 N, times 10 m; the sketch shows the force split into a part along the floor and a part across it; the answer is named as a dot product of force and displacement.
- **Estimated Depth:** High school
- **Principle:** The shadow; Sign and zero
- **Socratic Guidance Chain (if stuck):**
  1. If you pulled straight upwards with 20 N while walking 10 m, would your pull be moving the suitcase forward at all?
  2. Split the 20 N pull into a part along the floor and a part straight up. How big is the part along the floor at 60°?
  3. Which of the two parts acts in the direction the suitcase actually moves?
  4. Work is the force along the motion times the distance. What does that give here?
  5. Where have you already met "the part of one vector along another, times the length of the other"?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Only the part of the force along the motion does work | The shadow | Compute work for a slanted force and for a force at right angles to the motion | overgeneralization: work taken as force times distance whatever the direction |
  | Work is the dot product of force and displacement | The shadow | Compute work from the components of force and displacement | verbal-without-formal: explains the idea but cannot compute from components |
  | Negative work means the force opposes the motion | Sign and zero | Interpret a negative result in a concrete case | conflation: negative work treated as a mistake |
- **Teach Topics:** Definition of work and the joule (KF-7); the force along the motion as a shadow; here the raw dot product is wanted, with no division by lengths, because size matters; zero and negative work. Pitfalls: [overgeneralization] force times distance in every case; [conflation] "effort felt" confused with work done. Socratic teaching note: ask "which part of the pull is doing the moving?" before any number is written.
- **Final Test:** Wind pushes a boat with the force F = (−20, 50) N while the boat travels through the displacement d = (30, 10) m. How much work does the wind do on the boat? Reconstruct the reasoning: what does the sign of your answer say about the wind? In which direction would the boat have to travel for the wind to do no work at all, and why? (Expected: −600 + 500 = −100 J, the wind on balance opposes the motion; any displacement along (5, 2) or its opposite gives zero.)

### SG-9: Lists too long to draw
- **Discovery Question:** A film is described by four numbers: action, humour, romance, suspense. Nobody can draw an arrow with four components, so there is no shadow to look at and no angle to measure. Does "how well do these two films match" still have an answer, and how would you get it?
- **Initial Test:** Your film taste, in the order (action, humour, romance, suspense), is u = (1, 2, 0, 2). Three films: A = (2, 1, 2, 0), B = (2, 4, 4, 4), C = (0, 2, −1, 2). Rank the films by how well they match your taste and justify the ranking with numbers. (Designed tension: the raw dot products rank B first; the fair ranking puts C first.)
- **Pass Criteria:** Raw dot products 4, 18 and 8; lengths 3 for u, 3 for A, about 7.21 for B, 3 for C; match scores about 0.44, 0.83 and 0.89 (±0.02); ranking C, B, A; states that the same two steps work without any picture.
- **Estimated Depth:** High school
- **Principle:** Multiply-and-add scoring; Length versus direction
- **Socratic Guidance Chain (if stuck):**
  1. Does the rule "multiply in pairs and add" need a drawing? What does it give for u and each film?
  2. Film B has large numbers everywhere. What do you already know about long vectors and raw scores?
  3. With two components the length was the square root of the sum of the squares. What would be the natural length for four components?
  4. Divide each raw score by both lengths. What is the ranking now?
  5. You have just compared directions that you cannot draw. Which parts of the two-component reasoning did you actually need?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | The component rule and the length rule extend to any number of components | Multiply-and-add scoring | Compute a dot product and a length for five-component lists | missing-prerequisite: length of a longer list not known |
  | The match score still means "direction agreement" when no picture exists | Length versus direction | Interpret scores of 1, 0 and −1 for two lists of ratings | formal-without-intuitive: computes the score but cannot say what it means for ratings |
  | Raw and fair rankings can differ, and the fair one answers the "taste" question | Length versus direction | Give both rankings and say which to use, and why | overgeneralization: ranks by raw score |
- **Teach Topics:** Dot product and length for longer lists (KF-1, KF-5); cosine similarity (KF-6); a component of zero silences a category; what a negative match means for ratings. Pitfalls: [overgeneralization] ranking by raw score; [formal-without-intuitive] numbers without a reading. Socratic teaching note: ask "which step needed the drawing?" and let the learner find that none did.
- **Final Test:** A survey has five questions. Your answers: u = (1, 1, 1, 1, 0). Three classmates: X = (3, 3, 0, 0, 0), Y = (1, 1, 1, 0, 1), Z = (−1, −1, −1, −1, 2). Rank them by how well their views match yours. Reconstruct the reasoning: why does X win on the raw score and lose on the fair one? What does Z's score say? Why does question 5 contribute nothing to any of your scores? (Expected: raw 6, 3, −4; lengths 2 for u, about 4.24, 2 and about 2.83; match scores about 0.71, 0.75 and −0.71; ranking Y, X, Z.)

### SG-10: Teach it back
- **Discovery Question:** A classmate says: "The dot product is just a formula: multiply, add, done. It doesn't *mean* anything." You have five sentences, one sketch and one set of numbers to change their mind. What do you say?
- **Initial Test:** A delivery robot moves along a corridor whose direction is c = (4, 3). Four thrusters are available: T₁ = (8, 6), T₂ = (5, 0), T₃ = (−3, 4), T₄ = (−4, −3). (a) Compute c·T for each. (b) Find each thruster's shadow on the corridor line. (c) Find each match score. (d) In at most five sentences and one sketch, explain why the dot product measures how well a thruster matches the corridor, and what the raw number in (a) mixes together. (Designed tension: ranking by raw score or by thruster strength hides the difference between "strong" and "aligned"; T₂, T₃ and T₄ all have strength 5.)
- **Pass Criteria:** At least 10 of the 12 numbers correct: dot products 50, 20, 0, −25; shadows 10, 4, 0, −5; match scores 1, 0.8, 0, −1. The explanation contains all four ideas: products of components are votes that add; only the part along the other vector counts; the sign shows with, across or against; dividing by the lengths leaves alignment alone.
- **Estimated Depth:** High school
- **Principle:** All four
- **Socratic Guidance Chain (if stuck):**
  1. In c·T₂ = 4 × 5 + 3 × 0, what does each product say about T₂ and the corridor?
  2. Draw T₂ and the corridor from the same point. Which part of T₂ can move the robot along the corridor, and how long is it?
  3. T₃ and T₄ have the same strength as T₂. Why are their results so different, and what do the 0 and the minus sign tell you?
  4. T₁ is aligned with the corridor exactly, and so would be a thruster half its size. Which number in your table shows that, and what did you have to remove to get it?
  5. Put your four answers into one sentence each. What is the fifth sentence, the one that ties them together?
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | All four principles are used together on one case | All four principles | Complete the table of dot products, shadows and match scores | procedural-without-conceptual: correct table, no explanation |
  | The explanation connects arithmetic to geometry | SG-6 link | Explain one number in the table both as votes and as a shadow | formal-without-intuitive: quotes formulas without a picture |
  | Raw score and match score answer different questions | Length versus direction | Say when each should be used, with an example | overgeneralization: one of the two used everywhere |
  | The explanation is the learner's own and survives a "why" | Teach-back | Answer one follow-up "why" on any sentence of the explanation | verbal-without-formal: fluent words that the numbers do not support |
- **Teach Topics:** Combining the four principles in one account; choosing between raw score and match score; one sketch that carries the whole explanation. Pitfalls: [procedural-without-conceptual] numbers without meaning; [verbal-without-formal] story without numbers. Socratic teaching note: act as the sceptical classmate and ask "why?" after each sentence of the learner's explanation.
- **Final Test:** A listener's taste, in the order (beat, melody, lyrics), is l = (2, 2, 1). Four tracks: P = (4, 4, 2), Q = (6, 6, −3), R = (1, −2, 2), S = (−2, −2, −1). Give each track's dot product with l and its match score, and rank the tracks by match. Then write the explanation you would give a classmate: why does Q beat P on the raw score although P matches perfectly? What do R's and S's scores mean? What would change if every track were brought to length 1 before scoring, and why? (Expected: raw 18, 21, 0, −9; lengths 3 for l, 6, 9, 3 and 3; match scores 1, about 0.78, 0 and −1; ranking P, Q, R, S.)

## Artefacts Register
> _Visible anchor for every artefact this course produces. Seeded at plan
> creation and updated as sessions run — each artefact is reusable context._

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| Why the Dot Product Measures a Match (Socratic) | plan | — | dot-product-socratic_training_plan.md | current |

## Progress Log
(updated by /run-session)
