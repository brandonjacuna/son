# Fabrication handoff — espresso chiller station (Rev C)

For the fabricator/machinist. This file + the `drawings/` folder + `BOM.csv` are the working set;
`Design Package.md` is the engineering basis if a question goes deeper. System in one line:
espresso from an Eversys Enigma E'4s falls by gravity through two 316L chilling coils immersed in
a stock Penguin glycol chiller's tank, into a Fetco airpot — everything you make is stainless,
HDPE, or POM-C, food-contact, and CIP-cleanable.

## Drawings

| DWG | Sheet | You make | Reference only |
|---|---|---|---|
| D1 | Chilling coil (QTY 2 + spare stock) | ✓ wind + passivate | |
| D5 | Coil cassette lid (QTY 1) | ✓ CNC | |
| D6 | Dual-spout catch funnel (QTY 2) | ✓ CNC + polish | |
| D7 | Airpot bung, Fetco D041 (QTY 2) | ✓ CNC after measuring | |
| D8 | Station frame + under-bench installation | ✓ weld/fab + install | |
| D2 / D3 / D4 | Flow schematic / elevation / nitrogen system | | ✓ context |

## Parts manifest

| # | Part | DWG | Qty | Material + blank | Process | Critical | Finish | QC |
|---|---|---|---|---|---|---|---|---|
| P1 | Chilling coil | D1 | 2 (+spare stock) | 316L seamless 3/16 in OD × 0.035 in wall, ASTM A213 **annealed** (confirm on cert), cut 2.6 m each | wind on Ø72–75 mandrel; legs formed at fit-up (note 8) | ≥95 % bore retention, no kinks; Ø80 ±5 centerline; stack ≤100 | degrease → citric passivate A967 → neutral rinse | visual (no flats/wrinkles); leak-test 300 kPa |
| P2 | Coil cassette | D5 | 1 | HDPE 25 mm food grade (alt: 316 5 mm + stiffeners), ~440 × 240 blank | CNC; fit compression glands | **fit to Penguin rear-lid aperture** (their drawing first); glands seal; plate clears tank evaporator | deburr, break edges | gland leak-check 300 kPa with coil fitted; trial fit in tank |
| P3 | Catch funnel | D6 | 2 | 316 bar/plate | CNC; interior polish Ra ≤ 0.8 | spout openings on **measured pitch P**; neck falls continuously ≥15°; ~30 mL to overflow. Note: lid gas gallery is machined in the thickened rim band and closed by a flush 0.5 mm cover ring (tack/bond — weep-tight is sufficient at millibar blanket pressure); sign off this construction before cutting | passivate A967 | water flow test (no pooling); N2 gallery jet check |
| P4 | Airpot bung | D7 | 2 | POM-C (acetal) food grade + 316 dip tubes + food-grade silicone O-rings | CNC **after measuring neck ID N and pot depth on the physical Fetco** | O-ring grooves sized to measured N; dip tips 10 mm off pot bottom, 45° cut. Handle is an offset chord so the dip tubes pass beside it — check one-hand grip comfort at first article | deburr; polish sealing lands | seats + seals in the pot; hand-removable; gas tee holds 0.5 psi with vent capped |
| P5 | Station frame + bench | D8 | 1 | 40 × 40 × 3 SS (or powder steel) tube ~12 m; 304 sheet top 30 mm build-up; leveling feet | weld, level, sheet | bench top at **1000 mm**; hatch ≥ 420 × 420 over the chiller tank; zone dims per D8 | weld-clean | level ±2 mm; hatch cover lifts clear; Ø25 product holes drilled at **measured** head spacing |
| P6 | Purge stoppers | D4 (detail) | 2 | tapered food-grade silicone lab stopper + 1/4 in barb | drill + fit barb | seats in funnel mouth, self-seals ~0.3 psi | — | holds purge flow without lifting |
| P7 | Winding mandrel (shop aid) | D1 note 1 | 1 | Ø72–75 stub (3 in Sch 40 pipe drop) ~300 mm | — | — | — | — |

**Buy, don't make** (all sourced in `BOM.csv` with vendors): Penguin 2/3 HP Stainless XL chiller,
Swagelok 3/16 in compression fittings + bulkhead glands, 3-way diverter valves, the whole N2 gas
train, Fetco D041 airpots, PT100s + logger, CIP pump, silicone tubing, glycol.

## Measure-first campaign (one visit each — nothing below gets machined before its measurement)

**At the Eversys demo (with the coffee bench trial):** outlet-head spacing (module pitch, est.
~280 mm); spout-to-spout pitch **P** within one head; spout tip diameter; spout slide range;
drip-tray lip height + geometry for the funnel locating pins; recipe flow rate on a scale
(must be ≤ 1.7 g/s per module); one power-on rinse volume.
**From Penguin (phone/email before ordering):** rear-lid aperture drawing; tank interior dims;
evaporator position.
**On a Fetco D041 in hand:** neck ID **N**; internal depth (sets dip-tube length **L**).
**At the site:** water report (drives the treatment cartridge, Eversys spec); drain siphon
position; circuit for 208 V/30 A.

## Order of operations

1. Measurements above → freeze P, N, L, aperture, head spacing.
2. Order: chiller, tube, fittings, airpots, gas train, valves (BOM).
3. Make: coils (P1) → cassette (P2, trial-fit) → funnels (P3) → bungs (P4) → frame (P5).
4. Assemble on the frame; form coil legs at fit-up; leak-checks per QC column.
5. Commission per `Design Package.md` §13 (single-coil first, dye trace, setpoint walk, then
   both modules, then airpot + gas, then Freepour handoff).

## Rules that outrank convenience

- **Food contact:** 316, HDPE, POM-C, platinum/food silicone, PTFE only in the product path. No
  brass/copper anywhere coffee touches (gas-train brass upstream of the check valves is fine).
- **Passivate** every machined stainless product-path part (citric, ASTM A967).
- **The product path never rises** except the designed inverted-U at the cassette (D5) — check
  every run with a level at install.
- Tolerances: ±0.5 machined, ±2 fabricated unless a drawing says otherwise; coil form per D1's
  stated ranges (the ±0.5 default does *not* apply to hand-wound coil geometry).
- Placeholder dimensions are printed **orange** on the drawings and listed in each PARAMETERS
  box — they are not buildable numbers until replaced by measurements.
