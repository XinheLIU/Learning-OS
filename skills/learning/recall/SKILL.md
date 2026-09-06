---
name: recall
description: Retrieval planner and ledger owner for the course's due items. Use when the user asks "what's due", wants their daily retrieval plan, says "/recall" or "/recall <topic>", or pastes recall results to sync. Reads learning/<slug>/retrieval.md, reports what is due and where to do it (the course's recall.html page), regenerates the page's embedded queue, and applies the scheduling rules to self-graded results on sync. The firings happen in the browser; this skill plans and reschedules — it never teaches.
---

# Recall — Retrieval Planner & Ledger Owner

Last updated: 2026-09-06

The system's return path. `/learn` and `/practice` write knowledge in; this is the only skill that
brings it back on a schedule. In v3 the firings happen **in the course, not in chat**: `recall.html`
presents due items cold (prompt alone, answer behind a reveal, self-graded), and this skill does
everything around that page — computing what's due, keeping its queue fresh, and applying the
scheduling rules when the results sync back.

Deliberately narrow: it plans, syncs, and reschedules. It teaches nothing. A failed item goes back
into the queue at the first rung and, on a second consecutive lapse, is flagged for `/learn` to
re-teach in the next lesson revision. Planning takes seconds; the page is sized for ten to fifteen
minutes, so retrieval can actually be daily.

Ledger schema, interval ladders, and the scheduling rules: [`../learn/references/retrieval.md`](../learn/references/retrieval.md).
Page format: [`../curriculum/references/lesson-format.md`](../curriculum/references/lesson-format.md) (the recall page section).

## Prime directive

**The page fires cold; chat never leaks an answer.**

`recall.html` presents each prompt alone, with the answer behind a reveal, exactly as a chat firing
would. This skill never quotes an item's answer — not in the plan, not in the sync report, not as a
"reminder". The one place an answer legitimately appears is the page's own reveal, after the learner
committed an attempt, and a pre-attempt reveal is graded **peeked** (assistance `walkthrough`) —
the honest treatment of a warm retrieval.

This is not a style preference. A warm retrieval recorded as cold corrupts every row it touches.

## Rules

- **No firing in chat.** Never prompt an item, never batch prompts, never quiz the user here. The
  plan says *how many* are due and *where* — never *what the answers are*.
- **Cold only.** The page's grading enforces it: an attempt graded before any reveal is cold;
  anything after a reveal is `walkthrough`. If the learner opens lesson material mid-session and
  says so, those firings sync as `walkthrough` and their rows go `coached`. Never record a warm
  pass as clean.
- **Score on two axes and no others.** A correctness bit for the cold attempt and one value from
  the assistance enum. No percentages, no confidence ratings, no second scale.
- **Time-boxed to 15 minutes on the page.** The plan says when the queue overflows the box; the
  page orders the queue (highest-lapse first, then oldest-due), so whatever fits the box is the
  right subset. Unreached items keep their `next-due` — never reschedule an item that was not fired.
- **Never teach.** A wrong item is rescheduled, not explained. Naming the correct answer after a
  graded attempt is the page's job (one or two lines); re-deriving it is `/learn`'s.
- **Never create rows.** `/learn` and `/practice` create items; you only schedule them.
- Operational rows from the syllabus Memory Budget use the same cold prompt and scheduling rules;
  execution latency may be displayed as evidence, but does not create a second score.

## Preconditions

Requires at least one `learning/<slug>/retrieval.md`. If the named course has no ledger, say so and
recommend `/learn <slug>` — do not scaffold one from `notes.md`, because a row not backed by a
successful demonstration is a fabricated earning date.

`/recall` with no argument unions the due rows of every course under `learning/`; `/recall <slug>`
narrows to that course.

## Flow

### 1. Select and plan

Read every ledger in scope. Due = `next-due <= today` and `state != re-tutor`.

Report the queue, then point at the page:

```markdown
## Recall plan — <date>
| course | due | lapsing | where |
| :--- | --: | --: | :--- |
| herdr | 9 | 2 | learning/herdr/recall.html |
| swe-basics | 4 | 0 | learning/swe-basics/recall.html |

**Overflow:** <course> has 21 due — the page will serve the top ~15 (highest-lapse first);
the rest hold their dates and surface first tomorrow.
```

