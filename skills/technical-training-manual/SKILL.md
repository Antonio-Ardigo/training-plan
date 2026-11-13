---
name: "technical-training-manual"
description: "Write a step-by-step technical training manual as a PDF on any technical subject, in US corporate-manual style, with an explanation before and a worked example after every formula, rule or step."
---

# Technical Training Manual: Specification

Use this skill whenever the user asks for a manual, a training document, a technical note or a revision of one, in any field. Examples: engineering, finance, law, operations, science, software. The output is one PDF that teaches a capable student a technical method in a straight line, and that reads like a US corporate technical manual.

The specification has seven parts: workflow, prompt template, content rules, document architecture, writing style, visual identity and build pipeline. Follow all seven.

---

## 1. Workflow (always in this order)

1. **Restate the request as an expanded prompt.** Fill in the template in Section 2 and send it to the user (SendUserMessage). Do not compress it, and write it in the active voice.
2. **Plan the document.** Send a chapter table: chapter number, title, content. Also list the planned figures and the running examples.
3. **Execute** without waiting, unless the request is ambiguous and expensive to redo.
   - Set up a task list: write content, build figures and render, verify and deliver.
   - Compute every number in code before writing it into the text.
4. **Verify.** Run the QA checklist in Section 8.
5. **Deliver.** Send the PDF with SendUserFile. Finish with a short summary of what the manual covers, with no recap of the steps.

**Revisions and supplements.**
- A follow-up note goes out as a Technical Note (TN number) that cites the parent manual.
- If the user asks to integrate a note into its manual:
  - Issue the manual as the next revision letter.
  - Place each block of the note where it belongs in the reading order. Never just append it.
  - Renumber all chapters, sections, examples, tables, procedures and figures. Rewrite every cross-reference and check them with a regex.
  - Add a line to the Document Control table describing the change, and mark the note as superseded.
  - Remove forward references, for example an example that relies on a state introduced later.

---

## 2. Expanded-prompt template

```
Objective. Produce a PDF technical training manual that teaches a student to [TASK / METHOD] in [FIELD].

Audience. The reader knows [PREREQUISITES]. The reader has no prior knowledge of [WHAT IS NEW].
[If applicable: The reader has read companion manual [DOC-NO].]

Content requirements
1. Show every step of every calculation or procedure. Never skip steps or merge operations into one line.
2. Before each formula / rule / step, explain in plain words what it says and why it is true.
3. After each formula / rule / step, give a concrete worked example the reader can check by hand.
4. Build the material in a straight line: each chapter uses only ideas defined earlier. Order: [TOPIC SEQUENCE].
5. Use running examples that recur throughout: [RUNNING EXAMPLES]. Reuse examples from [COMPANION DOC] where possible.
6. Make the key contrasts explicit: [CONTRASTS / COMMON MISCONCEPTIONS].
7. Verify every number by code before publishing.

Style requirements
1. Active voice; address the reader directly ("Multiply row 1 by column 1").
2. US corporate technical-manual conventions: document control block, table of contents with page numbers, numbered chapters and sections, numbered procedures (Step / Action / Result), NOTE and CAUTION callouts, captioned tables and figures, troubleshooting table, quick-reference card, glossary.
3. US spelling, US Letter page size, house visual identity (navy / blue / orange).

Deliverable. One PDF, document number [PREFIX-TM-NNNN], Revision A.
```

---

## 3. Content rules

**The triad (mandatory for every algebraic line, rule or step).**
1. **Explanation.** A paragraph that starts with a bold "Explanation." and says, in plain words, what the next line states and why it holds.
2. **Formula.** The line itself, in a shaded box. Use the bold-bordered box for a defining or central formula.
3. **Example.** A numbered box (Example X-n) that applies the line to real numbers or a real case. Show the arithmetic term by term, then give the result and a check mark when you verify something.

Never introduce a symbol, term or formula without the triad. If a line depends on a rule the reader may not know (the transpose of a product, a logarithm rule, a sign convention), insert a triad for that rule first.

