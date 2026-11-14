# Training Plan: Compound Interest and Present Value of a Single Payment
Generated: 2026-11-13 | Status: in-progress

## Learning Goal
Learn to compute compound interest and present value of a single future payment

## SMART Goal
Accurately compute compound interest, future value, and present value of any single payment, unaided.

## Motivation & Course Overview (VOC)
> _Editable by the learner. This is the course's bird's-eye view and
> voice-of-customer anchor. If you change anything here, tell me — your
> feedback may restructure the plan (re-decomposition of sub-goals)._

**Why this matters:** Almost every money decision — saving, borrowing, accepting a payment later instead of now — compares amounts at different dates. Without compounding and discounting you cannot tell whether "$12,000 in three years" beats "$10,000 today", and the party who can do the arithmetic usually gets the better side of the deal.

**Bird's-eye view of the course:** The course starts with why a sum of money has a date attached to it, then builds the one formula that moves a single amount forward in time (compounding) and its mirror image that moves it backward (discounting). In between it deals with the detail that causes most real-world errors: interest that compounds more often than once a year. It finishes with a spreadsheet implementation and an integrated case where you choose between two real offers and defend the choice with numbers.

**Core principles & key facts:**
- **Time value of money** — an amount today is worth more than the same amount later, because today's amount can earn interest in the meantime.
- **Compounding** — interest is added to the balance and then earns interest itself, so growth is multiplicative, not additive.
- **Period matching** — the rate and the number of periods must both be expressed per compounding period (a 12% annual rate compounded monthly is 1% for 12 periods, not 12% for 1).
- **Discounting** — present value is compounding run in reverse: divide the future amount by the same growth factor.
- Key facts: compound interest earned = future value − starting amount; a higher rate or a longer wait always lowers present value; this plan covers a *single* payment only (no annuities or payment streams).

**What you'll be able to do on completion:**
- Compute the future value and the compound interest earned on a single deposit for any rate, term, and compounding frequency.
- Convert a quoted nominal rate into an effective annual rate and compare offers quoted on different bases.
- Compute the present value of a single future payment and verify it by compounding forward.
- Predict, before calculating, how a change in rate or time moves a present value.
- Build and check FV/PV calculations in a spreadsheet.
- Decide between "money now" and "money later" in a realistic case and justify the choice numerically.

## Principle Extraction

| Principle | Statement | Formally | Prerequisites |
|-----------|-----------|---------|---------------|
| Time value of money | An amount available today is worth more than the same amount later, because it can earn interest in between. | $PV \cdot (1+r) > PV$ for $r > 0$ | Percentages; percent ↔ decimal conversion |
| Compounding | Each period's interest is added to the balance, so later interest is earned on earlier interest. | $FV = PV\,(1+r)^{n}$ | Time value of money; exponents; order of operations |
| Period matching | The rate and the period count must both be stated per compounding period. | $FV = PV\left(1+\tfrac{r}{m}\right)^{m t}$ | Compounding; fractions/division |
| Discounting | Present value is the amount that would grow to the future payment; it is the inverse of compounding. | $PV = \dfrac{FV}{(1+r)^{n}}$ | Compounding; division as inverse of multiplication |

## Sub-Goals

| # | Axis | Sub-Goal | Domain | Difficulty | Depth | Principle | Status | Score |
|---|------|----------|--------|-----------|-------|-----------|--------|-------|
| SG-1 | Motivation | Explain why amounts at different dates cannot be compared without an interest rate. | Personal finance | low | intro | — | pending | - |
| SG-2 | Core Principle | State the time value of money and apply it to a one-year choice. | Financial math | low | intro | Time value of money | pending | - |
| SG-3 | Core Principle | State the compounding principle and grow a deposit year by year for three years. | Financial math | low | intro | Compounding | pending | - |
| SG-4 | Core Principle | State period matching and convert an annual rate into periodic rate and period count. | Financial math | low | intro | Period matching | pending | - |
| SG-5 | Core Principle | State discounting as inverse compounding and discount a payment due in one or two years. | Financial math | low | intro | Discounting | pending | - |
| SG-6 | Key Concept | Distinguish simple from compound interest and quantify the difference on one deposit. | Financial math | low | intro | Compounding | pending | - |
| SG-7 | Key Concept | Compute future value and total compound interest for multi-year annual compounding within 0.5%. | Financial math | low | intro | Compounding | pending | - |
| SG-8 | Key Concept | Compute future value under semiannual, quarterly, and monthly compounding within 0.5%. | Financial math | medium | inter | Compounding; Period matching | pending | - |
| SG-9 | Key Concept | Convert nominal rates to effective annual rates and rank competing offers correctly. | Financial math | medium | inter | Compounding; Period matching | pending | - |
| SG-10 | Key Concept | Compute present value of one future payment with annual compounding and verify forward. | Financial math | medium | inter | Compounding; Discounting | pending | - |
| SG-11 | Key Concept | Compute present value of one future payment under non-annual compounding within 0.5%. | Financial math | medium | inter | Period matching; Discounting | pending | - |
| SG-12 | Key Concept | Predict and compute how rate and time changes move a present value. | Financial math | medium | inter | Time value of money; Discounting | pending | - |
| SG-13 | Tools | Build spreadsheet FV and PV calculations that match manual formula results exactly. | Spreadsheet modelling | medium | inter | Compounding; Period matching; Discounting | pending | - |
| SG-14 | Verification | Solve an integrated now-versus-later case and defend the recommendation with correct figures. | Financial decision-making | high | adv | All four | pending | - |

