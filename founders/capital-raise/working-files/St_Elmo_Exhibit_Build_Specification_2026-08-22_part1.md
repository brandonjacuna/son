# St. Elmo investor exhibit workbook, build specification

Part 1 of 2. Companion: `St_Elmo_Exhibit_Build_Specification_2026-08-22_part2.md`.

Version 1.2, revised 22 August 2026. Supersedes versions 1.0 and 1.1 of the same date.
Authored by the Investor Financial Exhibit Architect seat, generate mode.

Source of every figure: St. Elmo Dashboard V2 (Airtable, base `appKHeje63inr1fLG`), read live
22 August 2026. Brand values from Sŏn Brand Guidelines v1.0 (Box file `2356731001214`).
No figure in this specification was carried from memory or from a deck.

**This document stands alone.** A Claude Code session with no memory of this work can build from it
without asking a question. Every open item from earlier versions is now decided. Two pieces of copy
are deliberate bracketed placeholders and are identified as such.

**Changes in version 1.2:**
Pre-opening burden corrected to the per-position figure at section 5.9. Ramp lever reduced to two
curves at section 12 and Part 2 section 8. Cushion resolved to Lean default with Full alongside at
section 7. Two copy placeholders added at section 6. Status colors and font recorded as decided
departures rather than open items. All open items from version 1.1 closed except the two carried in
Part 2 section 17, both of which are routed rather than blocking.

**Corrected in place, 22 August 2026, after initial upload.** Section 12 Zone 2 carried a
typed-constant alternative for the ramp factor. It now carries the derived version only. Section 5.11
gains a line stating that the six-decimal factors there are display values rather than entries. Both
parts remain version 1.2 as a set: the number is unchanged because Part 2 already carried the
corrected instruction at its section 0.1, and this edit brings Part 1 into line with it rather than
moving the specification forward.

---

## 1. What is being built

Three release artifacts:

| Artifact | File | Purpose |
| --- | --- | --- |
| Master | `Son_Investor_Exhibit_v1.0_2026-08-22.xlsx` | Read-only. The canonical figures. |
| Sandbox | `Son_Investor_Exhibit_SANDBOX_v1.0_2026-08-22.xlsx` | The reader may break this one. |
| PDF | `Son_Investor_Exhibit_v1.0_2026-08-22.pdf` | Exhibit sheets only, brand typography. |

One Excel workbook holds the exhibit package and the interactive scenario instrument. The sandbox is
a copy of the master with the lever cells unlocked. They are not two builds. Build the master, then
derive the sandbox by the procedure in Part 2, section 13.

### 1.1 Locked constraints

Settled. Do not reopen during build.

- Excel-native. No Google Sheets twin. No macros. No VBA.
- Excel 2016 formula floor. INDEX and MATCH, never XLOOKUP, LET or LAMBDA. Also excluded at this
  floor: IFS, SWITCH, TEXTJOIN, MAXIFS, MINIFS, CONCAT, dynamic arrays and any spill behavior.
- Data tables, Goal Seek, cell protection and conditional formatting are in play, subject to the
  library constraints at 1.3. Scenario Manager is not used; see 1.3B.
- Three layers, each complete alone: headline, drivers, assumption register. Layer three never
  contradicts layer one.
- Brand hex carries identity in the workbook. Brand typography lives in the PDF only. Workbook fonts
  limited to the cross-platform safe set.
- Reading order is designed. Sequence is argument.
- Locked everywhere except designated inputs. Inputs visually distinct, bounded by validation,
  failing visibly rather than silently.
- Read-only master plus an explicit sandbox copy.
- Fully gated. Released only after a live meeting.
- Shows the business, not the deal. No returns, no waterfall, no IRR.
- Operating levers only. No capital levers.

### 1.2 Two constraints that override the architect profile

The profile this seat runs on carries two rules that the locked constraints reverse. Both reversals
are deliberate. Build to the constraints.

1. **Cross-platform dialect.** The profile requires the workbook to open cleanly in Google Sheets and
   gates release on an Excel to Sheets to Excel round-trip. Sheets is out of scope, so that test is
   not a release gate. What-If data tables, which the profile bans on cross-platform grounds, are
   permitted. The Excel 2016 function floor still applies and is the real constraint, so the
   practical formula dialect is unchanged.
2. **Returns sheet.** The profile's canonical sequence includes a returns and distributions sheet
   carrying a subordinated IRR. That sheet does not exist here. See section 3.

### 1.3 Python build constraints, researched 22 August 2026

The workbook is built programmatically. These findings change the design, not only the
implementation. Read all four before writing code.

**Library selection: openpyxl, not xlsxwriter.** xlsxwriter cannot create What-If data tables. Its
`add_table` builds an Excel ListObject, a formatted range, which is a different feature that shares
the name. xlsxwriter also cannot read or modify an existing file, so the sandbox derivation at Part 2
section 13 would require rebuilding from scratch rather than copying. openpyxl does both.

**A. Native What-If data tables can be written, and they are live.**

openpyxl exposes `openpyxl.worksheet.formula.DataTableFormula`. It emits the same XML Excel writes:
`<f t="dataTable" ref="F4:M11" dt2D="1" dtr="1" r1="C3" r2="C4"/>`. A reader who changes an input
sees the grid recalculate, because the object is a real data table and not a picture of one.

```python
from openpyxl.worksheet.formula import DataTableFormula
ws['F4'] = DataTableFormula(ref="F4:M11", dt2D=True, dtr=True, r1="C3", r2="C4")
```

Arguments: `ref` is the full grid including the result formula cell corner. `dt2D=True` for a
two-variable table. `dtr=True` sets row-input orientation. `r1` is the row input cell, `r2` the
column input cell. For a one-variable table, set `dt2D=False` and supply only the relevant input.

Sources: openpyxl 3.1 documentation, "Simple Formulae", which states support for data table formulae
with a complete implementation; and a verified practitioner walkthrough that traced the OOXML and
confirmed the round trip (`https://evrim.zone/blog/projects/what_if_in_python`). The documentation is
thin and easy to misread, because "data table" in OOXML more often means a formatted range. The class
above is the correct one.

**B. Scenario Manager cannot be written programmatically. Nothing is lost.**

The OOXML `<scenarios>` and `<scenario>` elements exist in the ISO 29500 specification, but openpyxl
exposes no API to create them. `SheetProtection` carries a `scenarios` flag that protects scenarios
where they exist; it does not create them. Commercial libraries in other languages advertise scenario
authoring as a differentiating feature, which corroborates the absence in the open-source Python
stack.

**The replacement is the dropdown plus INDEX switch at sheet 06, and it is better for this
workbook.** Scenario Manager scenarios live behind a dialog under the Data menu. A reader who never
opens that menu never learns the scenarios exist, and a workbook whose scenario switching is
invisible fails the no-narrator test at Part 2 section 16. The dropdown is on the sheet, in the
reading path, with the mechanism description beside it.

**C. Protection survives the write, and protection plus validation coexist.**

