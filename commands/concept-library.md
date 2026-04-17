---
name: concept-library
description: Manage concept files generated during TTT sessions -- list, search, path, link
allowed_tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

You are managing the **concept library** -- a collection of concept files generated during `/run-session` Teach phases.

The user wants to: **$ARGUMENTS**

## Subcommands

If no subcommand is provided, default to `list`.

---

### /concept-library list

Scan the current directory for all `concept-*.md` files. Parse YAML frontmatter from each file and display an organized index.

**Workflow:**
1. Use Glob to find all `concept-*.md` files in the current directory
2. Use Read to parse YAML frontmatter (title, domain, date, type, session, plan, level, tags)
3. Group files by domain
4. Display as tables sorted by domain, then date

**Output Format:**

```markdown
## Concept Library

**[N] concept files found in [directory]**

### [Domain 1]
| File | Type | Title | Session | Plan | Date |
|------|------|-------|---------|------|------|
| [filename](filename) | ttt-session | [title] | SG-3 | [plan file] | [date] |
| [filename](filename) | ttt-session | [title] | SG-5 | [plan file] | [date] |

### [Domain 2]
| File | Type | Title | Session | Plan | Date |
|------|------|-------|---------|------|------|
| ... | ... | ... | ... | ... | ... |
```

If no concept files are found, tell the user: "No concept files found. Concept files are generated automatically when you run `/run-session` and gaps are identified. Run a session to create your first concept file."

---

### /concept-library search <query>

Search across all concept files for keyword matches in titles, tags, and content.

**Workflow:**
1. Use Glob to find all `concept-*.md` files
2. Use Grep to search for the query string across all matching files
3. Return files with matching context (surrounding lines)

**Output Format:**

```markdown
## Search Results for "[query]"

**[N] matches in [M] files**

### [filename1]
- **Title**: [title]
- **Domain**: [domain]
- **Session**: [session]
- **Match**: ...[context around match]...

### [filename2]
- **Title**: [title]
- **Domain**: [domain]
- **Match**: ...[context around match]...
```

---

### /concept-library path <start-concept> <end-concept>

Construct a recommended learning path between two concepts by analyzing concept files, training plans, and prerequisite relationships.

**Workflow:**
1. Use Glob to find all `concept-*.md` and `*_training_plan.md` files
2. Read frontmatter and content from each concept file to extract:
   - Prerequisites (from concept maps: `requires` relationships)
   - Related concepts (from concept maps: `rests on`, `enables` relationships)
   - Session source (from frontmatter: session, plan)
3. Build a dependency graph from these relationships
4. Find the shortest learning path from start to end through the graph
5. For each step, check if a concept file exists or needs to be created

**Output Format:**

```markdown
## Learning Path: [Start] --> [End]

| Step | Concept | Status | Action |
|------|---------|--------|--------|
| 1 | [concept] | Exists | Read [filename](filename) |
| 2 | [concept] | Missing | Run `/run-session` for related sub-goal, or `/explain [concept]` |
| 3 | [concept] | Exists | Read [filename](filename) |
| ... | ... | ... | ... |
| N | [end concept] | [status] | [action] |

### Gap Analysis
[N] of [M] concepts in this path already have files. [Suggestions to fill gaps]
```

If no connected path exists between two concepts, suggest an approximate path based on domain similarity and training plan structure.

---

### /concept-library link <file1.md> <file2.md>

Manually declare a relationship between two concept files. Adds a `related` entry to the YAML frontmatter of both files.

**Workflow:**
1. Verify both files exist
2. Read both files
3. Add or update `related` field in YAML frontmatter of each file:
   - In file1: add file2 to `related` list
   - In file2: add file1 to `related` list
4. Save both files using Edit

**Output:**
```
Linked [file1] <--> [file2]

[file1] now lists: [file2] as related
[file2] now lists: [file1] as related
```

---

## Notes

- The concept library operates on the current working directory only
- All operations are non-destructive: `/concept-library link` only adds metadata, never removes content
- Concept files with `type: ttt-session` were generated during `/run-session` Teach phases
- If concept-builder plugin is also installed, its `/library` command can index the same files (shared format)
- Learning path accuracy improves as more concept files are generated across sessions
