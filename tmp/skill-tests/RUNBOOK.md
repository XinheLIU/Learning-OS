# Skill Tests — Isolated Fixtures

Last updated: 2026-10-01

The generated materials are synthetic. `make-fixtures.sh` resets `materials/`, `materials-map/`,
`materials-archive/` and `drafts/` in this directory. Run it only when intentionally resetting those
outputs; preserve any active trial first. Its fixtures predate staged brief v2 and remain useful for
legacy compatibility and delivery checks.

## What each fixture plants

| Fixture | Purpose / planted defects |
| :--- | :--- |
| materials | off-topic note/images, cryptic image names, bulk folders; no author facts inferred from filenames |
| materials-map | key, redundant and peripheral rows for canonical selection checks |
| drafts/grill-case | legacy teaching brief; the draft asserts multi-head concatenation without explaining why |
| drafts/pkg-clean | valid local image, math and code for portability checks |
| drafts/pkg-broken | missing/absolute/escaping images, nonportable math, legacy tags, bare fences and invalid content IDs |
| materials-archive + drafts/archive-case | planned-unused images and an inbound reference that a rename must preserve |

## Brief and writing regressions

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/writing/scripts -p 'test_*.py' -v
python3 skills/writing/scripts/verify_brief.py tmp/skill-tests/drafts/grill-case/brief.md --stage ship
```

The chapter fixture passes **legacy reading**, not a ship-quality review. A current preparation
trial invokes `frame` for question/capability, `develop-argument` for teaching logic and
`develop-examples` for evidence/selection/code-math. All originals stay unchanged. The complete
scenario set is [the writing runbook](../../trials/writing/RUNBOOK.md).

## Delivery checks

```bash
python3 skills/writing/scripts/verify_references.py --portability tmp/skill-tests/drafts/pkg-clean/attention.md
python3 skills/writing/scripts/verify_references.py --portability tmp/skill-tests/drafts/pkg-broken/attention.md
```

The clean fixture should pass and the broken fixture should fail with located defects. A package
trial stamps known frontmatter only and copies the folder to a temporary location to prove its
relative assets resolve. Body repairs remain separate targeted edits.

## Interactive fixtures

- **grill:** request a quiz on `grill-case/attention.md`. An unexplained concatenation answer routes
  to a draft gap; inability to recall a mechanism actually taught routes to an author gap. The
  prompt must not reveal the answer. This needs a real respondent and cannot be replaced by grep.
- **archive:** work on a separate copy. First prepare the current `materials.md` map and source
  registry (the old fixture does not provide the entire current archive contract). Record actual
  usage as `used-in`, selected-but-unused material as `planned, unused`, and source verdicts only
  for used sources. Leave roles/tiers alone; do not expect the obsolete images-manifest/sources
  files in the archive. Re-running unchanged must not duplicate pointers or verdicts.
- **rename:** the cryptic image has an inbound note reference. A confirmed rename updates its map
  path and inbound reference together; declining it changes neither. Do not silently restructure.

Keep mechanical results distinct from live author outcomes. The Transformer runbooks cover the
full library and cold self-test; the writing runbook covers reasoning quality and snapshot reuse.
