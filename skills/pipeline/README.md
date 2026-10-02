# The Information Pipeline

Last updated: 2026-10-01

**Gather → process → scope → build: decide what is worth learning, and from what, before the learning loop starts.**

The pipeline is the input stage of Learning OS. It exists because raw material — video transcripts, scraped articles, course PDFs, loose document folders — is not usable for learning or writing as-is, and because *deciding what to learn* is planning work, not iteration. The pipeline moves material through four stages without losing provenance, so the [learning loop](../learning/README.md) receives a scoped plan over ranked material and the [writing system](../writing/README.md) gets citable sources.

## The four stages

```text
gather              process                 scope                build
raw capture    →    ranked material    →    what enters,     →   the course
+ registered        + tiered sources        how deep             (critical path,
  sources                                                         lessons)
```

| Stage | What it guarantees | Skills |
| :--- | :--- | :--- |
| Gather | Nothing is used without provenance: a source has a registry row, a capture has source, date, and medium | `/curate-sources` (the registry); intake conventions (below) |
| Process | Every file in an archive is ranked once, for every downstream reader; every note is readable | `/map-materials` (across an archive), `clean-notes` (inside one file), `organize-docs` (across a collection) |
| Scope | The mission's sources are dispositioned and every concept is `deep` or `connect` | `/survey` |
| Build | The deep nodes are ordered into one critical path and authored as a course | `/curriculum` |
| Distill *(optional)* | Knowledge is compressed into source-faithful, linkable pages that can teach | `llm-wiki-init`, `llm-wiki-ingest`, `llm-wiki-lint`, `llm-wiki-book` |

**Why planning lives here and not in the learning loop.** `/survey` and `/curriculum` decide what enters and in what order; they do not iterate. The learning loop is the set of skills that run again and again over the same topic memory — `/learn`, `/recall`, `/practice`, `/evaluate`, `/reflect`. Keeping a skill that runs once next to skills that run fifty times made the loop's boundary unreadable: see [ADR-010](../../docs/adr.md).

