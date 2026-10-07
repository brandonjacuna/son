// Sŏn track pipeline — capture a timed sequence as numbered viewport frames.
// Scroll frames show scrub-keyed travel; this shows TIMED choreography: the
// page is loaded (and optionally jumped to a position), then the viewport is
// captured on an interval from load, so entrance sequences become evidence.
// Usage: npm run timeframes -- <target> <name> [position] [count] [intervalMs]
//   <target>    a URL (http/https) or a local file path to an HTML file
//   <name>      output folder name under refs/shots/
//   [position]  scrollY in px, or seat=<selector> (element top at viewport
//               top, per device); default 0
//   [count]     frames per device, default 14
//   [intervalMs] target capture interval, default 150 (actual elapsed time
//               is recorded in each filename; headless capture cost makes
//               exact cadence impossible, so filenames are the truth)
// Writes refs/shots/<name>/{desktop,mobile}/NNNN-t<elapsedMs>.png

import { existsSync, mkdirSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const INSTALL_HINT = "npm install -D playwright && npx playwright install chromium";

const DEVICES = [
  { label: "desktop", width: 1440, height: 900 },
  { label: "mobile", width: 390, height: 844 },
];

function fail(message) {
  console.error(`timeframes: ${message}`);
  process.exit(1);
}

const [target, name, positionArg, countArg, intervalArg] = process.argv.slice(2);

if (!target || !name) {
  fail("usage: npm run timeframes -- <target> <name> [scrollY|seat=SEL] [count] [intervalMs]");
}

const count = countArg === undefined ? 14 : Number(countArg);
if (!Number.isInteger(count) || count < 2) {
  fail(`count must be an integer of at least 2, got "${countArg}"`);
}
const interval = intervalArg === undefined ? 150 : Number(intervalArg);
if (!Number.isFinite(interval) || interval <= 0) {
  fail(`intervalMs must be positive, got "${intervalArg}"`);
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

const seatMatch = positionArg ? positionArg.match(/^seat=(.+)$/) : null;
const fixedY = seatMatch ? null : Number(positionArg ?? 0);
if (fixedY !== null && !Number.isFinite(fixedY)) {
  fail(`position must be a number or seat=<selector>, got "${positionArg}"`);
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
  rmSync(outDir, { recursive: true, force: true });
  mkdirSync(outDir, { recursive: true });

  const context = await browser.newContext({
    viewport: { width, height },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  await page.goto(url, { waitUntil: "load", timeout: 60000 });

  if (seatMatch) {
    const top = await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      return el.getBoundingClientRect().top + window.scrollY;
    }, seatMatch[1]);
    if (top === null) {
      fail(`no element matches selector "${seatMatch[1]}"`);
    }
    await page.evaluate((y) => window.scrollTo(0, y), Math.round(top));
  } else if (fixedY > 0) {
    await page.evaluate((y) => window.scrollTo(0, y), fixedY);
  }

  const t0 = Date.now();
  for (let i = 0; i < count; i += 1) {
    const targetT = i * interval;
    const lag = targetT - (Date.now() - t0);
    if (lag > 0) await page.waitForTimeout(lag);
    const elapsed = Date.now() - t0;
    const nnnn = String(i + 1).padStart(4, "0");
    await page.screenshot({ path: resolve(outDir, `${nnnn}-t${elapsed}.png`) });
  }

  await context.close();
  console.log(
    `timeframes: ${label} — ${count} frame(s) at ~${interval}ms from load at ${width}px → refs/shots/${name}/${label}/`
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

console.log(`timeframes: wrote frames to refs/shots/${name}/`);
