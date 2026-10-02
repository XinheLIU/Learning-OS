---
name: grill
description: "Quiz the author from a reviewed teaching chapter, one question at a time, and route misses to author or draft gaps. Use for 拷问, 自测 or a requested pre-delivery chapter self-test; this assesses recall, not prose quality."
---

Last updated: 2026-10-01

# Grill

## Overview

A reviewed draft in, a routed miss list out. `review-draft` judges the text; this judges **the
author against the text**. The two failures it separates are invisible from either side alone:

| You couldn't answer, and… | Diagnosis | Route |
| :--- | :--- | :--- |
| …the draft *does* teach it | **author gap** — you wrote it, you don't hold it | a learning note; the loop can pick it up |
| …the draft *doesn't* teach it | **draft gap** — the chapter reads as if it taught it | an `edit-targeted` task |

That split is the whole skill. A chapter that survives a grill is one the author can defend without
the file open — which is the independence claim the writing system makes on the learning system's
behalf.

## When to Run

Run this skill when:
- `brief.md` has `brief-kind: chapter` **and** `教学目标` is present (a teaching claim)
- `review-draft` verdict is `ship`

Skip this skill when:
- `brief-kind: piece` — the chapter's value is the argument, not the retention
- No `教学目标` in the brief — the chapter makes no capability claim

These fields determine eligibility, not authorization. Run when requested or included in the authorized chapter workflow. Read v1/v2 fields with [brief-format.md](../../foundations/frame/references/brief-format.md).

## Hard Rules

1. **One question at a time.** Never print the next before the current answer lands. A batch of six
   questions is a reading comprehension test — the author skims for all six answers at once.
2. **Never show the anchor before the answer.** Every question is computed from a draft span, and
   that span is recorded in the log; quoting it in the question hands over the answer. An answer
   given with the anchor visible is **peeked** — log it as such, and it is never a pass.
3. **Never answer for the author.** No hints containing the answer, no "as your §2.3 explains…".
   One decomposition or one narrowing question when they're stuck, then log the miss.
4. **"I don't know" is a logged miss**, not a skipped question. It is the cheapest honest signal in
   the whole loop.
5. **Every miss gets exactly one route.** Not both, not neither. The routing test below decides.
6. **Never edit the draft.** This skill emits tasks; `edit-targeted` applies them.
7. **Never grade generously.** A partial answer that names the what but not the why is a miss on
   the why. Generosity here buys a chapter that ships undefended.
8. **The draft is the answer key, not your knowledge.** If the draft is wrong and the author is
   right, that is a finding for `review-draft`, not a miss — log it and move on.

## Workflow

### Step 1: Build the question set

Read the brief and the draft. Generate questions from **v2 required teaching nodes (claim, premise, concept or conclusion) and Code & math**, or legacy **二层 nodes and Code & math** —
one per node the chapter claims to teach, weighted toward what the reader would most doubt.

Three kinds, and a chapter needs all three:

| Kind | Asks | Fails when |
| :--- | :--- | :--- |
| **Concept check** | State the mechanism in your own words | The author can only recite the label |
| **Why-question** | Why is it this way and not the obvious alternative? | The chapter asserted a design without its reason |
| **面试题** | Apply it to a case the chapter never shows — a changed constraint, a broken assumption, a number that moves | The chapter teaches recognition, not use |

For each question record, **privately**, the anchor: `<file> § <section>`, plus the first and last
sentence of the span that answers it. A question with no anchor in the draft is out of scope — the
chapter never claimed it. Drop it, or, if it is something the chapter *should* claim, log it
directly as a draft gap and do not ask it.

Size: 6–10 questions for a chapter. Say the count up front.

### Step 2: Quiz

One question. Wait. Take the answer. Then, before saying anything about it, re-read the anchor span.

Grade against the anchor, not against everything you know about the topic:

- **Pass** — the answer carries what the anchor teaches, in the author's own words.
- **Partial** — the what without the why, or the right mechanism with the wrong direction. Name
  precisely which half is missing.
- **Miss** — absent, wrong, or "I don't know".

Say the grade, then move on. Do **not** teach the answer during the quiz — a grill that turns into
a tutorial has taught to its own test, and the remaining questions are now warm. Teaching happens
after the last question, or in `/learn` afterward.

### Step 3: Route every miss

