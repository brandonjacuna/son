CONCEPT / NOT FOR CONSTRUCTION

# Verdict: not as asked. Both requests fail; both have a fix that keeps the bartender from walking.

Driving ids: C6, A5, C8, C3, R7, R11.

## 1. Glass rinsers in the drink rail: rejected (C6, A5)
- The scupper is the drained strip at the bartender's edge where finished drinks sit. A rinser there puts waste next to food prep (garnish, finished drinks). Ellis calls this a health code failure. For Austin it is `unverified` until `codes/register.yaml` carries the item (R11). Code family: Texas Food Establishment Rules (25 TAC 228, adopting the FDA Food Code) plus APH (Austin Public Health). Log it there.
- Fix: relocate the rinser to a drainboard with physical separation from the scupper. The walk concern is real (C3), so put the drainboard inside the station cockpit (everything one bartender reaches without stepping). The tool rinse is a dipper well (a small running-water well for spoons and tools); it is a different item from a glass rinser.
- A glasswasher at the bar also needs a decision: low-temperature (chemical sanitizing) versus high-temperature (about 180 F, needs a booster heater). Whether the bar glasswasher alone satisfies APH's three-compartment-sink-or-dishwasher rule is open; no seat asks APH, so it is a fork for Brandon (R10). Drain, venting, and electrical are `unknown`.

## 2. One big deep ice bin: rejected (C8)
- Deep bins are hard to reach and hard to empty. Use a shallower ice chest with dividers by ice type. Specialty ice (clear cubes, spheres) gets a freezer, since it needs the wrong temperature otherwise.
- Sizing follows the peak assumption (R2): ice volume tracks drinks per hour at the peak hour, not "to last the night." That input comes from the Investor Review workbook via the R3 method, which I cannot reach here. Volume is `unknown`.
- Source figures, `estimated` and not Sŏn specs: Perlick ice chests come 24, 30, 36, 42 in wide with dividers (M7). Chest depth, bin depth, and work height are `needs-book` blanks.
- Ice home also needs a restock path for the barback that avoids stations (C9).

## 3. Units go to equipment-librarian first (R7)
No rinser, drainboard, ice chest, freezer, or glasswasher enters a layout until `equipment-librarian` has an `equipment/*.yaml` record built from the current spec sheet. Until then every size and utility is `estimated`.

## Unknowns
- Code items: rinser separation; APH glasswasher rule; hand sink per well; floor sink reach for every drained unit. All `unverified`.
- Book topics for `book-ingest`: bin depth, scupper width, work surface height.
- Fork for Brandon: glasswasher type; the bar-to-kitchen path until kitchen-layout exists.
