# St. Elmo investor exhibit workbook, build specification

Part 2 of 2. Companion: `St_Elmo_Exhibit_Build_Specification_2026-08-22_part1.md`.

Version 1.2, revised 22 August 2026. Supersedes versions 1.0 and 1.1 of the same date.

Part 1 covers purpose, reader model, the argument, Python build constraints, canonical figures, and
sheets 00 through 06. Part 2 covers sheets 07 through 13, mechanics, the lever set, and the two
routed items that remain.

**Read Part 1 first, then read section 0 below before writing any code.**

---

## 0. Binding corrections to Part 1

Two items in Part 1 are superseded by this part. Where they conflict, this part governs.

**0.1 The ramp factors are formulas, never typed constants.**

Part 1 section 5.11 displays the composite Year 1 factors as 0.839674 and 0.795543, and Part 1
section 12 Zone 2 offers `=IF(Lev_RampCurve="Conservative",0.839674,0.795543)` as one way to resolve
them. **Do not build it that way.** Two reasons:

1. It violates this specification's own forbidden-patterns rule at section 10: no hardcoded constants
   inside calculation formulas.
2. Six decimal places is not enough precision. A typed 0.839674 applied to $7,846,826 returns
   $6,588,775.77, which misses the Airtable Year 1 of $6,588,777.97 by $2.20. Check 22 would fail by
   construction.

The factor cells hold formulas that derive each factor from the model, per section 8 F4 and section
10. Built that way the reproduction is exact and check 22 passes at a one-cent tolerance. The six
decimal figures in Part 1 section 5.11 are correct as a display of what the formulas produce, and
should be read as documentation rather than as values to enter.

**0.2 `FY_CoE_Y1` and `FY_CoE_Y5` are not named ranges.**

Part 1 section 7 computes Company EBITDA on sheet 01 as `=E13+E15`, deriving it rather than reading
it. That is correct: one calculation per quantity. Version 1.2 of this part therefore does not
declare those two names. Company EBITDA is derived wherever it appears and cross-footed by check 6
and check 7.

---

## 1. Sheet 07, Break-even

Portrait. Four cases, reproducing Part 1 section 5.7.

**Block 1, rows 4 to 12: The cost structure.** Separates fixed from variable, because break-even is a
property of cost structure and a reader who does not see the split cannot check the arithmetic.

| Row | Line | Our Plan Y1 | Downside Y1 | Our Plan Y2 | Downside Y2 |
| --- | --- | --- | --- | --- | --- |
| 5 | Annual fixed cost block | $3,077,301.88 | $2,889,004.48 | $3,303,182.92 | $3,095,550.98 |
| 6 | Cost of sales, % | 26.50% | 29.50% | 26.50% | 29.50% |
| 7 | Variable operating expense, % | 13.366425% | 13.366425% | 13.366425% | 13.366425% |
| 8 | Percentage rent, % above breakpoint | 4.00% | 4.00% | 4.00% | 4.00% |
| 9 | **Contribution margin** | 60.133575% | 57.133575% | 60.133575% | 57.133575% |
| 11 | Natural breakpoint | $3,750,000 | $3,750,000 | $3,825,000 | $3,825,000 |

Row 9 is `=1-row6-row7-row8`, computed, never typed.

**Block 2, rows 15 to 22: The result.** Break-even annual revenue, break-even weekly revenue,
break-even covers per day, then headroom: planned mature annual revenue, planned mature week,
distance in dollars, distance in percent.

Our Plan Year 1 clears break-even by $1,373,892 of revenue. Downside Year 1 clears it by $272,904.
Both computed, not typed.

**Block 3, rows 25 to 30: The fixed block decomposed.** Labor, fixed operating expense, base rent,
NNN and CAM, corporate G&A. Sums to the fixed block, with a check row confirming.

The fixed operating expense line expands to its eight components: utilities $923, insurance $577,
repairs and maintenance $346, technology $2,000, linen $300, licenses $96, professional $400, kitchen
automation service $807.69, weekly, at 52 weeks. **The eighth line is named for its vendor in the
base. Use "kitchen automation service" and nothing else.**

**Block 4, rows 33 to 37: Notes.**

- "Best Case duplicates Our Plan on both rows. A case that changes only revenue cannot move a
  break-even, because break-even is a property of the cost structure. Best Case buys headroom above
  the line, not a lower line. **D3**"
- "Every case solves above the percentage-rent breakpoint, so percentage rent behaves as a fourth
  variable cost rather than as a fixed one."
- "Covers are held at 5,702.5 across all cases. The Downside reduction is therefore expressed as
  lower average check rather than as fewer customers. Read the other way, the covers requirement
  would be lower and the check requirement higher. **D4**"

That third note is the most important sentence on the sheet. A reader who assumes the Downside models
fewer customers, then discovers it models a lower check, stops trusting the scenario set. Stating it
first costs nothing and buys the opposite.

---

## 2. Sheet 08, Sources, uses and cash position

Portrait.

### 2.1 Scope note, decided 22 August 2026

**Pre-opening labor comes from Labor: Positions and from nowhere else.** The Lean Sources and Uses
table and the Pre-Opening Six-Month Use Schedule are out of scope **only as competing pre-opening
labor figures**. They do not govern that line and are not reconciled against it.

**The sources and uses structure of Lean Sources and Uses stands and governs this sheet.** Version 1.1
left the scope of that decision open. It is now closed to the narrow reading: blocks 1 and 2 build
from Lean Sources and Uses as normal, and block 3 builds pre-opening labor from the position-level
wage schedule.

The Pre-Opening Six-Month Use Schedule is not built into the workbook at all.

### 2.2 Block 1, rows 4 to 18: The two plan views

Columns B label, D Lean Opening, F Full Vision, H difference. Six use categories, adjusted project
cost, less allowance, outside capital after allowance, working capital cushion, total raise. Values
per Part 1 section 5.8.

Both columns total to $2,500,000. That identity is the point of the sheet and should be visually
emphasised: both plans, one raise, different cushion.

### 2.3 Block 2, rows 21 to 25: Sources

A one-line sources side against a $2.58M to $2.97M project invites the question of where the gap
went. Show the allowance as a source, not only as a deduction:

| Row | Source | Amount |
| --- | --- | --- |
| 22 | Equity raise | $2,500,000 |
| 23 | Landlord improvement allowance, contingent on lease execution | $1,100,000 |
| 24 | **Gross project funding** | $3,600,000 |
| 25 | Landlord-delivered scope, unconfirmed, carried at zero | $0 |

Row 25 stays at zero and is shown at zero. Its presence at zero is worth more than its absence: it
tells the reader an item was considered and excluded for lack of confirmation. Row 23 carries the
contingency in its label; the allowance is not cash and does not arrive unless the lease
executes. **D11**

### 2.4 Block 3, rows 28 to 36: Pre-opening labor

Source: Labor: Positions, `tblgOaCAo4IzsrfYT`. Thirteen positions, 51 heads. Verified by recomputation
from individual records on 22 August 2026.

| Row | Line | Amount |
| --- | --- | --- |
| 29 | Pre-opening wages | $92,560.00 |
| 30 | Employer burden, FICA and workers compensation | $7,775.04 |
| 31 | Employer burden, FUTA and SUTA | $2,681.88 |
| 32 | Total employer burden | $10,456.92 |
| 33 | **Total pre-opening labor** | **$103,016.92** |

Row 30 is `=D29*0.084` and computes to $7,775.04 exactly. Row 31 is an entered figure computed per
position against the wage bases. Row 32 is `=D30+D31`. Row 33 is `=D29+D32`.

