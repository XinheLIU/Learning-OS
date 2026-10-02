# HTML figure patterns

Last updated: 2026-09-01

Recipes for inserting images into HTML documents so they look native to the host design.
Every recipe reads the host's CSS custom properties — replace the `var(...)` names with
whatever tokens the document actually defines (inspect its `:root` first). Never introduce
a second design language.

## Contents

1. Shared figure kit (add once)
2. Article figure with caption
3. Cross-theme frame (light image in dark doc, and vice versa)
4. Wide image breakout in a narrow column
5. Tall/portrait image
6. Screenshot treatment
7. Slide-deck patterns
8. Do / don't

## 1. Shared figure kit (add once)

Add one `<style>` block (or append to the existing one) instead of repeating inline styles.
Derive every value from host tokens; the fallbacks below are neutral.

```html
<style>
  .fig{margin:2.2rem auto;max-width:100%}
  .fig img{display:block;width:100%;height:auto;border-radius:10px}
  .fig figcaption{margin-top:.6rem;font-size:.82rem;line-height:1.5;color:var(--muted,#6b7280);text-align:center}
</style>
```

Match `border-radius` to the document's existing radius (cards, code blocks). If the
document uses sharp corners, use `border-radius:0`.

## 2. Article figure with caption

```html
<figure class="fig">
  <img src="../aseets/apollo.png" alt="Apollo architecture: build system publishes to a registry, Apollo Hub deploys to dev and prod clouds" loading="lazy">
  <figcaption>Apollo 的发布闭环：Build System 注册产物，Hub 编排到各环境。</figcaption>
</figure>
```

- `alt` states what the image shows (for readers who can't see it); the caption states why
  it matters *here*. Don't duplicate one into the other.
- Caption language = document language.
- Add `width`/`height` attributes (native pixels) when the document cares about layout shift.

## 3. Cross-theme frame

An image whose background clashes with the page (white diagram on a dark page, dark
screenshot on a paper-white page) must sit in a deliberate panel, not bleed raw edges.

```css
/* light image hosted on a dark page: a padded light panel reads as intentional */
.fig-panel{background:#f4f4f2;border:1px solid var(--line,#2a2f36);border-radius:12px;padding:14px}
/* dark image on a light page: hairline + dark mat */
.fig-panel-dark{background:#14171b;border:1px solid var(--line,#e6e3dd);border-radius:12px;padding:14px}
```

```html
<figure class="fig">
  <div class="fig-panel"><img ...></div>
  <figcaption>...</figcaption>
</figure>
```

Wrap only the `<img>` in the panel — the caption stays outside on the page background so
it keeps the host's caption color token. Putting the panel class on the `<figure>` traps
the caption inside the mat, forcing an off-token caption color.

Images with *transparent* backgrounds need a panel whose tone matches the tone the image
was designed for (check where its text/strokes are legible).

## 4. Wide image breakout in a narrow column

For ultra-wide banners (aspect ≥ 2.4:1) inside a narrow article column, break out modestly
rather than shrinking the content to a ribbon:

```css
.fig-breakout{width:min(1100px,92vw);margin-left:50%;transform:translateX(-50%)}
```

Alternatively crop-as-band: fixed height, `object-fit:cover`, as a section divider:

```css
.fig-band img{height:180px;object-fit:cover}
```

## 5. Tall/portrait image

Never let a portrait image consume a full screen of scroll. Cap its height and center:

```css
.fig-tall img{width:auto;max-width:100%;max-height:70vh;margin:0 auto}
```

In two-column layouts, a tall image is the natural media column.

## 6. Screenshot treatment

UI screenshots need separation from the page (they contain their own chrome):

```css
.fig-shot img{border:1px solid var(--line,#e6e3dd);border-radius:10px;box-shadow:0 8px 28px rgba(0,0,0,.08)}
```

Drop the shadow entirely if the host design uses no shadows (flat design ⇒ hairline only).

## 7. Slide-deck patterns

Decks are grids, not flowing prose — an image joins a slide's layout system.

**Media split** — image as one column of the slide grid; text keeps the other:

```html
<div class="cols" style="display:grid;grid-template-columns:1.1fr 1fr;gap:28px;align-items:center">
  <div> ...existing bullets... </div>
  <figure class="fig" style="margin:0"><img ...><figcaption>...</figcaption></figure>
</div>
```

**Full-bleed evidence slide** — image is the slide; one caption line, no competing text:

```html
<section class="slide">
  <header class="s-head"><h2>...</h2></header>
  <figure class="fig" style="margin:0;flex:1;min-height:0;display:flex;flex-direction:column">
    <img style="flex:1;min-height:0;object-fit:contain" ...>
    <figcaption>...</figcaption>
  </figure>
</section>
```

**Accent integration** — if slides carry accent variables (e.g. `--a`), tint the figure's
border/caption with `var(--a)` so the image inherits the slide's color story.

Respect the deck's fixed slide height. In flex-based slides use `object-fit:contain`
inside a flexed figure (above); in absolutely-positioned or grid slides always give the
`<img>` an explicit `max-height` (portrait images especially — combine with the §5 cap).
Expect to restructure the slide's top-level container: adding an image to an existing
slide usually means wrapping its content in a new grid or adding `flex-wrap`, not just
dropping a `<figure>` in. That is legitimate — keep the slide's own classes and spacing.

## 8. Do / don't

- **Do** reuse the host's tokens (`--line`, `--muted`, accent vars) for every border,
  caption, and background.
- **Do** keep one visual grammar: same radius, same caption style for all figures in a doc.
- **Don't** upscale: rendered width ≤ native pixel width (÷2 for retina crispness).
- **Don't** stack two figures back-to-back unless they are an intentional comparison pair.
- **Don't** add shadows, gradients, or borders the document doesn't already use elsewhere.
- **Don't** hand images a caption that just repeats the heading above them.
