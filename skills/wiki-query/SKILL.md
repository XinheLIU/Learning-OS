---
name: wiki-query
description: Query a structured wiki with conversational Q&A — select relevant pages, load full content, answer with wiki-links.
---

# Query Wiki

Answer questions using the wiki: select the most relevant pages from the index, load their full content, and answer with proper `[[wiki-links]]` as citations.

No chunking or RAG — load complete pages for full context.

## Index Format

`{wiki}/index.md` lists all pages grouped by type:

```markdown
# Wiki Index

## Entities
- [[entities/{slug}|{slug}]] `aliases: a, b` - {summary line, max 100 chars}

## Concepts
...

## Sources
...
```

Aliases appear in backtick brackets after each entry. The LLM should consider aliases when matching queries to pages.

## Wiki-Link Citation Format

All citations in answers must use:
```
[[entities/{slug}|Display Name]]
[[concepts/{slug}|Display Name]]
[[sources/{slug}|Display Name]]
```

## Procedure

### 1. Read Index

Load `{wiki}/index.md`. If it is empty or contains "No pages yet", inform the user that content must be ingested first.

### 2. Select Relevant Pages (LLM call 1)

Provide the user's question + the full index content. Ask the LLM to select 3-5 most relevant pages, considering titles, summaries, AND aliases (in backticks). Return:

```json
{"relevant_pages": ["entities/deep-learning", "concepts/backpropagation", "sources/ml-survey"]}
```

### 3. Load Full Page Content

Read each selected page's full markdown (frontmatter + body). Concatenate with separators.

### 4. Answer the Question (LLM call 2)

Provide:
- System context: the wiki index + full content of selected pages
- Instruction: answer the question using only information from the provided pages; cite every claim with `[[wiki-links]]`; if the wiki doesn't contain the answer, say so
- The user's question

### 5. Multi-Turn / REPL Mode (optional)

If the user wants a conversation:
- Maintain history of previous Q&A pairs (cap at 10 exchanges)
- Include recent history in the context for each new question
- Save history to `.wiki-query-history.json` in the vault root for session persistence

## Constraints

- Max 3-5 pages selected per query
- Answers must cite sources with `[[wiki-links]]`
- If wiki content is insufficient to answer, state that clearly — don't fabricate
