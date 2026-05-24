---
name: wiki-suggest-schema
description: Analyze a wiki and propose schema improvements — appends to wiki/schema/suggestions.md, never auto-edits config.md.
---

# Suggest Schema Updates

Analyze the current wiki structure and propose improvements to the schema configuration. Suggestions are appended to `{wiki}/schema/suggestions.md` — they are never auto-applied. Human review is required before any changes to `config.md`.

## Schema Layout

```
{wiki}/schema/
├── config.md          # Active schema rules (human-edited)
└── suggestions.md     # LLM proposals (append-only, this skill writes here)
```

## Config Format

`config.md` contains sections like:
- Naming conventions (slug patterns, language preferences)
- Entity type classification rules
- Concept type classification rules
- Page templates (required sections, ordering)
- Maintenance policies

## Entity Types

`person` `organization` `project` `product` `event` `location` `other`

## Concept Types

`theory` `method` `technology` `term` `other`

## Procedure

### 1. Read Current Schema

Load `{wiki}/schema/config.md`. If it doesn't exist, create a minimal default:

```markdown
# Wiki Schema Configuration
version: 1

## Naming Conventions
- Use English slugs for all pages
- Preserve original-language names in page titles

## Classification
- Entity types: person, organization, project, product, event, location, other
- Concept types: theory, method, technology, term, other
```

### 2. Sample Wiki Content

Read `{wiki}/index.md` (first ~2000 characters) to understand current wiki scope.
Read up to 3 entity pages and 3 concept pages (first ~500 characters of body each) for structural analysis.
If user provides additional context (e.g., "After lint: 3 duplicate pairs"), include it.

### 3. Analyze and Generate Suggestions (LLM call)

Provide the schema content + wiki sample + any user context. Ask the LLM to consider:

- **New entity/concept types**: are there pages that don't fit existing type tags? Should new types be added?
- **Naming conventions**: are slugs consistent? Should conventions be adjusted?
- **Page templates**: are pages missing important sections? Should templates be updated?
- **Maintenance policies**: should `reviewed: true` protection rules change? Should extraction granularity change?

Return:
```json
{
  "changes_needed": true,
  "suggestions": "## Suggested Changes\n\n1. **Add entity type `framework`**: ...\n\n2. **Add concept type `paradigm`**: ..."
}
```

If no changes needed, set `changes_needed: false` with a brief explanation.

### 4. Append to Suggestions File

Add a dated entry to `{wiki}/schema/suggestions.md`:

```markdown
## {ISO datetime} — {context or "periodic review"}

{changes_needed ? "Changes suggested" : "No changes needed"}

{suggestions text}
```

### 5. Report

Print the suggestions to the user. Remind that `config.md` was NOT modified — human review is required.

## Constraints

- **Never** auto-edit `config.md`
- Append-only to `suggestions.md`
- Suggestions should be specific and actionable, not vague
- If the wiki is nearly empty (< 5 pages), note that more content is needed for meaningful suggestions
