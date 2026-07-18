# Learning OS Gap Analysis

Last updated: 2026-07-18

## Purpose

This document compares the current skill contracts under [`skills/`](skills/) with the target architecture in [README.md](README.md). It separates implemented strengths from missing learning-loop behavior so roadmap decisions are based on capability, not feature count.

The assessment is a static audit of `SKILL.md` files and their references. It evaluates specified behavior, not the quality of unseen live sessions.

Status labels:

- **Strong:** the behavior is explicit, operational, and covered by a contract test.
- **Partial:** the intent exists, but a required transition, artifact, or test is missing.
- **Missing:** the target behavior is not required by the current contract.

## Executive Finding

The current Learning OS is strongest at **mapping, scaffolding, retrieval, real-case practice, evidence storage, and reflective error compression**. Its main weakness is the center of the learning loop:

```text
current: explain -> construct -> feedback -> record
target:  predict -> attempt -> feedback -> retry -> compress -> fade support
```

The system often gives good feedback, but does not require the learner to apply that feedback in an immediate retry. It records evidence, but does not record assistance level, so assisted success and independent capability are hard to distinguish. It supports teach-back and compression, but neither is a consistently required learner-owned output.

No new top-level skill is needed. The shortest path is to tighten the contracts of `/survey`, `/curriculum`, `/learn`, `/practice`, `/evaluate`, and `/reflect` around one shared attempt schema.

## Target Capability Matrix

| Target capability | Status | Current evidence | Gap |
| :--- | :--- | :--- | :--- |
| Learn toward an output | Partial | `/curriculum` requires a mission and at least one real-world W milestone. | Mission can remain motivational; it does not require a concrete target artifact, quality bar, transfer test, and independence test. |
| Map before depth | Partial | `/survey` produces a domain map, DEEP/SKIM/SKIP mainline, sources, and diagnosis. | `/curriculum` may bypass `/survey` without producing an equivalent lightweight dependency map or 80/20 cut. |
| AI-guided, learner-owned thought | Strong | `/learn`, `/practice`, and `/research` forbid handing over schemas, models, or judgment. | Enforcement depends on prose; adversarial evaluations remain thin. |
| Prediction before explanation | Missing | ICAP theory mentions learner predictions; `/research` asks what the learner's model predicts. | `/learn` and lesson contracts do not require a prediction or attempt before explanation. |
| Practice before complete understanding | Partial | S lessons use retrieval and application; W milestones reach real work. | Strict K-before-S-before-W sequencing can become a waterfall, delaying use until the knowledge block feels complete. |
| Every input becomes a learner output | Partial | Lessons end with learner construction; research always produces a report. | Source ingestion and K lessons can end in AI-produced notes/reference material without a required learner artifact tied to each input. |
| Real problems over artificial exercises | Strong | `/practice` requires real cases; `/curriculum` ends with real-world W work. | Real cases are concentrated late; early lessons may rely on quizzes rather than slices of the target output. |
| Feedback changes the next attempt | Partial | `/learn` and `/practice` require immediate, precise feedback. `/reflect` turns recurring errors into micro-goals. | Neither skill requires an immediate retry, and case files have no feedback-to-retry trace. |
| Mistakes become curriculum | Strong | Case errors are mandatory; `/reflect` clusters recurring errors into the next micro-goals. | The loop usually waits for multiple cases and a separate command, so correction can be delayed. |
| Debugging over memorization | Partial | `/practice` treats “no model fits” and cracked models as valuable signals. | There is no explicit reproduce-localize-hypothesize-test-revise debugging protocol or evidence level. |
| Compression creates knowledge | Partial | `reference/`, canonical terms, learning records, and `playbook.md` compress knowledge. | `/curriculum` prebuilds reference documents before the learner earns them; learner-authored compression is not required after every loop. |
| Retrieval over rereading | Strong | `/learn` warm-ups retrieve prior lessons; S lessons require retrieval, spacing, and interleaving. | Contract tests cover presence more than retrieval quality or delayed retention. |
| Teach-back exposes gaps | Partial | Each `/learn` segment ends with construction; `can-teach` requires an explanation that survives challenge. | The explicit explain-simplify-challenge-reteach cycle is optional, and successful teach-back evidence has no standard artifact. |
| Reduce guidance over time | Partial | Diagnosis changes scaffolding; later curriculum stages specify reduced or no support; practice announces difficulty changes. | No assistance ledger, hint budget, monotonic fading rule, or next-support-to-remove field exists. |
| Store reusable systems | Strong | Records, terms, drills, references, research reports, and defended playbooks have clear homes. | The path from isolated records to a reusable system appears only after five cases and a manual `/reflect`. |
| Measure independent capability | Missing | `/evaluate` uses evidence-backed levels from recall through generation. | Evidence does not record how much AI help was used; there is no unaided graduation level or target-output quality gate. |
| Human judgment directs AI speed | Strong | Mission confirmation, syllabus approval, learner-owned research judgment, and soft wiki handoffs preserve human decisions. | Output and independence criteria should also require learner confirmation. |
| Short ignorance-to-correction loop | Partial | Feedback is immediate inside `/learn` and `/practice`. | Retry and result are absent; cross-case adaptation waits for `/reflect`. |
| Need less AI over time | Missing | Expertise reversal and low-support advanced stages point in this direction. | The system cannot show assistance trending downward or declare AI-independent graduation. |