**Linearity.**
- Chapters run from foundations, to the core method, to alternative and shortcut methods, to worked examples, to verification, troubleshooting and reference.
- No forward references inside the teaching chapters.

**Running examples.**
- Give one or two running examples a name and a highlighted box at their first appearance (`example key`), for example "State S" or "the biased coin".
- Solve the core running example by every method in the manual and show that all methods agree.

**Multiple routes.** When a quantity can be computed in several ways (full method, index formula, visual shortcut, pure-case shortcut), present each one and cross-check them against each other.

**Contrast sections.** Show explicitly where an intuition fails, using numbers. Examples: diagonal vs eigenvalues, classical vs quantum, selector vs projector.

**Verification is content.**
- Every chapter ends its examples with checks (sum, trace, units, bounds, symmetry).
- A dedicated Verification chapter lists checks V1…Vn in a table, each with its rule and a worked example.

**Numbers.**
- Compute every value in Python or Node first.
- Round final values to 3 decimal places and intermediate values to 4.
- Use exact fractions where they are clean.

**Field adaptation of "formula" and "example".**

| Field | "Formula" box holds | "Example" box holds |
|---|---|---|
| Math / physics / quantum | Equation | Numeric substitution, term by term |
| Electrical (MV, protection) | Equation (e.g. I = P / (√3·V·pf)) | Rated case with real nameplate values and units |
| Hydraulics / process | Equation or balance | Plant case with flows, heads and units, plus a unit check |
| Cost estimation / BOQ | Pricing formula or normalization rule | Line items with quantities, rates and totals |
| Finance | Formula (NPV, IRR, WACC) | Cash-flow table worked year by year |
| Law / contracts | Rule or clause | Fact pattern, then application, then conclusion |
| Software | Code snippet or API call | Concrete input, then the exact output |
| Operations / maintenance | Procedure step | Field reading, then decision, then record entry |

---

## 4. Document architecture

1. **Cover** (unnumbered, no header or footer).
   - Top rule with the document number, revision and class ("Technical Training Manual" or "Technical Note").
   - Kicker (series name), H1 title of 2–6 words, and a one-line subtitle.
   - A subject figure drawn to scale.
   - A meta table: document number, revision, issue date, page size or parent document, audience.
2. **Front matter.**
   - Document Control table (Revision, Date, Description of change).
   - Table of Contents with dotted leaders and real page numbers.
   - Conventions table (Explanation, Formula, Example, Procedure, NOTE, CAUTION, ✓ Check, cross-reference format), followed by a NOTE on scope conventions (units, rounding, number system).
3. **Chapter 1, Introduction:**
   - 1.1 Purpose: the single question the method answers.
   - 1.2 Scope: what is in and what is out.
   - 1.3 Prerequisites: a self-check table (Skill, Self-check, Expected result).
   - 1.4 How to Use This Manual: reading order, the triad, the running examples.
4. **Teaching chapters**, each starting on a new page. Headings read "X.0  TITLE" in uppercase and sections read "X.Y  Title".
5. **Worked Examples chapter.** Cover every case class (for example none, partial, full, edge case), each as a Procedure table. End with a summary table across all examples.
6. **Verification Procedure:** a table of checks V1…Vn (Check, Rule, Example).
7. **Troubleshooting:** a table of Symptom, Probable cause, Corrective action, with 6–9 rows. Each corrective action cites a section.
8. **Quick Reference Card:** a 2-column grid of boxed cells with navy headers, one page.
9. **Appendix A, Glossary:** a 2-column table of term and definition.
10. **End mark:** "— End of Document [DOC-NO] —".

**Numbering.**
- Chapters are X.0 and sections X.Y.
- Example X-n, Procedure X-n, Table X-n and Figure X-n all restart in each chapter.
- Cross-references always name the type: "Section 4.4", "Example 7-2", "Table 3-1".
- References to a companion manual use the form "[DOC-NO] x.y".

**Procedures.** A navy title bar reads "Procedure X-n. [Verb phrase]", followed by a table with the columns Step | Action | Result. Write each action as an imperative sentence and put the expected value in the Result column. Mark check steps with ✓.