`ws.protection.sheet = True` combined with `cell.protection = Protection(locked=False)` on the input
cells produces the intended locked and unlocked ranges in desktop Excel. All cells default to locked,
so the pattern is: enable sheet protection, then unlock the exceptions.

```python
from openpyxl.styles import Protection
ws.protection.sheet = True          # no password argument
ws['C11'].protection = Protection(locked=False)
```

Sheet protection may be enabled with or without a password. Without one, a reader can unprotect
without being challenged, which is exactly the intent at Part 2 section 12.1. Source: openpyxl
"Protection" documentation, which states that if no password is specified users can disable
configured sheet protection without specifying one.

Data validation is written through `openpyxl.worksheet.datavalidation.DataValidation` and is
independent of protection. No interaction problem between the two was found. The known limitation is
the same one Excel has natively: **validation does not fire on paste.** Check 15 at Part 2 section 7
exists to catch a pasted out-of-range value and is not optional.

One caution: cell protection is a style attribute. Assigning `cell.protection` after applying a named
style can be overwritten by a later style assignment. Set protection last, after all formatting, on
every input cell.

**D. openpyxl never evaluates formulas, and this is the most consequential finding.**

openpyxl writes formula text with no cached result. Every formula cell ships with no `<v>` value.
Four consequences, all of which change the build:

1. **Set `wb.calculation.fullCalcOnLoad = True`.** This is
   `openpyxl.workbook.properties.CalcProperties`, whose signature carries `fullCalcOnLoad` and
   defaults it to True. Set it explicitly rather than relying on the default, and verify it appears
   in the written XML. Without a full recalculation on load, a reader may open the file to empty or
   zero cells.
2. **The build cannot verify itself in Python.** Reading the file back with openpyxl returns
   formulas, not values. `data_only=True` returns `None`, because there is no cache to read. The
   check suite at Part 2 section 7 therefore cannot be confirmed by the build script. It must be
   confirmed by opening the file once in Excel, or by a headless LibreOffice recalculation pass.
   **This is release gate 1.** A build that reports success without this step has verified nothing.
3. **Any figure this specification states as an expected output is a target for the recalculation
   step, not something the build script can assert.** Write the formulas, open once, confirm the
   numbers match section 5, then save from Excel so the release copy carries cached values.
4. **The data table cells also have no cached values** and populate on the same recalculation.

**Recommended build pipeline, given D:**

```
openpyxl writes structure, formulas, formats, validation, protection
  -> open once in Excel (or LibreOffice headless) to recalculate
  -> verify every figure against Part 1 section 5 and every check at Part 2 section 7
  -> save from Excel so cached values ship with the file
  -> derive sandbox, re-verify
  -> export PDF
```

The recalculation step is a release gate, not a convenience. Excel or LibreOffice must be available to
the build environment. If neither is, the workbook cannot be released, because nobody will have
confirmed that the arithmetic in it is right.

---

## 2. Reader model

**Primary reader.** Has met Brandon and Dominic. Arrives with context, with the concept understood
and the people assessed. Reads for whether the operating result justifies the commitment. Reads the
first two sheets in minutes and forms a view.

**Secondary reader.** Their CPA, attorney or spouse. Was never in the room. Receives the file
forwarded, often within days. Starts from refute. Reads for reconciliation, for what is missing, and
for whether the front of the workbook promises anything the back cannot prove.

**The gating rule.** Every sentence the meeting supplied verbally must exist in the file. An oral
caveat that is not written down becomes a claim nobody made. Test before release: hand the file to
someone who missed the meeting. Every question they ask is a missing sentence.

One workbook serves both. No tiering. Sheet order serves the primary reader, cross-footing serves the
secondary reader, and the two never conflict because the headline layer is derived from the driver
layer rather than asserted alongside it.

---

## 3. The argument, and what leads without returns

The profile's default for an income-and-trophy raise is that distributable cash leads. Returns,
waterfall and IRR are out of scope, so distributable cash cannot lead in its usual form.

**What leads instead: Company EBITDA and what the money buys.**

The Summary sheet carries the ask, the sources and uses beside it, and Company EBITDA at Year 1 and
at Year 5, with break-even headroom underneath. That is the operating result and the honest ceiling
of what this workbook can say.

**The division of labor is stated explicitly on the cover.** The workbook produces the operating
result. It does not compute the reader's return. Their own advisor computes that from these figures
and the terms in the subscription documents. Saying so converts a gap into a boundary, and it is also
true: a workbook that computed a return would be making representations that belong to counsel, not
to this artifact.

Sequence, and the argument each sheet makes:

| # | Sheet | The argument it makes |
| --- | --- | --- |
| 00 | Cover and conventions | Here is what this is, what it is not, and how to read it. |
| 01 | Summary | This is the ask, this is what it buys, this is what it earns. |
| 02 | Revenue build | The revenue is not a target. It is built from covers and price, service by service. |
| 03 | Capacity and throughput | Every service fits inside the physical room. Here is the headroom. |
| 04 | Unit economics | Revenue becomes Company EBITDA in three lines, and here is every line. |
| 05 | Five-year projection | Growth is price-led, not traffic-led, and here is each year. |
| 06 | Scenario instrument | Move the drivers yourself. The answer holds across the range. |
| 07 | Break-even | Here is the floor, and here is the distance between the plan and the floor. |
| 08 | Sources, uses and cash position | Here is where every dollar goes, and what is held in reserve. |
| 09 | Corporate G&A scaling | The overhead is one unit's, and it does not triple at three units. |
| 10 | Occupancy and lease status | The largest commitment is not signed. Here it is anyway, quantified. |
| 11 | Assumption register | Every driver, its value, its source, its status, its tested range. |
| 12 | Disclosures | Everything this model does not do, named, in one place. |
| 13 | Checks and workings | The machinery that catches errors, visible and running. |

**Why break-even sits at 07 and not earlier.** Break-even is the reader's floor test and it is strong
here, so the temptation is to lead with it. It sits after the scenario instrument because a floor
means nothing until the reader has moved the drivers themselves. Shown first it is an assertion;
shown after the instrument it is a conclusion the reader has already half-reached.

**Why disclosures sit at 12 and not first.** Each disclosure also appears as a one-line marker beside
the figure it qualifies. Sheet 12 is the consolidated version for the secondary reader, not the first
thing the primary reader meets. Front-loading them reads as anxiety.

---

## 4. The three-layer rule

Every exhibit sheet carries three layers, and each is complete alone.

- **Layer one, headline.** The figure and its label. Readable in isolation.
- **Layer two, drivers.** What produced the figure, one calculation per quantity.
- **Layer three, assumption register.** The value, the source, the status, the tested range.

**Layer three never contradicts layer one.** Enforce mechanically: every headline figure is a formula
referencing the driver block, and every driver references the register. No headline is ever typed.
The checks sheet cross-foots each headline against an independently built total.

Where a disclosure qualifies a headline, the disclosure marker sits in layer one, adjacent to the
figure, and its full text sits on sheet 12. A headline figure that needs a caveat carries the caveat
at the same reading distance as the figure.

