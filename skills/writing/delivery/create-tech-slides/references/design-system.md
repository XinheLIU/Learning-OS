# Design System — create-tech-slides

Last updated: 2026-07-18

The look: Palantir product-deck engineering aesthetic. Dark, precise, wireframe, dense.

## Tokens (CSS custom properties, already in template.html)

```css
:root{
  --bg:#0b0d10;          /* canvas — near-black, slightly blue */
  --bg2:#101318;         /* raised panel */
  --line:#2a2f36;        /* hairline borders */
  --line2:#3d444d;       /* stronger line / diagram strokes */
  --ink:#e8eaec;         /* primary text */
  --ink2:#9aa3ad;        /* secondary text */
  --ink3:#5c6570;        /* tertiary / micro-labels */
  --acc:#aecbdd;         /* pale steel-blue — primary accent (Palantir arrows) */
  --teal:#4fd1c5;        /* section accent (Mesosphere teal) */
  --violet:#a78bfa;      /* section accent */
  --sand:#e3c99a;        /* section accent / warnings */
  --red:#e07a6b;         /* negatives, 存疑, risks */
  --mono:ui-monospace,'SF Mono',Menlo,Consolas,monospace;
  --sans:-apple-system,'Helvetica Neue','PingFang SC','Noto Sans SC',sans-serif;
}
```

Color rules: the deck is 95% grayscale. Accents mean something — one accent per
section (Why=sand, What=teal, How=acc/steel, 争议=red, or similar mapping), reuse it in the
eyebrow chip, title keyword, diagram highlights of that section. Never decorate randomly.

## Type scale (at 1920×1080 design size)

| Role | Size / weight | Notes |
|---|---|---|
| Slide title | 38–52px / 600 | one line; keyword may take the accent color |
| Section cover number | 130–160px / 200 | ghost outline ok |
| Lead sentence | 21–23px / 400 | max 2 lines, --ink2 |
| Body text | 17–18px / 400 | line-height 1.55 |
| Table cells | 15px | header row 12px uppercase tracked |
| Diagram node label | 13–14px | mono for identifiers |
| Micro-label / eyebrow | 11–12px / 500 | UPPERCASE, letter-spacing .14–.2em, --ink3 |
| Callout / verdict strip | 16–17px / 500 | left border 2px accent |

Never exceed 52px for content-slide titles. Big type is reserved for the cover and
section covers. If a slide feels empty, add the missing detail from the source, don't
inflate the font.

## Slide anatomy (chrome is auto-injected by template.html)

```
┌──────────────────────────────────────────────────────────┐
│ ◱ EYEBROW · SECTION        (top-left, 11px tracked)       │
│                       deck meta · © date (top-right, 10px)│
│  Title 38px — keyword accented                            │
│  lead sentence 20px --ink2                                │
│                                                          │
│  [content grid: 12-col, 24px gutter]                      │
│                                                          │
│ footer-left source note        page 07 / 21 (bottom-right)│
└──────────────────────────────────────────────────────────┘
```

Padding: 72px sides, 56px top, 48px bottom. Content area ≈ 1776×860.

### Vertical fill (the `.slide` is a flex column)

The `.slide` box is `display:flex; flex-direction:column`. `.s-body` gets `flex:1; min-height:0`
so it fills all remaining canvas space below the header. Three utilities control vertical
distribution:

- **`.s-body.vcenter`** — center the content block vertically (good for short-form slides
  with one big figure).
- **`.s-body.vspread`** — distribute children evenly top-to-bottom.
- **`.grow`** on a child — that child expands to fill remaining space.
- **`.push-b`** on a child — push that child to the bottom (like a verdict callout).

### Sizing figures — ALWAYS use `.figbox` (hard rule)

A bare `svg.fig` is `width:100%` and derives its **height from the viewBox aspect ratio ×
column width**. In a 1776px-wide content area, a half-column is ~870px wide, so a
`viewBox="0 0 520 520"` SVG renders **870px tall** and blows through the bottom of the
canvas. This is the #1 cause of overflow. Never let an SVG's intrinsic ratio set slide
height. Wrap every figure that sits inside a grid column:

```html
<div class="figbox">
  <svg class="fig" viewBox="0 0 520 460">…</svg>
</div>
```

`.figbox` is `position:relative; flex:1; min-height:0`; the SVG inside is absolutely
positioned to fill it and letterboxes via `preserveAspectRatio`. The figure gets exactly
the height the layout gives the column — it can never push the slide taller. Make the
figbox's sibling column a flex column (`display:flex;flex-direction:column`) so both
columns share the body height. `svg.fig.fill` still exists for the rare full-width,
only-child figure, but inside `cols-2`/`cols-3` use `.figbox`, no exceptions.