**Callouts.**
- NOTE (blue label): supporting information.
- CAUTION (amber label): a specific common error and how to avoid it.
- Use at most one or two callouts per section.

**Header and footer** on all pages except the cover:
- Header: bold document number and revision on the left, title on the right.
- Footer: a rule, the document class on the left, "Page n of N" on the right.

---

## 5. Writing style

- Use the active voice and imperative mood for actions ("Compute", "Add", "Confirm"). Address the reader as "you".
- Use US spelling, plain words and short declarative sentences. Never compress reasoning: one idea per sentence, every step written out.
- Define a term in bold at its first use. Use the term consistently afterwards and add it to the glossary.
- Avoid em-dash asides, "not X but Y" framing, rhetorical questions and filler.
- Captions describe what the figure shows and how to read it.
- Mark checks inline with a green ✓.

---

## 6. Visual identity

- **Palette:**
  - Structure: navy #1B2A4A; text: ink #1D2533; secondary text: muted #475569.
  - Rules: line #CBD5E1; formula boxes: panel #F1F4F9; table headers: head #E8EEF7.
  - Notes and category 1: blue #1F5FBF, tint #DCE7FA. Category 2: orange #C2410C, tint #FCE4D6.
  - Cautions: amber #B45309. Checks: green #2F7D4A. Negative or alert values: red #B42318.
- **Type:** Inter for body (9.6pt / 1.5) and Inter Display for headings, with tabular figures; KaTeX for all mathematics.
- **Page:** US Letter, margins 0.9in top, 0.8in sides, 0.85in bottom.
- **Semantic color:** give each category of the subject a fixed color (for example blue for case A, orange for case B) and use it consistently in text tables, figures and legends.
- **Figures:** inline SVG generated in code and drawn to scale.
  - Use one scale per axis, labelled ticks and enough padding that no label is clipped (top padding of at least 30px when a point sits at the maximum).
  - Mark key points in orange with a dashed drop line.
  - Give every figure a caption "Figure X-n.".

### Core stylesheet (copy as is)

