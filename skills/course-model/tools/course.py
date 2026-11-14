#!/usr/bin/env python3
"""Helper for course.json, the single source of truth of a training-plan course.

Python 3.8+, standard library only. Every command is also described in words in
../SKILL.md, so the plugin works without Python; this tool makes the work exact.

  course.py validate PATH/course.json [--files]   check schema and course rules
  course.py render-overview PATH/course.json      write overview.md beside it
  course.py next-lesson PATH/course.json          the lesson to do next, as JSON
  course.py progress [DIR ...]                    report over every course found
  course.py convert PLAN.md [--out DIR]           convert a 3.x plan, keep the old files
  course.py example                               print example-course.json (the shape to copy)
  course.py schema                                print course.schema.json
"""
import datetime as _dt
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "..", "course.schema.json")

LEVELS = ["high-school", "masters", "advanced"]
LEVEL_NAMES = {"high-school": "High school", "masters": "Master's", "advanced": "Advanced",
               "below-high-school": "below High school"}
KIND_NAMES = {"why": "Why it matters", "principle": "Principle", "concept": "Concept",
              "tool": "Tool", "capstone": "Capstone", "background": "Background"}
STATUS_NAMES = {"not-started": "Not started", "in-progress": "In progress", "done": "Done", "review": "Review"}
MISTAKE_NAMES = {"mixing-up": "mixing up two ideas", "overstretching": "stretching a rule too far",
                 "missing-background": "missing background", "steps-without-why": "steps without the why",
                 "words-without-maths": "words without the maths", "maths-without-picture": "maths without the picture"}


def today():
    return _dt.date.today().isoformat()


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, path)


# ---------------------------------------------------------------- schema check
def _type_ok(value, t):
    if isinstance(t, list):
        return any(_type_ok(value, x) for x in t)
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }[t]


