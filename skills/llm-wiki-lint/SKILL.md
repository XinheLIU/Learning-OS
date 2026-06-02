---
name: llm-wiki-lint
description: "Karpathy's LLM Wiki: run a full health-check audit covering broken links, orphans, index gaps, frontmatter validation, source drift, stale content, and tag sprawl. Use when the user says 'lint', 'audit', 'health-check', 'review the wiki', 'check for broken links', or asks about wiki maintenance. Use proactively after major ingests or before querying a wiki that hasn't been checked recently."
version: 3.0.0
author: Xinhe Liu
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wiki, knowledge-base, maintenance, audit]
    category: research
    related_skills: [llm-wiki, llm-wiki-init]
---

# Karpathy's LLM Wiki — Lint & Maintenance

Periodic health checks and audits for an existing wiki.
See `llm-wiki` for ingest/query and `llm-wiki-init` for first-time setup.

## When This Skill Activates

- Asking to lint, audit, health-check, or review the wiki
- Asking for broken links, orphan pages, or stale content
- Asking to rotate the log

## Wiki Location

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
```

## Orientation (always first)

① Read `SCHEMA.md` — conventions and tag taxonomy.
② Read `index.md` — current page inventory.
③ Scan last 30 lines of `log.md` — recent activity.

## Triage (always after orientation, before checks)

Before running the full checklist, do a quick triage to guide priorities:

1. Compare `index.md` entries against filesystem — if the index lists pages that don't exist on
   disk (ghost entries), the top recommendation should be **re-run ingest** to restore them, not
   "create N individual pages."
2. Check if `concepts/` is empty or nearly empty while `index.md` lists many concepts — this is
   a strong signal of an incomplete prior ingest.
3. Scan for raw files in ALL `raw*` directories (not just `raw/`) when checking for missing sha256.

Run all 12 checks afterward, but use the triage to weight the report's executive summary and to
avoid recommending micro-fixes for systemic problems.

## Lint Checks

Run all checks, then report grouped by severity. Each check is tagged with its actionability:
`[auto-fix]` = safe to fix without asking; `[human-review]` = flag and suggest; `[info]` = report
only, no action expected.

### 1. Broken wikilinks [human-review]
Find `[[links]]` pointing to pages that don't exist.
```bash
# For each .md in entities/ concepts/ comparisons/ queries/:
# Extract all [[wikilink]] targets → check if matching .md file exists
```

### 2. Orphan pages [info]
Pages with zero inbound `[[wikilinks]]` from other wiki pages.
```python
import os, re
from collections import defaultdict
wiki = "<WIKI_PATH>"
inbound = defaultdict(set)
for root, _, files in os.walk(wiki):
    for f in files:
        if not f.endswith(".md"): continue
        path = os.path.join(root, f)
        text = open(path).read()
        for link in re.findall(r'\[\[([^\]]+)\]\]', text):
            inbound[link].add(path)
# Pages with no entry in inbound are orphans
```

### 3. Index completeness [human-review]
Every wiki page in `entities/`, `concepts/`, `comparisons/`, `queries/` must appear in
`index.md`. Compare filesystem against index entries.

### 4. Frontmatter validation [auto-fix]
Every wiki page must have: `title`, `created`, `updated`, `type`, `tags`, `sources`.
Tags must all appear in the SCHEMA.md taxonomy.

### 5. Source drift [human-review]
For each file in `raw/` with a `sha256:` frontmatter field: recompute the hash over the
body (everything after the closing `---`) and flag mismatches.
Mismatch = raw file was edited (violates immutability) or URL content changed on re-ingest.

### 6. Stale content [info]
Pages whose `updated` date is >90 days older than the most recent source mentioning the
same entities. Flag for user review, not auto-update.

### 7. Contested pages [human-review]
Surface all pages with `contested: true` or non-empty `contradictions:` frontmatter.
These require human resolution before claims harden into accepted fact.

### 8. Quality signals [info]
- Pages with `confidence: low`
- Pages citing only a single source with no `confidence` field set
These are candidates for finding corroboration or demoting to `confidence: medium`.

### 9. Page size [info]
Flag pages over 200 lines — candidates for splitting into sub-topics with cross-links.

### 10. Tag audit [auto-fix]
List all tags in use across wiki pages. Flag any not in the SCHEMA.md taxonomy.

### 11. Log rotation [auto-fix]
If `log.md` exceeds 500 entries: rename to `log-YYYY.md` (use the year of the first entry),
start a fresh `log.md` with a rotation note. Confirm with user before rotating.

### 12. Missing sha256 on raw files [auto-fix]
Every file in `raw/` should have a `sha256:` frontmatter field. Flag any that don't —
they can't participate in the skip/drift detection logic.

## Report Format

Group findings by severity:

```
## Lint Report — YYYY-MM-DD

### Critical
- Broken wikilinks: N (list each)

### High
- Orphan pages: N (list each)
- Source drift: N (list each with old vs new hash)

### Medium
- Contested pages: N (list with contradiction links)
- Missing sha256 on raws: N

### Low
- Stale content: N (list with last-updated date)
- Confidence: low pages: N
- Pages over 200 lines: N
- Unknown tags: N

### Info
- Index gaps: N (in filesystem but not index, or vice versa)
- Log rotation needed: yes/no
```

For each finding: file path + specific issue + suggested action.

## After Linting

Append to `log.md`:
```
## [YYYY-MM-DD] lint | N issues found (X critical, Y high, Z medium)
```
