---
name: llm-wiki
description: "Karpathy's LLM Wiki: ingest articles, papers, transcripts, or pasted text and build an interlinked knowledge base. Use when the user wants to process a source into the wiki, add knowledge, ask domain questions, or mentions 'wiki', 'knowledge base', or 'KB'. Use even when the user doesn't explicitly say 'wiki' if they appear to be working within an existing wiki directory (SCHEMA.md, index.md, log.md present)."
version: 3.0.0
author: Xinhe Liu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wiki, knowledge-base, research, notes, markdown]
    category: research
    related_skills: [llm-wiki-init, llm-wiki-lint, obsidian, arxiv]
---

# Karpathy's LLM Wiki — Ingest & Query

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

**See also:** `llm-wiki-init` (first-time setup) · `llm-wiki-lint` (health checks & audit)

**Division of labor:** The human curates sources and directs analysis. The agent
summarizes, cross-references, files, and maintains consistency.

## When This Skill Activates

- Asking to ingest, add, or process a source into the wiki
- Asking a question when a wiki exists at the configured path
- References to "wiki", "knowledge base", or "notes" in a research context

## Wiki Location

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
```

The wiki is a directory of markdown files — open it in Obsidian, VS Code, or any editor.

## Architecture

```
wiki/
├── SCHEMA.md           # Conventions, structure rules, domain config
├── index.md            # Content catalog with one-line summaries
├── log.md              # Chronological action log (append-only)
├── raw/                # Layer 1: Immutable source material
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/           # Layer 2: People, orgs, products, models
├── concepts/           # Layer 2: Topic/concept pages
├── comparisons/        # Layer 2: Side-by-side analyses
└── queries/            # Layer 2: Filed query results worth keeping
```

**Layer 1 — Raw Sources:** Immutable. Read but never modified.
**Layer 2 — The Wiki:** Agent-owned markdown. Created, updated, cross-referenced.

## Orientation (every session — do this first)

Before doing anything with an existing wiki:

① Read `SCHEMA.md` — conventions and tag taxonomy.
② Read `index.md` — what pages exist and their summaries.
③ Scan last 20-30 lines of `log.md` — recent activity.

For wikis with 100+ pages, also `search_files` for the topic at hand before creating anything.
Skipping orientation causes duplicates, missed cross-references, and repeated work.

## Ingest

When the user provides a source (URL, file, paste):

① **Capture the raw source:**
   - URL → `web_extract`, save to `raw/articles/`
   - PDF → `web_extract`, save to `raw/papers/`
   - Pasted text → appropriate `raw/` subdirectory
   - Name descriptively: `raw/articles/karpathy-llm-wiki-2026.md`
   - Add raw frontmatter (`source_url`, `ingested`, `sha256` of body — everything after closing `---`).
   - **sha256 fallback chain:** (1) Try Bash: `shasum -a 256 "$file"`. (2) If Bash denied, skip the hash computation and note in the log entry "sha256: not computed (Bash unavailable)". (3) If the file has no YAML frontmatter at all, prepend one using Write (rewrite the file with frontmatter + original content) — this is an exception to the "never modify raw" rule since frontmatter is metadata, not content.
   - On re-ingest of the same URL: recompute sha256 — skip if unchanged, flag drift if different.

② **Discuss takeaways** — share the most interesting/surprising claims with the user before
   writing anything. This is where human judgment shapes what gets filed and how.
   *(In batch/cron mode: log 1-2 key takeaways in the log entry instead.)*

③ **Check what exists** — search `index.md` and `search_files` for entities/concepts
   mentioned in the source. This is the difference between a growing wiki and a pile of duplicates.

④ **For long sources (>~100 lines or >2 major sections) — two-pass parallel ingest:**

   **Pass 1 — extract (parallel across chunks):**
   Split by H2 headings (or ~80-line windows if no headings). One agent per chunk:
   > "Scan this chunk. List every entity and concept mentioned — names, dates, key claims.
   > Output the list only, no analysis.
   > When the source is in Chinese: extract entity names in Chinese first, append English
   > equivalents in parentheses. Use the most commonly referenced form as the canonical name."
   Merge all lists into a unified entity/concept inventory.

   **Pass 2 — write (parallel across chunks):**
   One agent per chunk, with the full inventory as context:
   > "Process this chunk. Full entity list from all chunks: [inventory].
   > Write or update wiki pages for entities/concepts in your chunk."
   Final synthesis agent: read all Pass 2 outputs, resolve cross-chunk contradictions.

   For short sources, a single agent is fine.

⑤ **Write or update wiki pages:**
   - **New pages:** Create only if entity/concept meets Page Thresholds in SCHEMA.md
     (2+ source mentions, or central to one source)
   - **Filename convention:** Default to English lowercase-hyphen slugs per SCHEMA.md
     (`economic-rent.md`, not `经济租.md`). If the source material is predominantly Chinese
     and the domain's natural working language is Chinese, **ask the user** before switching to
     Chinese filenames. Never mix conventions — check existing pages in `index.md` and match.
   - **Page threshold:** If an entity/person is mentioned in only 1 source and has fewer than
     3 distinct claims about them, fold the claims into the most relevant concept page rather
     than creating a dedicated entity page.
   - **Existing pages:** Add new info, bump `updated`, follow the Update Policy for contradictions
   - **Cross-references:** Every new/updated page links to ≥2 others via `[[wikilinks]]`
   - **Tags:** Only from the taxonomy in SCHEMA.md — add new tags there first
   - **Provenance:** On pages synthesizing 3+ sources, append `^[raw/articles/source.md]`
     markers to paragraphs whose claims trace to a specific source
   - **Confidence:** For opinion-heavy or single-source claims, set `confidence: medium` or `low`

⑥ **Update navigation:**
   - Add new pages to `index.md` alphabetically under the correct section
   - Bump "Total pages" count and "Last updated" date in the index header
   - Append to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`
   - List every file created or updated in the log entry

