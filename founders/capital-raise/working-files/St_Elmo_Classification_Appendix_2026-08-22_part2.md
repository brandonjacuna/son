# St. Elmo Dashboard V2, field classification appendix

Part 2 of 2. Companion to `St_Elmo_Classification_Main_2026-08-22.md`.

Base: St. Elmo Dashboard V2 (Airtable). Classified 22 August 2026, read-only.
The base was frozen; nothing was written to it.

Every live field in the base, sorted into exactly one class.

| Code | Meaning |
| --- | --- |
| AS-IS | Goes to the investor workbook unchanged |
| DERIVED | Informs a figure that ships, but not in this form |
| INTERNAL | Never leaves the base |

`F` marks a low-confidence row: a judgment call, a field whose name misstates what it
computes, or something a reader could misread without context. Every flagged row is
written up in section 6 of the main document.

Excluded as retired and not counted: 56 fields prefixed `DELETE`, 24 prefixed `LEGACY`.

Totals across both parts: 773 live fields. AS-IS 145, DERIVED 345, INTERNAL 283.
39 rows are flagged.

Tables in this part: Lunch Model, Late Night Model, Cash Flow, CapEx: FF&E, CapEx: OS&E, CapEx: Pre-Opening Expenses, CapEx: Reserves & Deposits, CapEx: Leasehold Improvements, Uniforms, Funding Treatment Schedule, Multi-Daypart Summary, Phase 1 Labor Case, Pre-Opening Six-Month Use Schedule, Lean Sources and Uses, Analysis: Seating Capacity Cases, Sources and Assumptions, Redcar Property Research, Lease Term Risk Summary, Lease Delivery Matrix, Lease: Rent Burden Analysis, Analysis: Seating Capacity Check, Model Assumptions, Lease Signing Cash Scenarios, LHI Working Budget, Landlord Direct Work Requests, Model Index, Lease: Rent Basis Sensitivity, Hardcoded Input Inventory, Labor: BOH Shift Build, Scaling View: Corporate G&A, Analysis: Break-Even

---

## Lunch Model

42 live fields. AS-IS 0, DERIVED 33, INTERNAL 9.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Lunch Format | INTERNAL | Record names carry a daypart code name |  |
| Service Type | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Days Per Week | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Daily Covers/Orders | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Average Check | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Food Cost % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Beverage Cost % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| FOH Hours Per Day | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| FOH Hourly Wage | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| BOH Hours Per Day | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| BOH Hourly Wage | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| 3PD Commission % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| 3PD Mix % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Packaging Cost Per Order | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Strategic Context | DERIVED | Positioning commentary; ships rewritten |  |
| Active | INTERNAL | Active flag points at a record that does not drive the model | * |
| Daily Revenue | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Revenue | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Daily FOH Labor | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Daily BOH Labor | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Daily Total Labor | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Total Labor | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Food Cost | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly 3PD Fees | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Packaging | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Contribution | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Labor % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Contribution Margin % | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| P&L Model | INTERNAL | Relational link, not data |  |
| Annual Revenue (50W) | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Annual Contribution (50W) | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Revenue Per Labor Hour | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Contribution Per Cover | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Weekly Labor Hours | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Operational Independence | INTERNAL | Internal portfolio strategy signal |  |
| Concept Incubator Value | INTERNAL | Internal portfolio strategy signal |  |
| Staff Cross-Training Required | DERIVED | Cross-training requirement behind the shared-crew argument |  |
| Ecosystem Customer Capture | INTERNAL | Internal portfolio strategy signal |  |
| Standalone Location Potential | INTERNAL | Signals concepts outside the single-unit scope |  |
| Weekly Covers | DERIVED | Parallel lunch build; does not feed the canonical mature week |  |
| Scenario Timeline | INTERNAL | Relational link, not data |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |

## Late Night Model

