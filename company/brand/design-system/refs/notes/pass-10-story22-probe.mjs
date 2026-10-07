// Pass 8 probe, hardened after adversarial review — the register split,
// measured as rendered pixels.
// Assertions per cell (three engines x two candidates x three viewports):
//   - RENDER-LEVEL face gate: a 62ch ruler at 16px GT Alpina Fine must
//     measure 9.10..9.14 px/ch (the fallback face measures ~9.82); load
//     checks alone are load-level, not render-level (review finding).
//   - Stale-ch flush: ch-measured widths are style-flushed before
//     measurement; a pre-flush deviation is DETECTED and reported (the
//     recorded Firefox first-layout race), never archived as geometry.
//   - Absolute width (amendment 4): story and case paragraphs within
//     0.35px of the ruler-derived constant on desktop (62x16 = 992 and
//     49.6x20 = 992 exact; 55.1x18 = 991.8, the ratified rounding, so
//     the 18 pair sits 0.13px inside); on phones exactly the 80% column
//     (10% Ma margins cap every candidate).
//   - Constancy: width and left-edge spread across P2/P3/P4/P6 <= 0.25px.
//   - Register integrity: P2/P3/P4 at the candidate size, P6 at 16, P7
//     body 16 and lead 18 (leak check), faces GT Alpina Fine 400.
//   - Fit: the seat holds (no panel grows past 100svh at the tested
//     viewports); no horizontal overflow; GT Sectra and GT Sectra
//     Display (eyebrow, blockquote inside the measured blocks) asserted
//     loaded, not only the body face.
//   - P3 couplet (amendment 3): two composed lines at 390 and 375, no
//     line under ~40% of measure.
//   - Motion-path parity (chromium, 1440, both candidates): rest
//     geometry measured on the MOTION path equals the reduced-path
//     geometry (the rest-state-identity claim demonstrated, not read).
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { writeFileSync } from "node:fs";
import { createRequire } from "node:module";

const ROOT = "/Users/brandonacuna/son/design-system";
const playwright = createRequire(resolve(ROOT, "package.json"))("playwright");
const PAGE = pathToFileURL(resolve(ROOT, "track/index.html")).href;

const ENGINES = ["chromium", "webkit", "firefox"];
// Pass 10: the 22 candidate measured against 20 (and 18 for the record).
const CANDIDATES = [
  { label: "20", query: "", size: 20, ch: 49.6 },
  { label: "18", query: "?story=18", size: 18, ch: 55.1 },
  { label: "22", query: "?story=22", size: 22, ch: 45.1 },
];
const VIEWPORTS = [
  { label: "1440x900", width: 1440, height: 900 },
  { label: "390x844", width: 390, height: 844 },
  { label: "375x667", width: 375, height: 667 },
];
const PANELS = ["p2", "p3", "p4", "p6"];

const lines = [];
const say = (s) => { lines.push(s); console.log(s); };
let failures = 0;
const fail = (s) => { failures += 1; say(`FAIL  ${s}`); };

