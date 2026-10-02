---
name: edit-targeted
description: "Apply one requested repair to a named span of a draft, preserving surrounding prose. Use for targeted edits, tightening a paragraph, replacing an example or applying a specific review finding."
---

Last updated: 2026-10-01

# Edit Targeted

## Overview

One instruction plus one location in, minimal diff out. This is the editing half of the writing loop; `review-draft` is the other half. Together they make the copilot cadence: review → edit → review, in minutes.

The value is entirely in what it *doesn't* touch. An agent that improves the paragraph below the one you asked about destroys the author's ability to trust the diff, and with it the whole loop.

## Hard Rules

1. **Minimal diff.** Change the smallest span that satisfies the instruction. Everything outside it stays byte-identical except the required near-top `Last updated` date. Report that metadata change separately.
2. **One finding at a time.** Given a review report, apply the named finding. In an authorized improvement workflow, apply findings sequentially and verify each affected span; a review-only request does not authorize editing.
3. **Never volunteer adjacent improvements.** Noticed something else? Mention it in the report afterward; do not edit it.
4. **Preserve the author's voice.** Their vocabulary, sentence rhythm, and register are the material, not the defect. If the brief carries a *Vocabulary* line, it is binding.
5. **Never fabricate.** No new examples, numbers, or citations that aren't in the materials or the brief. If the instruction requires evidence that doesn't exist, say so instead of inventing it.
6. **Don't reformat.** No heading-level changes, list-style normalization, or whitespace cleanup unless that *is* the instruction.
7. **Ask when the target is ambiguous.** Two paragraphs could match "the section on chunking" — ask which, rather than picking.

## Workflow

### Step 1: Resolve the target

Pin the instruction to an exact span: file, section, and the first and last sentence of the region to be changed. Quote it back before editing if the span is longer than a paragraph or the instruction is vague ("tighten the middle").

### Step 2: Check the constraints

- **Brief present?** Read the relevant lines. Read v2 Scope and node references, or legacy *Cost paid* and ladder fields, using [brief-format.md](../frame/references/brief-format.md). If the user has explicitly changed scope, use that authorization and update the framing through `frame`; otherwise surface the unresolved conflict.
- **Evidence needed?** Use the brief evidence row and its limits. Missing facts or personal details route to `develop-examples`; hypothetical illustrations must remain labelled and cannot prove a factual claim.
- **Logic affected?** A changed premise, claim or scope routes to `develop-argument`/`frame`. Identify dependent evidence, figures and passages before calling the repair complete.

### Step 3: Edit

Apply the change to that span only, then update the near-top `Last updated: YYYY-MM-DD` date. Common instruction types:

| Instruction | Scope of the diff |
| :--- | :--- |
| Tighten / cut length | Words inside the target paragraph; no reordering of surrounding paragraphs |
| Fix a transition | The last sentence of section A and/or the first of section B — nothing between |
| Replace a borrowed example with the author's incident | The example block; the claim it supports stays as written |
| Add a missing objection or cost line | One inserted passage at the named point — inserts at the specified location only, never drafts surrounding content |
| Define a term / add an anchor | The clause where the term first appears |
| Split a paragraph carrying two ideas | A break plus at most a connecting clause |

If satisfying the instruction genuinely requires touching more than the named span — the transition can't be fixed without changing section B's opening claim — **name the affected spans**. Continue when the broader repair is already authorized; otherwise ask for the newly required scope before changing it.

### Step 4: Report

State, in three lines or fewer:

- What changed, by location (`section 3, paragraph 2`)
- Why that satisfies the instruction
- Anything noticed but deliberately left alone

A standalone edit ends here. An authorized improvement workflow can continue with verification and the next finding.

## Handoff

- **`review-draft`** re-reviews the changed unit; if a premise changed, include its affected conclusions, evidence and diagrams.
- Repeated conflicts with the brief on the same section usually mean the angle is wrong, not the prose. Two or three of those and the honest move is `/frame`, not a third edit.

## Input Contract

**Required:** one instruction + one target location (file + section or span).

**Optional:** `brief.md` for constraint checking.

**Preconditions:** none for the location. If the instruction requires evidence (a fact, example, number), it must exist in the materials, brief markers, or verifiable public record.

## Completion Criteria

The skill is done when:
1. The diff is minimal — bytes outside the named span and required date are unchanged
2. The 3-line report states what changed, why, and what was noticed but left alone
3. Any changed logic/evidence is rechecked within authorized scope; no unresolved dependency is called complete
