---
name: equipment-record
description: Create or update an equipment/<slug>.yaml record from a spec sheet, model number, or product page. Use for any piece of equipment that will appear in a layout.
---
# Equipment record

1. Delegate extraction to the `equipment-librarian` subagent (Haiku) with the spec sheet or model number.
2. The record must validate against `equipment/schema.json`. Start from `equipment/_template.yaml`.
3. `dimensions.status: verified` only when a manufacturer spec sheet is cited in `sources` with a retrieval date. Otherwise `estimated`.
4. Capture every utility the install needs: electrical (volts, phase, amps, plug type), water (size, pressure, filtration), drain (direct or indirect, size), gas (BTU, connection), ventilation (hood or not), refrigeration heat rejection, and required clearances.
5. For equipment sold outside the US, fill `certifications` honestly. Default note: "inspiration only" unless a UL/ETL-listed and NSF-listed US variant exists.
6. Store the spec sheet PDF in Box, then record its file ID and SHA1 in `sources`.
7. Run `python3 scripts/validate_equipment.py equipment/<slug>.yaml`.
