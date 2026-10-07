# Stage 6: Ship (orchestrator and scripts)

1. Lint the master: `python3 .claude/skills/profile-build/scripts/profile_lint.py profiles/<cluster>/<slug>`. Zero errors.
2. Generate copies: `python3 .claude/skills/profile-build/scripts/ship.py profiles/<cluster>/<slug>`. It copies `agent.md` to `.claude/agents/<slug>.md` and `skill/` to `.claude/skills/<slug>/`, and fails if an existing generated copy was edited by hand (drift). Founder-only seats: skip this step until Brandon says where their agents live.
3. Measure: `python3 .claude/skills/profile-build/scripts/measure.py profiles/_builds/<slug> --master profiles/<cluster>/<slug> --log`. It totals the build folder, the per-call load (core, plus skill if any), and the reference size, and appends a row to `profiles/_builds/MEASUREMENTS.md`. Fill the token columns from `BUILD.md` (sum of worker usage lines, by stage) and the orchestrator's own context at this point (from `/context` where available; otherwise write "not measured").
4. Write `BUILD.md`'s closing block: mode, models per stage, flags accepted and rejected, test verdicts, model line and why, open items.
5. If the skill is a mode, add its row to `.claude/skills/REGISTRY.md` (one owner per trigger; resolve overlaps first).
6. Commit: `PROFILE <slug> <mode>: built, <n>/<n> tests pass`. The build folder stays until Brandon approves the seat; then delete everything in it except `BUILD.md`, `00-frame.md`, and `01-sources.md` (move those three into the master as `build/`).
7. Review routing: the master goes to Brandon for approval. Box mirror and Replacement Queue retirement belong to phase 3 step 6, not here.