**Decided 22 August 2026.** Version 1.1 carried $2,682.00 on row 31 and $103,017.04 on row 33, both
derived as residuals against a stated total of $10,457.04. That total was arithmetic in a report
rather than a source. The governing figure is $2,681.88. It does not equal a flat per-head rate
because it is computed per position against the wage bases: across 51 heads it averages $52.59, which
is what a wage-base computation produces when most pre-opening wages sit below the base.

Row 35 carries the scope note: "Pre-opening labor is built from the position-level wage schedule.
Other pre-opening modeling in the financial model is working analysis and does not govern this
figure."

### 2.5 Block 4, rows 39 to 47: Cash position

**This is a cash position, not a runway schedule, and every label on the block says so.**

**Decided 22 August 2026: Lean Opening is the default and Full Vision is shown alongside.** Two
columns at equal precision, the Lean column carrying the emphasis formatting.

| Row | Line | Lean (D) | Full (F) |
| --- | --- | --- | --- |
| 40 | Working capital and opening cash cushion | `=SU_Cushion_Lean` $1,016,000 | `=SU_Cushion_Full` $625,330 |
| 41 | Operating reserve held within reserves and deposits | $300,000 | $300,000 |
| 42 | Year 1 fixed cost block | `=INDEX(BE_Fixed_Y1,Scen_Index)` | same reference |
| 43 | Average monthly fixed cost | `=D42/12` $256,441.82 | `=F42/12` |
| 44 | Months of fixed-cost cover at opening | `=D40/D43` 3.96 | `=F40/F43` 2.44 |

Showing only the larger cushion would be exactly the kind of selection an experienced reader looks
for and finds. Both are shown.

Row 47, the statement that governs the block, as written:

> Monthly cash timing follows lease execution. Rent commencement, the abatement schedule and the
> disbursement mechanics of the improvement allowance are all set by executed lease language, and
> none of the three is executed. Building a monthly cash schedule on letter-of-intent terms would
> mean building it twice. What can be stated now is the cash held at opening and how many months of
> fixed operating cost it covers. That is above, and it is not a runway schedule. **D13**

**Why this is worth building even though it is not a runway.** A reader asks two cash questions. The
first is how much cushion exists, and this answers it precisely. The second is when the trough lands,
and this does not answer it and says so. Answering the first well makes the refusal to guess at the
second read as discipline rather than as a hole.

---

## 3. Sheet 09, Corporate G&A scaling

Portrait, short. Reproduces Part 1 section 5.10.

Column header for revenue must read "Annual revenue, Year 2 steady state" and not "Annual revenue".
At Year 1 revenue of $6,588,778 the same $326,055 is 4.95%, not 3.84%, and a reader who assumes Year 1
will find the discrepancy. **D10**

Two caveat rows directly beneath the table, not on sheet 12:

- "Recruiting and an employer health plan are carried at zero at two and three units. Both are
  decisions, not omissions: the mechanism for each is documented and neither cost has been sized from
  a source. Corporate G&A at two and three units is understated by both lines. **D9**"
- "The third-unit figure includes a booked Director of Operations seat at $103,275. Corporate G&A is
  1.68% of revenue at three units against 3.84% at one unit even with that seat included."

The second line is the argument of the sheet. It is stronger with the hire booked than without it,
which is why the hire is shown rather than deferred.

---

## 4. Sheet 10, Occupancy and lease status

Portrait. The largest commitment in the workbook is not signed, and this sheet says so at the top
rather than at the bottom.

**Block 1, rows 4 to 8: Status, dated.**

"Premises: 207 E St. Elmo Road, Austin, Texas. 5,178 rentable square feet. Status: letter of intent.
The lease is not signed. All figures on this sheet are letter-of-intent economics and are subject to
execution. Status as of 22 August 2026."

Re-date this sheet at every release. A stale date on a lease status sheet is worse than no date.

**Block 2, rows 11 to 21: The economics.** Annual base rent $225,000, base rent escalation 2%
annually, NNN and CAM $77,670 at $15 per square foot on 5,178 square feet, percentage rent 4% of sales
above the natural breakpoint, natural breakpoint yield 6%, breakpoint $3,750,000 in Year 1 and
$3,825,000 in Year 2, lease term ten years plus two five-year options at fair market value.

**Block 3, rows 24 to 31: Occupancy cost by year and case.** Base rent, NNN and CAM, percentage rent,
total occupancy, and occupancy as a percentage of sales, Years 1 through 5 under the selected
scenario. Our Plan Year 1: $225,000 plus $77,670 plus $113,551 equals $416,221, which is 6.32% of
sales.

**Block 4, rows 34 to 40: Rent commencement.**

| Row | Line | Value |
| --- | --- | --- |
| 35 | Rent commencement, as recorded | 1 May 2027 |
| 36 | Planned opening | August 2027 |
| 37 | Months of rent before revenue | 3 |
| 38 | Base rent over that period | $56,250 |
| 39 | Base rent plus NNN and CAM over that period | $75,667.50 |

Row 38 is three months at $18,750. Row 39 adds NNN and CAM at $6,472.50 monthly. Both computed.

Row 40, as written:

> Rent commencement currently precedes the planned opening by roughly three months. The amount above
> is not carried in any projection in this workbook, because commencement timing is a term still
> being negotiated rather than a settled input. It is stated here so the figure is visible rather
> than discovered. This is a live negotiation item, not a defect in the model. **D19**

Stating the exposure and stating that it sits outside the projections are both required. Stating only
the first invites the reader to assume it is inside them.

**Block 5, rows 43 to 48: Rent sensitivity.** Base rent varied across a stated range, showing total
occupancy, occupancy as a percentage of sales, and Company EBITDA at each level. Built as a
one-variable native data table with the input cell on this sheet, per Part 1 section 1.3A.

**The range is a mechanical stress, not a negotiation range.** Run it as plus and minus a stated
percentage of the letter-of-intent rent and label it exactly that. No sourced rent range exists, and
implying knowledge of where the rent lands would be a claim the model cannot support.

### 4.1 What this sheet does not contain, and why

**The walk-away threshold is omitted. Decided 22 August 2026, not an oversight.**

The architect profile calls for a published walk-away rent on the argument that a stated walk-away
reads as discipline under control. The decision is to omit it, for three reasons:

1. The lease is unsigned and the negotiation is live. A number disclosed to an investor can reach the
   landlord through one conversation, and the disclosure costs more in the negotiation than the
   presentational gain is worth.
2. A walk-away threshold is a negotiating position rather than an operating fact. This workbook shows
   the business, not the deal, and a negotiating position is squarely on the deal side of that line.
3. The discipline the profile wants demonstrated is already demonstrated by block 5, which shows what
   happens to Company EBITDA as rent moves, and by block 4, which volunteers an exposure the reader
   would not otherwise have found. A reader can locate the rent at which the economics stop working
   by reading block 5. They do not need the number labeled.

This reasoning is recorded here so a future build does not read the omission as a gap and fill it.

---

## 5. Sheet 11, Assumption register

Portrait, long, the sheet the secondary reader rebuilds from.

Columns: A reference, B driver, C value, D unit, E source, F status, G tested range, H sheet where it
appears, I disclosure marker.

Status vocabulary, exactly four values, no others:

- **Contracted.** Signed and binding.
- **Quoted.** A third party has given a figure in writing but nothing is signed.
- **Letter of intent.** Agreed in principle, not executed.
- **Modeled.** Set by the operator, defended by reasoning rather than by a document.

Nothing in this release is Contracted. Say so in a header line rather than letting the reader discover
a category with no entries.

