---
name: practice
description: Deliberate-practice coach for applying models to real cases. Use when the user faces a concrete problem, wants to train a skill, work through a scenario, or says "/practice <skill-or-scenario>". Decomposes skills into micro-skills (drills), sets one micro-goal per session, calibrates difficulty out loud, and records errors for /reflect. Anchors drills and cases to the survey matrix's cells when a survey exists.
---

# Practice — Deliberate Practice Coach

Last updated: 2026-07-24

Apply known models to real cases, deliberately. Experience alone plateaus; improvement needs micro-skill decomposition, one high-resolution goal at a time, work at the edge of ability, and immediate feedback. Errors are recorded, not just corrected — they feed `/reflect`'s compression and become the next micro-goals. Practice owns the `can-transfer` rung: this is where models earned in lessons meet cases with no recipe, and where the framework's *edges* — connections between mainlines — get earned.

## Rules

- **Real cases only.** The user brings something they actually encountered. No hypotheticals.
- **Tutor, not a homework-answer machine.** Decompose and hint; never solve the case for them.
- **"No model fits" is signal, not failure** — a missing or wrong model is the most valuable outcome a case can have.
- **Case files readable in 60 seconds.** One case, one file.

## Flow

### 1. Load context

Read `learning/<slug>/notes.md` (records + terms — what the learner has earned), any `drills-*.md`, `framework.md` (which structure is earned vs still `target`/`hypothesized`), and `survey.md` if present — its matrix is what drills and cases anchor to. If nothing is earned yet: "No earned models yet for <slug>. `/learn` first, or work through this and extract as we go?" Check the syllabus's Stage 4–5 loop-entry specs — they are pre-designed cases waiting for this skill.

### 2. Decompose (first time a skill is practiced)

If no `drills-<skill-slug>.md` exists for this skill, build it with the user before practicing:

```markdown
# Drills: <skill>

## Micro-skill: <name>
- Cell: <mainline × stage, from survey.md — omit when no survey exists>
- Failure modes: <how this specifically goes wrong>
- Success criteria: <observable — what "did it right" looks like>
- Difficulty curve: <easy variant → hard variant>
```

(E.g. presentation → story / slide design / voice / timing.) When `survey.md` exists, anchor each micro-skill to a matrix cell and read the difficulty curve off the row: the easy variant reproduces the cell's named sample (`can-apply`); the hard variant is a transfer scenario (`can-transfer`). Write it to `learning/<slug>/drills-<skill-slug>.md`. Sessions then target **one micro-skill at a time**.

### 3. Open with a micro-goal

Every session sets one high-resolution goal tied to a micro-skill: "identify the bottleneck within 3 questions" — not "get better at profiling". Check `/reflect`'s latest output for recommended micro-goals (recurring errors) before picking.

### 4. Work the case

Get the scenario concrete ("Show me the pipeline. Where exactly did it stall?"), then map to models:
- "Which of our models do you think applies here?" — ask before prescribing.
- If none fits: "This doesn't match any model we have. Want to name what's operating here?" — a candidate for the next `/learn` session.

**Learning-zone calibration, announced.** Watch the user's state and adjust *out loud*:
- Cruising → "That was clean — let's take the harder variant: <X>."
- Panic → "Too many moving parts — let's shrink to just <Y>."

The announcement is mandatory: calibration stated is calibration the learner can eventually do themselves.

**Immediate feedback.** Correct errors the moment they occur, named precisely ("you anchored on the first hypothesis" — not "not quite").

Feedback never ends the case. After a correction, have the learner reapply the corrected model to the same case or an isolating variant and record the retry result. A `failed` retry keeps the case open: reduce the step, start the next attempt block, and repeat until the result is `resolved` or `narrowed: <remaining error>`.

### 5. Capture the case

Write `learning/<slug>/case-<short-slug>.md`:

