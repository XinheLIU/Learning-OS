# Memory Execution Plan

Last updated: 2026-10-01

This file plans the move from per-topic file state to a memory-enabled system with sharper skill
boundaries, in two parts: **Part A** — the agent rebuilds the skill foundation until the closed loop
runs mechanically; **Part B** — the author runs every skill by hand on the Transformer materials
and evaluates output quality, slowly, one skill at a time. Only unfinished work is listed here.
When a skill or schema lands, its contract moves to the owning system README and durable rationale
moves to [`docs/adr.md`](../adr.md).

First case: Transformer, from the author's materials at
`C:\Users\xhl\GitHub\learning-infra\test\Transfomer\` (266 files; the folder name carries the
typo). Second case: RL, for the RLHF→Transformer cross-topic edge.

**Status (2026-09-28): Part A is implemented and its assertions pass.** Part B has not been run —
by design: Part A never touched the Transformer materials, so B1 is their first run. The runbook is
[`trials/transformer-memory/RUNBOOK.md`](../../trials/transformer-memory/RUNBOOK.md), and its
evaluation sections are empty and yours.

This file stayed the sketchpad through the build: the Part-A table below carries per-step status,
§7 records what the work changed about the plan, and §9 carries the questions that are now sharper
or new.

Writing update (2026-10-01): Part A below records the September implementation. Current chapter
preparation is `frame` → `develop-argument` → `develop-examples`; source selection and code/math
belong to the last skill. Editorial snapshots live separately in `writing-memory/` and never earn
learning edges. Use the updated B6/B7 runbook and writing README for current contracts.

## 0. Diagnosis

The three-stage vision — collect & process → learning loop → write-out — is close to the
repository's shape ([ADR-001](../adr.md)), with two structural exceptions and three missing
memories.

Structural exceptions:

- **Planning lives inside the loop.** `/survey` and `/curriculum` sit in `skills/learning/` next to
  the skills that iterate. They decide what enters and in what order; they do not iterate.
- **Nothing processes a materials folder before learning.** `organize-docs` restructures,
  `clean-notes` cleans one note, `archive-materials` records after a piece ships, `frame` scans
  cold per piece. No skill ranks a folder into key / redundant / peripheral once, for every
  downstream reader.

Missing memories:

| Memory | Scope | Today | Gap |
| :-- | :-- | :-- | :-- |
| Source registry (tiered, updated) | cross-topic | per-topic Read / Don't-read list in `survey.md`, then forgotten | Stage 1's premise |
| Material map (key vs redundant) | per topic | none — every skill re-scans | Stage 1's processing output |
| Deep-vs-connect partition | per topic | implicit in per-mainline target stages | the scoping decision, made explicit |
| Cross-topic concept index | cross-topic | none — every slug is an island | the "evolutionary state" |
| Harness feedback → tier / mode changes | write-back | nothing records "source X mis-taught lesson N" | the "iterated on feedback" |

Decisions made with the author (2026-09-28):

- Cross-topic graph: **split** — `learning/index.md` here, Markdown; synapse indexes it via the
  manifest protocol and never writes it.
- Order: **design Stage 1 first**; no baseline run of the old Transformer writing runbook.
- Registry: **in this repo, gitignored** for the MVP (`/sources/`, tracked README).
- The author's existing source judgments (`reference.md`, `01-Foundations`, `03-Core-Papers`) are
  **recorded directly** as tiered rows with an `author-judgment` verdict, not re-discovered.
- Two-part plan: agent builds (Part A), author runs and evaluates (Part B). **Evaluation criteria
  are authored by the author**; this plan states only the expected output of each skill.

## 1. Target state — two layers of output

Everything the system produces belongs to one of two layers, with different storage, different
lifetimes, and one direction of flow between them.

```text
┌──────────────────────────── ARCHIVE LAYER ─────────────────────────────┐
│ raw materials, organized and mapped — papers, PDFs, notebooks, images  │
│ one folder per topic, large, cloud/object storage, never in git        │
│   <archive>/<topic>/…                 the files, untouched             │
│   <archive>/<topic>/materials.md      the map: key / redundant / peripheral, used-in │
└───────────────────────────────┬────────────────────────────────────────┘
                                │ distill (learning loop + writing)
                                ▼
