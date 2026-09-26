# son-nerve: Build Brief for the Weekly Industry Digest

This brief carries every decision made in planning. Read it fully before writing code. Turn the standing rules and IDs into this repo's CLAUDE.md in the first session.

## 1. What we are building

A system that delivers one weekly digest on the state of Austin's hospitality and F&B industry, by concept type and by area. It acts as Sŏn's nerve endings during the startup and build-out phase: very sensitive to change, showing how the economy affects the industry, our peers, and our future.

Sŏn is a Korean fine dining restaurant in build-out at 207 E St. Elmo Rd, Austin, TX. It has no operating data yet.

## 2. Standing rules

- **Free data only.** Paid services (Placer.ai, Advan, Second Measure, Black Box, Yelp paid tiers, CoStar, etc.) may be mentioned in an appendix but nothing depends on them.
- **No Airtable.** We have moved off it.
- **Storage:** analytical store in this repo (DuckDB / Parquet), dated archives in Box, human layer in ClickUp.
- **Out of scope:** the "Weekly Restaurant Tech Intelligence Digest" in ClickUp is a separate project. Do not read, modify, merge with, or plan around it.
- **Legitimate access only.** Official APIs, open data portals, RSS, and official Claude connectors (Resy, Tripadvisor) at human scale. No scraping of Google, Yelp, OpenTable, or Resy. No community OpenTable MCP servers. Never store Google ratings or review counts as a time series (Google terms); store only place IDs.
- **Writing rules for everything the digest produces:** no em dashes (use commas, colons, or restructure). Restaurant patrons are "customers," never "guests." Declarative, not aspirational: no "we believe," "we hope," "our goal is." Scope is Sŏn only; never name or plan for other portfolio concepts.
- **Never invent numbers.** Every figure in a digest comes from a pulled source with its period and release date. If a source fails, say so in the Data Health section rather than substituting.

## 3. Destinations (IDs)

**ClickUp** (space: Business Intelligence, `90136734098`)
- Folder: Industry Digest, `1400400000000888`
- Doc: Weekly Industry Digest, `2ky45bmy-20073`
  - Standing page "Index and Page Template," `2ky45bmy-33313`. Never overwrite it. It holds the 10-section template.
  - Each digest is a NEW page in this doc named `YYYY-MM-DD | Week of Mon D to Mon D` (date = delivery Monday).
- List: Watchlist: Entities, `1400400000001380` (one task per tracked venue or pipeline item). Custom fields not yet created; create them to match what the scripts write (entity ID, concept type, area, hub tier, status Pipeline / Open / At-risk / Closed, distance in miles, last signal, signal count).
- List: Signals, `1400400000001381` (Act and Alert items; anything new within 2 miles of 207 E St. Elmo Rd lands here the same day).
- If any new list or table is needed, it goes in the Industry Digest folder. Nothing goes in Founding Sŏn.

**Box**
- Parent: Sŏn → 10. AI Projects, folder ID `393201935562`.
- Create a subfolder "Industry Digest" with `/raw/`, `/digests/`, `/reference/`, `/data-health/`. Confirm with Brandon before creating.

## 4. Architecture

| Job | Runs as | Cadence | Does |
|---|---|---|---|
| R1 ingest-daily | Claude Code routine (this repo) | Daily, off the hour (e.g., 6:07 a.m. CT) | Pull TABC pending applications and licenses, Comptroller sales tax permits, Austin inspections and construction permits, news RSS. Diff vs yesterday. Write Parquet/DuckDB. Push same-day Signals for the St. Elmo radius |
| R2 ingest-releases | Claude Code routine | Weekly | Check and pull new releases: Mixed Beverage Gross Receipts, sales tax allocations, BLS/FRED, Dallas Fed TSSOS, AUS passengers, CPI, Census, EIA, TWC WARN. Store by vintage |
| R3 digest-build | Claude Code routine + ClickUp, Box connectors only | Weekly, Monday early morning | Run change detection, write the digest page to ClickUp, update Watchlist and Signals, archive to Box |
| C1 peer-pulse (Phase 2) | Cowork scheduled task, connectors only | Weekly | Resy and Tripadvisor checks for the peer set at fixed times, human scale; record only our own observations (none / few / many slots) |