def check_schema(value, schema, root, where, errors):
    if "$ref" in schema:
        node = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            node = node[part]
        return check_schema(value, node, root, where, errors)
    if "oneOf" in schema:
        hits = 0
        for option in schema["oneOf"]:
            trial = []
            check_schema(value, option, root, where, trial)
            hits += not trial
        if hits != 1:
            errors.append(f"{where}: does not match exactly one allowed form")
        return
    if "const" in schema and value != schema["const"]:
        errors.append(f"{where}: must be {schema['const']!r}")
        return
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{where}: {value!r} is not one of {schema['enum']}")
        return
    if "type" in schema and not _type_ok(value, schema["type"]):
        errors.append(f"{where}: expected {schema['type']}, found {type(value).__name__}")
        return
    if isinstance(value, str) and "pattern" in schema and not re.search(schema["pattern"], value):
        errors.append(f"{where}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, int) and "minimum" in schema and value < schema["minimum"]:
        errors.append(f"{where}: below {schema['minimum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{where}: missing '{key}'")
        props = schema.get("properties", {})
        for key, sub in value.items():
            if key in props:
                check_schema(sub, props[key], root, f"{where}.{key}", errors)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{where}: unknown field '{key}'")
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            check_schema(item, schema["items"], root, f"{where}[{i}]", errors)


# ---------------------------------------------------------------- course rules
def check_rules(c, folder=None, check_files=False):
    """Course rules beyond the schema. Returns (errors, warnings)."""
    errors, warnings = [], []
    course = c["course"]
    lessons = c["lessons"]
    ids = [l["id"] for l in lessons]
    pids = [p["id"] for p in c["principles"]]
    for name, seq in (("lesson", ids), ("principle", pids), ("fact", [f["id"] for f in c["facts"]])):
        dup = {x for x in seq if seq.count(x) > 1}
        if dup:
            errors.append(f"duplicate {name} ids: {sorted(dup)}")
    numbers = [l["number"] for l in lessons]
    if numbers != list(range(1, len(lessons) + 1)):
        errors.append("lessons must be numbered 1, 2, 3 ... in order")
    for l in lessons:
        if l["id"] != f"L{l['number']}":
            errors.append(f"{l['id']}: id must be L{l['number']}")
        for n in l["needs"]:
            if n not in ids:
                errors.append(f"{l['id']}: needs unknown lesson {n}")
            if n == l["id"]:
                errors.append(f"{l['id']}: needs itself")
        for p in l["principles"]:
            if p not in pids:
                errors.append(f"{l['id']}: unknown principle {p}")
    # no cycles in needs
    graph = {l["id"]: list(l["needs"]) for l in lessons}
    state = {}

    def visit(node, path):
        if state.get(node) == 1:
            errors.append("lessons need each other in a circle: " + " -> ".join(path + [node]))
            return
        if state.get(node) == 2:
            return
        state[node] = 1
        for nxt in graph.get(node, []):
            visit(nxt, path + [node])
        state[node] = 2

    for node in graph:
        visit(node, [])
    for f in c["facts"]:
        for u in f["used_in"]:
            if u not in ids:
                errors.append(f"{f['id']}: used in unknown lesson {u}")
        if not f["used_in"]:
            warnings.append(f"{f['id']}: not used in any lesson")
    # principles and their lessons
    for p in c["principles"]:
        teaching = [l for l in lessons if l["kind"] == "principle" and p["id"] in l["principles"]]
        if len(teaching) != 1:
            warnings.append(f"{p['id']} ({p['name']}): taught in {len(teaching)} principle lessons, expected 1")
        if p["key_idea"] and not p.get("why_hard"):
            warnings.append(f"{p['id']}: key idea without why_hard")
    # level-dependent and method-dependent design rules
    above = LEVELS[1:LEVELS.index(course["level"]) + 1]
    for l in lessons:
        d = l["design"]
        tag = f"{l['id']} ({l['title']})"
        if not d.get("context"):
            warnings.append(f"{tag}: no context (why it matters, historical context); the lesson writes one when it opens")
        if l["kind"] == "principle" and not d.get("worked_example"):
            errors.append(f"{tag}: a principle lesson needs a worked example")
        we = d.get("worked_example")
        if we and not we.get("markdown") and not we.get("check"):
            warnings.append(f"{tag}: worked example has no Check")
        if l["key_idea"]:
            for field in ("trap", "aha", "picture", "worked_example"):
                if not d.get(field):
                    errors.append(f"{tag}: a key idea needs '{field}'")
            got = [x["level"] for x in d.get("levels", [])]
            if got != above:
                errors.append(f"{tag}: levels must be {above or 'empty'} for a {course['level']} course, found {got}")
            if not d.get("visual"):
                warnings.append(f"{tag}: key idea without a visual design")
        else:
            for field in ("trap", "aha", "picture"):
                if d.get(field):
                    errors.append(f"{tag}: '{field}' is only for key ideas")
        if course["method"] == "socratic":
            if not d.get("puzzle"):
                errors.append(f"{tag}: a Socratic course needs a puzzle in every lesson")
            if not 3 <= len(d.get("guiding_questions", [])) <= 6:
                errors.append(f"{tag}: a Socratic lesson needs 3 to 6 guiding questions")
        if not d["success_criteria"]:
            errors.append(f"{tag}: no success criteria")
        s = l["state"]
        if s["status"] in ("done", "review") and not s.get("finished"):
            warnings.append(f"{tag}: {s['status']} without a finished date")
        if s["status"] == "in-progress" and not s.get("step"):
            warnings.append(f"{tag}: in progress without a saved step")
        if s["status"] == "done" and l["key_idea"] and not s.get("level_reached"):
            warnings.append(f"{tag}: key idea done without level_reached")
    key_lessons = [l for l in lessons if l["key_idea"]]
    key_principles = {p["id"] for p in c["principles"] if p["key_idea"]}
    for l in key_lessons:
        if not set(l["principles"]) & key_principles:
            errors.append(f"{l['id']}: key-idea lesson does not teach a key-idea principle")
    # files
    paths = [f["path"] for f in c["files"]]
    dup = {p for p in paths if paths.count(p) > 1}
    if dup:
        errors.append(f"files listed twice: {sorted(dup)}")
    for f in c["files"]:
        if f.get("lesson") and f["lesson"] not in ids:
            errors.append(f"file {f['path']}: unknown lesson {f['lesson']}")
        if check_files and folder and not os.path.exists(os.path.join(folder, f["path"])):
            errors.append(f"file {f['path']}: listed but missing")
    return errors, warnings


def validate(path, check_files=False):
    schema = load(SCHEMA_PATH)
    try:
        c = load(path)
    except (OSError, json.JSONDecodeError) as e:
        return [f"cannot read {path}: {e}"], []
    errors = []
    check_schema(c, schema, schema, "course.json", errors)
    if errors:
        return errors, []
    e2, warnings = check_rules(c, os.path.dirname(os.path.abspath(path)), check_files)
    return errors + e2, warnings


# ---------------------------------------------------------------- derived views
def lesson_folder(lesson):
    slug = re.sub(r"[^a-z0-9]+", "-", lesson["title"].lower()).strip("-")[:40].strip("-") or "lesson"
    return f"lessons/{lesson['number']:02d}-{slug}"


def next_lesson(c):
    lessons = c["lessons"]
    done = {l["id"] for l in lessons if l["state"]["status"] == "done"}
    for l in lessons:
        if l["state"]["status"] == "in-progress":
            return {"lesson": l["id"], "number": l["number"], "title": l["title"], "why": "resume",
                    "step": l["state"].get("step")}
    for l in lessons:
        if l["state"]["status"] == "not-started" and set(l["needs"]) <= done:
            return {"lesson": l["id"], "number": l["number"], "title": l["title"], "why": "next"}
    for l in lessons:
        if l["state"]["status"] == "review":
            return {"lesson": l["id"], "number": l["number"], "title": l["title"], "why": "review"}
    for l in lessons:
        if l["state"]["status"] == "not-started":
            missing = [n for n in l["needs"] if n not in done]
            return {"lesson": l["id"], "number": l["number"], "title": l["title"], "why": "needs-not-done",
                    "missing": missing}
    return {"lesson": None, "why": "course-complete"}


def render_overview(c):
    """The learner's readable outline. Never contains tests, marking guides or solutions."""
    co, ov, st = c["course"], c["overview"], c["story"]
    pname = {p["id"]: p["name"] for p in c["principles"]}
    out = [f"# {co['title']}", "",
           f"**Goal:** {co['goal']}  ",
           f"**Level:** {LEVEL_NAMES[co['level']]} · **Method:** "
           + ("Socratic (you reach each idea through questions)" if co["method"] == "socratic"
              else "Direct (try first, then the gaps are explained)")
           + f" · **Lessons:** {'in the course app' if co['delivery'] == 'app' else 'in chat'}", ""]
    if co.get("app_url"):
        out += [f"**Course app:** {co['app_url']}", ""]
    out += ["> Generated from `course.json`. Edit the course through Claude, not this file.", "",
            "## Course overview", "", f"**Why it matters.** {ov['why_it_matters']}", "",
            f"**What you will learn.** {ov['what_you_will_learn']}", ""]
    if ov.get("principles_and_facts"):
        out += [ov["principles_and_facts"], ""]
    out += ["**You will be able to:**"] + [f"- {x}" for x in ov["you_will_be_able_to"]] + [""]
    if ov.get("learner_notes"):
        out += [f"**Your notes:** {ov['learner_notes']}", ""]
    out += ["## The story", "", f"**Before.** {st['before']}", "", f"**The aha.** {st['the_aha']}", "",
            f"**What it solved.** {st['what_it_solved']}", ""]
    out += ["## Principles", "", "| | Principle | Statement |", "|---|---|---|"]
    for p in c["principles"]:
        out.append(f"| {'★' if p['key_idea'] else ''} | {p['name']} | {_cell(p['statement'])} |")
    out.append("")
    keys = [p for p in c["principles"] if p["key_idea"]]
    if keys:
        out += ["★ **Key ideas** are the hardest principles. Each one is taught through the aha moment and then level by level."]
        out += [f"- **{p['name']}**: {p.get('why_hard') or ''}" for p in keys] + [""]
    if c["facts"]:
        out += ["## Facts to know", "", "| | Fact | Used in |", "|---|---|---|"]
        for f in c["facts"]:
            used = ", ".join(u.replace("L", "Lesson ") for u in f["used_in"])
            out.append(f"| {f['id']} | {_cell(f['fact'])}{' *(check this value)*' if f.get('verify') else ''} | {used} |")
        out.append("")
    if c["background"]:
        out += ["## Background you need", ""]
        for b in c["background"]:
            extra = f" (taught in Lesson {b['lesson'][1:]})" if b.get("lesson") else ""
            out.append(f"- {b['name']}{extra}{': ' + b['note'] if b.get('note') else ''}")
        out.append("")
    nxt = next_lesson(c)
    done = sum(1 for l in c["lessons"] if l["state"]["status"] == "done")
    out += ["## Lessons", "", f"{done} of {len(c['lessons'])} done."
            + (f" Next: **Lesson {nxt['number']}, {nxt['title']}**." if nxt.get("lesson") else " Course complete."), "",
            "| # | | Lesson | Kind | Needs | Status |", "|---|---|---|---|---|---|"]
    for l in c["lessons"]:
        needs = ", ".join(n[1:] for n in l["needs"]) or "—"
        status = STATUS_NAMES[l["state"]["status"]]
        lr = l["state"].get("level_reached")
        if lr and l["state"]["status"] in ("done", "review"):
            status += f" ({LEVEL_NAMES[lr]})"
        out.append(f"| {l['number']} | {'★' if l['key_idea'] else ''} | **{l['title']}**: {_cell(l['goal'])} "
                   f"| {KIND_NAMES[l['kind']]} | {needs} | {status} |")
    out.append("")
    if c["files"]:
        out += ["## Files", "", "| File | What it is | Lesson |", "|---|---|---|"]
        for f in c["files"]:
            out.append(f"| [{f['path']}]({f['path']}) | {f['title']} | {f['lesson'][1:] if f.get('lesson') else '—'} |")
        out.append("")
    return "\n".join(out)


def _cell(text):
    return (text or "").replace("\n", " ").replace("|", "\\|")


def progress(dirs):
    found = []
    for d in dirs or ["."]:
        for root, subdirs, files in os.walk(d):
            if root[len(d):].count(os.sep) > 3:
                subdirs[:] = []
                continue
            subdirs[:] = [s for s in subdirs if not s.startswith(".") and s != "node_modules"]
            if "course.json" in files:
                found.append(os.path.join(root, "course.json"))
    courses, mistakes, strong = [], {}, []
    for path in sorted(found):
        try:
            c = load(path)
        except (OSError, json.JSONDecodeError):
            continue
        ls = c.get("lessons", [])
        done = [l for l in ls if l["state"]["status"] == "done"]
        dates = [h["at"] for h in c.get("history", [])] + [l["state"].get("finished") or "" for l in ls]
        courses.append({
            "path": path, "title": c["course"]["title"], "level": LEVEL_NAMES[c["course"]["level"]],
            "done": len(done), "total": len(ls),
            "review": sum(1 for l in ls if l["state"]["status"] == "review"),
            "key_ideas_done": sum(1 for l in done if l["key_idea"]),
            "key_ideas": sum(1 for l in ls if l["key_idea"]),
            "last_activity": max([x for x in dates if x] or [""]), "next": next_lesson(c),
        })
        for l in ls:
            for w in l["state"].get("to_work_on", []):
                if w.get("kind"):
                    mistakes.setdefault(w["kind"], []).append(f"{c['course']['title']}, Lesson {l['number']}")
            tries = [a for a in l["state"]["attempts"] if a["step"] == "try-first"]
            if l["state"]["status"] == "done" and tries and tries[0]["verdict"] == "pass":
                strong.append(f"{c['course']['title']}: Lesson {l['number']}, {l['title']}")
    return {"courses": courses, "recurring_mistakes": {MISTAKE_NAMES[k]: v for k, v in mistakes.items() if len(v) >= 2},
            "all_mistakes": {MISTAKE_NAMES[k]: v for k, v in mistakes.items()}, "passed_first_time": strong}


# ---------------------------------------------------------------- 3.x conversion
FIELD_RE = re.compile(r"^- \*\*([^*]+?):\*\*\s*(.*)$")


def split_row(line):
    """Split a Markdown table row, ignoring pipes inside $math$ or `code`."""
    cells, cur, in_math, in_code, i = [], "", False, False, 0
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line):
            cur += line[i:i + 2]
            i += 2
            continue
        if ch == "$" and not in_code:
            in_math = not in_math
        elif ch == "`" and not in_math:
            in_code = not in_code
        if ch == "|" and not in_math and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def table_rows(text):
    rows = [split_row(l) for l in text.splitlines() if l.strip().startswith("|")]
    rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", x or "--") for x in r)]
    return rows[1:] if rows else []


