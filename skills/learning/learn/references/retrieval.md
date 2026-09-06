# retrieval.md Format

Last updated: 2026-09-06

`learning/<slug>/retrieval.md` is the course's retrieval ledger: one row per **item** — a unit
testable by a single cold recall prompt. It is the file that answers "what is due today". `/recall`
owns it; `/learn` and `/practice` create rows; nothing else writes it.

One ledger per course. `/recall` with no argument unions the due rows of every course under
`learning/`; `/recall <slug>` narrows to one.

## Full template

```markdown
# Retrieval: {Topic}

<!-- schedule: production -->

| id | kind | pointer | earned | last-fired | next-due | interval-days | streak | lapses | last-assistance | state |
| :-- | :-- | :-- | :-- | :-- | :-- | --: | --: | --: | :-- | :-- |
| two-state-machine | schema | notes.md#structural-memory:two-state-machine | 2026-08-31 | 2026-08-31 | 2026-09-01 | 1 | 0 | 0 | none | active |
| hold-vs-free | term | notes.md#terms:hold-vs-free | 2026-08-31 | 2026-09-02 | 2026-09-05 | 3 | 1 | 0 | none | active |
```

Column order is fixed. Alignment padding is not — do not reflow the table to keep it pretty.

## Columns

| Column | Value |
| :--- | :--- |
| `id` | kebab-case, unique within the course. Stable: never renumber, never reuse. |
| `kind` | `schema`, `term`, or `operational`. Operational rows cover bounded commands, shortcuts, patterns, or recovery actions from the syllabus Memory Budget. |
| `pointer` | Where the item's content lives: `notes.md#terms:<term>` (a term), `notes.md#0004` (a record), or `notes.md#structural-memory:<node>` (a Structural Memory node). One pointer per row. (`framework.md#<node>` appears only in pre-v2 ledgers — treat it as `notes.md#structural-memory:<node>`.) |
| `earned` | ISO date of the first successful demonstration — the row's creation date. Never changes. |
| `last-fired` | ISO date of the most recent `/recall` firing. Equals `earned` until the first firing. |
| `next-due` | ISO date. `/recall` selects rows where `next-due <= today`. |
| `interval-days` | Integer. The gap that produced `next-due`. |
| `streak` | Consecutive unassisted cold-recall passes. Starts at 0 — the earning demonstration was warm, not cold. |
| `lapses` | Cumulative failed cold recalls. Never decreases. |
| `last-assistance` | `none` \| `hint` \| `walkthrough` \| `solution-shown` — the existing enum, from the most recent firing. |
| `state` | `active` \| `lapsed` \| `coached` \| `re-tutor`. |

### state

- `active` — normal rotation.
- `lapsed` — the last firing was a lapse. One more consecutive lapse escalates.
- `coached` — the last pass needed a `walkthrough` or the answer. `/learn` may re-teach it; not urgent.
- `re-tutor` — two consecutive lapses. `/recall` stops firing it and `/learn` must re-tutor before it
  returns to rotation.

## Creating rows

A row is created **on first successful demonstration** at assistance `none` or `hint` — the same
moment `/learn` promotes a framework node or `/practice` closes a case at `none`/`hint`. Never at
exposure: a ledger seeded at exposure fails everything on day 2 and reads as a broken scheduler
rather than as forgetting.

Initial values: `earned` and `last-fired` = today, `interval-days` = the first rung, `next-due` =
today + that rung, `streak` = 0, `lapses` = 0, `last-assistance` = the demonstration's assistance,
`state` = `active`.

A demonstration at `walkthrough` or `solution-shown` creates nothing. Coached work does not earn a
row, for the same reason it does not earn a framework node.

### What is not an item

`kind` has three values. A case record is *evidence*, not an item — it is a specific
event, and re-asking it tests episodic memory rather than a chunk. A problem is a task, not a unit
of knowledge. A framework node that is not also a schema or a term has no single cold prompt. If
something cannot be tested by one prompt with one right answer, it does not get a row. Operational
items qualify only when the prompt tests a bounded recall or execution action.

## The schedule

The `<!-- schedule: -->` comment on line 3 selects the interval ladder. It is explicit because the
two ladders are not comparable and a ledger must never be read under the wrong one.

- `production` — 1, 3, 7, 16, 35 days, then monthly (30-day rungs) indefinitely.
- `trial` — 1, 2, then 2 indefinitely. Compressed so a three-day dogfood cycle produces two
  overnight intervals. See the [learning execution plan](../../../../docs/exec-plans/learning.md).

A trial ledger produces **zero evidence about interval sizing**. The production ladder is sourced
from the learning-science notes and is never revised from a cycle result.

## Scheduling rules

Every firing records two things: a **correctness bit** — was the cold attempt, before any help,
substantively right — and an **assistance level** from the enum, the maximum help given during the
firing. Four rules, applied in this order:

1. **Lapse** (`correct = no`, any assistance) — `interval-days` → the first rung, `next-due` →
   tomorrow, `lapses` +1, `streak` → 0. `state`: `active`/`coached` → `lapsed`; `lapsed` →
   `re-tutor`.
2. **Pass at `none`** — advance one rung, `streak` +1, `state` → `active`.
3. **Pass at `hint`** — hold the current rung, `streak` → 0, `state` → `active`. Assisted retrieval
   is retrieval, but it does not earn more time.
4. **Pass at `walkthrough` / `solution-shown`** — hold the current rung, `streak` → 0, `state` →
   `coached`.

In every case `last-fired` = today, `next-due` = today + `interval-days`, `last-assistance` = the
firing's value.

Rows at `state: re-tutor` are excluded from selection. `/learn` clears the flag by re-tutoring the
item to a successful construction, which resets the row to the first rung, `state: active`,
`streak` 0 — `lapses` is not reset.

## Pruning

Never delete a row. An item the learner has outgrown is not deleted either — a lapse history is the
only record of what decayed and why. If a course is abandoned, the ledger is abandoned with it.
