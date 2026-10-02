---
name: curate-sources
description: Discover and maintain the cross-topic source registry for one domain — find candidate sources, append them as unrated with a proposed tier, refresh what is still live, and apply pending verdicts to tier cells. Writes sources/<domain>.md and nothing else. Tier 2, workflow, ~30 min. Use for "/curate-sources <domain>", "find sources for X", 源头整理, 资料分级, or when /survey stops because a domain file is missing.
---

Last updated: 2026-09-28

# Curate Sources

## Overview

The registry's only writer of rows and tiers. A domain in, `sources/<domain>.md` out: candidate
sources found and appended as `unrated`, live sources re-verified, and any verdict that downstream
evidence produced since the last run applied to the tier cell it argues about.

This is **discovery**, split off from `/survey` on purpose. Survey's job is to decide what a
mission reads; going shopping for sources in the middle of that is how a survey turns into an
afternoon. Here the two are separate skills with separate outputs, and the registry is the seam:
this skill fills it, `/survey` reads it.

Schema, tier rules, and verdict format live in [`sources/README.md`](../../../sources/README.md).
This skill implements them; it does not restate them.

## Hard Rules

1. **Every new row enters `unrated`.** A proposed tier goes in the why line of the report and in the
   row's nothing-else — never in the `tier` cell. Tiers are earned by evidence, and a first
   impression is not evidence.
2. **A `tier` cell changes only by applying a pending verdict**, one line of reasoning each. A tier
   edit with no verdict behind it is a contract violation.
3. **Never delete a row.** A source that disappeared from the web is `verified: <date> (dead)` in
   its `source` cell, not a deletion. A source that disappointed is demoted by verdict.
4. **Never invent a verdict.** Verdicts come from `/archive-materials` and `/reflect`, which have
   evidence. This skill applies them; it does not author them. The one exception is the seeding
   run, where the author's own prior ranking is recorded as `author-judgment`.
5. **Re-runs append and refresh.** Existing ids, `domains`, and `verdicts` columns are preserved.
   A source already present is matched and refreshed, never added twice.
6. **Never touch anything but `sources/<domain>.md`.** Not `materials.md`, not `survey.md`, not the
   archive.
7. **A row must be openable.** A URL, or a path under the archive. A source you cannot point at is
   a memory, not a source.

## Workflow

### Step 1 — Read the registry and the pending verdicts

```bash
DOMAIN=<domain>
test -f "sources/$DOMAIN.md" && sed -n '/## Registry/,/## Verdicts/p' "sources/$DOMAIN.md"
sed -n '/## Verdicts/,$p' "sources/$DOMAIN.md" 2>/dev/null
```

If the file does not exist, this is a **seeding run**: create it from the README's template, and
say so in the report. Seeding is the one time tiers and verdicts land together, because the
judgments being recorded predate the registry — each seeded row gets an `author-judgment` verdict.

A verdict is **pending** when it names a `promote` or `demote` whose effect is not yet in the row's
`tier` cell. Build that list now; Step 4 applies it.

### Step 2 — Find candidates

Three places, in this order:

1. **The learner's own folders.** `materials.md` rows whose `source-id` is `—` are the highest-value
   candidates: material the author already has and the registry does not know about. Read the map,
   not the archive.
2. **The registry's own gaps.** Sources cited in `learning/<slug>/survey.md` as `gap` lines.
3. **The web**, last. Search for the domain's canonical courses, textbooks, and primary papers, plus
   anything the existing tier-1 rows cite repeatedly.

For each candidate decide **the one thing it would be read for**. A source with no answer to that is
not a candidate; drop it rather than filing it as tier 3.

**Do not fetch or distill the sources.** This lists them. Capturing one into `raw/` with provenance
is a separate step, and distilling it is `llm-wiki-ingest`.

### Step 3 — Append the new rows

One row per new source, `tier` = `unrated`, `verified` = today (you just confirmed it is live),
`verdicts` = `—`. `domains` reuses an existing value where one fits.