┌───────────────────────────── CORE LAYER ───────────────────────────────┐
│ what was actually learned and what was written — small, versioned     │
│   sources/<domain>.md                 tiered registry + verdicts       │
│   learning/index.md                   topics + cross-topic edges       │
│   learning/<slug>/                    survey · syllabus · notes · retrieval · cases │
│   drafts/<piece>/                     brief · chapter · grill log      │
│         │                                                              │
│         └─► writing/MachineLearning/  the shipped chapter (book repo)  │
│               └─► site-source/sources/ snapshot → published site      │
└────────────────────────────────────────────────────────────────────────┘
```

Rules:

- **Archive is big and dumb; core is small and earned.** The archive holds every input plus one
  map. The core holds only plans, learner evidence, and drafts. A file in the core must be either
  learner-produced or a plan for learner work.
- **Flow is one-way.** Archive → core through the loop and the writing system. The only write-back
  into the archive is `materials.md` (`used-in` cells, confirmed renames). Nothing in the core is
  ever copied into the archive.
- **The chapter is the graduation artifact.** It leaves the core by a manual move into the writing
  repository (`package-chapter` proves it portable; the author moves it). Publication is manifest
  membership there, per `writing/AGENTS.md`. The site snapshot follows on the writing system's own
  cadence.
- **The learning record is as durable as the chapter.** `learning/<slug>/` is the proof of how the
  chapter was earned; it is kept, not discarded after shipping.

Storage per layer:

| Layer | Where | Versioned | Size | Skills touch it |
| :-- | :-- | :-- | :-- | :-- |
| Archive | one root the author chooses, synced to cloud (`<archive>/<topic>/`); MVP uses `test/Transfomer/` in place | no (cloud sync) | GBs | read-only, except `materials.md` |
| Core — registry, index, `learning/` | this repo's gitignored `sources/`, `learning/` for the MVP; a private git repo after the MVP (§9) | yes | MBs | read/write by owner per §2 |
| Core — drafts | `tmp/<topic>/drafts/` for the MVP; the writing repo after the move | yes, in the writing repo | MBs | writing skills |

Learning skills locate the archive through one line in `learning/<slug>/survey.md`:
`archive: <absolute path>`; `map-materials` writes it first. No skill hard-codes a path.

## 2. Memory model and storage

### 2.1 Layers and owners

| L | Memory | Scope | Path | Owner (writes) | Readers |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | Raw materials | per topic | `<archive>/<topic>/` | human | `map-materials`, `frame` |
| 1 | Material map | per topic | `<archive>/<topic>/materials.md` | `map-materials` (rows), `archive-materials` (`used-in`, renames) | `/survey`, `/curriculum`, `frame` |
| 2 | Source registry | cross-topic | `sources/<domain>.md` | `curate-sources` (rows, tiers); `/reflect`, `archive-materials` (verdicts) | `/survey`, `frame` |
| 3 | Plan | per topic | `learning/<slug>/survey.md`, `syllabus.md` | `/survey`, `/curriculum` | loop skills |
| 4 | Learner memory | per topic | `notes.md`, `retrieval.md`, `case-*.md`, `research-*.md` | loop skills (existing contracts) | loop skills, `frame`, `/evaluate` |
| 5 | Cross-topic index | cross-topic | `learning/index.md` | `/survey` (hypothesized), `/reflect` (earned) | `/evaluate`, `frame`, synapse |
| 6 | Drafts | per piece | `drafts/<piece>/` | writing skills (existing contracts) | `/evaluate`, `archive-materials` |

Ids: node `<slug>:<node>`; source = registry `id`; material `m<nnn>` within one map. Every table in
L1, L2, L5 has a fixed column set stated in its owning README.

### 2.2 Canonical Markdown, derived SQL, staged

| Option | Inspectable in git | Skills read/write directly | Cross-topic queries | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| Markdown only | yes | yes | grep | **v1** |
| Markdown canonical + derived SQLite index (rebuilt from files) | yes | yes | SQL | **v2, on trigger** |
| SQLite canonical | no | via scripts only | SQL | rejected — breaks ADR-003; every skill would depend on a script |

- Canonical state is Markdown at every layer. No skill reads or writes a database.
- v2 adds a derived, gitignored, disposable SQLite index when a trigger fires: `/recall` across
  ≥3 topics; "which chapters used source X"; an edge lookup needing more than one grep. One
  stdlib script (`scripts/build-memory-index.py`, `sqlite3`, run with `uv`, no dependencies)
  rebuilds it from L1/L2/L5 and the ledgers; two runs must produce identical rows.
- Semantic recall stays in synapse (embedding-backed SQLite/FTS5 from manifests). This repo
  publishes `.learning-manifest.json` for the core layer and builds no second semantic index.

## 3. Boundary moves

| Blur today | Sharpened | Part A step |
| :-- | :-- | :-- |
| `/survey`, `/curriculum` live in `skills/learning/` | move to `skills/pipeline/`; Stage 1 = gather → process → scope → build; Stage 2 = only skills that iterate | A3 |
| `/survey` discovers, maps, diagnoses | `/survey` **reads** `sources/` and `materials.md`; discovery → `curate-sources`; processing → `map-materials` | A1, A2, A4, A5 |
| `/survey` Roadmap holds a critical path; `/curriculum` sequences again | `/survey` = field map + what enters (mode partition); `/curriculum` = the one critical path (主线) + lessons | A4 |
| Deep vs light learning implicit | every node has `mode: deep \| connect`; connect earns an edge in a `[C]` lesson, opens no ledger row | A4 |
| `frame` scans cold; `archive-materials` scans again | both use `materials.md`; `frame` selects, `archive-materials` fills `used-in` | A6, A7 |
| Nothing reads learner memory when writing | `frame` seeds author markers from earned nodes; `/evaluate` accepts a packaged chapter as `Independent` | A6 |
| Cross-topic links have no home | `learning/index.md`; `/survey` hypothesizes, `/reflect` earns | A8 |

## Part A — Agent builds the foundation

Goal: the closed loop runs mechanically end to end on a small synthetic fixture, every touched
skill has a current `## Contract test` block, and Part B's runbook exists. **Part A never runs on
the real Transformer materials** — that is the author's, so the first real run is evaluable.