## Prerequisite Graph

```
Compute compound interest and present value of a single payment (core)
  requires:
    Percent ↔ decimal conversion (prerequisite) ← CHECK learner profile
    Exponents and order of operations (prerequisite) ← CHECK learner profile
    Calculator or spreadsheet power key (y^x / ^) (prerequisite) ← CHECK learner profile
  rests on:
    Time value of money (principle) → SG-2
      led to:
        Compounding (principle) → SG-3
          led to:
            Period matching (principle) → SG-4
            Discounting (principle) → SG-5
```

> **WARNING — unconfirmed prerequisites:** No `learner_profile.md` exists, so none of the three external prerequisites is confirmed. If percent-to-decimal conversion or exponents feel shaky, say so at the start of SG-2 and the session will include a short refresher.

## Sequence
- SG-1 first (no dependencies).
- SG-2 → SG-3 (Compounding is derived from Time value of money).
- SG-3 → SG-4 and SG-3 → SG-5 (both Period matching and Discounting are derived from Compounding). SG-4 and SG-5 can be taken in either order.
- SG-6, SG-7 depend on SG-3.
- SG-8, SG-9 depend on SG-3 and SG-4.
- SG-10 depends on SG-3 and SG-5.
- SG-11 depends on SG-4 and SG-5.
- SG-12 depends on SG-2 and SG-5.
- SG-13 depends on SG-3, SG-4, SG-5.
- SG-14 last; depends on SG-2 through SG-5 (and in practice exercises everything in SG-6 to SG-13).

Recommended order: SG-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.

## Session Blueprints

### SG-1: Why money has a date on it
- **Initial Test:** A friend is selling a car. One buyer offers $10,000 today; another offers $12,000 paid in three years. Your friend's savings account pays 5% a year. No calculation required: explain what your friend needs to work out to choose, what piece of information makes the two offers comparable, and name two other everyday decisions with the same structure.
- **Pass Criteria:** States that amounts at different dates are not directly comparable; names the interest rate (what the money could earn) as the conversion tool; gives 2 valid everyday examples.
- **Estimated Depth:** introductory
- **Principle:** —
- **Exercise:** Write down three money decisions from your own life (one saving, one borrowing, one "pay now or later"). For each, note in one line: who earns the interest, who pays it, and over what length of time. Expected outcome: a three-row table with all three columns filled.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Amounts at different dates need conversion to a common date before comparison | Time value framing | Given two dated offers, says what must be computed before choosing | overgeneralization: "the bigger number wins" |
  | The interest rate represents what the money could otherwise earn | Opportunity cost | Explains in own words why the savings rate is relevant to the car sale | conflation: treating the rate as inflation only |
- **Teach Topics:** Dated cash amounts; opportunity cost of waiting; where the "right" rate comes from (your realistic alternative); the two directions of conversion (forward = future value, backward = present value) named but not computed. Pitfalls — [overgeneralization]: comparing face amounts directly; [conflation]: equating time value with inflation; [verbal-without-formal]: saying "money now is better" without being able to say what would be calculated.
- **Final Test:** A prize winner may take $50,000 now or $60,000 in four years; their bank pays 4%. Explain, without calculating, what must be computed to decide, why the 4% matters, and how the decision could change if the bank paid 1% instead.