Assign the `id`: lowercase kebab, short, recognizable a year from now — `cs224n-2024`, not
`stanford-course-3`. Never reuse an id, including one whose row was demoted to tier 3.

### Step 4 — Apply the pending verdicts

For each pending verdict, in verdict order:

- Move the named row's `tier` cell by one step in the verdict's direction (`promote` 3→2→1,
  `demote` 1→2→3). `hold` moves nothing and is applied by doing nothing.
- Add the verdict's `#v<n>` to the row's `verdicts` column.
- State the change in the report, one line: `cs224n-2024 2 → 1 (#v3, case-0001.md [none])`.

A verdict whose evidence pointer does not resolve to a file is **not applied**; report it and leave
the row alone. An unresolvable pointer is a bug in the skill that wrote it.

A `promote` on a row already at tier 1, or a `demote` on tier 3, is applied as a `hold`: record
that it saturated rather than silently dropping it.

**Opposing verdicts on the same row are normal and both apply, in verdict order.** A source can
carry a chapter and still mis-teach a step — `/archive-materials` writes `hold` from the chapter,
`/reflect` writes `demote` from the error cluster, and both are true. Apply them in id order and
report the net movement with both pointers:

```text
fx-vaswani 1 → 2 (#v4 demote, case-0001.md [hint]; #v5 hold, attention.md § 1.2 — net: demoted)
```

Never average them, never drop one as "contradicted". A row that both carried a piece and
mis-taught a step is exactly the row whose tier the author should look at.

### Step 5 — Refresh `verified`

Only for rows this run actually checked. A URL that resolves gets today's date; a URL that 404s
keeps its old date and gains `(dead)` in its `source` cell. Rows you did not check keep their date
untouched — a refreshed date you did not earn is worse than a stale one.

Local rows (a path under the archive) are checked by testing the path exists.

### Step 6 — Report

- New rows, with the **proposed** tier and the one-line why for each. This is the list the author
  argues with; the cells still say `unrated`.
- Verdicts applied, with the tier movement each caused.
- Verdicts not applied, and why.
- `verified` refreshed / dead / untouched counts.
- `materials.md` rows still at `source-id: —` after this run.

## Contract test

Given a seeded `sources/<domain>.md` and a `materials.md` with two unregistered sources: every
appended row has `tier: unrated`, a `kind`, a non-empty `domains`, and an openable pointer; no
existing row's `id`, `domains`, or `verdicts` column is rewritten; no row is deleted. A pending
`promote` verdict moves its row's tier by exactly one step and adds its `#v<n>` to the row's
`verdicts` column; a verdict whose evidence pointer does not resolve leaves the row unchanged and
is reported; a `tier` cell edited with no verdict behind it is rejected. A second run on the same
fixture appends no rows, applies no verdicts twice, and changes no tier — the file is byte-for-byte
identical apart from `verified` dates and `Last updated`. Only `sources/<domain>.md` is written.

## Handoffs

**In:** a domain name; `sources/<domain>.md` if it exists; `materials.md` rows at `source-id: —`;
verdicts appended by `/archive-materials` and `/reflect` since the last run.

**Out:**
- Registry current → `/survey <topic>` can run its Scope section.
- New rows registered → `/map-materials` can resolve `source-id` on its next run.
- Tier movements applied → the next `/survey` sees the demotion without being told.

## Boundaries

- vs `/survey`: this **finds and ranks** sources across topics; survey **scopes** them for one
  mission (`DEEP`/`SKIM`/`SKIP`). Survey never discovers; this never scopes.
- vs `/map-materials`: that maps files inside one archive; this maps sources across archives. The
  join is the `source-id` column.
- vs `llm-wiki-ingest`: that fetches and distills a source into pages. This only lists it.
- vs `/reflect` and `/archive-materials`: those write verdicts from evidence. This applies them.
  The skill that observes and the skill that changes the tier are deliberately different.
