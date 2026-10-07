#!/usr/bin/env python3
"""Turn a two-channel meeting recording into a speaker-labelled transcript in ClickUp.

Left channel = TX1 = Brandon, right channel = TX2 = Dominic (override with --speakers).

    python3 scripts/meeting_transcript.py ~/Desktop/founders-2026-10-06.m4a
    python3 scripts/meeting_transcript.py recording.m4a --task 86akk2ebn
    python3 scripts/meeting_transcript.py recording.m4a --dry-run

Tokens come from the macOS Keychain and are never printed:
    security add-generic-password -a son -s assemblyai-api-token -U -w
    security add-generic-password -a son -s clickup-api-token -U -w
"""
import argparse, datetime, json, os, subprocess, sys, time, urllib.request, urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from cu import req, WID  # ClickUp helper

MEETINGS_LIST = "901329089997"
NOTES_DOCS = {"Founders Meeting": "2ky45bmy-18193",
              "Founders Standup": "2ky45bmy-18213",
              "Investor/Lender": "2ky45bmy-18233"}
AAI = "https://api.assemblyai.com/v2"


def key(service):
    return subprocess.run(["security", "find-generic-password", "-s", service, "-w"],
                          capture_output=True, text=True, check=True).stdout.strip()


def aai(method, path, body=None, raw=None, token=None):
    r = urllib.request.Request(AAI + path, method=method,
                               headers={"authorization": token,
                                        "content-type": "application/octet-stream" if raw
                                        else "application/json"},
                               data=raw if raw else (json.dumps(body).encode() if body else None))
    with urllib.request.urlopen(r, timeout=300) as resp:
        return json.load(resp)


def transcribe(path, token, poll=15):
    up = aai("POST", "/upload", raw=open(path, "rb").read(), token=token)
    job = aai("POST", "/transcript", {"audio_url": up["upload_url"], "multichannel": True,
                                      "punctuate": True, "format_text": True}, token=token)
    while True:
        t = aai("GET", f"/transcript/{job['id']}", token=token)
        if t["status"] == "completed":
            return t
        if t["status"] == "error":
            raise RuntimeError(t.get("error"))
        time.sleep(poll)


def to_markdown(t, speakers, title):
    lines = [f"# {title}", "",
             f"_Transcribed {datetime.date.today()} from a two-channel recording. "
             f"Speakers come from the microphone channel, not from voice matching._", ""]
    for u in t.get("utterances", []):
        who = speakers.get(str(u.get("channel")), f"Channel {u.get('channel')}")
        mins, secs = divmod(int(u["start"] / 1000), 60)
        lines.append(f"**{who}** ({mins}:{secs:02d}) {u['text'].strip()}")
        lines.append("")
    if len(lines) <= 4:
        lines += ["_No utterances returned._", "", "## Full text", "", t.get("text", "")]
    return "\n".join(lines)


def find_meeting(task_id=None, when=None):
    tasks = req("GET", f"list/{MEETINGS_LIST}/task?include_closed=true")["tasks"]
    if task_id:
        return next(t for t in tasks if t["id"] == task_id)
    day = when or datetime.date.today()
    dated = [t for t in tasks if t.get("due_date") and
             datetime.datetime.fromtimestamp(int(t["due_date"]) / 1000).date() == day]
    if not dated:
        raise SystemExit(f"No meeting task with a due date of {day}. Pass --task <id>.")
    return sorted(dated, key=lambda t: int(t["due_date"]))[-1]


def meeting_type(task):
    for c in task["custom_fields"]:
        if c["name"] == "Meeting Type" and c.get("value") is not None:
            opts = c["type_config"]["options"]
            return next((o.get("name") or o.get("label") for o in opts
                         if str(o.get("orderindex")) == str(c["value"])), None)
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("audio")
    p.add_argument("--task", help="Meetings task id; otherwise matched by due date")
    p.add_argument("--date", help="YYYY-MM-DD of the meeting (default: today)")
    p.add_argument("--speakers", default="1=Brandon,2=Dominic",
                   help="channel=name pairs, e.g. 1=Brandon,2=Dominic")
    p.add_argument("--dry-run", action="store_true", help="print the transcript, write nothing")
    a = p.parse_args()

    speakers = dict(kv.split("=", 1) for kv in a.speakers.split(","))
    when = datetime.date.fromisoformat(a.date) if a.date else None

    task = find_meeting(a.task, when)
    mtype = meeting_type(task) or "Founders Meeting"
    doc = NOTES_DOCS.get(mtype)
    print(f"Meeting: {task['name']} ({task['id']}), type {mtype}")

    t = transcribe(a.audio, key("assemblyai-api-token"))
    md = to_markdown(t, speakers, task["name"])
    mins = round(t.get("audio_duration", 0) / 60, 1)
    print(f"Transcribed {mins} min, {len(t.get('utterances', []))} turns, "
          f"about ${mins / 60 * 0.42:.2f} at 2 channels")

    if a.dry_run or not doc:
        print(md[:2000])
        return

    page = req("POST", f"workspaces/{WID}/docs/{doc}/pages",
               {"name": task["name"], "content": md, "content_format": "text/md"}, v=3)
    url = f"https://app.clickup.com/{WID}/v/dc/{doc}/{page['id']}"
    fields = {c["name"]: c["id"] for c in req("GET", f"list/{MEETINGS_LIST}/field")["fields"]}
    # Leave the meeting at Held: filling Notes Doc Link triggers the agent, which
    # appends the summary and then sets Notes Synced itself.
    if task["status"]["status"] in ("scheduled", "prep sent"):
        req("PUT", f"task/{task['id']}", {"status": "held"})
    req("POST", f"task/{task['id']}/field/{fields['Notes Doc Link']}", {"value": url})
    req("POST", f"task/{task['id']}/comment",
        {"comment_text": f"Transcript filed from a two-channel recording ({mins} min). {url}"})
    print("Filed:", url)


if __name__ == "__main__":
    main()