Underfill is enforced by the `?check=1` audit: on non-cover slides, real content (table,
SVG ink, leaf text — excluding chrome and footer) must reach at least y=880 of the 1080
canvas. The audit measures SVG `getBBox()` ink, not the element box, so letterboxed SVGs
don't false-pass.

## Layout recipes

1. **split-figure** `.cols-2` (7/5 or 6/6): text+tables left, diagram right. The default
   for architecture topics. Mirror (figure left) every few slides for rhythm.
2. **full-diagram**: title strip + one big SVG (≈1776×760) + bracket labels on the right
   rail (the Palantir Foundry poster look). For the signature exploded stack.
3. **table-slide**: full-width comparison table, 3–7 columns; verdict callout strip
   underneath. For OWL/KG/Ontology-type comparisons.
4. **matrix**: 2×2 or 2×3 card grid, each card = icon-less header + 2–3 lines body.
   For "four challenges / five elements / six components".
5. **timeline/steps**: horizontal numbered stations with connector line, detail text
   under each. For evolutions and step-by-step flows.
6. **section-cover**: ghost number + act title + 1-line thesis + mini agenda. The only
   low-density slide type allowed besides the main cover.

## Density budget

- Content slides: 120–250 words each, or a diagram carrying ≥8 labeled nodes plus
  60–150 words of text. Under 80 words and no diagram → merge it into a neighbor.
- Tables: keep every row of the source table. If a table has >8 rows, split across two
  slides ("(1/2)" in title) rather than dropping rows.
- The deck as a whole should compress the source's *prose*, never its *structures*
  (tables, diagrams, lists of components, numbered principles).

## Isometric artwork rules

The signature artwork is fake-3D isometric drawn as inline SVG. **Mandatory, not optional:
any layered architecture in the source (N-layer stacks, "X sits on top of Y", operational
layer diagrams) MUST be drawn as an `ISO.stack()` exploded stack with right-rail bracket
labels — never as flat stacked rectangles.** Flat rect-on-rect versions of a layer diagram
read as generic boxes and lose the deck's identity; at least 1–2 slides per deck should
carry the iso look. Give the stack a full-width slide (`viewBox` ≈ 1660×700, rail on the
right) when it has ≥3 layers with per-layer item lists. Conventions:

- Projection 2:1 (30°): a "flat diamond" plane at (cx,cy) with half-width w and
  half-height h=w/2 has corners `(cx,cy-h) (cx+w,cy) (cx,cy+h) (cx-w,cy)`.
- Cube of size s at (x,y): top diamond + left face + right face; faces filled with
  --bg2 / #0d1014, strokes --line2 at 1–1.25px. Fill some cubes' top with the section
  accent at 12–18% opacity to highlight.
- Exploded stack: 3–6 planes at the same cx, stepped cy (Δ≈150–170px at w≈420), top
  layer drawn LAST (SVG paint order: draw from BOTTOM layer upward so upper layers
  overlap correctly). Each plane gets a right-rail bracket label (micro-label + 1-line
  description + optional item list). Use the template's `isoPlane()`/`isoCube()` JS
  helpers instead of hand-writing coordinates.
- Connector arrows: long curved paths, stroke --acc, 1.5px, marker-end small triangle,
  opacity .8. Dashed (4 4) = data flow / read; solid = write / action.
- Scatter fields ("your operational systems"): rows of small cubes/cylinders with
  jittered positions; keep them low-contrast (--line2 strokes only).

## Flow diagrams (mermaid replacement)

- Nodes: `<rect rx="6">` fill --bg2 stroke --line2; title 13px --ink, sub-lines 11px
  --ink2; mono for code-ish names. Decision = diamond; datastore = cylinder
  (rect + 2 ellipses); external = dashed stroke.
- Edges: orthogonal or gently curved paths, --ink3 1.25px, arrowhead marker; label on
  a small --bg pill so the line doesn't strike through text.
- Groups/subgraphs: dashed rounded rect + micro-label at its top-left.
- Cycles (the "loop vs line" motif): lay nodes on a circle, close the loop visibly —
  the closed circle IS the point.
- Keep node text ≤3 lines; overflow goes to a footnote under the figure.

## Anti-patterns (reject on sight)

- Big hero numbers with one word under them as a whole slide
- Emoji, gradient-blob backgrounds, glassmorphism, drop shadows
- Tables re-rendered as chat-style cards losing columns
- Mermaid.js embedded at runtime (uncontrollable layout, network dependency)
- Truncating a comparison table's columns to fit — shrink font to 13px or split slides
- Rounded corners >8px; border widths >2px