## Skill-by-Skill Assessment

### `/survey` — strong map, incomplete output contract

**Strong now**

- Produces an argued DEEP/SKIM/SKIP mainline with at least one explicit skip.
- Diagnoses prior knowledge with evidence.
- Separates field triage from course sequencing and research.
- Curates sources by purpose and rejects low-value sources.

**Gaps**

- Begins with the field, not a required target output and quality bar.
- Does not explicitly separate prerequisite, core, and advanced knowledge in the map.
- Does not cap the final resource set at three to five.
- The 80/20 claim is implicit in investment percentages, not tested as “which concepts unlock most common work?”
- The baseline diagnosis tests topic knowledge, not an attempt at the target output.

**Target contract change**

Require `survey.md` to contain `Target Output`, `Quality Bar`, `Transfer Test`, `Independence Test`, a prerequisite graph, an argued 80/20 core, and three to five ranked resources.

### `/curriculum` — strong sequencing, too course-first

**Strong now**

- Mission-first design and user approval prevent blind course generation.
- Prerequisite sequencing, one-chunk lessons, ICAP targets, and load notes are explicit.
- Retrieval, spacing, interleaving, real tasks, and transfer already appear in the K/S/W design.
- Stage 4 and 5 deliberately reduce support.

**Gaps**

- The whole HTML course is built upfront, which optimizes content production before learner evidence exists.
- K-before-S-before-W can delay attempts instead of alternating minimal knowledge with immediate use.
- Stages lack explicit target outputs and acceptance checks.
- There is no default weekly view with input, practice, and output for each checkpoint.
- Lesson specs do not require prediction, retry, compression, or assistance-fading fields.
- `/curriculum` can bypass `/survey` without recreating its essential map-first outputs.

**Target contract change**

Plan the full path but build only the next evidence-gated unit. Each unit should specify `Input`, `Prediction`, `Attempt`, `Feedback`, `Retry`, `Output`, and `Support Budget`. Weeks remain scheduling labels; evidence unlocks progression.

### `/learn` — strong tutoring, incomplete correction loop

**Strong now**

- Prevents AI from replacing learner construction.
- Recalibrates lessons against earned knowledge and misconceptions.
- Uses spaced retrieval, one-chunk pacing, immediate precise feedback, and ICAP escalation.
- Stores only insights that change future teaching.
- Requires learner-owned language before filing earned knowledge.

**Gaps**

- The session loop starts with a warm-up and then tutoring, not a required prediction or first attempt.
- Feedback can end a segment without the learner correcting the same task or a near-transfer variant.
- The Feynman loop is present only as general construction; it lacks the explicit simple-explanation, teach-back, severity-ranked critique, and reteach protocol.
- Reference documents may be extended by AI without a learner-produced compression check.
- There is no recorded assistance level or planned support reduction.

**Target contract change**

Replace the session core with:

```text
retrieve -> predict/attempt -> minimal explanation -> teach back ->
severity-ranked feedback -> retry -> learner compression -> record assistance
```

A segment closes only after the retry resolves or precisely narrows the error.

### `/practice` — strongest real-work component, missing retry evidence

**Strong now**

- Requires real cases and one observable micro-goal.
- Decomposes skills into failure modes, success criteria, and difficulty curves.
- Asks the learner to select a model before the AI prescribes one.
- Makes calibration visible and records errors for later compression.

**Gaps**

- “Immediate feedback” means correction, but not necessarily another learner attempt.
- The case schema stores one summary, not the sequence of attempts and changes.
- Artificial drills are banned even when a tiny synthetic case would efficiently isolate a failed micro-skill; the target design allows that narrow exception.
- Debugging is not a named protocol.
- Assistance used is not recorded.

**Target contract change**

Extend every case with:

```markdown
**Attempt 1:**
**Observed failure:**
**Hypothesis:**
**Feedback:**
**Retry:**
**Result:**
**Assistance used:**
**Next support to remove:**
```

### `/evaluate` — evidence-backed, not independence-backed

**Strong now**

- Rejects numeric scores and self-reported competence.
- Requires artifact pointers for every mastery claim.
- Separates measurement from trajectory changes.
- Covers recall, application, transfer, teaching, and generation.

**Gaps**

- `can-recall` can be established in a live AI-guided probe without assistance metadata.
- A successful case may be heavily coached but still support `can-apply`.
- `can-teach` does not require responding to another person's misconception.
- Debugging is absent from the rubric.
- There is no explicit independent target-output graduation level.

