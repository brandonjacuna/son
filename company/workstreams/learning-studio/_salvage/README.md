# Salvage: learning studio tooling (inert)

Copied 2026-10-07 from the retired clones in `imports/profile-builds-local/` (both clones held identical copies). Nothing here is registered or runs: the skills are not under `.claude/`, the workflow is not under `.github/`, and `mcp.json` is not `.mcp.json`.

- `skills/`: the 13 studio skills (`/identify`, `/ideate`, `/design-module`, `/draft-module`, `/review-module`, `/park-module`, `/bind`, `/render`, `/status`, `/refresh-capabilities`, `/build-profile`, `/validate-profile`, `/sync-profiles`).
- `settings.json`: the studio's permission allowlist.
- `lint.yml`: the studio's GitHub lint workflow.
- `mcp.json`: Box and ClickUp servers (Airtable removed; retired).

Phase 5 rebuilds the studio against the phase 3 profile system and decides what to register. Profile mechanics here (`/sync-profiles`, `/build-profile`, `/validate-profile`, Replacement Queue) are superseded by phase 3. Recover the full clones with `git show 644c585:imports/profile-builds-local/<path>`.
