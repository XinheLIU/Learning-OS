# Writing Redesign Verification

Last updated: 2026-10-02

## Analytical preparation redesign — 2026-10-02

Implemented on top of the existing staged folder reorganization without staging, committing or
adding dependencies. Existing teaching-track scaffolds were preserved.

| Check | Result |
| :--- | :--- |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/writing/scripts -p 'test_*.py' -v` | 31 passed (17 existing, 14 added) |
| Skill creator quick validator | all 9 revised entrypoints passed using an existing isolated interpreter with PyYAML |
| Catalog source paths versus canonical folders | all 38 resolve; exact membership; leaf skill names retained |
| Four project discovery layers | all 38 skill links resolve in each layer |
| Changed Markdown instruction links and near-top dates | passed |
| `git diff --check` | passed |

The new draft checks exercise budgets, selected evidence and section alignment, checkpoint basis
and state, unresolved central facts, exploratory questions, legacy compatibility and teaching kinds.
An invalid Unicode numeric budget initially exposed a conversion exception; its regression now
passes with a normal validation error. CLI checks leave the input bytes unchanged.

A retained implementation-agent walkthrough lives locally in
`tmp/analytical-preparation-x0rax0ff/`, with source fixtures, synthetic dialogue, staged briefs, a
draft, counterevidence and `checks.json`. It exercised:

- A source-restatement proposal was narrowed into a derived comparison rule after a concrete probe.
- Framework-only preparation passed argument validation and failed draft readiness; no prose existed.
- Four sources were considered: the decisive timing case developed, a corroborating passage cited
  briefly, a boundary case kept short, and pricing omitted. Source bytes remained unchanged.
- A 500-word section plan used targets 85 / 220 / 120 / 75. Pending material-plan agreement failed
  readiness; recorded synthetic delegation passed without another approval request.
- The draft used 81 / 210 / 113 / 70 section words plus a 19-word fixture note (493 total).
  Review found the planned depth, transitions, conditional reasoning and attribution intact.
- Later contrary evidence reopened the framework and dependent material plan; readiness failed,
  and the next action was a changed framework decision rather than local prose repair.

These artifacts were prepared and assessed by the implementing agent; this was not an independent
agent run. The author statements are fictional test inputs, not actual user approval. Originality,
source truth and live usefulness remain semantic judgments. A real author trial is tracked in the
writing execution plan.

## Earlier implementation — 2026-10-01

Implemented against the existing uncommitted workspace. No git commit or new dependency was added.
The public writing workflow now has 14 skills (three new), with 31 skills across the repository.

### Mechanical results

| Check | Result |
| :--- | :--- |
| `python3 -m unittest discover -s skills/writing/scripts -p 'test_*.py' -v` | 17 passed |
| Skill creator quick validator | all 11 changed skills passed; used an existing isolated interpreter with PyYAML |
| Catalog versus canonical skill folders | pipeline 11, learning 6, writing 14; exact membership |
| Four project discovery layers | 31 valid symlinks each |
| Changed documentation links and near-top dates | passed |
| `git diff --check` | passed |
| Legacy Learning How to Learn piece, missing brief-kind | inferred piece; readable without mutation |
| Legacy chapter fixture | read as chapter; no opponent requirement |
| New explanatory brief | v2 ship-stage structure passes; no opponent, personal anecdote or forced cut |
| Existing delivery fixtures | clean passes; broken correctly fails with 3 broken references and 6 portability violations |

The checker validates structure and references, not source truth, inference validity or reader gain.
The script and its regression suite use only the Python standard library. Legacy passes explicitly
report compatibility rather than claiming v2 validation or a ship verdict.

### Implementation-agent walkthrough

The temporary walkthrough artifacts were discarded on 2026-10-01 after implementation was
completed. The findings below remain as the verification record. The walkthrough exercised:

- A real-material explanation derived from a selected Learning How to Learn note passage, including
  source-quality limits and a clearly hypothetical example; no personal history was invented.
- Review of a broad quantitative inference in the existing brief, with reasoning/evidence routes.
- One targeted expression repair and re-review; surrounding draft bytes stayed unchanged.
- A synthetic author snapshot, duplicate/paraphrase no-change decisions, a changed judgment saved as
  the next version, and a grounded candidate connection to another topic.
- Recovery after removing the test's derived index: rebuilt from latest complete snapshots without
  a third snapshot. The original snapshot's byte hash stayed unchanged.
- Next-article framing read back the latest grounds and open question and proposed a distinct gain.
- Hash checks confirmed five original corpus files remained unchanged; six unaffected writing
  modules were also checked against the turn-start backup.

These are implementation-agent observations, not an independent agent evaluation. The invented
author statements are explicitly labelled test inputs and were never written to learner memory.
Retraction of a previously stored relation is specified in the runbook but was not exercised in this
walkthrough. A live author's judgment, a full second article and a cold chapter grill remain the
next usage validation, tracked in the writing execution plan.
