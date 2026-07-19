The Sŏn wordmark lock-up — use anywhere the brand mark appears (headers, covers, footers, splash). Typographic, never a drawn logo.

```jsx
<Wordmark variant="lockup" size={72} />
<Wordmark variant="latin" size={28} />
<Wordmark variant="glyph" size={40} />
```

Variants: `lockup` (primary, vertical — "Sŏn" with 선 centered below) · `latin` (secondary, wordmark alone) · `glyph` (icon / minimum-scale, 선 alone). The 선 glyph color resolves from `--son-glyph` per theme (Plum Ink on light, Bone on dark). Never render 선 in Jade.
