// Sŏn track pipeline — capture a scroll travel as numbered viewport frames.
// A still capture cannot demonstrate a wipe; this is the step that turns a
// scroll-keyed event into reviewable evidence.
// Usage: npm run scrollframes -- <target> <name> <spec> [count]
//   <target>  a URL (http/https) or a local file path to an HTML file
//   <name>    output folder name under refs/shots/
//   <spec>    seam=<selector>   frames across the viewport crossing of the
//             element's top edge, from edge-at-viewport-bottom to
//             edge-at-viewport-top
//             seat=<selector>   frames from the element seated (top edge at
//             viewport top) to the end of the document travel
//             range=<fromY>:<toY>  explicit document scrollY range
//             (device-blind: applies verbatim to both widths)
//   [count]   frames per device, default 12
// Writes refs/shots/<name>/desktop/0001-y<scrollY>.png … and the same under
// mobile/, top of the travel to the bottom, scroll position in the filename.

import { existsSync, mkdirSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const INSTALL_HINT = "npm install -D playwright && npx playwright install chromium";

const DEVICES = [
  { label: "desktop", width: 1440, height: 900 },
  { label: "mobile", width: 390, height: 844 },
];

const SETTLE_MS = 900; // fonts and layout; the travel itself is scroll-keyed
const STEP_SETTLE_MS = 140;

function fail(message) {
  console.error(`scrollframes: ${message}`);
  process.exit(1);
}

const [target, name, spec, countArg] = process.argv.slice(2);

if (!target || !name || !spec) {
  fail("usage: npm run scrollframes -- <target> <name> <seam=SEL|range=FROM:TO> [count]");
}

const count = countArg === undefined ? 12 : Number(countArg);
if (!Number.isInteger(count) || count < 2) {
  fail(`count must be an integer of at least 2, got "${countArg}"`);
}

let url;
if (/^https?:\/\//i.test(target)) {
  url = target;
} else {
  const filePath = resolve(target);
  if (!existsSync(filePath)) {
    fail(`cannot find local file "${target}"`);
  }
  url = pathToFileURL(filePath).href;
}

const seamMatch = spec.match(/^seam=(.+)$/);
const seatMatch = spec.match(/^seat=(.+)$/);
const rangeMatch = spec.match(/^range=(\d+):(\d+)$/);
if (!seamMatch && !seatMatch && !rangeMatch) {
  fail(`spec must be seam=<selector>, seat=<selector>, or range=<fromY>:<toY>, got "${spec}"`);
}

let chromium;
try {
  ({ chromium } = await import("playwright"));
} catch {
  fail(`playwright is not installed. Install it with:\n\n    ${INSTALL_HINT}\n`);
}

async function captureDevice(browser, device) {
  const { label, width, height } = device;
  const outDir = resolve(ROOT, "refs", "shots", name, label);

  const context = await browser.newContext({
    viewport: { width, height },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  await page.goto(url, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(SETTLE_MS);

  const elementTop = async (sel) => {
    const top = await page.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      return el.getBoundingClientRect().top + window.scrollY;
    }, sel);
    if (top === null) {
      fail(`no element matches selector "${sel}"`);
    }
    return top;
  };
  const maxScroll = () =>
    page.evaluate(() => document.documentElement.scrollHeight - window.innerHeight);

  let from;
  let to;
  if (seamMatch) {
    const seamTop = await elementTop(seamMatch[1]);
    if (seamTop < height) {
      console.warn(
        `scrollframes: ${label} — seam sits ${Math.round(seamTop)}px from the top, ` +
          `less than one viewport (${height}px); the sequence covers a partial crossing`
      );
    }
    from = Math.max(0, Math.round(seamTop - height));
    to = Math.round(seamTop);
  } else if (seatMatch) {
    from = Math.round(await elementTop(seatMatch[1]));
    to = Math.round(await maxScroll());
    if (from >= to) {
      fail(`seat "${seatMatch[1]}" sits at or past the end of the travel (y ${from}, end ${to})`);
    }
  } else {
    from = Number(rangeMatch[1]);
    to = Number(rangeMatch[2]);
  }

  // Fresh evidence only: a re-run must never union stale frames from an
  // earlier geometry or count into the reviewed sequence.
  rmSync(outDir, { recursive: true, force: true });
  mkdirSync(outDir, { recursive: true });

  // Frames are named by the ACTUAL scroll position after the browser has
  // clamped the request, so out-of-range requests cannot masquerade as
  // distinct positions. Drift and duplicates are reported, not hidden.
  let prevActual = null;
  for (let i = 0; i < count; i += 1) {
    const y = Math.round(from + ((to - from) * i) / (count - 1));
    await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
    await page.waitForTimeout(STEP_SETTLE_MS);
    const actual = Math.round(await page.evaluate(() => window.scrollY));
    if (actual !== y) {
      console.warn(`scrollframes: ${label} — requested y ${y}, page settled at ${actual}`);
    }
    if (prevActual !== null && actual === prevActual) {
      console.warn(`scrollframes: ${label} — frame ${i + 1} duplicates the previous position (y ${actual})`);
    }
    prevActual = actual;
    const nnnn = String(i + 1).padStart(4, "0");
    await page.screenshot({ path: resolve(outDir, `${nnnn}-y${actual}.png`) });
  }

  await context.close();
  console.log(
    `scrollframes: ${label} — ${count} frame(s), y ${from} to ${to} at ${width}px → refs/shots/${name}/${label}/`
  );
}

const browser = await chromium.launch({ headless: true });
try {
  for (const device of DEVICES) {
    await captureDevice(browser, device);
  }
} finally {
  await browser.close();
}

console.log(`scrollframes: wrote frames to refs/shots/${name}/`);
