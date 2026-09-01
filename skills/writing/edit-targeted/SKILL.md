---
name: edit-targeted
description: Apply one instruction to one location in a draft — minimal diff, surrounding text untouched. Never a full rewrite, never volunteers adjacent improvements. Use for "tighten this paragraph", "fix the transition between these two sections", "replace this example with my incident", 改这一段, or to apply a single review-draft finding.
---

Last updated: 2026-08-31

# Edit Targeted

## Overview

One instruction plus one location in, minimal diff out. This is the editing half of the writing loop; `review-draft` is the other half. Together they make the copilot cadence: review → edit → review, in minutes.

The value is entirely in what it *doesn't* touch. An agent that improves the paragraph below the one you asked about destroys the author's ability to trust the diff, and with it the whole loop.

## Hard Rules

1. **Minimal diff.** Change the smallest span that satisfies the instruction. Everything outside it stays byte-identical — including wording you would have written differently.
2. **One finding at a time.** Given a review report, apply the finding the author named. Do not batch the rest.
3. **Never volunteer adjacent improvements.** Noticed something else? Mention it in the report afterward; do not edit it.
4. **Preserve the author's voice.** Their vocabulary, sentence rhythm, and register are the material, not the defect. If the brief carries a *Vocabulary* line, it is binding.
5. **Never fabricate.** No new examples, numbers, or citations that aren't in the materials or the brief. If the instruction requires evidence that doesn't exist, say so instead of inventing it.
6. **Don't reformat.** No heading-level changes, list-style normalization, or whitespace cleanup unless that *is* the instruction.
7. **Ask when the target is ambiguous.** Two paragraphs could match "the section on chunking" — ask which, rather than picking.

## Workflow

### Step 1: Resolve the target

Pin the instruction to an exact span: file, section, and the first and last sentence of the region to be changed. Quote it back before editing if the span is longer than a paragraph or the instruction is vague ("tighten the middle").

### Step 2: Check the constraints

- **Brief present?** Read the relevant lines. An instruction that pulls in `cut` material or breaks the *Cost paid* line is a conflict — surface it and ask, rather than silently obeying or silently refusing.
- **Evidence needed?** If the edit requires a fact, example, or number, confirm it exists in the materials, the brief's author markers, or verifiable public record. Otherwise mark `[VERIFY: ...]`.

### Step 3: Edit

Apply the change to that span only. Common instruction types:

| Instruction | Scope of the diff |
| :--- | :--- |
| Tighten / cut length | Words inside the target paragraph; no reordering of surrounding paragraphs |
| Fix a transition | The last sentence of section A and/or the first of section B — nothing between |
| Replace a borrowed example with the author's incident | The example block; the claim it supports stays as written |
| Add a missing objection or cost line | One inserted passage at the named point |
| Define a term / add an anchor | The clause where the term first appears |
| Split a paragraph carrying two ideas | A break plus at most a connecting clause |

If satisfying the instruction genuinely requires touching more than the named span — the transition can't be fixed without changing section B's opening claim — **stop and say so** with what the wider change would be. Getting permission is cheaper than a diff the author can't read.

### Step 4: Report

State, in three lines or fewer:

- What changed, by location (`section 3, paragraph 2`)
- Why that satisfies the instruction
- Anything noticed but deliberately left alone

Then stop. Do not offer a next edit; the author drives.

## Handoff

- **`review-draft`** re-reviews the changed unit — not the whole piece, so the loop stays fast.
- Repeated conflicts with the brief on the same section usually mean the angle is wrong, not the prose. Two or three of those and the honest move is `/frame-piece`, not a third edit.
