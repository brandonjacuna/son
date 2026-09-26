# son-nerve

Weekly digest on the state of Austin's hospitality and F&B industry, by concept type and by area, built for Sŏn (Korean fine dining, in build-out at 207 E St. Elmo Rd, Austin, TX; no operating data yet). `BRIEF.md` is the full build brief; read it before starting new work.

## Standing rules

- **Free data only.** Paid services (Placer.ai, Advan, Second Measure, Black Box, Yelp paid tiers, CoStar, etc.) may be mentioned in an appendix, but nothing depends on them.
- **No Airtable.** We have moved off it.
- **Storage:** analytical store in this repo (DuckDB / Parquet), dated archives in Box, human layer in ClickUp.
- **Out of scope:** the "Weekly Restaurant Tech Intelligence Digest" in ClickUp is a separate project. Do not read, modify, merge with, or plan around it.
- **Legitimate access only.** Official APIs, open data portals, RSS, and official Claude connectors (Resy, Tripadvisor) at human scale.
  - No scraping of Google, Yelp, OpenTable, or Resy. No community OpenTable MCP servers.
  - Never store Google ratings or review counts as a time series (Google terms). Store only place IDs.
- **Writing rules for everything the digest produces:**
  - No em dashes. Use commas, colons, or restructure the sentence.
  - Restaurant patrons are "customers," never "guests."
  - Declarative, not aspirational: no "we believe," "we hope," "our goal is."
  - Scope is Sŏn only. Never name or plan for other portfolio concepts.
- **Never invent numbers.** Every figure in a digest comes from a pulled source, with its period and release date. If a source fails, say so in the Data Health section rather than substituting.
- **Secrets:** API keys live in `.env` (gitignored). Only `.env.example` with empty values is committed. Never commit a key, and never print one in logs or `run_health.json`.
- **Run health:** a green routine status does not mean success. Every script writes `run_health.json`, and the digest reads it.

## Destinations

### ClickUp (space: Business Intelligence, `90136734098`)

| Item | ID | Notes |
|---|---|---|
| Folder: Industry Digest | `1400400000000888` | Any new list or table goes here. Nothing goes in Founding Sŏn. |
| Doc: Weekly Industry Digest | `2ky45bmy-20073` | Each digest is a NEW page named `YYYY-MM-DD \| Week of Mon D to Mon D` (date = delivery Monday). |
| Page: Index and Page Template | `2ky45bmy-33313` | Standing page with the 10-section template. **Never overwrite it.** |
| List: Watchlist: Entities | `1400400000001380` | One task per tracked venue or pipeline item. Custom fields (to be created to match what scripts write): entity ID, concept type, area, hub tier, status (Pipeline / Open / At-risk / Closed), distance in miles, last signal, signal count. |
| List: Signals | `1400400000001381` | Act and Alert items. Anything new within 2 miles of 207 E St. Elmo Rd lands here the same day. |

### Box

- Parent: Sŏn → 10. AI Projects, folder ID `393201935562`.
- Industry Digest `421598750339` (created 2026-09-26): `01. Digests` `421603412611`, `02. Raw` `421598977707`, `03. Reference` `421597286002`, `04. Data Health` `421598632583`.
- Follow `Sŏn/00. Start Here/Start Here.md`: two-digit prefixes, ISO dates in file names, v1/v2 versions, "DRAFT " prefix for working files, "FINAL" only for frozen items. Box holds frozen digests and review artifacts; living docs stay in ClickUp.

## Repo layout

- `scripts/`: ingest and probe scripts.
  - `test_pull.py` probes every Phase 1 source and writes `data/test_pulls/run_health.json`.
  - `build_areas.py` rebuilds `config/areas.geojson` from City of Austin GIS. Change the rules in the script, never hand-edit the GeoJSON.
  - `areas.py` (`Areas().assign(lon, lat, city, zip)`) and `geocode.py` (offline, street centerlines) assign venues to hub, sub-section, off-hub cluster, and home-zone distance.
  - `korean_sweep.py` writes `data/korean_sweep/candidates.csv` for Brandon to confirm.
  - `venue_evidence.py <csv>` adds the latest alcohol receipts and inspection per venue (address and name match).
  - `assign_areas.py <csv>` adds area columns to any venue CSV (e.g. `config/peers_draft.csv`).
- `config/`: taxonomy, `areas.geojson`, peers, `events.csv` (drafted in later steps, each approved by Brandon).
- `data/`: DuckDB / Parquet store. `data/test_pulls/` and `data/geo_cache/` are scratch and gitignored.
- Geocoding: nominatim, Overpass, and the Census geocoder are blocked by the network policy; use `geocode.py`.
- `tests/`: offline unit tests (`pytest`), no network.

## Commands

```sh
pip install -r requirements.txt
cp .env.example .env        # then fill in keys locally
python scripts/test_pull.py # probe every Phase 1 source
python scripts/build_areas.py [--refresh]   # rebuild areas.geojson
python scripts/korean_sweep.py
pytest -q
```

## Network

This environment has full network access (Brandon, 2026-09-26). If routines move to a restricted environment, allowlist: data.texas.gov, data.austintexas.gov, api.bls.gov, api.stlouisfed.org, www.dallasfed.org, comptroller.texas.gov, www.flyaustin.com, austin.widen.net, api.census.gov, api.eia.gov, twc.texas.gov, plus RSS hosts. Keep the list short. Connectors per routine: R1 and R2 get none; R3 gets ClickUp and Box only.

## Decisions (Brandon, 2026-09-26)

- Schedule: R1 daily 6:07 a.m. Central; the Monday digest lands in ClickUp by 8:00 a.m. Central.
- Scope: Travis, Williamson, Hays (per the ClickUp Index and Page Template). Bastrop / Elgin is grouped but excluded from metro totals. Suburb and ZIP fallbacks approved.
- Hubs: Downtown, Rainey Street, 2nd Street / Warehouse, South Congress, South Lamar (Lamar Blvd plus S 1st St), East Austin (Holly / East Cesar Chavez, East 6th / 7th, East 12th and north, Manor Road). Off-hub clusters and fallbacks are still drafts.
- Peers (`config/peers_draft.csv`): open concepts only, and every Emmer & Rye Hospitality Group concept. Closed venues go to `config/closure_cases.csv` for backtesting.
- Korean: Oseyo is the only direct comp (`config/korean_watch.json`). Every other Korean concept is awareness only.
