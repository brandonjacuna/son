"""Publish a built digest to ClickUp as a sub-page of "Index and Page Template".

Usage: python scripts/publish_digest.py data/digests/<delivery>.md

Creates the page under the template page, or replaces it if a page with the same
delivery date already exists there (a DRAFT page for that date is renamed and replaced).
The template page itself is never written. Needs CLICKUP_API_TOKEN in the environment.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import TIMEOUT, env  # noqa: E402

WORKSPACE = "90131574430"
DOC = "2ky45bmy-20073"
TEMPLATE_PAGE = "2ky45bmy-33313"  # "Index and Page Template": parent of every digest, never edited
BASE = f"https://api.clickup.com/api/v3/workspaces/{WORKSPACE}/docs/{DOC}"


def children(headers) -> list[dict]:
    r = requests.get(f"{BASE}/pageListing", headers=headers, params={"max_page_depth": -1}, timeout=TIMEOUT)
    r.raise_for_status()
    top = next((p for p in r.json() if p["id"] == TEMPLATE_PAGE), {})
    return top.get("pages", [])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("markdown")
    args = ap.parse_args(argv)
    token = env("CLICKUP_API_TOKEN")
    if not token:
        print("CLICKUP_API_TOKEN not set; digest not published", file=sys.stderr)
        return 2
    lines = Path(args.markdown).read_text().splitlines()
    name = lines[0].lstrip("# ").strip()
    body = "\n".join(lines[2:])
    date_key = name.removeprefix("DRAFT ").split(" |")[0]
    headers = {"Authorization": token, "Content-Type": "application/json"}
    existing = next((p for p in children(headers) if p["name"].removeprefix("DRAFT ").startswith(date_key)), None)
    payload = {"name": name, "content": body, "content_format": "text/md"}
    if existing:
        if existing["id"] == TEMPLATE_PAGE:
            raise SystemExit("refusing to write the template page")
        r = requests.put(f"{BASE}/pages/{existing['id']}", headers=headers,
                         json={**payload, "content_edit_mode": "replace"}, timeout=TIMEOUT)
        page_id = existing["id"]
    else:
        r = requests.post(f"{BASE}/pages", headers=headers, json={**payload, "parent_page_id": TEMPLATE_PAGE}, timeout=TIMEOUT)
        page_id = r.json().get("id") if r.ok else None
    r.raise_for_status()
    print(f"published '{name}' as page {page_id}: https://app.clickup.com/{WORKSPACE}/v/dc/{DOC}/{page_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
