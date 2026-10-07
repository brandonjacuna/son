# Phase 1: Cleanup

## Goal
Nothing in the repo, Box, or ClickUp carries out-of-scope material or stale pointers into the work that follows. Every deletion is approved by Brandon first.

## Out-of-scope material (decisions 2026-10-07)
- Jun / June Shim (former chef partner), The Josephine, Sanctuary: erase from working context.
- Pullman: only a bio line in investor materials may stay. Remove anything carried in from the consulting work or opinions about it. The Box folder `10. AI Projects/Research/Pullman LnD Import` (400222760917) was an imported Claude project used as an L&D starting point: audit what came from it.
- Experiential guidelines: strip from canon; keep the PDF as a reference file in Box only. The Brand Guidelines design deck stays. Korean cultural tie-ins are removed from canon, but where the line falls (godwit, water deer letterform, Mandarin duck palette, persimmon-sumac-elderberry, the design system's Jaeyeonmi / Ma / Mahk frameworks) is Brandon's call after he sees the extraction.
- Airtable: retired everywhere. Figures come only from the Investor Review workbook in Box.
- Stale pointers: "Sŏn Home Folder" profile path, Replacement Queue, Master Pointer Index (2ky45bmy-16833), `/sync-profiles`, old repo names (son-build, son-nerve, son-learning-studio, son-operational-buildout), Mac-only token paths.

## Inputs
- `memory/audits/2026-10-07-readiness.md` (term counts and top files per workstream)
- Box inventory and ClickUp inventory (summarized in the claude.ai Project doc `claude/son-rebuild-plan.md` and below)

## Work
1. **Repo sweep (Sonnet agents, one per workstream).** For every hit of the terms above, classify: delete, rewrite, or keep (with the reason). Allowed keeps include: Pullman as a bio line, "Jun" as a month or in public data (inspection records), Korea as an equipment-import market, Airtable as a watched vendor in the tech digest. Record every keep in `memory/audits/cleanup-allowlist.md` so future sweeps skip it.
2. **Raw exports.** `company/workstreams/clickup-system/exports/` and `company/workstreams/operations/archive/` and `extraction/` hold most hits. Ask Brandon: delete the out-of-scope exports, or move all raw exports out of the working tree into an archive folder.
3. **Workstream CLAUDE.md files.** Rewrite stale routing in operations, learning-studio (except profile mechanics, which phase 3 replaces), nerve, build-out README. Point figures to the workbook, brand to the cleaned canon.
4. **Box (Brandon approves each batch).** Move the experiential guidelines PDF (2281626080747) to a Reference folder. Decide the Pullman LnD Import folder. Remove `_tmp_repr_part1_copy.md` (2421148304456). Move exhibit working files out of Profiles/Investment.
5. **ClickUp (Claude never deletes there; the guard blocks it).** Produce a list for Brandon of what to delete or archive: the "Event Co" section and Jun pages in "Claude Project Review" (2ky45bmy-16873), Jun meeting docs, Pullman legacy items, Josephine items. Retire the Master Pointer Index by replacing its contents with a pointer to this repo.
6. **Brand canon (show before cutting).** Extract the experiential sections and Korean cultural tie-ins from the ClickUp Brand Guidelines doc (2ky45bmy-15773: sections 06 spatial, 07 multi-sensory, 08 service choreography, the Ma / Yubaek-ui-mi page) and from the design system. Present them to Brandon section by section as pop-ups. Cut only what he marks.
7. **Investor materials check.** Confirm the 207 St. Elmo deck and the Investor Diligence White Paper mention Pullman only as a bio credential. Report; do not edit investor documents.
8. **Open question for Brandon:** is the V7 Business Strategies Notebook (ClickUp 2ky45bmy-11873) still canon? Several workstreams cite it.

## Done when
- A repo-wide grep of the terms returns only hits listed in `cleanup-allowlist.md`.
- Box and ClickUp changes are logged in `memory/audits/cleanup-log.md`, with Brandon's approval noted per batch.
- Brandon has marked the brand canon line, recorded in `memory/decisions.md`.

## Red team
Harsh for anything investor-facing or brand canon (blind agent checks that nothing in scope was missed and nothing in scope-but-allowed was cut). Standard for the rest.

## Session split
Session A: repo sweep and CLAUDE.md rewrites. Session B: Box and ClickUp lists, brand canon extraction and Brandon's pop-ups.