---

## 5. Canonical figures

Every figure below was read live from Airtable on 22 August 2026, cited by table and record.
**Re-verify before build.** If any figure has moved, the model moved, and this specification is stale
until reconciled.

### 5.1 Mature operating week
Source: P&L Model, record `recmYJ4G16Utam544`, "Core Day Parts".

| Line | Value |
| --- | --- |
| Total revenue, weekly | $150,900.50 |
| Restaurant wages, weekly | $40,650.07 |
| Restaurant labor % (rebased) | 29.571% |
| Restaurant prime cost % (rebased) | 56.07% |
| Restaurant-Level EBITDA, weekly | $31,696.53 |
| Restaurant-Level EBITDA % | 21.005% |
| Corporate G&A, weekly | $6,521.10 |
| Company EBITDA, weekly | $25,175.43 |
| Company EBITDA % | 16.68% |

Cost rates on the same record: food 28.0%, beverage 22.0%, card processing 3.0%, comps 3.0%,
voids 1.0%, menu printing 0.05%, smallwares 2.0%, marketing 1.5%. Week conventions: revenue 52,
labor 50. Base monthly rent $18,750. Percentage rent rate 4.0%. Natural breakpoint yield 6.0%.
Payroll burden: FICA 7.65%, workers compensation 0.75%, wage-proportional total 8.4%.

Wage build reconciliation, verified: hourly labor $32,770.07 plus salaried $7,880.00 equals
restaurant wages $40,650.07. Wages at 1.084 burden equal $44,064.68, plus per-hire FUTA and SUTA of
$558.60 weekly equals $44,623.28, which is 29.571% of revenue.

### 5.2 Mature week by daypart
Source: Restaurant Configurator, `tblb4TMjWnZI5J64Q`, day part records.

| Daypart | Covers | PPA | Revenue | Share | FOH labor | BOH labor |
| --- | --- | --- | --- | --- | --- | --- |
| i. Early Morning | 1,566 | $10.55 | $16,515.00 | 10.9% | $2,520.00 | $2,845.53 |
| ii. Lunch | 1,562.5 | $16.00 | $25,000.00 | 16.6% | $600.00 | $1,707.50 |
| iii. Brunch | 675 | $33.99 | $22,944.50 | 15.2% | $3,256.00 | $2,191.20 |
| iv. Dinner | 1,500 | $52.62 | $78,932.00 | 52.3% | $8,360.00 | $9,471.84 |
| v. Late Night | 399 | $18.82 | $7,509.00 | 5.0% | $666.00 | $1,152.00 |
| **Total** | **5,702.5** | **$26.46** | **$150,900.50** | **100%** | **$15,402.00** | **$17,368.07** |

PPA figures are derived, revenue divided by covers, and are display values. Do not enter them as
inputs. The daypart names above are the names carried in the base and are already neutral. No daypart
code name appears anywhere in the base's revenue spine, and none may appear in the workbook. Brand
Guidelines section 01 records Good Energy, Dosi and Luxx as internal names, with Luxx explicitly never
public-facing.

### 5.3 Service-level build
Source: Reference: Service Schedule, `tbltMSNK1GZ96rBe7`, 22 records. Covers here are the canonical
demand input. The 22 rows sum to exactly 5,702.5 covers and $150,900.50.

| Daypart | Day | Hours | Covers | Revenue | FOH labor | Seats |
| --- | --- | --- | --- | --- | --- | --- |
| Early Morning | Mon | 6am to 2pm, 8 | 167 | $1,294.25 | $280 | 0 |
| Early Morning | Tue | 6am to 2pm, 8 | 119 | $922.25 | $280 | 0 |
| Early Morning | Wed | 6am to 11am, 5 | 119 | $922.25 | $280 | 0 |
| Early Morning | Thu | 6am to 11am, 5 | 149 | $1,154.75 | $280 | 0 |
| Early Morning | Fri | 6am to 11am, 5 | 178 | $1,379.50 | $280 | 0 |
| Early Morning | Sat | 6am to 11am, 5 | 417 | $5,004.00 | $560 | 0 |
| Early Morning | Sun | 6am to 11am, 5 | 417 | $5,838.00 | $560 | 0 |
| Lunch | Mon to Fri | 11am to 3pm, 4 | 312.5 each | $5,000.00 each | $120 each | 0 |
| Brunch | Sat | 10am to 3pm, 5 | 350 | $11,899.50 | $1,628 | 126 |
| Brunch | Sun | 10am to 3pm, 5 | 325 | $11,045.00 | $1,628 | 126 |
| Dinner | Wed | 5pm to 11pm, 6 | 200 | $9,329.00 | $1,220 | 126 |
| Dinner | Thu | 5pm to 11pm, 6 | 270 | $13,821.00 | $1,380 | 126 |
| Dinner | Fri | 5pm to 11pm, 6 | 350 | $18,954.00 | $1,920 | 126 |
| Dinner | Sat | 5pm to 11pm, 6 | 350 | $18,954.00 | $1,920 | 126 |
| Dinner | Sun | 5pm to 11pm, 6 | 330 | $17,874.00 | $1,920 | 126 |
| Late Night | Fri | 11pm to 2am, 3 | 109 | $2,289.00 | $222 | 74 |
| Late Night | Sat | 11pm to 2am, 3 | 145 | $2,610.00 | $222 | 74 |
| Late Night | Sun | 11pm to 2am, 3 | 145 | $2,610.00 | $222 | 74 |

BOH labor rate by daypart, entered on the same table: dinner 12.00%, early morning 17.23%, brunch
9.55%, late night 15.3416%, lunch 6.83%. BOH labor is that rate applied to daypart revenue.
Third-party delivery inputs, lunch rows only: commission 28.0%, mix 25.0%, packaging $1.60 per order.

### 5.4 Capacity
Source: Reference: Seating & Capacity, `tblCxNuabfu99rEwR`; Model Assumptions, `tbl1mP7BuOuZqAx4f`.

126 seats: 52 main dining room, 74 patio. Patio standing capacity 24, confirmed against the floor
plan. Premises 5,178 rentable square feet. Table mix: patio 28 tables at a 70% two-top ratio, dining
room 17 tables at a 50% two-top ratio. Turn times: dinner 1.67 hours, brunch 1.25, lunch 1.00, late
night 1.75. Early morning is window service with no seat constraint.

### 5.5 Year 1 bridge, Our Plan
Source: Years 1-5 Projections, `tblbpcivasV0rrVap`, record `rec5nhQdOT17s6hkL`.

| Line | Amount | % of revenue |
| --- | --- | --- |
| Revenue | $6,588,777.97 | 100.00% |
| Cost of sales | ($1,746,026.16) | 26.50% |
| Labor, rebased | ($2,164,338.00) | 32.85% |
| Operating expense | ($1,164,065.76) | 17.67% |
| Occupancy | ($416,221.12) | 6.32% |
| **Restaurant-Level EBITDA** | **$1,098,126.93** | **16.67%** |
| Corporate G&A | ($326,910.00) | 4.96% |
| **Company EBITDA** | **$771,216.93** | **11.71%** |

