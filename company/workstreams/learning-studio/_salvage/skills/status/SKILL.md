---
name: status
description: Report the catalog by stage, catalog and module disagreements, open bindings by group, and modality variety.
---

# Status

Run, in order, and summarize in a few lines:

1. `python scripts/status.py`
2. `python scripts/status.py bindings`
3. `python scripts/status.py variety`
4. `python scripts/lint.py`

Lead with what is closest to parked and what is blocked on a single decision (a founder or chef binding that unblocks several modules at once).
