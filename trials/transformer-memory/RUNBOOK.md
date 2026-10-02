# Transformer Memory Trial — RUNBOOK (Part B)

Last updated: 2026-10-01

**Goal: run the memory-enabled chain by hand, on your own Transformer materials, one skill per
sitting — and judge each output before the next skill consumes it.**

This is Part B of [`docs/exec-plans/memory.md`](../../docs/exec-plans/memory.md). Part A rebuilt
the skills and proved the chain runs mechanically on a 12-file synthetic fixture. It deliberately
**never touched your Transformer materials**, so this is their first real run and every output is
evaluable.

| | |
| :--- | :--- |
| Archive | `../../test/Transfomer/` — 266 files (the folder name carries the typo; leave it) |
| Domain | `machine-learning` — `sources/machine-learning.md` is seeded with your own judgments |
| Slug | `transformer` |
| Depth | `quick` |
| Cadence | **one step per sitting.** A step that fails evaluation is a fix to the one skill named, then a re-run |

## How to read this runbook

Every step has the same four parts, plus one this runbook adds:

1. **Paste this** — the literal prompt.
2. **Watch for** — what should happen while it runs. Contract violations are visible here in real
   time and invisible afterward.
3. **Check** — a shell command whose output you compare against the assertions.
4. **L1 assertions** — mechanical, answerable by `ls` and `grep`. Any FAIL fails the step.
5. **Your evaluation** — **empty, and yours to fill.** Part A's job was the mechanics; the quality
   criteria are the author's, and writing them here before the step runs is the point. The
   dimension line names what the step is *for*; it is a prompt, not a criterion.

**Fill the evaluation section before you run the step.** Criteria written after seeing the output
grade the output against itself.

## Setup

```bash
cd C:/Users/olivia/GitHub/learning-infra/agent-skill-projects/learning-os
export ARCHIVE="$(cd ../../test/Transfomer && pwd)"
find "$ARCHIVE" -type f ! -name '.DS_Store' | wc -l     # expect ~266
test -f sources/machine-learning.md && grep -c '^| [a-z]' sources/machine-learning.md  # expect 10 (9 rows + header)
test ! -f "$ARCHIVE/materials.md" && echo "OK: archive not yet mapped"
test ! -d learning/transformer && echo "OK: clean slug"
```

> **The archive is read-only.** Only `materials.md` and confirmed renames may ever be written into
> it. If a step would write anything else there, stop and record **NOT RUN**.

---

## B1 — `/map-materials` · process the archive

**Paste this**

```
/map-materials transformer $ARCHIVE
```

**Watch for**

- It reports the file listing and the denominator **before** proposing any row.
- It reads the notes in full and only skims the PDFs — it should not be summarizing papers.
- The duplicate finding is stated as a finding you can argue with, not buried in the table.
- `06-Vision`, `07-Multimodal`, `08-Time-Series`, `12-Courseware`, `13-GPT-Resources` collapse to
  one `peripheral` row each, not one row per file.

**Check**