Occupancy decomposes as base rent $225,000, NNN and CAM $77,670, percentage rent $113,551.12. The
percentage rent figure is 4% of revenue above the $3,750,000 natural breakpoint, verified.

### 5.6 Five-year projection, three scenarios
Source: Years 1-5 Projections. Scenario definitions from Scenario Configurator, `tbljpekNyw4oSvl5k`.

Our Plan (`rec2GKw1KiM1bWzK5`): revenue adjustment 0.00%, COGS adjustment 0.00%, labor adjustment
0.00%, conservative ramp.

| Year | Revenue | RL EBITDA | % | Corp G&A | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $6,588,778 | $1,098,127 | 16.67% | $326,910 | $771,217 | 11.71% |
| 2 | $8,493,849 | $1,943,770 | 22.88% | $326,055 | $1,617,715 | 19.05% |
| 3 | $9,380,163 | $2,276,175 | 24.27% | $326,055 | $1,950,120 | 20.79% |
| 4 | $9,900,794 | $2,478,579 | 25.03% | $326,055 | $2,152,524 | 21.74% |
| 5 | $10,366,872 | $2,647,247 | 25.54% | $326,055 | $2,321,192 | 22.39% |

Downside, carried in the projections table as "Investor Downside" (`rec6QTcA4ebhu5RVa`): revenue
adjustment -13.05%, COGS adjustment +3.00%, labor adjustment -8.70%, its own twelve-month ramp curve.

| Year | Revenue | RL EBITDA | % | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- |
| 1 | $5,427,845 | $471,911 | 8.69% | $145,001 | 2.67% |
| 2 | $7,385,402 | $1,307,632 | 17.71% | $981,577 | 13.29% |
| 3 | $8,156,052 | $1,566,222 | 19.20% | $1,240,167 | 15.21% |
| 4 | $8,608,741 | $1,724,593 | 20.03% | $1,398,538 | 16.25% |
| 5 | $9,013,995 | $1,854,909 | 20.58% | $1,528,854 | 16.96% |

Best Case (`recXHnZMJxuSzNx8m`): revenue adjustment 0.00%, COGS adjustment 0.00%, labor adjustment
0.00%, out-year price uplift 6.00%.

| Year | Revenue | RL EBITDA | % | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- |
| 1 | $6,588,778 | $1,098,127 | 16.67% | $771,217 | 11.71% |
| 2 | $9,003,480 | $2,229,849 | 24.77% | $1,903,794 | 21.15% |
| 3 | $9,942,973 | $2,592,100 | 26.07% | $2,266,045 | 22.79% |
| 4 | $10,494,842 | $2,812,048 | 26.79% | $2,485,993 | 23.69% |
| 5 | $10,988,884 | $2,996,412 | 27.27% | $2,670,357 | 24.30% |

Mature annual revenue, needed for the ramp lever at section 12: Our Plan and Best Case $7,846,826,
Downside $6,822,815.21. **Verified property of the model:** the Downside revenue adjustment is an
exact flat multiplier. $7,846,826 times 0.8695 equals $6,822,815.21 to the cent. Seasonality is
common across all cases. This is what makes the ramp lever separable, per section 12 Zone 2.

**Scenario naming.** The projections tables label the middle case "Investor Downside" while the
configurator labels it "Downside", and the launch strategy field uses a third vocabulary. The
workbook uses exactly three names, everywhere, with no variants: **Our Plan**, **Downside**,
**Best Case**. Per the profile, scenarios are named by mechanism and never by virtue. None of these
three claims conservatism, so all three are acceptable.

### 5.7 Break-even
Source: Analysis: Break-Even, `tblbrT9gneQi9KTpQ`, recomputed 22 August 2026.

| Case | Fixed cost block | COGS % | Contribution margin | BE revenue | BE week | BE covers per day |
| --- | --- | --- | --- | --- | --- | --- |
| Our Plan, Year 1 | $3,077,301.88 | 26.50% | 60.133575% | $5,214,886 | $100,286 | 541.4 |
| Downside, Year 1 | $2,889,004.48 | 29.50% | 57.133575% | $5,154,941 | $99,133 | 615.5 |
| Our Plan, Year 2 steady | $3,303,182.92 | 26.50% | 60.133575% | $5,611,941 | $107,922 | 582.6 |
| Downside, Year 2 steady | $3,095,550.98 | 29.50% | 57.133575% | $5,538,026 | $106,500 | 661.2 |

Best Case duplicates Our Plan on both rows. Variable operating expense 13.366425%. Percentage rent
enters as a fourth variable cost at 4% above the breakpoint, which is $3,750,000 in Year 1 and
$3,825,000 in Year 2. Every case solves above the breakpoint. Mature weekly covers held at 5,702.5
across all cases.

Fixed operating expense of $283,383.88 is eight weekly lines totalling $5,449.69 at 52 weeks:
utilities $923, insurance $577, repairs and maintenance $346, technology $2,000, linen $300,
licenses $96, professional $400, kitchen automation service $807.69.

**Relabel required.** The eighth line is named for its vendor in the base. The vendor relationship is
unannounced. In the workbook it reads "kitchen automation service" and nowhere else.

### 5.8 Sources and uses
Source: Lean Sources and Uses, `tblDwuIFaYNYySQRg`. Raise target confirmed as a founder decision of
13 August 2026.

| Line | Lean Opening | Full Vision |
| --- | --- | --- |
| Confirmed leasehold improvements | $195,000 | $195,000 |
| Allowance-eligible hard-cost scope | $1,055,000 | $1,055,000 |
| Furniture, fixtures and equipment | $315,000 | $443,089 |
| Operating supplies and equipment | $300,000 | $399,581 |
| Pre-opening expenses | $252,000 | $415,000 |
| Reserves and deposits | $467,000 | $467,000 |
| **Adjusted project cost** | **$2,584,000** | **$2,974,670** |
| Less landlord improvement allowance | ($1,100,000) | ($1,100,000) |
| **Outside capital after allowance** | **$1,484,000** | **$1,874,670** |
| Working capital and opening cash cushion | $1,016,000 | $625,330 |
| **Total raise** | **$2,500,000** | **$2,500,000** |

Gross project funding is $3,600,000 including the allowance. Roughly $250,000 of landlord-delivered
scope traces to an internal task rather than the tenant proposal and is carried at zero. It stays at
zero in the workbook. Reserves and deposits of $467,000 carries a stated $300,000 reserve and a
$72,000 founder draw.

**Scope, decided 22 August 2026.** This table governs the sources and uses structure of the workbook.
It is out of scope only as a competing pre-opening labor figure. Pre-opening labor comes from
section 5.9 and from nowhere else. See Part 2 section 2.1.

### 5.9 Pre-opening labor
Source: Labor: Positions, `tblgOaCAo4IzsrfYT`. **This is the only place pre-opening labor lives.**

Thirteen positions carry pre-opening wages, 51 heads, summing to **$92,560**, verified by
recomputation from the individual records on 22 August 2026.

