# Sŏn Learning Studio

The working environment for identifying, ideating, and generating Sŏn's education and training modules.

It builds module **source packages** that stay independent of any operational tool. Everything that depends on an unset tool or workflow is a declared binding, so a finished module can sit parked until the operation is ready, then be bound and rendered to Trainual, Synthesia, print, or a live pre-shift in a short session.

## Setup (once)

1. Work in `company/workstreams/learning-studio/` inside the private `son` repo. Keep the repo private: modules describe internal operations.
2. Install Python 3.10 or newer, then `pip install -r requirements.txt`.
3. Open the folder in Claude Code. Use the Box and ClickUp connectors (cloud sessions) and sign in to each. Disable any you are not using that session. The studio's `.mcp.json` and slash commands are not in this folder: tooling is salvaged and inert until phase 5 (`_salvage/README.md`).
4. Profiles: repo `profiles/` (phase 3 rebuilds the profile system).
5. `/status` is salvaged tooling (inert until phase 5, `_salvage/README.md`). Read `catalog/catalog.yaml` for the catalog.

## Daily use

The slash commands below are salvaged tooling, inert until phase 5 (`_salvage/README.md`).

- New training need: `/identify`
- Work a module forward: `/ideate`, `/design-module`, `/draft-module`, `/review-module`, `/park-module`
- When a tool or workflow gets set: `/bind` with the binding key, for example `/bind tool.pos`, to see and fill every module that depends on it
- Ready to publish: `/render MOD-ID trainual`
- See a scenario as a learner would: `python scripts/build_scorm.py modules/_example/EX-001-allergy-at-the-table`, unzip the file in `exports/`, open `index.html`

## Before the first real render

Run the capability tour in `adapters/trainual.md`: one sandbox subject that uses every Trainual option (all five test types, checklist, flowchart, embed, SCORM, video response, e-signature), taken on a phone, with a note of what each one records.

## Map

```
CLAUDE.md               Instructions Claude Code reads every session
canon/                  Standing rules and live pointers (IDs only, no copied content)
profiles/manifest.yaml  Which Box profiles this studio uses, and for which stage
profiles/cache/         Pulled profile copies (git-ignored); profiles: repo `profiles/` (phase 3 rebuilds the profile system)
framework/              Lifecycle, module spec, bindings, review panels, modality library
templates/              Intake, concept brief, and the module package template
catalog/catalog.yaml    Every module and its status
modules/                Module source packages, one folder per module
bindings/registry.md    Generated report of every open binding across modules
adapters/               Researched capability maps and render guides: Trainual, SCORM, Synthesia, live and print
scorm/player/           The branching scenario player packaged by build_scorm.py
profile-builds/         Workspace for building new profiles before they go to Box
scripts/                lint.py (standing rules), status.py (catalog, bindings, variety), build_scorm.py
exports/                Rendered output (git-ignored)
```
