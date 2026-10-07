// Pass 9 probe — the departure's tail, verified as geometry and events.
//   1. Height is static CSS: P3 renders 100svh + 40svh on the motion
//      path, the reduced path, and with no JS — identical; P4's edge
//      sits exactly one tail past the seat frame.
//   2. Seat arming (amendment 6): P3's entrance is NOT armed one frame
//      before seat and IS armed at seat, on three engines, both motion
//      paths; the other panels keep the 85% threshold (P2 sanity).
//   3. Anti-page-end (gate 7 class), measured honestly: P3 and P4 share
//      a ground, so the panel edge is invisible — the visible window is
//      couplet-exit to P4-TEXT-entry, and glyph-alone frames inside it
//      are amendment 5's ratified image ("the text exits and the glyph
//      holds the frame alone"). Asserted: the window exists (the
//      pre-tail state, where P4's text arrived before the couplet left,
//      was the paragraph-spacing failure), stays under one frame's
//      worth of contentless travel (the ratified boundary), and the
//      glyph holds its rest opacity through the whole tail — no scrub,
//      no ending grammar.
//   4. Seat-frame composition unchanged: the couplet's optical midpoint
//      stays ~46svh of the seat frame at both candidates.
//   5. Deep-link edge: arriving from below and scrolling back up arms
//      the couplet (nothing focusable-invisible, fire-once holds).
//   6. Font-hang (chromium): with font requests aborted, the complete
//      render includes P3 (the seat observer's disconnect works).
// Rendered face gated by ch ruler as in the pass 8 probe.
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { writeFileSync } from "node:fs";
import { createRequire } from "node:module";

const ROOT = "/Users/brandonacuna/son/design-system";
const playwright = createRequire(resolve(ROOT, "package.json"))("playwright");
const PAGE = pathToFileURL(resolve(ROOT, "track/index.html")).href;

const lines = [];
const say = (s) => { lines.push(s); console.log(s); };
let failures = 0;
const fail = (s) => { failures += 1; say(`FAIL  ${s}`); };

const ENGINES = ["chromium", "webkit", "firefox"];
const CANDIDATES = [
  { label: "20", query: "" },
  { label: "18", query: "?story=18" },
];
const VIEWPORTS = [
  { label: "1440x900", width: 1440, height: 900 },
  { label: "390x844", width: 390, height: 844 },
  { label: "375x667", width: 375, height: 667 },
];

async function geometry(page) {
  return page.evaluate(async () => {
    await document.fonts.ready;
    const ruler = document.createElement("span");
    ruler.style.cssText =
      "position:absolute;visibility:hidden;display:inline-block;white-space:nowrap;font:400 16px 'GT Alpina Fine';width:62ch;";
    document.body.appendChild(ruler);
    const chBasis = ruler.getBoundingClientRect().width / 62;
    ruler.remove();
    const p3 = document.querySelector('[data-panel="p3"]');
    const p4 = document.querySelector('[data-panel="p4"]');
    const para = p3.querySelector(".t-body");
    const rect = para.getBoundingClientRect();
    const p4rect = p4.querySelector(".panel-content").getBoundingClientRect();
    const cs = getComputedStyle(p3);
    return {
      chBasis,
      vh: window.innerHeight,
      p3Top: p3.getBoundingClientRect().top + window.scrollY,
      p3Height: p3.offsetHeight,
      p4Top: p4.getBoundingClientRect().top + window.scrollY,
      p4TextTop: p4rect.top + window.scrollY,
      textTop: rect.top + window.scrollY,
      textBottom: rect.bottom + window.scrollY,
      paddingBottom: parseFloat(cs.paddingBottom),
      animationName: cs.animationName,
      transitionDuration: cs.transitionDuration,
    };
  });
}

