# Learning OS

A set of skills that take a learner from surveying a field to demonstrated mastery, and the
dogfood machinery that validates whether those skills actually work.

Last updated: 2026-09-01

## Language

### Validation

**Trial**:
One end-to-end validation of the skill chain against a chosen subject, run as repeated cycles
until it passes or is abandoned. Two exist: the DP trial and the herdr trial.
_Avoid_: test case, experiment, study

**Cycle**:
One three-day run of the chain inside a trial, ending in a PASS/FAIL verdict. A trial may run
up to three cycles.
_Avoid_: iteration, round, sprint

**Slice**:
The portion of a trial's total load that one cycle covers. A trial's load is split across cycles
so that a cycle failing on Layer 1 costs one slice of learning time, not all of it.
_Avoid_: batch, chunk (reserved), tranche

**Layer 1 / Layer 2 / Layer 3**:
The three evidence classes a cycle produces. Layer 1 is mechanical and agent-checkable
(did the chain run, did the files update correctly). Layer 2 is behavioral and learner-answered
but not self-flattering (cold recall pass/fail, accept/reject). Layer 3 is experiential
open-text self-report. Only Layers 1 and 2 gate a PASS.
_Avoid_: metric tier, evidence level

**Sealed battery**:
The assessment items chosen and written to a file before any teaching begins, in a session that
never sees the tutoring, and not opened until measurement day.
_Avoid_: holdout set, final exam

**Contract-verifiable** vs **outcome-verifiable**:
Contract-verifiable means a skill's artifacts obey the skill's own stated rules — what
`evals.json` checks. Outcome-verifiable means the learner demonstrably retained or transferred
more. The learning plan separates those checks and uses dogfood trials for the latter.
_Avoid_: testable, provable

### Retrieval

**Item**:
One unit tracked in `retrieval.md` and testable by a single cold recall prompt. Not every
artifact is an item — a case record is evidence, not an item.
_Avoid_: card, entry, fact

**Ledger**:
`learning/<slug>/retrieval.md` — the file that answers "what is due today". One per course.
`/learn` and `/practice` create rows in it; `/recall` alone fires and reschedules them.
_Avoid_: schedule, deck, queue

**Firing**:
One `/recall` test of one item on one day. Records exactly two things: a **correctness bit**
(was the cold attempt right, before any help) and an assistance level. The two are separate
axes — the bit governs whether the item lapsed, the assistance governs how far the interval
moves on a pass.
_Avoid_: review, rep, trial (reserved), attempt (reserved for `/learn`'s segment core)

**Rung**:
One step on an interval ladder — 1/3/7/16/35 then monthly in production, 1/2 in a trial. A pass
advances one rung, holds, or resets to the first; nothing ever jumps two.
_Avoid_: level, stage (reserved), step

**Modifier**:
A chunk that parameterizes a base schema rather than replacing it — it has its own trigger
condition and earns its own item, but is meaningless without the base. The stock family is one
base state machine plus four modifiers.
_Avoid_: variant, variation, special case

**Cold recall**:
Retrieval attempted with no material open and no hint offered before the attempt. The only
retrieval that advances an item's interval.
_Avoid_: quiz, review, test

**Lapse**:
A failed cold recall on an item that had previously succeeded. Resets the interval and
increments the lapse count.
_Avoid_: miss, failure, forget

**Assistance level**:
How much help a demonstration received — `none`, `hint`, `walkthrough`, `solution-shown`.
Caps what the evidence can claim; coached evidence supports at most `can-recall`.
_Avoid_: help level, scaffolding, support

### Skill-chain roles

**Case**:
A real problem a learner works during `/practice`, recorded as a case file. Reserved for this
meaning only.
_Avoid_: using "case" for a trial, a cycle, or a `test-cases/` fixture

**Fixture**:
A compliant or non-compliant artifact under `test-cases/`, used to check a skill's contract.
Never dogfood output.
_Avoid_: test case, example