26 live fields. AS-IS 0, DERIVED 24, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Late Night Format | DERIVED | Format label; ships restated |  |
| Service Type | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Days Per Week | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Daily Covers/Orders | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Average Check | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Food Cost % | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Beverage Cost % | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| FOH Hours Per Day | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| FOH Hourly Wage | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| BOH Hours Per Day | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| BOH Hourly Wage | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Strategic Context | DERIVED | Positioning commentary; ships rewritten |  |
| Operational Independence | INTERNAL | Internal portfolio strategy signal |  |
| Concept Incubator Value | INTERNAL | Internal portfolio strategy signal |  |
| Daily Revenue | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Weekly Revenue | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Weekly Labor | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Weekly Contribution | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Labor % | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Contribution Margin % | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Revenue Per Labor Hour | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Weekly Covers | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Annual Revenue (50W) | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Annual Contribution (50W) | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Weekly Labor Hours | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |
| Contribution Per Cover | DERIVED | Parallel late-night build; does not feed the canonical mature week |  |

## Cash Flow

6 live fields. AS-IS 0, DERIVED 0, INTERNAL 6.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Month ID | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |
| Month Number | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |
| Calendar Month | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |
| Phase | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |
| Cash In | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |
| Cash Out | INTERNAL | Incomplete 2025 placeholder; not usable for runway |  |

## CapEx: FF&E

11 live fields. AS-IS 0, DERIVED 5, INTERNAL 6.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item Name | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Location | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Unit Cost | DERIVED | Line cost; ships inside a uses category |  |
| Quantity | DERIVED | Line quantity; ships inside a uses category |  |
| Total Cost | DERIVED | Line cost; ships inside a uses category |  |
| Brandon Notes | INTERNAL | Founder working commentary |  |
| VE Round 1 Status | INTERNAL | Value-engineering review state |  |
| Reasoning & Context | INTERNAL | Internal buying rationale |  |
| Dominic's Ask | INTERNAL | Internal founder-to-founder review request |  |
| Reference Link | INTERNAL | Vendor links, relationships unannounced |  |
| Legacy Task ID | INTERNAL | Internal record key |  |

## CapEx: OS&E

13 live fields. AS-IS 0, DERIVED 7, INTERNAL 6.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item Name | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Department | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Location | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Category | DERIVED | Capital budget line; ships as a summarised uses category |  |
| Unit Cost | DERIVED | Line cost; ships inside a uses category |  |
| Quantity | DERIVED | Line quantity; ships inside a uses category |  |
| Total Cost | DERIVED | Line cost; ships inside a uses category |  |
| Brandon Notes | INTERNAL | Founder working commentary |  |
| VE Round 1 Status | INTERNAL | Value-engineering review state |  |
| Reasoning & Context | INTERNAL | Internal buying rationale |  |
| Reference Link | INTERNAL | Vendor links, relationships unannounced |  |
| Dominic's Ask | INTERNAL | Internal founder-to-founder review request |  |
| Legacy Task ID | INTERNAL | Internal record key |  |

## CapEx: Pre-Opening Expenses

16 live fields. AS-IS 3, DERIVED 3, INTERNAL 10.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item Name | DERIVED | Pre-opening budget line; ships as a summarised uses category |  |
| Category | DERIVED | Pre-opening budget line; ships as a summarised uses category |  |
| Original Budget | AS-IS | Full-plan cost line in sources and uses |  |
| Brandon Notes | INTERNAL | Founder working commentary |  |
| VE Round 1 Status | INTERNAL | Value-engineering review state |  |
| Reasoning & Context | INTERNAL | Internal buying rationale |  |
| Dominic's Ask | INTERNAL | Internal founder-to-founder review request |  |
| VE Round 1 Changes | INTERNAL | Value-engineering review state |  |
| Opening Tier | DERIVED | Lean versus full opening tier; ships as the two plan views |  |
| Funding Source | INTERNAL | Financing structure |  |
| TI Eligibility | INTERNAL | Landlord allowance eligibility; lease strategy |  |
| Legacy Task ID | INTERNAL | Internal record key |  |
| Lean Opening Cost | AS-IS | Lean-plan cost line in sources and uses |  |
| Savings | AS-IS | Delta between the two plan views |  |
| Lean Notes | INTERNAL | Working commentary |  |
| Original Notes | INTERNAL | Working commentary |  |

## CapEx: Reserves & Deposits

