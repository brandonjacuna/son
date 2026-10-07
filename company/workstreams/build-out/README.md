# son-build

Sŏn's construction-mode workspace for Claude Code. Owner: Brandon John Acuña-Cardona. Design intent, research, and build-out planning for the restaurant. Read `CLAUDE.md` for the rules Claude follows and `decisions/0001-architecture.md` for why it is built this way.

Moving into the unified `son` repo? Follow `HANDOFF.md` instead of the setup below.

## One-time setup, standalone repo (Brandon)

1. **Put it on GitHub.** Easiest: install GitHub Desktop (free), then File > Add Local Repository > pick this folder > "create a repository" > Publish, and keep **Private** checked.
   Finder hides folders that start with a dot (`.claude`, `.github`); GitHub Desktop still includes them. Do not use drag-and-drop upload on github.com, which can drop them.
   Terminal alternative: `cd son-build && git init && git add -A && git commit -m "Foundation" && gh repo create son-build --private --source . --push`
2. **Git LFS** (stores large CAD and image files): `brew install git-lfs && git lfs install`, once per Mac.
3. **Cloud environment.** At claude.ai/code, connect GitHub, pick `son-build`, create an environment, and paste `scripts/setup_cloud.sh` into Setup script. Keep network access on the default trusted list.
4. **Connectors.** In claude.ai Settings > Connectors, make sure ClickUp and Box are connected, so cloud sessions can use them.
5. **Local.** In the Claude Desktop app, Code tab, open the `son-build` folder. Local sessions are where Blender and FreeCAD get driven.
6. **GitHub Actions.** On the repo page, Actions tab > enable workflows. Create an issue label named `watch`.
7. Paste `KICKOFF.md` into a new cloud session.

## Commands
| Command | What it does |
|---|---|
| `/intake` | Triage photos, sketches, markups, spec sheets; then asks you questions one at a time |
| `/interview` | Walks you through a decision with pop-up choices |
| `/equipment-record` | Adds a piece of equipment from its spec sheet |
| `/sandbox <topic>` | New branch to ideate without touching canonical designs |
| `/promote` | Moves a sandbox design to canonical through a pull request |
| `/capture <idea>` | Files an idea to a ClickUp capture list |
| `/consolidate` | Merges research notes into `kb/` |
| `/profile-forge` | Builds a new specialist profile |
| `/deep <problem>` | Sends one hard problem to Fable |
| `/lease-signed` | Moves from concept to design phase (you only) |
| `/gate <phase>` | Later phase gates (you only) |
