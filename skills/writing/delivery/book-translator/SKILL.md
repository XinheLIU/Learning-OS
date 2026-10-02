---
name: book-translator
description: Translate Markdown chapters between English and Simplified Chinese preserving structure, technical terms, links, code, and authorial voice. Derives from a finished canonical draft; never edits back. Tier 3: adapter, ~45 min. Use for bilingual book translation, terminology normalization, or translation-quality review.
---

Last updated: 2026-07-28

# Book Translator

Translate as authored prose, not sentence-aligned text. Preserve argument, structure, technical meaning, and personality while making the target read as if written in that language.

## Required References

- Always read [`references/glossary.md`](references/glossary.md) before translating or reviewing a chapter.
- Read [`references/voice.md`](references/voice.md) whenever translating narrative prose, especially Chinese to English or when the output sounds technically clean but generic.
- Follow the target tree's `AGENTS.md` and the repository's structural rules. If they conflict with the glossary, the glossary controls terminology.

## Workflow

### 1. Establish Scope

1. Identify the source language, target language, and exact source and target paths.
2. Treat the source as read-only. Write only to the corresponding target path unless the user explicitly requests reconciliation in both directions.
3. Read the existing target file before overwriting it. Preserve deliberate target-language improvements that are not contradicted by the source.
4. For a new chapter translation, inspect `ROADMAP.md`, both `SUMMARY.md` files, and the relevant level `README.md` files. Update publication metadata only when repository rules require it.

### 2. Read for Meaning and Voice

1. Read the whole source before translating.
2. Extract heading-only outline. It must reveal article's main logic in target language.
3. Identify central problem, core argument, logical chain, point of view, rhythm.
4. Identify protected terms from glossary.
5. Mark code, identifiers, URLs, paths that must remain unchanged.

### 3. Translate the Argument

- Preserve heading levels, order, lists, tables, blockquotes, citations, code fences, links, image paths, frontmatter structure.
- Translate headings as claims or reader tasks. Heading outline must remain continuous narrative.
- Preserve meaning and emphasis, but freely change sentence order, length, idiom when target language requires it.
- Preserve opinions, uncertainty, tension, humor, first-person perspective. Do not neutralize into encyclopedia prose.
- Do not manufacture jokes, emotions, personal experience, certainty, or controversy absent from source.
- Make summary stand alone: reader who skips body must understand subject, main problem, core logic, practical conclusion.
- Do not add or remove claims, examples, citations, or sections unless user asks for editorial reconciliation.

### 4. Apply Direction-Specific Rules

**English to Simplified Chinese**

- Write natural Chinese; do not preserve English syntax or word order.
- Use required Chinese renderings in glossary and keep protected technical terms in English.
- Prefer direct, idiomatic wording. Result should not announce it's a translation.

**Simplified Chinese to English**

- Read voice reference and preserve author's stance instead of flattening.
- Vary sentence rhythm when source does. Use first person when perspective supports it.
- Prefer precise, spoken English over corporate, academic, or press-release phrasing.

### 5. Preserve Non-Translatable Content

Do not translate or alter:

- Inline code and fenced code blocks
- File paths, URLs, anchors, and image paths
- Function names, variable names, CLI flags, configuration keys, and other identifiers
- YAML or frontmatter keys
- Protected technical terms listed in the glossary

Translate descriptive image alt text and display-text frontmatter values.

### 6. Verify

- Compare source and target heading-level sequences.
- Confirm fenced code blocks, URLs, paths, identifiers unchanged.
- Scan for forbidden glossary variants and mistranslated protected terms.
- Read target without source. It must sound authored, not translated.
- Read only target headings; they must reproduce main argument.
- Read only target summary; it must explain subject, main problem, core logic, conclusion.
- Keep target `Last updated:` synchronized with source when translating; use today's date when editorially revising both.
- Run `npm run build` after changing published book content.

## Delivery

Report the translated files, glossary decisions, deliberate adaptations, and
verification performed. Do not add translator notes inside the chapter.