For each miss and partial, apply the routing test to the anchor span:

> **Could a reader who has only this text — no prior knowledge, no author in the room — answer this
> question?**

| Answer | Route | Output |
| :--- | :--- | :--- |
| **Yes** | author gap | A log row; and if `learning/<slug>/` exists, a suggested retrieval item — proposed, never written directly (the ledger is `/recall`'s) |
| **No** | draft gap | One `edit-targeted` task line: file, section, and the instruction |

Read the span before answering the test. The temptation is to route everything to the author (the
draft is yours, and you know what you meant) or everything to the draft (the miss stings). Both
produce a useless log.

A draft-gap task names one location and one instruction — it is the input format `edit-targeted`
takes, not a wish:

```markdown
- [ ] `transformer.md § 2.3 Multi-Head` — the split/merge is stated but never says why heads are
      concatenated rather than averaged. Add one sentence at the paragraph ending "…each head
      attends independently."
```

### Step 4: Write the log and report

Write `drafts/<piece>/grill-log.md`:

```markdown
# Grill log: <piece>

Last updated: YYYY-MM-DD

**Score:** <n> pass / <n> partial / <n> miss, over <n> questions
**Verdict:** defended | rewrite first | not yours yet

| # | Question | Anchor | Grade | Route |
| :--- | :--- | :--- | :--- | :--- |
| 1 | <question as asked> | `<file> § <section>` | pass | — |
| 2 | <question as asked> | `<file> § <section>` | miss | draft gap → task 1 |
| 3 | <question as asked> | `<file> § <section>` | partial | author gap |

## Draft-gap tasks — for `edit-targeted`

- [ ] `<file> § <section>` — <instruction>

## Author gaps — for the learning loop

- <concept> — <what was missing, in one line>. Anchor: `<file> § <section>`
```

Also write two companion files beside the log:

**`drafts/<piece>/tasks-for-edit-targeted.md`** — the draft-gap task list only, in `edit-targeted` input format:

```markdown
# Draft-gap tasks from grill — for `edit-targeted`

Last updated: YYYY-MM-DD

- [ ] `<file> § <section>` — <instruction>
```

**`drafts/<piece>/gaps-for-learning.md`** — the author-gap list only:

```markdown
# Author gaps from grill

Last updated: YYYY-MM-DD

- <concept> — <what was missing>. Anchor: `<file> § <section>`
```

These two files are the machine-readable handoffs. `grill-log.md` is the human-readable record.

Verdict rule: **rewrite first** if any draft gap exists — the chapter reads as if it taught
something it didn't. **Not yours yet** if author gaps outnumber passes on §1 nodes; the chapter may
be fine, but the claim behind shipping it isn't. Otherwise **defended**.

Report the score, the verdict, and the task count. Then stop — the author decides what to apply.

## Contract test

Every question has a recorded draft anchor, and no anchor was shown before its answer; every miss
and partial produces exactly one route (author gap **or** draft gap, never both); every draft-gap
task names one file, one section, and one instruction; the draft file is byte-for-byte unchanged;
the log lands at `drafts/<piece>/grill-log.md`; `tasks-for-edit-targeted.md` contains only draft-gap tasks; `gaps-for-learning.md` contains only author gaps; no retrieval ledger row is written directly.

## Handoffs

**In:** a draft `review-draft` has passed (verdict ship), plus its brief. Grilling an unreviewed
draft wastes the run — half the misses will be craft defects `review-draft` would have named.

**Out:**
- Draft gaps → `tasks-for-edit-targeted.md` (feed directly to `edit-targeted`) → re-`review-draft` the changed unit.
- Author gaps → `gaps-for-learning.md` → `/learn` (tutor mode) or a proposed `/recall` item, if a course exists for the topic.
- Verdict `defended` → `package-chapter`.

## Boundaries

- vs `review-draft`: that judges the text against the brief and returns findings. This judges the
  author against the text and returns questions. A defect only this skill can find is a passage
  that reads correctly and teaches nothing.
- vs `/evaluate`: that assigns rubric levels across a topic's accumulated learning evidence. This
  is a per-piece ship gate and assigns no mastery level.
- vs `/recall`: that owns the retrieval ledger and the scheduling. This proposes items; it never
  writes rows.
- vs `edit-targeted` (`edit-targeted`): this emits tasks, never applies them.