10 live fields. AS-IS 0, DERIVED 4, INTERNAL 6.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item Name | DERIVED | Reserve and deposit line; ships as a summarised uses category |  |
| Unit Cost | DERIVED | Line cost; ships inside a uses category |  |
| Quantity | DERIVED | Line quantity; ships inside a uses category |  |
| Total Cost | DERIVED | Line cost; ships inside a uses category |  |
| Brandon Notes | INTERNAL | Founder working commentary |  |
| VE Round 1 Status | INTERNAL | Value-engineering review state |  |
| Reasoning & Context | INTERNAL | Internal buying rationale |  |
| Dominic's Ask | INTERNAL | Internal founder-to-founder review request |  |
| VE Round 1 Changes | INTERNAL | Value-engineering review state |  |
| Legacy Task ID | INTERNAL | Internal record key |  |

## CapEx: Leasehold Improvements

14 live fields. AS-IS 0, DERIVED 7, INTERNAL 7.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| LHI Line Item | DERIVED | Buildout line; ships as a summarised uses category |  |
| Delivered by | INTERNAL | Landlord versus tenant delivery; lease negotiation |  |
| Description | DERIVED | Buildout line; ships as a summarised uses category |  |
| Location | DERIVED | Buildout line; ships as a summarised uses category |  |
| Category | DERIVED | Buildout line; ships as a summarised uses category |  |
| Quantity | DERIVED | Line quantity; ships inside a uses category |  |
| Unit Cost | DERIVED | Line cost; ships inside a uses category |  |
| Total Cost | DERIVED | Line cost; ships inside a uses category |  |
| Context | INTERNAL | Working commentary |  |
| Status | INTERNAL | Internal buildout tracking |  |
| Contractor / Vendor | INTERNAL | Vendor relationship unannounced |  |
| Start Date | INTERNAL | Internal buildout schedule |  |
| End Date | INTERNAL | Internal buildout schedule |  |
| Manual sort | INTERNAL | Airtable sort control, not data |  |

## Uniforms

7 live fields. AS-IS 0, DERIVED 4, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item Name | DERIVED | Small pre-opening cost line; ships inside a uses category |  |
| Quantity | DERIVED | Line quantity; ships inside a uses category |  |
| Purchase Cost | DERIVED | Small pre-opening cost line; ships inside a uses category |  |
| Total Cost | DERIVED | Line cost; ships inside a uses category |  |
| Source URL | INTERNAL | Vendor links, relationships unannounced |  |
| Notes | INTERNAL | Working commentary |  |
| Legacy Task ID | INTERNAL | Internal record key |  |

## Funding Treatment Schedule

5 live fields. AS-IS 0, DERIVED 0, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Use Category | INTERNAL | Maps uses to financing treatment including debt; financing structure |  |
| TI Eligibility | INTERNAL | Lease strategy or landlord negotiation |  |
| Equity Funded/SBA7a | INTERNAL | Financing structure |  |
| Recommended Funding Treatment | INTERNAL | Financing structure |  |
| Notes | INTERNAL | Working commentary |  |

## Multi-Daypart Summary

19 live fields. AS-IS 0, DERIVED 17, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Configuration | DERIVED | Configuration label; ships restated |  |
| Dinner Weekly Revenue | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Dinner Weekly Contribution | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Dinner EBITDA % | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Lunch Weekly Revenue | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Lunch Weekly Contribution | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Lunch Contribution Margin % | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Late Night Weekly Revenue | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Late Night Weekly Contribution | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Late Night Contribution Margin % | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Late Night Annual (50W) | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Combined Weekly Revenue | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Combined Weekly Contribution | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Annual Revenue (50W) | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Annual Contribution (50W) | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Delta vs Dinner Only (Revenue) | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| Delta vs Dinner Only (Contribution) | DERIVED | Daypart contribution comparison; supports the multi-daypart argument |  |
| In Base Projections | INTERNAL | Internal inclusion flag |  |
| Strategic Notes | INTERNAL | Internal strategy commentary |  |

## Phase 1 Labor Case

12 live fields. AS-IS 0, DERIVED 0, INTERNAL 12.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Role / Position | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Department | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Current Headcount | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Current Annualized Cost | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Phase 1 Headcount | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Phase 1 Annualized Cost | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Annualized Savings | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Required Pre-Opening? | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Automation Offset? | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Partner Absorbed? | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Phase 2 Trigger | INTERNAL | Headcount reduction case; exposes unfilled and partner-absorbed roles |  |
| Notes | INTERNAL | Working commentary |  |

## Pre-Opening Six-Month Use Schedule