### SG-2: Time value of money
- **Principle:** Time value of money — An amount available today is worth more than the same amount later, because it can earn interest in between.
- **Worked Example (foundational):**
  **Given:** You can have $1,000 today or $1,000 in one year. Your savings account pays 5% per year.
  **Step 1:** Convert the rate to a decimal: 5% = 0.05.
  > **Why:** Rates must be decimals before they go into any calculation.
  **Step 2:** Move today's $1,000 forward one year: $1,000 × (1 + 0.05) = $1,050.
  > **Why:** To compare the two options they must be expressed at the same date. Taking the money today and banking it gives principal plus one year of interest.
  **Step 3:** Compare at the one-year date: $1,050 (take it now) versus $1,000 (wait).
  > **Why:** Only now are both amounts in "one-year-from-now dollars", so the comparison is fair.
  **Result:** Taking $1,000 today leaves you $50 better off in one year. The same face amount is worth more the sooner you receive it.
- **Initial Test:** A client will pay your $2,000 invoice either today or in exactly one year — same amount either way. Your account pays 4% a year. Which do you choose, by how many dollars is it better one year from now, and what general principle does this illustrate (in your own words)?
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** introductory
- **Exercise:** Take $500 today. Compute what it becomes after one year at 3%, 6%, and 10%. Then answer: at which of those rates would you be exactly indifferent between $500 today and $530 in one year? Expected outcome: $515, $530, $550; indifferent at 6%.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Amounts must be brought to the same date before comparing | Time value of money | Moves a today-amount one year forward and compares at that date | procedural-without-conceptual: computes interest but compares against the wrong date's amount |
  | The rate used is the learner's own earning alternative | Time value of money | Explains why changing the account rate changes the size of the advantage | conflation: time value = inflation |
- **Teach Topics:** The principle; one-period growth factor (1 + r); "indifference" amount; boundary conditions (r = 0 makes dates irrelevant; the principle needs a positive rate); percent-to-decimal refresher if needed. Misunderstandings — [conflation]: inflation vs earning opportunity; [missing-prerequisite]: using 5 instead of 0.05; [overgeneralization]: "now is always better" even when the later amount is larger.
- **Final Test:** A landlord can return your $1,500 deposit today or the same $1,500 one year from now. Your account pays 6%. State the principle in your own words, say which you prefer, and quantify the difference at the one-year date.

### SG-3: Compounding
- **Principle:** Compounding — Each period's interest is added to the balance, so later interest is earned on earlier interest.
- **Worked Example (foundational):**
  **Given:** $1,000 deposited at 10% per year, compounded annually, for 2 years.
  **Step 1:** Year 1: $1,000 × 1.10 = $1,100.
  > **Why:** One year of growth multiplies the balance by (1 + r) = 1.10. Interest this year is $100.
  **Step 2:** Year 2: $1,100 × 1.10 = $1,210.
  > **Why:** The second year's 10% applies to the *new* balance of $1,100, not the original $1,000. Interest this year is $110 — $100 on the original deposit plus $10 on last year's interest.
  **Step 3:** Collapse the steps: $1,000 × 1.10 × 1.10 = $1,000 × (1.10)² = $1,210.
  > **Why:** Multiplying by the same factor n times is raising it to the power n. This is where FV = PV(1 + r)ⁿ comes from.
  **Result:** $1,210 after 2 years; $210 total interest, of which $10 is interest earned on interest.
- **Initial Test:** You deposit $2,000 at 5% per year, compounded annually, for 3 years. Show the balance at the end of each year, state the interest earned in each year, and explain in your own words why year 3's interest is larger than year 1's.
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** introductory
- **Exercise:** Build a year-by-year table for $1,000 at 8% for 4 years (columns: opening balance, interest, closing balance). Then compute $1,000 × 1.08⁴ in one step and confirm it matches the last row. Expected outcome: closing balances $1,080.00, $1,166.40, $1,259.71, $1,360.49.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Each period's rate applies to the current balance, not the original deposit | Compounding | Produces a correct year-by-year table with rising interest | conflation: applies the rate to the original principal every year (simple interest) |
  | Repeated multiplication is the origin of the exponent | Compounding | Explains why the formula has ⁿ and not × n | procedural-without-conceptual: uses the formula but cannot reproduce it with a table |
- **Teach Topics:** The principle; growth factor (1 + r); table method vs formula; interest-on-interest as the gap between the two; boundary conditions (n = 1 is identical to simple interest; n = 0 gives PV). Misunderstandings — [conflation]: simple vs compound; [procedural-without-conceptual]: PV × (1 + r × n) or PV × (1 + r) × n; [missing-prerequisite]: exponent entry on a calculator.
- **Final Test:** $5,000 is deposited at 4% per year, compounded annually, for 3 years. Give the balance after each year, the one-step formula result, and explain where the "extra" interest beyond 3 × $200 comes from.

