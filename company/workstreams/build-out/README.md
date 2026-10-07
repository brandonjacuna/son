# Build-out

Sŏn's construction-mode workspace for Claude Code. Owner: Brandon John Acuña-Cardona. Design intent, research, and build-out planning for the restaurant. Read `CLAUDE.md` for the rules Claude follows and `decisions/0001-architecture.md` for why it is built this way.

Setup lives in the root CLAUDE.md. Cloud sessions use the ClickUp and Box connectors (claude.ai Settings > Connectors). Local sessions (Claude Desktop, Code tab, open the son repo) are where Blender and FreeCAD get driven. Paste `KICKOFF.md` into the first session.

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