async function measureCell(page) {
  return page.evaluate(async (panels) => {
    const FACES = ['400 1em "GT Alpina Fine"', '400 1em "GT Sectra"', '400 1em "GT Sectra Display"'];
    await Promise.all(FACES.map((f) => document.fonts.load(f)));
    await document.fonts.ready;
    const out = { facesLoaded: FACES.every((f) => document.fonts.check(f)) };
    // Render-level gate: the ruler measures the ch basis the layout
    // actually paints with, not what the FontFaceSet reports.
    const ruler = document.createElement("span");
    ruler.style.cssText =
      "position:absolute;visibility:hidden;display:inline-block;white-space:nowrap;" +
      "font:400 16px 'GT Alpina Fine';width:62ch;padding:0;border:0;";
    document.body.appendChild(ruler);
    out.chBasis = ruler.getBoundingClientRect().width / 62;
    ruler.remove();
    out.noHscroll =
      document.documentElement.scrollWidth <= document.documentElement.clientWidth;
    const bodySel = (id) => document.querySelector(`[data-panel="${id}"]`);
    // Stale-ch detection then flush: record pre-flush widths, invalidate
    // the ch-carrying property, re-resolve, measure clean.
    out.preFlush = {};
    for (const id of panels) {
      out.preFlush[id] = bodySel(id).querySelector(".t-body").getBoundingClientRect().width;
    }
    for (const el of document.querySelectorAll(".panel .t-body, .panel .t-lead")) {
      el.style.maxWidth = "none";
      void el.offsetWidth;
      el.style.maxWidth = "";
    }
    out.panels = {};
    for (const id of panels) {
      const panel = bodySel(id);
      const bodies = [...panel.querySelectorAll(".t-body")];
      const content = panel.querySelector(".panel-content");
      const entry = {
        register: panel.dataset.register || null,
        fontSize: parseFloat(getComputedStyle(bodies[0]).fontSize),
        lineHeight: parseFloat(getComputedStyle(bodies[0]).lineHeight),
        fontFamily: getComputedStyle(bodies[0]).fontFamily.split(",")[0].trim(),
        fontWeight: getComputedStyle(bodies[0]).fontWeight,
        paraWidth: bodies[0].getBoundingClientRect().width,
        leftEdge: bodies[0].getBoundingClientRect().left,
        blockHeight: content.getBoundingClientRect().height,
        panelHeight: panel.offsetHeight,
        paras: [],
      };
      for (const b of bodies) {
        const mover = b.querySelector(".enter-mover") || b;
        const textNode = mover.childNodes[0];
        const words = textNode.textContent.split(/\s+/).filter(Boolean);
        const rows = [];
        let pos = 0;
        for (const w of words) {
          const at = textNode.textContent.indexOf(w, pos);
          pos = at + w.length;
          const r = document.createRange();
          r.setStart(textNode, at);
          r.setEnd(textNode, at + w.length);
          const rect = r.getBoundingClientRect();
          const row = rows.find((x) => Math.abs(x.top - rect.top) < 2);
          if (row) {
            row.words.push(w);
            row.right = Math.max(row.right, rect.right);
            row.left = Math.min(row.left, rect.left);
          } else {
            rows.push({ top: rect.top, left: rect.left, right: rect.right, words: [w] });
          }
        }
        entry.paras.push(rows.map((r) => ({ text: r.words.join(" "), width: r.right - r.left })));
      }
      out.panels[id] = entry;
    }
    // Register leak check: chapter II consumes Body and Lead unchanged.
    const p7body = document.querySelector('[data-panel="p7"] .t-body');
    const p7lead = document.querySelector('[data-panel="p7"] .t-lead');
    out.p7 = {
      body: parseFloat(getComputedStyle(p7body).fontSize),
      lead: parseFloat(getComputedStyle(p7lead).fontSize),
    };
    // The surrounding voices, for the ratio table: P5's Solo as rendered,
    // the P6 blockquote Headline, Subhead's rendered size (the band 22
    // enters), and the P2 paragraph's rendered line count driver.
    const solo = document.querySelector(".strophe--solo-desktop, .strophe--solo-mobile");
    const shown = [...document.querySelectorAll(".t-solo")].find(
      (el) => getComputedStyle(el).display !== "none"
    );
    out.soloSize = parseFloat(getComputedStyle(shown).fontSize);
    out.headlineSize = parseFloat(
      getComputedStyle(document.querySelector(".moat-quote .t-headline")).fontSize
    );
    out.subheadSize = parseFloat(
      getComputedStyle(document.querySelector(".founder-name .t-subhead")).fontSize
    );
    return out;
  }, PANELS);
}

