# Prototype snapshot: "Founders Meeting Assistant" (Brandon's Super Agent test)
Captured 2026-09-16 from the Founding Punch List (read-only).

## Structure it produced
- Series parent task per month ("Weekly Founders Sync – 2026-09", "Founders Thursday Standup – 2026-09"), task type Meeting, status "meetings"
- One child per occurrence: "<Meeting> Agenda YYYY-MM-DD", assigned to both founders, due date = meeting time
- Stores the Google Calendar event instance ID + series link in the description; "Timing source of truth: Google Calendar"
- Handled a reschedule (Tue 9/15 → Wed 9/16) and rewrote the text; recreated the Thursday GCal series; resets prep reminders
- Remote link in use: **Zoom** (not Meet)
- Pulled the "summary from last standup" in, but AI Notetaker notes were missing, so it created no action items

## Evidence this matters for the blueprint
- The Super Agent evidently DID read/write Google Calendar (series recreation, instance IDs). Verify which tool it used.
- Weekly Founders Sync block shown as 11:00–2:00 pm CDT (Brandon's brief said 11–1). Confirm.

Task refs: 86akfkagr (Sync 09-16), 86akgw0zn (Standup 09-17), parents 86akfka82, 86akgez3c, 86ake5ud3
