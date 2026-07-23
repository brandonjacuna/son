// eslint.config.mjs — the JSX canon, enforced.
// Migrated 2026-07-23 (handoff) from _adherence.oxlintrc.json: stock oxlint
// cannot parse that file's x-omelette key or run no-restricted-syntax, so the
// JSX rules never actually blocked. This config is the AUTHORITATIVE rule
// source from here on; the oxlint JSON is a compiler artifact kept only for
// external-regeneration compatibility and is not consumed by any check.
//
// Two departures from the artifact, both corrections, not weakenings:
// 1. Prop-contract allowlists include the DOM/event passthrough the
//    components actually implement (every component spreads ...rest; Button
//    declares type/disabled). The generated .d.ts files under-declare the
//    real contract — recorded in docs/handoff.md for the next regeneration.
// 2. The raw-px rule runs as a ratchet: the debt register below names the
//    files that carried raw-px sites when the rule first actually ran
//    (~91 sites). Those files keep every other rule; any new file gets the
//    full set. Known rule limitation, inherited: only string literals
//    containing "px" match — numeric style values (fontSize: 14) pass.
//
// ui_kits/good-energy/ios-frame.jsx is exempt entirely: it renders the
// device bezel around the morning app (hardware chrome, not a brand
// surface) — the same idiom as check-copy's sanctioned infra exceptions.
// Wired into npm run lint as lint:jsx; a violation exits non-zero.

const RESTRICTED_IMPORTS = [
      "error",
      {
            "patterns": [
                  {
                        "group": [
                              "adherence/**",
                              "components/brand/**",
                              "components/core/**",
                              "components/forms/**",
                              "components/immersive/**",
                              "components/navigation/**",
                              "guidelines-deck/**",
                              "slides/**",
                              "ui_kits/good-energy/**",
                              "ui_kits/son-website/**"
                        ],
                        "message": "Import design-system components from 'index.js', not component internals."
                  }
            ]
      }
];

