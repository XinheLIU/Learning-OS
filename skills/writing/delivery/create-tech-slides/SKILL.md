---
name: create-tech-slides
description: Build dense, deep-tech HTML slide decks (Palantir-style) from markdown docs/specs without losing detail. Derives from a finished draft; never edits back. Tier 3: adapter, ~90 min. Use when the user wants technical or architecture slides built from a markdown doc/spec WITHOUT losing detail (tables, diagrams, exact numbers, caveats), or mentions "deep-tech slides", "dense slides", "detailed HTML deck", "架构幻灯片", "深度技术 PPT", "别丢信息的 PPT", "Palantir 风格". Not for marketing-style decks with big fonts and one idea per slide.
---

# Deep-Tech Slides

Last updated: 2026-07-18

Produces the opposite of a keynote: engineering-drawing slides. Dark canvas, thin wireframe
diagrams, small type, every technical fact preserved. The reader is an engineer/architect who
wants the full picture on each slide, not a headline.

Files in this skill:

- `references/design-system.md` — tokens, type scale, slide anatomy, layout recipes, density budgets
- `references/components.md` — copy-paste markup for every component (tables, bracket rails, iso stacks, cube fields, SVG flow diagrams, tags, timelines)
- `assets/template.html` — self-contained working shell (nav, scaling, chrome injection, iso/node generators, `?check` overflow audit, print CSS). Demo slides between `<!-- SLIDES-START -->` and `<!-- SLIDES-END -->` markers show each major pattern.

## Non-negotiables

1. **Information preservation is the contract.**
   - Every table in the source stays a table (never prose-ified, never truncated to "top 3 rows").
   - Every diagram in the source (mermaid, ASCII, or described architecture) becomes a **native inline SVG** redrawn in the design system. Never embed mermaid.js, never screenshot, never replace a diagram with a sentence.
   - Every quantitative claim keeps its exact value **and its qualifier/evidence tag** (e.g. 【官方】【独立】【存疑】) if the source has one.
   - Keep the source's bilingual terminology as-is (e.g. "Action Type（动作类型）").
2. **Density, not size.** Fixed 1920×1080 canvas. Body text 17–18px, tables 15px, micro-labels 11–12px uppercase tracked, slide titles ≤ 52px. A content slide carries 120–250 words, or a full diagram plus supporting text. The lower half of the canvas must carry real content — the `.slide` is a flex column, and the `?check=1` audit flags underfill (content bottom < y=880). One-liner slides are only allowed as cover/closer.
3. **Self-contained single HTML.** System font stack, no CDN, no network requests; must work from `file://` and print to PDF.
4. **Verified, not assumed.** Ship only after the `?check=1` overflow audit passes and representative slides have been screenshotted and inspected.

## Workflow

1. **Read the source fully.** No skimming.
2. **Asset inventory.** List every table (T1..), diagram (M1..), key number/claim, and term. This list is the completeness contract.
3. **Slide manifest.** Map every inventory item to a slide before writing HTML. Summarizing prose is fine; dropping an inventory item is only allowed if you explicitly report it to the user as dropped. Group by the source's own narrative arc (e.g. Why → What → How), one section accent color per act.
4. **Build.** Copy the framework from `assets/template.html` (everything outside the `SLIDES-START/END` markers is the engine — reuse verbatim; see "Assembling a deck" below). Author slides using `references/components.md` patterns. Set `window.DECK = {title, meta, footer}` as the first line inside the slides section.
5. **Convert diagrams.** For each mermaid/described diagram: identify nodes, edges, groupings; redraw with the SVG conventions (`data-node` + edge paths + markers, or iso planes for layered architectures). Layered "stack" architectures MUST use the isometric exploded-stack pattern (`ISO.stack()` + right-rail bracket labels) — it is the signature look; never draw them as flat stacked rectangles. Every figure inside a grid column must be wrapped in `.figbox` (a bare `svg.fig` derives its height from viewBox ratio × column width and overflows the canvas — the #1 layout bug).
6. **Verify.** Open `deck.html?check=1` headless; the page sets `document.title` to `CHECK-OK`, `CHECK-UNDERFILL n`, or `CHECK-FAIL n` and appends `<pre id="check-report">` with per-slide overflow JSON and underfill detection. Screenshot the cover, the densest table slide, and every diagram slide at 1920×1080 (`#N` hash selects slide N). Fix overflow by tightening copy, shrinking a diagram, or splitting the slide — never by silently deleting content. Fix underfill by adding missing detail from the source, or using `.push-b` / `.grow` / `svg.fig.fill` to distribute content vertically.
7. **Report coverage.** Tell the user: slides produced, inventory items covered, anything dropped or compressed.

## Assembling a deck

```bash
SK=.claude/skills/create-tech-slides
sed -n '1,/SLIDES-START/p'  $SK/assets/template.html  > /tmp/deck-head.html
sed -n '/SLIDES-END/,$p'    $SK/assets/template.html  > /tmp/deck-tail.html
cat /tmp/deck-head.html my-slides-*.html /tmp/deck-tail.html > deck.html
```

Write slides in a few part-files if the deck is large. After assembly, fix `<title>` if needed
(`window.DECK.title` also sets it at runtime).

## Verification commands (macOS)

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# overflow audit — grep the report out of the DOM
"$CHROME" --headless --disable-gpu --dump-dom --virtual-time-budget=4000 \
  "file://$PWD/deck.html?check=1" | grep -o 'OVERFLOW-REPORT.*' | head -c 2000
# screenshot slide 12
"$CHROME" --headless --disable-gpu --screenshot=/tmp/s12.png --window-size=1920,1080 \
  --virtual-time-budget=4000 "file://$PWD/deck.html#12"
```

Then Read the PNGs and actually look at them: check for clipped text, cramped diagrams,
labels colliding with artwork, dead whitespace.

## Style DNA (summary — full spec in references/design-system.md)

Near-black blue canvas with a faint dot grid; 1px hairlines; pale steel-blue primary accent plus
teal/violet/sand section accents; isometric 2:1 wireframe artwork (exploded layer stacks, cube
fields, fan-outs); right-hand bracket annotation rails; uppercase micro-labels with wide
tracking; an engineering-drawing frame on every slide (eyebrow chip top-left, deck meta
top-right, page number bottom-right). Diagram line work is thin and precise; color is used
sparingly and semantically. The slide is a flex column — `.s-body` fills all remaining canvas below the header; `.push-b` / `.grow` / `.vcenter` / `svg.fig.fill` distribute content vertically so the lower half is never wasted.