### SG-4: Period matching
- **Principle:** Period matching — The rate and the period count must both be stated per compounding period.
- **Worked Example (foundational):**
  **Given:** $1,000 at a quoted 12% per year, compounded semiannually (twice a year), for 1 year.
  **Step 1:** Find the rate per period: 12% ÷ 2 = 6% per half-year.
  > **Why:** The quoted 12% is an annual label. The bank actually applies interest every six months, so each application uses half the annual rate.
  **Step 2:** Find the number of periods: 1 year × 2 = 2 half-years.
  > **Why:** The exponent counts how many times interest is applied, not how many years pass.
  **Step 3:** Compound: $1,000 × (1.06)² = $1,123.60.
  > **Why:** Same compounding principle as before, now with a matched pair: 6% per period, 2 periods.
  **Result:** $1,123.60 — $3.60 more than the $1,120 that annual compounding would give, because the first half-year's $60 of interest itself earned interest in the second half.
- **Initial Test:** $1,000 is deposited at a quoted 8% per year, compounded quarterly, for 1 year. State the rule for handling the rate and the number of periods, identify the periodic rate and period count, and compute the balance.
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** introductory
- **Exercise:** For a quoted 12% annual rate over 3 years, fill in a table of (periodic rate, number of periods) for annual, semiannual, quarterly, and monthly compounding. No future values needed. Expected outcome: (12%, 3), (6%, 6), (3%, 12), (1%, 36).
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Rate and period count are converted together, as a pair | Period matching | Gives correct (r/m, m·t) for any frequency | procedural-without-conceptual: divides the rate but leaves the exponent in years (or vice versa) |
  | More frequent compounding of the same quoted rate gives a larger result | Period matching | Predicts direction of change before computing | overgeneralization: assumes the quoted annual rate is what is actually earned |
- **Teach Topics:** The principle; compounding frequency m (1, 2, 4, 12, 365); periodic rate r/m and period count m·t; quoted (nominal) rate as a label; boundary condition m = 1 reduces to the annual formula. Misunderstandings — [procedural-without-conceptual]: mismatched pair, e.g. 1% with 3 periods or 12% with 36; [conflation]: nominal rate vs rate actually earned (developed fully in SG-9).
- **Final Test:** $2,000 is deposited at a quoted 6% per year, compounded monthly, for 2 years. State the principle, give the periodic rate and number of periods, and compute the final balance.

### SG-5: Discounting
- **Principle:** Discounting — Present value is the amount that would grow to the future payment; it is the inverse of compounding.
- **Worked Example (foundational):**
  **Given:** You will receive $1,210 in 2 years. Money can earn 10% per year, compounded annually.
  **Step 1:** Ask the compounding question backwards: what amount X today satisfies X × (1.10)² = $1,210?
  > **Why:** "Worth today" means the amount that would become the future payment if invested at the available rate.
  **Step 2:** Compute the growth factor: (1.10)² = 1.21.
  > **Why:** It is the same factor used to compound forward over two years.
  **Step 3:** Divide instead of multiply: X = $1,210 ÷ 1.21 = $1,000.
  > **Why:** Division undoes multiplication, so dividing by the growth factor undoes two years of growth.
  **Step 4:** Check forward: $1,000 × 1.21 = $1,210. ✓
  > **Why:** Every present value can be verified by compounding it back to the future date.
  **Result:** The present value of $1,210 due in 2 years at 10% is $1,000. Being handed $1,000 today and being promised $1,210 in two years are equivalent at this rate.
- **Initial Test:** You are owed $5,250, payable in one year. Money can earn 5% a year. What is that promise worth today? State in your own words how present value relates to compounding, and show a check of your answer.
- **Pass Criteria:** Can state the principle in own words AND apply it to a basic scenario correctly
- **Estimated Depth:** introductory
- **Exercise:** Find the present value at 10% of $1,000 due in 1 year, in 2 years, and in 3 years. Then pick one answer and compound it forward to confirm it returns $1,000. Expected outcome: $909.09, $826.45, $751.31.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | PV is found by dividing by the growth factor, not by subtracting interest | Discounting | Discounts one payment and verifies by compounding forward | conflation: computes FV × (1 − r)ⁿ or FV − FV × r × n |
  | PV and FV are the same value seen at two dates | Discounting | Explains why PV < FV whenever r > 0 | formal-without-intuitive: applies the formula but cannot say what the PV means |
