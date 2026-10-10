# T4: Sŏn-branded opening checklist dashboard (claude.ai artifact)

## Plan
Build a single-file artifact (React or HTML) for tracking opening tasks. Artifacts run in a sandbox: no outside network calls, limited storage, and no reliable persistence across sessions. That shapes the design.

## Constraints to settle first
1. **Data source.** Is the checklist content real (from ClickUp) or an editable template? The artifact cannot read ClickUp live. Options: (a) paste/import a list, (b) hardcoded starter set, (c) export/import as JSON. State clearly in the UI that the artifact is a working copy, not the source of truth; ClickUp stays canonical.
2. **Persistence.** Use the artifact storage API if available, else in-memory state with an export button. Do not use localStorage in an artifact if the environment blocks it.
3. **Brand assets.** I do not have the design-system tokens in this answer. Pull colors, fonts, and spacing from the Sŏn design system (`company/brand/design-system`) and define them once as CSS variables at the top of the file. Do not invent a palette or use hex literals scattered in components. Fonts that cannot load in the sandbox need a defined fallback stack.
4. **Phase lock.** Build-out work is locked to P0 (concept) until the lease is signed; checklist items for later phases should be shown as not yet available rather than as active tasks.

## Features (v1)
- Grouped checklist (by area or phase) with check, owner, due date, and notes.
- Progress per group and overall (count and bar with text alternative).
- Filter: all, open, done, mine; search.
- Add and edit item; export/import JSON.
- Item kinds can follow the ClickUp prefixes (ACTION, CONFIRM, DECIDE, and so on) if the team wants parity.

## Quality bar
Keyboard operable; visible focus; contrast 4.5:1; status never by color alone; loading, empty, and error states written; mobile layout; semantic list markup. Copy: "customer," no em dashes, declarative.

## Questions
1. Where does the list come from, and who edits it?
2. Which groups and which owners?
3. Needed on a phone at the site, or desktop only?
4. Is the dashboard internal (founders and team) only? It should not hold financial figures; those come only from the Investor Review workbook.

## Output
One file, tokens at the top, sample data labeled as sample.
