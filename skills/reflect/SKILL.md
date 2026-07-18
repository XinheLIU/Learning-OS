---
name: reflect
description: Close the learning loop - decide what should change next. Use after several practice sessions, when models feel off, at the end of a project, or when the user says "/reflect <topic>". Compresses recurring errors into next micro-goals, checks drift against the survey mainline, and gates playbook synthesis behind an adversarial defense.
---

# Reflect — Continuous Feedback

The loop-closer: **what should change next.** Reflect consumes `/evaluate`'s snapshot rather than duplicating it — evaluate measures state; reflect changes trajectory (model edits, next micro-goals, playbook). It keeps the knowledge base alive rather than a frozen snapshot.

## Rules

- **Short session, sharp questions.** 10–15 minutes, not an hour.
- **Don't rewrite everything.** Touch only what's wrong, stale, or missing; minimal model edits.
- **Archive, don't delete.** Dead records get marked `(archived: <reason>)` in `notes.md` — the history of wrong models is valuable.
- **Never write mastery levels.** That's `/evaluate`'s job; recommend running it first if the snapshot is stale or missing.
- **Don't reflect on 0 cases.** It's navel-gazing.

## Flow

### 1. Gather state

Read `learning/<slug>/`: `notes.md` (records + terms, including the latest Mastery Snapshot — if absent or stale, recommend `/evaluate <slug>` first), all `case-*.md`, and `survey.md`.

### 2. Three questions

**a) "Since last session, what's the most surprising thing you learned?"** — surprise means a model was wrong or incomplete; probe it. Nothing surprising → "What was harder than expected?"

**b) "Which model feels weakest right now?"** — weak = never used in practice, can't be applied confidently, or vague boundary conditions. Cross-check against the mastery snapshot.

**c) "What kind of problem are you avoiding?"** — surfaces practice gaps.

### 3. Error compression

Scan all `case-*.md` **Errors made** fields. Surface patterns: "a variant of this error appears in 3 of 5 cases." Recurring errors become the **next `/practice` micro-goals** — state them explicitly ("next session's micro-goal: <X>, targeting the <error> pattern"). This closes the deliberate-practice loop.

### 4. Mainline drift check

Compare time actually spent (which subtopics the cases and models cluster on) against `survey.md`'s learning mainline. Flag drift: "your mainline says DEEP on X but all 5 cases are on skim-tier Y — recalibrate the mainline or the habit?" Either answer is fine; unexamined drift is not. Mainline edits go through `/survey`, not here.

### 5. Update models

For any record that needs adjustment: ask what changed (sharper boundary? new example? doesn't hold?), edit it minimally in `notes.md`, append `(revised <date> — <what changed>)`. Dead records → archive (see Rules).

### 6. Playbook — behind the defense gate

At **5+ cases**, offer playbook synthesis. But first, the **adversarial defense gate (ICAP-I)**:

- Steelman 2–3 objections to the user's key positions — the strongest version an informed critic would make, not strawmen.
- The user defends or revises. A position enters the playbook **only** if it survives or is revised — this keeps positions defensible from both sides and guards against self-congratulation.
- You MUST refuse to write the playbook for positions that were neither defended nor revised.

Then write/update `learning/<slug>/playbook.md`: the user's repeatable method and defended positions, each noting the objection it survived.

### 7. Close

Set next micro-goals (from step 3).

## Contract test

Recurring error surfaced across ≥2 cases; drift vs mainline reported; playbook refused until positions survive the steelman.

## Boundaries

- vs `/evaluate`: evaluate measures (mastery snapshot); reflect changes trajectory. Reflect never writes mastery levels.
- vs `/practice`: practice records per-case errors; reflect compresses across cases and hands micro-goals back.
- vs `/survey`: reflect flags mainline drift but the mainline itself is `/survey`'s to change.