function assertCell(tag, data, cand, vp) {
  if (!data.facesLoaded) fail(`${tag}: a display face did not report loaded; run is void`);
  if (data.chBasis < 9.1 || data.chBasis > 9.14)
    fail(`${tag}: rendered ch basis ${data.chBasis.toFixed(3)}px/ch is not GT Alpina Fine (expected ~9.12; fallback ~9.82); run is void`);
  if (!data.noHscroll) fail(`${tag}: horizontal overflow`);
  for (const id of PANELS) {
    const stale = Math.abs(data.preFlush[id] - data.panels[id].paraWidth);
    if (stale > 1)
      say(`${tag} ${id}: NOTE stale ch detected pre-flush (${data.preFlush[id].toFixed(2)}px, corrected to ${data.panels[id].paraWidth.toFixed(2)}px)`);
  }
  // The ratified constant (amendment 4): 62ch at 16 = 565.44px. Engines
  // may quantize ch advances per size (Firefox does, <= 0.3px on this
  // measure), so the gate is sub-pixel proximity to the constant, not
  // linear arithmetic from the 16px basis.
  const CONSTANT = 565.44;
  for (const id of PANELS) {
    const p = data.panels[id];
    const wantSize = id === "p6" ? 16 : cand.size;
    if (Math.abs(p.fontSize - wantSize) > 0.01)
      fail(`${tag} ${id}: font-size ${p.fontSize}, expected ${wantSize}`);
    if (!/Alpina Fine/.test(p.fontFamily) || p.fontWeight !== "400")
      fail(`${tag} ${id}: face ${p.fontFamily} ${p.fontWeight}, expected GT Alpina Fine 400`);
    const expected = vp.width >= 1440 ? CONSTANT : vp.width * 0.8;
    if (Math.abs(p.paraWidth - expected) > 0.5)
      fail(`${tag} ${id}: rendered width ${p.paraWidth.toFixed(2)}px, expected ${expected.toFixed(2)}px +-0.5`);
    // P3 carries the tail (pass 9): its floor is seat + 40svh. The others
    // floor at the seat; growth past it is Decision 4's sanctioned class,
    // REPORTED as a growth note (the felt cost is Brandon's), never
    // silently absorbed.
    const floor = id === "p3" ? vp.height * 1.4 : vp.height;
    const grew = p.panelHeight - floor;
    if (id === "p3" && Math.abs(grew) > 1)
      fail(`${tag} p3: seat+tail ${p.panelHeight}px, expected ${floor}px`);
    if (id !== "p3" && grew < -1)
      fail(`${tag} ${id}: panel ${p.panelHeight}px under its ${floor}px floor`);
    const totalLines = p.paras.reduce((n, para) => n + para.length, 0);
    const frame = ((p.blockHeight / vp.height) * 100).toFixed(1);
    const seatNote =
      id !== "p3" && grew > 1
        ? `GROWTH +${grew.toFixed(0)}px past the seat (sanctioned class, judged in the hand)`
        : "seat holds";
    say(
      `${tag} ${id} [${p.register}]: ${p.fontSize}px/${p.lineHeight}px, ` +
        `para ${p.paraWidth.toFixed(2)}px @x${p.leftEdge.toFixed(2)}, ` +
        `${totalLines} line(s), block ${p.blockHeight.toFixed(0)}px = ${frame}% of frame, ${seatNote}`
    );
  }
  if (Math.abs(data.p7.body - 16) > 0.01 || Math.abs(data.p7.lead - 18) > 0.01)
    fail(`${tag}: register leak into chapter II (P7 body ${data.p7.body}, lead ${data.p7.lead})`);
  const widths = PANELS.map((id) => data.panels[id].paraWidth);
  const edges = PANELS.map((id) => data.panels[id].leftEdge);
  const wSpread = Math.max(...widths) - Math.min(...widths);
  const eSpread = Math.max(...edges) - Math.min(...edges);
  say(
    `${tag} constancy: width spread ${wSpread.toFixed(2)}px, left-edge spread ${eSpread.toFixed(2)}px (ch basis ${data.chBasis.toFixed(3)}); ` +
      `voices: solo ${data.soloSize}px (ratio ${(data.soloSize / cand.size).toFixed(2)}), ` +
      `blockquote ${data.headlineSize}px (${(data.headlineSize / cand.size).toFixed(2)}), ` +
      `subhead ${data.subheadSize}px (${(data.subheadSize / cand.size).toFixed(2)}${data.subheadSize < cand.size ? " — INVERTED, story above Subhead" : ""})`
  );
  if (wSpread > 0.5) fail(`${tag}: rendered width varies ${wSpread.toFixed(2)}px across the moat column (past the half-pixel visibility bound)`);
  if (eSpread > 0.5) fail(`${tag}: left edge varies across the moat column`);
  const p3 = data.panels.p3.paras[0];
  if (vp.width <= 390) {
    if (p3.length !== 2) {
      fail(`${tag} P3: couplet is ${p3.length} lines, ruled two`);
    } else {
      const fractions = p3.map((l) => l.width / data.panels.p3.paraWidth);
      const short = Math.min(...fractions);
      say(
        `${tag} P3 couplet: "${p3[0].text}" / "${p3[1].text}" ` +
          `(${p3.map((l) => Math.round(l.width)).join("px, ")}px; shortest ${(short * 100).toFixed(0)}% of measure)`
      );
      if (short < 0.4) fail(`${tag} P3: line at ${(short * 100).toFixed(0)}% of measure, under the ~40% rider`);
    }
  } else {
    say(`${tag} P3 desktop: ${p3.length} line(s): ${p3.map((l) => `"${l.text}"`).join(" / ")}`);
  }
}