| Line | Amount | Basis |
| --- | --- | --- |
| Pre-opening wages | $92,560.00 | 13 positions, 51 heads |
| Employer burden, FICA and workers compensation | $7,775.04 | $92,560 at 8.4% wage-proportional, verified exact |
| Employer burden, FUTA and SUTA | $2,681.88 | Computed per position against the wage bases |
| **Total employer burden** | **$10,456.92** | |
| **Total pre-opening labor** | **$103,016.92** | |

**Decided 22 August 2026.** Version 1.1 of this specification carried $2,682.00 for the FUTA and SUTA
line and a total of $103,017.04, derived as a residual against a stated total of $10,457.04. That
$10,457.04 was arithmetic in a report rather than a source. The governing figure is $2,681.88,
computed per position against the wage bases, which is why it does not equal a flat per-head rate.
Across 51 heads it averages $52.59, which is what a wage-base computation produces when most
pre-opening wages sit below the base. Check 20 at Part 2 section 7 asserts against $103,016.92.

### 5.10 Corporate G&A scaling
Source: Scaling View: Corporate G&A, `tblWr1DLYJ8XUkMe6`.

| Units | Annual revenue | Founder comp | Burden | Corporate hire | Total | % of revenue |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $8,493,849 | $300,000 | $26,055 | $0 | $326,055 | 3.84% |
| 2 | $16,987,698 | $300,000 | $26,055 | $0 | $326,055 | 1.92% |
| 3 | $25,481,547 | $300,000 | $26,055 | $103,275 | $429,330 | 1.68% |

The revenue basis is Year 2 steady state, not Year 1. The column header must say so.

### 5.11 Year 1 ramp
Source: Scenario Timeline, `tblJkSA7dIYWN6BDq`, capacity utilization by operating month.

Conservative curve, used by Our Plan and Best Case: 58%, 63%, 68%, 73%, 78%, 84%, 90%, 95%, 100%,
100%, 100%, 100%.

Downside curve: 52%, 57%, 62%, 67%, 72%, 78%, 84%, 89%, 95%, 100%, 100%, 100%.

**Composite Year 1 factors, derived from the Airtable-computed outcomes above and used by the ramp
lever at section 12 Zone 2:**

| Curve | Year 1 revenue / mature annual revenue | Factor |
| --- | --- | --- |
| Conservative | $6,588,777.97 / $7,846,826.00 | 0.839674 |
| Downside | $5,427,844.67 / $6,822,815.21 | 0.795543 |

**The two factors above are display values, not entries.** The workbook derives both as formulas, per
section 12 Zone 2 and Part 2 section 10. Do not type 0.839674 or 0.795543 into a cell: at six decimal
places the conservative factor reproduces Year 1 to within $2.20 rather than to the cent, which
fails check 22.

These factors carry the ramp and the seasonality layer together. Because seasonality is common across
cases and the revenue adjustment is an exact flat multiplier (verified at section 5.6), a factor
derived from one case applies correctly to another case's mature revenue. **This is what allows the
ramp lever to exist without the workbook recomputing Year 1 from a monthly build.**

A third curve, 65% to 100% over six months, is documented in the assumption register. **It is not
exposed as a lever**, because no Airtable-computed Year 1 outcome exists for it and deriving one would
require the monthly rebuild this specification excludes. Carry it in the register as a documented
alternative, not as a selectable option.

Dinner runs five days a week throughout Year 1 in every active case. The six-day dinner expansion
enters in Year 2 as a half increment and reaches full increment in Year 3.

---

## 6. Sheet 00, Cover and conventions

Portrait, one printed page. The only sheet with prose paragraphs.

| Cell | Content |
| --- | --- |
| B2 | Title: "Sŏn, 207 E St. Elmo Road, Austin, Texas" |
| B3 | Subtitle: "Investor financial exhibit" |
| B4 | "Version 1.0. Figures as of 22 August 2026." |
| B5 | File identity: "MASTER, read-only" or "SANDBOX, editable" |
| B7 | Section heading: "What this workbook is" |
| B8:H11 | Purpose paragraph |
| B13 | Section heading: "What this workbook does not contain" |
| B14:H17 | Boundary paragraph |
| B19 | Section heading: "The single admonition" |
| B20:H22 | **PLACEHOLDER, see below** |
| B24 | Section heading: "How to read it" |
| B25:H32 | Conventions block |
| B34 | Section heading: "Lease status" |
| B35:H37 | Lease status, including rent commencement |
| B39 | Master check indicator, formula `=Chk_Master`, conditional formatted |
| B41 | **PLACEHOLDER, see below** |

### 6.1 The two copy placeholders

Both are deliberate. A builder places the bracketed text exactly as written. Brandon fills both before
release, and release gate 10 at Part 2 section 16 blocks shipping with either still in place.

**B20:H22, the admonition:**

```
[ADMONITION PENDING COMPLIANCE REVIEW. This workbook must not be released with this
placeholder in place. Wording is owned by the compliance seat, not by the builder.]
```

**B41, the contact line:**

```
[CONTACT LINE PENDING. Name and email only. No phone number.]
```

Do not draft substitute wording for either. An admonition drafted by a builder is a legal
representation authored by the wrong person, and a contact line invented by a builder is a factual
error. The placeholder is the correct output.

### 6.2 Prose blocks, as written

**Purpose paragraph:**

> This workbook shows how Sŏn produces an operating result. It builds revenue from covers and price
> service by service, carries that revenue down to Company EBITDA in three lines, and projects five
> years across three cases. Sheet 06 lets you move the drivers yourself. Every figure traces to the
> financial model, and sheet 13 shows the checks that police it.

**Boundary paragraph:**

> This workbook does not compute your return. It contains no return schedule, no distribution
> waterfall and no internal rate of return, by design. Those depend on terms that live in the
> subscription documents, not in the operating model. What this workbook gives you is the business:
> what it earns, what it costs, and how far the plan sits above its own break-even. Your own advisor
> computes the rest from these figures and those terms.

**Lease status block:**

> The premises at 207 E St. Elmo Road are under a letter of intent and the lease is not signed. All
> occupancy figures in this workbook are letter-of-intent economics and are subject to execution.
> Rent commencement is currently recorded as a date that precedes the planned opening. Sheet 10
> carries both, quantified.

### 6.3 Conventions block, verbatim rows

- Pale Jade fill with a Peacock border: an input you may change. Only on sheet 06 and one cell on
  sheet 10, and only in the sandbox file.
- Plum Ink text on Bone: a calculated figure. Do not type over it.
- Aubergine italic: a figure carried from another sheet, or a driver sitting outside its
  substantiated range.
- Onggi bold with a hairline border: a check has failed. See sheet 13.
- Peacock: a check has passed.
- Negatives appear in parentheses. Costs are shown as negatives in bridge tables and as positives in
  rate tables. Every table states which.