**Target contract change**

Add assistance metadata to every evidence pointer and add `can-debug` plus `independent`. The latter requires an unfamiliar case, no hints during execution, an explicit quality bar, decision explanation, and self-correction.

### `/reflect` — strong delayed adaptation, weak scaffold fading

**Strong now**

- Compresses recurring errors into concrete next micro-goals.
- Checks drift against the learning mainline.
- Revises models minimally and preserves the history of wrong models.
- Requires adversarial defense before playbook synthesis.

**Gaps**

- It changes future goals but does not verify that prior feedback changed an actual retry.
- It has no view of assistance trends because cases do not store them.
- It does not choose the next scaffold to remove.
- Waiting for multiple cases is appropriate for pattern detection but too slow for single-attempt correction.

**Target contract change**

Keep cross-case reflection here, but add `Assistance Trend`, `Next Support to Remove`, and a check for unresolved feedback with no successful retry. Immediate retry remains owned by `/learn` and `/practice`.

### `/research` — strong judgment ownership, indirect learning loop

**Strong now**

- Requires a real tension, source combinations, a located crux, learner-owned judgment, action, and falsifier.
- Explicitly asks what the learner's model predicts.
- Produces a durable written output and feeds contradictions back to reflection.

**Gaps**

- The learner's prediction is a standing question, not a required pre-research baseline.
- The report can be completed without comparing the final judgment to the initial prediction.
- Assistance used in forming the judgment is not visible.

**Target contract change**

Add `Initial Prediction`, `What Changed My Mind`, and `Independent Judgment` fields. Preserve the rule that AI cannot ghost-write the learner's position.

### `llm-wiki-*` — strong external memory, not learner evidence

**Strong now**

- Preserves source fidelity, provenance, contradictions, indexes, and reusable external knowledge.
- Maintains a strict boundary between source knowledge and earned learner knowledge.
- The ingest discussion adds a human gate before filing takeaways.

**Gaps**

- Ingestion produces system outputs, not necessarily learner outputs.
- A well-populated wiki can increase familiarity and retrieval convenience without increasing independent capability.
- The README previously described a 12-point linter, while the current linter contract contains 16 checks; documentation had drifted.

**Target contract change**

Do not add learning behavior to the wiki suite. Keep the boundary explicit: wiki content may prompt predictions and attempts, but never counts as learner evidence by itself.

## Recommended Implementation Order

### P0 — close the attempt-feedback-retry loop

1. Update `/learn` so prediction or attempt precedes explanation and every correction is followed by a retry.
2. Update `/practice` case files to store attempt, failure, hypothesis, feedback, retry, result, and assistance.
3. Update `/evaluate` so coached evidence cannot be mistaken for independent capability.

**Why first:** this shortens the ignorance-to-correction loop without adding a new component or changing the file-based architecture.

### P1 — design backward from outputs and fade support

1. Add target output, quality bar, transfer test, and independence test to `/survey` and `/curriculum`.
2. Add prerequisite/core/advanced mapping, an explicit 80/20 core, and a three-to-five-resource cap to `/survey`.
3. Make curriculum units locally alternate knowledge and use; add weekly input/practice/output checkpoints.
4. Add support budgets and an explicit next-scaffold-to-remove decision to `/curriculum`, `/learn`, and `/reflect`.

### P2 — make compression and teaching observable

1. Add the full AI Feynman cycle to `/learn`.
2. Require learner-owned compression after successful retries.
3. Add debugging and independent performance to the evidence rubric.
4. Update contract tests and eval fixtures for prediction, retry, compression, assistance, and unaided transfer.

### P3 — reduce documentation and evaluation drift

1. Add contract fixtures for every Learning OS skill, not only curriculum.
2. Test cross-skill handoffs using fixture files.
3. Keep README architecture claims linked to executable or inspectable contract checks.
4. Retain the existing wiki roadmap separately: triage-first ingest, walk-up path discovery, and optional local hybrid search are useful infrastructure work, but do not close the learner loop.

## Acceptance Criteria for the Target Design

The gap is closed when a fixture learning journey can prove all of the following:

- The plan begins with a target output and an explicit map of prerequisites, core knowledge, and skips.
- The learner predicts or attempts before receiving the relevant explanation.
- Every substantive input produces a learner-generated output.
- Every correction is followed by a retry whose result is recorded.
- At least one real case appears before the learner completes all conceptual coverage.
- Errors from cases change the next micro-goal.
- The learner compresses a corrected idea in their own words and later retrieves it from memory.
- A teach-back exposes a gap, the learner repairs it, and the second explanation survives challenge.
- Assistance is recorded and decreases across comparable attempts.
- Final graduation uses a new real case, a visible quality bar, and no AI guidance during execution.

Until those checks pass, the project should describe itself as a strong AI tutoring and learning-memory system moving toward an independence-oriented Learning OS.