⑦ **Report** every file created or updated to the user.

### Differential Ingest (new raws added to existing wiki)

When new raw files have been dropped into an existing wiki:

1. **Find unprocessed raws** — diff `raw/` against `log.md` ingest entries:
   ```bash
   # Files mentioned in log ingest entries
   grep "## \[.*\] ingest" "$WIKI/log.md" | grep -oE "raw/[^[:space:]]+"
   # Files in raw/ but not in the above list = unprocessed
   ```
2. **Ingest only the unprocessed files** using the flow above.
3. **Update existing wiki pages** touched by the new raws — add info, bump `updated`,
   follow contradiction policy. Do not re-read old raws.
4. **Never re-process** a raw file that appears in log.md with an `ingest` entry and whose
   sha256 is unchanged.

`sha256` on all raw files enables skip logic on re-ingest — see the fallback chain in step ① for when Bash is unavailable.

### Bulk Ingest

When ingesting multiple sources at once:

1. Read all sources.
2. **Note the 1-2 most interesting/surprising claims per source. Report to the user before
   writing any pages** — this shapes emphasis and catches contradictions early.
3. Run Pass 1 (entity extraction) across all sources in parallel. For each source that is
   long (>~100 lines or >2 major sections), split it by H2 headings (or ~80-line windows)
   and run one sub-agent per chunk:
   > "Scan this chunk. List every entity and concept mentioned — names, dates, key claims.
   > Output the list only, no analysis.
   > When the source is in Chinese: extract entity names in Chinese first, append English
   > equivalents in parentheses."
   For short sources, a single agent per source is fine.
4. Merge entity lists; check existing pages for all of them in one search pass.
5. Run Pass 2 (write pages) in parallel.
6. Update `index.md` once at the end.
7. Write a single log entry covering the batch.

## Query

When the user asks a question about the wiki's domain:

① Read `index.md` to identify relevant pages.
② For wikis with 100+ pages, also `search_files` across all `.md` files for key terms.
③ Read the relevant pages.
④ Synthesize an answer from compiled knowledge. Cite pages: "Based on [[page-a]] and [[page-b]]..."
⑤ **File valuable answers back:**
   - Outputs can take any form — markdown summaries, comparison tables, Marp slides, or charts.
   - `queries/` is for specific one-off answers worth preserving.
   - If the answer reveals something generalizable about the domain, create a `concepts/` page
     instead and link to it from the query result.
   - Don't file trivial lookups — only answers painful to re-derive.
⑥ Append to `log.md`: `## [YYYY-MM-DD] query | Question (filed: yes/no)`

## Git Integration

The wiki directory works as a git repo — version history and collaboration come free.

```bash
cd "$WIKI"
git init
printf ".obsidian/workspace*\n.obsidian/plugins/\n" >> .gitignore
```

Commit message convention:
- `ingest: <source title>`
- `update: <page name>`
- `lint: N issues found`

Obsidian Sync and git coexist fine — git tracks the markdown; Sync handles cross-device access.

## Obsidian Integration

The wiki directory works as an Obsidian vault out of the box:
- `[[wikilinks]]` render as clickable links; Graph View visualizes the network
- YAML frontmatter powers Dataview queries
- `raw/assets/` holds images referenced via `![[image.png]]`

Use **Obsidian Web Clipper** (browser extension) to clip web articles directly to `raw/articles/`
— cleaner than programmatic extraction for complex pages.

For image-heavy sources: save images to `raw/assets/` and reference by filename. Process text
first; read images in a second pass only if the text is insufficient.

## Related Tools

- **qmd** — local markdown search with BM25/vector hybrid and LLM re-ranking (CLI + MCP server).
  Use when the wiki exceeds ~100 pages and keyword grep starts missing semantically relevant content.
- **llm-wiki-compiler** — Node.js CLI for batch compile of a source directory without agent
  curation. Use when you want scheduled/CLI-driven pipeline; skip when you want human-in-the-loop.

## Pitfalls

- **Never modify `raw/` content** — sources are immutable. The only exception: prepending YAML frontmatter with `sha256`/`source_url`/`ingested` fields, which is metadata, not content.
- **Always orient first** — SCHEMA + index + recent log before any operation. Skipping causes duplicates.
- **Always update `index.md` and `log.md`** — these are the navigational backbone.
- **Don't create pages for passing mentions** — an entity mentioned in only 1 source with <3 distinct claims should be folded into a concept page, not given its own entity page. Follow Page Thresholds in SCHEMA.md.
- **Don't create pages without cross-references** — every page links to ≥2 others.
- **Frontmatter is required** — enables search, filtering, staleness detection.
- **Tags must come from the taxonomy** — add to SCHEMA.md first, then use.
- **Ask before mass-updating** — if an ingest touches 10+ existing pages, confirm scope first.
- **Handle contradictions explicitly** — note both claims with dates, mark frontmatter, flag for user.
