// Sŏn reference pipeline — decompose a video into numbered stills.
// Usage: npm run frames -- <file> <name> [fps]
//   <file>  path to the source video (drop it in refs/clips/)
//   <name>  output folder name under refs/frames/
//   [fps]   frames per second to sample; defaults to 10
// Video cannot be read directly. This is the step that turns a clip
// into evidence a session can look at.

import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const DEFAULT_FPS = 10;
const INSTALL_HINT = "brew install ffmpeg";

function fail(message) {
  console.error(`frames: ${message}`);
  process.exit(1);
}

const [file, name, fpsArg] = process.argv.slice(2);

if (!file || !name) {
  fail("usage: npm run frames -- <file> <name> [fps]");
}

if (!existsSync(file)) {
  fail(`cannot find video "${file}"`);
}

const fps = fpsArg === undefined ? DEFAULT_FPS : Number(fpsArg);
if (!Number.isFinite(fps) || fps <= 0) {
  fail(`fps must be a positive number, got "${fpsArg}"`);
}

// Check for ffmpeg before doing anything else, so the failure is clear.
const probe = spawnSync("ffmpeg", ["-version"], { stdio: "ignore" });
if (probe.error || probe.status !== 0) {
  fail(`ffmpeg is not installed. Install it on macOS with:\n\n    ${INSTALL_HINT}\n`);
}

const outDir = resolve(ROOT, "refs", "frames", name);
mkdirSync(outDir, { recursive: true });

const pattern = resolve(outDir, "%04d.png");
const result = spawnSync(
  "ffmpeg",
  ["-hide_banner", "-loglevel", "error", "-i", file, "-vf", `fps=${fps}`, pattern],
  { stdio: "inherit" }
);

if (result.status !== 0) {
  fail(`ffmpeg exited with code ${result.status}`);
}

console.log(`frames: wrote stills to refs/frames/${name}/ at ${fps}fps`);
