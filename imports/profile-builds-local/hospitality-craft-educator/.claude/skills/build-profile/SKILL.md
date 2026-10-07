---
name: build-profile
description: Build a new specialist profile using stages 0 to 5 of the seven-stage synthesis procedure, working in profile-builds/<slug>/. Stages 6 and 7 run separately with /validate-profile in a fresh session on a different model. Full runbook in profile-builds/RUNBOOK.md.
---

# Build profile

Usage: `/build-profile <slug>`

Read first, every time:
1. The procedure from ClickUp (doc `2ky45bmy-16853`, page `2ky45bmy-27213`). It is the source of truth and may have changed.
2. `profile-builds/<slug>/00-frame.md`, including Brandon's answers to its open questions. If an open question that affects scope is unanswered, stop and ask. Workflows cannot take input mid-run, so every scope decision is settled before any workflow starts.
3. `profile-builds/<slug>/HEAD-START.md` if present. Head-start files are unvalidated input.
4. Two finished profiles from `profiles/cache/` for format and seam conventions: the Curriculum & Program Architect and the Hospitality Operations Realist. Also every profile named in the frame's seam table.
5. `canon/standing-rules.md` and the Brand Guidelines page the frame cites.

Stages, one file each in `profile-builds/<slug>/`:

- `01-corpus.md` Stage 1. 5 to 15 curated sources targeting the seat's judgment, not a survey. Each row: source, what judgment it grounds, verification status (verified at source this build, or held from established literature). Use `/deep-research` per research target in the frame, then curate. Record excluded sources and why.
- `02-elicit.md` Stage 2. Cue inventory (cue, indicates, source, judgment); decision requirements table (difficult judgment, why hard, cues, strategy, novice error); if-then rules; anti-patterns; mental models. Quote or cite the source for each row.
- `03-consolidate.md` Stage 3. Themes, deduplicated and named, each checked back against its sources. Unresolved tensions listed, not smoothed over.
- `04-draft.md` Stage 4. The typed XML template in the house profile format: role_anchor, scope, mental_models, cue_table, decision_rules, diagnostic_procedure, anti_patterns, worked_examples, outputs, uncertainty, interfaces, project_block, interaction_guide, source_manifest, reanchor.
- `05-tagged.md` Stage 5. Every claim tagged `[sourced: ...]`, `[inferred]`, or `[project: ...]`. The confabulation firewall.

Rules:
- Encode what the expert does, not who they are. No credential inflation.
- Every standing rule in `canon/standing-rules.md` baked into the project_block (customer terminology, no em dashes, declarative, sentence case, no daypart code names, brand facts defer to canon, figures from Airtable only, profanity spoken only).
- Never reconstruct a practice from Brandon's lineage. Flag it.
- Seams: every interface names the neighbor's Box file ID from `profiles/manifest.yaml`.
- Run `python scripts/lint.py profile-builds/<slug>` before finishing. Zero errors.

Stop after Stage 5. Commit: `PROFILE <slug> stages 1-5`. Tell Brandon to run `/validate-profile <slug>` in a new session on a different model.
