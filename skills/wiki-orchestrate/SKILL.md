---
name: wiki-orchestrate
description: Orchestrate the full wiki pipeline end-to-end — ingest, lint, regenerate index, suggest schema, and sanity-check with a query.
---

# Wiki Orchestrator

Run the complete wiki pipeline: ingest sources, scan for issues, apply fixes, regenerate the index, suggest schema improvements, and verify with a test query.

## Skill Map

| Step | Skill | What it does |
|------|-------|-------------|
| 1. Ingest | wiki-ingest-source / wiki-ingest-folder | Extract entities/concepts from notes into wiki pages |
| 2. Lint | wiki-lint | Scan for duplicates, dead links, empty pages, orphans, missing aliases |
| 3. Fix | wiki-lint (fix mode) | LLM-powered repair of lint issues |
| 4. Index | wiki-regenerate-index | Rebuild index.md from all pages |
| 5. Schema | wiki-suggest-schema | Propose schema improvements |
| 6. Query | wiki-query | Sanity-check with a test question |

## Wiki Conventions (summary)

All skills follow these conventions:

- **Wiki root**: `{wiki}/` directory (default: `wiki/`)
- **Slug**: strip special chars `/\:*?"<>|,()'、，。；：！？（）【】《》`, replace spaces with `-`, preserve CJK
- **Frontmatter**: `type` (entity/concept/source), `tags`, `created`, `updated`, `sources`, `aliases`, `reviewed`
- **Wiki-links**: `[[entities/slug|Display]]`, `[[concepts/slug|Display]]`, `[[sources/slug|Display]]`
- **Write gate**: display text must not repeat folder prefix; paths must not duplicate folder name
- **Reviewed pages**: pages with `reviewed: true` are protected — never overwritten, append-only
- **Language**: wiki content in EN or CN; entity/concept names in original source language

## Common Workflows

### Bootstrap a New Wiki from a Folder

1. Ingest all `.md` files in the folder (wiki-ingest-folder)
2. Lint scan → review report
3. Lint fix (optional, if issues found)
4. Schema suggestions → human review
5. Test query to verify

### Ingest a Single File

1. Ingest the file (wiki-ingest-source)
2. Regenerate index
3. Optional: lint scan + query test

### Health Check Only

1. Lint scan → review report
2. Apply fixes selectively

## Procedure

### 1. Verify Setup

Confirm the source material exists (folder or file) and the vault root is accessible. The wiki directory is created automatically if missing.

### 2. Ingestion

**Folder mode (default):** apply the wiki-ingest-folder procedure — collect all `.md` files (excluding `{wiki}/` and `.obsidian/`), skip already-ingested, ingest each serially.

**Single file mode:** apply the wiki-ingest-source procedure for one file.

### 3. Regenerate Index

Always rebuild `{wiki}/index.md` after ingestion to reflect all new pages.

### 4. Lint Scan

Apply wiki-lint scan phase. Review the report:
- Missing aliases → run fix
- Duplicates → run fix (carefully — reviewed pages are protected)
- Dead links → run fix
- Empty pages → run fix
- Orphans → run fix
- Polluted basenames → fix manually

### 5. Lint Fix (Optional)

Apply wiki-lint fix phase for detected issues. Review changes after.

### 6. Schema Suggestions

Apply wiki-suggest-schema with context from lint results (e.g., "After lint: found 3 duplicate pairs, consider adding naming convention rules").

### 7. Human Review Gate

- Review `{wiki}/schema/suggestions.md`
- If suggestions are accepted, manually edit `{wiki}/schema/config.md`
- Never auto-apply schema changes

### 8. Sanity Check Query

Ask a test question via wiki-query to verify the wiki works:
- "What are the main topics covered in this wiki?"
- Or a domain-specific question based on the ingested content
- Verify answers include proper `[[wiki-links]]`

### 9. Summary

Report: total pages, entities/concepts/sources counts, lint status, schema suggestions (yes/no), query test result.
