// Sŏn adherence — track stacking-invariant pass. Run: node adherence/check-track.mjs
// Enforces the load-bearing invariant the wipe mechanism depends on
// (ratified at gate A, 2026-07-21; see track/track.css and build-spec §2.2):
// body, html, main.track, and the dark panels must never gain a
// stacking-context-creating property. Any of these demotes a dark panel
// below the fixed still layer and locally scopes its content z-order, so
// content drowns under the glyph, silently, at 0.06 opacity. The daylight
// panels are exempt: they are already positioned stacking contexts above
// the layer by design. Z-bands: layer 1, content 2, chrome 3 and above.
// This is enforcement of an invariant the build depends on, the same class
// as the copy pass. It scans CSS wherever it can style the track (all
// tracked .css files plus track/ HTML style blocks and inline styles);
// selectors are guarded by their SUBJECT (the last compound), so
// positioning content INSIDE a panel stays legitimate.
// Static analysis only: a script mutating panel style at runtime is not
// caught here; the same invariant binds any track JS by review.
// Exit 1 on any violation — a violation blocks, it does not warn.

const isNode = typeof process !== "undefined" && process.versions && process.versions.node;

async function main() {
  const { readFileSync, readdirSync, statSync } = await import("node:fs");
  const { join, relative, resolve, dirname } = await import("node:path");

  const ROOT = resolve(dirname(process.argv[1]), "..");
  // The dark set is the settled panel map (build-spec §3): chapter I, the
  // ask, and the coda. Daylight is P7–P9.
  const DARK_PANELS = new Set(["p1", "p2", "p3", "p4", "p5", "p6", "p10", "p11"]);
  const SKIP = /^(uploads|node_modules|assets|adherence|guidelines-deck|refs|site)\/|(^|\/)(_ds_bundle\.js|_ds_manifest\.json)/;

  // property -> the only permitted value pattern (lowercased, trimmed).
  // Anything else on a guarded subject is a violation. var() indirection on
  // a guarded property is unverifiable statically and is treated as a
  // violation rather than trusted.
  const FORBIDDEN = {
    "transform": /^none$/,
    "translate": /^none$/,
    "rotate": /^none$/,
    "scale": /^none$/,
    "perspective": /^none$/,
    "offset-path": /^none$/,
    "filter": /^none$/,
    "backdrop-filter": /^none$/,
    "will-change": /^auto$/,
    "isolation": /^auto$/,
    "mix-blend-mode": /^normal$/,
    "clip-path": /^none$/,
    "mask": /^none$/,
    "mask-image": /^none$/,
    "contain": /^(none|size|inline-size)$/,
    "content-visibility": /^visible$/,
    "opacity": /^(1|1\.0+)$/,
    "position": /^static$/,
    "z-index": /^auto$/,
    "animation": /^none$/,
    "animation-name": /^none$/,
  };

  const problems = [];
  const flag = (file, line, detail) => problems.push(`${file}:${line}  [stacking-invariant]  ${detail}`);
  const lineOf = (text, idx) => text.slice(0, idx).split("\n").length;
  const blank = (s) => s.replace(/[^\n]/g, " ");

  // A selector is guarded when its subject (last compound) targets html,
  // body, main, .track, a [data-panel] in the dark set, or .panel without
  // the daylight modifier.
  function subjectIsGuarded(selector) {
    const subject = selector.trim().split(/\s*[>+~]\s*|\s+/).filter(Boolean).pop() || "";
    if (subject.includes("panel--daylight")) return false;
    // A pseudo-element is a child of the guarded box, not the box itself;
    // a stacking context on it cannot demote the panel.
    if (subject.includes("::")) return false;
    const dataPanel = subject.match(/\[data-panel="?([a-z0-9]+)"?\]/);
    if (dataPanel) return DARK_PANELS.has(dataPanel[1]);
    if (/(^|[^a-z0-9_-])\.panel(?![a-z0-9_-])/.test(subject)) return true;
    if (/\.track(?![a-z0-9_-])/.test(subject)) return true;
    const tag = subject.match(/^[a-z][a-z0-9]*/i);
    return !!tag && ["html", "body", "main"].includes(tag[0].toLowerCase());
  }

  function checkDeclarations(file, text, cssBody, bodyOffset, label) {
    for (const decl of cssBody.matchAll(/([a-z-]+)\s*:\s*([^;{}]+)/gi)) {
      const prop = decl[1].toLowerCase();
      const rule = FORBIDDEN[prop];
      if (!rule) continue;
      const value = decl[2].trim().toLowerCase().replace(/\s*!important$/, "");
      if (!rule.test(value)) {
        flag(file, lineOf(text, bodyOffset + decl.index), `${label}: "${prop}: ${decl[2].trim()}" creates a stacking context on a guarded element — the still layer would drown its content (track/track.css invariant)`);
      }
    }
  }

  // Blank at-rule preludes and braces while keeping inner rules in place,
  // so @media/@supports/@keyframes contents are scanned with every offset
  // and line number intact. Loops until no braced at-rule remains, which
  // also unwraps nested at-rules.
  function unwrapAtRules(css) {
    let out = css;
    const atRe = /@[a-z-][^{};]*\{((?:[^{}]|\{[^{}]*\})*)\}/i;
    for (let guard = 0; guard < 50; guard += 1) {
      const m = out.match(atRe);
      if (!m) break;
      const preludeLen = m[0].indexOf("{") + 1;
      out =
        out.slice(0, m.index) +
        blank(out.slice(m.index, m.index + preludeLen)) +
        m[1] +
        blank("}") +
        out.slice(m.index + m[0].length);
    }
    return out;
  }

  // Walk rules in a CSS chunk. At-rule wrappers are unwrapped first; their
  // inner rules are checked the same way.
  function checkCss(file, text, css, offset) {
    const stripped = unwrapAtRules(css.replace(/\/\*[\s\S]*?\*\//g, blank));
    for (const m of stripped.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
      const selectors = m[1].split(",");
      if (!selectors.some(subjectIsGuarded)) continue;
      const bodyStart = offset + m.index + m[1].length + 1;
      checkDeclarations(file, text, m[2], bodyStart, `selector "${m[1].trim().replace(/\s+/g, " ").slice(0, 60)}"`);
    }
  }

  const files = [];
  (function walk(dir) {
    for (const name of readdirSync(dir)) {
      const p = join(dir, name);
      const rel = relative(ROOT, p);
      if (SKIP.test(rel) || name.startsWith(".")) continue;
      if (statSync(p).isDirectory()) walk(p);
      else if (/\.(html|css)$/.test(name)) files.push(rel);
    }
  })(ROOT);

  for (const file of files) {
    const text = readFileSync(join(ROOT, file), "utf8");
    if (file.endsWith(".css")) {
      checkCss(file, text, text, 0);
    } else if (file.startsWith("track/")) {
      for (const m of text.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi)) {
        checkCss(file, text, m[1], m.index + m[0].indexOf(m[1]));
      }
      // Inline styles on guarded elements: body, main, html, dark panels.
      for (const m of text.matchAll(/<(html|body|main|section)\b([^>]*)>/gi)) {
        const attrs = m[2];
        const style = attrs.match(/style="([^"]*)"/i);
        if (!style) continue;
        const cls = attrs.match(/class="([^"]*)"/i)?.[1] ?? "";
        const dataPanel = attrs.match(/data-panel="([a-z0-9]+)"/i)?.[1];
        const tag = m[1].toLowerCase();
        const guarded =
          ["html", "body", "main"].includes(tag) ||
          (dataPanel ? DARK_PANELS.has(dataPanel) : /(^|\s)panel(\s|$)/.test(cls) && !cls.includes("panel--daylight"));
        if (!guarded) continue;
        checkDeclarations(file, text, style[1], m.index + m[0].indexOf(style[1]), `inline style on <${tag}>`);
      }
    }
  }

  if (problems.length) {
    console.error(`Sŏn track invariant: ${problems.length} violation(s)\n` + problems.join("\n"));
    process.exit(1);
  }
  console.log(`Sŏn track invariant: clean (${files.length} files checked)`);
}

if (isNode) main();