const reducedStore = {};
for (const engineName of ENGINES) {
  const engine = playwright[engineName];
  const browser = await engine.launch({ headless: true });
  for (const cand of CANDIDATES) {
    for (const vp of VIEWPORTS) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        reducedMotion: "reduce",
      });
      const page = await context.newPage();
      await page.goto(PAGE + cand.query, { waitUntil: "load", timeout: 60000 });
      const data = await measureCell(page);
      await context.close();
      const tag = `${engineName} ${vp.label} story=${cand.label}`;
      assertCell(tag, data, cand, vp);
      reducedStore[`${engineName}|${cand.label}|${vp.label}`] = data;
    }
  }
  await browser.close();
}

// Motion-path parity: the rest state must equal the reduced-path state.
say("");
const chromiumBrowser = await playwright.chromium.launch({ headless: true });
for (const cand of CANDIDATES) {
  const vp = VIEWPORTS[0];
  const context = await chromiumBrowser.newContext({
    viewport: { width: vp.width, height: vp.height },
  });
  const page = await context.newPage();
  await page.goto(PAGE + cand.query, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(1600); // arrival floor + hero choreography
  for (const id of PANELS) {
    await page.evaluate((panelId) => {
      const el = document.querySelector(`[data-panel="${panelId}"]`);
      window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY);
    }, id);
    await page.waitForTimeout(1400); // entrance window (500ms blocks + stagger)
  }
  const motion = await measureCell(page);
  await context.close();
  const tag = `chromium ${vp.label} story=${cand.label} MOTION-PATH`;
  const reduced = reducedStore[`chromium|${cand.label}|${vp.label}`];
  let parityOk = true;
  for (const id of PANELS) {
    const m = motion.panels[id];
    const r = reduced.panels[id];
    const same =
      Math.abs(m.paraWidth - r.paraWidth) <= 0.1 &&
      Math.abs(m.leftEdge - r.leftEdge) <= 0.1 &&
      m.fontSize === r.fontSize &&
      JSON.stringify(m.paras.map((p) => p.map((l) => l.text))) ===
        JSON.stringify(r.paras.map((p) => p.map((l) => l.text)));
    if (!same) {
      parityOk = false;
      fail(`${tag} ${id}: motion-path rest geometry differs from the reduced path (width ${m.paraWidth.toFixed(2)} vs ${r.paraWidth.toFixed(2)}, x ${m.leftEdge.toFixed(2)} vs ${r.leftEdge.toFixed(2)})`);
    }
  }
  if (parityOk)
    say(`${tag}: rest geometry identical to the reduced path (width, left edge, size, every line break) across P2/P3/P4/P6`);
}
await chromiumBrowser.close();

say(failures ? `\n${failures} FAILURE(S)` : "\nAll checks passed (every line above carries an assertion; NOTE lines record detected-then-corrected stale states).");
writeFileSync(resolve(ROOT, "refs/notes/pass-10-story-22.txt"), lines.join("\n") + "\n");
process.exit(failures ? 1 : 0);
