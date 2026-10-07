#!/usr/bin/env python3
"""Build a SCORM 1.2 package from a module's scenarios.md.

Usage:
  python scripts/build_scorm.py modules/<domain>/<module>          # requires all bindings filled
  python scripts/build_scorm.py modules/<domain>/<module> --draft  # shows open bindings visibly

Output: exports/<ID>/scorm/<ID>-scenarios.zip
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLAYER = ROOT / "scorm" / "player"
BIND_RE = re.compile(r"\{\{bind:([a-z0-9_.\-]+)\}\}")
END_RE = re.compile(r"^end\s*\((strong|recoverable|failure)\)$", re.I)


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def load_bindings(module_dir):
    p = module_dir / "bindings.yaml"
    if not p.exists():
        return {}
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return {b["key"]: b for b in (data.get("bindings") or [])}


def resolve(text, bindings, draft, missing):
    def sub(m):
        key = m.group(1)
        b = bindings.get(key)
        if b and b.get("status") == "filled" and b.get("value") is not None:
            return str(b["value"])
        missing.add(key)
        return f"[binding: {key}]" if draft else m.group(0)
    return BIND_RE.sub(sub, text or "")


def field(block, name):
    m = re.search(rf"^{name}:\s*(.+?)(?=^\w[\w ]*:|^-\s|\Z)", block, re.M | re.S | re.I)
    return " ".join(m.group(1).split()) if m else None


def bold_field(block, name):
    m = re.search(rf"\*\*{name}\.\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", block, re.S | re.I)
    return " ".join(m.group(1).split()) if m else None


def node_id(label):
    return label.strip().lower().replace(" ", "-")


def parse_scenarios(md):
    scenarios = []
    for chunk in re.split(r"^## ", md, flags=re.M)[1:]:
        title_line, _, body = chunk.partition("\n")
        m = re.match(r"Scenario\s+(\S+):\s*(.+)", title_line.strip())
        if not m:
            continue
        parts = re.split(r"^### ", body, flags=re.M)
        head, node_blocks = parts[0], parts[1:]
        sc = {
            "title": m.group(2).strip(),
            "setup": bold_field(head, "Setup") or "",
            "media": bold_field(head, "Media"),
            "nodes": {},
            "start": None,
        }
        for nb in node_blocks:
            label, _, content = nb.partition("\n")
            label = label.strip()
            if not label:
                continue
            nid = node_id(label)
            if label.lower().startswith("decision"):
                choices = []
                for cm in re.finditer(r"^-\s*[A-Z]\.\s*(.+?)\s*->\s*go to\s+(.+)$", content, re.M):
                    choices.append({"label": cm.group(1).strip(), "to": node_id(cm.group(2))})
                sc["nodes"][nid] = {"type": "decision", "prompt": field(content, "Prompt") or "",
                                    "choices": choices, "media": field(content, "Media")}
                if sc["start"] is None:
                    sc["start"] = nid
            else:
                nxt = (field(content, "Next") or "").strip()
                em = END_RE.match(nxt)
                sc["nodes"][nid] = {
                    "type": "outcome",
                    "consequence": field(content, "Consequence"),
                    "feedback": field(content, "Feedback"),
                    "rationale": field(content, "Expert rationale"),
                    "media": field(content, "Media"),
                    "end": em.group(1).lower() if em else None,
                    "next": None if em else node_id(nxt),
                }
        scenarios.append(sc)
    return scenarios


def validate(scenarios):
    errors = []
    for sc in scenarios:
        ids = set(sc["nodes"])
        if not sc["start"]:
            errors.append(f"{sc['title']}: no Decision node")
        for nid, n in sc["nodes"].items():
            targets = [c["to"] for c in n.get("choices", [])] if n["type"] == "decision" else [n["next"]] if n["next"] else []
            for t in targets:
                if t not in ids:
                    errors.append(f"{sc['title']}: {nid} points to missing node '{t}'")
            if n["type"] == "outcome" and not n["end"] and not n["next"]:
                errors.append(f"{sc['title']}: {nid} has no Next")
        if not any(n.get("end") == "recoverable" for n in sc["nodes"].values()):
            errors.append(f"{sc['title']}: needs at least one recoverable end (see framework/module-spec.md)")
    return errors


def walk_strings(obj, fn):
    if isinstance(obj, dict):
        return {k: walk_strings(v, fn) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_strings(v, fn) for v in obj]
    if isinstance(obj, str):
        return fn(obj)
    return obj


MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="SON-{id}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-{id}">
    <organization identifier="ORG-{id}">
      <title>{title}</title>
      <item identifier="ITEM-{id}" identifierref="RES-{id}" isvisible="true">
        <title>{title}</title>
        <adlcp:masteryscore>{mastery}</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-{id}" type="webcontent" adlcp:scormtype="sco" href="index.html">
{files}
    </resource>
  </resources>
</manifest>
"""


def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("module_dir")
    ap.add_argument("--draft", action="store_true", help="build with open bindings shown visibly")
    ap.add_argument("--mastery", type=int, default=None)
    args = ap.parse_args()

    mdir = (ROOT / args.module_dir).resolve() if not Path(args.module_dir).is_absolute() else Path(args.module_dir)
    meta = front_matter(mdir / "module.md")
    mod_id = meta.get("id", mdir.name)
    title = meta.get("title", mod_id)
    mastery = args.mastery or int(meta.get("mastery_score", 70))

    scen_path = mdir / "scenarios.md"
    if not scen_path.exists():
        sys.exit(f"No scenarios.md in {mdir}")
    scenarios = parse_scenarios(scen_path.read_text(encoding="utf-8"))
    if not scenarios:
        sys.exit("No scenarios parsed. Check the format in framework/module-spec.md.")
    errors = validate(scenarios)
    if errors:
        sys.exit("Scenario errors:\n  " + "\n  ".join(errors))

    bindings = load_bindings(mdir)
    missing = set()
    scenarios = walk_strings(scenarios, lambda s: resolve(s, bindings, args.draft, missing))
    if missing and not args.draft:
        sys.exit("Open bindings, fill them or build with --draft:\n  " + "\n  ".join(sorted(missing)))

    data = {"id": mod_id, "title": title, "mastery": mastery, "scenarios": scenarios,
            "closing": meta.get("closing")}
    out_dir = ROOT / "exports" / str(mod_id) / "scorm"
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = "-DRAFT" if args.draft and missing else ""
    zpath = out_dir / f"{mod_id}-scenarios{suffix}.zip"

    player_files = ["index.html", "player.css", "player.js", "scorm_api.js"]
    all_files = player_files + ["data.js"]
    files_xml = "\n".join(f'      <file href="{f}"/>' for f in all_files)
    manifest = MANIFEST.format(id=xml_escape(str(mod_id)), title=xml_escape(str(title)),
                               mastery=mastery, files=files_xml)

    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        for f in player_files:
            z.write(PLAYER / f, f)
        z.writestr("data.js", "window.MODULE_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")

    print(f"Built {zpath.relative_to(ROOT)}")
    print(f"  scenarios: {len(scenarios)}, mastery score: {mastery}")
    if missing:
        print(f"  DRAFT: {len(missing)} open binding(s) shown in the package: {', '.join(sorted(missing))}")


if __name__ == "__main__":
    main()
