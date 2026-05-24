---
name: wiki-regenerate-index
description: Rebuild wiki/index.md from current entity, concept, and source pages — no LLM required, idempotent.
---

# Regenerate Index

Rebuild `{wiki}/index.md` by scanning all existing entity, concept, and source pages. No LLM calls needed — purely programmatic.

## Wiki Structure

```
{wiki}/
├── entities/{slug}.md       # type: entity
├── concepts/{slug}.md       # type: concept
├── sources/{slug}.md        # type: source
└── index.md                 # ← this file
```

## Index Format

```markdown
# Wiki Index

> {subtitle}

## Entities
- [[entities/{slug}|{slug}]] `aliases: a, b` — {summary}
...

## Concepts
- [[concepts/{slug}|{slug}]] `aliases: a, b` — {summary}
...

## Sources
- [[sources/{slug}|{slug}]]
...
```

If no pages exist, output:
```markdown
# Wiki Index

> {subtitle}

_No pages yet. Ingest a source file to populate the wiki._
```

## Labels (EN / CN)

| EN | CN |
|----|----|
| Auto-generated index of all Wiki pages | 所有 Wiki 页面的自动生成索引 |
| Entities | 实体 |
| Concepts | 概念 |
| Sources | 来源 |
| No pages yet. Ingest a source file to populate the wiki. | 暂无页面，请先导入源文件。 |

Use the language matching the wiki content language.

## Procedure

### 1. Collect Pages

Read all `*.md` files from:
- `{wiki}/entities/`
- `{wiki}/concepts/`
- `{wiki}/sources/`

Sort each group alphabetically by filename.

### 2. Extract Metadata

For each page, parse the frontmatter to get:
- `aliases` (if present)
- `type` (entity/concept/source)

Extract the summary line: the first non-empty, non-heading, non-frontmatter line of the body, truncated to 100 characters.

### 3. Build Index Content

```
# Wiki Index
> {subtitle in wiki language}
> Aliases shown in `backticks` after each entry.

## {Entities label}
- [[entities/{slug}|{slug}]] `aliases: a, b` — {summary}
...

## {Concepts label}
- [[concepts/{slug}|{slug}]] `aliases: a, b` — {summary}
...

## {Sources label}
- [[sources/{slug}|{slug}]]
...
```

Sources section: list paths only, no summaries or aliases.

### 4. Write

Write the assembled content to `{wiki}/index.md`. This operation is idempotent — safe to run any time.