```bash
test -f "$ARCHIVE/materials.md" && head -12 "$ARCHIVE/materials.md"
grep -c '^| m' "$ARCHIVE/materials.md"                       # rows
grep -c '| key |' "$ARCHIVE/materials.md"
grep -c 'redundant-of' "$ARCHIVE/materials.md"
grep -c '| peripheral |' "$ARCHIVE/materials.md"
grep -cE '\| — \|$' "$ARCHIVE/materials.md"                  # used-in all empty at map time
grep -n '^archive: ' learning/transformer/survey.md
find "$ARCHIVE" -type f ! -name 'materials.md' ! -name '.DS_Store' -newermt '-1 hour'   # expect empty
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.1 | Every file covered by a row or an ancestor folder row; counts reconcile to the denominator | ☐ |
| L1.2 | Both Vaswani PDFs present; the second is `redundant-of` the first and names its id | ☐ |
| L1.3 | Each off-topic folder is **one** `peripheral` row with `/**` and a file count | ☐ |
| L1.4 | Every `key` row has a non-empty `concepts` cell | ☐ |
| L1.5 | Every `used-in` cell is `—` | ☐ |
| L1.6 | `learning/transformer/survey.md` exists with an `archive:` line | ☐ |
| L1.7 | Archive byte-for-byte unchanged apart from `materials.md` | ☐ |

**Your evaluation** — *material processing: did it find the real duplicates; is the key set the set
you would have picked; are the peripheral calls right for a Transformer-LM topic; does the concept
column say what each key item actually teaches.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B2 — `/curate-sources` · extend and verify the registry

**Paste this**

```
/curate-sources machine-learning
```

**Watch for**

- Your nine seeded rows are not re-tiered, re-worded, or re-ordered.
- Candidates come from `materials.md`'s `source-id: —` rows **first**, the web last.
- Every proposed tier is in the report, not in a `tier` cell.

**Check**

```bash
git diff --no-index /dev/null /dev/null 2>/dev/null   # (registry is gitignored; diff by hand)
grep -c '^| [a-z]' sources/machine-learning.md
grep -c '| unrated |' sources/machine-learning.md
grep -c '^- `#v' sources/machine-learning.md
grep -nE '^\| (d2l-attention|vaswani-attention|bert) ' sources/machine-learning.md | cut -d'|' -f2,5
grep -c 'source-id: —\|\| — |' "$ARCHIVE/materials.md"
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.8 | ≥2 new rows, **all** `unrated` | ☐ |
| L1.9 | Every new row has `kind`, `domains`, and an openable pointer | ☐ |
| L1.10 | No seeded row's `id`, `tier`, `domains`, or `verdicts` changed | ☐ |
| L1.11 | No verdict was invented (verdict count unchanged unless you asked for one) | ☐ |
| L1.12 | `verified` refreshed only on rows the run actually checked | ☐ |
| L1.13 | A second run appends nothing and moves no tier | ☐ |

**Your evaluation** — *source tiering: are the candidates genuinely tier-1/2 material; did it
respect your judgments; is anything proposed you would reject.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B3 — `/survey` · scope what enters

**Paste this**

```
/survey transformer
```

Answer the Mission Contract interview honestly. When it asks for the output:

```
Mission: one book chapter in writing/MachineLearning that takes a reader who knows linear algebra
to being able to hand-derive scaled dot-product attention and explain the block's anatomy. I
already know this topic — I need the chapter, not the education. Target can-apply on attention
mechanics. Don't teach me the vision or multimodal branches.
```

**Watch for**

- It **refuses to discover sources.** Every source it names resolves to a registry `id`; anything
  else is a `gap` line.
- The mainlines are the field's, not the course's — a survey whose mainlines are
  `01-Foundations … 14-LLM-Papers` has copied the folder tree.
- The mode partition is argued per node, not assigned in bulk.
- The Roadmap does **not** contain a critical path.

**Check**

```bash
grep -n '^archive: ' learning/transformer/survey.md
awk '/### Scope — sources/,/### Scope — nodes/' learning/transformer/survey.md
awk '/### Scope — nodes/,/## Gap/' learning/transformer/survey.md | grep -cE '\| (deep|connect) \|'
awk '/### Scope — nodes/,/## Gap/' learning/transformer/survey.md | grep -c '| connect |'
grep -c 'SKIP' learning/transformer/survey.md
grep -n 'gap —' learning/transformer/survey.md
grep -nE 'critical path' learning/transformer/survey.md          # expect none, or a pointer to /curriculum
grep -c 'Iteration: 0' learning/transformer/notes.md
grep -n 'fixture-attention\|transformer' learning/index.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.14 | 3–5 mainlines, each with the one question it answers | ☐ |
| L1.15 | Every registry row touching the field has a `DEEP`/`SKIM`/`SKIP` with a mission-tied why | ☐ |
| L1.16 | ≥1 argued SKIP; every SKIM names the part to read | ☐ |
| L1.17 | No source named anywhere fails to resolve to a registry `id`; needed-but-unregistered ones are `gap` lines | ☐ |
| L1.18 | ~15 nodes, **every one** with a mode and a why; ≥1 `connect` | ☐ |
| L1.19 | Structural Memory in `notes.md`: only `target`/`hypothesized`, every node moded, `Iteration: 0` | ☐ |
| L1.20 | Roadmap carries **no** critical path | ☐ |
| L1.21 | `learning/index.md` has a `transformer` row; every appended edge is `hypothesized` with both endpoints resolving | ☐ |

**Your evaluation** — *the partition: is deep-vs-connect where you'd put it for someone who already
knows the topic and wants to write the chapter; are the mainlines the field's, not the course's; is
the SKIP argued.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B4 — `/curriculum` · the 主线

**Paste this**

```
/curriculum transformer --depth=quick
```

Approve the syllabus when asked — after checking the Critical Path, which is the thing this step
exists to produce.

**Watch for**

- It cites **only** Scope sources and **only** `key` map rows, by `m<nnn>`.
- The Critical Path is hardest-first within the dependency order, not easiest-first.
- `[C]` lessons are ~10 minutes at `quick` and stay ~10 minutes — depth does not scale them.
- The hardest concepts are *explained* in the lessons, not named.

**Check**

```bash
awk '/^## Critical Path/,/^## Stage 1/' learning/transformer/syllabus.md
awk '/^## Critical Path/,/^## Stage 1/' learning/transformer/syllabus.md | grep -cE '^\| [0-9]+ \|'
awk '/### Scope — nodes/,/## Gap/' learning/transformer/survey.md | grep -c '| deep |'   # must match ↑
grep -c '`\[C\]`' learning/transformer/syllabus.md
awk '/### Scope — nodes/,/## Gap/' learning/transformer/survey.md | grep -c '| connect |'  # must match ↑
grep -c 'Path:' learning/transformer/syllabus.md
grep -n 'Interleaves:' learning/transformer/syllabus.md
grep -oE 'm[0-9]{3}' learning/transformer/syllabus.md | sort -u | while read m; do
  grep -q "^| $m " "$ARCHIVE/materials.md" && grep "^| $m " "$ARCHIVE/materials.md" | grep -q '| key |' || echo "NOT KEY: $m"; done
ls learning/transformer/lessons/
test ! -f learning/transformer/syllabus.html && echo "OK: no syllabus.html"
open learning/transformer/index.html
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.22 | Critical Path row count **equals** the `deep` node count; each appears once, in dependency order | ☐ |
| L1.23 | No `connect` node appears in a Critical Path row | ☐ |
| L1.24 | `[C]` lesson count **equals** the `connect` node count | ☐ |
| L1.25 | Every cited `m<nnn>` is a `key` row (the loop above prints nothing) | ☐ |
| L1.26 | No lesson cites a `SKIP` source or an unregistered one | ☐ |
| L1.27 | Every `[K]`/`[S]` lesson has a `Path:`; every `[S]` an `Interleaves:` naming a non-adjacent prior lesson | ☐ |
| L1.28 | Each `[C]` lesson: one named excerpt, one edge-statement task, **zero** drills, no quiz | ☐ |
| L1.29 | No `[C]` lesson is the first lesson | ☐ |
| L1.30 | ≥1 mini-case with its own file; ≥1 W milestone with **no** file; no `syllabus.html` | ☐ |
| L1.31 | Load notes say ~10 min; `[S]` specs name 1–2 drills — `quick` landed | ☐ |

**Your evaluation** — *does the course hit the mark: is the critical path the hardest-first thread a
strong learner needs; are the hardest concepts (scaled dot-product and the √d_k argument, why
residual + norm, KV cache) explained rather than named; did every lesson use the key material it
cites; are the `[C]` lessons worth ten minutes.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B5 — the learning loop · one cycle

**Paste this** — over several sittings, in this order

```
/learn transformer
```
then, after each lesson, paste its completion manifest with `done L<n>`. Cover **≥3 lessons
including ≥1 `[C]`**. Then:

```
/recall transformer
```
(fire ≥2 items on `recall.html`, then `sync recall`)

```
/practice transformer
```
(bring one real case — the chapter section you are about to write is the natural one)

```
/evaluate transformer
/reflect transformer
```

**Watch for**

- `/learn start` reports and **stops** — no tutoring in chat.
- `done` on a `[C]` lesson asks for nothing but the edge statement, and records no Attempt Log line.
- The recall prompt shows **alone**. An answer seen before you committed is `peeked` and syncs as
  `walkthrough`. If that happens once, the step fails regardless of every other box.
- `/reflect` writes a verdict with a pointer, and does **not** touch a `tier` cell.

**Check**

```bash
grep -c 'earned' learning/transformer/notes.md
awk '/#### Concepts/,/#### Models/' learning/transformer/notes.md | grep -c 'connect · earned'
grep -cE '^\| [a-z0-9-]+ \| (schema|term|operational) \|' learning/transformer/retrieval.md
# every ledger row must point at a DEEP node:
awk '/#### Concepts/,/#### Models/' learning/transformer/notes.md | grep 'connect' | \
  sed 's/.*\*\*\(.*\)\*\*.*/\1/' | while read n; do grep -q "structural-memory:$n" learning/transformer/retrieval.md \
  && echo "LEDGER ROW FOR CONNECT NODE: $n"; done