- **Teach Topics:** The principle; discount factor 1/(1 + r)ⁿ; forward check as a habit; "discount rate" as the same rate viewed backwards; boundary conditions (r = 0 → PV = FV; n = 0 → PV = FV). Misunderstandings — [conflation]: discounting vs taking a percentage off; [formal-without-intuitive]: no interpretation of PV as "the deposit that would grow into it"; [procedural-without-conceptual]: multiplying instead of dividing.
- **Final Test:** A relative promises you $2,420 in two years. Money can earn 10% a year, compounded annually. State the principle, compute what the promise is worth today, and verify it.

### SG-6: Simple vs compound interest
- **Initial Test:** Two banks offer a 5-year term deposit for your $10,000. Bank A pays 6% simple interest; Bank B pays 6% compounded annually. Compute the maturity amount at each, the dollar difference, and explain where the difference comes from.
- **Pass Criteria:** Both maturity amounts within $1; difference correct; explanation identifies interest earned on prior interest.
- **Estimated Depth:** introductory
- **Principle:** Compounding
- **Exercise:** For $1,000 at 10%, tabulate the balance at the end of years 1 to 5 under simple interest and under annual compounding, plus a third column for the gap. Expected outcome: simple $1,100 / $1,200 / $1,300 / $1,400 / $1,500; compound $1,100 / $1,210 / $1,331 / $1,464.10 / $1,610.51; gap $0 / $10 / $31 / $64.10 / $110.51 — note that the gap itself accelerates.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Simple interest grows linearly; compound grows exponentially | Simple vs compound | Selects the right formula from a verbal description of the terms | conflation: uses PV(1 + rn) when terms say "compounded" |
  | The two coincide for one period and diverge afterwards | Simple vs compound | States when the methods give the same answer | overgeneralization: "compound is always much bigger" regardless of term |
  | The gap is interest on interest | Compounding | Decomposes compound interest into simple interest + interest on interest | procedural-without-conceptual: computes both but cannot explain the gap |
- **Teach Topics:** Simple interest formula; compound formula side by side; linear vs exponential shape; reading contract wording ("simple", "compounded annually", "per annum"); decomposition of total interest. Pitfalls — [conflation]: formula mix-up; [overgeneralization]: ignoring that the gap is small for short terms and low rates; [procedural-without-conceptual]: no account of the gap.
- **Final Test:** You lend $4,000 for 8 years at 5%. Compute what you are repaid if the agreement says simple interest and if it says annual compounding, give the difference, and state how much of the compound total is interest on interest.

### SG-7: Future value and compound interest, annual compounding
- **Initial Test:** You place $7,500 in an account paying 4.5% per year, compounded annually, and leave it for 10 years. Compute the balance at the end and the total compound interest earned.
- **Pass Criteria:** Future value within 0.5%; interest earned reported separately and consistent with FV − PV.
- **Estimated Depth:** introductory
- **Principle:** Compounding
- **Exercise:** Compute the future value of $2,500 at 7% compounded annually for 6 years in one step with the formula, then state the compound interest earned. Expected outcome: FV ≈ $3,751.83; interest ≈ $1,251.83.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | FV = PV(1 + r)ⁿ applied in a single step for any n | FV formula | Correct FV for a 10+ year term without a table | procedural-without-conceptual: multiplies by n instead of raising to n |
  | Compound interest is FV − PV, not FV | Interest vs balance | Reports both figures, correctly labelled | conflation: gives the ending balance when asked for interest earned |
  | Rate entered as a decimal, non-round rates included | Rate handling | Uses 0.045 for 4.5% | missing-prerequisite: 1.45 or 1.0045 for 4.5% |
- **Teach Topics:** One-step formula; identifying PV, r, n from a word problem; interest earned vs ending balance; rounding only at the end; sanity check against simple interest (compound FV must exceed PV(1 + rn) for n > 1). Pitfalls — [procedural-without-conceptual]: × n; [conflation]: interest vs FV; [missing-prerequisite]: decimal conversion of fractional percentages.
- **Final Test:** $12,000 is invested at 3.2% per year, compounded annually, for 15 years. Compute the ending balance and the total interest earned, and give a quick sanity check that your answer is plausible.

