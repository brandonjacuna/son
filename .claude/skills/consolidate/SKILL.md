---
name: consolidate
description: Merge raw research notes into the structured knowledge base. Run weekly or when research/raw has more than about ten unmerged notes.
model: sonnet
---
# Consolidate research into kb/

1. List files in `research/raw/` not yet referenced by any `kb/*.md` (check the `merged_from:` lines).
2. Group by trade: bar, kitchen, live-fire-ventilation, plumbing-water, electrical, lighting, av-network, hvac, materials, storage, codes, fabrication, equipment-landscape.
3. For each group, update `kb/<trade>.md`:
   - Add new facts as short bullets, each with a source link and date.
   - When a new fact contradicts an old one, keep both, mark the old one `superseded`, and say why.
   - Record the merged note filenames under `merged_from:` at the bottom.
4. Never delete raw notes. They are the audit trail.
5. Report: files merged, contradictions found, anything that should become a decision.