Build and test everything locally first, then schedule as cloud routines. Cloud routines need a custom network environment allowlisting: data.texas.gov, data.austintexas.gov, api.bls.gov, api.stlouisfed.org, www.dallasfed.org, comptroller.texas.gov, www.flyaustin.com, api.census.gov, api.eia.gov, twc.texas.gov, plus RSS hosts. Keep the list short. Routine docs: https://code.claude.com/docs/en/routines. A green run status does not mean success: every script writes run_health.json, and the digest reads it.

Scope connectors per routine: R1 and R2 get none; R3 gets ClickUp and Box only.

## 5. Data sources, Phase 1

| Source | ID / endpoint | Use |
|---|---|---|
| TABC pending original license applications | data.texas.gov `mxm5-tdpj` | Strongest leading indicator of new competitors (daily) |
| TABC license information | data.texas.gov `7hf9-qc9f` | Status changes = closure evidence |
| Comptroller active sales tax permit holders | data.texas.gov `jrea-zgmq` | Openings via NAICS 7225xx / 722410 / 722330 / 311811 / 312120 and first sales date |
| Mixed Beverage Gross Receipts | data.texas.gov `naix-2893` | Best free venue-level revenue proxy (alcohol only, about 1 to 2 month lag, back-fills) |
| Austin food establishment inspections | data.austintexas.gov `ecmv-9xxi` | Openings (new facility_id), dormancy |
| Austin issued construction permits | data.austintexas.gov `3syk-w9eu` | Restaurant finish-outs and change of use, 3 to 12 months ahead |
| BLS CES / FRED | e.g., FRED `AUSLEIHA175MFRBDAL` | Austin MSA leisure and hospitality jobs |
| Dallas Fed Texas Service Sector Outlook | dallasfed.org/research/surveys/tssos | Revenue, prices, wages, outlook |
| Comptroller local sales tax allocations | comptroller.texas.gov | City-level spending |
| AUS passenger traffic | flyaustin.com monthly releases | Tourism demand |

Verify every dataset ID, field name, and update cadence against the live portal before building on it.

## 6. Area model: hubs vs off-hub (Brandon's structure)

The digest must compare the health of the main restaurant hubs and their sub-sections against off-hub neighborhoods.

**Hubs (draft boundaries, confirm each with Brandon before encoding):**
- **Downtown.** Draft: Lady Bird Lake to MLK, Lamar to I-35. Open question: do Rainey Street and the 2nd Street / Warehouse districts count as Downtown or as their own sub-sections?
- **South Congress.** Draft: Congress Ave corridor, river to Oltorf, a few blocks either side.
- **South Lamar.** Draft: Lamar corridor, Barton Springs Rd to Ben White, a few blocks either side.
- **East Austin**, with sub-sections:
  - **Holly / East Cesar Chavez.** Draft: south of 5th St to the river, I-35 to Pleasant Valley.
  - **East 6th / 7th.** Draft: the 5th to 7th St corridors, I-35 to Pleasant Valley.
  - **East 12th and north ("12th+").** Draft: 11th and 12th St corridors northward (confirm whether Manor Rd belongs here).

**Off-hub:** everything else, grouped into neighborhood clusters built from City of Austin neighborhood planning areas (free GIS), plus suburban groups (Round Rock / Georgetown, Cedar Park / Leander, Pflugerville / Manor, Westlake / Lakeway, Hays County).

**Home zone overlay:** 1-mile and 2-mile radius around 207 E St. Elmo Rd, reported by name every week regardless of hub.

Encode hubs as GeoJSON polygons in `/config/areas.geojson`, assign every entity by point-in-polygon, and keep zip code as a fallback level. Report metrics at three tiers: hub, sub-section, off-hub cluster, with hub-vs-off-hub comparisons in the digest.

## 7. Peer set (main list)

Build a ranked list of 30 to 40 peers from recent acclaim, then have Brandon approve it.

**Sources to pull (most recent editions):** Michelin Guide Texas (and check whether a 2026 edition has been announced), James Beard 2026 semifinalists, finalists, and winners (Austin), Eater Austin Essential 38, Austin American-Statesman annual dining guide (Matthew Odam), Texas Monthly best new restaurants, Resy Hit List Austin, CultureMap Tastemaker Awards, national lists (NYT, Food & Wine, Bon Appétit, Esquire).

