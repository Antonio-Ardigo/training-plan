---
description: "Concept map generation for training plan topics. Use when the user asks to map concepts, visualize concept relationships, see how topics connect, generate a concept map for a training plan argument, create a knowledge map, show dependencies between concepts, or map all concepts in a domain with links to the training plan's main concepts."
---

# Concept Map -- Domain Knowledge

Reference knowledge for generating concept maps that visualize how all concepts within a given argument relate to each other and to the training plan's main concepts (Core Principles and Key Concepts).

## What This Skill Does

Takes an argument (a topic, domain, sub-goal, or free-form subject) and produces a structured concept map that:

1. **Maps all concepts** within the argument -- principles, innovations, applications, prerequisites
2. **Cross-references the training plan** -- every node that corresponds to a training plan Core Principle or Key Concept is annotated with its SG number
3. **Shows relationships** between concepts using the standard relationship vocabulary
4. **Highlights coverage gaps** -- concepts in the map that are NOT covered by any sub-goal in the training plan

---

## Inputs

The skill requires two things:

1. **Argument**: the topic or domain to map (provided by the user)
2. **Training plan context**: the active training plan file in the current directory (read automatically)

If no training plan file is found, produce the concept map standalone (without SG annotations) and note that no plan was found.

---

## Step-by-Step Process

### Step 1: Read the Training Plan

1. Use Glob to find `training-plan-*.md` files in the current directory
2. Read the plan to extract:
   - **Core Principles** table (principle name, statement)
   - **Sub-Goals** table (SG number, axis, sub-goal statement, principle mapping)
   - **Prerequisite Graph**
3. Build an index: `{concept_name -> SG-N}` for every Core Principle and Key Concept sub-goal

### Step 2: Analyze the Argument

Decompose the argument into its constituent concepts:

1. Identify the **core concept** (the argument itself or its central idea)
2. Extract **principles** -- foundational truths the argument rests on
3. Extract **innovations** -- key breakthroughs or contributions within the argument
4. Extract **applications** -- practical uses or derived outcomes
5. Extract **prerequisites** -- what must be known before understanding the argument
6. Identify **cross-links** -- how concepts within the argument relate to each other

### Step 3: Cross-Reference with Training Plan

For each concept extracted in Step 2:

1. Check if it matches (exact or semantic) a Core Principle or Key Concept in the plan
2. If matched, annotate the node with `[SG-N]`
3. If NOT matched, mark as `(unmapped)` -- this concept exists in the domain but is not covered by the plan

### Step 4: Build the Concept Map

Use the standard concept map format (see Format section below) with these additions:

- **SG annotations** on mapped nodes: `**[Concept Name]** (principle) [SG-3]: description`
- **Unmapped markers** on uncovered nodes: `**[Concept Name]** (principle) [unmapped]: description`
- **Plan coverage summary** after the map

### Step 5: Generate Coverage Analysis

After the map, produce:

```markdown
## Plan Coverage Analysis

**Mapped concepts**: N of M total concepts are covered by sub-goals
**Unmapped concepts**: list of concepts not in the training plan
**Suggestion**: whether unmapped concepts warrant new sub-goals or are acceptable gaps
```

---

## Concept Map Format

Maps are markdown nested lists. Each node has a **bold name**, a type in parentheses, an optional SG annotation in brackets, and a one-line description after a colon.

### Node Types

| Type | Meaning | Usage |
|------|---------|-------|
| **(core)** | Central concept being mapped | Exactly one per map |
| **(principle)** | Foundational truth or constraint | The 3-5 load-bearing ideas |
| **(innovation)** | Conceptual breakthrough or key contribution | Creative leaps that built the concept |
| **(application)** | Practical use or derived concept | Where theory meets reality |
| **(prerequisite)** | Required prior knowledge | What you need before this concept |

### Relationship Labels

| Label | Meaning | Direction |
|-------|---------|-----------|
| `rests on` | Built on these principles | core -> principle |
| `requires` | Needs these prerequisites | core -> prerequisite |
| `led to` | Produced these innovations | principle -> innovation |
| `enables` | Enables these applications | innovation -> application |
| `generalizes` | Generalization of the child | parent -> child |
| `is a special case of` | Specialization | child -> parent |
| `contrasts with` | In tension or opposition | sibling <-> sibling |
| `equivalent to` | Different formulations of same idea | sibling <-> sibling |

