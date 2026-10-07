# 0001: Workspace architecture

Date: 2026-09-28. Status: accepted.

## Decision
One private GitHub repo, run by Claude Code in two modes:
- Cloud (Claude Code on the web, Ubuntu): research, monitoring, headless geometry (build123d, IfcOpenShell, ezdxf), exports, docs.
- Local (Claude Desktop Code tab on Brandon's Mac): GUI CAD over MCP (Blender + Bonsai for IFC, FreeCAD; SketchUp Pro later).

## Stack (start at near $0)
Core now: build123d/CadQuery, IfcOpenShell + Blender/Bonsai, FreeCAD, ezdxf, KCL CADalog web (free manufacturer downloads), Zoo (free tier, optional).
Later: SketchUp Pro when layout iteration is weekly. Fusion Startup only if the fabricator uses Fusion.
Skip: Revit (Windows only), Fusion personal (non-commercial license), AutoCAD LT, Vectorworks, Archicad.
Plan: Claude Max 5x. Fable via /deep only.

## Handoff
IFC model + DXF/DWG plan layers + PDF sheet set + equipment schedule (CSV/XLSX from equipment YAML). Native files on request. Fabrication: STEP + PDF drawing + DXF flats, 3MF for printing, weld symbols on drawings, never G-code.

## Phases and gates
| Phase | Entry gate |
|---|---|
| P0 Concept | default |
| P1 Design | /lease-signed + executed lease in Box + typed phrase |
| P2 Permitting | architect engaged, real design plans in Box, /gate review passed |
| P3 Construction | permit issued |
| P4 Closeout | certificate of occupancy received |

## Enforcement
PreToolUse hook blocks writes to locked phase folders and to PHASE.yaml, hooks, and state. A UserPromptSubmit hook opens a 10-minute unlock window only when Brandon types a confirmation phrase. ClickUp writes: capture lists allowed, other writes ask, deletes denied.

## Model routing
haiku: triage, extraction, diffs, monitoring. sonnet: default design work. opus: code interpretation, live fire ventilation, clash review, gate reviews. Fable: /deep only.

## Build plan
Week 1: foundation (this commit). Weeks 2 to 3: equipment records, parametric bar module library, local MCP install, first bar concept and live-fire envelope. Weeks 3 to 4: monitoring routine, profile-forge, first six specialist profiles. Month 2: export pipeline, fabrication workflow, SketchUp decision.