def sections(text, level=2):
    marker = "#" * level + " "
    out, name, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith(marker):
            if name is not None:
                out[name] = "\n".join(buf).strip("\n")
            name, buf = line[len(marker):].strip(), []
        elif name is not None:
            buf.append(line)
    if name is not None:
        out[name] = "\n".join(buf).strip("\n")
    return out


def find_section(secs, *starts):
    for k, v in secs.items():
        if any(k.lower().startswith(s.lower()) for s in starts):
            return k, v
    return None, ""


def bold_part(text, label):
    """Text after **label:** up to the next bold label at line start or a blank line before one."""
    m = re.search(r"\*\*" + re.escape(label) + r"[^*]*\*\*\s*(.*?)(?=\n\s*\*\*[A-Z][^*]{2,60}:\*\*|\n\|\s|\Z)", text, re.S)
    return m.group(1).strip() if m else ""


def blueprint_fields(body):
    """Top-level '- **Field:** value' entries, each with its indented continuation."""
    fields, name, buf = {}, None, []
    for line in body.splitlines():
        m = FIELD_RE.match(line)
        if m:
            if name:
                fields[name] = "\n".join(buf).strip()
            name, buf = m.group(1).strip(), [m.group(2)]
        elif name:
            buf.append(line[2:] if line.startswith("  ") else line)
    if name:
        fields[name] = "\n".join(buf).strip()
    return fields


