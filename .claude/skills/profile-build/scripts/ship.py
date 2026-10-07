#!/usr/bin/env python3
"""Generate .claude/agents/<slug>.md and .claude/skills/<slug>/ from a profile master.

Usage:
  python3 ship.py <master-dir>      # generate copies for one seat
  python3 ship.py --check           # drift check every master under profiles/ (no writes)

A generated copy that differs from what was last shipped was edited by hand: ship refuses
and names it. Edit the master, then ship again. Hashes of shipped copies live in
<master>/.shipped. Standard library only.
"""
import hashlib
import shutil
import sys
from pathlib import Path


def repo_root():
    p = Path.cwd().resolve()
    for d in [p, *p.parents]:
        if (d / ".git").exists():
            return d
    sys.exit("not inside a git repository")


def digest(path):
    if path.is_dir():
        h = hashlib.sha256()
        for f in sorted(path.rglob("*")):
            if f.is_file():
                h.update(str(f.relative_to(path)).encode())
                h.update(f.read_bytes())
        return h.hexdigest()[:16]
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def read_shipped(master):
    rec = {}
    f = master / ".shipped"
    if f.exists():
        for line in f.read_text().splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                rec[k] = v
    return rec


def targets(root, master):
    slug = master.name
    out = []
    if (master / "agent.md").exists():
        out.append(("agent", master / "agent.md", root / ".claude" / "agents" / f"{slug}.md"))
    if (master / "skill").is_dir():
        out.append(("skill", master / "skill", root / ".claude" / "skills" / slug))
    return out


def drift(master, root):
    rec, problems = read_shipped(master), []
    for kind, src, dst in targets(root, master):
        if dst.exists() and kind in rec and digest(dst) != rec[kind]:
            problems.append(f"{dst} was edited by hand since the last ship")
        if dst.exists() and kind in rec and digest(src) != rec[kind] and digest(dst) == rec[kind]:
            problems.append(f"{dst} is stale: the master changed and was not shipped")
    return problems


def ship(master, root):
    master = master.resolve()
    if "founders" in master.parts:
        sys.exit(f"{master} is founder-only: ask Brandon where its agent lives before shipping")
    problems = [p for p in drift(master, root) if "by hand" in p]
    if problems:
        sys.exit("\n".join(problems))
    rec = read_shipped(master)
    for kind, src, dst in targets(root, master):
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copyfile(src, dst)
        rec[kind] = digest(dst)
        print(f"shipped {kind}: {dst.relative_to(root)}")
    (master / ".shipped").write_text("".join(f"{k}={v}\n" for k, v in sorted(rec.items())))


def main(argv):
    root = repo_root()
    if argv == ["--check"]:
        masters = [p.parent for p in (root / "profiles").rglob(".shipped") if "_source" not in p.parts]
        problems = [x for m in masters for x in drift(m, root)]
        print("\n".join(problems) or f"no drift in {len(masters)} shipped seats")
        return 1 if problems else 0
    if len(argv) != 1:
        print(__doc__)
        return 2
    ship(Path(argv[0]), root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
