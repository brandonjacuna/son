#!/usr/bin/env python3
"""Lint a profile master folder (profiles/<cluster>/<slug>/).

Usage: python3 profile_lint.py <master-dir> [<master-dir> ...]
Exit 1 on any error. Warnings never fail the run. Standard library only.
"""
import re
import sys
from pathlib import Path

CORE_TARGET, CORE_CAP = 10 * 1024, 12 * 1024
REF_CAP = 30 * 1024
DESC_WARN = 300
# Seats never run on Fable (model policy: Fable only for strategy, design, orchestration).
MODELS = {"haiku", "sonnet", "opus", "inherit"}
CORE_HEADINGS = ["Scope", "Cues", "Decision rules", "Rejects", "When to distrust my read", "Seams", "Output"]

TEXT_ERRORS = [
    (re.compile("—"), "em dash"),
    (re.compile(r"\bguests?\b", re.I), "'guest'; write 'customer'"),
    (re.compile(r"\b(we believe|we hope|our goal is)\b", re.I), "performed conviction"),
    (re.compile(r"\b(fuck\w*|shit\w*|bullshit)\b", re.I), "profanity is spoken only"),
    (re.compile(r"\b(good energy|dosi|luxx)\b", re.I), "daypart code name"),
    (re.compile(r"\bairtable\b", re.I), "retired tool (Airtable)"),
    (re.compile(r"\[(sourced|inferred|project|assumed)\b", re.I), "inline provenance tag; move it to provenance.md"),
    (re.compile(r"<\s*/?\s*(project_block|interaction_guide|reanchor)\s*>|\breanchor\b", re.I), "shared plumbing; it lives in CLAUDE.md"),
    (re.compile(r"\byou are an? (world[- ]class|expert|seasoned|renowned)\b", re.I), "identity inflation"),
]
TEXT_WARNINGS = [
    (re.compile(r"\b(coqodaq|alinea|gracious)\b", re.I), "lineage name; flag for Brandon, never reconstruct"),
    (re.compile(r"\$\s?\d|\b\d+(\.\d+)?\s?%"), "figure; financial figures come only from the Investor Review workbook"),
]
# A row is defined by "| C1 |", "- R1." or "## E1"; a mention elsewhere is not a definition.
ROW_ID = re.compile(r"^\s*(?:\|\s*([A-Z]{1,2}\d{1,3})\s*\||-\s+([A-Z]{1,2}\d{1,3})\.|#+\s+([A-Z]{1,2}\d{1,3})\b)")


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg):
        self.errors.append(f"ERROR   {where}  {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"warning {where}  {msg}")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields


def scan_text(path, rep, ids):
    in_code = in_comment = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if "<!--" in s:
            in_comment = "-->" not in s
            continue
        if in_comment:
            in_comment = "-->" not in s
            continue
        if in_code:
            continue
        for rx, msg in TEXT_ERRORS:
            if rx.search(line):
                rep.err(f"{path}:{n}", msg)
        for rx, msg in TEXT_WARNINGS:
            if rx.search(line):
                rep.warn(f"{path}:{n}", msg)
        m = ROW_ID.match(line)
        if m and ids is not None:
            rid = next(g for g in m.groups() if g)
            if rid in ids:
                rep.err(f"{path}:{n}", f"duplicate row id {rid}")
            ids[rid] = f"{path}:{n}"


def lint(master, rep):
    master = Path(master)
    slug = master.name
    agent, skill, ref, prov = master / "agent.md", master / "skill" / "SKILL.md", master / "reference", master / "provenance.md"
    if not agent.exists() and not skill.exists():
        rep.err(master, "neither agent.md nor skill/SKILL.md")
        return
    ids = {}
    if agent.exists():
        text = agent.read_text(encoding="utf-8")
        size = len(text.encode("utf-8"))
        if size > CORE_CAP:
            rep.err(agent, f"core {size} B over the {CORE_CAP} B cap; move examples and long cue detail to reference/")
        elif size > CORE_TARGET:
            rep.warn(agent, f"core {size} B over the {CORE_TARGET} B target")
        fm = frontmatter(text)
        if fm is None:
            rep.err(agent, "frontmatter must start on line 1")
        else:
            for key in ("name", "description", "tools", "model"):
                if not fm.get(key):
                    rep.err(agent, f"frontmatter missing {key}")
            if fm.get("name") and fm["name"] != slug:
                rep.err(agent, f"name '{fm['name']}' does not match folder '{slug}'")
            if fm.get("model") and fm["model"] not in MODELS:
                rep.err(agent, f"model '{fm['model']}' not one of {sorted(MODELS)}")
            if len(fm.get("description", "")) > DESC_WARN:
                rep.warn(agent, f"description over {DESC_WARN} chars; it loads every session")
        for h in CORE_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(h)}\s*$", text, re.M):
                rep.err(agent, f"missing section '## {h}'")
        scan_text(agent, rep, ids)
    if skill.exists():
        fm = frontmatter(skill.read_text(encoding="utf-8"))
        if fm is None or not fm.get("description"):
            rep.err(skill, "frontmatter with a description must start on line 1")
        elif fm.get("name") and fm["name"] != slug:
            rep.err(skill, f"skill name '{fm['name']}' does not match folder '{slug}'")
        scan_text(skill, rep, None)  # the skill cites agent rows by id; it defines none
    if ref.is_dir():
        total = 0
        for f in sorted(ref.rglob("*.md")):
            total += f.stat().st_size
            scan_text(f, rep, ids)
        if total > REF_CAP:
            rep.err(ref, f"reference {total} B over the {REF_CAP} B cap")
    if not prov.exists():
        rep.err(master, "provenance.md missing")
        return
    prov_ids = {}
    for n, line in enumerate(prov.read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"^\|\s*([A-Z]{1,2}\d{1,3})\s*\|\s*([a-z ()+,;/]+?)\s*\|", line)
        if m:
            prov_ids[m.group(1)] = m.group(2)
    for rid, where in ids.items():
        if rid not in prov_ids:
            rep.err(where, f"row {rid} has no provenance row")
    for rid in prov_ids:
        if rid not in ids:
            rep.warn(prov, f"provenance row {rid} matches no row in the master")
    if not (master / "tests.md").exists():
        rep.err(master, "tests.md missing")


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    rep = Report()
    for a in argv:
        lint(a, rep)
    for line in rep.errors + rep.warnings:
        print(line)
    print(f"{len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
