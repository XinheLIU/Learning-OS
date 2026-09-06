---
name: reflect
description: Close the learning loop - decide what should change next. Use after several practice sessions, when models feel off, at the end of a project, or when the user says "/reflect <topic>". Compresses recurring errors into next micro-goals, checks drift against the survey matrix on both axes (mainline and stage), and gates playbook synthesis behind an adversarial defense.
---

# Reflect — Continuous Feedback

Last updated: 2026-09-02

The loop-closer: **what should change next.** Reflect consumes `/evaluate`'s snapshot rather than duplicating it — evaluate measures state; reflect changes trajectory (model edits, next micro-goals, playbook, framework structure). It keeps the knowledge base alive rather than a frozen snapshot.

## Rules

- **Short session, sharp questions.** 10–15 minutes, not an hour.
- **Don't rewrite everything.** Touch only what's wrong, stale, or missing; minimal model edits.
- **Archive, don't delete.** Dead records get marked `(archived: <reason>)` in `notes.md` — the history of wrong models is valuable.
- **Never write mastery levels.** That's `/evaluate`'s job; recommend running it first if the snapshot is stale or missing.
- **Don't reflect on 0 cases.** It's navel-gazing.

## Flow

### 1. Gather state

Read `learning/<slug>/`: `notes.md` (the consolidated file containing Records, Terms, Structural Memory, Micro-Skills, Playbook, and the latest Mastery Snapshot — if absent or stale, recommend `/evaluate <slug>` first), all `case-*.md`, and `survey.md`.

### 2. Three questions

**a) "Since last session, what's the most surprising thing you learned?"** — surprise means a model was wrong or incomplete; probe it. Nothing surprising → "What was harder than expected?"

**b) "Which model feels weakest right now?"** — weak = never used in practice, can't be applied confidently, or vague boundary conditions. Cross-check against the mastery snapshot.

**c) "What kind of problem are you avoiding?"** — surfaces practice gaps.

### 3. Error compression

Scan all `case-*.md` **Errors made** fields. Surface patterns: "a variant of this error appears in 3 of 5 cases." Recurring errors become the **next `/practice` micro-goals** — state them explicitly ("next session's micro-goal: <X>, targeting the <error> pattern"). This closes the deliberate-practice loop.

### 4. Matrix drift check

Compare where effort actually went (which mainlines and stages the cases and models cluster on) against `survey.md`'s matrix, on both axes:

- **Breadth drift** — effort clusters on a mainline the investment table didn't prioritize, or on stop-early/SKIP items: "30% was allocated to X but all 5 cases are on Y — recalibrate the matrix or the habit?"
- **Depth drift** — evidence piles up left of a target: all cases reproduce samples (`can-apply`) on a mainline whose target is `can-transfer`, and transfer is never attempted. Comfort-zone stagnation is invisible without this check.

Either answer (recalibrate the matrix, or change the habit) is fine; unexamined drift is not. Matrix edits go through `/survey`, not here.

### 5. Update models & framework structure

For any record that needs adjustment: ask what changed (sharper boundary? new example? doesn't hold?), edit it minimally in the **Records** section of `notes.md`, append `(revised <date> — <what changed>)`. Dead records → archive (see Rules).

Then mirror the structural consequences in the **Structural Memory** section of `notes.md` (per [../learn/references/notes-format.md](../learn/references/notes-format.md)): a cracked model archives or re-glosses its node; a revised boundary may re-label an edge; a "no model fits" pattern becomes a Missing-links entry. If the tables changed, regenerate the Map and **bump `Iteration` by 1** — you are the only skill that touches the counter. Earning is not yours: never flip `target` → `earned` here (that needs `/learn` or `/practice` evidence).

### 6. Playbook — behind the defense gate

At **5+ cases**, offer playbook synthesis. But first, the **adversarial defense gate (ICAP-I)**:

- Steelman 2–3 objections to the user's key positions — the strongest version an informed critic would make, not strawmen.
- The user defends or revises. A position enters the playbook **only** if it survives or is revised — this keeps positions defensible from both sides and guards against self-congratulation.
- You MUST refuse to write the playbook for positions that were neither defended nor revised.

Then write/update the **Playbook** section of `notes.md`: the user's repeatable method and defended positions, each noting the objection it survived.

### 7. Close

Set next micro-goals (from step 3).

## Contract test

Recurring error surfaced across ≥2 cases; drift vs the matrix reported on both axes (breadth and depth); playbook refused until positions survive the steelman; a structural change to Structural Memory regenerates the Map and bumps `Iteration` exactly once; no `target` → `earned` flip happens here.

## Handoffs

**In:** ≥1 case in `learning/<slug>/`; a fresh Mastery Snapshot (else recommend `/evaluate <slug>` first).

**Out:**
- Recurring errors compressed → next micro-goals → `/practice`'s next session opener.
- Model revisions + framework structure revised, `Iteration` bumped → Playbook and Structural Memory sections in `notes.md`.
- Matrix drift confirmed as a targets problem → back to `/survey` — the matrix is not yours to edit.
- 5+ cases and positions survive the steelman → Playbook section in `notes.md` (its positions enter Structural Memory General frameworks).
- A `/synthesis-research` judgment contradicted a record → resolve here via minimal model edit or archive.

## Boundaries

- vs `/evaluate`: evaluate measures (mastery snapshot); reflect changes trajectory. Reflect never writes mastery levels.
- vs `/practice`: practice records per-case errors; reflect compresses across cases and hands micro-goals back.
- vs `/survey`: reflect flags matrix drift but the matrix itself is `/survey`'s to change.
