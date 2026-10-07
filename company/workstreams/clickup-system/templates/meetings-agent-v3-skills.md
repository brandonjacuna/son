# Meetings Agent v3 — skills to build

Three skills, all for things a founder asks for in chat. Everything automation-driven (roll-forward, notes, close-out, date sync) stays in the jobs and automation instruction boxes, so no procedure exists in two places.

---

## Skill 1 — Schedule an investor meeting

Use when a founder asks to schedule a meeting with an investor or lender.

1. Ask for anything missing: investor name, date, start time, length (default 45 minutes), and the investor's email.
2. Create a task in the Meetings list named "Investor/Lender — <Investor name> — YYYY-MM-DD" with only that name and Meeting Type = Investor/Lender.
3. Wait until the Automation has applied the template (the description is no longer empty). If it has not after a few minutes, say so and stop.
4. Set status Scheduled, start and due dates, Attendees, and Capture Source = AI Notetaker.
5. Create the event on the "Sŏn Meetings" calendar, titled exactly like the task, with a Google Meet link, inviting dominic@son.restaurant and the investor. Do not invite Brandon.
6. Write the event ID into GCal Event ID and the title into Event Title.
7. If the investor has a record in the Investor CRM, link it through the meeting's Related Meetings field, and set that record's Last Contact to the meeting date.
8. Reply with the task link, the event time and who was invited.

---

## Skill 2 — Make a meeting remote or in person

Use when a founder says a specific meeting is now remote, or now in person.

**Remote:** add a Google Meet link to that meeting's existing event (never delete and recreate it), set Capture Source = AI Notetaker, and reply with the Meet link. The AI Notetaker will then attend.

**In person:** you cannot remove a Meet link from an existing event. Reply saying so, and ask the founder to delete the event. Once they confirm it is gone, rebuild it on "Sŏn Meetings" with the same title, time and guests and no Meet link, set Capture Source = Wispr Flow, and update GCal Event ID and Event Title on the task.

---

## Skill 3 — File a transcript I give you

Use when a founder pastes or points you at a transcript or notes for a meeting that is not covered by AI Notetaker or Wispr Flow (for example an Apple recording).

1. Identify which meeting it belongs to, by date and type. If it is ambiguous, ask.
2. Write it into the matching notes Doc ("Founders Meeting Notes", "Founders Standup Notes" or "Investor & Lender Meeting Notes") as a page named after the meeting. Keep the content as given; do not summarise unless asked.
3. Set Notes Doc Link on the meeting task and set the status to Notes Synced.
4. Reply with the page link. Change nothing else on the task.
