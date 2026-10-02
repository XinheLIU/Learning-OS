---
name: reflect
description: Close the learning loop - decide what should change next. Use after several practice sessions, when models feel off, at the end of a project, or when the user says "/reflect <topic>". Compresses recurring errors into next micro-goals, checks drift against the survey matrix on both axes (mainline and stage), writes source verdicts and cross-topic edges from case evidence, and gates playbook synthesis behind an adversarial defense.
---

# Reflect — Continuous Feedback

Last updated: 2026-09-28

The loop-closer: **what should change next.** Reflect consumes `/evaluate`'s snapshot rather than duplicating it — evaluate measures state; reflect changes trajectory (model edits, next micro-goals, playbook, framework structure). It keeps the knowledge base alive rather than a frozen snapshot.

## Rules

- **Short session, sharp questions.** 10–15 minutes, not an hour.
- **Don't rewrite everything.** Touch only what's wrong, stale, or missing; minimal model edits.
- **Archive, don't delete.** Dead records get marked `(archived: <reason>)` in `notes.md` — the history of wrong models is valuable.
- **Never write mastery levels.** That's `/evaluate`'s job; recommend running it first if the snapshot is stale or missing.
- **Propose, don't apply, upstream changes.** A source's `tier` and a node's `mode` are owned by
  `/curate-sources` and `/survey`. Reflect writes the *evidence* that argues for a change — a
  verdict line, a proposal line — and stops there. Observing and deciding are deliberately
  different skills, so that the decision is made by something that read the whole file.
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

### 4b. Write source verdicts from the error clusters

An error cluster that traces to how a **source** explained something is evidence about that source,
and the registry is where it belongs — otherwise every learner rediscovers the same bad chapter.

For each cluster from step 3, ask: did the learner's model come from a registered source, and did
the source mislead? If yes, append one line to `sources/<domain>.md` under `## Verdicts`, per
[`sources/README.md`](../../../sources/README.md#verdict-format):

```text
#v12 2026-10-05 dlai-attention-pytorch demote learning/transformer/case-0003.md [hint] — its QKV
  diagram labels V as "the thing you search with"; three of five cases repeated that error.
```

Rules:

- **A verdict needs a pointer** to a `case-*.md` or an Attempt Log row. "It felt thin" is not a
  verdict.
- **`hold` is a real verdict** and usually the right one: a source the cases leaned on and that
  held up should say so, or tier 1 never means anything.
- **Never edit a `tier` cell.** `/curate-sources` applies the verdict on its next run.
- One verdict per source per reflect pass, not one per case.

Also propose `mode → deep` for any `connect` node that keeps appearing in the error clusters — the
learner needed to *use* something the survey said they only needed to *place*. Write the proposal as
a line in the reflect output and in `notes.md`; **do not edit `survey.md`**. The mode changes on the
next `/survey` deepening pass, and that lag is the point: one wrong-feeling session is not a
re-scope.

### 4c. Earn cross-topic edges

When a case used a model from **another slug**, `learning/index.md` is where that shows. Flip the
matching `hypothesized` row to `earned` with the case as pointer, or add an `earned` row the
surveys never predicted:

```markdown
| rl:rlhf-reward-model | transformer:lm-head | bridges | earned | learning/rl/case-0002.md [hint] |
```

Same rules as within-topic edges, one addition: **both endpoints must still exist** in their slugs'
Structural Memory. An edge whose endpoint was renamed or archived gets
`archived: <reason>` here too — never silently dropped. Only cases at `none`/`hint` earn. A
hypothesis that two cycles failed to earn is archived with its reason, which is a result.

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

Recurring error surfaced across ≥2 cases; drift vs the matrix reported on both axes (breadth and depth); playbook refused until positions survive the steelman; a structural change to Structural Memory regenerates the Map and bumps `Iteration` exactly once; no `target` → `earned` flip happens here for a *node*. A cluster traced to a source appends exactly one verdict line carrying a `case-*.md` or Attempt Log pointer and does **not** touch any `tier` cell; a `connect` node recurring in the clusters produces a `mode → deep` proposal line and leaves `survey.md` unchanged; a case that used another slug's model flips or adds an `earned` row in `learning/index.md` with both endpoints resolving, and a two-cycle-old hypothesis is archived with a reason rather than deleted. Reject a verdict with no pointer, a tier edit, a mode edit, and a cross-topic edge earned from `walkthrough`/`solution-shown` evidence.

## Handoffs

**In:** ≥1 case in `learning/<slug>/`; a fresh Mastery Snapshot (else recommend `/evaluate <slug>` first).

**Out:**
- Recurring errors compressed → next micro-goals → `/practice`'s next session opener.
- Model revisions + framework structure revised, `Iteration` bumped → Playbook and Structural Memory sections in `notes.md`.
- Matrix drift confirmed as a targets problem → back to `/survey` — the matrix is not yours to edit.
- Error cluster traced to a source → verdict in `sources/<domain>.md` → applied by `/curate-sources` on its next run.
- `connect` node that kept being needed → `mode → deep` proposal → applied by the next `/survey` deepening pass.
- Case crossed two slugs → `earned` edge in `learning/index.md` → read by `frame` and indexed by synapse.
- 5+ cases and positions survive the steelman → Playbook section in `notes.md` (its positions enter Structural Memory General frameworks).
- A `/synthesis-research` judgment contradicted a record → resolve here via minimal model edit or archive.

## Boundaries

- vs `/evaluate`: evaluate measures (mastery snapshot); reflect changes trajectory. Reflect never writes mastery levels.
- vs `/practice`: practice records per-case errors; reflect compresses across cases and hands micro-goals back.
- vs `/survey`: reflect flags matrix drift and proposes mode changes; the matrix and the modes are `/survey`'s to change.
- vs `/curate-sources`: reflect writes verdicts from case evidence; that skill applies them to tiers. The skill that observes and the skill that decides are different on purpose.
- vs `archive-materials`: both write verdicts. That one writes from a shipped chapter (`hold`/`promote` — the source held up in use); this one writes from error clusters (`demote`/`hold` — the source mis-taught). Learning evidence and writing evidence, same file.