**Selection rule:** score each restaurant by how many lists it appears on (Michelin stars and James Beard weighted highest), then make sure each hub and major concept type has representation. Tag each with concept type, hub, and sources.

**Verified seed from Michelin Guide Texas 2025 (October 29, 2025 ceremony):**
- One Star (Austin): Barley Swine, Craft Omakase, Hestia, InterStellar BBQ, La Barbecue, LeRoy and Lewis BBQ, Olamaie. Note: Olamaie closed July 19, 2026. Keep it as a historical closure case for backtesting the closure-detection rules, not as a live peer.
- Green Star: Dai Due, Emmer & Rye, Nixta Taqueria.
- New Bib Gourmand: Mercado Sin Nombre, Parish Barbecue (pull the full Austin Bib list).
- Recommended: Apt 115, Birdie's, Comedor, Discada, Este, Ezov, Fabrik, Garrison, Jeffrey's, Joe's Bakery & Coffee Shop, La Condesa, Launderette, Le Calamar, Lenoir, Ling Kitchen, Lutie's, Maie Day, Mexta, Mum Foods Smokehouse & Delicatessen, Pasta|Bar Austin, Poeta, Siti, Suerte, Tare, Terry Black's BBQ, Toshokan.

Birdie's note: walk-in first with limited OpenTable reservations, so reservation signals understate it; rely on receipts and review velocity.

## 8. Korean micro-watch (separate sub-section)

Korean concepts will not crack an acclaim-based list, so this is a full sweep, not a curated list:
- Find every Korean concept in the metro by scanning TABC, sales tax permit, and inspection records for Korean names and terms (Korean, Seoul, Hansik, KBBQ, bibimbap, galbi, soju, pocha, banchan, kimchi, and similar), then confirm matches with Brandon.
- Track openings, closings, receipts trends, and pipeline for the whole genre, plus an "Asian chef-driven" adjacent tier (e.g., Craft Omakase, Ling Kitchen, Toshokan, Tare).
- Give it its own digest section even when nothing changed that week.

## 9. Change detection

- Compare YoY and 3-month rolling YoY (handles SXSW, ACL, F1, UT football, summer heat). Keep an event calendar in `/config/events.csv`; flag calendar shifts instead of reporting false swings.
- Robust z-score per cell against its own 24-month history (median and MAD).
- Tiers: Watch (|z| ≥ 2, or any new event in the St. Elmo radius), Alert (|z| ≥ 2.5 sustained two periods or confirmed by a second source), Act (peer set or 1-mile radius, two sources, or a macro threshold crossed).
- Report breadth (share of venues up YoY) with every total; minimum 8 venues per cell or roll up.
- Every metric carries period covered, release date, staleness. Exclude the latest one to two receipts months from YoY until at least 90% of last year's reporters have filed.
- Openings and closings are inferred from multiple sources, never one.

## 10. Phases

- **Phase 0:** repo scaffold, CLAUDE.md, keys, config files (taxonomy, areas, peers, events), local test pulls of every Phase 1 source.
- **Phase 1:** R1, R2, R3 producing digest sections 1, 2, 3, 6, 9, 10; Korean sweep; hub assignment.
- **Phase 2:** area heatmap and concept scorecard with robust z and breadth; C1 peer-pulse; news RSS; remaining macro series.
- **Phase 3:** backtest thresholds on 2023 to 2026 history (use Olamaie), QCEW, hardening.
- **Phase 4 (at opening):** add Sŏn's own POS and reservation data as the "Us" layer.

## 11. First session: do these in order

1. Create CLAUDE.md from sections 2 and 3 of this brief.
2. Scaffold the repo: `/scripts`, `/config`, `/data`, `/tests`, `.env.example` (no secrets committed).
3. Confirm API keys are present; run a test pull of each Phase 1 source and report row counts, fields, and freshness.
4. Draft `/config/areas.geojson` from the hub definitions above and show Brandon a map for approval.
5. Draft the peer list from the sources in section 7 and present it for approval.
6. Run the Korean sweep against the pulled data and present candidate matches.
7. Stop and review with Brandon before creating any routines.