const RESTRICTED_SYNTAX = [
      "error",
      {
            "selector": "Literal[value=/#[0-9a-fA-F]{3,8}\\b/]",
            "message": "Raw hex color — use a design-system color token via var()."
      },
      {
            "selector": "Literal[value=/\\b\\d+px\\b/]",
            "message": "Raw px value — use a design-system spacing token via var()."
      },
      {
            "selector": "Literal[value=/font-family\\s*:\\s*(?!['\\\"]?(?:Sandoll Myeongjo|GT Sectra Book|GT Sectra Book Fallback|GT Sectra|GT Sectra Display|GT Alpina|Nanum Myeongjo))/i]",
            "message": "Font not provided by the design system. Available: Sandoll Myeongjo, GT Sectra Book, GT Sectra Book Fallback, GT Sectra, GT Sectra Display, GT Alpina, Nanum Myeongjo."
      },
      {
            "selector": "JSXOpeningElement[name.name='AmbientField'] > JSXAttribute > JSXIdentifier[name!=/^(?:theme|glyph|speed|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<AmbientField> doesn't accept that prop. Declared props: theme, glyph, speed, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='AmbientField'] > JSXAttribute[name.name='theme'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<AmbientField> theme must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Badge'] > JSXAttribute > JSXIdentifier[name!=/^(?:variant|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Badge> doesn't accept that prop. Declared props: variant, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='Badge'] > JSXAttribute[name.name='variant'] > Literal[value!=/^(?:outline|accent|solid)$/]",
            "message": "<Badge> variant must be one of 'outline' | 'accent' | 'solid'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Button'] > JSXAttribute > JSXIdentifier[name!=/^(?:variant|size|fullWidth|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Button> doesn't accept that prop. Declared props: variant, size, fullWidth, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='Button'] > JSXAttribute[name.name='variant'] > Literal[value!=/^(?:primary|secondary|ghost)$/]",
            "message": "<Button> variant must be one of 'primary' | 'secondary' | 'ghost'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Button'] > JSXAttribute[name.name='size'] > Literal[value!=/^(?:sm|md|lg)$/]",
            "message": "<Button> size must be one of 'sm' | 'md' | 'lg'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Card'] > JSXAttribute > JSXIdentifier[name!=/^(?:as|surface|padding|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Card> doesn't accept that prop. Declared props: as, surface, padding, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='Card'] > JSXAttribute[name.name='surface'] > Literal[value!=/^(?:primary|secondary)$/]",
            "message": "<Card> surface must be one of 'primary' | 'secondary'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Card'] > JSXAttribute[name.name='padding'] > Literal[value!=/^(?:none|sm|md|lg)$/]",
            "message": "<Card> padding must be one of 'none' | 'sm' | 'md' | 'lg'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Chapter'] > JSXAttribute > JSXIdentifier[name!=/^(?:theme|timeLabel|scrub|length|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Chapter> doesn't accept that prop. Declared props: theme, timeLabel, scrub, length, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='Chapter'] > JSXAttribute[name.name='theme'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<Chapter> theme must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Checkbox'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|error|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Checkbox> doesn't accept that prop. Declared props: label, error."
      },
      {
            "selector": "JSXOpeningElement[name.name='DaypartTakeover'] > JSXAttribute > JSXIdentifier[name!=/^(?:from|to|fromTime|toTime|auto|progress|label|onComplete|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<DaypartTakeover> doesn't accept that prop. Declared props: from, to, fromTime, toTime, auto, progress, label, onComplete."
      },
      {
            "selector": "JSXOpeningElement[name.name='DaypartTakeover'] > JSXAttribute[name.name='from'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<DaypartTakeover> from must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='DaypartTakeover'] > JSXAttribute[name.name='to'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<DaypartTakeover> to must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Divider'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|spacing|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Divider> doesn't accept that prop. Declared props: label, spacing."
      },
      {
            "selector": "JSXOpeningElement[name.name='Divider'] > JSXAttribute[name.name='spacing'] > Literal[value!=/^(?:sm|md|lg)$/]",
            "message": "<Divider> spacing must be one of 'sm' | 'md' | 'lg'."
      },
      {
            "selector": "JSXOpeningElement[name.name='FullBleedSection'] > JSXAttribute > JSXIdentifier[name!=/^(?:theme|ground|as|minHeight|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<FullBleedSection> doesn't accept that prop. Declared props: theme, ground, as, minHeight, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='FullBleedSection'] > JSXAttribute[name.name='theme'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<FullBleedSection> theme must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='FullBleedSection'] > JSXAttribute[name.name='ground'] > Literal[value!=/^(?:primary|secondary|inverse)$/]",
            "message": "<FullBleedSection> ground must be one of 'primary' | 'secondary' | 'inverse'."
      },
      {
            "selector": "JSXOpeningElement[name.name='ImageSlot'] > JSXAttribute > JSXIdentifier[name!=/^(?:ratio|src|alt|caption|emptyCaption|theme|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<ImageSlot> doesn't accept that prop. Declared props: ratio, src, alt, caption, emptyCaption, theme."
      },
      {
            "selector": "JSXOpeningElement[name.name='ImageSlot'] > JSXAttribute[name.name='ratio'] > Literal[value!=/^(?:full-bleed|portrait|landscape)$/]",
            "message": "<ImageSlot> ratio must be one of 'full-bleed' | 'portrait' | 'landscape'."
      },
      {
            "selector": "JSXOpeningElement[name.name='ImageSlot'] > JSXAttribute[name.name='theme'] > Literal[value!=/^(?:morning|dosi|dinner|luxe)$/]",
            "message": "<ImageSlot> theme must be one of 'morning' | 'dosi' | 'dinner' | 'luxe'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Input'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|error|hint|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Input> doesn't accept that prop. Declared props: label, error, hint."
      },
      {
            "selector": "JSXOpeningElement[name.name='KineticDisplay'] > JSXAttribute > JSXIdentifier[name!=/^(?:as|size|progress|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<KineticDisplay> doesn't accept that prop. Declared props: as, size, progress, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='KineticDisplay'] > JSXAttribute[name.name='size'] > Literal[value!=/^(?:display|headline)$/]",
            "message": "<KineticDisplay> size must be one of 'display' | 'headline'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Marquee'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|separator|duration|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Marquee> doesn't accept that prop. Declared props: label, separator, duration."
      },
      {
            "selector": "JSXOpeningElement[name.name='SectionHeader'] > JSXAttribute > JSXIdentifier[name!=/^(?:eyebrow|kicker|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<SectionHeader> doesn't accept that prop. Declared props: eyebrow, kicker, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='SeededCTA'] > JSXAttribute > JSXIdentifier[name!=/^(?:href|children|note|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<SeededCTA> doesn't accept that prop. Declared props: href, children, note."
      },
      {
            "selector": "JSXOpeningElement[name.name='Select'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|error|hint|children|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Select> doesn't accept that prop. Declared props: label, error, hint, children."
      },
      {
            "selector": "JSXOpeningElement[name.name='Switch'] > JSXAttribute > JSXIdentifier[name!=/^(?:label|error|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Switch> doesn't accept that prop. Declared props: label, error."
      },
      {
            "selector": "JSXOpeningElement[name.name='TabItem'] > JSXAttribute > JSXIdentifier[name!=/^(?:id|label|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<TabItem> doesn't accept that prop. Declared props: id, label."
      },
      {
            "selector": "JSXOpeningElement[name.name='Wordmark'] > JSXAttribute > JSXIdentifier[name!=/^(?:variant|size|color|glyphColor|align|className|style|key|ref|className|style|children|on[A-Z][A-Za-z]+|type|disabled|checked|defaultChecked|value|defaultValue|placeholder|name|id|required|readOnly|autoFocus|role|tabIndex|title|aria-[a-z]+|data-[a-z-]+)$/]",
            "message": "<Wordmark> doesn't accept that prop. Declared props: variant, size, color, glyphColor, align, className, style."
      },
      {
            "selector": "JSXOpeningElement[name.name='Wordmark'] > JSXAttribute[name.name='variant'] > Literal[value!=/^(?:lockup|latin|glyph)$/]",
            "message": "<Wordmark> variant must be one of 'lockup' | 'latin' | 'glyph'."
      },
      {
            "selector": "JSXOpeningElement[name.name='Wordmark'] > JSXAttribute[name.name='align'] > Literal[value!=/^(?:left|center|right)$/]",
            "message": "<Wordmark> align must be one of 'left' | 'center' | 'right'."
      }
];