Register contents, at minimum, each with a source string naming the Airtable table:

Capacity and physical: 126 seats total, 52 dining room, 74 patio, 24 patio standing places confirmed
against floor plan, 5,178 rentable square feet, turn times by daypart, table mix by area.

Revenue drivers: covers by service, 22 entries or one entry pointing at sheet 02; per-person average
by daypart; operating days by daypart; revenue weeks 52; seasonality layer netting approximately 5%
above a flat baseline.

Cost drivers: food 28.0%, beverage 22.0%, blended cost of sales 26.50%, card processing 3.0%,
comps 3.0%, voids 1.0%, menu printing 0.05%, smallwares 2.0%, marketing 1.5%, the eight fixed
operating expense lines, labor weeks 50.

Labor: BOH rate by daypart, FOH schedule by service, salaried weekly $7,880.00, payroll burden
components FICA 7.65% and workers compensation 0.75% giving 8.4% wage-proportional, per-hire FUTA and
SUTA $558.60 weekly, Year 1 calendar straddle $41,208.12 against $27,930 steady state, wage escalation
3.5% annually Years 2 to 5, turnover 75% annually, pre-opening wages $92,560 across 51 heads,
pre-opening employer burden $10,456.92.

Ramp: conservative curve twelve monthly values, downside curve twelve monthly values, composite Year 1
factors derived on sheet 06 as described at section 8 F4, and the third documented curve at 65% to
100% over six months carried as a documented alternative that is not selectable.

Occupancy: base rent $225,000, escalation 2%, NNN and CAM $77,670, percentage rent 4%, breakpoint
yield 6%, lease term, rent commencement 1 May 2027 as recorded.

Corporate: founder compensation $300,000 across three seats at $100,000 each flat in all years, founder
tax treatment modeled as W-2 pending CPA confirmation, corporate allocation 100% for founder seats,
four-wall versus corporate boundary rule.

Growth: out-year growth is price-led with covers flat from Year 2, out-year price uplift 0% in Our Plan
and 6% in Best Case, six-day dinner expansion entering Year 2 at half increment, cost of sales held
flat all five years, fixed operating expense held flat all five years.

Capital: raise $2,500,000, landlord improvement allowance $1,100,000, opening month August 2027,
opening cash cushion $1,016,000 Lean and $625,330 Full.

**One register entry carries a known internal conflict. Show it as it is, not smoothed.**

Early morning service runs 6am to 2pm on Monday and Tuesday and 6am to 11am Wednesday through Sunday,
while lunch runs 11am to 3pm Monday through Friday. Monday and Tuesday therefore carry two dayparts
claiming the same 11am to 2pm window, both with revenue and both with labor. **Routed to the CFO. Do
not resolve it in the workbook.** Carry the schedule as the model carries it and note the overlap in
the register.

**Source citation rule.** Several assumptions in the base cite the tenant proposal sent to the
landlord. That citation names a live negotiation counterparty and does not ship. Restate those entries
as "letter of intent, dated" without naming the counterparty or the proposal document.

---

## 6. Sheet 12, Disclosures

Portrait. Every disclosure in full text, numbered, cross-referenced from the sheet where its figure
appears.

The one prominent admonition lives on sheet 00, not here, and is a placeholder until compliance
supplies it. This sheet carries specifics, not hedges. An admonition governs the whole document; a
disclosure qualifies one number. Full register at section 11 below.

---

## 7. Sheet 13, Checks and workings

Portrait. Visible, labeled, unpolished by design. Never hidden, never protected differently from any
other sheet.

**Block 1, rows 4 to 6: The master flag.**

`Chk_Master` = `=IF(COUNTIF(Chk_Range,"BREAK")>0,"BREAK","OK")`.

Displayed on sheet 00 and in the freeze pane header of every exhibit sheet. Conditional formatted per
section 12.3.

**Block 2, rows 9 to 32: The checks.** Each row: check name, computed value A, computed value B,
difference, tolerance, result. Result pattern `=IF(ABS(D9-E9)<=G9,"OK","BREAK")`.

| # | Check | Asserts | Tolerance |
| --- | --- | --- | --- |
| 1 | Service-level covers sum to daypart covers sum | 5,702.5 | 0.01 |
| 2 | Service-level revenue sums to daypart revenue sum | $150,900.50 | 0.01 |
| 3 | Daypart revenue sums to mature week revenue | $150,900.50 | 0.01 |
| 4 | FOH plus BOH plus salaried equals total wages | $40,650.07 | 0.01 |
| 5 | Wages at burden plus per-hire equals total labor | $44,623.28 | 0.01 |
| 6 | Mature week bridge foots to Company EBITDA | $25,175.43 | 0.01 |
| 7 | Year 1 bridge foots to Company EBITDA, each case | per case | 0.01 |
| 8 | Occupancy components sum to total occupancy, each year | per year | 0.01 |
| 9 | Percentage rent equals 4% of revenue above breakpoint | per case | 0.01 |
| 10 | Sources and uses: both plan columns total $2,500,000 | $2,500,000 | 0.01 |
| 11 | Fixed block components sum to fixed block, each case | per case | 0.01 |
| 12 | Contribution margin equals 1 minus the three variable rates | per case | 0.000001 |
| 13 | Break-even revenue times contribution margin equals fixed block | per case | 1.00 |
| 14 | Corporate G&A weekly at 50 weeks equals annual steady state | $326,055 | 0.01 |
| 15 | Every lever input is non-blank and inside hard bounds | n/a | n/a |
| 16 | Worst-corner block recomputes to displayed values | n/a | 1.00 |
| 17 | Scenario index resolves to 1, 2 or 3 | n/a | n/a |
| 18 | Year 1 Our Plan equals Year 1 Best Case | $6,588,777.97 | 0.01 |
| 19 | Pre-opening wages sum to $92,560 across 51 heads | $92,560.00 | 0.01 |
| 20 | Pre-opening wages plus burden equals total pre-opening labor | **$103,016.92** | 0.01 |
| 21 | Pre-opening FICA and workers compensation equals wages at 8.4% | $7,775.04 | 0.01 |
| 22 | Ramp factor reproduces the native Year 1 when the native curve is selected | per case | 0.01 |

Check 18 is deliberate. It asserts as a passing check the thing that looks like an error. If someone
later manufactures a Year 1 difference, this check breaks and the workbook says so.

Check 15 exists because Excel data validation does not fire on paste. It recomputes bounds
independently of validation.

Check 20 asserts $103,016.92 per the decision at section 2.4. Check 21 exists because the FICA and
workers compensation line is the only component of pre-opening burden that can be recomputed from a
rate; isolating it means a future change to either component surfaces as a specific failure rather
than as a total that no longer foots.

**Check 22 and its one-cent tolerance.** With Our Plan selected and the conservative curve, mature
annual revenue times the resolved factor must reproduce $6,588,777.97. With Downside selected and the
downside curve, it must reproduce $5,427,844.67. **This passes at one cent only because the factors
are formulas that derive from the same figures they reproduce, per section 0.1 and section 10.** If a
builder types the six-decimal display values instead, the conservative case misses by $2.20 and this
check breaks. That is the check doing its job, and the fix is to build the factor as a formula, not
to widen the tolerance.

**Block 3, rows 35 onward: Workings.** The intermediate calculations no exhibit sheet shows:
seasonality application, ramp factor derivation, burden build, percentage rent build by year. Labeled,
laid out plainly, not formatted for presentation. Their presence is the credibility instrument.

