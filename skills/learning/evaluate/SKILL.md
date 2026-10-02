---
name: evaluate
description: Evidence-backed mastery snapshot for a topic. Use when the user asks how well they know something, wants a mastery check, a progress assessment, or says "/evaluate <topic>". Read-mostly - assigns rubric levels (can-recall to can-generate) only where evidence files support them. Never numeric scores.
---

# Evaluate — Learning Evaluator

Last updated: 2026-09-28

A standalone, read-mostly assessor: a snapshot of **how deep mastery actually is**, separate from the feedback loop. The core discipline is *evidence before claims* — a level may only be claimed with a pointer to an evidence file. Self-reported competence doesn't count. Evaluate is also the system's **tier gate**: it alone declares when a mainline leaves the course tier (recall/apply), the loop tier (transfer), and reaches generation.

## Rules

- **No numeric scores, ever.** "Schemas 92%" is LLM confabulation. Rubric levels with evidence only.
- **Read-mostly.** Three writes only: the Mastery Snapshot section in `notes.md`; checking off a Stage 4–5 loop-entry checkbox in `syllabus.md` (mirrored in `index.html`) when evidence reaches its cell; and this slug's row in `learning/index.md` (`status`, `earned nodes`, `last evaluate`). No record edits, no Structural Memory writes, no cross-topic *edges*, no recommendations engine — that's `/reflect`.
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
| Independent | a **shipped writing artifact** — see below |

Levels are cumulative — claiming `can-transfer` implies `can-apply` evidence exists too.

Assistance gates every rung. Evidence at `walkthrough`, `solution-shown`, or `assistance-unknown` supports at most `can-recall`. `can-apply` and every higher level require evidence produced at `none` or `hint`, in addition to the rubric's existing requirement. When several attempts support one pointer, use the most-assisted level from the relevant cycle or case.

The ladder is shared with `/survey`'s matrix (its four stages: articulate / samples / adapt / synthesize). Survey folds `can-teach` into the synthesis stage at its granularity; evaluate keeps the two rungs distinct when assigning levels.

## Flow

### 1. Gather evidence

Read everything in `learning/<slug>/`: `notes.md` (the consolidated file containing Records, Terms, Structural Memory with earned nodes and edges), `syllabus.md` (checked lessons), all `case-*.md`, any `research-*.md`. Build the map: which cases used which records (via Models-applied fields), which explanations survived challenge, which research outputs exist, and what assistance produced each item. Treat pre-schema artifacts without assistance metadata as `assistance-unknown`; do not infer or retrofit a value.

### 2. Assess per node

**`deep` and `connect` nodes are assessed on different questions.** A `deep` node is assessed on
the rubric below — can the learner use it, and at what assistance. A `connect` node was never a
claim to be able to use anything, so the rubric does not apply to it: its only assessable state is
**placed** (an `earned` edge names it as an endpoint, with a learner-worded because-clause) or
**unplaced**. Report `connect` nodes in their own short table, never with a rubric level, and never
as `unassessed` merely because no case used them — no case was ever going to.

For each `deep` knowledge node (every record and term in the Records and Terms sections of `notes.md`):
- Find the strongest level the evidence and its assistance support; record the pointer with `[assistance: <value>]`.
- For `can-recall` where no session evidence exists, you MAY probe live: "In one line, what does <model> say?" — one question per node. Conduct it without tutoring by default. If any scaffolding is supplied, record the actual assistance rather than treating the probe as independent.
- A node with no evidence at all is reported as **unassessed**, not zero.

Record every live probe in the Mastery Snapshot as its own attempt cycle: initial attempt, observed outcome, feedback, retry, result, and assistance. A probe requiring `walkthrough` or `solution-shown` remains evidence of at most `can-recall`, even if its retry succeeds.

When `survey.md` exists, also roll nodes up to their mainline (cases and drills carry cell tags) and compare the strongest evidenced stage against the mainline's target cell.

### 2a. The `Independent` rung — a shipped chapter as evidence

`Independent` is the rung the whole system aims at: the learner produced the target output, judged
it, and corrected it without AI guidance. Until now nothing could evidence it, because the
learning loop's artifacts are all assisted by construction. A **shipped chapter is the natural
independent output** — the learner wrote it, and the draft is checkable.

A packaged draft supports `Independent` when **all four** hold:

1. **It is packaged.** `package-chapter` has stamped its six frontmatter fields and reported zero
   BROKEN references. An unpackaged draft is a work in progress, not an output.
2. **Assistance is declared and ≤ `hint`.** The draft folder records the assistance level the
   author worked at. An undeclared level is `assistance-unknown` and supports nothing above
   `can-recall`, exactly as everywhere else — do not infer it from how the prose reads.
3. **Its brief's author markers trace to `earned` nodes.** Every marker in `brief.md` names a node
   or edge that is `earned` in this slug's Structural Memory, at `none`/`hint`. This is the check
   that matters: a chapter can be fluent about things the author never learned, and a marker
   traced to a `target` node is precisely that chapter.
4. **`/grill` was answered from memory.** The grill log shows the author answered with the draft
   closed; a `peeked` answer caps the chapter's contribution at `can-apply`.

Reject, naming the failed condition, when any is missing. Two failures are worth calling out
specifically because they look like passes:

- **Assistance above `hint`.** A chapter drafted at `walkthrough` evidences that the *system* can
  produce a chapter, not that the author can. Record it as `can-apply` evidence and say so.
- **Markers that don't trace.** Name the markers and the nodes they claim. This is a finding about
  the brief, not about the chapter — route it back to `frame`.

