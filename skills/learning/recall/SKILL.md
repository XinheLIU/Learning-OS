---
name: recall
description: Cold retrieval practice against the course's due items. Use when the user wants to review, test themselves, do their daily retrieval, asks "what's due", or says "/recall" or "/recall <topic>". Reads learning/<slug>/retrieval.md, tests every due item cold — prompt emitted alone, answer withheld until an attempt exists — records the outcome, and reschedules. Tests and reschedules only; it never teaches.
---

# Recall — Retrieval Scheduler

Last updated: 2026-08-31

The system's return path. `/learn` and `/practice` write knowledge in; this is the only skill that
pulls it back out on a schedule. It reads the retrieval ledger, tests everything due **cold**,
records what happened, and moves the due dates.

Deliberately narrow: it selects, prompts, scores, reschedules. It teaches nothing. A failed item
goes back into the queue at the first rung and, on a second consecutive lapse, is flagged for
`/learn` to re-tutor. Ten to fifteen minutes, so it can actually be daily.

Ledger schema, interval ladders, and the scheduling rules: [`../learn/references/retrieval.md`](../learn/references/retrieval.md).

## Prime directive

**Emit the prompt and stop.**

You MUST NOT include the answer, a hint, a worked example, or a leading restatement of the item in
the same message as the prompt. Send the prompt; end the turn; wait for the learner's attempt. Help
of any kind is feedback that follows an attempt, never material that precedes one.

This is not a style preference. An answer visible in the same message makes the retrieval warm, and
a warm retrieval recorded as cold corrupts every row it touches.

## Rules

- **Cold only.** No material open, no lesson linked, no `notes.md` quoted. If the learner opens the
  material mid-item, say so and record the firing at `walkthrough` — it holds the rung and flags the
  row `coached`, which is the honest treatment for a retrieval that was not cold. Never record it as
  a clean pass.
- **One item, one message.** Never batch prompts; the second prompt cues the first.
- **Score on two axes and no others.** A correctness bit for the cold attempt and one value from the
  assistance enum. No percentages, no confidence ratings, no second scale.
- **Time-boxed to 15 minutes.** Overflow is normal and is not a failure.
- **Never teach.** A wrong item is rescheduled, not explained. Naming the correct answer as feedback
  after the attempt is recorded is allowed and expected; re-deriving it, working an example, or
  giving a second attempt at a variant is `/learn`'s job.
- **Never create rows.** `/learn` and `/practice` create items; you only fire them.

## Preconditions

Requires at least one `learning/<slug>/retrieval.md`. If the named course has no ledger, say so and
recommend `/learn <slug>` — do not scaffold one from `notes.md`, because a row not backed by a
successful demonstration is a fabricated earning date.

`/recall` with no argument unions the due rows of every course under `learning/`. `/recall <slug>`
narrows to that course.

## Flow

### 1. Select

Read every ledger in scope. Due = `next-due <= today` and `state != re-tutor`.

Report the queue before starting: how many due, from which courses, how many carry lapses.

**Overflow.** If the due set will not fit the 15-minute box, sort by `lapses` descending, then by
`next-due` ascending, and take the top of that order. Highest-lapse-first because a lapsing item is
the one actually at risk; oldest-due breaks ties. Items not reached keep their `next-due` and
surface first tomorrow — never reschedule an item that was not fired.

### 2. Fire each item

Per item, in order:

1. **Prompt.** One question, derived from the item's `pointer`, answerable in one or two lines.
   A `term` prompts for the definition; a `schema` prompts for the rule, its trigger condition, or
   the transition — never for a name you have already said. End the turn here.
2. **Receive the attempt.** Record the correctness bit against the pointer's content: was the cold
   attempt substantively right, before any help.
3. **Feedback.** State what was right or wrong and give the correct answer plainly. One or two
   lines. If the learner asks for more and you supply the reasoning, that is `walkthrough`; if you
   supply the answer before any attempt exists, that is `solution-shown` and the firing carries no
   cold evidence — record it at that level rather than discarding it.
4. **Score.** Correctness bit plus the maximum assistance used during the firing.

### 3. Reschedule

Apply the scheduling rules in [`../learn/references/retrieval.md`](../learn/references/retrieval.md)
to each fired row and write the ledger. Rewrite only the fired rows; leave every other row byte-for-byte
alone.

### 4. Report

A short summary, not an analysis:

```markdown
## Recall — <date>  (<n> fired, <n> due unreached)
| item | result | assistance | next due |
| :--- | :--- | :--- | :--- |
| two-state-machine | pass | none | 2026-09-03 (3d) |
| k-transactions | lapse | hint | 2026-09-01 (1d) |

**Flagged for re-tutor:** <item> (2 consecutive lapses) — run `/learn <slug>`.
```

Nothing is written to `notes.md`. The ledger is the record; a `/recall` firing is not a learning
record and does not become one.

## Contract test

Given a ledger with due and not-due rows: only due rows with `state != re-tutor` are selected; each
prompt is emitted in a message containing no answer, hint, or restatement, and the turn ends there;
every firing records exactly one correctness bit and one enum assistance value; a pass at `none`
advances one rung and increments `streak`; a pass at `hint` holds the rung and zeroes `streak`; a
pass at `walkthrough`/`solution-shown` holds and sets `state: coached`; any incorrect cold attempt
resets to the first rung, increments `lapses`, and sets `lapsed`, escalating to `re-tutor` on the
second consecutive one; an over-box queue is cut highest-lapse-first then oldest-due and unreached
rows keep their `next-due`; no new rows are created; `notes.md` and `framework.md` are unmodified;
the output contains no numeric score. Reject a session that explains a missed item beyond naming
the answer, or that fires a `re-tutor` row.

## Handoffs

**In:** `retrieval.md` rows created by `/learn` (schemas and terms earned in lessons) and
`/practice` (schemas earned on cases).

**Out:**
- Rows rescheduled → `retrieval.md` → the next `/recall`.
- Item flagged `re-tutor` → `/learn <slug>` re-tutors it, then clears the flag.
- Repeated lapses clustered on one mainline → `/reflect <slug>`.
- Nothing to `/evaluate`: a recall pass is retrieval evidence, not a mastery claim. `/evaluate`
  reads the ledger as corroboration and still requires its own rubric evidence.

## Boundaries

- vs `/learn`: learn builds and re-teaches; recall only tests what learn already built. A lapsing
  item goes back to learn — recall never re-explains it.
- vs `/evaluate`: recall *builds* retention through testing and writes the ledger; evaluate
  *measures* mastery and stays read-mostly. Recall never assigns a rubric level.
- vs `/practice`: practice applies models to real cases and produces case files; recall fires
  single-prompt items and produces no artifact but the ledger.
- vs `/reflect`: recall reports lapses; reflect decides what to do about a pattern of them.
