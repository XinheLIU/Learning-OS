# Cycle 1 — DP stock family

Last updated: 2026-09-01

Trial: `dp-stocks` · Cycle 1 of at most 3 · Phase under test: **Phase 1** (the return path)

Protocol: [`docs/exec-plans/learning.md`](../../../docs/exec-plans/learning.md). Vocabulary:
[`CONTEXT.md`](../../../CONTEXT.md). Fill this file **during** the cycle, not after — a rating
reconstructed from memory is a Layer 3 answer wearing a Layer 1 costume.

## Slice

| | type | content | problems | Interleaves |
|---|---|---|---|---|
| L1 | `[K]` | two-state machine (hold / free), taught on 122 where it is clearest | 122 | — |
| L2 | `[K]` | transaction cap adds a dimension | 121 (k=1), 123 (k=2), 188 (k) | — |
| L3 | `[S]` | interleaved retrieval, no new chunk | mixed | `two-state-machine` (L1, non-adjacent) |
| W | spec | writeup unifying 121/122/123/188 as one state machine → LeetCode Discuss or r/leetcode | — | — |

The W milestone is a **loop-entry spec only**. `/curriculum`'s contract requires the spec to exist,
not its execution, so it stays compliant at zero cost to the 3-hour budget. It is executed after the
cycle.

Expected ledger: **~5 items** — 2 `schema` rows (`two-state-machine`,
`k-transactions-adds-a-dimension`) plus ~3 `term` rows earned during the lessons. `retrieval.md`
carries `<!-- schedule: trial -->`.

## Day plan — 60 minutes of attention per day

**Day 0 — unattended, costs no budget.** `survey.md` stub written · `/curriculum` builds L1–L3 plus
the W spec · herdr sealed battery authored in a separate session.

| Day | Minutes | Sequence |
| :-- | :-- | :--- |
| 1 | 60 | `/learn` L1 (20) + L2 (20) → `/practice` one drill on 188 (20) |
| 2 | 60 | `/recall` (15) → `/learn` L3 (20) → `/practice` hard-first case (25) |
| 3 | 60 | `/recall` (15) → **lapse stress test** (30) → `/reflect` (15) |

**Hard-first fires on Day 2's practice case only** — not Day 1. `curriculum/SKILL.md` is explicit
that for K-lessons "difficulty is the enemy", so desirable difficulty belongs at S and after.

**Day 3 is a lapse stress test, not a sealed battery.** Deliberately fail one item on Day 2, then
verify the scheduler on Day 3. Pure Layer 1, and completely immune to the learner already knowing
DP — which is why it replaces a sealed battery in this trial.

## Layer 1 — mechanical (gating)

Agent-checked from files and transcripts. Every line resolves to a file state or a transcript fact.
Mark `PASS` / `FAIL` + the evidence pointer. **Any FAIL fails the cycle.**

### Ledger construction

| # | Assertion | Result | Evidence |
| :-- | :--- | :-- | :--- |
| 1 | Every `retrieval.md` row's `earned` date matches a successful demonstration in the transcript at assistance `none`/`hint` — no row was created at exposure | | |
| 2 | No row exists for a case, a drill, a problem, or a lesson; `kind` is `schema` or `term` on every row | | |
| 3 | Every row created by L1/L2/L3 has `streak` 0, `lapses` 0, `state: active`, and `interval-days` at the first rung on creation | | |
| 4 | The ledger header carries `<!-- schedule: trial -->` | | |

### `/recall` behavior

| # | Assertion | Result | Evidence |
| :-- | :--- | :-- | :--- |
| 5 | **No `/recall` prompt message contains its own answer**, a hint, or a leading restatement — the turn ends at the prompt | | |
| 6 | Every firing recorded exactly one correctness bit and one enum assistance value; no second scale, no numeric score | | |
| 7 | Only rows with `next-due <= today` and `state != re-tutor` were fired | | |
| 8 | `notes.md` and `framework.md` are unmodified by every `/recall` session | | |

### Scheduling arithmetic

| # | Assertion | Result | Evidence |
| :-- | :--- | :-- | :--- |
| 9 | Every pass at `none` advanced exactly one rung and incremented `streak` | | |
| 10 | **A pass at `hint` held its rung and did not advance** — and `streak` reset to 0 | | |
| 11 | Every lapse reset `interval-days` to the first rung, incremented `lapses`, zeroed `streak` | | |
| 12 | First lapse set `state: lapsed`; the **second consecutive** lapse set `state: re-tutor` | | |
| 13 | The `re-tutor` row was excluded from the next `/recall` selection | | |
| 14 | `/learn` re-tutored the flagged item and reset it to the first rung, `state: active`, `lapses` preserved | | |

### Pruning and interleaving

| # | Assertion | Result | Evidence |
| :-- | :--- | :-- | :--- |
| 15 | No Attempt Log line was pruned for a task whose ledger item has `streak < 2` — checked lesson boxes triggered no pruning | | |
| 16 | L3 (`[S]`) carries an `Interleaves:` field naming `two-state-machine` from **L1 — non-adjacent** | | |
| 17 | No `[S]` lesson in the syllabus has an absent, empty, or adjacent-only `Interleaves:` field | | |

**Layer 1 verdict:** ☐ green (all 17 PASS) ☐ red — first failure: ____

## Layer 2 — behavioral (⚠️ contaminated, non-gating for this trial)

The learner is simulating a beginner and already knows DP. A pass here is a smoke test, not
evidence. Record it; do not cite it. Genuine Layer 2 evidence comes only from the herdr trial.

| Item | Day 2 cold recall | Day 3 cold recall |
| :--- | :-- | :-- |
| `two-state-machine` | | |
| `k-transactions-adds-a-dimension` | | |

## Layer 3 — experiential (never gating)

Recorded **per skill invocation**. The two questions are fixed and identical every cycle so answers
compare across cycles. Open text — do not score, do not summarize, do not argue with the answer.

### `/curriculum` (Day 0)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/learn` L1 + L2 (Day 1)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/practice` drill on 188 (Day 1)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/recall` (Day 2)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/learn` L3 (Day 2)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/practice` hard-first case (Day 2)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/recall` (Day 3)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

### `/reflect` (Day 3)
1. *What did this make you do that grinding editorials wouldn't have?*
2. *Where did it waste your attention?*

## Verdict

**PASS** = Layer 1 fully green. (The sealed-item requirement applies to the herdr trial, not this
one; Layer 2 here is contaminated and non-gating.)

- **Result:** ☐ PASS ☐ FAIL
- **Attention actually spent:** Day 1 ___ · Day 2 ___ · Day 3 ___
- **Next cycle's target, set by Layer 3 only:**

PASS is mechanical — nobody declares it. The agent computes Layer 1 and has no discretion; the
learner owns Layer 3 and the agent may not argue with it.
