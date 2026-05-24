---
name: wiki-ingest-folder
description: Batch-ingest all markdown notes in a folder into a structured wiki, skipping already-ingested files.
---

# Ingest Folder

Ingest all markdown files in a folder, processing each one serially through the same extraction pipeline as single-file ingest.

## Already-Ingested Check

For each source file, check whether it has already been ingested before running extraction:

1. Compute `slug = slugify(basename_of_source_file)` using the slug rules below
2. Check if `{wiki}/sources/{slug}.md` exists
3. If it exists, parse its frontmatter and read the `sources` field
4. Normalize brackets in `sources` values (strip `[[` `]]`)
5. If the sources list includes the original source file path → **skip**
6. If the source page exists but has no `sources` field → **skip** (treat as ingested)
7. To force re-ingest of already-ingested files, set flag `force: true`

## Slug Rules (for the check above)

```
slugify(name):
  1. Trim whitespace; if empty → "untitled"
  2. Remove: /\:*?"<>|,()'、，。；：！？（）【】《》 and ASCII control chars
  3. Replace spaces/dots with "-", collapse multiple "-", trim leading/trailing "-"
  4. Preserve CJK and other Unicode letters
```

## Procedure

### 1. Collect Source Files

- Recursively find all `*.md` files under the target folder
- Exclude `{wiki}/` directory and `.obsidian/` directory

### 2. Filter Already-Ingested

Apply the already-ingested check (see above) to each file. Build a list of files that need processing.

### 3. Ingest Each File Serially

For each file that needs processing, apply the **wiki-ingest-source** procedure (ingest single source → extract entities/concepts → write pages).

Process one file at a time (serial, not parallel) to avoid rate-limit issues.

Collect per-file results: ok/failed, pages created, pages updated, entity count, concept count.

### 4. Regenerate Index Once

After all files are processed, regenerate `{wiki}/index.md` once (not after each file).

### 5. Output Batch Report

Return a summary:
- Folder path
- Total files found
- Skipped (already ingested)
- Ingested successfully
- Failed
- Per-file details (path, status, created/updated pages, entity/concept counts)
