---
name: validate-profile
description: Stages 6 and 7 of the synthesis procedure for a profile in profile-builds/. Must run in a fresh Claude Code session with no memory of the build, so the critique is independent.
---

# Validate profile

If this session has built or discussed this profile, stop and tell Brandon to start a new session (`/clear` or a new terminal). Independence is the point.

Stage 6, adversarial validation, against `05-tagged.md` and `01-corpus.md` only:
- Flag every claim not supported by the corpus.
- Flag credential inflation.
- Flag any decision rule that is generic rather than specific to this seat.
- Flag seam collisions with existing profiles in the manifest.
Write `06-validation.md` with each flag and the revision made. Produce `06-revised.md`.

Stage 7, behavioral test: run 3 to 5 representative tasks from the Sŏn training context with the revised profile loaded. Confirm it produces the diagnostic moves in its cue table and decision rules, not just the right tone. Write `07-behavioral-test.md`.

Then hand off to Brandon: the final file goes to Box through the Profile Update Protocol (upload to the right cluster folder, add the Replacement Queue row, add the registry row in the Master Pointer Index), and the manifest entry gets its `box_id` and `status: live`. Claude does not upload to Box without Brandon's go-ahead.
