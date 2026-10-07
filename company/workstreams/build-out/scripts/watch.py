#!/usr/bin/env python3
"""Fetch each watched page, reduce it to visible text, hash it, and record changes.
Writes codes/snapshots/<id>.txt (or monitoring/snapshots/) and prints changed ids.
Runs in GitHub Actions; no model calls, no cost.
"""
import hashlib, html, re, sys, urllib.request
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
cfg = yaml.safe_load((ROOT / "monitoring/sources.yaml").read_text())
changed = []
for group, items in cfg.items():
    outdir = ROOT / ("codes/snapshots" if group == "codes" else "monitoring/snapshots")
    outdir.mkdir(parents=True, exist_ok=True)
    for it in items:
        try:
            req = urllib.request.Request(it["url"], headers={"User-Agent": "Mozilla/5.0 (son watcher)"})
            raw = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "ignore")
        except Exception as e:
            print(f"WARN {it['id']}: {e}", file=sys.stderr); continue
        raw = re.sub(r"(?is)<(script|style|noscript|header|footer|nav)\b.*?</\1>", " ", raw)
        text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
        text = "\n".join(l.strip() for l in text.splitlines() if l.strip())
        text = re.sub(r"[ \t]+", " ", text)
        f = outdir / f"{it['id']}.txt"
        old = f.read_text() if f.exists() else None
        if old is None or hashlib.sha1(old.encode()).hexdigest() != hashlib.sha1(text.encode()).hexdigest():
            f.write_text(text)
            if old is not None:
                changed.append(f"{group}:{it['id']}")
print("\n".join(changed))
