"""Push home-zone Signals and sync the Watchlist in ClickUp.

Usage:
  python scripts/clickup_sync.py signals     # queued changes within 2 miles -> Signals list, once each
  python scripts/clickup_sync.py watchlist   # peers, direct comp, Korean awareness -> Watchlist tasks (upsert)
  add --dry-run to write the planned tasks to data/signals/pending_<mode>.json without calling ClickUp

Uses CLICKUP_API_TOKEN. Without it, runs as --dry-run so a routine with the ClickUp connector
can post the pending file instead. Task ids are remembered in data/signals/*.json so reruns
update instead of duplicating.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import CONFIG_DIR, DATA_DIR, TIMEOUT, env  # noqa: E402

SIG = DATA_DIR / "signals"
QUEUE, SENT, TASKS = SIG / "queue.jsonl", SIG / "sent.json", SIG / "watchlist_tasks.json"
FIELDS = json.loads((CONFIG_DIR / "clickup_fields.json").read_text())
API = "https://api.clickup.com/api/v2"


def field(name: str, value):
    f = FIELDS["fields"][name]
    if value is None or value == "" or (isinstance(value, float) and pd.isna(value)):
        return None
    if f["type"] == "drop_down":
        return {"id": f["id"], "value": f["options"][value]}
    if f["type"] == "date":
        return {"id": f["id"], "value": int(pd.Timestamp(value).tz_localize("America/Chicago").timestamp() * 1000)}
    if f["type"] == "number":
        return {"id": f["id"], "value": float(value)}
    return {"id": f["id"], "value": str(value)}


def area_text(r) -> str:
    if r.get("subsection"):
        return f"{r.get('hub')}: {r['subsection']}"
    return r.get("hub") or (f"Off-hub: {r['cluster']}" if r.get("cluster") else "Unassigned")


# ---------------------------------------------------------------- plans

def plan_signals() -> list[dict]:
    sent = set(json.loads(SENT.read_text())) if SENT.exists() else set()
    rows = [json.loads(line) for line in QUEUE.read_text().splitlines()] if QUEUE.exists() else []
    plans = []
    for r in rows:
        key = f"{r['source']}|{r['record_id']}|{r['change']}"
        if key in sent:
            continue
        tier = "Act" if r.get("home_1mi") else "Alert"
        what = {"new": "new record", "new_facility": "first inspection", "removed": "dropped from source",
                "status_change": "status change"}.get(r["change"], r["change"])
        plans.append({"key": key, "list_id": FIELDS["signals_list_id"],
                      "name": f"{tier}: {r.get('name') or 'Unnamed'} ({r.get('distance_mi')} mi), {what}",
                      "description": (f"Source: {r['source']} ({r['run_date']})\nAddress: {r.get('address')}, {r.get('city')}\n"
                                      f"Area: {area_text(r)}\nDistance from 207 E St. Elmo Rd: {r.get('distance_mi')} mi\n"
                                      f"Detail: {r.get('detail') or r.get('status') or ''}\n"
                                      "Single-source signal until a second source confirms it.")})
    return plans


def plan_watchlist() -> list[dict]:
    peers = pd.read_csv(CONFIG_DIR / "peers_draft.csv", dtype=str, keep_default_na=False)
    korean = pd.read_csv(DATA_DIR / "korean_sweep" / "candidates.csv", dtype=str, keep_default_na=False)
    plans = []
    for r in peers.to_dict("records"):
        reason = "Direct comp" if r["inclusion"] == "direct_comp" else "Peer"
        plans.append({"entity_id": f"peer:{r['name']}", "name": r["name"], "reason": reason, "concept": r["concept_type"],
                      "area": area_text(r), "hub_tier": "Hub" if r.get("hub") else "Off-hub", "status": "Open",
                      "distance": r.get("distance_mi"), "last_signal": (r.get("last_receipts") or r.get("last_inspection") or "")[:10],
                      "description": f"{r['address']}\n{r['notes']}\nState records: {r.get('evidence', '')}"})
    for r in korean[(korean["tier"] != "direct_comp") & korean["activity"].str.startswith("operating")].to_dict("records"):
        plans.append({"entity_id": f"korean:{r['addr_key']}", "name": r["name"], "reason": "Korean awareness",
                      "concept": "Korean", "area": area_text(r), "hub_tier": "Hub" if r.get("hub") else "Off-hub",
                      "status": "Open", "distance": r.get("distance_mi"), "last_signal": (r.get("latest_date") or "")[:10],
                      "description": f"{r['address']}, {r['city']}\n{r['activity']}\nSources: {r['sources']}"})
    return plans


# ---------------------------------------------------------------- push

def push_signals(headers, plans) -> int:
    sent = set(json.loads(SENT.read_text())) if SENT.exists() else set()
    for p in plans:
        r = requests.post(f"{API}/list/{p['list_id']}/task", headers=headers,
                          json={"name": p["name"], "description": p["description"]}, timeout=TIMEOUT)
        r.raise_for_status()
        sent.add(p["key"])
    SENT.write_text(json.dumps(sorted(sent), indent=1))
    return len(plans)


def push_watchlist(headers, plans) -> int:
    """Upsert by entity id; entries whose content is unchanged since the last push are skipped."""
    ids = json.loads(TASKS.read_text()) if TASKS.exists() else {}
    ids = {k: (v if isinstance(v, dict) else {"id": v, "hash": None}) for k, v in ids.items()}
    changed = 0
    for p in plans:
        digest = hashlib.sha1(json.dumps(p, sort_keys=True).encode()).hexdigest()
        if ids.get(p["entity_id"], {}).get("hash") == digest:
            continue
        changed += 1
        cf = [x for x in [field("Entity ID", p["entity_id"]), field("Watch reason", p["reason"]),
                          field("Concept type", p["concept"]), field("Area", p["area"]), field("Hub tier", p["hub_tier"]),
                          field("Venue status", p["status"]), field("Distance (mi)", p["distance"] or None),
                          field("Last signal", p["last_signal"] or None)] if x]
        tid = ids.get(p["entity_id"], {}).get("id")
        if tid:
            requests.put(f"{API}/task/{tid}", headers=headers, json={"name": p["name"], "description": p["description"]},
                         timeout=TIMEOUT).raise_for_status()
            for c in cf:
                requests.post(f"{API}/task/{tid}/field/{c['id']}", headers=headers, json={"value": c["value"]},
                              timeout=TIMEOUT).raise_for_status()
        else:
            r = requests.post(f"{API}/list/{FIELDS['list_id']}/task", headers=headers,
                              json={"name": p["name"], "description": p["description"], "custom_fields": cf}, timeout=TIMEOUT)
            r.raise_for_status()
            tid = r.json()["id"]
        ids[p["entity_id"]] = {"id": tid, "hash": digest}
        TASKS.write_text(json.dumps(ids, indent=1, sort_keys=True))
    return changed


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=["signals", "watchlist"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    SIG.mkdir(parents=True, exist_ok=True)
    plans = plan_signals() if args.mode == "signals" else plan_watchlist()
    token = env("CLICKUP_API_TOKEN")
    if args.dry_run or not token:
        out = SIG / f"pending_{args.mode}.json"
        out.write_text(json.dumps({"written": datetime.now(timezone.utc).isoformat(), "items": plans}, indent=1))
        print(f"{len(plans)} {args.mode} items written to {out} (not posted: {'dry run' if args.dry_run else 'no CLICKUP_API_TOKEN'})")
        return 0
    headers = {"Authorization": token, "Content-Type": "application/json"}
    n = push_signals(headers, plans) if args.mode == "signals" else push_watchlist(headers, plans)
    (SIG / f"pending_{args.mode}.json").unlink(missing_ok=True)
    print(f"{n} {args.mode} items posted or updated in ClickUp ({len(plans)} planned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
