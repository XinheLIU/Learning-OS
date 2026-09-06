# Learning System Improvements: Intent and Orientation

_Last updated: 2026-09-06_

## Analysis

The current learning system already has several useful pieces: `/survey` produces a mainline × mastery-stage matrix and a gap diagnosis; `/curriculum` requires a mission and uses the survey to set scope and depth; and `/learn` calibrates lessons against the learner's recorded state. The weak point is the handoff into that system. `/survey` can proceed with insufficiently specific intent, unsupported self-assessments, or an unclear reason for learning the topic. That makes the mission and gap analysis unreliable, which then affects the matrix, lesson sequence, and tutoring difficulty.

The second weakness is orientation. The system stores scope decisions and lesson plans, but the learner does not consistently receive a clear view of the whole roadmap, the deferred parts of the field, or the concrete change expected after a small group of lessons. Without that before → after view, individual lessons can feel disconnected from the mission even when the underlying files are aligned.

## Plan

### 1. Strengthen `/survey` intake

- Replace the minimal initial intake with a required interview covering:
  - the desired real-world change or output;
  - current experience, supported by examples of work, reading, or performance;
  - why the topic matters now;
  - the capability gap between the current state and desired outcome;
  - constraints and explicit non-goals.
- Add adaptive grilling when answers are vague, unsupported, inconsistent, or overly broad.
- Ask for a concrete output when the user says they want to “understand” a topic.
- Use small probes or explanation requests to validate the claimed starting level.
- Continue only when the goal is observable, relevance is concrete, current level has evidence, and the gap can guide the matrix. Record remaining uncertainty instead of silently guessing.
- Store the result as a durable Mission Contract in `survey.md`.

### 2. Add a visible roadmap

- Add a Roadmap section to `survey.md` showing the whole field at a useful level, the selected critical path, and topics that are deferred, skimmed, or skipped.
- Add 3–5 checkpoint outcomes tied to the mission.
- Phrase each checkpoint as an observable before → after change, for example: “Before: can name the concepts but cannot diagnose a failing case. After checkpoint 2: can reproduce the canonical sample and explain the failure signal.”
- Carry the roadmap and checkpoint outcomes into `syllabus.md` so the course plan remains aligned with survey decisions.

### 3. Orient the learner in the first course sessions

- Require the first lesson to explain the mission, baseline, target output, full roadmap, out-of-scope areas, and the next checkpoint before introducing new material.
- Give every lesson a checkpoint identifier and a capability delta describing how that lesson advances the learner.
- Have `/learn` name the active checkpoint and connect each opening task, construction, and retry to the expected before → after change.
- If evidence changes the baseline or mission, record it in `notes.md` and route structural changes back to `/curriculum`.

### 4. Update contracts and verification

- Update the contracts and templates for `/survey`, `/curriculum`, `/learn`, and the syllabus format.
- Add evaluation cases for vague intent, unsupported level claims, unclear relevance, explicit scope cuts, roadmap preservation, and first-lesson orientation.
- Update the learning README and execution plan with the new data flow and acceptance criteria.
- Keep the existing mastery ladder and file-based architecture; introduce no new runtime dependency or database.

## Acceptance Criteria

- A vague survey goal triggers follow-up questions until it becomes an observable outcome.
- A claimed experience level is supported by evidence or conservatively rounded down.
- Every completed survey records goal, current level evidence, relevance, gap, constraints, and non-goals.
- Survey and syllabus both show what is in scope, deferred, and skipped.
- The syllabus contains 3–5 checkpoint outcomes with before → after capability changes.
- The first course lesson presents the roadmap and next checkpoint before teaching new content.
- Subsequent lessons identify the checkpoint they serve and reconnect work to the mission.
- Existing survey, curriculum, and learning contract tests remain passing.

## Implementation Status

Implemented in the learning contracts and evaluation fixtures: Mission Contract intake, roadmap and
checkpoint orientation, syllabus Memory Budget fields, `/learn` capability deltas and optional
memory-palace coaching, operational retrieval rows, README/execution-plan handoffs, and new evaluation
cases. No runtime dependency or catalog metadata was added.
