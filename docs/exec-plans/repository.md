# Repository Execution Plan

Last updated: 2026-10-01

The three-system restructure and first skill implementations are complete. The work below remains.

## 1. Connect learning evidence to writing

- Let `/evaluate` recognize a new published or publishable draft produced at assistance `none` as
  independent output evidence.
- Let `/reflect` route a mainline that is ready to teach toward a writing task.
- Make `learning/<slug>/notes.md`, `framework.md`, and `research-*.md` explicit inputs to the writing
  workflow while preserving the rule that source material is not learner evidence.

Acceptance: a fixture moves earned learning artifacts into a draft, records the assistance used,
and lets `/evaluate` accept or reject it against an explicit quality bar.

## 2. Add pipeline and writing contract coverage

- The learning chain is covered end to end by two runbooks in
  [`trials/`](../../trials/README.md). The writing chain now has a third —
  [`trials/transformer/RUNBOOK.md`](../../trials/transformer/RUNBOOK.md), eight stages from
  `frame` to `archive-materials` — **live author trial pending**. The staged article/snapshot trial
  is now [writing](../../trials/writing/RUNBOOK.md), with stdlib brief regression checks.
- It covers `frame`, `develop-argument`, `develop-examples`, `write-content`, `insert-inline-images`, `book-diagrams`,
  `review-draft`, `edit-targeted`, `grill`, `package-chapter`, `archive-materials`, and
  `synthesis-research` in its gap-fill role. Still uncovered by any trial: `build-skeleton`,
  `book-translator`, `create-tech-slides`, `clean-notes`, `organize-docs`, and the four
  `llm-wiki-*` skills — those rest on `## Contract test` blocks alone.
- Decide, after the Transformer run: whether the uncovered set needs a second writing trial (a
  wiki-to-book line would reach `llm-wiki-*` and `build-skeleton` in one pass), or whether contract
  tests are the accepted standard for them.

Acceptance: every documented verification path exists and is tracked, and no skill claims a
verification that nothing exercises.

## 3. Verify the current uncommitted restructure

Before the owner decides whether to commit:

1. Regenerate all four flat skill layers from the nested tree.
2. Check that no symlink in those layers is broken.
3. Build the local catalog in `../agent-skills` and confirm all 23 skills resolve at nested source
   paths with category counts matching `catalog/skill-set.json` (currently pipeline 11, learning 6, writing 14).
4. Check README and manifest skill counts against the catalog.
5. Run repository link checks and inspect `git diff --check`.

No commit is part of this plan; committing remains an explicit owner action.