Cite the chapter in the snapshot with its path, its assistance, and the mainline it evidences:

```markdown
| independent output | Independent | drafts/transformer/transformer.md (packaged 2026-10-12) [assistance: hint] — 4 brief markers all trace to earned nodes |
```

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

**Connect nodes** (placed / unplaced — no rubric level applies):
| Node | State | Edge |
| :--- | :--- | :--- |
| mixture-of-experts | placed | `contrasts-with` dense FFN — C-02 [none] |
| RNN encoder-decoder | unplaced | no edge yet |

**Depth distribution:** N terms · N schemas/models · N frameworks (playbook, research)

**Live probe attempts** (include when probes were used):
- <date> probe <node>: attempt <response> → observed <outcome> → feedback <correction or none> → retry <resolved | narrowed: remaining error | failed> [assistance: <enum>]

**Regression:** <node> changed from <prior level> to <new level> because <prior evidence lacks assistance metadata or used coached assistance>. <!-- Required when the assistance cap lowers a previously reported level; otherwise omit. -->

**vs targets** (when `survey.md` exists):
| Mainline | Target | Achieved | Tier | Evidence gap |
| :--- | :--- | :--- | :--- | :--- |
| <mainline> | can-transfer | can-apply | course closed → in loop | no case outside the home domain yet |
```

### 3b. Refresh the cross-topic index row

Update this slug's row in `learning/index.md` ([schema](../README.md#the-cross-topic-index)):
`status` (`surveyed` / `course` / `loop` / `shipped`), `earned nodes` (count them in Structural
Memory), `last evaluate` (today). Create the row if the survey never did.

Rows only. Cross-topic **edges** are `/survey`'s to hypothesize and `/reflect`'s to earn; writing
one here would be claiming structure from a measurement, which is the one thing this skill must
never do.

### 4. Report the depth gauge

State the depth distribution and what it means: notes that are mostly terms are vocabulary, not understanding; mastery concentrated at `can-recall` means models were filed but never used independently. When targets exist, say which mainlines are closed (evidence reached the target cell), which are stalled, and at which stage — and state each mainline's tier. If the assistance cap lowers a level from the previous snapshot, state the regression and its cause explicitly; never preserve or hide the prior level. One or two sentences — the trajectory response belongs to `/reflect`.

Suggest `/reflect <slug>` if the snapshot shows drift or stagnation. When a mainline's loop tier closes, recommend `/synthesis-research <slug>` on the Structural Memory Frontier entries touching it — that mainline's next rung is generative.

## Contract test

Given fixture models + cases: every claimed mastery level cites an evidence file and assistance value; missing assistance is reported as `assistance-unknown`; `walkthrough`, `solution-shown`, and unknown evidence never support above `can-recall`; `can-apply` and above use `none` or `hint` evidence; live probes are recorded as attempt cycles with assistance; cap-driven regressions are stated; nodes without evidence stay at the lowest supportable level; output contains no percentages; `connect` nodes are reported as `placed`/`unplaced` with their edge and never carry a rubric level, and a `connect` node without an edge is `unplaced`, not `unassessed`. `Independent` is claimed only for a packaged draft whose assistance is declared and ≤ `hint`, whose brief markers every trace to `earned` nodes, and whose grill log shows no `peeked` answer — a draft failing any of the four is rejected with the condition named, and one drafted above `hint` is recorded as `can-apply` evidence instead. This slug's `learning/index.md` row is refreshed with `status`, `earned nodes`, and `last evaluate`, and **no cross-topic edge is written**. Tier gates: a course-tier close cites every can-apply sample reproduction; a loop-tier close cites an outside-domain case *and* an earned cross-mainline edge in Structural Memory; a declaration missing either is rejected with the gap named; a reached loop-entry cell gets its syllabus checkbox checked.

## Handoffs

**In:** run on demand, after `/practice` suggests closing a cell, after a chapter is packaged, or before `/reflect` needs a fresh snapshot. Requires `learning/<slug>/` evidence files; works without a survey (no tier gating then). A packaged `drafts/<piece>/` with its `brief.md` and grill log is optional input for the `Independent` rung.

**Out:**
- Snapshot written → `notes.md` Mastery Snapshot → consumed by `/reflect`.
- Course tier closed for a mainline → declaration in the snapshot → `/practice` takes the mainline (transfer work starts).
- Loop tier closed for a mainline → Frontier entries touching it in Structural Memory → `/synthesis-research <slug>`.
- A packaged chapter at assistance ≤ `hint` with tracing markers → `Independent` in the snapshot → the graduation claim this system exists to make.
- Brief markers that don't trace to earned nodes → named in the report → back to `frame`.
- `learning/index.md` row refreshed → read by `frame` and indexed by synapse.
- Drift or stagnation visible → suggest `/reflect <slug>`.
- Targets themselves look wrong → that's `/survey`'s call, not yours.

## Boundaries

- vs `/reflect`: **evaluate measures state; reflect changes trajectory.** Evaluate never edits models, never sets micro-goals, never writes the playbook. Reflect consumes this snapshot but never writes mastery levels itself.
- vs `/practice`: practice produces the evidence; evaluate only reads it.
- vs the writing system: `package-chapter` proves a draft is portable and conformant; this reads that proof as *learner* evidence. Evaluate never edits a draft, and a chapter's craft quality is `review-draft`'s judgment, not a mastery level.
- vs `/survey`: survey sets targets and node modes; evaluate measures against them and gates tiers. Neither writes the other's columns — a `connect` node that should have been `deep` is reported, not re-moded.