### SG-8: Future value with non-annual compounding
- **Initial Test:** You have $5,000 to deposit for 3 years at a quoted 6% per year. Compute the ending balance if interest is compounded (a) annually, (b) quarterly, (c) monthly, and state how much extra monthly compounding earns over annual.
- **Pass Criteria:** All three future values within 0.5%; correct ordering; rate and periods correctly paired in each case.
- **Estimated Depth:** intermediate
- **Principle:** Compounding; Period matching
- **Exercise:** Compute the 1-year future value of $1,000 at a quoted 12% under annual, semiannual, quarterly, and monthly compounding. Expected outcome: $1,120.00, $1,123.60, $1,125.51, $1,126.83 — increasing, but by smaller steps each time.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | FV = PV(1 + r/m)^(m·t) with both adjustments made | General FV formula | Correct FV for a multi-year monthly case | procedural-without-conceptual: adjusts only the rate or only the exponent |
  | Higher frequency raises FV, with diminishing increments | Frequency effect | Predicts ordering and rough size of gaps before calculating | overgeneralization: expects monthly to be dramatically larger than quarterly |
  | Periodic rate kept at full precision | Numerical care | Uses 0.06/12 = 0.005 exactly, not a rounded percent | missing-prerequisite: rounding the periodic rate early and compounding the error |
- **Teach Topics:** General formula; extracting m from wording ("compounded monthly", "semiannually", "daily"); terms not in whole years (e.g., 18 months quarterly = 6 periods); diminishing gains from higher frequency; precision. Pitfalls — [procedural-without-conceptual]: mismatched pair; [overgeneralization]: frequency effect size; [missing-prerequisite]: early rounding.
- **Final Test:** $8,000 is deposited for 5 years at a quoted 4.8% per year. Compute the ending balance with monthly compounding and with quarterly compounding, and state the dollar advantage of monthly.

### SG-9: Effective annual rate
- **Initial Test:** Bank A advertises 5.9% per year compounded monthly. Bank B advertises 6.0% per year compounded annually. Which account actually pays more over a year? Support the answer with each bank's effective annual rate.
- **Pass Criteria:** Both effective rates correct to 0.02 percentage points; correct ranking; explains why the lower quoted rate can win.
- **Estimated Depth:** intermediate
- **Principle:** Compounding; Period matching
- **Exercise:** Compute the effective annual rate for a quoted 12% compounded semiannually, quarterly, and monthly. Expected outcome: 12.36%, 12.55%, 12.68%.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | EAR = (1 + r/m)^m − 1 is the true one-year growth | Effective rate | Converts any nominal rate/frequency to EAR | conflation: treats the nominal (quoted) rate as the rate earned |
  | Offers must be compared on EAR, not on quoted rate | Rate comparison | Ranks two offers quoted on different bases | overgeneralization: "higher quoted rate is always better" |
  | EAR applies to borrowing as well as saving | Rate comparison | Identifies the more expensive of two loans | formal-without-intuitive: computes EAR but cannot say what it means for the cost of a loan |
- **Teach Topics:** Nominal vs effective rate; EAR formula as a one-year FV of $1; using EAR for multi-year FV (PV × (1 + EAR)^t gives the same result as the periodic formula); borrower's view (APR on cards and loans). Pitfalls — [conflation]: nominal vs effective; [overgeneralization]: ranking by headline rate; [formal-without-intuitive]: EAR without interpretation.
- **Final Test:** A credit card charges 18% per year compounded monthly. A personal loan charges 19% per year compounded annually. Which is the more expensive way to borrow for a year? Give both effective annual rates.

### SG-10: Present value, annual compounding
- **Initial Test:** An investment promises a single payment of $20,000 five years from now. You could otherwise earn 6% per year, compounded annually. What is the most you should pay for it today? Verify your figure.
- **Pass Criteria:** Present value within 0.5%; forward check shown; correctly interprets PV as a maximum price.
- **Estimated Depth:** intermediate
- **Principle:** Compounding; Discounting
- **Exercise:** Compute the present value of $10,000 due in 4 years at 5% compounded annually, then compound your answer forward 4 years to confirm it returns $10,000. Expected outcome: PV ≈ $8,227.02.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | PV = FV ÷ (1 + r)ⁿ for multi-year terms | PV formula | Correct PV for a 5+ year single payment | conflation: FV × (1 − r)ⁿ, or subtracting simple interest |
  | Recognising which amount is given (PV or FV) in a word problem | Problem setup | Classifies four short scenarios as "find FV" or "find PV" | procedural-without-conceptual: compounds when the question requires discounting |
  | PV is a decision threshold (max price / min acceptable amount today) | Interpretation | States whether to accept a given asking price | formal-without-intuitive: correct number, no decision |
- **Teach Topics:** PV formula and discount factor; cue words for direction ("worth today", "need to deposit now", "will grow to"); forward verification; PV as a price ceiling; discount factor tables as an optional aid. Pitfalls — [conflation]: percentage-off thinking; [procedural-without-conceptual]: wrong direction; [formal-without-intuitive]: no decision drawn.
- **Final Test:** A supplier will pay you a $50,000 rebate eight years from now. Your alternative earns 4.5% per year, compounded annually. A financing firm offers to buy the rebate from you today for $34,000. Compute the present value and say whether to accept.

