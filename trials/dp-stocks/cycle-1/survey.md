# Survey: DP — the stock family (cycle 1 stub)

Last updated: 2026-09-01

> **This is a stub, not a survey.** It exists because `/curriculum`'s contract requires every lesson
> to name a matrix cell, and `/survey` is deliberately cut from the DP trial's chain — surveying a
> field the learner already knows would produce a fabricated gap diagnosis. It covers **one**
> mainline and is scoped to cycle 1's slice. See the [learning execution plan](../../../docs/exec-plans/learning.md).
>
> **Deliberate deviations from the `/survey` contract**, so nobody reads this as a compliant
> artifact: one mainline instead of 3–5, and therefore **no cross-mainline links** — the contract's
> ≥3 labeled links have nothing to connect. Both are stub properties. Do not use this file as a
> `test-cases/` fixture.

## Learner

Knows programming and basic 1D DP — climbing stairs, coin change. **No experience with
state-machine DP, 2D DP, or tree DP.** The two named problems are assumed prior knowledge, not
taught content.

## Mainline

| Mainline | The question it answers | What folds into it |
| :--- | :--- | :--- |
| **State-machine DP** | When the answer depends on which *mode* I am in, how do I carry one value per mode and move between them? | the two-state hold/free machine (122); the transaction cap as an extra dimension (121, 123, 188); later — cooldown (309) and fee (714) as further modifiers |

The slice is chosen because six problems that grinding turns into six memorized solutions are in
fact **one state machine plus four modifiers**. That makes the cycle a direct test of whether
`/curriculum` finds the unifying chunk (diagnosis gap 5), with an objective oracle on every item and
interleaving that has real work to do — 123 and 188 cannot be solved without retrieving 122's
transition.

## Matrix

| | can-recall (articulate) | can-apply (samples) | can-transfer (adapt) | can-generate (synthesize) |
| :-- | :-- | :-- | :-- | :-- |
| **State-machine DP** | State the two modes (hold / free) and both transitions without reference to any problem; say what the cap adds. | Solve 122 and 121 from the machine, not from memory; extend to 123 (k=2) and 188 (general k). | Given an unseen variant, name the modes and write the transitions before coding. | **◀** Write up 121/122/123/188 as one state machine plus one modifier, and defend it publicly. |

Target is **can-generate** because the W milestone — the public writeup — is the cycle's real
output. Cycle 1's lessons carry the learner to `can-apply`; the writeup reaches for the target cell
and is a loop-entry spec, executed after the cycle by `/practice` and closed by `/evaluate`.

## Triage

| Mainline | Investment | Target | Why this deep and no deeper |
| :--- | :--- | :--- | :--- |
| State-machine DP | 100% | can-generate | one mainline is the whole cycle-1 slice; depth here is what tests the unifying-chunk claim |

**Stop-early / SKIP:**

- SKIP — cooldown (309) and transaction fee (714): further modifiers on the same machine. Cycle 2's
  slice. Teaching them now would test breadth, not whether one chunk generalizes.
- SKIP — 2D string DP (edit distance), grid paths, tree DP: different mainlines entirely.
  Cycles 2 and 3.
- Stop at can-recall — the O(1)-space rolling-variable rewrite: a coding habit, not a schema.
  Mentioned, never drilled.

## Sources

### Read
- The four problem statements themselves (LC 121, 122, 123, 188) — the primary source. The machine
  is derived in the lessons, not read off an editorial.

### Don't read
- Per-problem editorials — the exact failure mode this trial exists to test against. Reading them
  supplies the memorized solutions instead of the shared chunk.

## Gap Diagnosis

| Mainline | Current | Target | Evidence |
| :--- | :--- | :--- | :--- |
| State-machine DP | can-recall | can-generate | Solves 1D DP where the state is a single index (climbing stairs, coin change); has never carried more than one value per index, and cannot state the hold/free transitions. |
