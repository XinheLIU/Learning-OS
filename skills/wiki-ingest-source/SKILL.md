---
name: wiki-ingest-source
description: Ingest a single markdown note into a structured wiki — extract entities and concepts, write entity/concept/source pages with cross-links and aliases.
---

# Ingest Single Source

Read a markdown note and extract entities (people, organizations, projects, products, events, locations) and concepts (theories, methods, technologies, terms) into a structured wiki with cross-linked pages.

## Wiki Directory Layout

```
{wiki}/                          # default: wiki/
├── entities/{slug}.md           # type: entity
├── concepts/{slug}.md           # type: concept
├── sources/{slug}.md            # type: source (summary of ingested note)
├── schema/
│   ├── config.md                # co-evolved rules (human-reviewed)
│   └── suggestions.md           # LLM proposals (append-only)
├── contradictions/{slug}.md
├── index.md                     # auto-generated listing
└── log.md                       # operation log
```

User source notes live **outside** `{wiki}/`.

## Slug Rules

```
slugify(name):
  1. Trim whitespace; if empty → "untitled"
  2. Remove: /\:*?"<>|,()'、，。；：！？（）【】《》 and ASCII control chars
  3. Replace spaces/dots with "-", collapse multiple "-", trim leading/trailing "-"
  4. Preserve CJK and other Unicode letters
```

## Frontmatter Schema

| Field | Values | Notes |
|-------|--------|-------|
| `type` | `entity` / `concept` / `source` | Required |
| `tags` | entity: `person` `organization` `project` `product` `event` `location` `other`; concept: `theory` `method` `technology` `term` `other` | Required |
| `created` | ISO date (YYYY-MM-DD) | Required on new pages |
| `updated` | ISO date | Set on merge |
| `sources` | YAML list of wiki-links to source pages | |
| `aliases` | YAML list of strings | 1+ required for entities/concepts |
| `reviewed` | `true` | If set, page is protected on re-ingest |

## Wiki-Link Format

```
[[entities/{slug}|Display Name]]
[[concepts/{slug}|Display Name]]
[[sources/{slug}|Display Name]]
```

Correct: `[[entities/Qwen|Qwen]]`
Wrong: `[[entities/Qwen|entities/Qwen]]` — display text must NOT repeat folder prefix
Wrong: `[[concepts/conceptsLayout|Layout]]` — path must NOT contain duplicated folder prefix

## Write Gate (apply before every write)

