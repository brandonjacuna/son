#!/usr/bin/env python3
"""Measure a profile build against its caps.

Usage:
  python3 measure.py <build-dir>                                  # caps check during stage 2
  python3 measure.py <build-dir> --master <master-dir> [--log]    # full measurement at ship

Bytes are measured; tokens are estimated as bytes / 4. --log appends a row to
profiles/_builds/MEASUREMENTS.md (token columns from worker usage are filled by hand
from BUILD.md). Standard library only.
"""
import argparse
import datetime
import sys
from pathlib import Path

CARD_CAP, CARDS_CAP = 3 * 1024, 40 * 1024
CORE_CAP = 12 * 1024


def size(p):
    if p.is_file():
        return p.stat().st_size
    if p.is_dir():
        return sum(f.stat().st_size for f in p.rglob("*") if f.is_file() and f.name != ".shipped")
    return 0


def kb(n):
    return f"{n / 1024:.1f} KB"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build")
    ap.add_argument("--master")
    ap.add_argument("--log", action="store_true")
    a = ap.parse_args()
    build = Path(a.build)
    over = []
    cards = sorted((build / "extract").glob("*.md"))
    for c in cards:
        if size(c) > CARD_CAP:
            over.append(f"card {c.name} {kb(size(c))} over {kb(CARD_CAP)}")
    cards_total = sum(size(c) for c in cards)
    if cards_total > CARDS_CAP:
        over.append(f"cards total {kb(cards_total)} over {kb(CARDS_CAP)}")
    stage_total = size(build)
    print(f"build folder {kb(stage_total)}; {len(cards)} cards, {kb(cards_total)}")
    row = None
    if a.master:
        m = Path(a.master)
        core, skill = size(m / "agent.md"), size(m / "skill")
        ref, prov = size(m / "reference"), size(m / "provenance.md")
        per_call = core + skill
        if core > CORE_CAP:
            over.append(f"core {kb(core)} over {kb(CORE_CAP)}")
        print(f"per-call load {kb(per_call)} (~{per_call // 4} tokens): core {kb(core)}, skill {kb(skill)}")
        print(f"on demand: reference {kb(ref)}; build-time only: provenance {kb(prov)}")
        row = (f"| {datetime.date.today()} | {m.name} | {kb(stage_total)} | {kb(cards_total)} | "
               f"{kb(per_call)} (~{per_call // 4} tok) | {kb(ref)} | | | |")
    for o in over:
        print("OVER CAP:", o)
    if a.log and row:
        log = Path("profiles/_builds/MEASUREMENTS.md")
        if not log.exists():
            sys.exit(f"{log} not found; run from the repo root")
        with log.open("a", encoding="utf-8") as f:
            f.write(row + "\n")
        print(f"row appended to {log}")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())
