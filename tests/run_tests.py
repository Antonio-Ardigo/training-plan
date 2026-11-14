#!/usr/bin/env python3
"""Repository checks for the training-plan plugin. Python 3.8+, standard library only.

  python3 tests/run_tests.py

1. The example course is valid.
2. Each 3.x fixture plan converts into a valid course, with the expected shape.
3. next-lesson and progress work on the converted courses.
4. The generated overview never contains tests, marking guides or worked solutions.
5. Lint: every skill and agent has a unique name; no prompt file outside the
   allowed places uses the storage or vocabulary that version 4 removed; every
   skill a prompt names exists.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(ROOT, "skills", "course-model", "tools", "course.py")
FIX = os.path.join(ROOT, "tests", "fixtures", "plans-3x")
failures = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        failures.append(msg)


def run(*args):
    p = subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


# 1. example course
code, out = run("validate", os.path.join(ROOT, "skills", "course-model", "example-course.json"))
check(code == 0 and "0 warnings" in out, "example-course.json is valid with no warnings")

# 2-4. conversion of the fixtures
EXPECT = {
    "transformer-attention_training_plan.md": {"lessons": 14, "key": ["L4", "L6"], "method": "direct", "level": "masters",
                                               "done": ["L1", "L6"], "files": {"record", "practice"}},
    "dot-product-socratic_training_plan.md": {"lessons": 10, "key": ["L3", "L5"], "method": "socratic", "level": "high-school",
                                              "done": [], "files": set()},
    "compound-interest-present-value_training_plan.md": {"lessons": 14, "key": [], "method": "direct", "level": "high-school",
                                                         "done": [], "files": set()},
}
tmp = tempfile.mkdtemp()
try:
    for name in os.listdir(FIX):
        shutil.copy2(os.path.join(FIX, name), tmp)
    courses = []
    for plan, exp in EXPECT.items():
        code, out = run("convert", os.path.join(tmp, plan))
        check(code == 0, f"{plan}: converts into a valid course")
        path = out.splitlines()[0].strip()
        c = json.load(open(path, encoding="utf-8"))
        courses.append(path)
        L = c["lessons"]
        check(len(L) == exp["lessons"], f"{plan}: {exp['lessons']} lessons (found {len(L)})")
        check([l["id"] for l in L if l["key_idea"]] == exp["key"], f"{plan}: key ideas {exp['key']}")
        check(c["course"]["method"] == exp["method"] and c["course"]["level"] == exp["level"],
              f"{plan}: method {exp['method']}, level {exp['level']}")
        check([l["id"] for l in L if l["state"]["status"] == "done"] == exp["done"], f"{plan}: lessons done {exp['done']}")
        kinds = {f["kind"] for f in c["files"]}
        check(exp["files"] <= kinds, f"{plan}: copied files {sorted(exp['files'])}")
        check(all(l["design"]["success_criteria"] for l in L), f"{plan}: every lesson has success criteria")
        check(all(l["needs"] for l in L if l["kind"] in ("concept", "tool", "capstone")),
              f"{plan}: every concept, tool and capstone lesson has needs")
        check(os.path.exists(os.path.join(tmp, plan)), f"{plan}: the old plan is left in place")
        overview = open(os.path.join(os.path.dirname(path), "overview.md"), encoding="utf-8").read()
        leaks = [l["id"] for l in L if l["design"]["try_first"]["question"][:60] in overview
                 or (l["design"].get("trap") or "#none#")[:60] in overview]
        check(not leaks, f"{plan}: overview shows no test or trap (leaks in {leaks})")
        code, out = run("next-lesson", path)
        check(code == 0 and json.loads(out)["why"] in ("next", "resume", "review", "course-complete"),
              f"{plan}: next-lesson answers")
    code, out = run("progress", tmp)
    rep = json.loads(out)
    check(rep["summary"]["courses"] == 3 and rep["summary"]["lessons_done"] == 2, "progress counts 3 courses and 2 lessons done")
    code, out = run("convert", os.path.join(tmp, "transformer-attention_training_plan.md"))
    check(code == 0, "converting the same plan twice is harmless")
finally:
    shutil.rmtree(tmp)

# 5. lint
PROMPTS = []
for d in ("commands", "agents", "skills"):
    for root, _, files in os.walk(os.path.join(ROOT, d)):
        PROMPTS += [os.path.join(root, f) for f in files if f.endswith(".md")]
names = {}
for p in PROMPTS:
    head = open(p, encoding="utf-8").read(1500)
    m = re.search(r"^name:\s*(\S+)", head, re.M)
    if m and (p.endswith("SKILL.md") or "/agents/" in p):
        names.setdefault(m.group(1), []).append(os.path.relpath(p, ROOT))
check(all(len(v) == 1 for v in names.values()), "skill and agent names are unique")

# Storage and words removed in version 4. Allowed only where old plans are described.
REMOVED = [r"learner_profile\.md", r"_checkpoint_SG", r"_session_SG", r"Artefacts Register", r"_artefact_SG",
           r"\bSG-<N>\b", r"\bCTQ", r"\bblueprint", r"[Hh]ard[- ]core", r"Tempting answer", r"\brung\b",
           r"Initial Test", r"Final Test", r"Guidance Chain", r"Discovery Question", r"concept file", r"exercise book"]
ALLOWED = ("skills/course-model/convert-3x.md", "skills/course-model/glossary.md", "skills/course-model/tools/",
           "skills/technical-training-manual/", "tests/")
offenders = {}
for p in PROMPTS:
    rel = os.path.relpath(p, ROOT)
    if rel.startswith(ALLOWED):
        continue
    text = open(p, encoding="utf-8").read()
    text = re.sub(r"(?s)<!-- older-names -->.*?<!-- /older-names -->", "", text)
    text = re.sub(r"(?ms)^#+ (?:\d+\.\s*)?Older names[^\n]*\n.*?(?=^#|\Z)", "", text)
    text = re.sub(r"(?m)^\*\*Older names[^\n]*(?:\n(?!\n)[^\n]*)*", "", text)
    hits = sorted({pat for pat in REMOVED if re.search(pat, text)})
    if hits:
        offenders[rel] = hits
for rel, hits in sorted(offenders.items()):
    print(f"     {rel}: {', '.join(hits)}")
check(not offenders, "no prompt uses storage or words removed in version 4 (outside 'Older names' notes)")

skills = {d for d in os.listdir(os.path.join(ROOT, "skills")) if os.path.isdir(os.path.join(ROOT, "skills", d))}
missing = set()
for p in PROMPTS:
    for m in re.finditer(r"\b(?:skill|the)\s+`([a-z][a-z-]+)`\s+(?:skill)?", open(p, encoding="utf-8").read()):
        name = m.group(1)
        if name in ("course-model", "course-design", "lesson-flow", "explaining", "progress", "visual-explainer",
                    "technical-training-manual") and name not in skills:
            missing.add((os.path.relpath(p, ROOT), name))
check(not missing, f"every named skill exists {sorted(missing) if missing else ''}")

print(f"\n{'FAILED: ' + str(len(failures)) if failures else 'All checks passed'}")
sys.exit(1 if failures else 0)