ls learning/transformer/case-*.md
grep -n 'Mastery Snapshot' learning/transformer/notes.md
grep -n 'Iteration:' learning/transformer/notes.md
grep -c '^- `#v' sources/machine-learning.md            # ≥1 more than after B2
grep -E '^\| (vaswani-attention|d2l-attention)' sources/machine-learning.md | cut -d'|' -f5   # tier unchanged
grep -n 'mode → deep' learning/transformer/survey.md    # expect NONE — a proposal lives in notes.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.32 | ≥3 `earned` deep nodes, each with a `none`/`hint` pointer and a learner-worded gloss | ☐ |
| L1.33 | ≥2 `earned` edges, ≥1 of them from a `[C]` lesson | ☐ |
| L1.34 | The `[C]` lesson added **zero** ledger rows (count before == count after) | ☐ |
| L1.35 | No ledger row points at a `connect` node (the loop above prints nothing) | ☐ |
| L1.36 | `retrieval.md` state transitions follow the ledger contract; no warm retrieval recorded as cold | ☐ |
| L1.37 | ≥1 `case-*.md` with every attempt field and a valid assistance enum | ☐ |
| L1.38 | Mastery Snapshot reports `connect` nodes as `placed`/`unplaced`, with no rubric level | ☐ |
| L1.39 | `/reflect` appended ≥1 verdict with a `case-*.md` pointer and changed **no** `tier` cell | ☐ |
| L1.40 | Any `mode → deep` proposal is in `notes.md`; `survey.md` is unchanged | ☐ |
| L1.41 | `Iteration` bumped exactly once | ☐ |