**No blanket IFERROR anywhere in the workbook.** Guard only legitimate empty states, and let
structural errors surface to the master flag.

---

## 8. The lever set

The profile's selection rule is locus of control. Fragile demand-side drivers are featured as
adjustable levers precisely because they are fragile: a reader will stress them in their own rebuild
regardless, and silence there reads as concealment. Operator-controlled ratios stay fixed at defended
values, because making them adjustable implies the operator does not control them.

### Tier 1, featured levers, adjustable in the sandbox

Sensitivity measured against mature annual revenue of $7,846,826 at a 60.133575% contribution margin.
Impact figures are computed, not asserted; the build should reproduce them.

**F1. Dinner covers index.** Base 100%, equal to 1,500 covers per week across five dinner services.
Hard bounds 50% to 150%. Substantiated range 80% to 115%. Moves 52.3% of revenue. A 10% move is
$410,446 of annual revenue and $246,816 of Company EBITDA. Upper bound support: the tightest dinner
service carries 42 seats of headroom at capacity, so 115% remains inside the room. Lower bound: below
roughly 87% the mature week approaches break-even. **The highest-sensitivity input in the model.**

**F2. Dinner per-person average.** Base $52.62 blended, entered per day in the range $46 to $54. Hard
bounds $30 to $90. Substantiated range $46 to $62. Moves 52.3% of revenue with only the cost-of-sales
offset, so it is slightly harder per dollar than F1, which carries incremental labor. A $5 move is
$390,000 of annual revenue.

**F3. Non-dinner covers index.** Base 100%, equal to 4,202.5 covers per week across early morning,
lunch, brunch and late night, producing $71,968.50 of the mature week. Hard bounds 50% to 150%.
Substantiated range 80% to 115%. Moves 47.7% of revenue. This lever is the multi-daypart thesis
exposed to attack, which is the correct place for it.

**F4. Year 1 ramp curve. Two options, decided 22 August 2026.**

A dropdown with exactly two values, "Conservative" and "Downside". Defaults to the curve native to the
selected scenario: Conservative for Our Plan and Best Case, Downside for Downside. Moves Year 1 only,
and moves it hard. Our Plan Year 1 revenue is 84.0% of the mature annual run rate, so the ramp is
worth roughly $1.26M of Year 1 revenue.

**Build `Ramp_Factors` as a two-row table on sheet 06 whose factor column holds formulas, not typed
constants:**

| Curve label (col 1) | Factor (col 2), as a formula |
| --- | --- |
| Conservative | `=INDEX(FY_Rev_Y1,1)/INDEX(FY_MatureAnnual,1)` |
| Downside | `=INDEX(FY_Rev_Y1,2)/INDEX(FY_MatureAnnual,2)` |

Index 1 is Our Plan, whose native curve is conservative. Index 2 is Downside, whose native curve is
the downside curve. Each factor is therefore that scenario's own Year 1 divided by that scenario's own
mature annual revenue, which makes the reproduction exact rather than approximate. Displayed at six
decimals the two read 0.839674 and 0.795543, which is what Part 1 section 5.11 documents.

**Why the factor approach works and does not double-count the scenario.** Each scenario's Airtable
Year 1 already embeds that scenario's native ramp. Applying a ramp factor to the scenario's mature
annual revenue reproduces the scenario's own Year 1 exactly when the native curve is selected, and
produces a legitimate hybrid when the other curve is selected: Downside demand with the conservative
ramp, or Our Plan demand with the downside ramp. Both derive only from Airtable-computed outcomes.
Neither requires a monthly rebuild.

This is arithmetically valid because two properties of the model were verified on 22 August 2026: the
Downside revenue adjustment is an exact flat multiplier, $7,846,826 times 0.8695 equalling
$6,822,815.21 to the cent; and the seasonality layer is common across all cases. A factor derived from
one case therefore applies correctly to another case's mature revenue.

The third documented curve, 65% to 100% over six months, is **not an option**, because no
Airtable-computed Year 1 outcome exists for it and deriving one would require the monthly rebuild this
specification excludes. It stays in the register as a documented alternative.

**F5. Out-year price uplift.** Base 0.00% in Our Plan, 6.00% in Best Case. Hard bounds 0% to 15%.
Substantiated range 0% to 8%. Moves Years 2 through 5 only. Worth $622,012 of Year 5 revenue between
the two current settings. This is the only input that separates Best Case from Our Plan, so it is
exposed rather than hidden behind a scenario name.

### Tier 2, fixed and defended, displayed but not adjustable

Each appears on sheet 06 in a locked block with its value and a one-line rationale.

**X1. Blended cost of sales, 26.50%.** Food 28.0% and beverage 22.0% at the modeled mix. Operator
controlled through purchasing and menu engineering. Held flat across five years with no supplier
negotiation improvement modeled, which is a conservative treatment stated rather than claimed.

**X2. Kitchen labor rate by daypart, dinner 12.00%.** Operator controlled through the shift build.
Carries disclosure D2.

**X3. Front-of-house schedule, $15,402 weekly.** Operator controlled week to week. Carries disclosure
D1.

**X4. Wage escalation, 3.5% annually.** A deliberate above-market premium rather than a market rate.
Fixed because it is a compensation decision, not a market input.

### The published stress panel

Static block on sheet 06, rows 45 to 60, showing the four fixed drivers moved adversely and
simultaneously: cost of sales at 29.50%, kitchen labor rate plus 300 basis points, front-of-house
schedule plus 15%, wage escalation at 5.0%. Output: Company EBITDA at Year 1 and Year 5, and distance
to break-even.

Publishing this costs the workbook a little and buys a great deal. The reader's advisor will stress
exactly these four. Finding that the workbook already did tells them the operator is not hiding from
the question.

---

## 9. Named ranges

Minimum viable set. Every extra name is a maintenance cost.

| Name | Points at |
| --- | --- |
| `Scen_Names` | Three scenario names, one column |
| `Scen_Selected` | Sheet 06 C4, dropdown cell |
| `Scen_Index` | Sheet 06 E4, MATCH result |
| `Scen_Desc` | Three mechanism descriptions |
| `Lev_DinnerCovers` | Sheet 06 C11, input, F1 |
| `Lev_DinnerPPA` | Sheet 06 C12, input, F2 |
| `Lev_OtherCovers` | Sheet 06 C13, input, F3 |
| `Lev_RampCurve` | Sheet 06 C14, input, F4 |
| `Lev_PriceUplift` | Sheet 06 C15, input, F5 |
| `Lev_Bounds` | Sheet 06 bounds block, five rows by four columns |
| `Lev_Base` | Sheet 06 base values column, for reset |
| `Lev_Min` | Sheet 06 substantiated-minimum column, drives the worst corner at Zone 5 |
| `Ramp_Factors` | Sheet 06 two-row factor table, curve label and derived factor |
| `Base_DinnerRevenue` | Sheet 02 E8, dinner revenue total, $78,932.00 |
| `Base_DinnerPPA` | Sheet 02 D8, dinner per-person average, $52.62 |
| `Base_OtherRevenue` | Sheet 02, non-dinner revenue subtotal, $71,968.50 |
| `PL_MatureWeekRev` | Sheet 02 mature week total |
| `RB_TotalCovers` | Sheet 02 covers total |
| `RB_FOH_Total` | Sheet 02 FOH total |
| `RB_BOH_Total` | Sheet 02 BOH total |
| `FY_Rev_Y1` … `FY_Rev_Y5` | Sheet 05, three rows each |
| `FY_RLE_Y1` … `FY_RLE_Y5` | Sheet 05 |
| `FY_GA_Y1` … `FY_GA_Y5` | Sheet 05 |
| `FY_MatureAnnual` | Sheet 05, three rows, mature annual revenue by case |
| `BE_Weekly_Y1` | Sheet 07, three rows |
| `BE_CoversDay_Y1` | Sheet 07, three rows |
| `BE_Fixed_Y1` | Sheet 07, three rows |
| `SU_TotalRaise` | Sheet 08 |
| `SU_Allowance` | Sheet 08 |
| `SU_Cushion_Lean` | Sheet 08, $1,016,000 |
| `SU_Cushion_Full` | Sheet 08, $625,330 |
| `SU_Lean_*` | Sheet 08, six use categories |
| `Chk_Range` | Sheet 13 result column |
| `Chk_Master` | Sheet 13 master flag cell |