- Currency at whole dollars on annual figures, two decimals on weekly figures.
- Percentages at two decimals.
- Displayed figures are rounded. Calculations underneath are not.
- Revenue weeks per year: 52. Labor weeks per year: 50. This is deliberate and stated on sheet 11.
- A marker such as **D4** beside a figure points to sheet 12, Disclosures, entry 4.
- Sheets are protected without a password. You may unprotect any sheet in two clicks. Nothing in this
  file is hidden from you.

**Note on the input convention.** Financial modeling convention marks inputs in light blue. The brand
palette contains no blue. Inputs are Pale Jade with a Peacock border instead. The convention line
above exists so a reader expecting blue is not confused by its absence.

---

## 7. Sheet 01, Summary

Landscape, one printed page. The most important sheet in the file. Nothing on it is typed; every
figure is a formula pointing at a driver sheet.

**Band A, rows 3 to 9: The ask and what it buys.**

| Cell | Content |
| --- | --- |
| B3 | "The raise" |
| B4 | Label "Total equity sought" |
| D4 | `=SU_TotalRaise` formatted $#,##0 |
| B5 | Label "Structure" |
| D5 | Text "Full equity. No debt in this plan." |
| B6 | Label "Landlord improvement allowance, separate and contingent" |
| D6 | `=SU_Allowance` |
| B7 | Label "Gross project funding" |
| D7 | `=SU_TotalRaise+SU_Allowance` |
| F3 | "Uses, Lean Opening plan" |
| F4:H9 | Six use categories with values from `SU_Lean_*`, plus total |

**Band B, rows 11 to 20: What it earns.**

A three-line bridge shown twice, Year 1 and Year 5, under the selected scenario, with the scenario
name displayed from `Scen_Selected`. On the master this reads "Our Plan" and cannot be changed.

| Row | Label | Year 1 column (E) | Year 5 column (G) |
| --- | --- | --- | --- |
| 12 | Revenue | `=INDEX(FY_Rev_Y1,Scen_Index)` | `=INDEX(FY_Rev_Y5,Scen_Index)` |
| 13 | Restaurant-Level EBITDA | `=INDEX(FY_RLE_Y1,Scen_Index)` | `=INDEX(FY_RLE_Y5,Scen_Index)` |
| 14 | as % of revenue | `=E13/E12` | `=G13/G12` |
| 15 | Corporate G&A | `=-INDEX(FY_GA_Y1,Scen_Index)` | `=-INDEX(FY_GA_Y5,Scen_Index)` |
| 16 | **Company EBITDA** | `=E13+E15` | `=G13+G15` |
| 17 | as % of revenue | `=E16/E12` | `=G16/G12` |

Row 16 is the headline of the workbook and carries the largest type on the sheet. It is derived rather
than read from a named range, which is why no `FY_CoE_*` names exist. See Part 2 section 0.2.

Row 19: "Year 1 is one figure for Our Plan and Best Case. Cases separate from Year 2. **D3**"

**Band C, rows 22 to 28: The floor.**

| Row | Label | Value |
| --- | --- | --- |
| 23 | Mature operating week, revenue | `=PL_MatureWeekRev` |
| 24 | Break-even week, Year 1 | `=INDEX(BE_Weekly_Y1,Scen_Index)` |
| 25 | Headroom above break-even | `=D23-D24` |
| 26 | Headroom as % of mature week | `=D25/D23` |
| 27 | Break-even covers per day | `=INDEX(BE_CoversDay_Y1,Scen_Index)` |
| 28 | Planned covers per day, mature | `=RB_TotalCovers/7` |

Row 26 for Our Plan computes to 33.5%. Do not type that. Let it compute.

**Band D, rows 30 to 35: Cash position.**

**Decided 22 August 2026: the Lean Opening plan is the default and Full Vision is shown alongside.**
Two columns, D for Lean and F for Full, so the reader sees both without either being buried. Full
derivation at Part 2 section 2.5.

| Row | Label | Lean (D) | Full (F) |
| --- | --- | --- | --- |
| 31 | Working capital and opening cash cushion | `=SU_Cushion_Lean` | `=SU_Cushion_Full` |
| 32 | Year 1 fixed cost block | `=INDEX(BE_Fixed_Y1,Scen_Index)` | same reference |
| 33 | Average monthly fixed cost | `=D32/12` | `=F32/12` |
| 34 | Months of fixed-cost cover at opening | `=D31/D33` | `=F31/F33` |

Row 34 computes to 3.96 months on Lean and 2.44 months on Full. Row 35 carries the label: "This is a
coverage statement, not a runway schedule. **D13**"

The Lean column carries the emphasis formatting. The Full column is present at equal precision and
lesser weight. Showing only the larger of the two cushions would be the kind of selection an
experienced reader looks for and finds.

**Band E, rows 37 to 41: The four things a reader must know before going further.**

Four single lines, each with a disclosure marker:

- "Front-of-house labor is modeled at base wages only. A menu-embedded compensation structure is
  designed and is not modeled here. **D1**"
- "The kitchen build is a budget authored by an operator whose depth is front of house. A founding
  chef partner is being recruited and will own it. **D2**"
- "The lease is not signed, and rent commencement currently precedes opening. **D11**"
- "This release contains a cash position, not a monthly cash flow or runway schedule. **D13**"

Putting these on the Summary rather than burying them on sheet 12 is deliberate. A reader who finds
them later reads them as concealment. A reader who meets them on the first page reads them as
control.

---

## 8. Sheet 02, Revenue build

Landscape. The driver layer for revenue.

**Block 1, rows 4 to 11: Mature week by daypart.** Columns: B daypart, C covers, D per-person
average, E revenue, F share of revenue, G FOH labor, H BOH labor, I BOH rate.

Rows 5 to 9 carry the five dayparts. Row 10 totals. Row 11 checks:
`=IF(ABS(E10-PL_MatureWeekRev)<0.01,"OK","BREAK")`.

Covers in column C and revenue in column E are formulas summing the service block below, never typed.
Per-person average in column D is `=E5/C5`, a derived display figure.

**Named range anchors on this sheet.** `Base_DinnerRevenue` is E8, the dinner revenue total.
`Base_DinnerPPA` is D8, the dinner per-person average. `Base_OtherRevenue` is the non-dinner revenue
subtotal, $71,968.50. All three are referenced by the lever formulas at Part 2 section 10 and are
declared at Part 2 section 9.

**Block 2, rows 14 to 36: Service-level build.** One row per service, 22 rows, matching section 5.3
exactly. Columns: B daypart, C day, D start, E end, F service hours, G covers, H revenue, I
per-person average, J FOH labor, K seats available.

Covers in column G are the canonical demand input. Header note: "Covers here are the model's demand
input. Every revenue figure in this workbook is built from this column."

Row 37 totals. Row 38 checks against block 1.

**Block 3, rows 41 to 47: Third-party delivery, lunch only.** Commission 28.0%, mix 25.0%, packaging
$1.60 per order, with resulting cost lines and a note that these apply to the lunch daypart only,
which is 16.6% of revenue.

**Argument note, row 49:** "Dinner is 26.3% of covers and 52.3% of revenue. Four dayparts outside
dinner produce 47.7% of revenue from one kitchen and one lease."

