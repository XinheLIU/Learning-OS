# Trials — End-to-End Testing Guide

Last updated: 2026-09-06

A trial walks **one topic** through the entire skill chain and answers two questions at once: did
the learner actually learn it, and did the chain hold up while they did.

```text
/survey → /curriculum → /learn (start · done) → /practice → /recall (plan · sync) → /evaluate → /reflect
  map       orchestrate     lessons in HTML       real case    recall.html          gate      change
```

v3 note: the HTML course carries the learning experience. `/learn` opens lessons and does
checkpoint bookkeeping; `/recall` plans and reschedules — the retrieval itself happens in
`recall.html`. Chat sees bookkeeping and questions, not re-teaching.

## The trials

| Trial | Topic | Depth | Budget | Independence test |
| :--- | :--- | :--- | :--- | :--- |
| [`herdr/`](herdr/RUNBOOK.md) | herdr — safe agent delegation | `standard` | 60 min × 3 days | 8-item sealed battery, opened Day 3 |
| [`swe-basics/`](swe-basics/RUNBOOK.md) | Writing good code and design patterns | `quick` | 2 × 30 min × 3 days | 6-item rubric-graded battery, opened Day 3 |

Everything you need is in the runbook: the prompt to paste at each step, what to watch for while it
runs, a shell check, and numbered assertions to tick.

**The two are deliberately different topics, not two runs of the same test.** herdr is bounded and
has a ground truth — the installed CLI settles every question, so the trial can assert exact
answers. `swe-basics` has neither: the field is unbounded, its literature openly contradicts
itself, and an agent can lecture on it fluently from memory without citing anything. Each trial
reaches failure modes the other cannot.

| Property under test | herdr | swe-basics |
| :--- | :--- | :--- |
| Triage of an unbounded field — the SKIP list as deliverable | weak | **central** |
| `--depth` | `standard` | **`quick` — the other end** |
| `/synthesis-research` | not covered | **covered** |
| Refusal to teach from parametric memory | CLI is the authority | **must cite real sources** |
| Opinion presented as settled fact | n/a | **central** |
| Transfer onto the learner's own repository | small task | **refactor own code** |

Running both is what tells you whether `--depth` is a real parameter: same chain, opposite ends. If
`quick` and `standard` produce the same lesson lengths, it is a comment, not a parameter.

## How to read a runbook

Every step has the same four parts:

1. **Paste this** — the literal prompt. Don't paraphrase; the wording is part of the test.
2. **Watch for** — what should happen while it runs. Contract violations are visible here in real
   time and invisible afterward.
3. **Check** — a shell command whose output you compare against the table.
4. **Assertions** — numbered checkboxes. `L1.*` mechanical, `L2.*` you answer honestly.

## Evidence layers

| Layer | What it is | Gates? |
| :--- | :--- | :--- |
| **Layer 1** — mechanical | Did the files change correctly? Answerable by `ls` and `grep`. | **Always.** Any FAIL fails the trial. |
| **Layer 2** — behavioral | Did the teaching work *on you*? Cold recall, battery score. | **Yes**, on this trial. |
| **Layer 3** — experiential | "What did this make me do that grinding wouldn't?" | Never. Steers the next run. |

Layer 2 gates on both trials because the ignorance is genuine. On herdr the earlier course was
archived to `learning/herdr-v1/` and is not read during the run; on `swe-basics` the battery is
graded against rubrics you did not write and cannot see beforehand.

**A rubric-graded battery is easier to pass generously than an answer-keyed one.** `swe-basics`
carries three literal grading questions for exactly that reason — score the item 0 if any of them
fails. Generosity is the default failure mode there, not forgetting.

## Two rules that carry every trial

**The battery stays sealed.** It is authored on Day 0, in its own session, before any lesson
exists — then not printed, `cat`-ed, grepped, hashed, or summarized until Day 3. A session that has
seen it cannot honestly teach against it. Confirming the file exists is the only permitted
interaction.

**No recall firing may be warm.** In v3 the firing happens on `recall.html`: the prompt shows
alone, and an answer revealed before the learner committed an attempt is graded **peeked** and must
sync as `walkthrough` — never as a clean pass. The same rule binds the chat side: `/recall`'s plan
and sync report must never quote an item's answer. A warm retrieval recorded as cold corrupts every
row it touches and every mastery claim built on those rows. If it happens once, the trial FAILS
regardless of every other box.

## What the trials are really testing

Shared by both:

| Property | How it's caught |
| :--- | :--- |
| **v2 file contract** | Explicit `test ! -f framework.md / playbook.md / syllabus.html / drills-*.md` sweeps |
| **Depth is real, not cosmetic** | Ask it to name concrete quick/standard/deep differences. Adjectives only → FAIL |
| **Do-first** | The opening task must run or read something real *before* the first explanation |
| **Tutor, not answer machine** | You demand the answer outright; it must decompose and hint |
| **Cold retrieval** | `recall.html` shows the prompt alone; peeked-first syncs as `walkthrough`, never `none` |
| **Checkpoint bookkeeping** | `done L<n>` + manifest updates notes.md/retrieval.md/syllabus.md without re-teaching |
| **Lapse → re-tutor** | You fail the same item twice on purpose; `/learn` must fold it into the next lesson's warm-up |
| **Tier gate** | You ask it to close a tier whose criteria aren't met. It must refuse and name the gap |
| **Independence** | The sealed battery, worked alone with nothing open |

Reached only by `swe-basics`:

| Property | How it's caught |
| :--- | :--- |
| **Unbounded-field triage** | ≥3 argued SKIPs required. Mainlines that are one famous book's table of contents → FAIL |
| **Sources, not parametric memory** | Every lesson claim must cite a linked source; every survey source must be named and locatable |
| **Disagreement kept, not flattened** | "Is inheritance bad?" must name the condition and who argues each side, never a slogan |
| **Diagnosis before catalog** | No lesson may open by enumerating patterns; every pattern arrives with its problem *and* its cost |
| **`/synthesis-research` entry gate** | A tension-free question (`what does the S in SOLID mean`) must be refused and routed |
| **Steelman + crux** | Both positions stated as their authors would; the crux located as assumption / evidence / values |
| **HITL judgment** | **My Judgment** must be drawn out of you in dialogue, never ghost-written |
| **Real-code safety** | Work happens in a throwaway worktree; the live checkout must be byte-identical afterward |

## Notes

- **Each trial has a safety boundary, and neither is advisory.** herdr manages your live terminal:
  never touch a pre-existing pane, always `--no-focus`, always use IDs captured from returned JSON.
  `swe-basics` edits code you own: all work happens in a throwaway `git worktree`, no commits
  anywhere, the live checkout never written to. Read the boundary before Day 0.
- **Fresh session per tutoring day.** The file contract is the interface between steps, which is
  itself part of what's under test. Nothing needs to be carried in an agent's head.
- **`learning/herdr-v1/` is the archived earlier course** — v1 file layout, 3 lessons, 6 ledger
  rows. Reference only. Do not read it before Day 3, and do not feed it to `/survey`; comparing v1
  against v2 output afterward is one of the trial's two payoffs.
- **Contract fixtures.** Static compliant/non-compliant pairs used to live under `test-cases/`.
  They're gone: every contract they encoded is now stated in its skill's `## Contract test` block
  and exercised live by this runbook.
