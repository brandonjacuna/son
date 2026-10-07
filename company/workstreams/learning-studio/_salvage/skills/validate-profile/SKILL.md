---
name: validate-profile
description: Stages 6 and 7 of the synthesis procedure for a profile in profile-builds/. Must run in a fresh Claude Code session, on a different model from the one that built the profile, so the critique is independent. Full runbook in profile-builds/RUNBOOK.md.
---

# Validate profile

Usage: `/validate-profile <slug>`

Independence check first. If this session built or discussed this profile, stop and tell Brandon to open a new session. The procedure calls for a separate model or a fresh session; do both. If the session model is the one that built the profile (see the commit or `05-tagged.md` header), say so and recommend switching.

Inputs, and only these: `05-tagged.md`, `01-corpus.md`, `00-frame.md`, `canon/standing-rules.md`, and the seam profiles named in the frame (from `profiles/cache/`). Do not read `02` to `04`; the critique judges the output against its grounding.

Stage 6, adversarial validation. Run it as a workflow (include the keyword `ultracode` in the prompt) so each check fans out to independent agents that verify each other:
- Every `[sourced]` claim: is it supported by the cited corpus item? Fetch the source where possible.
- Credential inflation anywhere.
- Every decision rule and cue: specific to this seat, or generic advice any trainer would give?
- Seam collisions with each neighbor profile.
- Standing-rule violations.
Write `06-validation.md`: each flag, the evidence, the revision made. Write `06-revised.md`: the full revised profile.

Stage 7, behavioral test. Load `06-revised.md` as the working profile. Run 3 to 5 representative tasks from the Sŏn training context (the frame lists candidates; add your own). For each: the task, the output, and whether it produced the diagnostic moves in the cue table and decision rules, not just the right tone. Revise `06-revised.md` if a test fails and rerun that test. Write `07-behavioral-test.md`.

Finish: `python scripts/lint.py profile-builds/<slug>` with zero errors. Commit: `PROFILE <slug> validated`. Do not upload to Box. The profile returns to Brandon's claude.ai session for the Box upload and registry update.