```css
:root{--navy:#1B2A4A;--ink:#1D2533;--muted:#475569;--line:#CBD5E1;--panel:#F1F4F9;--head:#E8EEF7;--blue:#1F5FBF;--blueT:#DCE7FA;--orange:#C2410C;--orangeT:#FCE4D6;--amber:#B45309;--green:#2F7D4A}
@page{size:Letter;margin:0.9in 0.8in 0.85in 0.8in}
*{box-sizing:border-box} html,body{margin:0;padding:0}
body{font-family:Inter,"Liberation Sans",Arial,sans-serif;font-size:9.6pt;line-height:1.5;color:var(--ink);font-feature-settings:"tnum" 1;-webkit-print-color-adjust:exact;print-color-adjust:exact}
p{margin:0 0 7pt} b{font-weight:600} .katex{font-size:1.08em} .katex-display{margin:4pt 0}
.cover{height:9.2in;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always}
.cover-top{display:flex;justify-content:space-between;border-bottom:3pt solid var(--navy);padding-bottom:8pt;font-size:9pt;color:var(--muted)}
.docno{font-weight:700;color:var(--navy);letter-spacing:.04em} .class{text-transform:uppercase;letter-spacing:.12em}
.cover-mid{display:flex;flex-direction:column;gap:14pt}
.cover-kicker{text-transform:uppercase;letter-spacing:.14em;font-size:9pt;color:var(--blue);font-weight:600}
.cover h1{font-family:"Inter Display",Inter,sans-serif;font-size:34pt;line-height:1.08;margin:0;color:var(--navy);font-weight:800;letter-spacing:-.01em;max-width:6.2in}
.cover-sub{font-size:13pt;color:var(--muted);max-width:5.6in;margin:0} .cover-fig{margin-top:18pt}
.cover-meta{width:100%;border-collapse:collapse;font-size:8.8pt}
.cover-meta th,.cover-meta td{border:0.75pt solid var(--line);padding:5pt 7pt;text-align:left;vertical-align:top}
.cover-meta th{background:var(--head);color:var(--navy);width:17%;font-weight:600}
.chapter{break-before:page}
h2{font-family:"Inter Display",Inter,sans-serif;font-size:16pt;color:var(--navy);text-transform:uppercase;letter-spacing:.02em;margin:0 0 12pt;padding:6pt 0;border-top:3pt solid var(--navy);border-bottom:0.75pt solid var(--line);font-weight:700;break-after:avoid}
h2.nonum{font-size:13pt;margin-top:18pt} .front h2.nonum:first-child{margin-top:0}
h3{font-size:11.5pt;color:var(--navy);margin:16pt 0 7pt;font-weight:700;break-after:avoid}
.formula{background:var(--panel);border:0.75pt solid var(--line);padding:3pt 10pt;margin:6pt 0 9pt;break-inside:avoid;overflow:hidden}
.formula.big{border:1.5pt solid var(--navy);background:#fff}
.example{border:0.75pt solid var(--line);margin:8pt 0 12pt;padding:0 10pt 6pt;break-inside:avoid}
.exlab{margin:0 -10pt 7pt;padding:3pt 10pt;background:var(--head);font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--navy)}
.example.key{border-color:var(--navy);border-width:1.2pt} .example.key .exlab{background:var(--navy);color:#fff}
.callout{display:flex;border:0.75pt solid var(--line);margin:9pt 0 12pt;break-inside:avoid}
.callout .lab{flex:none;width:68pt;padding:6pt 8pt;color:#fff;font-weight:700;font-size:8pt;letter-spacing:.1em}
.callout > div:last-child{padding:6pt 10pt}
.callout.note{border-color:var(--blue)} .callout.note .lab{background:var(--blue)}
.callout.caution{border-color:var(--amber)} .callout.caution .lab{background:var(--amber)}
.tag{display:inline-block;color:#fff;font-weight:700;font-size:7.5pt;letter-spacing:.1em;padding:1pt 6pt}
.tag.note{background:var(--blue)} .tag.caution{background:var(--amber)} .ok{color:var(--green);font-weight:700}
table{border-collapse:collapse}
.grid-table{width:100%;margin:6pt 0 12pt;font-size:9pt;break-inside:avoid} .grid-table.narrow{width:auto;min-width:2.4in}
.grid-table caption{caption-side:top;text-align:left;font-weight:700;font-size:8.5pt;color:var(--navy);padding-bottom:4pt}
.grid-table th,.grid-table td{border:0.75pt solid var(--line);padding:4pt 7pt;text-align:left;vertical-align:middle}
.grid-table thead th{background:var(--head);color:var(--navy);font-weight:600} .grid-table tbody th{background:#F7F9FC;font-weight:600}
td.b0{background:var(--blueT);color:var(--blue);font-weight:700} td.b1{background:var(--orangeT);color:var(--orange);font-weight:700}
td.neg{color:#B42318;font-weight:700} .gloss th{width:32%}
.procedure{margin:8pt 0 12pt;break-inside:avoid}
.ptitle{background:var(--navy);color:#fff;font-weight:700;font-size:9pt;padding:4pt 8pt}
.steps{width:100%;font-size:9pt} .steps th,.steps td{border:0.75pt solid var(--line);padding:4pt 7pt;vertical-align:middle;text-align:left}
.steps thead th{background:var(--head);color:var(--navy);font-weight:600}
.steps td:first-child{width:7%;text-align:center;font-weight:700;color:var(--navy)} .steps td:nth-child(2){width:50%}
figure{margin:10pt 0 12pt;break-inside:avoid;text-align:center} figure svg{max-width:100%;height:auto}
figcaption{font-size:8.5pt;color:var(--muted);margin-top:6pt;text-align:left}
.toc2,.toc3{display:flex;align-items:baseline;gap:4pt}
.toc2{font-weight:700;color:var(--navy);margin-top:6pt;font-size:9.6pt} .toc3{padding-left:18pt;font-size:9pt}
.dots{flex:1;border-bottom:0.75pt dotted #94A3B8;transform:translateY(-3pt)} .tp{min-width:16pt;text-align:right}
.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:10pt} .qcell{border:1pt solid var(--navy);padding:0 10pt 8pt;break-inside:avoid}
.qcell.wide{grid-column:1 / -1}
.qh{margin:0 -10pt 6pt;background:var(--navy);color:#fff;font-weight:700;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;padding:3pt 10pt}
.endmark{text-align:center;color:var(--muted);margin-top:24pt;font-size:8.5pt;letter-spacing:.08em}
```