All scenario-indexed ranges are ordered identically: **Our Plan, Downside, Best Case.** `Scen_Index`
resolves against that order, check 17 confirms it, and F4's factor table depends on it.

Two names from earlier versions do not exist. `SU_Cushion` was ambiguous between plan views and is
replaced by the two names above. `FY_CoE_Y1` and `FY_CoE_Y5` are not declared, because Company EBITDA
is derived wherever it appears rather than stored. See section 0.2.

---

## 10. Formula patterns at the 2016 floor

**Permitted:** INDEX, MATCH, CHOOSE, SUMPRODUCT, SUM, SUMIF, SUMIFS, COUNTIF, COUNTIFS, IF, AND, OR,
NOT, MIN, MAX, ABS, ROUND, EOMONTH, DATE, TEXT, VLOOKUP where the lookup column is leftmost.

**Excluded, and they break on a perpetual Excel 2016 licence:** XLOOKUP, LET, LAMBDA, IFS, SWITCH,
TEXTJOIN, CONCAT, MAXIFS, MINIFS, FILTER, SORT, UNIQUE, SEQUENCE, and any dynamic array or spill
behavior.

**Scenario switch, the core pattern:** `=INDEX(FY_Rev_Y1, Scen_Index)`. `Scen_Index` is computed once
on sheet 06 and referenced everywhere. One calculation per quantity.

**Three-way branch:** `=CHOOSE(Scen_Index, value_ourplan, value_downside, value_bestcase)`. Use CHOOSE
for three-branch logic and INDEX for range lookups. Do not nest IF three deep.

**Lever application, dinner revenue:**

```
=Base_DinnerRevenue * Lev_DinnerCovers * (Lev_DinnerPPA / Base_DinnerPPA)
```

**Lever application, non-dinner revenue:**

```
=Base_OtherRevenue * Lev_OtherCovers
```

Both applied at the daypart level, not the service level, so a lever move does not require recomputing
22 rows. The service block stays at base and carries a note saying levers act on the daypart aggregate.

**Ramp factor derivation, in the `Ramp_Factors` table, per section 8 F4:**

```
Conservative row, factor cell:  =INDEX(FY_Rev_Y1,1)/INDEX(FY_MatureAnnual,1)
Downside row, factor cell:      =INDEX(FY_Rev_Y1,2)/INDEX(FY_MatureAnnual,2)
```

**Ramp factor resolution from the dropdown:**

```
=INDEX(Ramp_Factors, MATCH(Lev_RampCurve, INDEX(Ramp_Factors,0,1), 0), 2)
```

**Year 1 revenue from the resolved factor:**

```
=INDEX(FY_MatureAnnual, Scen_Index) * Ramp_Factor_Resolved
```

Because the factors are derived rather than typed, this reproduces the native Year 1 exactly when the
native curve is selected. Check 22 asserts that at a one-cent tolerance.

**Lever status, the two-tier bound test:**

```
=IF(Lev_DinnerCovers="", "BLANK",
  IF(OR(Lev_DinnerCovers<INDEX(Lev_Bounds,1,1), Lev_DinnerCovers>INDEX(Lev_Bounds,1,2)), "HARD",
    IF(OR(Lev_DinnerCovers<INDEX(Lev_Bounds,1,3), Lev_DinnerCovers>INDEX(Lev_Bounds,1,4)),
      "Outside substantiated range", "Within substantiated range")))
```

Three levels of IF is the practical ceiling for readability. Anything deeper becomes a helper column.

**Forbidden patterns:** hardcoded constants inside calculation formulas; daisy chains; merged cells
anywhere; hidden rows, columns or sheets; white text; deliberate circular references; blanket IFERROR.
The ramp factor is the case where this rule bites hardest; see section 0.1.

**Rounding:** display rounding only, through number formats. Never ROUND inside a calculation chain.
The one exception is a genuinely integer quantity such as headcount, documented in the register.

---

## 11. The disclosure register

| ID | Disclosure | Appears on |
| --- | --- | --- |
| D1 | Front-of-house labor, modeled at base wages only | 01, 04, 06 |
| D2 | Kitchen build authorship, pending founding chef partner | 01, 04, 06 |
| D3 | Best Case Year 1 equals Our Plan Year 1 by design | 01, 05, 07 |
| D4 | Covers held constant across cases | 05, 07 |
| D5 | Patio is 58.7% of seats; weather factor not applied | 03 |
| D6 | Excluded revenue channels, all at zero | 02, 11 |
| D7 | Cost of sales held flat across five years | 05, 11 |
| D8 | Fixed operating expense held flat across five years | 05, 11 |
| D9 | Corporate G&A excludes recruiting and a health plan at scale | 09 |
| D10 | Corporate G&A scaling is anchored on Year 2 revenue | 09 |
| D11 | Lease unsigned; all occupancy is letter-of-intent economics | 00, 01, 08, 10 |
| D12 | Year 1 corporate G&A carries a payroll calendar straddle | 04, 05 |
| D13 | Cash position stated; no monthly cash flow or runway schedule | 01, 08, 11 |
| D14 | No comparable-operator revenue is carried | 11 |
| D15 | Covers are persons served, not transactions | 03 |
| D16 | Revenue weeks 52, labor weeks 50 | 00, 11 |
| D17 | Founder compensation books three seats | 09, 11 |
| D18 | No returns, waterfall or IRR, by design | 00 |
| D19 | Rent commencement precedes opening; amount outside projections | 10, 11 |

**D1, full text as it appears on sheets 04 and 12:**

> Front-of-house labor is modeled at $15,402 per mature week, which is 10.21% of revenue. Full-wage
> fine dining commonly runs front-of-house labor between 15% and 20% of revenue. The difference is not
> a productivity claim and should not be read as one.
>
> A menu-embedded compensation structure has been designed for Sŏn. It is not modeled in this
> workbook, pending legal and regulatory review. Until that review completes and the structure is
> modeled, the labor line here reflects base wages only.
>
> This workbook makes no claim about what modeling that structure would do to the labor line. Read the
> 10.21% as incomplete rather than as favorable.

That last sentence is load-bearing. It is the difference between disclosure and spin, and it must
survive editing.

**D2, full text as it appears on sheets 04 and 12:**

> The kitchen labor build is a budget. It was authored by an operator whose professional depth is
> front of house, and it is expressed as a percentage of revenue by daypart with a shift build beneath
> it.
>
> A founding chef partner is being recruited and will own this line. Expect revision when that seat is
> filled. The figures here are a reasonable operator's budget for a kitchen, not a chef's build of
> this kitchen.

**D3, full text as it appears on sheets 01, 05, 07 and 12:**

