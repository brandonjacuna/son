#!/usr/bin/env python3
"""Read-only ClickUp baseline export. Token is read from macOS Keychain, never printed."""
import json, os, subprocess, sys, time, urllib.request, urllib.error, urllib.parse, re

WID = "90131574430"
OUT = sys.argv[1] if len(sys.argv) > 1 else "exports/2026-09-16-baseline"
FULL_LISTS = {  # full fidelity: custom fields + markdown descriptions
    "901323485125": "founding-punch-list",
    "901327884538": "carryover-register",
    "901323733488": "saas-map",
    "901327544218": "saas-catalog",
}
DOCS = ["Sŏn Operating System", "Scaling People: Translation Program", "Operating Agreement",
        "Finance and Technology Seat", "FDN.01", "Claude Project Review", "Master Pointer Index",
        "Technology OS"]
TOKEN = subprocess.run(["security", "find-generic-password", "-s", "clickup-api-token", "-w"],
                       capture_output=True, text=True, check=True).stdout.strip()

def get(url, params=None):
    if params: url += "?" + urllib.parse.urlencode(params, doseq=True)
    for attempt in range(6):
        req = urllib.request.Request(url, headers={"Authorization": TOKEN})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                if int(r.headers.get("X-RateLimit-Remaining", "99")) < 3:
                    time.sleep(max(1, int(r.headers.get("X-RateLimit-Reset", time.time() + 5)) - time.time()))
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(15); continue
            raise RuntimeError(f"HTTP {e.code} on {url.split('?')[0]}: {e.read()[:200]!r}")
    raise RuntimeError("rate limited repeatedly")

def dump(name, obj):
    path = os.path.join(OUT, name); os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f: json.dump(obj, f, ensure_ascii=False, indent=1)

def list_tasks(list_id):
    tasks, page = [], 0
    while True:
        d = get(f"https://api.clickup.com/api/v2/list/{list_id}/task",
                {"include_closed": "true", "subtasks": "true", "include_timl": "true",
                 "include_markdown_description": "true", "archived": "false", "page": page})
        tasks += d.get("tasks", [])
        if d.get("last_page", True) or not d.get("tasks"): break
        page += 1
    return tasks

report = {}
# Hierarchy
V2 = "https://api.clickup.com/api/v2"
spaces = get(f"{V2}/team/{WID}/space", {"archived": "false"})["spaces"]
hier = []
for s in spaces:
    folders = get(f"{V2}/space/{s['id']}/folder", {"archived": "false"})["folders"]
    loose = get(f"{V2}/space/{s['id']}/list", {"archived": "false"})["lists"]
    hier.append({"space": s, "folders": folders, "folderless_lists": loose})
dump("hierarchy.json", hier)
all_lists = [(h["space"]["name"], l) for h in hier for l in h["folderless_lists"]] + \
            [(h["space"]["name"], l) for h in hier for f in h["folders"] for l in f.get("lists", [])]
captures = {l["id"]: (sp, l["name"]) for sp, l in all_lists if "capture" in l["name"].lower()}

# List definitions + custom field definitions for every list we export
for lid in list(FULL_LISTS) + list(captures):
    dump(f"lists/{lid}-list.json", get(f"{V2}/list/{lid}"))
    dump(f"lists/{lid}-fields.json", get(f"{V2}/list/{lid}/field"))

for lid, slug in FULL_LISTS.items():
    t = list_tasks(lid); dump(f"tasks/{slug}.json", t)
    home = sum(1 for x in t if x.get("list", {}).get("id") == lid)
    report[slug] = {"tasks": len(t), "home_list": home, "subtasks": sum(1 for x in t if x.get("parent"))}
for lid, (sp, name) in captures.items():
    t = list_tasks(lid)
    slim = [{k: x.get(k) for k in ("id", "name", "status", "parent", "date_created", "date_updated",
            "tags", "assignees", "custom_item_id", "url")} for x in t]
    dump(f"tasks/capture-{lid}.json", slim)
    report[f"capture: {sp} / {name}"] = {"tasks": len(t)}

# Docs (v3)
V3 = f"https://api.clickup.com/api/v3/workspaces/{WID}"
docs, cursor = [], None
while True:
    d = get(f"{V3}/docs", {"limit": 100, **({"next_cursor": cursor} if cursor else {})})
    docs += d.get("docs", []); cursor = d.get("next_cursor")
    if not cursor: break
dump("docs/_index.json", [{k: x.get(k) for k in ("id", "name", "parent", "date_created", "deleted", "archived")} for x in docs])
norm = lambda s: re.sub(r"\W+", " ", s or "").lower()
doc_report = {}
for want in DOCS:
    hits = [x for x in docs if norm(want) in norm(x.get("name")) and not x.get("deleted")]
    doc_report[want] = [h["name"] for h in hits]
    for h in hits:
        pages = get(f"{V3}/docs/{h['id']}/pages", {"content_format": "text/md", "max_page_depth": -1})
        dump(f"docs/{h['id']}.json", pages)
        def walk(ps, acc):
            for p in ps: acc.append(p); walk(p.get("pages", []), acc)
            return acc
        flat = walk(pages if isinstance(pages, list) else pages.get("pages", []), [])
        safe = re.sub(r"[^\w.-]+", "_", h["name"])[:60]
        with open(os.path.join(OUT, "docs", f"{safe}.md"), "w") as f:
            for p in flat: f.write(f"\n\n# {p.get('name','')}\n\n{p.get('content','')}")
        doc_report[want + " :: chars"] = sum(len(p.get("content") or "") for p in flat)
report["docs_total_in_workspace"] = len(docs); report["docs"] = doc_report
dump("REPORT.json", report)
print(json.dumps(report, ensure_ascii=False, indent=1))