### SG-11: Present value, non-annual compounding
- **Initial Test:** You need exactly $15,000 in 3 years for a deposit on a home. An account pays a quoted 6% per year, compounded monthly. How much must you put in today as a single deposit? Show the periodic rate and period count you used.
- **Pass Criteria:** Present value within 0.5%; periodic rate and period count correctly paired; forward check shown.
- **Estimated Depth:** intermediate
- **Principle:** Period matching; Discounting
- **Exercise:** Compute the present value of $5,000 due in 2 years at a quoted 8% compounded quarterly, then recompute with annual compounding and compare. Expected outcome: ≈ $4,267.45 quarterly vs ≈ $4,286.69 annual — more frequent compounding gives a *lower* present value.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | PV = FV ÷ (1 + r/m)^(m·t) with matched rate and periods | General PV formula | Correct PV for a monthly-compounded multi-year case | procedural-without-conceptual: adjusts rate but not exponent when discounting |
  | Higher compounding frequency lowers PV | Frequency effect on PV | Predicts direction before computing | overgeneralization: carries "more frequent = bigger number" over from FV |
- **Teach Topics:** General PV formula; symmetry with SG-8; why frequency moves PV in the opposite direction to FV; equivalent route via EAR; forward check with the periodic formula. Pitfalls — [procedural-without-conceptual]: mismatched pair; [overgeneralization]: wrong direction of the frequency effect; [missing-prerequisite]: early rounding of the periodic rate.
- **Final Test:** A contract pays you a single $25,000 in 4 years. Value it today at a quoted 5% per year under semiannual compounding and again under monthly compounding. Which is lower, and why?

### SG-12: How rate and time move present value
- **Initial Test:** A single $10,000 payment is valued under three conditions: (a) 4% for 10 years, (b) 8% for 10 years, (c) 8% for 20 years, all compounded annually. First, *without calculating*, rank the three present values from highest to lowest and justify the ranking. Then compute all three.
- **Pass Criteria:** Ranking correct with a valid justification before calculating; all three values within 0.5%.
- **Estimated Depth:** intermediate
- **Principle:** Time value of money; Discounting
- **Exercise:** Build a 2 × 3 grid of the present value of $1,000 at 5% and 10% (rows) for 5, 10, and 20 years (columns), annual compounding. Expected outcome: 5% row ≈ $783.53, $613.91, $376.89; 10% row ≈ $620.92, $385.54, $148.64.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | PV falls as the rate rises and as the wait lengthens | Sensitivity | Predicts direction of change for any single-variable change | formal-without-intuitive: must recalculate to know the direction |
  | The effect is not proportional — doubling r or n does not halve PV | Non-linearity | Explains why 20 years at 10% is far less than half of 10 years at 10% | overgeneralization: assumes linear scaling |
  | The preferred of two dated payments can flip with the rate | Decision relevance | Finds the preferred option at two different rates | procedural-without-conceptual: computes one PV pair and treats the ranking as fixed |
- **Teach Topics:** Direction of rate and time effects; exponential (non-linear) decay of the discount factor; comparing payments at different dates by bringing both to today; rate-dependent rankings; tie back to SG-1's "now vs later" question. Pitfalls — [formal-without-intuitive]: no directional intuition; [overgeneralization]: linear thinking; [procedural-without-conceptual]: ignoring rate dependence.
- **Final Test:** A legal settlement can be paid as $40,000 in 5 years or $55,000 in 12 years. Evaluate both at 3% and again at 7% (annual compounding). Which do you prefer at each rate, and why does the answer change?

### SG-13: Spreadsheet FV and PV
- **Initial Test:** In a spreadsheet, compute (1) the future value of $3,000 at a quoted 5% compounded monthly for 4 years and (2) the present value of $9,000 due in 6 years at 7% compounded annually. Do each twice: once with a typed-out formula using `^`, once with the built-in `FV` / `PV` function. Report the four results and the formulas used.
- **Pass Criteria:** Manual and built-in results agree to the cent in both cases; inputs are in separate cells (not hard-coded in the formula); results shown as positive amounts with the sign convention explained.
- **Estimated Depth:** intermediate
- **Principle:** Compounding; Period matching; Discounting
- **Exercise:** Build a small calculator with four input cells (starting amount, quoted annual rate, compounding periods per year, years) and one output cell for future value. Test it with $1,000, 12%, 12, 1. Expected outcome: $1,126.83, matching the SG-8 exercise.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | `rate` and `nper` arguments must be per period | Function arguments | Sets up a monthly case with rate/12 and years*12 | procedural-without-conceptual: passes the annual rate with a monthly period count |
  | Sign convention: money paid out and money received have opposite signs | Cash-flow signs | Explains a negative result and corrects it deliberately | missing-prerequisite: "fixes" the sign without knowing why it appeared |
  | Single-payment problems use a zero payment argument | Function arguments | Leaves `pmt` at 0 and places the amount in the correct argument | conflation: puts the lump sum in the `pmt` argument |
