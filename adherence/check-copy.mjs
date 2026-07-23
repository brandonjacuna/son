// Sŏn adherence — copy + markup pass. Run: node adherence/check-copy.mjs
// Applies the canon to the .css and .html surfaces the JSX pass can't see:
// specimen cards, the seven slides, the deck template, the ui-kit surfaces.
// Comments are not copy — they are stripped — EXCEPT @dsCard / @template /
// @startingPoint labels, which print in the UI and are held to the canon.
// Exit 1 on any violation — a violation blocks, it does not warn.
// (Node-only; guarded so the design-system bundler treats it as a no-op.)

const isNode = typeof process !== "undefined" && process.versions && process.versions.node;

async function main() {
  const { readFileSync, readdirSync, statSync } = await import("node:fs");
  const { join, relative, resolve, dirname } = await import("node:path");

  // Project root = the parent of this script's directory (adherence/).
  const ROOT = resolve(dirname(process.argv[1]), "..");
  // guidelines-deck/ is a rendered documentation artifact (it quotes both sides
  // of the voice rules); infra js + compiler outputs + uploads are not surfaces.
  // refs/ is reference material dropped in for review, not an authored surface.
  const SKIP = /^(uploads|node_modules|assets|adherence|guidelines-deck|refs)\/|(^|\/)(_ds_bundle\.js|_ds_manifest\.json|_adherence\.oxlintrc\.json|deck-stage\.js|image-slot\.js|ds-base\.js|\.thumbnail)$/;
  // Copy rules (em dash, lexicon) apply to authored brand surfaces:
  const COPY_SCOPE = /^(components|guidelines|slides|templates|ui_kits|site|track)\//;
  const HEX_EXEMPT = new Set(["tokens/colors.css", "guidelines/colors-special.html"]);
  // "experience" is forbidden lexicon (site canon); "guest" is banned in favor of "customer".
  const LEXICON = /\b(elevated|experiential|experiences?|innovative|disruptive|authentic|delicious|mouthwatering|vibrant|seasonal|chef-driven|hand-crafted|house-made|community-driven|curated|farm-to-table|artisanal|must-try|amazing|incredible|unforgettable|guests?)\b/gi;
  const FONT_OK = /^(var\(--son-font-[a-z-]+\)|"?(GT Sectra Book Fallback|GT Sectra Fine Arrival|GT Sectra Fine|GT Sectra Book|GT Sectra Display|GT Sectra|GT Alpina|Sandoll Myeongjo|Nanum Myeongjo|Apple Myungjo|Batang|Georgia)"?|inherit|serif)/;

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

  const problems = [];
  const flag = (file, line, rule, detail) => problems.push(`${file}:${line}  [${rule}]  ${detail}`);
  const lineOf = (text, idx) => text.slice(0, idx).split("\n").length;
  const blank = (s) => s.replace(/[^\n]/g, " "); // preserve offsets/line numbers

  for (const file of files) {
    const text = readFileSync(join(ROOT, file), "utf8");
    const isHtml = file.endsWith(".html");
    const inCopyScope = COPY_SCOPE.test(file);

    // Comment-stripped view for copy checks (offsets preserved).
    const copyText = isHtml
      ? text.replace(/<!--[\s\S]*?-->/g, blank).replace(/<style[\s\S]*?<\/style>/gi, blank).replace(/<script[\s\S]*?<\/script>/gi, blank)
      : text.replace(/\/\*[\s\S]*?\*\//g, blank);

    // 1. Em dashes in copy — hard canon: none in specimen or slide copy.
    if (inCopyScope) {
      for (const m of copyText.matchAll(/—/g))
        flag(file, lineOf(text, m.index), "em-dash", "em dash in copy — use a period, comma, colon, or interpunct");
      // 1b. Printed labels inside comments are copy too.
      for (const c of text.matchAll(/<!--\s*@(dsCard|template|startingPoint)[\s\S]*?-->/g))
        if (c[0].includes("—"))
          flag(file, lineOf(text, c.index), "em-dash", `em dash in @${c[1]} label`);
    }

    // 2. Removed tokens must not resurface (all scopes).
    for (const m of text.matchAll(/--son-color-(white|gold-foil)/g))
      flag(file, lineOf(text, m.index), "removed-token", `${m[0]} was removed from the palette`);

    // CSS contexts: whole file for .css; <style> blocks + style="" attrs for .html.
    const cssChunks = isHtml
      ? [...text.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi), ...text.matchAll(/style="([^"]*)"/gi)]
          .map((m) => ({ css: m[1].replace(/\/\*[\s\S]*?\*\//g, blank), at: m.index }))
      : [{ css: copyText, at: 0 }];

    for (const { css, at } of cssChunks) {
      // 3. Raw hex in CSS values (primitives + gold-foil stripe exempt).
      if (!HEX_EXEMPT.has(file))
        for (const m of css.matchAll(/#[0-9a-fA-F]{3,8}\b/g))
          flag(file, lineOf(text, at + m.index), "raw-hex", `${m[0]} — use var(--son-*)`);
      // 4. Font families outside the system.
      for (const m of css.matchAll(/font-family\s*:\s*([^;}]+)/gi))
        if (!FONT_OK.test(m[1].trim()))
          flag(file, lineOf(text, at + m.index), "font-family", `"${m[1].trim().slice(0, 60)}" is not a design-system font`);
    }

    // 5. Forbidden lexicon in visible HTML copy.
    if (isHtml && inCopyScope)
      for (const m of copyText.matchAll(LEXICON))
        flag(file, lineOf(text, m.index), "lexicon", `forbidden word "${m[0]}"`);
  }

  if (problems.length) {
    console.error(`Sŏn adherence: ${problems.length} violation(s)\n` + problems.join("\n"));
    process.exit(1);
  }
  console.log(`Sŏn adherence: clean (${files.length} files checked)`);
}

if (isNode) main();