def parse_example(text, title=None):
    if not text:
        return None
    ex = {}
    if title:
        ex["title"] = title
    parts = re.split(r"(?m)^\s*(?:>\s*)?\*\*(Given|Step \d+|Why|Result|Check):\*\*\s*", text)
    if len(parts) < 3:
        return {"markdown": text.strip()}
    steps = []
    for i in range(1, len(parts) - 1, 2):
        label, value = parts[i], parts[i + 1].strip()
        value = re.sub(r"\n\s*>\s*$", "", value).strip()
        if label == "Given":
            ex["given"] = value
        elif label.startswith("Step"):
            steps.append({"do": value})
        elif label == "Why":
            if steps:
                steps[-1]["why"] = value
        elif label == "Result":
            ex["result"] = value
        elif label == "Check":
            ex["check"] = value
    ex["steps"] = steps
    return ex


def parse_levels(text):
    if not text or text.strip().lower().startswith("none"):
        return []
    out = []
    chunks = re.split(r"(?m)^\s*\*\*(Master's|Masters|Advanced)[^*\n]*\*\*[^\n]*$", text)
    for i in range(1, len(chunks) - 1, 2):
        level = "advanced" if chunks[i].lower().startswith("adv") else "masters"
        ex = parse_example(chunks[i + 1].strip())
        if ex:
            out.append({"level": level, "example": ex})
    return out


MISTAKE_MAP = [("conflation", "mixing-up"), ("overgeneral", "overstretching"), ("missing", "missing-background"),
               ("procedural", "steps-without-why"), ("verbal", "words-without-maths"), ("formal", "maths-without-picture")]


def mistake_kind(text):
    t = (text or "").lower()
    for key, kind in MISTAKE_MAP:
        if t.startswith(key) or t.startswith("[" + key):
            return kind
    for key, kind in MISTAKE_MAP:
        if key in t[:40]:
            return kind
    return None


def level_of(text):
    t = (text or "").lower()
    if "advanced" in t:
        return "advanced"
    if "master" in t or "intermediate" in t or "msc" in t:
        return "masters"
    if "high school" in t or "introductory" in t or t.strip() == "hs":
        return "high-school"
    return None


