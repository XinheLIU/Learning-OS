---
name: insert-inline-images
description: Place existing images from disk into Markdown and HTML documents at contextually appropriate points, styled to match host document. Never authors new images — use book-diagrams for that. Tier 1: primitive, ~15 min. Use when asked to illustrate with images that already exist on disk.
---

Last updated: 2026-09-22

# Inline Illustrator

Place existing images into `.md` / `.html` documents so each image lands where text needs it and looks native to document's design. Avoid: wrong placement (filename guesswork), ugly placement (ignoring design system), under-placement (leaving curated images unused).

## Workflow

1. Inventory the images (script)
2. Look at every image — actually view it
3. Read the target document — content and design system
4. Match images to insertion points
5. Insert with document-native markup
6. Verify (script + visual check)

### 1. Inventory

```bash
scripts/image_inventory.py <images-or-dirs> --relative-to <target-doc>
```

Reports format, pixel size, aspect class (banner/landscape/portrait), file weight, and the
URL-encoded relative `src` to use from the target document. Trust the printed `src` —
hand-computed relative paths and unencoded spaces are the top cause of broken images.

### 2. Look at every image

View each candidate with Read tool. Never insert an image that has not been viewed — filenames lie. For each image record:

- **Subject**: what it depicts, including text/labels inside
- **Type**: diagram / screenshot / photo / logo / banner
- **Background tone**: light, dark, or transparent
- **Native width**: keep CSS width ≤ native pixels ÷ 2 for retina displays

### 3. Read the target document

Skim full document, then note:

- **Theme and tokens**: light or dark; CSS custom properties, border-radius, border and shadow habits
- **Language**: captions and alt text follow document's language
- **Layout unit**: article column width, or slide grid with fixed heights
- **Existing figures**: if convention exists, extend it; don't invent a second one
- **Redundancy**: sections with diagrams/tables don't need duplicate images

### 4. Match images to insertion points

Start from inclusion: folder user points at is usually curated. For each image, actively search document for best placement; mark skipped only after search fails. Bar for skipping: "no honest, informative placement exists", not "text survives without it".

Where placements hide:

- **Body claims** — image is evidence or structure for what paragraph just said. Place after text that introduces idea.
- **Document's frame** — intro, methodology, conclusion. Image about where document comes from can anchor frame.
- **Transitions** — image with two readings can bridge sections.
- **Caption-rescued images** — if honest caption teaches reader something, image qualifies.

Guards:

- Never overcrowd: fixed-height slides that are full stay imageless; no two figures back-to-back unless deliberate comparison.
- Never duplicate: section already visualized doesn't get redundant image.
- Never stretch too-small image into hero slot.

Write plan as short list — image → section → one-line reason, plus reason per skipped image. If skipping more than ⅓ of images user pointed at, show skipped list before finalizing.

### 5. Insert

**Markdown** — standard syntax; alt text says what the image shows, an italic caption line
(if the doc benefits) says why it matters here:

```markdown
![Apollo 发布闭环：Build System → Registry → Hub → 各环境](../aseets/Apollo.png)
*Apollo 用一个注册中心把发布从"推送"变成"编排"。*
```

URL-encode spaces and parentheses in paths. In an Obsidian vault, use the vault's existing
embed style (`![[image.png]]` vs relative paths) — match what neighboring pages do.
Pure Markdown has no width control; where the renderer allows inline HTML, use
`<img src="..." alt="..." width="640">` to apply the retina-target width — otherwise
accept full-column rendering and note it.

**HTML** — read [references/html-patterns.md](references/html-patterns.md) before the
first HTML insertion. Core discipline: add one shared figure kit `<style>` block wired to
the host's own CSS variables, then insert `<figure class="fig"><img ...><figcaption>` at
each point. The reference covers cross-theme framing (light image on dark page and vice
versa), wide-banner breakouts, tall images, screenshot chrome, and slide-deck layouts
(media split, full-bleed evidence slide, fixed slide-height handling).

Theme mismatches are the #1 elegance killer: an image whose background clashes with the
page must sit in a padded panel or hairline frame — never raw.

### 6. Verify

```bash
python3 ../scripts/verify_references.py <docs...>
```

Must report zero BROKEN. Then re-read each modified region for flow, and for HTML render a screenshot (headless browser if available) to confirm images sit within their layout — especially fixed-height slides, where an unconstrained image overflows. Long pages don't fit one screenshot: capture at a large fixed `--window-size` height and crop a band around each insertion point, rather than trusting a single squashed full-page shot.

## Input Contract

**Required:** a curated images folder + a target document.

**Precondition:** images must already exist on disk. This skill NEVER creates new images — use `book-diagrams` for that.

**Boundary:** if the images don't exist yet, stop and say so. Do not generate placeholder content.
