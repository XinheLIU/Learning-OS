---
name: package-chapter
description: Verify a draft folder is portable and contract-conformant — frontmatter stamped, image refs resolving, no absolute paths, math in $…$, code fences languaged — then prove it by copying the folder to temp and re-resolving. Generates manifest stub DATA (not the full book.yml entry). Tier 2: workflow, ~20 min. Use for "package this chapter", "is this ready for the book repo", 封装章节, 归档成章, or before handing a draft to MachineLearning / ComputerScience / Coding-with-Agents.
---

Last updated: 2026-09-22

# Package Chapter

## Overview

A draft folder in, a **provably portable** draft folder out. Every check here answers one question:
*if this folder were moved into the book repository tomorrow, what would break?*

The proof is mechanical: copy the folder to a temporary directory and re-resolve every reference
there. A reference that only works in place is a reference that works because of where it sits —
which is exactly what breaks on the move.

**This skill never touches the destination repository.** It does not move the folder, does not edit
`collections/book.yml`, does not add navigation. It reports a ready-to-move path and a manifest
stub for the author to paste.

## Hard Rules

1. **Never move or copy into the writing repositories.** The author performs the move by hand. The
   only copy this skill makes is a throwaway portability probe. Generating the manifest stub data is not
   writing to the destination — it is handing the author values to paste. The entry in `collections/book.yml`
   is written by `build-skeleton`.
2. **The body is byte-for-byte unchanged except frontmatter.** If a check fails, report the
   offending line — do not fix prose, do not rewrite a path, do not "helpfully" move an image.
   Fixes go through `edit-targeted`, or back to `insert-inline-images` for image work.
3. **Report every failure with its file and line.** "Some images are broken" is not a report.
4. **Never invent frontmatter values.** `id`, `title`, and `created` come from the author or the
   brief. A guessed `id` is a permanent identifier that is wrong forever — it never changes when
   the file moves, which is the whole point of it.
5. **Zero BROKEN, or the package fails.** There is no "mostly resolving".

## The contract being checked

From `site-source/docs/architecture/CONTENT-CONTRACT.md` in the writing workspace. Read that file
when it's reachable — it is normative and this list is a mirror, not a substitute.

| Rule | Requirement |
| :--- | :--- |
| Frontmatter | `id`, `locale`, `title`, `status`, `created`, `updated` — all six required |
| `id` | `^[a-z0-9]+(-[a-z0-9]+)*$`, stable forever; translation pairs share it |
| `locale` | `en` or `zh-CN` |
| `status` | `draft` \| `published` \| `archived` |
| dates | `YYYY-MM-DD`, `updated >= created` |
| Images | beside the content under `./assets/`, referenced relatively, never escaping the folder |
| Math | inline `$…$`, display `$$…$$` |
| Mermaid | fenced ```` ```mermaid ```` blocks — never Hexo `{% mermaid %}` |
| Code fences | carry a language |
| Internal links | `[text](content:<id>)`, not a filesystem path into another repo |

Publication fields — route, part, order, layout, publish date — **do not** belong in frontmatter.
They live in `collections/book.yml`. Stamping `route:` into the chapter is a contract violation
this skill must catch, not commit.

## Workflow

### Step 1: Stamp the frontmatter

Read the existing frontmatter and the brief. Ask the author only for what neither supplies —
normally just `id` and `created`. Derive `locale` from the body's language, `updated` from today,
`status: draft` until the author says otherwise.

Then write the block, and nothing below it.

```yaml
---
id: transformer
locale: zh-CN
title: Transformer
status: draft
created: 2026-09-21
updated: 2026-09-21
tags:
  - deep-learning
---
```

### Step 2: Run the checks

Checks 1–7 of the old list are now one call. `verify_references.py --portability` is the shared
definition of "verified" — the same script `insert-inline-images` and `archive-materials` run, so
the three cannot drift apart.

```bash
PIECE=<draft-folder>          # e.g. tmp/transformer/drafts/transformer
DOC="$PIECE"/<chapter>.md
SKILLS=<learning-os>/skills