Exit for every step is mechanical: a file exists with the stated shape, a contract-test assertion
resolves, a symlink is not broken. Quality is Part B's.

| # | Step | Deliverable | Done when | Status |
| :-- | :-- | :-- | :-- | :-- |
| A1 | Registry schema | `sources/README.md` (columns, tier rules, entry states, verdict format); `.gitignore` entry; seed `sources/machine-learning.md` from `reference.md` + `01-Foundations` + `03-Core-Papers` with `#v1 author-judgment` | ≥6 rows, every tier row links a verdict | DONE |
| A2 | `map-materials` | `skills/pipeline/map-materials/SKILL.md` + contract test; columns `id \| path \| kind \| source-id \| role \| concepts \| used-in`; writes `archive:` line into `survey.md` stub | on a 12-file synthetic fixture with one duplicate and one off-topic folder: every file covered, duplicate is `redundant-of`, folder is one `peripheral` row, fixture byte-for-byte unchanged | DONE |
| A3 | Move planning skills | `survey/`, `curriculum/` under `skills/pipeline/`; **five** symlink layers regenerated (`.claude/skills/` is a fifth, gitignored, and was carrying two broken links); `catalog/skill-set.json` (`pipeline: 11`, `learning: 6`, `writing: 11`); both READMEs and root README counts | no broken symlink; catalog builds `--local` in `../agent-skills` | DONE |
| A4 | Scope + critical path + `[C]` | `/survey`: reads registry + map, refuses without them, step 7 → **Scope** (sources × DEEP/SKIM/SKIP; node × `mode` with why), Roadmap drops the critical path, appends hypothesized edges to `learning/index.md`. `/curriculum`: reads Scope + `key` rows only, writes `## Critical Path` (ordered deep nodes, each with its key materials), one `[C]` lesson per connect node (~10 min, one excerpt, one edge-statement task, no drills, no checkpoint quiz). `/learn done` on `[C]`: writes one Connections row, no ledger row. `/practice`, `/evaluate`: connect nodes only as edge endpoints | fixture `survey.md` has a mode per node and ≥1 connect; fixture `syllabus.md` Critical Path contains only deep nodes; `done C-01` on the fixture writes an edge and zero `retrieval.md` rows | DONE |
| A5 | `curate-sources` | `skills/pipeline/curate-sources/SKILL.md` + contract test: appends `unrated` rows, refreshes `verified`, applies pending verdicts to `tier` with one line each, never deletes | second run on the fixture registry is idempotent; a tier edit with no verdict fails the test | DONE |
| A6 | Writing reads memory | `frame`: reads `materials.md`, selection rows are `m<nnn>`, `redundant-of`/`peripheral` refused with the canonical id named, author markers seeded from `earned` nodes, connect nodes only as transitions. `/evaluate`: `Independent` rung from a packaged draft + declared assistance ≤ hint; rejects if markers do not trace to earned nodes | fixture brief: every core row is `key`; refusal message names the canonical id; fixture snapshot cites the draft | DONE |
| A7 | Write-back | `archive-materials`: fills `used-in`, appends `hold`/`promote` verdicts citing chapter + section; drops `images-manifest.md` / `sources.md` (subsumed). `/reflect`: `demote`/`hold` verdicts citing cases; proposes `mode → deep` for connect nodes in recurring errors; never edits `tier` or `mode` | fixture: ≥1 verdict with a `drafts/` pointer; ≥1 `used-in`; a `/reflect` proposal line exists and `survey.md` is unchanged until `/survey` deepening applies it | DONE |
| A8 | Cross-topic index | `learning/index.md` schema in learning README (Topics table; Cross-topic edges with the closed vocabulary); `/survey` and `/reflect` writers; `.learning-manifest.json` generated with `uv run synapse manifest generate` | fixture index has one hypothesized and one earned edge with pointers; manifest validates | DONE* |
| A9 | Smoke run | the whole chain on the synthetic fixture: `map-materials` → `curate-sources` → `/survey` → `/curriculum` → `/learn` start/done (K, S, C) → `/recall` → `/practice` → `/evaluate` → `/reflect` → `frame` → `write-content` → `review-draft` → `package-chapter` → `archive-materials` | every file in §1's core layer exists for the fixture slug; every Part-A "done when" still holds afterward | DONE |
| A10 | Part B runbook | `trials/transformer-memory/RUNBOOK.md` in the four-part format (Paste this / Watch for / Check / assertions), one block per Part-B step, with **empty evaluation sections for the author to fill** | every Part-B step has a block; mechanical assertions filled; evaluation headings present and blank | DONE |