def parse_visual(text):
    if not text:
        return None
    keys = {"objects": "objects", "colour roles": "colour_roles", "color roles": "colour_roles", "steps": "steps",
            "your-turn": "your_turn", "your turn": "your_turn", "control": "control"}
    out = {}
    for m in re.finditer(r"(?m)^\s*-\s*\*\*([^*]+?)\*\*\s*:?\s*(.*?)(?=^\s*-\s*\*\*|\Z)", text, re.S):
        label = m.group(1).rstrip(":").strip().lower()
        for k, v in keys.items():
            if label.startswith(k):
                prefix = "" if label.rstrip(":") == k else f"({m.group(1).rstrip(':').strip()[len(k):].strip(' ()')}) "
                out[v] = (out.get(v, "") + "\n" + prefix + m.group(2).strip()).strip()
                break
    return out or {"objects": text.strip()}


def convert(plan_path, out_dir=None):
    text = open(plan_path, encoding="utf-8").read()
    plan_dir = os.path.dirname(os.path.abspath(plan_path))
    base = os.path.basename(plan_path)
    stem = re.sub(r"(-socratic)?_training_plan\.md$", "", base)
    topic_prefix = re.sub(r"_training_plan\.md$", "", base)
    socratic = "-socratic_training_plan" in base or "Socratic Discovery" in text
    secs = sections(text)
    title_m = re.search(r"^#\s+(?:Socratic\s+)?Training Plan:\s*(.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else stem.replace("-", " ").title()
    gen_m = re.search(r"Generated:\s*(\d{4}-\d{2}-\d{2})", text)
    created = gen_m.group(1) if gen_m else today()
    lvl_m = re.search(r"Target level:\s*([^|\n]+)", text)
    level = level_of(lvl_m.group(1)) if lvl_m else None

    _, goal_given = find_section(secs, "Learning Goal")
    _, smart = find_section(secs, "SMART Goal")
    _, voc = find_section(secs, "Motivation & Course Overview", "Motivation and Course Overview")
    _, story = find_section(secs, "Breakthrough")
    _, pe = find_section(secs, "Principle Extraction")
    _, hc = find_section(secs, "Hard Core")
    _, kf = find_section(secs, "Key Facts")
    _, sgt = find_section(secs, "Sub-Goals")
    _, graph = find_section(secs, "Prerequisite Graph")
    _, seq = find_section(secs, "Sequence")
    _, bps = find_section(secs, "Session Blueprints")
    _, reg = find_section(secs, "Artefacts Register", "Artifacts Register")
    _, plog = find_section(secs, "Progress Log")

    # principles
    principles = []
    for i, r in enumerate(table_rows(pe), 1):
        if len(r) < 2:
            continue
        needs = [x.strip() for x in re.split(r"[;,]", r[3]) if x.strip() and x.strip() not in ("—", "-")] if len(r) > 3 else []
        principles.append({"id": f"P{i}", "name": r[0].strip("* "), "statement": r[1],
                           "formal": r[2] if len(r) > 2 else "", "needs": needs, "key_idea": False, "why_hard": None})

    def pid_for(name):
        n = name.strip().strip("*").lower()
        for p in principles:
            if p["name"].lower() == n:
                return p["id"]
        for p in principles:
            if p["name"].lower() in n or n in p["name"].lower():
                return p["id"]
        return None

    for r in table_rows(hc):
        if len(r) >= 2:
            pid = pid_for(r[0])
            if pid:
                p = next(p for p in principles if p["id"] == pid)
                p["key_idea"], p["why_hard"] = True, r[1]

    # lessons from the Sub-Goals table and the blueprints
    kinds = {"motivation": "why", "core principle": "principle", "key concept": "concept", "tools": "tool",
             "tool": "tool", "verification": "capstone", "background": "background", "prerequisite": "background"}
    status_map = {"complete": "done", "completed": "done", "needs-review": "review", "needs review": "review",
                  "in-progress": "in-progress", "in progress": "in-progress", "pending": "not-started"}
    table = {}
    for r in table_rows(sgt):
        m = re.match(r"SG-(\d+)", r[0]) if r else None
        if m and len(r) >= 8:
            table[int(m.group(1))] = r
    blueprints = {}
    for m in re.finditer(r"(?ms)^### SG-(\d+):\s*([^\n]+)\n(.*?)(?=^### |\Z)", bps):
        blueprints[int(m.group(1))] = (m.group(2).strip(), blueprint_fields(m.group(3)))
    numbers = sorted(set(table) | set(blueprints))
    renumber = {n: i for i, n in enumerate(numbers, 1)}
    if level is None:
        for n in numbers:
            lv = level_of(blueprints.get(n, ("", {}))[1].get("Estimated Depth", ""))
            if lv:
                level = lv
                break
    level = level or "masters"

    lessons = []
    for n in numbers:
        row = table.get(n, [])
        bp_title, f = blueprints.get(n, ("", {}))
        num = renumber[n]
        kind = kinds.get((row[1] if len(row) > 1 else "").strip().lower(), "concept")
        pcell = row[6] if len(row) > 6 else f.get("Principle", "")
        if pcell.strip().lower().startswith("all"):
            plist = [p["id"] for p in principles]
        else:
            plist = []
            for part in re.split(r",| and ", pcell):
                pid = pid_for(part.split("—")[0]) if part.strip() and part.strip() not in ("—", "-") else None
                if pid and pid not in plist:
                    plist.append(pid)
        key = bool(f.get("Tempting answer") and f.get("Insight") and f.get("Picture"))
        crit = []
        for r in table_rows(f.get("Anticipated CTQs", "")):
            if len(r) >= 3:
                mk = r[3] if len(r) > 3 else ""
                kind_m = mistake_kind(mk)
                text_m = re.sub(r"^\[?[a-z-]+\]?:\s*", "", mk) if kind_m else mk
                crit.append({"what": r[0], "from": r[1], "how_tested": r[2],
                             "common_mistake": {"kind": kind_m, "text": text_m} if mk.strip() else None})
        if not crit:
            crit.append({"what": row[2] if len(row) > 2 else bp_title, "how_tested": "Show you've got it", "from": ""})
        guiding = [re.sub(r"^\d+\.\s*", "", x).strip() for x in
                   f.get("Socratic Guidance Chain (if stuck)", f.get("Socratic Guidance Chain", "")).splitlines()
                   if re.match(r"\s*\d+\.", x)]
        principle_field = f.get("Principle", "")
        statement = principle_field if principle_field and principle_field not in ("—", "-") else None
        design = {
            "context": f.get("Context") or None,
            "principle_statement": statement,
            "puzzle": f.get("Discovery Question") or None,
            "try_first": {"question": f.get("Initial Test", ""),
                          "marking": {"pass": f.get("Pass Criteria", ""), "trap": f.get("Tempting answer") or None}},
            "guiding_questions": guiding,
            "trap": f.get("Tempting answer") or None if key else None,
            "aha": f.get("Insight") or None if key else None,
            "picture": f.get("Picture") or None if key else None,
            "visual": parse_visual(f.get("Visual design")) if key else None,
            "worked_example": parse_example(f.get("Worked Example (foundational)", f.get("Worked Example", ""))),
            "levels": parse_levels(f.get("Level ladder", "")) if key else [],
            "practice_task": f.get("Exercise") or None,
            "success_criteria": crit,
            "to_teach": f.get("Teach Topics", ""),
            "final_check": {"question": f.get("Final Test", ""),
                            "marking": {"pass": "The same standard as Try first, on this new case: "
                                        + (f.get("Pass Criteria", "") or "the lesson's success criteria."),
                                        "trap": None,
                                        "explain_it_back": ("Rebuild the reasoning that leads to the idea, in your own words."
                                                            if socratic else None)}},
        }
        status = status_map.get((row[7] if len(row) > 7 else "pending").strip().lower(), "not-started")
        lessons.append({
            "id": f"L{num}", "number": num, "kind": kind, "title": bp_title or (row[2] if len(row) > 2 else f"Lesson {num}"),
            "goal": row[2] if len(row) > 2 else bp_title, "area": row[3] if len(row) > 3 else "",
            "difficulty": (row[4].strip().lower() if len(row) > 4 and row[4].strip().lower() in ("low", "medium", "high") else "medium"),
            "principles": plist, "needs": [], "key_idea": key, "design": design,
            "state": {"status": status, "step": None, "saved": None, "level_reached": None, "delivery": None,
                      "rounds": 0, "started": None, "finished": None, "to_work_on": [], "attempts": [], "notes": ""}})
    by_old = {n: lessons[renumber[n] - 1] for n in numbers}

    # needs, from the Sequence section (free text in 3.x: "SG-6 needs SG-2 and SG-3", "SG-2 -> SG-3", ...)
    def sg_list(t):
        found = []
        for a, b in re.findall(r"SG-(\d+)\s*(?:to|through|-|–)\s*SG-(\d+)", t):
            found += list(range(int(a), int(b) + 1))
        t = re.sub(r"SG-\d+\s*(?:to|through|-|–)\s*SG-\d+", " ", t)
        return found + [int(x) for x in re.findall(r"SG-(\d+)", t)]

    def add_need(subject, need):
        if subject in by_old and need in by_old and need != subject:
            ref = f"L{renumber[need]}"
            if ref not in by_old[subject]["needs"]:
                by_old[subject]["needs"].append(ref)

    for line in seq.splitlines():
        if re.search(r"(?i)\b(order|start)\s*:", line):
            continue
        for clause in re.split(r";|(?<=\.)\s", line.replace("**", "")):
            chain = re.findall(r"SG-(\d+)\s*(?:→|->)\s*(?=SG-(\d+))", clause)
            for a, b in chain:
                add_need(int(b), int(a))
            m = re.search(r"(?i)\b(needs?|depends? on|depend on|after|requires?|leans? on|draws? on|builds? on)\b", clause)
            if not m:
                continue
            subjects = sg_list(clause[:m.start()])
            for s_ in subjects:
                for nd in sg_list(clause[m.start():]):
                    add_need(s_, nd)
    # fallback: a lesson with no needs found needs the principle lessons of its principles
    plesson = {p: l["id"] for l in lessons if l["kind"] == "principle" for p in l["principles"]}
    for l in lessons:
        if not l["needs"] and l["kind"] in ("concept", "tool", "capstone"):
            l["needs"] = sorted({plesson[p] for p in l["principles"] if p in plesson and plesson[p] != l["id"]},
                                key=lambda x: int(x[1:]))
    # facts
    facts = []
    for i, r in enumerate(table_rows(kf), 1):
        if len(r) < 2:
            continue
        used = [f"L{renumber[int(x)]}" for x in re.findall(r"SG-(\d+)", r[-1]) if int(x) in renumber]
        fact_text = r[1]
        facts.append({"id": f"F{i}", "fact": re.sub(r"\s*\(verify\)", "", fact_text).strip(),
                      "why_it_matters": r[2] if len(r) > 3 else "", "used_in": used, "verify": "(verify)" in fact_text})
    # background, from the Prerequisite Graph 'requires' block
    background = []
    req = re.search(r"requires:\n(.*?)(?=\n\s*rests on:|\n```|\Z)", graph, re.S)
    if req:
        for line in req.group(1).splitlines():
            line = re.sub(r"←.*$", "", line).strip()
            line = re.sub(r"\s*\((?:prerequisite)[^)]*\)\s*$", "", line).strip()
            if line:
                background.append({"name": line, "note": "", "lesson": None})
    # overview and story
    able = [re.sub(r"^[-*]\s*", "", x).strip() for x in
            bold_part(voc, "What you'll be able to do").splitlines() if x.strip().startswith(("-", "*"))]
    overview = {"why_it_matters": bold_part(voc, "Why this matters"),
                "what_you_will_learn": bold_part(voc, "Bird's-eye view") or bold_part(voc, "Bird"),
                "principles_and_facts": bold_part(voc, "Core principles"), "you_will_be_able_to": able}
    by_principle = []
    for r in table_rows(story):
        pid = pid_for(r[0]) if r else None
        if pid and len(r) >= 3:
            by_principle.append({"principle": pid, "before": r[1], "what_it_solved": r[2]})
    story_obj = {"before": bold_part(story, "Before the intuition"), "the_aha": bold_part(story, "The intuition"),
                 "what_it_solved": bold_part(story, "What it solved"), "by_principle": by_principle}

    course_id = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    out_dir = out_dir or os.path.join(plan_dir, course_id)
    os.makedirs(out_dir, exist_ok=True)
    files = [{"path": "overview.md", "kind": "overview", "lesson": None, "title": "Course overview", "updated": today()},
             {"path": os.path.relpath(os.path.abspath(plan_path), out_dir), "kind": "old-plan", "lesson": None,
              "title": "The 3.x plan this course was converted from (kept unchanged)", "updated": created}]
    history = [{"at": created, "event": "Course created (3.x plan)"},
               {"at": today(), "event": f"Converted from {base} to course.json"}]

    # progress log
    for m in re.finditer(r"(?ms)^### SG-(\d+)\s*--\s*([^\n]*)\n(.*?)(?=^### |\Z)", plog):
        n = int(m.group(1))
        if n not in by_old:
            continue
        l, head, body = by_old[n], m.group(2), m.group(3)
        s = l["state"]
        date_m = re.search(r"\d{4}-\d{2}-\d{2}", head)
        s["finished"] = date_m.group(0) if date_m else created
        s["status"] = "review" if "review" in head.lower() else "done"
        lines = {}
        for line in body.splitlines():
            mm = re.match(r"-\s*([^:]+):\s*(.*)", line.strip())
            if mm:
                lines[mm.group(1).strip().lower()] = mm.group(2).strip()

        def verdict(t):
            t = t.lower()
            if "not attempted" in t or "not familiar" in t:
                return "start-from-scratch"
            if "not taken" in t or "waived" in t:
                return "skipped"
            if "tempting" in t or "fell for" in t:
                return "trap"
            for k in ("partial", "pass", "fail"):
                if t.startswith(k):
                    return k
            return "partial"

        if "initial test" in lines:
            s["attempts"].append({"at": s["finished"], "step": "try-first", "verdict": verdict(lines["initial test"]),
                                  "feedback": lines["initial test"], "source": "converted"})
        if "final test" in lines:
            s["attempts"].append({"at": s["finished"], "step": "final-check", "verdict": verdict(lines["final test"]),
                                  "feedback": lines["final test"], "source": "converted"})
        for gap in re.findall(r"\[([a-z-]+)\]\s*([^\[]+)", lines.get("gaps found", "")):
            s["to_work_on"].append({"what": gap[1].strip(" ;,"), "kind": mistake_kind(gap[0]), "resolved": s["status"] == "done"})
        lr = lines.get("level reached", "")
        s["level_reached"] = ("below-high-school" if "below" in lr.lower() else level_of(lr.split("(")[0])) if lr else None
        dl = lines.get("delivery", "").lower()
        s["delivery"] = "app" if dl.startswith("visual") else ("chat" if dl.startswith("chat") else None)
        loops = re.search(r"\d", lines.get("loops", ""))
        s["rounds"] = int(loops.group(0)) if loops else 0
        s["notes"] = "; ".join(v for k, v in lines.items() if k in ("notes", "page checks"))
        history.append({"at": s["finished"], "event": f"Lesson {l['number']} {s['status']} (from the 3.x progress log)"})

    # files the 3.x plan produced: copied, never moved
    def add_file(src, lesson, kind, name, title):
        if not os.path.exists(src):
            return
        rel = f"{lesson_folder(lesson)}/{name}" if lesson else name
        dst = os.path.join(out_dir, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
        if rel not in [f["path"] for f in files]:
            files.append({"path": rel, "kind": kind, "lesson": lesson["id"] if lesson else None, "title": title,
                          "updated": _dt.date.fromtimestamp(os.path.getmtime(src)).isoformat()})

    registered = []
    for r in table_rows(reg):
        if len(r) >= 4:
            registered.append((r[0], r[1].strip().lower(), r[2], r[3].strip("` ")))
    for name in os.listdir(plan_dir):
        if (name.startswith(topic_prefix + "_") or name.startswith(stem + "_")) and name != base \
                and not name.endswith("_training_plan.md") and not any(name == x[3] for x in registered):
            registered.append((name, "", "", name))
    for label, typ, source, path in registered:
        src = os.path.join(plan_dir, path)
        sg = re.search(r"SG-?(\d+)", source + " " + path)
        lesson = by_old.get(int(sg.group(1))) if sg else None
        low = path.lower()
        if typ == "plan" or low == base.lower() or typ == "profile" or "learner_profile" in low:
            continue
        if "_checkpoint_" in low and lesson:
            ck = open(src, encoding="utf-8").read() if os.path.exists(src) else ""
            phase = re.search(r"Current Phase:\s*([^\n]+)", ck)
            step = {"INITIAL_TEST": "try-first", "EVALUATE": "try-first", "TEACH": "learn", "CONCEPT_MAP_OFFER": "learn",
                    "FINAL_TEST": "final-check", "EVALUATE_FINAL": "final-check", "RECORD": "record"}
            token = phase.group(1).strip().split()[0].strip("`*.,;:") if phase else ""
            if lesson["state"]["status"] == "not-started" and phase and token.upper() != "CLOSED":
                lesson["state"].update({"status": "in-progress", "step": step.get(token, "learn"),
                                        "saved": ck[:4000]})
            continue
        if "_session_" in low:
            add_file(src, lesson, "record", "record.md", f"Lesson record: {label}")
        elif low.startswith("concept-") or typ == "concept-file":
            add_file(src, lesson, "notes", "notes.md", f"Lesson notes: {label}")
        elif "exercises" in low:
            add_file(src, lesson, "practice", "practice.md", "Practice book")
        elif low.endswith(".html"):
            add_file(src, lesson, "lesson-page", "page.html", f"Lesson page: {label}")
        else:
            add_file(src, lesson, "other", os.path.basename(path), label)

    course = {
        "schema": "course/1",
        "course": {"id": course_id, "title": title, "goal": (smart or goal_given).strip().splitlines()[0] if (smart or goal_given).strip() else title,
                   "goal_as_given": goal_given.strip() or title, "level": level,
                   "method": "socratic" if socratic else "direct", "delivery": "app", "created": created,
                   "app_url": None, "converted_from": os.path.relpath(os.path.abspath(plan_path), out_dir)},
        "overview": overview, "story": story_obj, "principles": principles, "facts": facts,
        "background": background, "lessons": lessons, "files": files, "history": history,
    }
    path = os.path.join(out_dir, "course.json")
    save(path, course)
    with open(os.path.join(out_dir, "overview.md"), "w", encoding="utf-8") as f:
        f.write(render_overview(course) + "\n")
    return path


# ---------------------------------------------------------------- CLI
def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[1], argv[2:]
    if cmd in ("example", "schema"):
        name = "example-course.json" if cmd == "example" else "course.schema.json"
        with open(os.path.join(HERE, "..", name), encoding="utf-8") as f:
            sys.stdout.write(f.read())
        return 0
    if cmd == "validate":
        errors, warnings = validate(args[0], "--files" in args)
        for w in warnings:
            print("warning:", w)
        for e in errors:
            print("error:", e)
        print(f"{'FAIL' if errors else 'OK'}: {len(errors)} errors, {len(warnings)} warnings")
        return 1 if errors else 0
    if cmd == "render-overview":
        c = load(args[0])
        out = os.path.join(os.path.dirname(os.path.abspath(args[0])), "overview.md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(render_overview(c) + "\n")
        print(out)
        return 0
    if cmd == "next-lesson":
        print(json.dumps(next_lesson(load(args[0])), ensure_ascii=False))
        return 0
    if cmd == "progress":
        print(json.dumps(progress(args), ensure_ascii=False, indent=2))
        return 0
    if cmd == "convert":
        out = args[args.index("--out") + 1] if "--out" in args else None
        path = convert(args[0], out)
        errors, warnings = validate(path, True)
        print(path)
        for w in warnings:
            print("warning:", w)
        for e in errors:
            print("error:", e)
        return 1 if errors else 0
    print(f"unknown command {cmd!r}\n{__doc__}")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