12 live fields. AS-IS 1, DERIVED 9, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Month | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Founder / Operator Draw | DERIVED | Founder pre-opening draw; ships inside pre-opening uses |  |
| Sous Chef Salary | INTERNAL | Names the only pre-opening kitchen hire, framing the senior seat as open | * |
| F&B / Drink R&D | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Training | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Opening Inventory | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Insurance | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Uniforms | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Graphic Design | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Opening Event / Sponsor Cash | DERIVED | Pre-opening cash use by month; ships inside sources and uses |  |
| Total Month Cash Use | AS-IS | Pre-opening cash use by month |  |
| Notes | INTERNAL | Working commentary |  |

## Lean Sources and Uses

7 live fields. AS-IS 4, DERIVED 0, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Use / Source | AS-IS | Sources and uses line label |  |
| Full Vision | AS-IS | Full-plan uses column |  |
| Lean Opening | AS-IS | Lean-plan uses column |  |
| Savings | AS-IS | Delta between the two plan views |  |
| TI Eligibility | INTERNAL | Landlord allowance eligibility; lease strategy |  |
| Funding Source | INTERNAL | Names debt and vendor financing; financing structure |  |
| Notes | INTERNAL | Carries landlord negotiation history and superseded debt structure |  |

## Analysis: Seating Capacity Cases

8 live fields. AS-IS 0, DERIVED 6, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Case | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Indoor Seats | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Outdoor Seats | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Total Seats | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Indoor % | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Outdoor % | DERIVED | Seat-count stress cases behind the capacity argument |  |
| Revenue Use | INTERNAL | Internal modelling instruction |  |
| Notes | INTERNAL | Working commentary |  |

## Sources and Assumptions

5 live fields. AS-IS 0, DERIVED 4, INTERNAL 1.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Item | DERIVED | Citation register line |  |
| Value | DERIVED | Citation register value |  |
| Units | DERIVED | Citation register unit |  |
| Source | DERIVED | Citation; screen for landlord and vendor references | * |
| Notes | INTERNAL | Working commentary |  |

## Redcar Property Research

5 live fields. AS-IS 0, DERIVED 0, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Fact | INTERNAL | Landlord financial-condition research; never an investor surface |  |
| Value | INTERNAL | Landlord financial-condition research; never an investor surface |  |
| Amount | INTERNAL | Landlord financial-condition research; never an investor surface |  |
| Source | INTERNAL | Landlord financial-condition research; never an investor surface |  |
| Finance Notes | INTERNAL | Working commentary |  |

## Lease Term Risk Summary

8 live fields. AS-IS 0, DERIVED 0, INTERNAL 8.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Term | INTERNAL | Lease negotiation positions and risk catches |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| LOI Language | INTERNAL | Lease strategy or landlord negotiation |  |
| Financial Impact | INTERNAL | Lease negotiation positions and risk catches |  |
| Risk / Catch | INTERNAL | Lease negotiation positions and risk catches |  |
| Model Treatment | INTERNAL | Lease negotiation positions and risk catches |  |
| Negotiation Ask | INTERNAL | Lease strategy or landlord negotiation |  |
| Source | INTERNAL | Lease negotiation positions and risk catches |  |

## Lease Delivery Matrix

9 live fields. AS-IS 0, DERIVED 0, INTERNAL 9.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scope Area | INTERNAL | Landlord versus tenant delivery negotiation scope |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Landlord Delivers | INTERNAL | Lease strategy or landlord negotiation |  |
| Tenant Responsible For | INTERNAL | Landlord versus tenant delivery negotiation scope |  |
| Likely Cost Owner | INTERNAL | Landlord versus tenant delivery negotiation scope |  |
| Funding Treatment | INTERNAL | Financing structure |  |
| Cost Risk | INTERNAL | Landlord versus tenant delivery negotiation scope |  |
| Open Items | INTERNAL | Landlord versus tenant delivery negotiation scope |  |
| Source | INTERNAL | Landlord versus tenant delivery negotiation scope |  |

## Lease: Rent Burden Analysis