### Structure Rules

1. Start from the core concept (the argument) at the top level
2. Group children by relationship type: `requires` first, then `rests on`, then `enables`
3. Nest innovations under their parent principle using `led to`
4. Add applications showing practical impact
5. Add prerequisites for context
6. Keep descriptions to one line
7. Annotate every node that maps to a training plan sub-goal with `[SG-N]`
8. Mark nodes not covered by the plan with `[unmapped]`

### Example (with Training Plan Cross-Reference)

```markdown
## Concept Map: Cost Estimation Methods

- **Cost Estimation Methods** (core): Techniques for predicting project costs at various accuracy levels
  - requires:
    - **Work Breakdown Structure** (prerequisite) [SG-2]: Hierarchical decomposition of project scope into deliverables
    - **Basic Accounting** (prerequisite) [unmapped]: Understanding of cost categories and financial statements
  - rests on:
    - **Cost traceability** (principle) [SG-3]: Every cost is either direct (traceable to scope) or indirect (project-wide)
      - led to:
        - **Unit-rate estimation** (innovation) [SG-6]: Quantity x unit rate = direct cost for each line item
          - enables:
            - **Definitive estimates** (application) [SG-9]: AACE Class 1-2 estimates with -5%/+10% accuracy
        - **Factored estimation** (innovation) [SG-7]: Scale from known costs using capacity or complexity factors
          - enables:
            - **Screening estimates** (application) [unmapped]: Quick order-of-magnitude for early feasibility
    - **Accuracy improves with definition** (principle) [SG-4]: Estimate accuracy is a function of project definition level
      - led to:
        - **AACE classification system** (innovation) [SG-8]: 5-class system mapping definition % to accuracy range
  - enables:
    - **Bid evaluation** (application) [unmapped]: Comparing contractor bids against independent estimates
    - **Budget authorization** (application) [SG-10]: Securing funding based on estimate confidence level

## Plan Coverage Analysis

**Mapped concepts**: 8 of 11 total concepts are covered by sub-goals
**Unmapped concepts**: Basic Accounting (prerequisite), Screening estimates (application), Bid evaluation (application)
**Suggestion**: Basic Accounting is a prerequisite gap -- verify learner has this knowledge. Screening estimates and Bid evaluation are applications outside the plan's scope -- acceptable gaps unless the learner's role requires them.
```

---

## Depth Scaling

| Depth | Total Nodes | Levels | When to Use |
|-------|------------|--------|-------------|
| shallow | 5-8 | 2 | Quick overview, single sub-goal scope |
| standard | 10-15 | 3 | Default -- one topic or related group of sub-goals |
| deep | 15-25 | 4 | Full training plan scope, complex multi-principle topic |

Default: **standard** (10-15 nodes).

If the argument spans the entire training plan, use **deep** depth automatically.

---

## Whole-Plan Map Mode

When the argument is the training plan itself (e.g., "map the whole plan", "show all concepts"), produce a map that:

1. Uses the plan's main goal as the **(core)** node
2. Places every Core Principle as first-level **(principle)** nodes with `[SG-N]`
3. Nests every Key Concept under its parent Core Principle with `[SG-N]`
4. Shows the prerequisite graph from the plan as **(prerequisite)** nodes
5. Adds Verification sub-goals as **(application)** nodes
6. Uses **deep** depth (15-25 nodes)

This gives a complete structural overview of the training plan's concept architecture.

---

## Integration with Other Skills

- **concept-explainer**: If the user wants a full explanation of a node in the map, invoke concept-explainer for that node
- **goal-decomposer**: The prerequisite graph from goal-decomposer feeds into this skill's cross-reference
- **ttt-session**: Concept maps generated during sessions (Phase 3.5) use the same format but are scoped to the session's teaching content
- **concept-library**: Concept files exported from sessions can be referenced to enrich the map with previously taught content
