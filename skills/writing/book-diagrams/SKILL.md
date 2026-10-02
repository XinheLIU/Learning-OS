---
name: book-diagrams
description: "Hand-author SVG diagrams for articles and chapters from agreed logic or concept relationships, deriving visual style from the target document. Creates new SVGs only — never places pre-existing images (use insert-inline-images for that). Tier 1: primitive, ~30 min per diagram. Use when asked to create diagrams, make svg plots, illustrate this chapter, convert a table or ASCII block into a diagram."
---

Last updated: 2026-10-01

# Book Diagrams

Hand-authored SVG illustrations for the target article or chapter. The deliverable is not any
single diagram — it is a *visual language*: a set of diagrams that read as siblings across
the whole book. Every file is plain SVG that a future session can reopen and edit as text.

This file is self-contained: principles, the book's current style facts, repo conventions,
and workflow are all here.

## What to Diagram

1. **Diagram relationships, keep tables for lookup.** Tool catalogs and reference lists
   that readers scan row by row stay as tables. Convert only content whose *shape* the
   prose or table flattens: flows, contrasts, hierarchies, cycles, splits, timelines.
2. **One diagram answers one question.** Phrase that question as the alt text. If a draft
   answers two questions, split it.
3. **Insert after the concept, before the detail.** The diagram gives the shape; the table
   under it keeps the detail. Never delete a table when adding its diagram. ASCII-art
   blocks *may* be replaced — the SVG is the same content, better rendered.
4. **Compress wording, not meaning.** Text inside a diagram is distilled from the
   surrounding prose — shorter than the sentence, never different from it.

## How to Choose a Form

Do not pick from a template menu. Ask what the idea *is*, and let that dictate the layout:

- A **judgment** (right vs wrong, before vs after) wants a side-by-side contrast the eye
  can compare item against item.
- A **process** wants direction: a chain, a wrapped sequence of steps, a loop. Feedback and
  failure paths look different from the main path (dashed, or a different color).
- A **classification** wants same-shaped cards whose hue separates the categories, with
  hierarchy shown by position (parent above, rail down to children).
- A **proportion or split** wants length or area, not a list.
- A **culmination** — many steps producing one key artifact — wants that artifact visually
  heavier than everything feeding it (full-width, warm color, bold).

Most concepts combine these (a chain that fans out, a grid that ends in a warning). Invent
the combination the concept needs; the constraint is coherence, not repertoire. Before
drawing, say in one sentence what the reader's eye should do first, second, third — if you
can't, the form is wrong.

## How to Derive the Style

Style is *discovered, then extended* — never invented per diagram and never copied
pixel-for-pixel from a reference image:

1. **Read the existing family first.** Open two or three SVGs already in the tree's
   `assets/` and extract their invariants: palette, corner radii, stroke weights, font
   stack, density, how arrows and captions are handled. New diagrams must keep those
   invariants unless the user asks for a redesign.
2. **Treat reference images as evidence of taste, not specs.** From a sample, extract the
   *decisions* — flat pastel fills with slightly darker strokes, generous whitespace, no
   gradients or shadows, semantic color, short labels — then re-make those decisions for
   your content. Matching the sample's exact boxes while the content mismatches is failure;
   matching its restraint with a layout the content actually needs is success.
3. **Color carries meaning before decoration.** Keep the semantic assignments stable across
   the whole book (in this book: green = good practice or established fact; red = violation,
   danger, or the one thing that matters most; muted gray-blue = neutral/human-side; pastel
   hues distinguish peer categories; dashed strokes = uncertain, emerging, or feedback).
   A reader who has seen three diagrams should predict the fourth's colors.
4. **Typography is a scale, not a choice per label.** One sans stack, one mono stack for
   code, and 3–4 sizes used consistently (roughly: section labels ~16 bold, card titles
   15–17 bold near-black, body 13–15 in the category color, captions 12.5–13 italic gray).
   Titles dark, content colored, annotations gray — that contrast does the layering.

### Example family (fallback only when the target has no established style)

- Canvas: white, width 1310, height to fit; `font-family="-apple-system, 'PingFang SC',
  'Helvetica Neue', Arial, sans-serif"`; code in `ui-monospace, 'SF Mono', Menlo, monospace`.
- Shapes: rounded rects (`rx` 10–16), stroke-width 1.5, dashes `6 5`/`7 5`, 2px arrows with
  small triangle markers (one `<marker>` per color).
- Established palette (fill/stroke/text): green `#e9f3ee`/`#3d8b70`/`#1f6a51` · red
  `#fdf0ef`/`#c0564f`/`#b5453c` · gray-blue `#eef0f4`/`#8592a6`/`#45536b` · beige panel
  `#f7f7ee`/`#cfcfc0` · step-blue `#e8f2fd`/`#7aabdd`/`#2b5d9b` · category pastels
  (purple `#f4f1fe`/`#9b8cf0`, green `#e9f6f0`/`#4bab8d`, blue `#e8f2fc`/`#6ea8dc`,
  orange `#fdf4e3`/`#d9a648`, pink `#fdeeee`/`#d98080`, dashed beige `#f4f3ec`/`#b9b7a8`).
  Add hues sparingly and at the same saturation level; never introduce gradients, shadows,
  or pure-saturated colors.
- Shipped examples: the `Legacy-*.svg` set in `book/en/assets/`, referenced from
  `book/en/03-power-user/legacy-codebases.md`.

## Craft

SVG has no layout engine — you are the layout engine:

- Compute coordinates explicitly; check that labels clear every arrow lane they cross.
- Budget characters before writing: Latin width ≈ `font-size × 0.54` per char (bold ≈ ×1.1);
  CJK ≈ `font-size × 1.0`. Keep each line inside container width minus padding; break into
  a second `<text>` line rather than shrinking below ~12.5px.
- Escape `&` as `&amp;` and `<` as `&lt;` in text content.
- Validate every file: `python3 -c "import xml.etree.ElementTree as ET; ET.parse('f.svg')"`.

## Destination conventions

- **Files:** local `assets/<Topic>-<Concept>.svg` beside the target document, following existing naming.
- **References:** content-local relative paths such as `./assets/X.svg`; alt text states the diagram's question. Keep packaged assets inside the piece folder.
- **Language:** match the target document. Translation or mirroring occurs only when requested; use `book-translator` for chapter prose.
- **Update the chapter's `Last updated:` date** on any edit.
- **Preview:** use the destination's existing preview mechanism or an image/browser viewer; inspect labels, arrows and clipping at readable scale.

## Workflow

1. **Ground.** Read the brief's Logic nodes/relations and relevant prose (legacy: ladder and source passages). Use the already agreed question and style; propose choices only when unresolved. Keep a mapping from each SVG element/arrow to its node/relation. If logic is missing, resolve it through `develop-argument` before illustrating.
2. **Draw** against the derived style; **validate**; **insert**; **preview**. Final check
   per diagram: does it answer its one question, does every element trace to the prose, is
   nothing clipped, and would it sit next to the existing family without looking adopted?

## Input Contract

**Required:** diagram question plus article/chapter context or an agreed logic structure. Existing SVGs are optional style evidence. Preserve relation direction and limiting conditions; visual grouping cannot invent causality. Check the semantic mapping after any logic change.

**Precondition:** the diagram concept. This skill NEVER uses pre-existing images as content — it draws new SVGs. For placing existing images, use `insert-inline-images`.

**Boundary:** one diagram answers one question. If you need two questions answered, this skill runs twice.
