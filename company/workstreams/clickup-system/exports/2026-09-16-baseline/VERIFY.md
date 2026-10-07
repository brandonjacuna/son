# Baseline export verification — 2026-09-16
Script: scripts/export_baseline.py (read-only REST; token from Keychain). Archived tasks checked separately: 0 in Punch List and Carryover Register.

| Set | Exported | Live check | Audit said | Verdict |
|---|---|---|---|---|
| Founding Punch List | 491 (418 subtasks), all with custom_fields; 371 have descriptions | ids unique | 491 | ✅ |
| Carryover Register | 125 | list task_count = 125 | 126 | ✅ matches live; 1 task gone since audit (not by Claude — no writes made) |
| Function → SaaS Map | 241 | — | 241 | ✅ |
| SaaS Catalog | 46 | — | 46 | ✅ |
| 11 Capture lists | 56 total (summary fidelity) | — | Ops Capture was 8, now 9 | ✅ |
| 8 key Docs | all 8 matched, markdown + raw JSON | 174 docs in workspace (index saved) | — | ✅ |

Correction to audit: Punch List `identified` = **255** tasks (not ~330): ~242 under the two Scaling People parents + 13 non-SP tasks (e.g. "Choose Plan for Box…", "ClickUp vs Notion", bank-account moves). The approved #4 rename identified→Inbox moves all 255.
Punch List status counts: identified 255 · complete 208 · ongoing 6 · in progress 6 · active queue 5 · meetings 5 · up next 4 · in review 2.