- **Teach Topics:** Manual formulas with `^`; `FV(rate, nper, pmt, pv)` and `PV(rate, nper, pmt, fv)`; sign convention; cell-referenced inputs; cross-checking built-in against manual; `EFFECT` for effective rate as an optional extra. Pitfalls — [procedural-without-conceptual]: unmatched rate/nper; [missing-prerequisite]: sign convention; [conflation]: `pmt` vs `pv`/`fv`.
- **Final Test:** A colleague's sheet uses `=FV(6%, 5, 0, -1000)` to value $1,000 left for 5 years at a quoted 6% compounded monthly. Say what is wrong, write the corrected formula, give the corrected result, and confirm it with a manual `^` formula. Then add a cell that computes the present value of $20,000 due in 10 years at a quoted 4% compounded quarterly.

### SG-14: Integrated now-versus-later case
- **Initial Test:** You have inherited $18,000 and will not need it for 6 years. Option A: a term deposit paying a quoted 4.8% per year, compounded monthly. Option B: lend it to a relative's business, which will repay a single $24,500 at the end of year 6. Produce: (1) the maturity value and total interest for Option A; (2) Option A's effective annual rate; (3) the present value of Option B's repayment, discounted at Option A's terms; (4) what Option A would have paid under simple interest, for comparison; (5) a recommendation on the numbers, plus one non-numerical factor you would weigh.
- **Pass Criteria:** At least 4 of the 5 numerical results within 0.5%; recommendation consistent with the learner's own figures; FV comparison and PV comparison shown to point the same way; no rate/period mismatch anywhere.
- **Estimated Depth:** advanced
- **Principle:** Time value of money; Compounding; Period matching; Discounting
- **Exercise:** Write a one-page "method card" in your own words: the two formulas, the three things to extract from any problem (amount and its date, rate per period, number of periods), the cue words that signal FV vs PV, and the forward check. Expected outcome: a card you can solve the Final Test from without other notes.
- **Anticipated CTQs:**
  | CTQ | Source | Mastery Test | Common Failure Mode |
  |-----|--------|-------------|---------------------|
  | Chooses the correct direction (compound or discount) for each part unaided | Problem setup | Completes a multi-part case with no prompts on method | procedural-without-conceptual: applies one formula to every part |
  | Comparing at the future date and comparing at today give the same decision | Equivalence of FV and PV comparison | Shows both comparisons and explains why they must agree | formal-without-intuitive: treats disagreement between the two as possible |
  | Keeps rate and periods matched through a long calculation | Period matching | No mismatched pair in any step | procedural-without-conceptual: reverts to annual rate midway |
  | Separates the numerical answer from judgement factors | Decision quality | Names a relevant non-numerical factor (e.g., risk of non-repayment) | overgeneralization: treats the higher number as automatically the right choice |
- **Teach Topics:** End-to-end method; consistency of FV-based and PV-based comparisons; presenting results (labelled amounts, dates, rate basis); limits of the model (certainty of payment, taxes, access to funds) named but not computed. Pitfalls — [procedural-without-conceptual]: single-formula habit, mismatched periods; [formal-without-intuitive]: not seeing FV/PV comparisons as equivalent; [overgeneralization]: number-only decisions.
- **Final Test:** A small firm is selling a machine. Buyer X offers $42,000 today. Buyer Y offers a single $50,000 payment in 3 years. The firm's bank account pays a quoted 5.5% per year, compounded quarterly. Produce: (1) what Buyer X's $42,000 would grow to in 3 years and the interest earned; (2) the account's effective annual rate; (3) the present value of Buyer Y's offer; (4) the result for part 1 under simple interest; (5) a recommendation consistent with your figures, with one non-numerical factor.

## Artefacts Register
> _Visible anchor for every artefact this course produces. Seeded at plan
> creation and updated as sessions run — each artefact is reusable context._

| Artefact | Type | Source | Path | Status |
|----------|------|--------|------|--------|
| Compound Interest and Present Value of a Single Payment | plan | — | compound-interest-present-value_training_plan.md | current |

## Progress Log
(updated by /run-session)