**Your evaluation** — *the learning record: does `notes.md` read as what you actually constructed;
did recall fire cold; did the `[C]` lesson leave an edge you can state; did `/reflect` propose
something you agree with.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B6 — framing, logic and evidence · the chapter brief

**Paste this**

```
/frame chapter mode on the Transformer materials. The archive is mapped and there is a learning
run under learning/transformer/. Write the brief to tmp/transformer/drafts/transformer/brief.md.
Continue with /develop-argument and /develop-examples for logic, source selection and code/math.
```

**Watch for**

- Preparation reuses `materials.md`; `develop-examples` owns its selection rows. Check only for
  files that arrived after mapping rather than producing a competing inventory.
- A `redundant-of` or `peripheral` selection is refused **with the canonical id named**.
- Markers are proposed from `earned` nodes and **confirmed with you**; a marker you don't recognize
  is dropped, not argued for.
- Code/math records existing choices; only unresolved tradeoffs require a question.

**Check**

```bash
PIECE=tmp/transformer/drafts/transformer
grep -oE 'm[0-9]{3}' $PIECE/brief.md | sort -u | while read m; do
  grep "^| $m " "$ARCHIVE/materials.md"; done | grep -vE '\| key \|' && echo "NON-KEY SELECTED" || echo "OK: all key"
grep -n 'earned' $PIECE/brief.md
awk '/#### Concepts/,/#### Models/' learning/transformer/notes.md | grep 'earned'
grep -n 'gap' $PIECE/brief.md
grep -nE '^\| .* \| cut \|' $PIECE/brief.md | wc -l
find "$ARCHIVE" -type f ! -name 'materials.md' ! -name '.DS_Store' -newermt '-1 hour'   # expect empty
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.42 | Every selection row is an `m<nnn>` id; every `core`/`support` row is a `key` row | ☐ |
| L1.43 | Every author marker names an `earned` node or edge (cross-check the two greps above) | ☐ |
| L1.44 | No `connect` node holds a 一层 or 二层 section | ☐ |
| L1.45 | Every required node has evidence or an explicit gap; cuts are justified, not required by quota | ☐ |
| L1.46 | Every Code & math row has a source pointer **and** a placement | ☐ |
| L1.47 | Archive byte-for-byte unchanged | ☐ |

**Your evaluation** — *did it draw on the processed material rather than re-scanning; do the markers
match what you learned in B5; does the selection make sense for the chapter form.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B7 — draft, review, grill, package

**Paste this** — one per sitting

```
/write-content from tmp/transformer/drafts/transformer/brief.md
/insert-inline-images    ·    /book-diagrams
/review-draft    ⇄    /edit-targeted
/grill
/package-chapter
```

**Watch for**

- The draft uses `core` + `support` only — no `cut`, no `redundant-of`, no `peripheral` material.
- `/grill` records each question's draft anchor but never shows it before your answer. An answer
  given with the anchor visible is `peeked`, never a pass.
- `review-draft` checks chapter capability and dependencies without opponent requirements.
  Requiring a 正方 is a regression. V2 and legacy briefs both remain readable.

**Check**

```bash
PIECE=tmp/transformer/drafts/transformer
python3 skills/writing/scripts/verify_references.py --portability $PIECE/*.md
sed -n '2,8p' $PIECE/transformer.md | cut -d: -f1
grep -c 'peeked' $PIECE/grill-log.md          # expect 0
ls $PIECE/assets/
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.48 | Six frontmatter fields stamped; zero BROKEN; portability clean | ☐ |
| L1.49 | No `cut`/`redundant-of`/`peripheral` material appears in the draft | ☐ |
| L1.50 | Placed images are under `assets/` with captions | ☐ |
| L1.51 | `review-draft` verdict is `ship` | ☐ |
| L1.52 | `grill-log.md` has every miss routed and **zero** `peeked` | ☐ |

**Your evaluation** — *the writing: is it a chapter you would publish; did it use the material the
brief selected; are the hardest sections the strongest; did grill find real gaps.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B8 — write-back · `archive-materials` and `/evaluate`

**Paste this**

```
/archive-materials on the shipped Transformer chapter
```
then
```
/evaluate transformer
```

**Watch for**

- Renames are offered in **one batch**, with the inbound-reference check, and nothing is applied
  without your yes.
- No `role` cell and no `tier` cell is touched.
- `/evaluate` claims `Independent` only if all four conditions hold, and names the failed one
  otherwise.

**Check**

```bash
grep -cE '\| transformer § ' "$ARCHIVE/materials.md"
grep -c 'planned, unused' "$ARCHIVE/materials.md"
grep -c '^- `#v' sources/machine-learning.md
grep -nE '^- `#v.* (hold|promote) (tmp/)?(drafts|transformer)' sources/machine-learning.md
grep -E '^\| (vaswani-attention|d2l-attention)' sources/machine-learning.md | cut -d'|' -f5  # tier still unchanged
grep -n 'Independent' learning/transformer/notes.md
grep -n '| transformer |' learning/index.md
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.53 | Every material the draft used has a `used-in` naming piece and section | ☐ |
| L1.54 | Every brief `core`/`support` row the draft dropped is `planned, unused` | ☐ |
| L1.55 | ≥1 verdict with a pointer into the draft; all `hold`/`promote`; **no** `tier` cell written | ☐ |
| L1.56 | Renames left zero BROKEN and updated their `path` cells in the same batch | ☐ |
| L1.57 | `Independent` is claimed with all four conditions cited, or refused with the failed one named | ☐ |
| L1.58 | `learning/index.md`'s `transformer` row refreshed; no cross-topic edge written by `/evaluate` | ☐ |

**Your evaluation** — *is the archive now something you would upload and trust to find things in a
year; does the registry verdict reflect how the sources actually held up.*

- Criteria (write before running):
- Verdict:
- If it failed, the one skill to fix:

---

## B9 — move and snapshot (manual, no skill)

Move the packaged folder into `writing/MachineLearning/`, add the `book.yml` entry with
`build-skeleton` **there**, and later pin the snapshot in `site-source/sources/`. Read
`writing/AGENTS.md` first. Nothing is committed or pushed unless you say so.

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.59 | The chapter is in the writing system; `learning/transformer/` retained as its provenance | ☐ |
| L1.60 | `sources/` and `learning/` are still small enough to read end to end | ☐ |

**Your evaluation** — *the target state: core layer small and earned, archive layer complete and
mapped, one shipped chapter traceable to both.*

- Criteria (write before running):
- Verdict:

---

## B10 — RL · the cross-topic proof

Run **B1–B5** for reinforcement learning from `../../test/Reinforcement-Learning/`.

This is the step Part A could not fake. A cross-topic edge needs a case that crossed both topics,
and one topic cannot produce one — the Part-A smoke run left `learning/index.md` with a
`hypothesized` edge and no `earned` one, deliberately, rather than assert structure it had no
evidence for.

**Check**

```bash
grep -c '^| [a-z-]*:' learning/index.md
grep -c '| earned |' learning/index.md
( cd ../../../synapse && uv run synapse graph rlhf )
```

| # | Layer 1 | Pass |
| :-- | :--- | :--- |
| L1.61 | `learning/index.md` has two topic rows | ☐ |
| L1.62 | `/survey reinforcement-learning` seeded ≥1 `hypothesized` edge to an existing `transformer:` node | ☐ |
| L1.63 | After one RL cycle, `/reflect` earned ≥1 cross-topic edge with a `none`/`hint` pointer | ☐ |
| L1.64 | `synapse graph rlhf` returns the Transformer node with the index as source path | ☐ |
| L1.65 | The RL survey scoped `connect` for what Transformer already earned | ☐ |

**Your evaluation** — *whether the second topic actually reused the first: the edge is stated in
your words, and the RL survey did not re-teach what Transformer covered.*

- Criteria (write before running):
- Verdict:

---

## Expected end state after B8

```text
sources/machine-learning.md              ~12 rows; ≥1 verdict citing the chapter
<archive>/materials.md                    ~40 rows; ≥5 used-in filled            ← archive layer
learning/index.md                         1 topic row (2 after B10)
learning/transformer/
  survey.md  syllabus.md  notes.md  retrieval.md  case-0001.md  lessons/ …       ← core: process record
tmp/transformer/drafts/transformer/
  brief.md  transformer.md  grill-log.md                                          ← core: output
writing/MachineLearning/…/transformer.md  (after B9)                              ← destination
```

## What this trial does and does not prove

It proves the chain runs on real material, that its mechanics match the contracts, and that you
judged each output. It does **not** prove the loop teaches Transformers better than reading — you
already know the topic ([ADR-004](../../docs/adr.md)).

Expected friction, in order:

- **The first mode partition will be wrong somewhere.** A `/reflect` proposal at B5 is a success
  signal, not a defect.
- **`chapter-format.md`'s fixed five sections will fight the Critical Path's order.** Decide at B6
  which yields, and record it.
- **`review-draft` has no chapter-brief mode.** Decide at B7.
- **Two verdicts may disagree about one source.** That is expected —
  `/archive-materials` writes `hold` from the chapter and `/reflect` writes `demote` from the
  errors. `/curate-sources` applies both in id order; check the net movement is the one you want.
