# The Information Pipeline

Last updated: 2026-09-01

**Gather → process → distill: turn raw material into teaching-ready knowledge before it enters the learning system.**

The pipeline is the input stage of Learning OS. It exists because raw material — video transcripts, scraped articles, bilingual course notes, loose document folders — is not usable for learning or writing as-is. The pipeline's job is to move material through three stages without losing provenance, so the [learning loop](../learning/README.md) gets grounded teaching material and the [writing system](../writing/README.md) gets citable sources.

## The three stages

```text
gather                    process                     distill
raw capture       →       clean, structured notes  →  source-faithful knowledge
(dumps, transcripts,      (navigable, sourced,        (wiki pages, comparisons,
 mixed language)           claims separated)           book plans)
```

| Stage | What it guarantees | Skills today |
| :--- | :--- | :--- |
| Gather | Nothing is captured without provenance: source, capture date, medium | intake conventions (below); capture is mostly manual today |
| Process | Material is clean, navigable, and attributable; the source's claims are separated from the note-taker's commentary | `clean-notes` (inside one material), `organize-docs` (across a collection) |
| Distill | Knowledge is compressed into source-faithful, linkable pages that can teach | `llm-wiki-init`, `llm-wiki-ingest`, `llm-wiki-lint`, `llm-wiki-book` |

The layer layout that mirrors these stages on disk is a convention, not a skill — see [Project layout](#project-layout) below.

## The Skills

| Component | Skill | Primary responsibility | Durable output |
| :--- | :--- | :--- | :--- |
| Note processor | `clean-notes` | Clean one material's raw capture: cluster by topic, dedupe, fix formatting | `notes/<slug>.md` |
| Document organizer | `organize-docs` | Restructure document collections into a MECE system | organized tree and index |
| Wiki bootstrap | `llm-wiki-init` | Scaffold a new external knowledge base | `wiki/` skeleton |
| Knowledge distillation | `llm-wiki-ingest` | Preserve and distill curated sources | `raw/`, source-faithful pages |
| Wiki maintenance | `llm-wiki-lint` | Audit links, orphans, drift, and tag sprawl | audit reports |
| Book planner | `llm-wiki-book` | Turn a mature wiki into a thesis and narrative plan | book plan document |

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

## Planned skills

| Task | Skill (working name) | Stage |
| :--- | :--- | :--- |
| Capture a source into `raw/` with provenance attached (URL fetch, transcript pull, rights note) | `capture-source` | gather |

Planned work is iterated against the `tmp/` corpus, per the [project layout](#project-layout) above. Remaining repository work is tracked in [`docs/exec-plans/repository.md`](../../docs/exec-plans/repository.md).