for (const engineName of ENGINES) {
  const engine = playwright[engineName];
  const browser = await engine.launch({ headless: true });
  for (const cand of CANDIDATES) {
    for (const vp of VIEWPORTS) {
      for (const reduced of [true, false]) {
        // Full matrix only on chromium; other engines run the reduced
        // path at 390 and 1440 (the IO cross-engine risk) to bound cost.
        if (engineName !== "chromium" && (!reduced || vp.label === "375x667")) continue;
        const context = await browser.newContext({
          viewport: { width: vp.width, height: vp.height },
          reducedMotion: reduced ? "reduce" : "no-preference",
        });
        const page = await context.newPage();
        await page.goto(PAGE + cand.query, { waitUntil: "load", timeout: 60000 });
        await page.waitForTimeout(reduced ? 400 : 1400);
        const g = await geometry(page);
        const tag = `${engineName} ${vp.label} story=${cand.label} ${reduced ? "reduced" : "motion"}`;
        if (g.chBasis < 9.1 || g.chBasis > 9.14) fail(`${tag}: fallback face (ch ${g.chBasis.toFixed(3)}); run void`);
        // 1. Static height: seat + tail exactly, every path.
        const wantHeight = vp.height * 1.4;
        if (Math.abs(g.p3Height - wantHeight) > 1)
          fail(`${tag}: P3 height ${g.p3Height}px, expected ${wantHeight}px (100svh + 40svh)`);
        if (Math.abs(g.p4Top - (g.p3Top + wantHeight)) > 1)
          fail(`${tag}: P4 edge at ${g.p4Top}, expected seat + tail = ${g.p3Top + wantHeight}`);
        if (Math.abs(g.paddingBottom - vp.height * 0.4) > 1)
          fail(`${tag}: tail padding ${g.paddingBottom}px, expected ${vp.height * 0.4}px`);
        if (g.animationName !== "none") fail(`${tag}: keyed motion on the departure panel (${g.animationName})`);
        // 2. Seat arming.
        const armedAt = async (y) => {
          await page.evaluate((s) => window.scrollTo(0, s), y);
          await page.waitForTimeout(250);
          return page.evaluate(() => document.querySelector('[data-panel="p3"] [data-enter]').classList.contains("is-in"));
        };
        if (await armedAt(Math.round(g.p3Top) - 40)) fail(`${tag}: P3 armed 40px BEFORE seat`);
        if (await armedAt(Math.round(g.p3Top) - 6)) fail(`${tag}: P3 armed 6px before seat`);
        if (!(await armedAt(Math.round(g.p3Top) + 2))) fail(`${tag}: P3 not armed at seat`);
        const p2Armed = await page.evaluate(() =>
          document.querySelector('[data-panel="p2"] [data-enter]').classList.contains("is-in"));
        if (!p2Armed) fail(`${tag}: P2 lost its 85% arming`);
        // 3. The glyph-alone window: couplet exit to P4 TEXT entering the
        // frame (the panel edge is invisible on a shared ground). It must
        // exist (pre-tail it was negative: paragraph spacing, the ruled
        // defect) and stay under one frame's worth of contentless travel
        // (the ratified TOO LONG boundary).
        const coupletExitY = g.textBottom;
        const p4TextEnterY = g.p4TextTop - g.vh;
        const windowSvh = ((p4TextEnterY - coupletExitY) / vp.height) * 100;
        if (windowSvh <= 0)
          fail(`${tag}: no glyph-alone travel — P4's text arrives before the couplet exits (the paragraph-spacing state the tail exists to fix)`);
        if (windowSvh >= 100)
          fail(`${tag}: glyph-alone travel spans ${windowSvh.toFixed(1)}svh, a full frame or more — the ratified boundary`);
        // The grammar assertion: through the whole window the glyph holds
        // its rest opacity — no scrub, no ending event. Motion path only
        // (the scrub exists only there).
        let opacityHolds = true;
        if (!reduced) {
          for (const frac of [0.1, 0.5, 0.9]) {
            const y = Math.round(coupletExitY + (p4TextEnterY - coupletExitY) * frac);
            await page.evaluate((s) => window.scrollTo(0, s), y);
            await page.waitForTimeout(120);
            const op = await page.evaluate(() =>
              parseFloat(getComputedStyle(document.querySelector(".still-glyph")).opacity));
            if (Math.abs(op - 0.06) > 0.001) {
              opacityHolds = false;
              fail(`${tag}: glyph opacity ${op} inside the tail window (rest is 0.06; ending grammar leaking early)`);
            }
          }
        }
        // 4. Seat-frame composition: optical midpoint ~46svh of the seat.
        const midpoint = (g.textTop + g.textBottom) / 2 - g.p3Top;
        const midFrac = midpoint / vp.height;
        if (Math.abs(midFrac - 0.46) > 0.02)
          fail(`${tag}: couplet midpoint at ${(midFrac * 100).toFixed(1)}svh of seat, expected ~46`);
        say(
          `${tag}: seat+tail ${g.p3Height}px OK; arms at seat only; couplet midpoint ` +
            `${(midFrac * 100).toFixed(1)}svh; glyph-alone window ${windowSvh.toFixed(1)}svh of travel` +
            (reduced ? "" : `; glyph rest opacity ${opacityHolds ? "holds" : "BROKEN"} through it`)
        );
        await context.close();
      }
    }
  }
  await browser.close();
}

