Paste everything below the line into the first Claude Code session that has the build-out files in place (cloud is fine). Paths are relative to the build-out root, `company/workstreams/build-out/`.

---

You are starting the Sŏn construction-mode workspace. Read the build-out `CLAUDE.md`, `PHASE.yaml`, `decisions/0001-architecture.md`, and `HANDOFF.md` first. We are in P0 concept; no lease is signed.

Do these in order. Stop and ask me (one AskUserQuestion at a time, each with enough context to answer on its own) whenever something is unclear. Keep each report short.

1. **Health check.** Confirm the session-start banner fired and shows the build-out phase. Tell me whether this is a cloud or local session. Run `python3 scripts/validate_equipment.py` and `python3 -c "import build123d, ifcopenshell, ezdxf"`. Report pass or fail only.
2. **Guard test.** Try to create `phases/P1-design/test.md`. It should be blocked. Then try to edit `PHASE.yaml`. It should be blocked. Report both results. Do not try to work around the blocks.
3. **Capture list IDs.** Using the ClickUp connector (read only), find the Product Capture and Technology Capture lists. Show me the list names and IDs, then ask me before adding them to `clickup/allowlist.yaml`.
4. **Seed the knowledge base.** Read only, from the ClickUp doc "Claude Project Review" (doc 2ky45bmy-16873). Import ONLY these pages, all under the "Sŏn Home Base" parent page (2ky45bmy-27433):
   - 2ky45bmy-27473 solid-fuel exhaust ventilation
   - 2ky45bmy-27513 fire suppression and fire alarm
   - 2ky45bmy-27533 and 2ky45bmy-27553 plumbing, grease interceptor, roof penetrations (two pages with the same title: diff them, keep one, tell me which)
   - 2ky45bmy-27573 flooring
   - 2ky45bmy-27593 HVAC distribution, walk-in cooler, acoustics
   - 2ky45bmy-27613 electrical, low-voltage, tunable lighting, audio
   - 2ky45bmy-27633 outdoor BBQ pit compliance and operations
   - 2ky45bmy-27653 bar millwork, masonry, budget
   Import only the pages listed above. Read no other page of that doc.
   For each page: save a paraphrased note to `research/raw/YYYY-MM-DD-<slug>.md` with a source line (doc and page ID). Use neutral file names and titles with no cuisine or cultural descriptors. Keep code and technical facts; drop cultural framing. Do not carry any dollar figures: replace them with "[figure removed: budget numbers come only from the current Investor Review workbook]". Then run the `consolidate` skill to create the first `kb/` files. Flag anything that conflicts with `codes/register.yaml` (Austin uses UPC/UMC, not IPC/IMC; Austin adopted the 2024 codes effective July 10, 2025, so older guides may cite superseded editions).
5. **Box folder.** Using the Box connector, check `Sŏn / 04. Property and Build-Out` (folder 420132927884). Propose the subfolder structure from `decisions/open.md` #2 and ask me before creating anything.
6. **First real work.** Start a sandbox with `/sandbox bar-concept`. Read `kb/bar/tobin-ellis/` first. Then run the `interview` skill to capture my bar equipment list and how I want the front bar and back bar laid out. After the interview, create `equipment/*.yaml` records for each item using the `equipment-record` skill, starting with the ones I mark as locked in. Score the concept against `kb/bar/tobin-ellis/son-bar-review-checklist.md`.
7. Commit on the sandbox branch and give me a five-line summary: what exists, what is blocked on me, and the next three steps.

Rules for this session: Sonnet is the default. Use Haiku subagents for extraction. Do not use /deep. No em dashes. Patrons are "customers."