### HTML building blocks

```html
<section class="chapter"><h2 data-toc="4.0">4.0  Title</h2>
<h3 data-toc="4.1">4.1  Section</h3>
<p class="lead-ex"><b>Explanation.</b> ...</p>
<div class="formula">$$ ... $$</div>
<div class="example"><div class="exlab">Example 4-1</div> ... </div>
<div class="example key"><div class="exlab">Example 4-2  &middot;  Running example: NAME</div> ... </div>
<div class="callout note"><div class="lab">NOTE</div><div>...</div></div>
<div class="callout caution"><div class="lab">CAUTION</div><div>...</div></div>
<div class="procedure"><div class="ptitle">Procedure 4-1. Verb phrase</div>
<table class="steps"><thead><tr><th>Step</th><th>Action</th><th>Result</th></tr></thead><tbody>...</tbody></table></div>
<table class="grid-table"><caption>Table 4-1. ...</caption>...</table>
<figure>{{FIG_NAME}}<figcaption>Figure 4-1. ...</figcaption></figure>
</section>
```

---

## 7. Build pipeline

1. **Workspace:**
   - `npm i katex@0.16.11 playwright-core@1.56.1`. pdf-lib is usually at `/opt/npm-tools/node_modules/pdf-lib`; otherwise run `npm i pdf-lib`.
   - Chromium is at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
   - Fonts: Inter and Inter Display are installed locally.
2. **Source:** `src.html` holds the cover section, the front matter with `{{TOC}}`, the chapters, and figure placeholders `{{FIG_X}}`. Mathematics goes inline as `$...$` and in display as `$$...$$`. Never use a literal `$` in prose.
3. **build.js:**
   - Replace figure placeholders with SVG strings generated in JavaScript.
   - Render the mathematics server-side: `katex.renderToString(tex, {displayMode, throwOnError:true})`, display first, then inline.
   - Wrap the result in an HTML page that links the local `katex.min.css` through `file://`, with the stylesheet inlined.
   - Split out the cover. Print it with `page.pdf({format:'Letter', printBackground:true, preferCSSPageSize:true, displayHeaderFooter:false})`.
   - Print the body with `displayHeaderFooter:true` and the header and footer templates. Use inline styles, 7.5pt Inter, and the `pageNumber` / `totalPages` classes.
   - **Two-pass TOC.** Pass 1 renders the TOC with "00" placeholders. Then run `pdftotext` per page, normalize the text (remove whitespace, lowercase) and find the *last* page that contains each heading. Match on the heading number plus the title text before any `$`. Pass 2 renders the real numbers.
   - Merge the cover and body with pdf-lib, then set the title, subject and author.
4. **Gotchas:**
   - Use `&#8209;` (non-breaking hyphen) in cover titles that contain hyphens.
   - Give headings `break-after: avoid`.
   - Keep `.example`, `.procedure` and tables `break-inside: avoid`.
   - Reduce the font size of very wide display equations, or split them.

---

## 8. QA checklist (all must pass before delivery)

- [ ] Every number re-computed by script, and the printed values match.
- [ ] `grep -c katex-error body.html` returns 0.
- [ ] No TOC entry shows `?` or `00`.
- [ ] A cross-reference scan finds no dangling Section, Example, Table, Procedure or Figure numbers, and no forward references in the teaching chapters.
- [ ] Contact sheets of all pages reviewed: no clipped labels, no orphan headings, no empty half pages caused by a heading at a page foot.
- [ ] Figures zoomed and checked for clipping and for scale.
- [ ] Every formula has an Explanation before it and an Example after it.
- [ ] File named `[Title_Words]_[DOC-NO][_RevX].pdf`, sent with SendUserFile.