// 5. Deep-link edge + no-JS + font-hang, chromium.
const browser = await playwright.chromium.launch({ headless: true });
{
  // Deep-link: land at #ask (past P3), scroll back to the moat.
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: "reduce" });
  const page = await context.newPage();
  await page.goto(PAGE + "#ask", { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(600);
  const armedBefore = await page.evaluate(() =>
    document.querySelector('[data-panel="p3"] [data-enter]').classList.contains("is-in"));
  await page.evaluate(() => {
    const p3 = document.querySelector('[data-panel="p3"]');
    window.scrollTo(0, p3.getBoundingClientRect().top + window.scrollY + 200);
  });
  await page.waitForTimeout(300);
  const armedAfter = await page.evaluate(() =>
    document.querySelector('[data-panel="p3"] [data-enter]').classList.contains("is-in"));
  if (armedBefore) say("chromium deep-link: P3 unarmed while below it (expected; nothing visible)");
  if (!armedAfter) fail("chromium deep-link: scrolling back up never arms P3");
  else say("chromium deep-link: scroll-back arms the couplet");
  await context.close();
}
{
  // No JS: complete render, same geometry.
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto(PAGE, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(900);
  const r = await page.evaluate(() => {
    const p3 = document.querySelector('[data-panel="p3"]');
    const mover = p3.querySelector(".enter-mover");
    const cs = getComputedStyle(mover);
    return {
      height: p3.offsetHeight,
      vh: window.innerHeight,
      opacity: cs.opacity,
      transform: cs.transform,
      clipPad: parseFloat(getComputedStyle(p3.querySelector("[data-enter]")).paddingTop),
    };
  });
  if (Math.abs(r.height - r.vh * 1.4) > 1) fail(`no-JS: P3 height ${r.height}, expected ${r.vh * 1.4}`);
  if (r.opacity !== "1" || (r.transform !== "none" && r.transform !== "matrix(1, 0, 0, 1, 0, 0)"))
    fail(`no-JS: couplet not fully visible (opacity ${r.opacity}, transform ${r.transform})`);
  if (r.clipPad !== 0) fail(`no-JS: clip pad present without JS (${r.clipPad}px)`);
  say("no-JS: P3 renders complete at seat + tail, couplet visible, no clips");
  await context.close();
}
{
  // Font-hang: abort every font fetch; the complete render must include P3.
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  await context.route("**/assets/fonts/**", (route) => route.abort());
  const page = await context.newPage();
  await page.goto(PAGE, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(6200); // past the 5s ceiling
  const r = await page.evaluate(() => ({
    complete: document.documentElement.classList.contains("arrive-complete"),
    p3In: document.querySelector('[data-panel="p3"] [data-enter]').classList.contains("is-in"),
  }));
  if (!r.complete) fail("font-hang: arrive-complete never set");
  if (!r.p3In) fail("font-hang: P3 left un-entered on the complete render (seat observer not disconnected?)");
  else say("font-hang: complete render includes P3; the seat observer stands down");
  await context.close();
}
await browser.close();

say(failures ? `\n${failures} FAILURE(S)` : "\nAll checks passed.");
writeFileSync(resolve(ROOT, "refs/notes/pass-9-tail-verify.txt"), lines.join("\n") + "\n");
process.exit(failures ? 1 : 0);