> Our Plan and Best Case carry an identical Year 1. This is the model's design, not a duplicated
> figure. Best Case does not mean Sŏn opens stronger; it means Sŏn commands more once established.
> Both cases therefore share one opening year and separate from Year 2 through out-year pricing.
> Downside differs from Year 1 onward, because it carries both a demand adjustment and its own ramp.
>
> A case that changes only revenue cannot move a break-even, which is why Best Case and Our Plan share
> a break-even as well.

**D13, full text as it appears on sheets 01, 08 and 12:**

> This workbook states a cash position and does not contain a monthly cash flow or runway schedule.
>
> The cash position is the working capital and opening cash cushion, the Year 1 fixed cost block, and
> the number of months of fixed operating cost that cushion covers. Those are on sheet 08, shown for
> both the Lean Opening and Full Vision plans.
>
> The schedule is deferred rather than omitted. Rent commencement, the abatement schedule and the
> disbursement mechanics of the improvement allowance are all set by executed lease language, and the
> lease is not executed. A monthly schedule built on letter-of-intent terms would be rebuilt once the
> lease signs. It will be produced then.

**D15, full text as it appears on sheets 03 and 12:**

> A cover is one person served. It is not a transaction. A single transaction may serve more than one
> cover, for example two coffees bought together, so transactions per hour are lower than covers per
> hour.
>
> Covers per transaction is not modeled in this release, so this workbook states covers and covers per
> hour and does not state transaction counts. Where throughput matters, sheet 03 shows service hours,
> covers, covers per hour, seats, turn time and utilization, so no figure needs to be derived by the
> reader.

**D19, full text as it appears on sheets 10 and 12:**

> Rent commencement is currently recorded as 1 May 2027 against a planned opening in August 2027,
> roughly three months of rent before the restaurant earns revenue. At the letter-of-intent base rent
> that is $56,250, or $75,667.50 including NNN and CAM.
>
> That amount is not carried in any projection in this workbook. Commencement timing is a term under
> negotiation rather than a settled input, and modeling it as settled would misstate it in the other
> direction. It is disclosed here so the figure is visible rather than discovered.

**Remaining disclosures** are written to the same standard: state what is modeled, state what is not,
state why, and do not claim the direction of the correction.

---

## 12. Mechanics

### 12.1 Protection scheme

**No passwords.** Protect every sheet with `ws.protection.sheet = True` and no password argument. This
prevents accidental overtyping and permits any reader to unprotect in two clicks. Password protection
antagonizes diligence and signals that something is being withheld. Sheet 00 states that sheets are
protected without a password and that the reader may unprotect anything.

| Range | Master | Sandbox |
| --- | --- | --- |
| All exhibit sheets, all cells | Locked | Locked |
| Sheet 06, C11:C15 (levers) | Locked | **Unlocked** |
| Sheet 06, C4 (scenario selector) | Locked | **Unlocked** |
| Sheet 06, data table input cells | Locked | **Unlocked** |
| Sheet 10, rent sensitivity input cell | Locked | **Unlocked** |
| Sheet 13, all cells | Locked | Locked |

Workbook structure protected in both builds so sheets cannot be reordered or deleted accidentally.
Blank password again.

Master additionally carries the read-only recommended flag so it opens read-only and announces itself.

**Implementation order matters.** Cell protection is a style attribute in openpyxl. Apply all
formatting first, then set `cell.protection = Protection(locked=False)` on the input cells last, then
enable sheet protection. A later style assignment will silently overwrite an earlier protection
setting.

### 12.2 Input validation

Applied to C11:C15 on sheet 06 in the sandbox, via
`openpyxl.worksheet.datavalidation.DataValidation`.

| Lever | Type | Reject below | Reject above |
| --- | --- | --- | --- |
| F1 dinner covers index | Decimal | 50% | 150% |
| F2 dinner per-person average | Decimal | $30 | $90 |
| F3 non-dinner covers index | Decimal | 50% | 150% |
| F4 ramp curve | List | "Conservative", "Downside" | two values only |
| F5 out-year price uplift | Decimal | 0% | 15% |

**Error alert style: Stop.** Impossible values are rejected outright. Write the custom message to say
what the bound is and why, not "invalid entry".

**Aggressive but possible values are not rejected.** They are accepted, flagged by conditional
formatting, and reported in the status column as "Outside substantiated range". The workbook still
calculates. The reader is permitted to build a case the operator would not, and permitted to see that
they have done so.

**Blank behavior.** A blank lever cell is not silently replaced by its base value. It sets the status
column to "BLANK", fires the blank-input alert, and breaks check 15, which breaks the master flag.
Outputs remain visible so the reader can see what a blank produced, and the workbook says loudly that
they are not valid. Silent substitution is the failure mode this rule exists to prevent.

**Validation does not fire on paste.** This is native Excel behavior, not a library limitation. Check
15 recomputes bounds independently and catches a pasted out-of-range value. It is not optional.

### 12.3 Conditional formatting

Single-color rules and color scales only. No icon sets, which render inconsistently and carry meaning
that lives only in a glyph.

| Rule | Applies to | Format |
| --- | --- | --- |
| Lever outside substantiated range | Sheet 06 lever cells | Aubergine italic text |
| Lever blank | Sheet 06 lever cells | Onggi bold, Onggi hairline border |
| Check result "BREAK" | Sheet 13 result column | Onggi bold, Onggi hairline border |
| Check result "OK" | Sheet 13 result column | Peacock text |
| Master flag "BREAK" | Sheet 00 and freeze panes | Plum Ink fill, Bone text |
| Master flag "OK" | Sheet 00 and freeze panes | Bone fill, Peacock text |
| Negative Company EBITDA | Any bridge total row | Onggi bold |
| Below break-even | Sheet 06 output block | Aubergine italic |

**No meaning may live in color alone.** Every conditional format is accompanied by a text status in an
adjacent cell. This matters more than usual here, because the brand palette provides no amber and
because Peacock and Onggi sit at similar luminance, 6.52:1 and 5.78:1 on Bone, so they are not
reliably distinguishable in greyscale or to a reader with colour vision deficiency. The
differentiators that carry the meaning are the words themselves, the font weight, and the border:
failures are the only state with a border, warnings are the only state in italic.

### 12.4 Hex values by use

**Populated from Sŏn Brand Guidelines v1.0, section 05, Box file `2356731001214`.** The eight-color
palette is final: no tints, no shades, no exceptions.

The governing section of canon for this artifact is section 14, Deck Design Governing Principles,
which states that decks are an editorial format rather than a brand expression format, and that the
temporal arc does not govern them. A workbook is the same class of artifact: a document about the
restaurant, not the restaurant. Build to section 14, not to the daypart themes.

| Slot | Value | Name | Contrast | Canon basis |
| --- | --- | --- | --- | --- |
| `BRAND_PRIMARY` | `#120916` | Plum Ink | 15.81:1 with Bone text | Section title background |
| `BRAND_SECONDARY` | `#2E1F31` | Aubergine | 12.55:1 with Bone text | Statement callout, used as header bands |
| `BRAND_NEUTRAL_DARK` | `#120916` | Plum Ink | 19.51:1 on white, 15.81:1 on Bone | Body text |
| `BRAND_NEUTRAL_MID` | `#2E1F31` | Aubergine | 12.55:1 on Bone | Carried-figure italics |
| `BRAND_RULE` | `#3E5640` | Peacock | non-text | `son.color.border.default` |
| `SURFACE_DEFAULT` | `#EDE7D8` | Bone | 1.23:1 vs white | Default content background |
| `BRAND_NEUTRAL_LIGHT` | `#DBC9B0` | Parchment | 1.32:1 vs Bone | Alternating row banding |
| `INPUT_FILL` | `#C8D4BE` | Pale Jade | — | `son.color.pale-jade` |
| `INPUT_TEXT` | `#120916` | Plum Ink | 12.65:1 on Pale Jade | Text primary in morning resolution |
| `INPUT_BORDER` | `#3E5640` | Peacock | non-text | Canon permits Peacock as border and icon only |
| `STATUS_WARN` | `#2E1F31` | Aubergine, italic | 12.55:1 on Bone | See note |
| `STATUS_FAIL` | `#804A33` | Onggi, bold, with border | 5.78:1 on Bone | See note |
| `STATUS_PASS` | `#3E5640` | Peacock | 6.52:1 on Bone | Accent as category label, per section 14 |

