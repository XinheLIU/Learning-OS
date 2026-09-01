---
name: write-content
description: Draft publishable prose from a brief (preferred) or raw materials — notes, outlines, research — through intake → outline → draft → revise. Use for blog posts, articles, book chapters. Non-fiction only.
---

# Write Content

> Last updated: 2026-09-01

## Overview

Transform a brief, or raw materials, into publishable prose (blog posts, articles, book chapters) that argues one idea well. Interactive workflow: settle intent before outlining, get outline approval before drafting.

Two modes:

| Mode | Input | Use when |
|---|---|---|
| **Brief-driven** (preferred) | `drafts/<slug>/brief.md` from `frame-piece` | The piece needs a point of view — an angle, an opponent, a cut-list |
| **Brief-less** | Materials only | Course notes into clean prose, explainers, summaries — where restating the source well *is* the goal |

Brief-less mode is honest and supported; it just cannot produce an authored angle, because the thesis it derives is the corpus's own. See Step 2.

## Hard Rules

1. **Non-fiction only.** No invented anecdotes, fictional characters, dramatized scenes.
2. **Never fabricate evidence.** Every example, number, quote must trace to materials or verifiable public facts. Mark unverified claims `[VERIFY: ...]`.
3. **Preserve attribution.** Carry citations from materials into output.
4. **Match materials' language** unless user specifies otherwise.
5. **One piece, one idea.** If materials contain several independent ideas, ask which to write.
6. **The brief is a contract.** With a brief present: draft only `core` and `support` sections, never `cut` material; keep the author's vocabulary verbatim; stay inside the *Cost paid* line. Widening scope needs the author's approval, not the drafter's judgment.

## Workflow

### Step 1: Intake

**Look for `brief.md` first** — in the working directory, in `drafts/<slug>/`, or wherever the user pointed. If one exists, read it plus only the sources its selection map marks `core` and `support`, then go straight to Step 3. The brief already answers thesis, audience, register, and scope with more depth than a clarify round could.

Without a brief, read all provided materials fully and build a private inventory:

- Candidate core idea(s) — the single claim the post could argue
- Evidence available: data, examples, cases, citations
- Gaps: claims with no support, missing context, undefined audience
- Reusable raw phrasing worth keeping

### Step 2: Clarify (interactive, brief-less mode only)

**Skip entirely when a brief is present.**

First check whether the candidate thesis is one the materials already argue — i.e. it restates a claim you could point to a line for. When it is, say so in one sentence and offer the choice:

> The materials argue this themselves (`06-practice-strategy.md:55`). Run `/frame-piece` first to find an angle of your own, or proceed with a faithful explainer?

Then ask **one round** of questions via AskUserQuestion — only what materials don't answer:

- **Audience & expertise level**
- **Register**: technical (precise, code-level detail) vs business (decision-level, minimal jargon)
- **Thesis**, if multiple core ideas are viable
- **Length target** and publishing venue

Skip if everything is clear.

### Step 3: Outline (interactive)

Produce a short outline following [references/techniques.md](references/techniques.md):

1. Opening tension — challenge a default belief or present a concrete problem
2. Ladder of question → answer → new question
3. Payoff — framework, checklist, decision rule, or applied takeaway
4. One-line compressed close

With a brief, the tension comes from the brief's 对立面 and the author's markers — not from tension manufactured out of the corpus. Show outline (section headers + one line each on argument and evidence) and get approval before drafting.

### Step 4: Draft

Read [references/techniques.md](references/techniques.md) and apply while writing. Register calibration:

| | Technical | Business |
|---|---|---|
| Examples | code, architecture, incidents | companies, decisions, tradeoffs |
| Depth | mechanism — how it works | consequence — what it changes |
| Jargon | define once, use freely | avoid; translate to outcomes |
| Specifics | component names, limits, versions | rounded figures tied to outcomes |
| Diagrams | Mermaid for every flow/cycle (~3–8) | at most one simple flow |
| Payoff | how-to steps, gotchas | decision framework, criteria |

**Weave the author's markers** (brief-driven mode). The disagreement from the brief is opening-tension material; the author's past mistake is example material and outranks any borrowed example from the sources (technique 16). Keep the author's vocabulary as written — do not upgrade it to more standard phrasing.

Write to `.md` file in working directory (kebab-case from title, with `Last updated: YYYY-MM-DD`). With a brief, write to `drafts/<slug>/` beside it.

### Step 5: Revise and deliver

Run revision checklist from [references/techniques.md](references/techniques.md), fix failures. With a brief, also confirm no `cut` material leaked in and the *Cost paid* line still holds. Deliver: file path, thesis in one sentence, any `[VERIFY]` markers to resolve.

**Next:** `review-draft` for structured feedback, then `edit-targeted` to apply findings.
