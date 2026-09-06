---
name: evaluate
description: Evidence-backed mastery snapshot for a topic. Use when the user asks how well they know something, wants a mastery check, a progress assessment, or says "/evaluate <topic>". Read-mostly - assigns rubric levels (can-recall to can-generate) only where evidence files support them. Never numeric scores.
---

# Evaluate — Learning Evaluator

Last updated: 2026-09-02

A standalone, read-mostly assessor: a snapshot of **how deep mastery actually is**, separate from the feedback loop. The core discipline is *evidence before claims* — a level may only be claimed with a pointer to an evidence file. Self-reported competence doesn't count. Evaluate is also the system's **tier gate**: it alone declares when a mainline leaves the course tier (recall/apply), the loop tier (transfer), and reaches generation.

## Rules

- **No numeric scores, ever.** "Schemas 92%" is LLM confabulation. Rubric levels with evidence only.
- **Read-mostly.** Two writes only: the Mastery Snapshot section in `notes.md`, and checking off a Stage 4–5 loop-entry checkbox in `syllabus.md` (mirrored in `index.html`) when evidence reaches its cell. No record edits, no Structural Memory writes, no recommendations engine — that's `/reflect`.
- **No evidence → lowest supportable level.** When in doubt, round down.
- **Assistance is part of every pointer.** Copy `none`, `hint`, `walkthrough`, or `solution-shown` from the source attempt record. If a grandfathered artifact has no assistance metadata, label the pointer `assistance-unknown`.

## The rubric

| Level | Evidence required |
| :--- | :--- |
| can-recall | correct restatement in session |
| can-apply | a `case-*.md` where the model was used successfully, or a reproduced sample named by a survey matrix can-apply cell |
| can-transfer | a case from a *different* domain |
| can-teach | learner explanation that survived tutor challenge (ICAP-I) |
| can-generate | a `/synthesis-research` report (judgment + so-what) or novel model |

Levels are cumulative — claiming `can-transfer` implies `can-apply` evidence exists too.

Assistance gates every rung. Evidence at `walkthrough`, `solution-shown`, or `assistance-unknown` supports at most `can-recall`. `can-apply` and every higher level require evidence produced at `none` or `hint`, in addition to the rubric's existing requirement. When several attempts support one pointer, use the most-assisted level from the relevant cycle or case.

The ladder is shared with `/survey`'s matrix (its four stages: articulate / samples / adapt / synthesize). Survey folds `can-teach` into the synthesis stage at its granularity; evaluate keeps the two rungs distinct when assigning levels.

## Flow

### 1. Gather evidence

Read everything in `learning/<slug>/`: `notes.md` (the consolidated file containing Records, Terms, Structural Memory with earned nodes and edges), `syllabus.md` (checked lessons), all `case-*.md`, any `research-*.md`. Build the map: which cases used which records (via Models-applied fields), which explanations survived challenge, which research outputs exist, and what assistance produced each item. Treat pre-schema artifacts without assistance metadata as `assistance-unknown`; do not infer or retrofit a value.

### 2. Assess per node

For each knowledge node (every record and term in the Records and Terms sections of `notes.md`):
- Find the strongest level the evidence and its assistance support; record the pointer with `[assistance: <value>]`.
- For `can-recall` where no session evidence exists, you MAY probe live: "In one line, what does <model> say?" — one question per node. Conduct it without tutoring by default. If any scaffolding is supplied, record the actual assistance rather than treating the probe as independent.
- A node with no evidence at all is reported as **unassessed**, not zero.

Record every live probe in the Mastery Snapshot as its own attempt cycle: initial attempt, observed outcome, feedback, retry, result, and assistance. A probe requiring `walkthrough` or `solution-shown` remains evidence of at most `can-recall`, even if its retry succeeds.

When `survey.md` exists, also roll nodes up to their mainline (cases and drills carry cell tags) and compare the strongest evidenced stage against the mainline's target cell.

### 2b. Gate the tiers (when `survey.md` exists)

Each mainline sits in exactly one tier; declare a transition only when its exit criteria are all evidenced:

