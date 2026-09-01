# Repository Execution Plan

Last updated: 2026-09-01

The three-system restructure and first skill implementations are complete. The work below remains.

## 1. Connect learning evidence to writing

- Let `/evaluate` recognize a new published or publishable draft produced at assistance `none` as
  independent output evidence.
- Let `/reflect` route a mainline that is ready to teach toward a writing task.
- Make `learning/<slug>/notes.md`, `framework.md`, and `research-*.md` explicit inputs to the writing
  workflow while preserving the rule that source material is not learner evidence.

Acceptance: a fixture moves earned learning artifacts into a draft, records the assistance used,
and lets `/evaluate` accept or reject it against an explicit quality bar.

## 2. Add pipeline and writing contract fixtures

- Add compliant and non-compliant fixtures for preprocessing and writing skills.
- Resolve whether the currently ignored `test-cases/tier-handoffs/`, `test-cases/framework/`, and
  `test-cases/case1/` are canonical fixtures. Track canonical fixtures or remove their references;
  do not leave referenced tests excluded from version control.

Acceptance: every maintained fixture is tracked, every documented fixture path exists, and no
ignored fixture is part of a claimed verification path.

## 3. Verify the current uncommitted restructure

Before the owner decides whether to commit:

1. Regenerate all four flat skill layers from the nested tree.
2. Check that no symlink in those layers is broken.
3. Build the local catalog in `../agent-skills` and confirm all 23 skills resolve at nested source
   paths with category counts `pipeline: 6`, `learning: 8`, `writing: 9`.
4. Check README and manifest skill counts against the catalog.
5. Run repository link checks and inspect `git diff --check`.

No commit is part of this plan; committing remains an explicit owner action.