All ratios computed against WCAG 2.2 and satisfy the AA floor for their use. Body text at 15.81:1
exceeds the AAA target canon sets for type-heavy surfaces.

**Structural usage rules carried from canon:**

- Dark fills are sparing. One Plum Ink title bar per sheet, thin Aubergine header bands on tables,
  everything else Bone. Canon prohibits Aubergine or Plum Ink as a content background and prohibits
  more than two consecutive dark surfaces without returning to a neutral.
- Type on any dark fill is Bone or Parchment only. Never Jade or Peacock on dark.
- One accent color in use at a time within a single visual block.
- No gradient fills of any kind.

**Three colors from the palette do not appear in the workbook, and here is why:**

- **Gold Foil `#BC9A5C`** is excluded absolutely. Canon enforces this structurally: the tokens
  `son.color.surface.foil` and `son.color.text.foil` do not exist, and foil is a physical production
  specification, never a flat fill. It also fails contrast at 2.15:1 on Bone. A spreadsheet is
  entirely flat fill, so there is no compliant use.
- **Jade `#8DA982`** fails as text everywhere: 2.09:1 on Bone, and canon explicitly prohibits Jade on
  Bone for text. It is available only as a non-text decorative element, and a spreadsheet has
  effectively no non-text surface. Jade does not appear.
- **Pale Jade `#C8D4BE`** appears only as the input fill. Canon records it as a derived token value
  rather than one of the eight brand colors, which is the correct register for a functional interface
  element.

**The status mapping is a decided departure, approved 22 August 2026. It is not an open RFC.**

Canon carries no functional status palette. The eight colors are identity, not function, and Brand
Guidelines v1.0 defines no error, warning or success value anywhere. Section 12 requires state
completeness including an error state but supplies no hex.

The resolution above stays inside the existing palette and invents nothing. It works because the
differentiation is carried by weight and border rather than by a fourth color: failures are the only
state with a border, warnings the only state in italic, and every conditional format is accompanied by
a text status. That is what makes the mapping safe in greyscale and for a reader with colour vision
deficiency, notwithstanding that Peacock and Onggi sit at similar luminance.

**There is no amber and none is invented.** The nearest warm mid-tone is Gold Foil, prohibited as fill
and failing contrast. The warning state is Aubergine italic with no fill change.

### 12.5 Fonts

**Workbook: Arial throughout. Courier New for reference codes and check identifiers.**
**PDF: GT Sectra for headings, GT Alpina Fine Standard for body, LNUM figures on every numeric column.**

**This is a decided departure from the canon fallback stack, approved 22 August 2026. It is not an
open RFC.**

Canon section 04 gives the fallback chains as GT Sectra to Cormorant Garamond to Georgia, and GT
Alpina to Source Serif 4 to Georgia. In a text document Georgia would be the correct terminal
fallback. It is wrong here for one reason: Georgia sets old-style figures by default, with varying
digit heights, and Excel exposes no OpenType feature control to switch them. Canon itself requires
lining figures for all tabular and pricing contexts, LNUM on both families. Georgia in a financial
column would therefore violate the canon rule it is being chosen to satisfy.

Arial has lining figures natively, is present on every Windows and macOS installation, and is
metrically compatible with Helvetica. It satisfies the locked constraint that workbook fonts come from
the cross-platform safe set, and it satisfies canon's tabular figure requirement. The brand faces
carry the identity in the PDF, where OpenType features are available and LNUM can be applied.

No other font may appear in the workbook. Brand typography does not go in the xlsx: an uninstalled
face substitutes silently, and the substitution is uncontrolled.

### 12.6 Number formats

| Content | Format |
| --- | --- |
| Annual currency | `$#,##0;($#,##0)` |
| Weekly currency | `$#,##0.00;($#,##0.00)` |
| Percentages | `0.00%` |
| Ramp factors | `0.000000` |
| Covers | `#,##0.0` where halves occur, `#,##0` otherwise |
| Rates entered as percentages | `0.00%` |
| Counts, seats, headcount | `#,##0` |

Lunch covers are 312.5 per service, a genuine half, so the covers format must carry one decimal where
the underlying figure does. Do not round it to 313 and break the cross-foot.

Ramp factors display at six decimals. **This is display rounding only.** The underlying cells are
formulas carrying full precision, per section 0.1, and the six-decimal display exists so a reader can
see roughly what the dropdown is doing without being able to mistake the display for the value.

**Fallback rule if data tables ever fail.** Native data tables are confirmed buildable per Part 1
section 1.3A, so this does not apply to the current build. If a future library or platform change
breaks them, do not substitute a precomputed grid that looks live. A grid that does not respond to a
reader's input, while sitting on a sheet whose whole promise is that inputs respond, is the single
most damaging thing this workbook could contain. Replace it with an explicitly static sensitivity
table, labeled "Computed at build, 22 August 2026. This table does not respond to the drivers above,"
and keep the live single-variable outputs elsewhere on the sheet.

---

## 13. Sandbox versus master

Build the master first and completely. Derive the sandbox from it. Never build them in parallel, or
they diverge invisibly.

**Derivation procedure:**

1. Save the master as the sandbox filename.
2. Unprotect sheets 06 and 10.
3. Unlock C4 and C11:C15 on sheet 06, the data table input cells on sheet 06, and the rent sensitivity
   input on sheet 10.
4. Apply `INPUT_FILL`, `INPUT_TEXT` and `INPUT_BORDER` to those cells.
5. Apply the data validation rules from section 12.2.
6. Re-protect sheets 06 and 10 with a blank password, leaving unlocked cells editable.
7. Insert a banner in row 1 of every sheet: "SANDBOX COPY. Values on this file may be changed. The
   master file is the canonical version."
8. Set every tab color to Aubergine `#2E1F31`.
9. Change sheet 00 cell B5 to "SANDBOX, editable".
10. Remove the read-only recommended flag.
11. Add the reset block below.
12. Recalculate in Excel and run the full check suite. Master flag must read OK.

**Reset without macros.** Sheet 06 carries a `Lev_Base` column holding the base value of each lever,
locked, beside the live column, with an instruction block:

> To restore the original settings: select the Base column, copy it, then select the Current column and
> use Paste Special, Values. This workbook contains no macros, so the reset is manual by design.

Naming the absence of macros as a design choice rather than a limitation matters. A reader who finds no
reset button and no explanation assumes the workbook is unfinished.

**Differences, complete list:** unlocked cells, input formatting, validation rules, the banner, tab
colors, cell B5, the read-only flag, the reset block. **Nothing else may differ.** If a figure differs
between master and sandbox, the build is wrong.

---

## 14. PDF export

The PDF carries the exhibit sheets only: 00, 01, 02, 03, 04, 05, 07, 08, 09, 10, 11, 12. Sheet 06 is
interactive and does not export meaningfully. Sheet 13 is the workings layer, available in the
workbook but not part of the exhibit.

