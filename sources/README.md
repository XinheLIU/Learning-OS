# Sources — the cross-topic registry

Last updated: 2026-09-28

One tiered registry of **sources**, shared by every topic. A source is a thing you could read or
watch: a course, a textbook, a paper, a documentation site, a blog. Tiers say how much a source's
word is worth; verdicts say why, and are the only thing that moves a tier.

The registry is cross-topic on purpose. A tier is a property of the source, not of one learning
run — CS224n is tier 1 whether you are learning Transformers or tokenization. Per-topic decisions
(what to read *for this mission*) belong to `/survey`'s Scope section, and per-file decisions
belong to the archive's `materials.md`.

```text
sources/
├── README.md              # tracked: this file — schema, tier rules, verdict format
└── <domain>.md            # gitignored: machine-learning.md, reinforcement-learning.md, …
```

`<domain>` is a field, not a topic slug: `machine-learning`, not `transformer`. Domains are coarse
enough that tiers stay stable and few enough that a human can list them.

## Who writes it

| Action | Skill | Rule |
| :--- | :--- | :--- |
| Append a row | `/curate-sources` | always as `unrated`, with a *proposed* tier in the why line |
| Refresh `verified` | `/curate-sources` | only rows the run actually checked |
| Change a `tier` cell | `/curate-sources` | only by applying a verdict that is not yet applied |
| Append a verdict | `/archive-materials`, `/reflect` | evidence pointer required; never touches `tier` |
| Read | `/survey`, `/curate-sources`, `frame` | — |

No skill deletes a row. A source that turned out useless is demoted with a verdict, not removed;
the demotion is the useful record.

## File shape

One domain file, two sections in this order.

````markdown
# Sources — machine-learning

Last updated: YYYY-MM-DD

## Registry

| id | source | kind | tier | domains | verified | verdicts |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| cs224n-2024 | Stanford CS224n, Winter 2024 — lectures + notes | course | 1 | nlp, transformer | 2026-09-28 | #v3 |
| blog-x | … | blog | unrated | transformer | — | — |

## Verdicts

- `#v3 2026-09-28 cs224n-2024 promote learning/transformer/case-0001.md [none] — lecture 8 was the
  only source that made the √d_k argument land.`
````

## Columns

| Column | Rule |
| :-- | :-- |
| `id` | lowercase kebab, unique within the file, stable forever. Referenced by `materials.md` `source-id` and by `/survey`'s Scope. Never renumber |
| `source` | the human name, enough to find it again: title, author or institution, edition or year |
| `kind` | `course` \| `textbook` \| `paper` \| `docs` \| `blog` \| `video` \| `code` \| `link-list` |
| `tier` | `1` \| `2` \| `3` \| `unrated`. Entry state is always `unrated` |
| `domains` | comma-separated; free text, but reuse an existing value before inventing one |
| `verified` | last date a human or a skill confirmed the source is live and current. `—` when never checked |
| `verdicts` | the `#v<n>` ids that touched this row, comma-separated. `—` when none |

A row also needs a pointer to the thing itself — a URL in the `source` cell, or a path when the
source is local. A row nobody can open is not a source.

## Tier rules

- **Tier 1 — open, timely, authoritative.** University open courses, canonical textbooks, primary
  papers. You would cite it in writing and trust it against your own memory.
- **Tier 2 — reputable secondary.** Well-cited surveys, maintained official docs, known
  practitioner blogs. Good enough to learn from, not good enough to settle a dispute.
- **Tier 3 — useful once.** It taught you something and you would not send it to anyone else.
- **unrated** — the entry state for every new find. A skill may *propose* a tier in the why line;
  only an applied verdict writes the cell.

**No verdict, no tier change.** A tier cell that moved without a verdict citing evidence is a
contract violation, and `/curate-sources`'s contract test rejects it.

## Verdict format

One line per verdict, under `## Verdicts`, newest last:

```text
#v<n> <date> <source-id> <promote|demote|hold> <evidence pointer> — <one line>
```

- `<n>` increments across the whole file and is never reused.
- `<evidence pointer>` is a path into `learning/<slug>/` or `drafts/<piece>/`, with an assistance
  level in brackets when it comes from learner evidence: `case-0002.md [hint]`. The one exception
  is `author-judgment`, used for rows seeded from the author's own prior ranking — evidence that
  predates the system.
- `hold` is a real verdict. "This source was used and it held up" is what keeps a tier 1 honest.

A verdict is **proposed** when written and **applied** when `/curate-sources` next runs and moves
the `tier` cell. Until then the row's tier is unchanged and the verdict is still listed — that lag
is intentional, so that the skill that changes a tier is the one that reads the whole file.

## Boundaries

- vs `materials.md` (in the archive): this ranks *sources*; that maps *files*. A `materials.md` row
  points at a registry `id` via its `source-id` column; the registry never lists individual files.
- vs `/survey`'s Scope: this says how much a source is worth in general; Scope says whether this
  mission reads it (`DEEP` / `SKIM` / `SKIP`). A tier-1 source is often a SKIP.
- vs `wiki/`: the wiki distills a source's content. This records the source's standing.