1. Display text after `|` must NOT contain `entities/`, `concepts/`, or `sources/` prefixes
2. Path segment must NOT duplicate the folder name (e.g., `entities/entitiesFoo`)
3. Basenames (file names) must NOT contain `/` or `\`

## Section Labels (EN / CN)

Use the language matching the wiki content language (default: EN).

| Key | EN | CN |
|-----|----|----|
| basic_information | Basic Information | 基本信息 |
| description | Description | 描述 |
| related_content | Related Content | 相关内容 |
| mentions_in_source | Mentions in Source | 来源提及 |
| new_information | New Information | 新信息 |
| definition | Definition | 定义 |
| key_characteristics | Key Characteristics | 关键特征 |
| applications | Applications | 应用 |
| related_concepts | Related Concepts | 相关概念 |
| related_entities | Related Entities | 相关实体 |
| source | Source | 来源 |
| core_content | Core Content | 核心内容 |
| key_entities | Key Entities | 关键实体 |
| key_concepts | Key Concepts | 关键概念 |
| main_points | Main Points | 要点 |
| resolved_contradictions | Resolved Contradictions | 已解决的矛盾 |
| new_claim | New Claim | 新主张 |
| existing_knowledge | Existing Knowledge | 已有知识 |
| resolution_suggestion | Resolution Suggestion | 解决建议 |
| source_page | Source Page | 来源页面 |
| related_pages | Related Pages | 相关页面 |
| updated | Updated | 更新于 |

## Entity Types

`person` `organization` `project` `product` `event` `location` `other`

## Concept Types

`theory` `method` `technology` `term` `other`

## Extraction Granularity

| Level | Batch size | Total cap |
|-------|-----------|-----------|
| `fine` | 30 | 100 |
| `standard` | 20 | 50 |
| `coarse` | 10 | 10 |
| `minimal` | 5 | 5 |

Default: `standard`. Adaptive batching: if any LLM response exceeds ~70% of output tokens, reduce batch size by 25% (min 5) for next round.

## Procedure

### 1. Ensure Wiki Structure

Create directories if missing: `{wiki}/entities`, `{wiki}/concepts`, `{wiki}/sources`, `{wiki}/schema`, `{wiki}/contradictions`.

Create `{wiki}/schema/config.md` if missing:
```markdown
# Wiki Schema Configuration
version: 1
# Add naming conventions, type rules, and templates below.
```

Create `{wiki}/log.md` if missing.

### 2. Read Source File

Read the target `.md` file. Note if it exceeds ~1000 lines (may need more batches).

### 3. List Existing Wiki Pages

Scan `{wiki}/entities/*.md`, `{wiki}/concepts/*.md`, `{wiki}/sources/*.md`. For each, extract: slug, title, wiki-link path, aliases (from frontmatter), type, tags. This list is used for deduplication and cross-linking in step 4.

### 4. Iterative Source Analysis

Extract entities and concepts from the source in batches. Each batch is one LLM call.

**Round 1 prompt** — provide: source content (first batch), existing pages list, granularity config, language directive ("Write ALL wiki content in {lang}"), section labels in the target language. Ask for:

```json
{
  "source_title": "string",
  "summary": "2-4 sentence overview",
  "key_points": ["point 1", "point 2", ...],
  "entities": [
    {
      "name": "Original Name (never translate)",
      "type": "person|organization|project|product|event|location|other",
      "summary": "4-6 sentence description",
      "mentions_in_source": ["verbatim quote 1", "verbatim quote 2"],
      "aliases": ["alias1", "alias2"],
      "related_entities": ["entity name"],
      "related_concepts": ["concept name"]
    }
  ],
  "concepts": [
    {
      "name": "Original Name (never translate)",
      "type": "theory|method|technology|term|other",
      "summary": "4-6 sentence description",
      "mentions_in_source": ["verbatim quote 1", "verbatim quote 2"],
      "aliases": ["alias1", "alias2"],
      "related_entities": ["entity name"],
      "related_concepts": ["concept name"]
    }
  ],
  "contradictions": [
    {
      "new_claim": "claim text",
      "existing_knowledge": "what was previously known",
      "resolution_suggestion": "how to resolve"
    }
  ],
  "more_remaining": true
}
```

**Round N prompt** — provide remaining source content + list of already-extracted entity/concept names. Set `more_remaining: false` when done.

**Stop conditions**: LLM returns empty arrays, all items are duplicates, or total cap reached.

**Critical rules**:
- Entity/concept NAMES must stay in the original source language — never translate names
- `mentions_in_source` must be verbatim quotes from the source (2-4 per item)
- `aliases` must include translations, abbreviations, alternate spellings, full forms

### 5. Write Source Summary Page

Path: `{wiki}/sources/{slugify(source_filename)}.md`

Frontmatter:
```yaml
---
type: source
tags: []
created: YYYY-MM-DD
aliases: [alias1, alias2]
---
```

Body sections (using section labels in the wiki language):
- **Source**: original file path
- **Core Content**: 100-200 word summary
- **Key Entities**: bullet list with `[[entities/slug|name]]` links
- **Key Concepts**: bullet list with `[[concepts/slug|name]]` links
- **Main Points**: numbered list of key takeaways

### 6. Process Each Entity and Concept

For each extracted item, run with concurrency (default: 3 at a time):

#### 6a. Resolve Page Path

1. Compute `slug = slugify(name)`, build candidate path `{wiki}/{entities|concepts}/{slug}.md`
2. Check if candidate exists on disk — if yes, done
3. Check existing pages' aliases for a match — if found, use that path
4. If still ambiguous, use LLM semantic dedup: provide the name + existing page list, ask for `{"match": true/false, "path": "..."}`. If no match, use the candidate path from step 1.

#### 6b. Determine Merge Mode

- **No existing page** → generate from scratch (mode: NEW)
- **Existing page with `reviewed: true`** → append-only, preserve existing body (mode: REVIEWED)
- **Existing page without `reviewed: true`** → full incremental merge (mode: MERGE)

#### 6c. Generate or Merge

**NEW — Entity page template:**

Frontmatter:
```yaml
---
type: entity
tags: [person|organization|project|product|event|location|other]
created: YYYY-MM-DD
sources:
  - "[[sources/{source_slug}|source title]]"
aliases: [alias1, alias2]
---
```

Body sections: Basic Information, Description, Related Entities, Related Concepts, Mentions in Source (with verbatim quotes using `>` blockquotes).

**NEW — Concept page template:**

Frontmatter:
```yaml
---
type: concept
tags: [theory|method|technology|term|other]
created: YYYY-MM-DD
sources:
  - "[[sources/{source_slug}|source title]]"
aliases: [alias1, alias2]
---
```

Body sections: Definition, Key Characteristics, Applications, Related Concepts, Related Entities, Mentions in Source.

**REVIEWED — Append-only:**

Keep all existing content. If there is genuinely new information not already covered, append a "New Information" section (use the section label) at the end. Do NOT modify existing sections.

**MERGE — Incremental merge:**

Add new source to the `sources` list in frontmatter. Set `updated: YYYY-MM-DD`. Integrate new information into existing body sections; preserve all existing content. If contradictions are detected, add a note under "Resolved Contradictions".

#### 6d. Write Page

- Apply write gate checks before writing
- Verify `type` field is correct (entity vs concept)
- Verify at least 1 alias present
- All wiki-links must use correct format

### 7. Regenerate Index

Rebuild `{wiki}/index.md` from all current entity, concept, and source pages (see wiki-regenerate-index skill).

### 8. Append to Log

Add entry to `{wiki}/log.md`:
```markdown
- **{date}** — Ingested `{source_path}`: created [{page_list}], updated [{page_list}]
```

### 9. Output Report

Return a summary: source path, source title, created pages (list), updated pages (list), entity count, concept count, contradiction count.
