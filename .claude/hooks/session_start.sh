#!/usr/bin/env bash
# SessionStart hook: tells Claude where it is running and what build-out phase it is in.
# Works standalone (PHASE.yaml at repo root) or in the unified son repo (company/workstreams/build-out/).
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
BUILD=""
for c in ${SON_BUILD_DIR:+"$ROOT/$SON_BUILD_DIR"} "$ROOT" "$ROOT/company/workstreams/build-out"; do
  if [ -f "$c/PHASE.yaml" ]; then BUILD="$c"; break; fi
done
BRANCH=$(git -C "$ROOT" branch --show-current 2>/dev/null)
if [ "$(uname)" = "Darwin" ]; then ENVNAME="local Mac (GUI CAD over MCP available if the app is open)"; else ENVNAME="cloud (headless only: no Blender/FreeCAD/SketchUp GUI)"; fi
if [ -n "$BUILD" ]; then
  PHASE=$(grep -E '^current_phase:' "$BUILD/PHASE.yaml" | awk '{print $2}')
  REL="${BUILD#$ROOT}"; REL="${REL#/}"
  echo "Session context: environment=$ENVNAME | build-out phase=$PHASE | build-out root=${REL:-.} | branch=${BRANCH:-unknown}"
else
  echo "Session context: environment=$ENVNAME | branch=${BRANCH:-unknown}"
fi
case "$BRANCH" in
  main) echo "On main: canonical designs only. Start build-out ideation with /sandbox." ;;
  sandbox/*) echo "Sandbox branch: free to experiment. Promote with /promote." ;;
esac
# Credentials are injected at session runtime, never in the setup script.
if [ -z "$CLICKUP_API_TOKEN" ] && [ "$(uname)" != "Darwin" ]; then
  echo "Note: no CLICKUP_API_TOKEN in this cloud session. Use the ClickUp connector for ClickUp work."
fi
exit 0
