#!/usr/bin/env python3
"""File an existing transcript (Wispr Flow export, Apple recording, anything text) on a meeting.

    python3 scripts/file_transcript.py ~/Downloads/founders-2026-10-06.md
    python3 scripts/file_transcript.py notes.txt --task 86akk2ebn
    python3 scripts/file_transcript.py notes.txt --date 2026-10-06 --dry-run

It writes the text as a page in the meeting type's notes Doc, sets Notes Doc Link on the
meeting task and leaves the meeting at Held. Filling Notes Doc Link triggers the ClickUp
automation that has the agent append a summary and set Notes Synced.
"""
import argparse, datetime, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cu import req, WID

MEETINGS_LIST = "901329089997"
NOTES_DOCS = {"Founders Meeting": "2ky45bmy-18193",
              "Founders Standup": "2ky45bmy-18213",
              "Investor/Lender": "2ky45bmy-18233"}


def find_meeting(task_id=None, when=None):
    tasks = req("GET", f"list/{MEETINGS_LIST}/task?include_closed=true")["tasks"]
    if task_id:
        return next(t for t in tasks if t["id"] == task_id)
    day = when or datetime.date.today()
    dated = [t for t in tasks if t.get("due_date") and
             datetime.datetime.fromtimestamp(int(t["due_date"]) / 1000).date() == day]
    if not dated:
        raise SystemExit(f"No meeting task due {day}. Pass --task <id>.")
    return sorted(dated, key=lambda t: int(t["due_date"]))[-1]


def meeting_type(task):
    for c in task["custom_fields"]:
        if c["name"] == "Meeting Type" and c.get("value") is not None:
            return next((o.get("name") or o.get("label")
                         for o in c["type_config"]["options"]
                         if str(o.get("orderindex")) == str(c["value"])), None)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("transcript", help="path to a .txt or .md transcript")
    p.add_argument("--task")
    p.add_argument("--date")
    p.add_argument("--source", default="Wispr Flow", help="where the transcript came from")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    text = open(a.transcript, encoding="utf-8").read().strip()
    when = datetime.date.fromisoformat(a.date) if a.date else None
    task = find_meeting(a.task, when)
    mtype = meeting_type(task) or "Founders Meeting"
    doc = NOTES_DOCS.get(mtype)
    body = (f"# {task['name']}\n\n_Transcript filed {datetime.date.today()} from {a.source}._\n\n"
            + text)
    print(f"Meeting: {task['name']} ({task['id']}), type {mtype}, {len(text)} chars")
    if a.dry_run or not doc:
        print(body[:1500])
        return

    page = req("POST", f"workspaces/{WID}/docs/{doc}/pages",
               {"name": task["name"], "content": body, "content_format": "text/md"}, v=3)
    url = f"https://app.clickup.com/{WID}/v/dc/{doc}/{page['id']}"
    fields = {c["name"]: c["id"] for c in req("GET", f"list/{MEETINGS_LIST}/field")["fields"]}
    if task["status"]["status"] in ("scheduled", "prep sent"):
        req("PUT", f"task/{task['id']}", {"status": "held"})
    req("POST", f"task/{task['id']}/field/{fields['Notes Doc Link']}", {"value": url})
    req("POST", f"task/{task['id']}/comment",
        {"comment_text": f"Transcript filed from {a.source}. {url}"})
    print("Filed:", url)


if __name__ == "__main__":
    main()