- **Course tier closed** (→ loop tier): every K/S lesson of the mainline checked in `syllabus.md`; its can-recall cells evidenced; every can-apply cell's **named sample reproduced** at assistance `none`/`hint`.
- **Loop tier closed** (→ research tier): target cell reached at `none`/`hint` including ≥1 case **outside the home domain or on the learner's own project**; ≥1 `earned` cross-mainline edge touching the mainline in the Structural Memory section of `notes.md`.
- **Generation reached:** a `research-*.md` report (judgment + falsifier) touching the mainline — frontier-mode Frontier entries alone don't count.

A tier declaration missing any criterion is a contract violation — name the missing evidence instead. When a loop-entry spec's cell is reached, check its Stage 4–5 checkbox in `syllabus.md` and mirror `index.html`.

### 3. Write the snapshot

- In `notes.md`, write/replace a summary section:

```markdown
## Mastery Snapshot — <date>
| Node | Mastery | Evidence |
| :--- | :--- | :--- |
| record 0003 (model X) | can-transfer | case-y (different domain) [assistance: none] |
| term: <schema Z> | can-recall | live probe 01 [assistance: hint] |
| record 0005 (model W) | unassessed | — |

**Depth distribution:** N terms · N schemas/models · N frameworks (playbook, research)

**Live probe attempts** (include when probes were used):
- <date> probe <node>: attempt <response> → observed <outcome> → feedback <correction or none> → retry <resolved | narrowed: remaining error | failed> [assistance: <enum>]

**Regression:** <node> changed from <prior level> to <new level> because <prior evidence lacks assistance metadata or used coached assistance>. <!-- Required when the assistance cap lowers a previously reported level; otherwise omit. -->

**vs targets** (when `survey.md` exists):
| Mainline | Target | Achieved | Tier | Evidence gap |
| :--- | :--- | :--- | :--- | :--- |
| <mainline> | can-transfer | can-apply | course closed → in loop | no case outside the home domain yet |
```

### 4. Report the depth gauge

State the depth distribution and what it means: notes that are mostly terms are vocabulary, not understanding; mastery concentrated at `can-recall` means models were filed but never used independently. When targets exist, say which mainlines are closed (evidence reached the target cell), which are stalled, and at which stage — and state each mainline's tier. If the assistance cap lowers a level from the previous snapshot, state the regression and its cause explicitly; never preserve or hide the prior level. One or two sentences — the trajectory response belongs to `/reflect`.

Suggest `/reflect <slug>` if the snapshot shows drift or stagnation. When a mainline's loop tier closes, recommend `/synthesis-research <slug>` on the Structural Memory Frontier entries touching it — that mainline's next rung is generative.

## Contract test

Given fixture models + cases: every claimed mastery level cites an evidence file and assistance value; missing assistance is reported as `assistance-unknown`; `walkthrough`, `solution-shown`, and unknown evidence never support above `can-recall`; `can-apply` and above use `none` or `hint` evidence; live probes are recorded as attempt cycles with assistance; cap-driven regressions are stated; nodes without evidence stay at the lowest supportable level; output contains no percentages. Tier gates: a course-tier close cites every can-apply sample reproduction; a loop-tier close cites an outside-domain case *and* an earned cross-mainline edge in Structural Memory; a declaration missing either is rejected with the gap named; a reached loop-entry cell gets its syllabus checkbox checked.

## Handoffs

**In:** run on demand, after `/practice` suggests closing a cell, or before `/reflect` needs a fresh snapshot. Requires `learning/<slug>/` evidence files; works without a survey (no tier gating then).

**Out:**
- Snapshot written → `notes.md` Mastery Snapshot → consumed by `/reflect`.
- Course tier closed for a mainline → declaration in the snapshot → `/practice` takes the mainline (transfer work starts).
- Loop tier closed for a mainline → Frontier entries touching it in Structural Memory → `/synthesis-research <slug>`.
- Drift or stagnation visible → suggest `/reflect <slug>`.
- Targets themselves look wrong → that's `/survey`'s call, not yours.

## Boundaries

- vs `/reflect`: **evaluate measures state; reflect changes trajectory.** Evaluate never edits models, never sets micro-goals, never writes the playbook. Reflect consumes this snapshot but never writes mastery levels itself.
- vs `/practice`: practice produces the evidence; evaluate only reads it.
- vs `/survey`: survey sets targets; evaluate measures against them and gates tiers. Neither writes the other's columns.
