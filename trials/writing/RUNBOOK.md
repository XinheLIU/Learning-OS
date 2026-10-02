# Writing Redesign Trial

Last updated: 2026-10-01

Test reader gain, reasoning, evidence and continuity as separate properties. For each future run,
create a fresh output folder under `tmp/`; do not overwrite the existing Learning How to Learn brief
or the original Transformer library. The mechanical suite is reproducible without those private
materials. The completed implementation walkthrough's temporary artifacts were discarded on
2026-10-01.

## Mechanical regressions

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/writing/scripts -p 'test_*.py' -v
python3 skills/writing/scripts/verify_brief.py tmp/learning-how-to-learn/drafts/ai-10x-and-taste/brief.md --stage examples
python3 skills/writing/scripts/verify_brief.py tmp/skill-tests/drafts/grill-case/brief.md --stage ship
```

The last two commands are optional local corpus checks: use them when those files exist. A legacy
compatibility pass does not certify evidence or publishability. Do not regenerate existing fixtures
merely to run them; the fixture generator resets its generated directories.

## Semantic scenarios

Invoke the named skill with each input in an isolated working folder. Evaluate the actual response,
not whether it repeats terminology from SKILL.md. Save findings with quoted passages and repair
conditions. No scenario permits inventing a real author experience.

| Scenario/input | Skill | Required observable result |
| :--- | :--- | :--- |
| Explain to junior engineers why idempotency matters; the definition is settled and there is no opponent | frame → logic → examples → draft → review | a reader situation and gain; no manufactured debate or forced cut |
| Explore whether AI reduces total learning time; retrieval time, practice time and task scope differ; no final author judgment supplied | frame → logic | distinct possible answers and comparison criteria; uncertainty retained |
| Draft says: “我用 AI 在一小时写出了 demo。因此 AI 让所有团队的交付速度提高十倍。” | review-draft | quotes inference gap; prototype time does not establish team delivery speed; route to logic/evidence |
| Explain a mechanism using only a reliable public case; no personal incident supplied | develop-examples | attributable external evidence is sufficient; no invented anecdote or personal-case gate |
| A synthetic request-count illustration is labelled as a measured production outcome | review-draft | distinguish illustration from factual evidence; require a source or correct attribution |
| Remove a logic node but leave its evidence and figure reference | develop-argument / checker | stale references named; dependent sections rechecked |
| Teaching chapter contains no opposing view | review-draft | assess capability, prerequisites and evidence without requesting 正方 |
| A ready brief and outline were already confirmed | write-content | use them without asking to approve the same outline again |

## Real corpus walkthrough

1. Read the Learning How to Learn brief and only relevant selected note passages. Leave their bytes
   unchanged. Review the existing broad inference about total learning speed: identify which parts
   are supported locally and which need empirical evidence. Do not infer this is an endorsed change
   in the author's view.
2. In a separate output folder, frame an explanatory article around the distinction between finding
   an answer and independently using it. Reuse actual author wording with its source pointer; ask
   only about a genuinely new judgment. Build logic and evidence, draft, then run one review/edit
   loop. The result should add reader understanding even if it contradicts nobody.
3. Run the updated Transformer preparation stages or read its legacy chapter fixture. Check v2 node
   references/Code & math and purpose-aware review. The full author grill belongs to the Transformer
   runbook; reviewing a fixture cannot establish author mastery.

## Snapshot continuity and recovery

Use fictional author statements clearly labelled as synthetic test data:

1. Initial statement: “I now distinguish search time from practice time; I do not yet know the total
   effect of AI.” Run `snapshot-writing` into a clean `writing-memory/`. Expect `0001.md`, explicit
   attribution/uncertainty and an index link. Save its byte hash.
2. Invoke again with the same statement, then a paraphrase. Expect no `0002.md` and unchanged files.
3. Supply new grounded information: “The effect depends on whether scope stayed constant.” Ask to
   record this revised understanding. Expect `0002.md` → Previous `0001.md`, a stated delta and the
   original hash unchanged. This is a fixture judgment, never the real user's learning record.
4. Add a second topic with a first grounded snapshot; propose an `extends` relation with a reason
   and basis. Unendorsed connections remain `candidate`. Rebuild the index from latest snapshots.
5. Simulate an interrupted index refresh by removing only the test index. Re-run with unchanged
   latest understanding. Expect a rebuilt index and no additional snapshot. A later snapshot that
   retracts a relation removes it from the derived index while preserving its historical row.
6. Ask `frame` for a related next article. It must retrieve the existing grounds/open question and
   identify the new gain, rather than pitch the first article again. Inspect that `learning/`,
   material maps, source registries and draft bytes were not written by snapshotting.

## Recording results

The implementation run is recorded in [RESULTS.md](RESULTS.md).

Record command results separately from semantic walkthrough results. For each behavioral case,
retain input, output, actual finding and remaining uncertainty. A checker's pass means only that
fields/references obey the contract. An implementation-agent walkthrough is not independent skill
validation; an author's live evaluation remains a separate result.

- Mechanical suite: record command, date, counts and failures.
- Semantic walkthrough: identify who ran it and which artifacts were actually exercised.
- Live author evaluation: reader gain, inference quality, usefulness of retrieved snapshots.