const RESTRICTED_SYNTAX_NO_PX = RESTRICTED_SYNTAX.filter(
  (r) => typeof r === "string" || !r.message.startsWith("Raw px value")
);

const PX_DEBT_REGISTER = [
      "components/core/Badge.jsx",
      "components/core/Button.jsx",
      "components/core/Card.jsx",
      "components/core/Divider.jsx",
      "components/forms/Checkbox.jsx",
      "components/forms/Input.jsx",
      "components/forms/Select.jsx",
      "components/forms/Switch.jsx",
      "components/immersive/DaypartTakeover.jsx",
      "components/immersive/SeededCTA.jsx",
      "components/navigation/Tabs.jsx",
      "ui_kits/good-energy/app.jsx",
      "ui_kits/son-website/app.jsx"
];

const LANGUAGE = {
  ecmaVersion: "latest",
  sourceType: "module",
  parserOptions: { ecmaFeatures: { jsx: true } },
};

export default [
  {
    files: ["components/**/*.{js,jsx}", "ui_kits/**/*.{js,jsx}"],
    ignores: [...PX_DEBT_REGISTER, "ui_kits/good-energy/ios-frame.jsx"],
    languageOptions: LANGUAGE,
    rules: {
      "no-restricted-imports": RESTRICTED_IMPORTS,
      "no-restricted-syntax": RESTRICTED_SYNTAX,
    },
  },
  {
    files: PX_DEBT_REGISTER,
    languageOptions: LANGUAGE,
    rules: {
      "no-restricted-imports": RESTRICTED_IMPORTS,
      "no-restricted-syntax": RESTRICTED_SYNTAX_NO_PX,
    },
  },
  // Barrels legitimately import component internals.
  { files: ["**/index.js"], rules: { "no-restricted-imports": "off" } },
];