# 1. references + portability — image refs, absolute paths, folder escapes,
#    math delimiters, legacy renderer tags, unlanguaged fences, malformed content: links.
#    Exit 0 is the pass; every failure is printed as file:line with the rule it breaks.
python3 "$SKILLS"/writing/scripts/verify_references.py --portability "$DOC"

# 2. informational — remote images, reported not failed
grep -nE '!\[[^]]*\]\(https?://' "$DOC"

# 3. assets live beside the content
find "$PIECE" -type f ! -name '.DS_Store' | sed "s|^$PIECE/||" | sort
```

The script resolves the bare-fence judgment call itself: it tracks open/close state, so a bare
```` ``` ```` that *closes* a block passes and only an unlanguaged *opener* is reported.

Check 3 is a layout check, not a grep: every file under the piece folder is either the chapter
Markdown, something under `assets/`, or a working file that must not ship (`brief.md`,
`grill-log.md`, `tasks-for-edit-targeted.md`, `gaps-for-learning.md`, `research-*.md`). Name the
working files in the report — the author leaves them behind on the move.

### Step 3: The portability probe

The checks above all pass in place. This one proves they pass anywhere.

```bash
PROBE=$(mktemp -d)
cp -R "$PIECE" "$PROBE"/chapter
python3 "$SKILLS"/writing/scripts/verify_references.py "$PROBE"/chapter/<chapter>.md
```

Zero BROKEN in the probe is the package's actual pass condition. A reference that resolved in
`$PIECE` and breaks in `$PROBE` was resolving through the corpus directory — the exact failure the
move would have produced, found for the cost of a `cp`.

Remove the probe when done.

### Step 4: Report

State, in this order:

1. **Verdict** — packaged, or failed with the count.
2. **Ready-to-move path** — `$PIECE`, and the files to leave behind.
3. **Failures**, each as `file:line` plus the rule it breaks. No fixes applied.
4. **Informational** — remote images, site-absolute refs.
5. **The manifest stub data**, for the author to use when adding the entry to the destination repo's
   `collections/book.yml` after the move. The actual entry and navigation update belong to `build-skeleton`, not here:

```yaml
  - id: transformer
    source:
      zh-CN: book/src/11-deep-learning/transformer/transformer.md
    part: deep-learning
    order: 11.4
```

Say plainly that the `source:` path is a guess at the destination layout and the author owns it —
and that adding the item, and any navigation around it, belongs to the destination repo (and to
`build-skeleton`), not here.

## Contract test

Every check is mechanical and file-resolvable — no check requires judgment about prose quality; a
fixture with an absolute path and a missing image fails with both offending lines named; the
portability probe runs from a directory outside the corpus and reports zero BROKEN before the
verdict is `packaged`; the chapter body is byte-for-byte unchanged except the frontmatter block; no
file is written outside the draft folder; the destination repository is not touched.

## Handoffs

**In:** a draft with verdict `ship` from `review-draft`, and `defended` from `grill` when the
chapter carries a capability claim.

**Out:**
- Verdict `packaged` → the author moves the folder into the book repository and uses the
  manifest stub data; navigation there is `build-skeleton`'s.
- Failures → `edit-targeted` (prose, paths, math) or `insert-inline-images` (image refs, asset
  placement), then re-run.
- The chapter shipped → `archive-materials` closes the loop on the materials folder.
- Chinese draft packaged → `book-translator` derives the English mirror, which packages separately
  under the same `id` with `locale: en`.

## Boundaries

- vs `build-skeleton`: this skill produces the data (id, locale, status, suggested source path) for one book.yml entry. Writing that entry into the destination repo is `build-skeleton`'s job. This skill ends at the source folder boundary.
- vs the planned `publish-*` adapters: those derive a new artifact per medium. This verifies and
  stamps the canonical one, and derives nothing.
- vs `book-translator`: that produces the other locale. This packages whichever locale it is given.
- vs `archive-materials`: that writes into the materials folder after the ship. This only ever
  writes frontmatter, in the draft folder.