The layer layout that mirrors these stages on disk is a convention, not a skill — see [Project layout](#project-layout) below.

## The Skills

| Component | Skill | Primary responsibility | Durable output |
| :--- | :--- | :--- | :--- |
| Source curator | `/curate-sources` | Discover sources for a domain, tier them, apply pending verdicts | `sources/<domain>.md` |
| Material mapper | `/map-materials` | Rank one archive's files once: key / redundant / peripheral, plus what each teaches | `<archive>/materials.md` |
| Investment gate | `/survey` | Map the field; disposition every source; set every node's `deep`/`connect` mode | `survey.md`, Structural Memory v0, `learning/index.md` rows |
| Course orchestrator | `/curriculum` | Order the deep nodes into one critical path; build the HTML course | `syllabus.md` (+ `## Critical Path`), the course |
| Note processor | `clean-notes` | Clean one material's raw capture: cluster by topic, dedupe, fix formatting | `notes/<slug>.md` |
| Document organizer | `organize-docs` | Restructure document collections into a MECE system | organized tree and index |
| Materials archivist | `archive-materials` | After a piece ships, fill `used-in` in the map and write source verdicts | `materials.md` `used-in`, registry verdicts |
| Wiki bootstrap | `llm-wiki-init` | Scaffold a new external knowledge base | `wiki/` skeleton |
| Knowledge distillation | `llm-wiki-ingest` | Preserve and distill curated sources | `raw/`, source-faithful pages |
| Wiki maintenance | `llm-wiki-lint` | Audit links, orphans, drift, and tag sprawl | audit reports |
| Book planner | `llm-wiki-book` | Turn a mature wiki into a thesis and narrative plan | book plan document |

**Why the archivist runs last.** `archive-materials` is the only pipeline skill that runs *after*
the writing system, and that ordering is the point: it is the **write-back** that makes the
registry and the map iterate. `/map-materials` ranks the archive on a guess about what will be
useful; `archive-materials` records what a shipped chapter actually used, and turns that into
`used-in` cells and registry verdicts. Without it the registry's tiers never move and the map is a
one-time opinion. It is additive — `used-in` cells, verdicts, and confirmed renames, never a
deletion or a move. When a folder genuinely needs a different shape, that is `organize-docs`, and
it is a separate, explicit decision. Its place in the chapter line is in
[the writing system](../writing/README.md#common-paths). Writing judgments, open questions and
topic connections are owned separately by `snapshot-writing`; that memory does not change tiers
or earned learner edges. `develop-examples` owns pre-draft selection against the material map,
while `frame` only reads it to ground a reader question.

## Wiki layout

The distill stage's canonical store:

```text
wiki/
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
├── entities/
├── concepts/
├── comparisons/
└── queries/
```

## Project layout

One folder per source material, four layers left to right:

```text
<material-slug>/
├── raw/       # untouched source dumps (transcripts, scraped notes, mixed language)
├── notes/     # processed notes — clean, navigable, sourced
├── wiki/      # distilled pages (optional; see Wiki layout above)
└── drafts/    # writing output, one folder per piece: brief.md + draft
```

**Promotion rule:** a layer may read from the layer to its left and write only to itself. Nothing writes leftward — a processed note never edits its `raw/` source, a wiki page never edits notes, a draft never edits the wiki. This is what makes provenance checkable: every claim can be walked back one layer at a time to a `raw/` capture.

**Gitignore:** `raw/` is normally excluded (course materials are usually not republishable, and PDFs are large). `notes/`, `wiki/`, and `drafts/` are tracked. The `tmp/` corpus is gitignored wholesale for that reason — only `tmp/README.md` is tracked.

Materials in this repo live under `tmp/<material-slug>/`. A pipeline or writing skill is judged by whether it moves a material one stage to the right, fast, without losing provenance.

## Intake conventions (gather stage)

Every capture into a `raw/` directory should carry, at minimum:

- **Source:** URL or citation of the original material
- **Captured:** date of capture
- **Medium:** video transcript, article, course notes, book excerpt, …
- **Rights note:** whether the material may be republished (raw course materials are usually not — which is why the `tmp/` corpus is gitignored)

Downstream stages must preserve these; a processed note that cannot say where a claim came from has failed the pipeline.

Publication structure — the book, site, or deck a `drafts/` piece eventually lands in — is not the pipeline's business. That belongs to `build-skeleton` in the [writing system](../writing/README.md).

## Boundaries

- The pipeline produces **teaching material and sources**, never learner evidence. `llm-wiki-*` skills never write to `learning/<slug>/`; a wiki page proves nothing about what the learner can do.
- The learning loop never writes to `wiki/` — distillation stays source-faithful, uncontaminated by the learner's in-progress models.
- The writing system consumes pipeline output (processed notes, wiki pages) as raw material but owns its own drafts.

## The memory the pipeline owns

Two cross-cutting files, both written here and read everywhere:

| File | Scope | Owner | Schema |
| :--- | :--- | :--- | :--- |
| `sources/<domain>.md` | cross-topic | `/curate-sources` (rows, tiers); `/reflect` and `archive-materials` (verdicts) | [`sources/README.md`](../../sources/README.md) |
| `<archive>/materials.md` | per topic | `/map-materials` (rows); `archive-materials` (`used-in`, renames) | [`map-materials/SKILL.md`](map-materials/SKILL.md#the-map) |

They join on `source-id`: a map row says which registered source a file came from. Both are
gitignored — the registry because it is the author's, the map because it lives in the archive,
outside this repository entirely.

## Planned skills

| Task | Skill (working name) | Stage |
| :--- | :--- | :--- |
| Capture a source into `raw/` with provenance attached (URL fetch, transcript pull, rights note) | `capture-source` | gather |

Planned work is iterated against the `tmp/` corpus, per the [project layout](#project-layout) above. Remaining repository work is tracked in [`docs/exec-plans/repository.md`](../../docs/exec-plans/repository.md).
