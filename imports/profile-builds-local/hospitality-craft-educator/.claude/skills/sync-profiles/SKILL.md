---
name: sync-profiles
description: Pull the current specialist profiles from Box into profiles/cache/, checking the Profile Replacement Queue for updates. Run at the start of any session that uses profiles.
---

# Sync profiles

Box is canonical. The cache is a read-only convenience that git ignores.

1. Read `profiles/manifest.yaml`.
2. Using the Box connector, get each `live` profile's details (modified date) and compare against `profiles/cache/.synced.yaml` if it exists.
3. Read the Profile Replacement Queue (ClickUp doc `2ky45bmy-16833`, page `2ky45bmy-27093`). Any profile listed with status Pending must be re-pulled even if the date looks unchanged.
4. For each profile that is new, changed, or pending: fetch its content with the Box connector and write it to `profiles/cache/<slug>.md`, with a first line `<!-- READ-ONLY MIRROR of Box <box_id>, pulled <date>. Edit in Box, never here. -->`.
5. Update `profiles/cache/.synced.yaml` with slug, box_id, Box modified date, pulled date.
6. Report: pulled, unchanged, failed, and any manifest entry whose Box file could not be found.

If the session only needs one stage, pull only the profiles whose `stages` include it. Never edit a cached profile. Never commit the cache.
