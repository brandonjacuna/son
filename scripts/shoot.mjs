// Sŏn reference pipeline — capture a page as durable stills.
// Usage: npm run shoot -- <target> <name>
//   <target>  a URL (http/https) or a local file path to an HTML file
//   <name>    output folder name under refs/shots/
// A live page cannot be read directly next session. This is the step that
// turns a rendered page into evidence: a full-page capture plus a set of
// viewport-height captures down the page, at desktop and mobile widths.
//
// Writes:
//   refs/shots/<name>/desktop/full.png   whole page, one image
//   refs/shots/<name>/desktop/0001.png … one viewport height each, top to bottom
//   refs/shots/<name>/mobile/full.png
//   refs/shots/<name>/mobile/0001.png  …

import { existsSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const INSTALL_HINT = "npm install -D playwright && npx playwright install chromium";

// Two widths, one row of assumptions each. Height is the viewport slice height.
const DEVICES = [
  { label: "desktop", width: 1440, height: 900 },
  { label: "mobile", width: 390, height: 844 },
];

const SETTLE_MS = 1500; // let fonts load and any entrance motion finish
const MAX_SLICES = 60; // guard against a runaway-tall page

function fail(message) {
  console.error(`shoot: ${message}`);
  process.exit(1);
}

const [target, name] = process.argv.slice(2);

if (!target || !name) {
  fail("usage: npm run shoot -- <target> <name>");
}

// Resolve the target to something a browser can open. A URL is used as-is;
// anything else is treated as a local file path and must exist.
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

// Playwright is a dev dependency. If it is missing, say so plainly.
let chromium;
try {
  ({ chromium } = await import("playwright"));
} catch {
  fail(`playwright is not installed. Install it with:\n\n    ${INSTALL_HINT}\n`);
}

// Scroll the whole page once so lazy content loads and motion settles,
// then return to the top. Returns the full scrollable height.
async function primeAndMeasure(page, step) {
  return page.evaluate(async (viewportStep) => {
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    const height = () =>
      Math.max(
        document.body.scrollHeight,
        document.documentElement.scrollHeight,
        document.body.offsetHeight,
        document.documentElement.offsetHeight
      );
    for (let y = 0; y < height(); y += viewportStep) {
      window.scrollTo(0, y);
      await sleep(120);
    }
    window.scrollTo(0, 0);
    await sleep(200);
    return height();
  }, step);
}

async function captureDevice(browser, device) {
  const { label, width, height } = device;
  const outDir = resolve(ROOT, "refs", "shots", name, label);
  mkdirSync(outDir, { recursive: true });

  const context = await browser.newContext({
    viewport: { width, height },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();

  // Local React bundles can leave a request hanging, so do not wait on
  // networkidle. Wait for load, then settle on a fixed delay.
  await page.goto(url, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(SETTLE_MS);

  const fullHeight = await primeAndMeasure(page, height);
  await page.waitForTimeout(300);

  // One image of the whole page.
  await page.screenshot({
    path: resolve(outDir, "full.png"),
    fullPage: true,
  });

  // Then viewport-height slices, top to bottom, clipped against the full page.
  const slices = Math.min(Math.ceil(fullHeight / height), MAX_SLICES);
  for (let i = 0; i < slices; i += 1) {
    const y = i * height;
    const sliceHeight = Math.min(height, fullHeight - y);
    if (sliceHeight <= 0) break;
    const nnnn = String(i + 1).padStart(4, "0");
    await page.screenshot({
      path: resolve(outDir, `${nnnn}.png`),
      clip: { x: 0, y, width, height: sliceHeight },
      fullPage: true,
    });
  }

  await context.close();
  console.log(
    `shoot: ${label} — full page + ${slices} slice(s) at ${width}px → refs/shots/${name}/${label}/`
  );
  return { label, slices, fullHeight };
}

const browser = await chromium.launch({ headless: true });
try {
  for (const device of DEVICES) {
    await captureDevice(browser, device);
  }
} finally {
  await browser.close();
}

console.log(`shoot: wrote captures to refs/shots/${name}/`);