If the queue is empty, say so and name the next due date. That is the whole plan. Do not summarize
the items themselves.

### 2. Refresh the page queue

For each course in scope, regenerate `recall.html`'s embedded due-item snapshot
(`window.<SLUG>_RECALL`) from the current ledger: due rows only, ordered by `lapses` descending
then `next-due` ascending, each carrying its id, kind, prompt (derived from the pointer), and
reference answer. This keeps the page correct over `file://`, where it cannot fetch the ledger.
(Over http the page prefers the live ledger — the snapshot is the fallback.)

Open the page for the user when there's exactly one course in scope (`open learning/<slug>/recall.html`).

### 3. Sync ("sync recall" + manifest)

The user pastes the recall results manifest copied from the page's sync block: JSON mapping item
ids to `{grade, revealed-before-attempt}`. Map grades to the two scoring axes:

| Page grade | Correctness | Assistance |
| :--- | :--- | :--- |
| got it (no pre-attempt reveal) | yes | `none` |
| got it (peeked first) | yes | `walkthrough` |
| missed it | no | `none` (a clean lapse) |
| peeked (answered only after reveal) | yes | `walkthrough` |

A grade of "got it" after the learner says they used a hint from the page's context is `hint` —
apply judgment, and when in doubt record the more-assisted value.

Apply the scheduling rules in [`../learn/references/retrieval.md`](../learn/references/retrieval.md)
to each fired row and write the ledger. Rewrite only the fired rows; leave every other row
byte-for-byte alone. Then regenerate the page snapshot (the queue changed).

### 4. Report

A short summary, not an analysis:

```markdown
## Recall — <date>  (<n> fired, <n> due unfired)
| item | result | assistance | next due |
| :--- | :--- | :--- | :--- |
| two-state-machine | pass | none | 2026-09-09 (3d) |
| k-transactions | lapse | none | 2026-09-07 (1d) |

**Flagged for re-tutor:** <item> (2 consecutive lapses) — `/learn <slug>` will fold it into the
next lesson's warm-up.
```

Nothing is written to `notes.md`. The ledger is the record; a firing is not a learning record and
does not become one.

## Contract test

Given a ledger with due and not-due rows: only due rows with `state != re-tutor` enter the page
queue; the plan reports counts and locations and contains no answers; a peeked-first grade syncs as
`walkthrough` and sets `state: coached`; a clean pass at `none` advances one rung and increments
`streak`; a clean lapse resets to the first rung, increments `lapses`, and sets `lapsed`,
escalating to `re-tutor` on the second consecutive one; an over-box queue is ordered
highest-lapse-first then oldest-due and unreached rows keep their `next-due`; no new rows are
created; `notes.md` is unmodified; the output contains no numeric score. Reject a sync that records
a peeked-first pass as `none`, a plan that quotes item answers, or a session that fires or explains
items in chat.

## Handoffs

**In:** `retrieval.md` rows created by `/learn` (schemas and terms earned in lessons) and
`/practice` (schemas earned on cases); the recall results manifest pasted by the user.

**Out:**
- Due plan + refreshed snapshot → `recall.html` → the learner fires items in the browser.
- Rows rescheduled → `retrieval.md` → the next `/recall`.
- Item flagged `re-tutor` → `/learn <slug>` re-teaches it in the next lesson revision, then clears
  the flag.
- Repeated lapses clustered on one mainline → `/reflect <slug>`.
- Nothing to `/evaluate`: a recall pass is retrieval evidence, not a mastery claim. `/evaluate`
  reads the ledger as corroboration and still requires its own rubric evidence.

## Boundaries

- vs `/learn`: learn builds and re-teaches; recall only schedules what learn already built. A
  lapsing item goes back to learn — recall never re-explains it, in chat or on the page.
- vs `/evaluate`: recall *builds* retention through testing and writes the ledger; evaluate
  *measures* mastery and stays read-mostly. Recall never assigns a rubric level.
- vs `/practice`: practice applies models to real cases and produces case files; recall schedules
  single-prompt items and produces no artifact but the ledger.
- vs `/reflect`: recall reports lapses; reflect decides what to do about a pattern of them.
