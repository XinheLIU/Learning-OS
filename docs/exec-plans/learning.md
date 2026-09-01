# Learning System Execution Plan

Last updated: 2026-09-01

Only unfinished work is listed here. The current learning architecture lives in
[`skills/learning/README.md`](../../skills/learning/README.md); durable rationale lives in
[`docs/adr.md`](../adr.md).

## 1. Validate the return path

The retrieval ledger and `/recall` skill are implemented but have not completed their dogfood gate.

### Protocol

- A cycle lasts three days with at most 60 minutes of learner attention per day. Day 0 generation
  and ledger bookkeeping do not consume that budget.
- A trial runs at most three cycles. Ship only after Layer 1 is green in two consecutive cycles.
- Layer 1 is mechanical and gating: assertions resolve to files or transcript facts.
- Layer 2 is behavioral and gates only when the learner's ignorance is genuine.
- Layer 3 asks, after each skill invocation, “What did this make you do that grinding would not?”
  and “Where did it waste your attention?” It informs the next cycle and never gates PASS.
- Trial ledgers use 1/2-day intervals. They test scheduler mechanics and single-overnight retrieval,
  not production interval sizing.

### Trials

1. Run `trials/dp-stocks/cycle-1/`: build its lessons, then execute the three-day plan in
   `RATING.md`. Its behavioral evidence is contaminated because the learner knows dynamic
   programming, so Layer 2 is non-gating.
2. Design the herdr trial only after DP cycle 1 reports. Its pre-authored sealed battery lives
   outside the repository at `~/.learning-os-sealed/herdr-battery.md`; tutoring must run in a fresh
   session that has never inspected the battery or the CLI.

### Acceptance

Across two consecutive cycles:

- ledger rows open only after successful `none`/`hint` demonstrations;
- no `/recall` prompt contains its answer or an advance hint;
- interval, streak, lapse, and state transitions match the ledger contract;
- no Attempt Log row is pruned before the matching item reaches `streak >= 2`;
- every `[S]` lesson names a non-adjacent schema to interleave.

## 2. Design backward from independent output

- Add target output, quality bar, transfer test, and independence test to `/survey` and
  `/curriculum`.
- Add prerequisite/core/advanced mapping, an explicit 80/20 core, and a three-to-five-resource cap
  to `/survey`.
- Alternate knowledge and use locally instead of completing all conceptual coverage first.
- Add support budgets and a next-scaffold-to-remove decision to `/curriculum`, `/learn`, and
  `/reflect`; compute assistance trends across comparable attempts.
- Make `/evaluate` graduate a learner only on a new real case or target artifact completed without
  guidance.

Acceptance: a fixture journey starts from an explicit output and quality bar, uses a real case before
coverage is complete, shows assistance decreasing, and ends with unaided work against a visible bar.

## 3. Make sessions respect consolidation

- Add consolidation to `learning-theory.md`: focus/diffuse alternation, sleep-dependent
  consolidation, spacing, breaks, and exercise.
- Give `/learn` and `/practice` a 25-50 minute block with a hard maximum and a recorded break.
- Plant an unsolved hard problem before a break or session end; ask what surfaced at the next open.
- Record sleep before `/recall` or `/evaluate` attributes a bad session to a knowledge gap; have
  `/reflect` inspect clustering.

Acceptance: two consecutive dogfood cycles respect the session envelope, include one planted
problem and return, and record sleep before diagnosing a knowledge failure.

## 4. Make compression, teaching, and debugging observable

- Add an explicit explain-simplify-challenge-reteach cycle to `/learn`.
- Require learner-owned compression after a successful retry.
- Add a reproduce-localize-hypothesize-test-revise debugging protocol and evidence level.
- Add `Initial Prediction`, `What Changed My Mind`, and `Independent Judgment` to
  `/synthesis-research` without allowing AI to author the judgment.
- Fold the recorded user feedback into contracts: keep explanations on the mathematical mainline
  before introducing unexplained code, and support the sequence concept recall -> code -> variants
  and tricks -> later review.

Acceptance: a fixture preserves the original explanation, challenge, correction, second teach-back,
learner compression, and assistance level as inspectable evidence.

## 5. Introduce hard-first practice and chunk states

- Open `/practice` with the hardest available item, attempt for one or two minutes, then explicitly
  solve or park it while reactive load calibration remains in force.
- Within prerequisite constraints, order same-stage curriculum work hardest-first.
- Check for Einstellung after successful cases by asking whether another approach was better.
- Replace binary framework `target`/`earned` with `focused`/`understood`/`contextualized`, and allow a
  retrieval lapse to move a node backward.

Acceptance: two consecutive cycles record the hard-first decision in every practice session, every
framework node has a formation state, and at least one lapse moves a node backward.

## 6. Add encoding and minimal habit support

- Permit one deliberate metaphor per abstract concept and require its failure boundary.
- Add an encoding reference for learner-authored imagery, memory palaces, multisensory encoding, and
  handwriting plus recall. Mnemonic evidence alone remains capped at `can-recall`.
- Let `/recall` use the learner's cue and vary retrieval context.
- Have `/reflect` compare planned and actual sessions. Keep night-before planning and a short daily
  list as guidance, not a new productivity subsystem.

Acceptance: two consecutive cycles fire at least one learner-authored cue and report planned versus
actual sessions without inflating the item's mastery level.

## 7. Close contract coverage

- Add compliant and non-compliant fixtures for every learning skill.
- Test cross-skill handoffs with fixture files.
- Keep architecture claims linked to inspectable contract checks.
