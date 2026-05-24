---
name: wiki-lint
description: Health-scan a structured wiki for duplicates, dead links, empty pages, orphans, and missing aliases, with optional LLM-powered fixes.
---

# Lint Wiki

Two modes: **scan** (no LLM, programmatic only) and **fix** (LLM-powered repair of detected issues).

## Wiki Structure

```
{wiki}/
├── entities/{slug}.md       # type: entity
├── concepts/{slug}.md       # type: concept
├── sources/{slug}.md        # type: source
├── schema/                  # excluded from scan
├── contradictions/          # excluded from scan
├── index.md                 # excluded from scan
└── log.md                   # excluded from scan
```

## Frontmatter Fields (for parsing)

| Field | Values |
|-------|--------|
| `type` | `entity` / `concept` / `source` |
| `aliases` | YAML list of strings |
| `reviewed` | `true` if protected |
| `sources` | YAML list of wiki-links |
| `tags` | entity: `person` `organization` `project` `product` `event` `location` `other`; concept: `theory` `method` `technology` `term` `other` |

## Wiki-Link Scan Pattern

```
[[(entities|concepts|sources)/([^|\]]+)(?:\|[^\]]+)?]]
```

## Write Gate Violations (polluted basenames)

A filename is polluted if:
- Display text after `|` contains `entities/`, `concepts/`, or `sources/` prefix (Pattern A: `[[entities/X|entities/Y]]`)
- Path contains duplicated folder prefix like `entities/entitiesFoo` (Pattern B: `[[concepts/conceptsLayout|Layout]]`)
- Basename contains `/` or `\`

## Section Labels (EN / CN)

Used when generating aliases or expanding empty pages.

| Key | EN | CN |
|-----|----|----|
| basic_information | Basic Information | 基本信息 |
| description | Description | 描述 |
| definition | Definition | 定义 |
| key_characteristics | Key Characteristics | 关键特征 |
| applications | Applications | 应用 |
| related_concepts | Related Concepts | 相关概念 |
| related_entities | Related Entities | 相关实体 |
| mentions_in_source | Mentions in Source | 来源提及 |
| new_information | New Information | 新信息 |
| core_content | Core Content | 核心内容 |

---

## Phase 1 — Scan (no LLM)

### 1. Collect All Wiki Pages

Read all `.md` files under `{wiki}/entities/`, `{wiki}/concepts/`, `{wiki}/sources/`. Exclude `schema/`, `contradictions/`, `index.md`, `log.md`.

### 2. Build Indices

- **pathSet**: all valid page paths (`entities/slug`, `concepts/slug`, `sources/slug`)
- **aliasIndex**: for each page, normalize (lowercase) its title slug and every alias → map to the page path
- **inboundCount**: for each target path, count how many other pages link to it via `[[...]]`

### 3. Detect Issues

For each page, parse frontmatter and body:

**Missing Aliases:** entity or concept page with no `aliases` field, or `aliases` is an empty list. (Sources are exempt.)

**Empty Pages:** body text after frontmatter is whitespace-only.

**Dead Links:** scan all `[[wiki-links]]` in the body. For each link target, check if it exists in `pathSet`. Flag any that don't.

**Orphans (post-scan):** entity or concept pages with `inboundCount == 0` (no other page links to them).

**Duplicates (post-scan):** two different page paths share the same normalized alias or slug key. Flag as candidate pairs.

**Polluted Basenames:** filenames matching write gate violation patterns.

### 4. Output Scan Report

```json
{
  "pages_scanned": 42,
  "missing_aliases": ["entities/foo", "concepts/bar"],
  "dead_links": [{"source": "entities/foo", "target": "entities/missing"}],
  "empty_pages": ["concepts/stub"],
  "orphans": ["entities/lonely"],
  "duplicates": [{"path_a": "entities/ML", "path_b": "entities/machine-learning", "reason": "shared alias"}],
  "polluted": ["entities/entitiesFoo"]
}
```

---

## Phase 2 — Fix (LLM required)

Only run if the user explicitly requests fixes. Each fix type has a per-run cap to limit cost.

### Fix Caps

| Fix type | Cap per run |
|----------|-------------|
| Missing aliases | 20 |
| Duplicates | 10 |
| Dead links | 15 |
| Empty pages | 10 |
| Orphans | 10 |

### Fix 1: Missing Aliases

For each page with missing aliases: provide the page title + first 4000 characters of body. Ask the LLM to generate 3-8 aliases (translations, abbreviations, alternate spellings, full forms). Return `{"aliases": [...]}`. Inject into frontmatter, preserving all other fields.

### Fix 2: Duplicate Pages

For each duplicate pair (target = keep, source = merge-into-target):
- **Safety**: skip if target has `reviewed: true`
- Strip frontmatter from both, provide bodies to LLM
- LLM merges content and outputs `{"body": "...", "extracted_aliases": [...]}`
- Write merged body to target page
- Update target aliases (merge existing + extracted)
- **Rewrite inbound links**: find every `[[...|source-slug]]` or `[[.../source-slug]]` across the entire wiki, replace with target path
- Delete source file

### Fix 3: Dead Links

For each dead link: provide the containing page content + list of all existing page paths with aliases. LLM decides:
- **Correct to alias match**: if an existing page has an alias matching the dead link text, replace the link target
- **Create stub page**: if no match, create a minimal stub page at the target path with `type` guessed from the link prefix, empty body, frontmatter with `created` date

### Fix 4: Empty Pages

For each empty page: provide the page type (entity/concept), title, existing frontmatter, wiki index (for context). Granularity-aware entity/concept limits per page expansion:
- fine: max 5 entities + 5 concepts
- standard: max 3 entities + 3 concepts
- coarse/minimal: max 2 entities + 2 concepts

LLM generates 150-300 word body with proper sections (use section labels in the wiki language). Preserve all existing frontmatter fields.

### Fix 5: Orphan Pages

For each orphan: provide orphan page content + wiki index. LLM selects 1-3 existing pages that should link to the orphan and returns `{"links": [{"target_page": "entities/X", "link_text": "see also [[entities/orphan|Orphan]] for ..."}]}`. Append the link text to each target page body.

### Post-Fix: Regenerate Index

After all fixes are applied, regenerate `{wiki}/index.md`.

### Fix Report

Return counts for each fix type applied, plus list of modified files.

---

## Safety Rules

- Never merge away pages with `reviewed: true`
- Never auto-edit `{wiki}/schema/config.md`
- Never invent source citations for expanded empty pages
- Always preserve all existing frontmatter fields during fixes
- Caps are per-run to prevent runaway changes
