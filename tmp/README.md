# tmp/ — Iteration Corpus

Last updated: 2026-08-30

This directory is the testing set for iterating **pipeline** (preprocessing) and **writing** skills against real material. Everything here except this README is gitignored — raw course materials may be copyright-sensitive and are never published with the repo.

## Convention

One folder per source material, mirroring the pipeline end to end:

```text
tmp/<material-slug>/
├── raw/       # untouched source dumps (transcripts, scraped notes, mixed-language)
├── notes/     # processed course notes (clean, structured, claims sourced)
├── wiki/      # distilled pages (optional)
└── drafts/    # writing-output iterations
```

Rules:

- `raw/` is immutable — skills read it, never edit it. Each capture carries its provenance (source URL, capture date, medium) per the [pipeline intake conventions](../skills/pipeline/README.md).
- Each later stage is produced from the previous one by a skill under test. A skill is judged by whether it moves a material **one stage to the right, fast, without losing provenance**.
- Keep failed attempts: a bad `notes/` or `drafts/` output is a non-compliant fixture worth diffing against the next iteration.

## Materials

| Slug | Source | Stage reached |
| :--- | :--- | :--- |
| `learning-how-to-learn` | Coursera *Learning How to Learn* (bilingual video notes) | notes (`clean-notes`, 2026-08-30) |