**Brand typography lives in the PDF only**, which creates a divergence risk between workbook and PDF.
The export is therefore a controlled release step, not a live workbook state.

**Export procedure:**

1. Confirm the master check flag reads OK after recalculation in Excel.
2. Save a working copy as `_PDFPREP`. Never export from the master directly.
3. On the working copy, change fonts on the exhibit sheets: GT Sectra for headings per the canon
   hierarchy at section 04, GT Alpina Fine Standard for body. Apply LNUM figures to every numeric
   column, which canon requires for all tabular and pricing contexts. The exporting machine must have
   both faces installed and licensed for embedding.
4. Re-verify page breaks. A font change reflows every column width, and a sheet that fit one page in
   Arial may not fit in the brand faces. Adjust column widths, never font size, to restore fit.
5. Set print area, orientation and scaling per sheet. Sheets 01 and 05 are landscape one page wide.
   Sheet 11 may run multiple pages tall and must repeat its header row.
6. Footer on every page: file name, version, as-of date, page number of total.
7. Export as PDF at standard quality, which embeds fonts.
8. Verify embedding in the PDF's document properties. If a brand face did not embed, stop, and export
   in Arial rather than shipping a PDF that substitutes fonts on the reader's machine.
9. Discard the `_PDFPREP` copy. It is not a release artifact and must not reach Box.

**Licensing check before step 3.** Confirm GT Sectra and GT Alpina are licensed for PDF embedding. If
they are not, the PDF ships in Arial and the brand carries through hex alone. That is an acceptable
outcome and a better one than a licensing breach.

**Automation note.** If the pipeline exports headlessly, LibreOffice will substitute any font it cannot
find, silently. Verify the output rather than trusting the conversion.

---

## 15. Build order

1. Pull every figure fresh from Airtable and reconcile against Part 1 section 5. Any movement stops the
   build until this specification is reconciled.
2. Build sheet 02, then 03, then 04. The revenue spine first, because everything derives from it.
3. Build sheets 05, 07, 08, 09, 10.
4. Build sheets 11 and 12 from the register content in Part 1 section 5 and section 11 above.
5. Build sheet 06. It references everything, so it comes after. Build `Ramp_Factors` as formulas per
   section 8 F4.
6. Build sheet 13.
7. Build sheet 01. The summary is built last because it is entirely derived, and building it first
   invites typing figures that should be formulas.
8. Build sheet 00, including both bracketed placeholders exactly as written at Part 1 section 6.1.
9. Set `wb.calculation.fullCalcOnLoad = True` and save.
10. **Open in Excel and recalculate.** Verify every figure against Part 1 section 5 and every check at
    section 7. Save from Excel so cached values ship.
11. Run the release gates at section 16.
12. Derive the sandbox per section 13, recalculate, re-verify.
13. Export the PDF per section 14.

---

## 16. Release gates

Every gate passes or the workbook does not ship. A deadline is not a gate.

1. **Recalculation.** The file has been opened and recalculated in Excel or LibreOffice, and cached
   values ship with it. **A build script cannot verify itself, per Part 1 section 1.3D.** A build
   reporting success without this step has verified nothing.
2. **The no-narrator test.** Hand the file to someone who did not attend the meeting and did not build
   it. Every question they ask is a missing sentence. Add the sentence, retest.
3. **Reconciliation sweep.** Every figure traces to Airtable. Master check flag OK. Every cross-foot at
   section 7 passing, including checks 20, 21 and 22.
4. **Standing-rule sweep.** No em dashes anywhere, including cell comments and sheet names. "Customer"
   never "guest". No daypart code name anywhere, and note that canon marks Luxx as never public-facing.
   No vendor name for the kitchen automation line or any other unannounced vendor. No landlord name and
   no negotiation position. No performed-conviction language. No forbidden lexicon from canon
   section 09.
5. **Internal-only sweep.** No debt or financing structure, no landlord negotiation, no raw Airtable
   field, table or record identifiers, no comparable-operator revenue, no service-charge or point-pool
   mechanics.
6. **Hidden-content sweep.** No hidden sheets, rows or columns. No white text. No very-hidden sheets.
   Check the name manager for stale names and the workbook for stray external links.
7. **Disclosure completeness.** Every entry in section 11 appears on every sheet listed against it.
8. **Version stamp.** Sheet 00 carries version and as-of date. Footer carries both. Filename carries
   both.
9. **Prose handoff.** All workbook prose through House voice.
10. **Placeholder sweep. Blocking.** Neither bracketed placeholder from Part 1 section 6.1 may remain.
    Search the file for the character "[" and confirm zero results outside formula syntax. The
    admonition comes from the compliance seat; the contact line comes from Dominic. **The workbook does
    not ship with either placeholder in place.**

---

## 17. Routed items

No item blocks the build. Two are routed and neither prevents a complete workbook from being
constructed and verified.

**1. Early morning and lunch overlap on Monday and Tuesday. Routed to the CFO.**
Two dayparts claim the same 11am to 2pm window on two days, both carrying revenue and labor. The
workbook carries the schedule as the model carries it and notes the overlap in the register at
section 5. Not resolved in the workbook, and it does not stop the build: the figures foot either way,
because the overlap is a scheduling question rather than an arithmetic one.

**2. No monthly cash flow. Deferred by decision, reasoned.**
Rent commencement, abatement and allowance disbursement all come from executed lease language, so
building on letter-of-intent terms means building twice. Sheet 08 block 4 states the cash position that
can be stated now, for both plan views, and D13 states what is deferred and why. This remains a real
gap for a reader who wants a trough date. It is now a disclosed and reasoned gap rather than a silent
one, and it will be closed when the lease executes.

**Two items are pending content rather than pending decision:** the sheet 00 admonition and the contact
line. Both are bracketed placeholders, both are the builder's correct output, and gate 10 blocks
release until they are filled.

---

## 18. What this workbook does not contain, and why

Stated once so a builder does not add them back in good faith:

- **No returns, waterfall or IRR.** Locked constraint. The cover states the boundary and hands the
  return calculation to the reader's own advisor.
- **No Scenario Manager.** Not writable programmatically, and the dropdown replacement is better, per
  Part 1 section 1.3B.
- **No third ramp curve.** F4 carries two options. The 65% to 100% curve has no Airtable-computed
  Year 1 outcome and exposing it would require the monthly rebuild this specification excludes. It
  stays in the register as a documented alternative.
- **No typed ramp factors.** The factor cells are formulas. See section 0.1.
- **No comparable-operator revenue.** The model previously carried revenue attributed to five named
  local businesses with no source. Those were removed on 22 August 2026. No sourced comparable set
  exists, so no comparables sheet is built. Item 19 discipline forbids an average without its median
  and range, and there is nothing here to average.
- **No walk-away threshold.** Decided 22 August 2026. Reasoning at section 4.1.
- **No capital levers.** Locked constraint. The raise is fixed at $2,500,000 and the sources and uses
  is not adjustable.
- **No monthly cash flow or runway schedule.** Deferred by decision. See section 17 item 2.
- **No pre-opening six-month use schedule.** Out of scope by decision. Pre-opening labor comes from the
  position-level wage schedule and appears at sheet 08 block 3.
- **No industry benchmark bands.** None are sourced in the model. Every alert fires against the
  workbook's own break-even instead. Where a benchmark range is stated, as in D1's 15% to 20%, it is
  described as commonly observed rather than cited, and it is used to make a number look incomplete
  rather than to make one look good.
- **No team argument.** The deck and the plan argue the team. This workbook argues the numbers those
  documents promised.