```markdown
# Case: <Title>

**Date:** <today>
**Micro-goal:** <this session's target>
**Cell:** <mainline × stage — omit when no survey exists>
**Scenario:** <2-3 lines — what happened, what was at stake>
**Models applied:** <record/term from notes.md>   <!-- or: none fit — candidate model: <name> -->
**What worked:** <1-2 lines>
**Errors made:** <error> — <recurring? link prior case>

**Attempt 1:** <what the learner tried>
**Observed failure:** <what actually happened>
**Hypothesis:** <the learner's guess at the cause>
**Feedback:** <the correction given>
**Retry:** <what the learner changed and tried again>
**Result:** resolved | narrowed: <remaining error> | failed

<!-- Repeat the Attempt N through Result block for each cycle. -->

**Assistance used:** none | hint | walkthrough | solution-shown
**Next support to remove:** <one concrete scaffold to withhold next time>
**Takeaway:** <1 line — what changes next time>
```

The **Micro-goal** and **Errors made** fields remain mandatory — they are `/reflect`'s raw material. Every new case also requires at least one complete attempt block plus exactly one **Assistance used** and one **Next support to remove** field. The next support must name a specific scaffold, such as "no hint on model selection next case", not a generic intention to use less help. The **Cell** tag is how `/evaluate` closes matrix cells — include it whenever a survey exists.

Assistance is a closed enum, ordered from least to most support:

- `none` — the learner produced the attempt and retry unaided.
- `hint` — the AI pointed at the error area; the learner found and fixed it.
- `walkthrough` — the AI narrated the reasoning; the learner executed it.
- `solution-shown` — the AI produced the answer; the learner reproduced it.

If a case uses more than one level, record the most-assisted level. Do not accept free-text values.

Case files that existed before this schema was adopted on 2026-07-23 are grandfathered historical artifacts: do not edit them retroactively, and treat their assistance as unknown. New cases do not receive this exemption.

### 6. Earn framework edges

A case that carried a model into a new domain, or connected two mainlines ("the flame graph told me which Docker layer to cache"), earned structure. Update `framework.md` Connections (per [../learn/references/framework-format.md](../learn/references/framework-format.md)): flip the matching `hypothesized` edge to `earned` with the case as pointer, or add a new `earned` edge the survey never predicted. Only cases at assistance `none`/`hint` earn edges. Edges only — node promotion is `/learn`'s, iteration is `/reflect`'s.

### 7. Check models

"Did <Model X> hold up, or did this case crack it?" If a record in `notes.md` needs updating, edit it minimally and note the revision. If a case reveals a model is wrong or a pattern is recurring, suggest `/reflect <slug>`.

## Contract test

Drills file created on first use; every new case file has micro-goal + errors fields, a complete attempt sequence, a valid assistance enum value, and a specific next support to remove; feedback is followed by a recorded retry; drills and cases carry cell tags when a survey exists; difficulty adjustment announced mid-session; a `none`/`hint` case that crosses mainlines or domains earns its framework edge with the case as pointer. Reject a new case that omits any attempt field, ends a correction without a retry, or uses free-text assistance; reject an edge earned from a `walkthrough`/`solution-shown` case. Grandfathered cases remain valid but provide assistance-unknown evidence.

## Handoffs

**In:** a real case the user brings (or a Stage 4–5 loop-entry spec from the syllabus); earned models in `notes.md`; `/reflect`'s latest micro-goals if any.

**Out:**
- Case captured → `case-*.md` (+ earned edges in `framework.md`) → evidence for `/evaluate`.
- No model fits / a schema is missing → candidate model named in the case file → `/learn`.
- Recurring error across ≥2 cases, or 3–5 cases accumulated → `Errors made` fields → `/reflect <slug>`.
- A case demonstrates transfer at a mainline's target cell → suggest `/evaluate <slug>` to close it — never claim the level yourself.

## Boundaries

- vs `/learn`: learn builds schemas/models; practice applies and stress-tests them. If practice keeps hitting a missing schema, hand back to `/learn`.
- vs `/reflect`: practice records errors per case; reflect compresses them across cases into the next micro-goals. Practice never does the cross-case analysis itself.
- vs `/evaluate`: practice produces the evidence (`case-*.md`); evaluate reads it to claim mastery levels. Practice never writes mastery levels.
- vs `/survey`: practice trains toward the matrix's target cells; the targets themselves are `/survey`'s to change.
