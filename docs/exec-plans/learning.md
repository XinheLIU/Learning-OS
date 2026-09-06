# Learning System Execution Plan

Last updated: 2026-09-06

## 0. Intent, orientation, and operational memory

The next implementation slice unifies `docs/learning-system-improvements.md` and
`docs/learning-memory-practice-plan.md`:

- `/survey` must interview for an observable outcome, evidence-backed baseline, relevance, gap,
  constraints, non-goals, and uncertainty, then write a Mission Contract and Roadmap with 3–5
  `Before → After` checkpoints.
- `/curriculum` must preserve that contract in `syllabus.md`, add checkpoint identifiers and a bounded
  Memory Budget for mission-critical operational items, and orient the first lesson before teaching.
- `/learn` must name the active checkpoint and capability delta, connect opening tasks and retries to it,
  rehearse operational items through the existing retrieval ledger, and offer an opt-in staged memory
  palace. Palace cues never count as mastery evidence.
- `notes.md`, `retrieval.md`, `/practice`, `/recall`, and the README must use the same operational-item
  fields and handoffs.

Acceptance is covered by expanded contract/evaluation fixtures for vague intent, unsupported levels,
scope cuts, roadmap preservation, first-lesson orientation, cold operational recall, spacing/lapses,
execution fluency, memory-palace opt-in/opt-out, and mission-change routing. No standalone validator or
runtime dependency is planned.

Only unfinished work is listed here. The current learning architecture lives in
[`skills/learning/README.md`](../../skills/learning/README.md); durable rationale lives in
[`docs/adr.md`](../adr.md).

> **2026-09-06 — v3 landed (HTML-first).** The interaction redesign is done: checkpoint blocks +
> completion manifests in lessons, `recall.html` as the firing surface, `/learn` in
> start/done/tutor modes, `/recall` as planner + sync, `/curriculum` as orchestrator + builder,
> and `learning/herdr` migrated as the exemplar. **The dogfood gate below is now owed against the
> v3 flow** — the runbooks have been updated to assert it, but no cycle has run yet.

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

Two trials, executed by the learner step by step. See
[`trials/README.md`](../../trials/README.md) for the shared protocol.

- [`trials/herdr/RUNBOOK.md`](../../trials/herdr/RUNBOOK.md) — herdr at `--depth=standard`, 60
  minutes per day across three days. A **bounded** topic whose ground truth is the installed CLI,
  so assertions can name exact answers.
- [`trials/swe-basics/RUNBOOK.md`](../../trials/swe-basics/RUNBOOK.md) — writing good code and
  design patterns at `--depth=quick`, two 30-minute sessions per day across three days. An
  **unbounded** topic with contradictory literature and no ground truth, run against the learner's
  own repository in a throwaway worktree.

The pair is chosen to fail differently. herdr cannot catch a chain that lectures fluently from
parametric memory, because its CLI settles every question; `swe-basics` gates on citation, argued
SKIPs, and refusal to flatten a live disagreement. Running both at opposite ends of `--depth`
(`standard` and `quick`) is also the only way to establish that the parameter does anything.

Layer 2 gates on both trials. The earlier partial course is archived at `learning/herdr-v1/` and is
not read during the run, so the Day 3 sealed-battery score is genuine evidence rather than recall of
a previous pass. The battery is authored on Day 0 in its own session, before any lesson exists, and
stays sealed at `~/.learning-os-sealed/herdr-battery.md` until measurement. The `swe-basics`
battery is sealed the same way at `~/.learning-os-sealed/swe-basics-battery.md`, but is graded
against rubrics rather than an answer key — its runbook carries three literal grading questions,
because a rubric is easy to pass generously.

Comparing `learning/herdr-v1/` (v1 chain) against `learning/herdr/` (v2 chain) afterward — same
topic, same budget — is the trial's second payoff: whether opening tasks, Stage 2–3 mini-cases, and
the consolidated `notes.md` produced better retention, or only a differently-shaped set of files.

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

- Keep every skill's `## Contract test` block current with its `SKILL.md`, and reachable from a
  runbook assertion. The static `test-cases/` fixture tree was removed on 2026-09-02: the contracts
  it encoded are now stated in each skill and exercised live by the two trials.
- `/synthesis-research` is now covered by the `swe-basics` runbook (Session 5): entry gate,
  steelman, located crux, ≥2-source insights, HITL judgment, and a negative check that a
  tension-free question is refused and routed.
- Still uncovered: the pipeline and writing skills. Extend a runbook or add a third trial.
- Keep architecture claims linked to inspectable contract checks.