10 live fields. AS-IS 3, DERIVED 5, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scenario | DERIVED | Canonical occupancy table; ships as an occupancy summary |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Annual Sales | AS-IS | Sales basis for the occupancy ratio |  |
| Base Rent | DERIVED | Canonical occupancy table; ships as an occupancy summary |  |
| NNN Estimate | DERIVED | Canonical occupancy table; ships as an occupancy summary |  |
| Percentage Rent | DERIVED | Canonical occupancy table; ships as an occupancy summary |  |
| Total Occupancy | AS-IS | Total occupancy cost |  |
| Occupancy % of Sales | AS-IS | Occupancy as a share of sales, a standard operator ratio |  |
| Monthly Fixed Occupancy Before % Rent | DERIVED | Canonical occupancy table; ships as an occupancy summary |  |
| Finance Notes | INTERNAL | Internal lease commentary |  |

## Analysis: Seating Capacity Check

10 live fields. AS-IS 3, DERIVED 4, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Area | AS-IS | Area label |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Documented SF | AS-IS | Documented square footage by area |  |
| Conservative Seats | DERIVED | Downside seat case |  |
| Base Planning Seats | AS-IS | The 126-seat planning basis |  |
| Aggressive Seats | DERIVED | Upside seat case |  |
| Planning Notes | INTERNAL | Working commentary |  |
| Constraints | DERIVED | Physical constraints; ship restated |  |
| Model Treatment | INTERNAL | Internal modelling instruction |  |
| Source | DERIVED | Citation |  |

## Model Assumptions

6 live fields. AS-IS 0, DERIVED 4, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Assumption | DERIVED | Assumption label; ships after record screening and rewrite |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Value | DERIVED | Assumption value; ships after record screening |  |
| Dollar Value | DERIVED | Assumption value; ships after record screening |  |
| Notes | INTERNAL | Working commentary |  |
| Source | DERIVED | Citation; several cite the Redcar proposal and must be restated | * |

## Lease Signing Cash Scenarios

9 live fields. AS-IS 0, DERIVED 0, INTERNAL 9.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scenario | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Monthly Occupancy | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Security Deposit Months | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Security Deposit | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| First Month Prepaid Rent | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Utility Deposit | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Total Signing Cash | INTERNAL | Deposit and prepaid-rent negotiation cases |  |
| Finance Notes | INTERNAL | Working commentary |  |

## LHI Working Budget

10 live fields. AS-IS 0, DERIVED 5, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scope Category | DERIVED | Buildout scope grouping |  |
| Line Item | DERIVED | Buildout line label |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Low Estimate | DERIVED | Buildout range; ships as a single figure |  |
| Base Estimate | DERIVED | Buildout base case; ships as a single figure |  |
| High Estimate | DERIVED | Buildout range; ships as a single figure |  |
| TI Funding Gap | INTERNAL | Landlord allowance gap; lease strategy |  |
| Funding Treatment | INTERNAL | Financing structure |  |
| Lease Basis | INTERNAL | Lease delivery obligations; negotiation |  |
| Pricing Notes | INTERNAL | Working commentary |  |

## Landlord Direct Work Requests

5 live fields. AS-IS 0, DERIVED 0, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Ask Item | INTERNAL | Direct asks to the landlord; live negotiation |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Value Shift | INTERNAL | Direct asks to the landlord; live negotiation |  |
| Why It Is Fair | INTERNAL | Direct asks to the landlord; live negotiation |  |
| Fallback | INTERNAL | Direct asks to the landlord; live negotiation |  |

## Model Index

6 live fields. AS-IS 0, DERIVED 0, INTERNAL 6.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Section | INTERNAL | Raw table names and internal reconciliation notes |  |
| Table | INTERNAL | Raw table names and internal reconciliation notes |  |
| Role | INTERNAL | Raw table names and internal reconciliation notes |  |
| Status | INTERNAL | Raw table names and internal reconciliation notes |  |
| Presentation Note | INTERNAL | Raw table names and internal reconciliation notes |  |
| Sort | INTERNAL | Airtable sort control, not data |  |

## Lease: Rent Basis Sensitivity

12 live fields. AS-IS 0, DERIVED 0, INTERNAL 12.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Case | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Sort | INTERNAL | Airtable sort control, not data |  |
| Base Rent | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Additional Rent Basis SF | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Additional Rent PSF | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Estimated Additional Rent | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Fixed Occupancy Before Percentage Rent | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Monthly Fixed Occupancy | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Natural Breakpoint | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Model Treatment | INTERNAL | Rent-basis negotiation sensitivity cases |  |
| Finance Notes | INTERNAL | Working commentary |  |
| Source | INTERNAL | Rent-basis negotiation sensitivity cases |  |