ADRs 008–013 are written: [`docs/adr.md`](../adr.md). The numbering shifted by one against §8's
sketch — the shipped-chapter ADR is **013**, not 010, because ADR-010 went to the planning-skill
move, which turned out to need its own record (it supersedes ADR-001's placement).

**`DONE*` on A8.** The schema, both writers, and the manifest all landed and the manifest
validates. What did **not** land is an `earned` cross-topic edge: a single-topic fixture cannot
produce one, because earning a cross-topic edge requires a case that crossed both topics. The
smoke run left `learning/index.md` with one `hypothesized` edge and a note saying why, rather than
asserting structure it had no evidence for — which is the rule the table exists to enforce. That
assertion moves to **B10**.

### What the smoke run found

A9 ran the full chain on `tmp/skill-tests/materials-map/` (12 files) and produced
`learning/fixture-attention/` plus `tmp/fixture-attention/drafts/`. It caught four things the
contracts got wrong, each fixed in the one skill that owned it:

| # | Found | Fix |
| :-- | :--- | :--- |
| 1 | `map-materials` Hard Rule 7 said peripheral is *always* folder-level, which leaves a loose off-topic file unrowable | Rule now forbids exploding a folder, not the role |
| 2 | `/archive-materials` writes `hold` from the chapter while `/reflect` writes `demote` from the errors — the same source, opposite directions, and `curate-sources` had no rule | Opposing verdicts both apply, in id order, with the net movement reported and both pointers named |
| 3 | `make-fixtures.sh` does `rm -rf drafts`, which deleted the smoke run's own draft folder | Smoke-run output moved to `tmp/<topic>/drafts/`, outside the generator's reach, and the generator says so |
| 4 | The fixture generator was gitignored, so no Part-A assertion was reproducible from a clean checkout | `.gitignore` now tracks `make-fixtures.sh` and the skill-tests runbook, still ignoring their output |

Two frictions found against synapse, both synapse's call and neither blocking:

- **`confidence` is required-ish and numeric.** `manifest generate` stamped `confidence` on all 856
  concepts. A 0–1 number published under `repo: learning-os` is a numeric mastery score, which is
  an explicit non-goal of the learning README. It is synapse's heuristic, not ours, but it is
  published in our name.
- **Edge types don't survive.** Manifest schema v1 carries `prerequisites` and nothing else, so
  `bridges`, `contrasts-with`, and `special-case-of` are lost on the way in. `learning/index.md`
  keeps them; the index does not.

`.learning-manifest.json` and `.synapse-cache.json` are gitignored: they index gitignored learner
state, and synapse reads sibling checkouts locally rather than from git.

## Part B — Author runs and evaluates, one skill at a time

Cadence: slow, one skill per sitting, in order. Each step states the invocation, inputs, and the
**expected output** — concrete for the Transformer folder. The **evaluation criteria are the
author's** and go into the runbook's evaluation section for that step; the dimensions listed
below are the ones the author named and are placeholders for those criteria, not criteria
themselves. A step that fails evaluation is a fix to the one skill named, made in Part A style,
then re-run.

### B1 — `map-materials` · process the archive

- **Run:** `/map-materials transformer <archive path>`
- **Reads:** the 266 files.
- **Expected output:** `<archive>/transformer/materials.md`, roughly 40 rows: ~12 `key`
  (both Vaswani PDFs → one; five DLAI notebook sets → one `key` + four `redundant-of`;
  `transformer-note.md` `key` with per-section concepts; `Deepseek.md`, the `05-Architecture-Variants`
  papers, the RoPE/GQA/MoE images as `key`), ~8 `redundant-of`, one `peripheral` row each for
  `06-Vision`, `07-Multimodal`, `08-Time-Series`, `12-Courseware`, `13-GPT-Resources`. Archive
  byte-for-byte unchanged. `learning/transformer/survey.md` stub with `archive:` line.
- **Author evaluates:** material processing — did it find the real duplicates; is the key set the
  set you would have picked; are the peripheral calls right for a Transformer-LM topic; did the
  concept column say what each key item actually teaches.

### B2 — `curate-sources` · extend and verify the registry

- **Run:** `/curate-sources machine-learning`
- **Reads:** seeded `sources/machine-learning.md`, `materials.md` `source-id` placeholders.
- **Expected output:** your seeded rows untouched; ≥2 `unrated` candidates (CS224n, the Annotated
  Transformer, Karpathy's nanoGPT are the likely finds) with a proposed tier and one-line why;
  `verified` dates refreshed.
- **Author evaluates:** source tiering — are the candidates genuinely tier-1/2 material; did it
  respect your judgments; is anything proposed that you would reject.

### B3 — `/survey` · scope what enters

- **Run:** `/survey transformer`
- **Reads:** registry, `materials.md`, the Mission Contract interview.
- **Expected output:** `survey.md` with Mission Contract; 3–5 mainlines (likely: sequence
  representation → attention → block anatomy & training → efficiency variants); the matrix;
  **Scope**: every registry source × DEEP/SKIM/SKIP with a why, ≥1 SKIP; ~15 v0 nodes each with
  `mode` — expected deep: self-attention/QKV, multi-head, positional encoding, block anatomy,
  masked attention + KV cache; expected connect: BoW, Word2Vec, RNN enc-dec, Hugging Face API, MoE
  (first pass), the vision/multimodal variants. Structural Memory v0 in `notes.md`; no critical
  path in the Roadmap.
- **Author evaluates:** the partition — is deep vs connect where you'd put it for someone who
  already knows the topic and wants to write the chapter; are the mainlines the field's, not the
  course's; is the SKIP argued.

### B4 — `/curriculum` · the 主线

- **Run:** `/curriculum transformer --depth=quick`
- **Reads:** `survey.md` Scope + matrix, `materials.md` `key` rows.
- **Expected output:** `syllabus.md` with `## Critical Path` — ~7 deep nodes in dependency order,
  each naming the key material(s) that teach it (e.g. self-attention ← `m003` Vaswani §3.2 +
  `m020` DLAI notebook 2); ~7 K/S lessons + ~4 `[C]` lessons + ≥1 mini-case; HTML course under
  `learning/transformer/`; `recall.html`.
- **Author evaluates:** does the course hit the mark — is the critical path the hardest-first
  thread a strong learner needs; are the hardest concepts (scaled dot-product and the √d_k
  argument, why residual + norm, KV cache) explained in the lessons rather than named; did every
  lesson actually use the key material it cites; are the `[C]` lessons worth ten minutes.

### B5 — learning loop · one cycle

- **Run:** `/learn transformer` → `done L<n>` × ≥3 (≥1 `[C]`), `/recall` × ≥2 firings,
  `/practice transformer` × 1, `/evaluate transformer`, `/reflect transformer`.
- **Expected output:** `notes.md` with ≥3 earned deep nodes, ≥2 earned edges (≥1 from a `[C]`
  lesson) at `none`/`hint`; `retrieval.md` with ~6 rows, deep items only, correct state
  transitions; `case-0001.md`; a Mastery Snapshot; `/reflect` output including any `mode → deep`
  proposal.
- **Author evaluates:** the learning record — does `notes.md` read as what you actually
  constructed; did recall fire cold; did the `[C]` lesson leave an edge you can state; did
  `/reflect` propose something you agree with.

### B6 — `frame` · the chapter brief

- **Run:** `/frame` chapter mode on the Transformer draft.
- **Reads:** `materials.md`, `notes.md`, `chapter-format.md`.
- **Expected output:** `drafts/transformer/brief.md` — selection map over `m<nnn>` ids with every
  core/support row `key`; author's markers naming earned nodes; code-&-math gate decisions; `gap`
  rows for what the archive lacks (sinusoidal PE math, RMSNorm, parameter sharing).
- **Author evaluates:** did it draw on the processed material rather than re-scanning; do the
  markers match what you learned in B5; does the selection make sense for the chapter form.

### B7 — draft, review, grill, package

- **Run:** `/write-content` → `/insert-inline-images` · `/book-diagrams` → `/review-draft` ⇄
  `/edit-targeted` → `/grill` → `/package-chapter`.
- **Expected output:** `drafts/transformer/transformer.md` following the brief ladder, no
  `cut`/`redundant`/`peripheral` material; placed images under `assets/` with captions; review
  verdict `ship`; `grill-log.md` with every miss routed; six frontmatter fields; zero BROKEN refs;
  ready-to-move path for `writing/MachineLearning/`.
- **Author evaluates:** the writing — is it a chapter you would publish; did it use the material
  the brief selected; are the hardest sections the strongest; did grill find real gaps.

### B8 — write-back · `archive-materials` and `/evaluate`

- **Run:** `/archive-materials` on the shipped chapter; `/evaluate transformer` again.
- **Expected output:** `materials.md` `used-in` filled for every material the chapter used;
  ≥1 registry verdict citing the chapter; renames offered in one batch, none applied without
  confirmation; Mastery Snapshot records the chapter as `Independent` with its assistance level.
  The archive folder is now cloud-ready: files plus one map with usage.
- **Author evaluates:** is the archive now something you would upload and trust to find things
  in a year; does the registry verdict reflect how the sources actually held up.

### B9 — move and snapshot (manual)

- **Run:** move the packaged folder into `writing/MachineLearning/`, add the `book.yml` entry via
  `build-skeleton` there, later pin the snapshot in `site-source/sources/`.
- **Expected output:** the chapter in the writing system; `learning/transformer/` retained as
  its provenance.
- **Author evaluates:** the target state — core layer small and earned, archive layer complete
  and mapped, one shipped chapter traceable to both.

### B10 — RL · the cross-topic proof

- **Run:** B1–B5 for RL from the author's RL materials.
- **Expected output:** `learning/index.md` with two topics, ≥1 hypothesized edge from `/survey`
  (e.g. `rl:policy-gradient → transformer:decoder-block`), ≥1 earned edge from `/reflect`
  (e.g. `rl:rlhf-reward-model → transformer:lm-head`); `synapse graph rlhf` returns the
  Transformer node with the index as source path.
- **Author evaluates:** whether the second topic actually reused the first — the edge is stated
  in your words, and the RL survey scoped `connect` for what Transformer already earned.

### Expected end state after B8

```text
sources/machine-learning.md              ~8 rows; ≥1 verdict citing the chapter
<archive>/transformer/materials.md        ~40 rows; ≥5 used-in filled            ← archive layer
learning/index.md                         1 topic row
learning/transformer/
  survey.md   syllabus.md   notes.md   retrieval.md   case-0001.md   lessons/ …   ← core: process record
drafts/transformer/brief.md  transformer.md  grill-log.md                          ← core: output
writing/MachineLearning/…/transformer.md  (after B9)                               ← destination
```

What this proves (ADR-004): the chain runs, its mechanics match the contracts, and the author
judged each output. It does not prove the loop teaches Transformers better than reading — the
author already knows the topic. Expected friction, in order: the first mode partition will be
wrong somewhere (a `/reflect` proposal is a success signal); `chapter-format.md`'s fixed sections
will fight the Critical Path's order (decide at B6 which yields); `review-draft` has no
chapter-brief mode ([article-loop.md](article-loop.md) §7; decide at B7).

## 8. ADR candidates

- **ADR-008** — Two output layers: a large mapped archive outside git and a small earned core
  that ends in the writing system; flow is one-way. (§1)
- **ADR-009** — Memory is layered Markdown with one owner per layer; SQL is a derived, disposable
  index on a stated trigger; semantic recall is synapse's. (§2)
- **ADR-010** — Planning skills belong to Stage 1; the learning loop contains only skills that
  iterate. (§3, A3)
- **ADR-011** — Sources and materials are ranked once with evidence-gated tiers and roles;
  discovery, processing, scoping, and write-back are four separate skills. (A1, A2, A5, A7)
- **ADR-012** — Every node has a learning mode; `connect` nodes are earned by an edge and never
  enter the retrieval ledger. (A4)
- **ADR-013** — A shipped chapter at assistance ≤ hint is `Independent` evidence; the brief must
  trace to earned structure. (A6)

## 9. Open questions

Updated 2026-09-28 after Part A. Answered ones are struck through with their answer.

- **Durable home for the core layer.** Unchanged, and now more pressing: `sources/`, `learning/`,
  and `learning/index.md` are gitignored here, so nothing versions the state the whole system is
  built on. Ranked: a private `learning-memory` repo (synapse indexes it as one more configured
  repo); or a `learning/` folder inside the writing system. Decide after B9.
- **Archive root.** MVP uses `test/Transfomer/` in place. The cloud-synced root and its per-topic
  naming are the author's; `materials.md` at each topic root is the only requirement.
- ~~Does `capture-source` fold into `curate-sources`?~~ **Still open, and B2 is still the decider.**
  Part A drew the line where the plan said: `curate-sources` lists, it does not fetch. If B2's
  candidates are all things the author must then download by hand, the fold-in is worth it.
- ~~`[C]` lesson vs. folding connect nodes into `Interleaves:`~~ **Decided: `[C]` lesson.** The
  ledger rule forced it — a `connect` node earns an edge and opens no row, and an `Interleaves:`
  mention has nowhere to record that edge. Revisit only if B5 shows `[C]` lessons get skipped.
- ~~`materials.md` concepts are free text until `/survey` names nodes; does `/survey` rewrite
  them?~~ **Decided: no.** `/survey` reads the map and never writes it — the concepts column stays
  the mapper's free text, and the join to node ids happens in `/curriculum`'s Critical Path
  (`Teaches from`) instead. One less writer on a file two skills already share.
- **`learning/index.md` node ids reference `notes.md` headings; renames break them.** Sharper now
  that the index exists: `/survey` checks both endpoints on write, but nothing checks on rename.
  Decide after B10 whether `/reflect` must check inbound references before archiving a node.
- **Synapse's `confidence` field.** The manifest stamps a 0–1 number on every concept, published
  under `repo: learning-os`, against this repo's no-numeric-scores rule. Either synapse makes it
  optional, or this repo stops publishing a manifest, or the rule gets a stated exception for
  derived indexes. Not blocking; needs one decision.
- **Edge types are lost in the manifest.** Schema v1 has `prerequisites` only. If cross-topic
  recall is supposed to answer "what contrasts with X", v1 cannot. Synapse's call.
- **`planned, unused` was never exercised.** The smoke-run draft used every `core`/`support` row
  the brief selected, so the marker's path is untested. B8 on a real chapter will exercise it —
  briefs over-promise at 266 files in a way they do not at 12.
- **`review-draft` has no chapter-brief mode** ([article-loop.md](article-loop.md) §7). Unchanged,
  and B7 is where it gets decided.
- **`chapter-format.md`'s five fixed sections vs. the Critical Path's order.** New. Both are now
  real orderings over the same concepts, written by different skills, and nothing says which
  yields. B6 decides.
