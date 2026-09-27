# Profiles

`manifest.yaml` lists every profile this studio uses, with its Box ID, cluster, and the lifecycle stages it serves. Box holds the canonical files. `/sync-profiles` pulls read-only copies into `cache/`, which git ignores.

Never edit a profile here. Changes follow the Profile Update Protocol in the Master Pointer Index (ClickUp `2ky45bmy-16833`): replace the Box file, log the Replacement Queue row, refresh copies.

New profiles are built in `profile-builds/` and added to the manifest with `status: live` and a `box_id` once they are in Box.