## Hardcoded Input Inventory

21 live fields. AS-IS 0, DERIVED 0, INTERNAL 21.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Inventory Key | INTERNAL | Raw Airtable identifier |  |
| Source Table | INTERNAL | Raw Airtable identifier |  |
| Source Table ID | INTERNAL | Raw Airtable identifier |  |
| Source Field | INTERNAL | Raw Airtable identifier |  |
| Source Field ID | INTERNAL | Raw Airtable identifier |  |
| Field Type | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Input Classification | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Model Domain | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Source Record Count | INTERNAL | Raw Airtable identifier |  |
| Nonblank Value Count | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Review State | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Field Description | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Allowed Choices | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Current Use State | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Canonical Path / Dependency | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Value Scan State | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Observed Nonblank Values | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Schema Scanned At | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Audit Note | INTERNAL | Working commentary |  |
| Is Primary Field | INTERNAL | Raw Airtable table, field and record identifiers |  |
| Linked Table ID | INTERNAL | Raw Airtable identifier |  |

## Labor: BOH Shift Build

13 live fields. AS-IS 0, DERIVED 10, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Crew Line | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Crew | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Position | INTERNAL | Relational link, not data |  |
| Headcount | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Shift Start | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Shift End | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Hours Per Shift | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Days Per Week | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Serves Dayparts | INTERNAL | Relational link, not data |  |
| Notes | INTERNAL | Working commentary |  |
| Hourly Wage | DERIVED | Lookup of an upstream value; ships through its source |  |
| Weekly Hours | DERIVED | Kitchen shift build behind the BOH labor line |  |
| Weekly Cost | DERIVED | Kitchen shift build behind the BOH labor line |  |

## Scaling View: Corporate G&A

11 live fields. AS-IS 10, DERIVED 1, INTERNAL 0.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Unit Count | AS-IS | Corporate G&A scaling at one, two and three units |  |
| Units | AS-IS | Corporate G&A scaling at one, two and three units |  |
| Annual Revenue | AS-IS | Corporate G&A scaling at one, two and three units |  |
| Founder Compensation | AS-IS | Founder compensation, the whole of corporate G&A at one unit |  |
| Founder Payroll Burden | AS-IS | Corporate G&A scaling at one, two and three units |  |
| Recruiting | AS-IS | Held at zero by decision; must ship with the caveat | * |
| ACA Health Plan | AS-IS | Held at zero by decision; must ship with the caveat | * |
| Corporate Hire | AS-IS | Third-unit corporate seat, booked |  |
| Basis | DERIVED | Method notes including two step-ups held at zero; ships rewritten | * |
| Total Corporate G&A | AS-IS | Corporate G&A scaling at one, two and three units |  |
| Corporate G&A % of Revenue | AS-IS | Corporate G&A scaling at one, two and three units |  |

## Analysis: Break-Even

15 live fields. AS-IS 14, DERIVED 1, INTERNAL 0.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Case | AS-IS | Break-even case label |  |
| Scenario | AS-IS | Scenario the case belongs to |  |
| Cost Basis | AS-IS | Year 1 versus steady state basis |  |
| Annual Fixed Cost Block | AS-IS | Break-even by scenario and cost basis |  |
| COGS % | AS-IS | Break-even by scenario and cost basis |  |
| Variable OpEx % | AS-IS | Break-even by scenario and cost basis |  |
| Percentage Rent Rate | AS-IS | Break-even by scenario and cost basis |  |
| Natural Breakpoint | AS-IS | Break-even by scenario and cost basis |  |
| Mature Weekly Covers | AS-IS | Break-even by scenario and cost basis |  |
| Mature Annual Revenue | AS-IS | Break-even by scenario and cost basis |  |
| Notes | DERIVED | Method notes; ship rewritten as exhibit footnotes |  |
| Contribution Margin % | AS-IS | Break-even by scenario and cost basis |  |
| Break-Even Annual Revenue | AS-IS | Break-even by scenario and cost basis |  |
| Break-Even Weekly Revenue | AS-IS | Break-even by scenario and cost basis |  |
| Break-Even Covers per Day | AS-IS | Break-even by scenario and cost basis |  |
