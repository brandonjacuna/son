#!/usr/bin/env python3
"""Lint module content against the standing rules and the module spec.

Usage:
  python scripts/lint.py               # modules/ and templates/
  python scripts/lint.py path ...      # specific files or folders
  python scripts/lint.py --all         # every authored file in the repo

Exit code 1 if any error. Warnings never fail the run.
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"canon/standing-rules.md", "scripts/lint.py"}
SKIP_DIRS = {"profiles/cache", "exports", ".git", "node_modules"}
STATUSES = ["identified", "concept", "designed", "drafted", "reviewed", "parked",
            "bound", "rendered", "published", "measured", "retired", "routed-out"]
MOVES = ["Activate", "Demonstrate", "Practice", "Retrieve", "Integrate"]
REQUIRED_META = ["id", "title", "domain", "status", "learners", "program", "transfer_goal", "components"]
BIND_RE = re.compile(r"\{\{bind:([a-z0-9_.\-]+)\}\}")

ERRORS = [
    (re.compile("\u2014"), "em dash; use a comma, a colon, or restructure"),
    (re.compile(r"\bguests?\b", re.I), "'guest'; the person we serve is the customer"),
    (re.compile(r"\b(good energy|dosi|luxx)\b", re.I), "daypart code name; never on any surface"),
    (re.compile(r"\b(we believe|we hope|our goal is)\b", re.I), "performed conviction; write it declaratively"),
    (re.compile(r"\b(fuck\w*|shit\w*|damn\w*|bullshit)\b", re.I), "profanity is spoken only"),
]
WARNINGS = [
    (re.compile(r"(?=.*\bstag(e|es|ing)\b)(?=.*\b(kitchen|chef|cook|trial|tryout|line)\b)", re.I),
     "'stage' in the kitchen-trial sense is written 'paid practical'"),
    (re.compile(r"\$\s?\d|\b\d+(\.\d+)?\s?%"), "figure detected; figures come from Airtable via a fact.* binding"),
    (re.compile(r"\b(coqodaq|alinea|gracious)\b", re.I), "lineage practice; flag for Brandon, do not reconstruct"),
]


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, path, line, msg):
        self.errors.append(f"ERROR   {path}:{line}  {msg}")

    def warn(self, path, line, msg):
        self.warnings.append(f"warning {path}:{line}  {msg}")


def rel(p):
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def strip_bindings(line):
    return BIND_RE.sub("", line)


def lint_text(path, rep):
    text = path.read_text(encoding="utf-8")
    in_code = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        clean = strip_bindings(line)
        for rx, msg in ERRORS:
            if rx.search(clean):
                rep.err(rel(path), i, msg)
        for rx, msg in WARNINGS:
            if rx.search(clean):
                rep.warn(rel(path), i, msg)


def front_matter(path):
    m = re.match(r"^---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def lint_module(mdir, rep):
    mod = mdir / "module.md"
    meta = front_matter(mod)
    if meta is None:
        rep.err(rel(mod), 1, "missing YAML front matter")
        return
    for k in REQUIRED_META:
        if k not in meta:
            rep.err(rel(mod), 1, f"front matter missing '{k}'")
    if meta.get("status") not in STATUSES:
        rep.err(rel(mod), 1, f"status '{meta.get('status')}' not one of {STATUSES}")

    content = mdir / "content.md"
    if content.exists():
        heads = re.findall(r"^## (\w+)", content.read_text(encoding="utf-8"), re.M)
        moves = [h for h in heads if h in MOVES]
        if moves != MOVES:
            rep.err(rel(content), 1, f"the five moves must appear in order: {', '.join(MOVES)} (found {', '.join(moves) or 'none'})")
    elif meta.get("status") not in ("identified", "concept", "routed-out"):
        rep.err(rel(mdir), 0, "content.md required from 'designed' onward")

    used = {}
    for f in mdir.glob("*.md"):
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for key in BIND_RE.findall(line):
                used.setdefault(key, f"{rel(f)}:{i}")
    declared = {}
    bfile = mdir / "bindings.yaml"
    if bfile.exists():
        data = yaml.safe_load(bfile.read_text(encoding="utf-8")) or {}
        for b in data.get("bindings") or []:
            declared[b.get("key")] = b
            if b.get("status") == "filled" and not b.get("source"):
                rep.err(rel(bfile), 0, f"{b.get('key')} is filled but has no source")
    for key, where in used.items():
        if key not in declared:
            rep.err(where.rsplit(":", 1)[0], where.rsplit(":", 1)[1], f"binding '{key}' used but not declared in bindings.yaml")
    for key in declared:
        if key not in used:
            rep.warn(rel(bfile), 0, f"binding '{key}' declared but never used")

    status = meta.get("status")
    if status in ("bound", "rendered", "published", "measured"):
        open_keys = [k for k, b in declared.items() if b.get("status") != "filled"]
        if open_keys:
            rep.err(rel(mod), 1, f"status '{status}' but bindings still open: {', '.join(open_keys)}")


def targets(args):
    if args.all:
        paths = [ROOT]
    elif args.paths:
        paths = [Path(p).resolve() for p in args.paths]
    else:
        paths = [ROOT / "modules", ROOT / "templates"]
    files, mods = [], set()
    for p in paths:
        items = [p] if p.is_file() else p.rglob("*")
        for f in items:
            r = rel(f)
            if any(r.startswith(d) for d in SKIP_DIRS) or r in SKIP:
                continue
            if f.is_file() and f.suffix in (".md", ".yaml", ".yml"):
                files.append(f)
            if f.is_file() and f.name == "module.md" and "templates" not in r:
                mods.add(f.parent)
    return files, mods


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    rep = Report()
    files, mods = targets(args)
    for f in files:
        lint_text(f, rep)
    for m in sorted(mods):
        lint_module(m, rep)
    for line in rep.errors + rep.warnings:
        print(line)
    print(f"\n{len(files)} files, {len(mods)} modules: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