That sentence is the multi-daypart thesis stated once, where the numbers prove it. It does not appear
again anywhere in the workbook.

---

## 9. Sheet 03, Capacity and throughput

Landscape. This sheet exists to solve a specific misreading, and its layout is driven by that.

**The problem.** A reader who sees 417 covers on a Saturday early morning and divides by the
five-hour service window reaches 83.4 covers per hour, forms a view about plausibility, and never
asks whether a cover is a transaction. Left to compute it themselves, they compute it wrong or they
compute it right and still distrust it, because nothing on the page anticipated the question.

**The solve.** Compute it for them, on the page, beside the covers figure, with the definition stated
and the seat math shown.

**Block 1, rows 4 to 6: Definitions, stated before any number.**

- "A cover is one person served. It is not a transaction. One transaction may serve more than one
  cover, for example two coffees bought together. Covers per transaction is not modeled in this
  release. **D15**"
- "Covers per hour below is covers divided by service hours. Transactions per hour are lower than
  covers per hour by the covers-per-transaction ratio."
- "Window services carry no seat constraint. Seated services are constrained by seats and turn time,
  and both are shown."

**Block 2, rows 9 to 31: Throughput by service.** One row per service, 22 rows.

| Col | Header | Source or formula |
| --- | --- | --- |
| B | Daypart | from sheet 02 |
| C | Day | from sheet 02 |
| D | Service hours | from sheet 02 |
| E | Covers | link to sheet 02 column G |
| F | Covers per hour | `=E9/D9` |
| G | Service type | "Window" or "Seated", from a lookup |
| H | Seats available | from sheet 02 |
| I | Turn time, hours | INDEX/MATCH on daypart |
| J | Maximum turns | `=IF(G9="Window","n/a",D9/I9)` |
| K | Maximum covers at capacity | `=IF(G9="Window","n/a",H9*J9)` |
| L | Utilization | `=IF(G9="Window","n/a",E9/K9)` |
| M | Headroom, covers | `=IF(G9="Window","n/a",K9-E9)` |

Column F is the whole point of the sheet. It sits two columns from the covers figure so the reader
never divides anything.

Verified reference values the build should reproduce: Saturday early morning 417 covers over 5 hours
equals 83.4 covers per hour, window service, no seat constraint. Saturday dinner 350 covers over 6
hours equals 58.3 covers per hour against 126 seats at a 1.67-hour turn, giving 3.59 turns, 452
maximum covers, 77.4% utilization. Saturday late night 145 covers against 74 patio seats at a
1.75-hour turn over 3 hours gives 1.71 turns and 127 seated maximum, so the service relies on patio
standing capacity, separately confirmed at 24 places.

**Block 3, rows 34 to 40: The room.** 126 seats, 52 dining room and 74 patio, 24 patio standing
places, 5,178 rentable square feet, table mix by area. Plus one line: "74 of 126 seats, 58.7%, are
outdoors. **D5**" That percentage is computed, not typed, and the disclosure is adjacent because a
reader in Austin will ask about weather within thirty seconds of reading it.

**Block 4, row 43: Late night standing reliance.** "Peak late night services exceed seated capacity
and rely on patio standing places. Usage at peak is 10.58 of 24 places." Sourced from the assumption
register, not computed here.

---

## 10. Sheet 04, Unit economics

Portrait. The three-line bridge in full, at two grains.

**Block 1, rows 4 to 18: Mature operating week.**

| Row | Line | Value | % of revenue |
| --- | --- | --- | --- |
| 5 | Revenue | `=PL_MatureWeekRev` | 100.00% |
| 6 | Cost of sales | negative | `=-D6/$D$5` |
| 7 | Labor, wages | negative | |
| 8 | Labor, payroll burden | negative | |
| 9 | Labor, total | `=D7+D8` | |
| 10 | Operating expense, variable | negative | |
| 11 | Operating expense, fixed | negative | |
| 12 | Occupancy | negative | |
| 13 | **Restaurant-Level EBITDA** | `=SUM(D5:D12)` | |
| 15 | Corporate G&A | negative | |
| 16 | **Company EBITDA** | `=D13+D15` | |
| 18 | Prime cost, % of revenue | `=(-D6-D9)/D5` | |

**Block 2, rows 21 to 35: Year 1 annual, selected scenario.** Same structure, values via
`INDEX(range, Scen_Index)`. Reproduces section 5.5 for Our Plan.

**Block 3, rows 38 to 46: The labor detail, and its two disclosures.**

| Row | Line | Value |
| --- | --- | --- |
| 39 | Front-of-house labor, weekly | `=RB_FOH_Total` = $15,402.00 |
| 40 | as % of revenue | `=D39/PL_MatureWeekRev` = 10.21% |
| 41 | Kitchen labor, weekly | `=RB_BOH_Total` = $17,368.07 |
| 42 | as % of revenue | `=D41/PL_MatureWeekRev` = 11.51% |
| 43 | Salaried, weekly | $7,880.00 |
| 44 | Total wages, weekly | `=D39+D41+D43` = $40,650.07 |
| 45 | Payroll burden at 8.4% plus per-hire | |
| 46 | Total labor, weekly | = $44,623.28, 29.571% of revenue |

Rows 48 to 53 carry disclosures D1 and D2 in full text on the same sheet as the figures they qualify.
Full wording at Part 2 section 11. The requirement that governs the layout:

**D1 is written so the 10.21% reads as incomplete, not as favorable.** The sheet states the modeled
figure, states the range full-wage fine dining typically occupies, states that a menu-embedded
compensation structure is designed and not modeled pending counsel, and states that the workbook
makes no claim about what modeling it would do to the labor line. It does not assert that the
structure explains the gap.

**D2 names the authorship of the kitchen build plainly**, at the same reading distance as the 11.51%,
not on a later sheet.

---

## 11. Sheet 05, Five-year projection

Landscape. Solves the Best Case Year 1 problem structurally.

**The problem.** Best Case Year 1 equals Our Plan Year 1 to the cent. In a conventional three-column
table this reads as a copy-paste failure, on the sheet that most needs credibility.

**The solve.** Present Year 1 once, above the scenario split. Do not merge cells; merged cells are
banned and they break sorting and reference. Use a separate block.

**Block 1, rows 4 to 15: The opening year.** A single column of Year 1 figures for Our Plan and Best
Case, headed "Year 1, common to Our Plan and Best Case", with the Downside Year 1 beside it in its own
column. Row 16 carries the note:

> Our Plan and Best Case share an identical Year 1. That is the model's design, not a duplicate.
> Best Case does not mean Sŏn opens stronger, it means Sŏn commands more once established, so those
> two cases separate from Year 2 through out-year pricing. Downside differs from Year 1 onward,
> because it carries both a demand adjustment and its own ramp. **D3**

**Block 2, rows 19 to 41: Years 2 through 5, three cases.** Three column groups, one per case. Rows:
revenue, cost of sales, labor, operating expense, occupancy, Restaurant-Level EBITDA, RL EBITDA %,
corporate G&A, Company EBITDA, Company EBITDA %, growth from Year 1.

