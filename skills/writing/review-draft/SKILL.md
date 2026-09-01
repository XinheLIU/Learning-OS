---
name: review-draft
description: Review a draft and return ranked findings — never rewrites. Runs a depth gate against the piece's brief first, then the craft checklist. Works on any unit: a paragraph, a section, a chapter, a whole post. Use for "review this draft", "what's wrong with this section", "is this deep enough", 评审, 修改意见.
---

Last updated: 2026-09-01

# Review Draft

## Overview

Draft in, ranked findings out. This skill is the reviewer half of the writing loop; `edit-targeted` is the other half. The two must cycle in minutes — that cadence, not any single skill, is what human-in-the-loop cashes out to.

Runs on **any unit**: one paragraph, one section, a chapter, a finished post. Reviewing a paragraph mid-draft is the normal case, not a degraded one.

## Hard Rules

1. **Never rewrite.** No corrected version, no "here's how I'd phrase it" paragraph. A suggested replacement of more than a clause is a rewrite wearing a suggestion's clothes — hand the finding to `edit-targeted` instead.
2. **Every finding quotes the offending passage** and names what it violates: a brief line or a numbered technique.
3. **Rank fix-first.** Findings are ordered by what would change the piece most, not by where they appear in the text.
4. **Depth before craft.** Axis 1 runs first and can stop the review — polishing a flat piece is wasted motion.
5. **No invented facts.** Never suggest an example, number, or citation that isn't in the materials or the brief.
6. **Say when it's fine.** A section with no real findings gets "no findings" — manufactured nitpicks train the author to ignore the reviewer.

## Workflow

### Step 0: Locate the brief

Look for `brief.md` beside the draft (`drafts/<slug>/`) or wherever the user points.

- **Brief present:** run both axes.
- **No brief:** run axis 2 only, and say so in one line — "no brief found; craft review only, depth unchecked." Do not invent an angle to review against.

### Axis 1 — Against the brief (the depth gate)

Read the brief, then the draft, and answer each question with evidence from the text:

| Check | Failure looks like |
| :--- | :--- |
| Does the draft argue the **angle**, or slide back into summarizing the source? | Section headers that mirror the source's headers |
| Is the **议题** still a live question the reader could answer either way? | The question resolved in the first section, or never restated |
| Is **正方** engaged at full strength, or forgotten after the opening? | The opponent named in paragraph 1 and never answered; or weakened into a strawman nobody holds |
| Is the opponent someone **outside the material**? | The piece's target is the source author — inconsistent, overclaiming, decorative. That is a book review, not a piece |
| Is every **一层论点** actually argued, and in the brief's order? | A pillar reduced to one passing sentence, or silently dropped |
| Does every **二层** line reach its **三层** evidence? | A mechanism asserted where the ladder promised a source section or the author's incident |
| Is each **author marker** present at the node it was anchored to? | The incident moved to the intro as colour, leaving its own claim unevidenced |
| Did `cut` material leak in? | A section carrying content the selection map excluded |
| Does the *Cost paid* line still hold? | Scope quietly widened back to covering everything |
| Are the **author's markers** used, or replaced by borrowed examples? | The author's incident missing at the point the reader most doubts the claim |
| Does anything here disagree with anyone? | Every claim uncontested |

Then the decisive test, applied paragraph by paragraph:

> **Could the source's author have written this paragraph?**

And the companion test, for the review failure mode:

> **Would this paragraph mean anything to a reader who never saw the source?**

If the first is yes for every paragraph, the piece is flat. If the second is no for most of them, the piece is a book review — the material became the subject instead of the evidence. Either way, **verdict: reframe or kill.** Say it plainly, name the two or three paragraphs that come closest to being the author's own, and send the piece back to `/frame-piece` Step 4 with the draft as new evidence. Do not continue to axis 2 — craft findings on a piece that is about to be reframed are noise.

If the piece passes, list axis-1 findings as normal findings and continue.

### Axis 2 — Against the craft checklist

Run the revision checklist in [`../write-content/references/techniques.md`](../write-content/references/techniques.md) as a *reviewer*, not a self-check: each failed line becomes a finding with the offending passage quoted and the technique named.

Scope to the unit under review. Whole-piece checks (opening tension, compressed close, one thesis) don't apply when reviewing a single paragraph — skip them rather than reporting them as failures.

### Step 3: Rank and report

Order by impact: depth failures → structural failures (ladder broken, section changes nothing) → local craft (missing example, undefined term, absent anchor) → line-level. Within a tie, earlier in the document first.

## Output Format

```markdown
## Review: <unit reviewed>

**Verdict:** ship / edit / reframe or kill
<one sentence saying why>

### Findings

**1. <what's wrong>** — `<brief line or technique N>`
> <quoted passage>

<what it fails, and what would satisfy it — one or two sentences. No replacement prose.>

**2. …**

### No findings on
<sections that are fine — one line, so the author knows they were read>
```

Deliver findings and stop. The author decides which to act on; `edit-targeted` applies them one at a time.

## Handoff

- **`edit-targeted`** consumes findings individually. Feed it one finding, not the whole report.
- **`frame-piece`** receives the piece when the verdict is "reframe or kill".
- Re-review after edits: review the changed unit, not the whole piece, so the loop stays fast.