Year 1 appears in this block only as a light reference row at row 20, labelled "Year 1, per block
above", so the reader sees the series without the block implying three independent opening-year
forecasts.

**Block 3, rows 44 to 49: What drives the out-years.** Four lines, each pointing to the register:
growth is price-led with covers flat from Year 2; the Year 2 step includes the six-day dinner
expansion at a half increment, full from Year 3; base rent escalates 2% annually; fixed operating
expense is held flat across all five years. Each carries a disclosure marker.

**Named range anchor on this sheet.** `FY_MatureAnnual` is a three-row range holding mature annual
revenue by case, ordered Our Plan, Downside, Best Case. The ramp lever at section 12 Zone 2 depends
on it.

---

## 12. Sheet 06, Scenario instrument

Landscape. The only sheet with unlocked cells, and only in the sandbox build.

**Zone 1, rows 3 to 6: The switch.**

| Cell | Content |
| --- | --- |
| C4 | Scenario dropdown. Data validation list, source `Scen_Names`. Named `Scen_Selected`. |
| E4 | `=MATCH(Scen_Selected,Scen_Names,0)`. Named `Scen_Index`. |
| C6 | Mechanism description, `=INDEX(Scen_Desc,Scen_Index)` |

Mechanism descriptions, not virtue labels:

- Our Plan: "Demand and cost at the modeled base. Conservative twelve-month ramp. No out-year price uplift."
- Downside: "Revenue 13.05% below base, cost of sales 3.00 points higher, labor 8.70% lower. Slower twelve-month ramp."
- Best Case: "Demand and cost at the modeled base, identical to Our Plan through Year 1. Out-year price uplift of 6.00% from Year 2."

**Zone 2, rows 9 to 22: The featured levers.** Five levers. Each row carries name, base value, current
value (the input), unit, hard minimum, hard maximum, substantiated minimum, substantiated maximum,
status, and what it moves. Input cells are C11 through C15. Full lever specification at Part 2
section 8.

**F4, the ramp lever, decided 22 August 2026 to carry two curves.** It is a dropdown with exactly two
options, Conservative and Downside, both of which have Airtable-computed Year 1 outcomes.

It resolves through a two-row labeled factor table on this sheet, `Ramp_Factors`, whose factor column
holds **formulas, not typed values**:

| Curve label (col 1) | Factor (col 2), as a formula |
| --- | --- |
| Conservative | `=INDEX(FY_Rev_Y1,1)/INDEX(FY_MatureAnnual,1)` |
| Downside | `=INDEX(FY_Rev_Y1,2)/INDEX(FY_MatureAnnual,2)` |

Index 1 is Our Plan, whose native curve is conservative. Index 2 is Downside, whose native curve is
the downside curve. Each factor is that scenario's own Year 1 divided by that scenario's own mature
annual revenue, which makes the reproduction exact rather than approximate.

The dropdown resolves against the table with
`=INDEX(Ramp_Factors, MATCH(Lev_RampCurve, INDEX(Ramp_Factors,0,1), 0), 2)`, and Year 1 revenue is
`=INDEX(FY_MatureAnnual, Scen_Index) * Ramp_Factor_Resolved`. Full formula set at Part 2 section 10.

Putting the factors in a visible table rather than inside a formula is deliberate: a reader can see
what the dropdown is doing without opening the formula bar.

**Superseded, and why.** An earlier version of this section offered
`=IF(Lev_RampCurve="Conservative",0.839674,0.795543)` as an alternative resolution. **Do not use it.**
Typed constants violate the forbidden-patterns rule at Part 2 section 10, and six decimal places is
not enough precision: 0.839674 applied to $7,846,826 returns $6,588,775.77, missing the Airtable
Year 1 of $6,588,777.97 by $2.20 and failing check 22 by construction. Part 2 section 0.1 records the
same correction and describes the constant version that used to appear here; read that description as
historical, because this section now carries the derived version only.

**Why the factor approach works and does not double-count the scenario.** Each scenario's Airtable
Year 1 already embeds that scenario's native ramp. Applying a ramp factor to the scenario's mature
annual revenue reproduces the scenario's own Year 1 exactly when the native curve is selected, and
produces a legitimate hybrid when the other curve is selected: Downside demand with the conservative
ramp gives $5,728,942, Our Plan demand with the downside ramp gives $6,242,490. Both derive only from
Airtable-computed outcomes. Neither requires a monthly rebuild. F4 therefore defaults to the curve
native to the selected scenario, and a reader who changes it is applying an override that the status
column labels as such.

The third documented curve is not an option. See section 5.11.

**Zone 3, rows 25 to 34: Live output.** Mature week revenue, Year 1 revenue, Restaurant-Level EBITDA
and margin, Company EBITDA and margin, break-even weekly revenue, headroom above break-even, covers
per day against break-even covers per day.

**Zone 4, rows 37 to 42: Business alerts.** Four alerts, each firing off the reader's own lever
settings, each computed against the model's own figures rather than an external benchmark:

| Alert | Fires when | Text |
| --- | --- | --- |
| Break-even coverage | mature week < break-even week | "The configured mature week falls below break-even." |
| Percentage rent | annual revenue > natural breakpoint | "Revenue clears the percentage-rent breakpoint. Rent above this line is 4% of incremental sales." |
| Lever outside range | any lever outside substantiated bounds | "One or more drivers sit outside their substantiated range. See the status column." |
| Blank input | any lever cell empty | "A driver input is blank. Outputs on this sheet are not valid." |

No alert fires against an unsourced industry benchmark. The workbook has no sourced benchmark bands
and must not invent them.

**Zone 5, rows 45 to 60: The worst corner, published.** A live formula block, not a static table,
showing the outcome with all five featured levers at their substantiated minimum simultaneously, with
resulting Company EBITDA and distance to break-even. Driven by the `Lev_Min` column holding the
substantiated minimums, so it recalculates with the model and cannot go stale. Check 16 cross-foots
it.

**Zone 6, rows 63 to 75: Sensitivity grid.** A two-variable native data table on dinner covers index
against dinner per-person average, output Company EBITDA at Year 1. Nine by nine.

Built with `DataTableFormula` per section 1.3A. **Technical constraint:** an Excel data table's row
and column input cells must be on the same worksheet as the table. Both driver cells live on this
sheet. A cross-sheet data table will not build.

**Recalculation note:** data tables recalculate on every workbook edit. With one nine by nine table
the cost is negligible. Do not add further data tables without measuring. Do not set calculation to
"Automatic except data tables", because a reader who changes a lever and sees a stale grid will
conclude the workbook is broken.

---

**Part 2 opens with section 0, binding corrections. Read it before writing any code.** Beyond that it
covers sheets 07 through 13, named ranges, formula patterns, the protection scheme, validation rules,
hex and font specification, the full lever set, sandbox derivation, PDF export, the disclosure
register, build order, release gates, and the two routed items that remain.
