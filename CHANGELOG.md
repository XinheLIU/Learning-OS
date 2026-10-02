# Changelog

Last updated: 2026-10-01

## 2026-10-01

### Added — Pre-write grilling and confirmation gates

- **`pre-write-grill` skill** — Intensive upfront questioning before material processing or writing begins. Establishes shared understanding on topic selection (which angle), scope boundaries (in/out), target length/depth, material priorities (primary/supporting/peripheral), example specifications (personal/external cases), and endorsed structure. Mandatory gate for original articles synthesizing scattered materials; optional for faithful single-source summaries. Output: confirmed specification document that feeds `/frame`. Prevents misaligned drafts by confirming intent before downstream work.
- **Confirmation gates in workflow** — Updated `frame` to require explicit author confirmation before proceeding ("Does this brief capture your intent? Ready to proceed?"). Added checkpoint after pre-write-grill outputs.
- **Brief requirement rule in write-content** — Original articles synthesizing scattered author materials now require brief (via `/pre-write-grill` → `/frame`). Faithful summaries of single external source remain optional. Distinction: transforming author's materials requires upfront shared understanding; summarizing one document does not.
- **Mid-workflow confirmation gates** — Added explicit author confirmation checkpoints after logic development (`develop-argument`: "Does this reasoning path make sense?") and after evidence development (`develop-examples`: "Do these examples support the reasoning appropriately?"). Prevents misaligned downstream work.

### Changed

- **Workflow reordered** — New sequence: `materials → pre-write-grill → frame → map (targeted) → logic ⇄ examples → write`. Material mapping now runs AFTER topic confirmed, with focus from grilling. External search happens during evidence development, not topic exploration.
- **Frame skill** — Added workflow section distinguishing two paths: "With pre-write-grill specification" (translate specification to brief) vs "Without pre-write-grill" (establish framing through questioning, legacy path). Added Step 5: explicit "Confirm before proceeding" gate.
- **Map-materials skill** — Now requires confirmed topic as input (from `/pre-write-grill`, `frame`, or explicit author statement). New Step 2: categorize materials by topic relevance before deep reading (likely relevant / possibly relevant / likely peripheral). Deep-read only relevant materials; light-categorize peripheral ones from filename/folder. Updated Handoffs to reflect workflow ordering.
- **Writing README** — Updated workflow diagram to include pre-write-grill as first stage with confirmation gate. Updated skills ownership table to include pre-write-grill and note map-materials timing.
- **Catalog** — Added `pre-write-grill` to writing category skills.

### Context

Addresses systematic workflow problems identified in writing test (tmp/writing-test): premature material processing before shared understanding, missing iterative confirmation loops, weak output not matching author intent. Root cause: `frame` is minimalist by design; `grill` runs post-writing as ship gate, not for establishing shared understanding. Solution: new pre-writing grilling phase that confirms topic, scope, length, material priorities, examples, and structure before any downstream processing.

Implementation phases complete:
- **Phase A (core skill)** — Created pre-write-grill skill, integrated into workflow, updated catalog
- **Phase B (reorder and gate)** — Updated map-materials to require confirmed topic and focus on relevant materials first
- **Phase C (mid-workflow confirmations)** — Added confirmation gates after develop-argument and develop-examples

Remaining work: Phase D (documentation updates for docs/adr.md, docs/exec-plans/writing.md, worked examples). See `/Users/xhl/.claude/plans/i-ran-a-writing-eventual-phoenix.md` for full improvement plan.

## 2026-10-02

### Added — writing memory and framework-driven explanation technique

- **Writing memory system** — `writing-memory/<topic>/<number>.md` stores immutable snapshots of understanding changes at any stage: framing, reasoning, evidence work, or after drafts. Each snapshot records the current judgment, grounds, topic relations, open questions, and piece pointers. `writing-memory/index.md` is derived from the latest valid snapshots and serves as navigation. `snapshot-writing` is the only writer; `frame` reads it before proposing related pieces. Snapshots are editorial state, not learner evidence.
- **Technique 18: Framework-driven explanation (框架式展开)** — Added to `write-content/references/techniques.md` under a new "Advanced structural techniques" section. When explaining complex concepts with multiple dimensions, build a multi-part logical framework (3-5 dimensions/types/stages) and systematically fill each part with: sub-concept definition, research establishing it (as chronological narrative), examples at 2-3 different scales, and transition to next part. Extracted from three Chinese expository samples showing systematic logic+example+research weaving.
- **Multi-scale example triangulation** — Enhanced Technique 2 with guidance on giving 2-3 examples at different scales (individual → team → organization → industry) that converge on the same principle, showing the mechanism is general rather than cherry-picked.
- **Systematic alternation at scale** — Enhanced Technique 6 with guidance on applying abstract/concrete alternation both at paragraph level and section level using the framework-driven pattern.
- **Research narrative patterns** — Created `write-content/references/research-narrative-patterns.md` with six execution patterns: progressive understanding, chronological discovery arc, research as specific investigation, introducing researchers with their insight, transition phrases signaling intellectual progression, and inline citations as narrative beats. Supports Technique 18 execution.

### Changed

- Updated `write-content/SKILL.md` to cross-reference Technique 18 and research-narrative-patterns.md in the Evidence and presentation section.
- Writing memory first snapshot: `framework-driven-explanation/001.md` documenting the pattern extracted from analyzing three Chinese samples (经济租, 系统思维, 组织资本).

## 2026-09-28

### Added — memory: a source registry, a material map, and a cross-topic index

Part A of [`docs/exec-plans/memory.md`](docs/exec-plans/memory.md). Three memories the system was
missing, plus the write-back that makes them iterate. Part B — running the chain on real
Transformer materials — is [`trials/transformer-memory/RUNBOOK.md`](trials/transformer-memory/RUNBOOK.md)
and has not been run.

- **`sources/<domain>.md` — a tiered, cross-topic source registry.** Tier 1/2/3, entry state
  `unrated`, and one rule that carries the whole file: **no verdict, no tier change**. A verdict is
  one line with an evidence pointer into `learning/` or `drafts/`. Previously `/survey` wrote a
  per-topic Read/Don't-read list that was forgotten the moment the survey ended, so every topic
  started from the same guess. Schema in the tracked `sources/README.md`; the domain files are the
  author's and are gitignored. ([ADR-011](docs/adr.md))
- **`<archive>/materials.md` — one map per archive, written once.** `/map-materials` ranks every
  file `key`, `redundant-of`, or `peripheral`, says what each teaches, and joins to the registry
  through a `source-id` column. `/survey`, `/curriculum`, and `frame` each used to scan the same
  folder cold and reach their own private conclusion; now they read a row. The archive stays
  read-only apart from this one file. ([ADR-008](docs/adr.md))
- **`learning/index.md` — the only cross-topic learner state.** Topics and the edges between them,
  node ids as `<slug>:<node>`, the same closed edge vocabulary as within a topic. `/survey`
  hypothesizes, `/reflect` earns with a case pointer, `/evaluate` refreshes the row. Markdown, so
  synapse indexes it through the manifest protocol without owning it. ([ADR-009](docs/adr.md))

### Added — two pipeline skills

- **`/curate-sources`** — discovers sources for a domain, appends them as `unrated`, refreshes
  what is still live, and applies pending verdicts to tier cells. The only writer of rows and
  tiers. Opposing verdicts on one row both apply, in id order.
- **`/map-materials`** — writes the map above, plus the `archive:` line in `survey.md` that every
  learning skill locates the archive through. No skill hard-codes a path.

### Changed — planning moved to the pipeline

- **`/survey` and `/curriculum` now live in `skills/pipeline/`.** The division that matters is
  *runs once* versus *iterates*: they decide what enters and in what order, and keeping them beside
  skills that run fifty times made the loop's boundary unreadable — most visibly in `/survey`
  quietly acquiring source discovery, a gather-stage job. Pipeline stages are now
  gather → process → scope → build. Counts: pipeline 11, learning 6, writing 11.
  ([ADR-010](docs/adr.md))
- **`/survey` refuses to run without the registry and the map**, and routes to the skill that
  writes the missing one. Its step 7 is now **Scope**: every registry source dispositioned
  `DEEP`/`SKIM`/`SKIP` against the mission, and every node assigned a `deep`/`connect` mode. The
  Roadmap no longer carries a critical path.
- **`/curriculum` writes `## Critical Path`** — every `deep` node exactly once, in dependency
  order, each row naming the `key` materials that teach it. It cites Scope sources and `key` map
  rows only.

### Added — `connect` nodes and the `[C]` lesson

- **Every Structural Memory node now carries a mode.** `deep` means the learner will *use* it;
  `connect` means they will *place* it. A `connect` node gets one ~10-minute `[C]` lesson — one
  excerpt, one edge statement in the learner's own words, zero drills, no quiz — and is earned by
  that edge. **It opens no `retrieval.md` row**, because it was never a claim to be able to use
  anything, and a ledger row for one fails on its first firing and reads as a broken scheduler.
  `/evaluate` reports `connect` nodes as `placed`/`unplaced`, never on the mastery rubric.
  ([ADR-012](docs/adr.md))

### Changed — writing reads learner memory, and evaluation reads writing

- **`frame` reads the map instead of scanning.** Selection rows are `m<nnn>` ids; only `key` rows
  may be `core` or `support`, and a `redundant-of` selection is refused **with the canonical id
  named**. Author markers are seeded from `earned` Structural Memory only — a marker traced to a
  `target` node is rejected — and `connect` nodes supply transitions, never sections.
- **`/evaluate` can claim the `Independent` rung** from a packaged draft, gated on four conditions:
  packaged with zero BROKEN refs, assistance declared and ≤ `hint`, every brief marker tracing to
  an `earned` node, and no `peeked` grill answer. `Independent` was defined in the evidence model
  and evidenceable by nothing. ([ADR-013](docs/adr.md))
- **`archive-materials` is the system's write-back.** It no longer writes `images-manifest.md` and
  `sources.md` — those duplicated the map. It fills `used-in` in `materials.md` and appends one
  `hold`/`promote` verdict per registry source the chapter leaned on, each citing chapter and
  section. It touches no `role` cell and no `tier` cell.
- **`/reflect` writes `demote`/`hold` verdicts** from error clusters, proposes `mode → deep` for
  `connect` nodes that keep recurring, and earns cross-topic edges in `learning/index.md`. It
  proposes; it never applies — tiers are `/curate-sources`'s and modes are `/survey`'s.

### Added — fixtures and the Part B runbook

- A 12-file synthetic fixture (`tmp/skill-tests/materials-map/`) with one duplicate pair and one
  off-topic folder, and a full-chain smoke run over it producing `learning/fixture-attention/`.
  The smoke run caught four contract defects, each fixed in the owning skill — listed in
  [`docs/exec-plans/memory.md`](docs/exec-plans/memory.md) §7.
- `tmp/skill-tests/make-fixtures.sh` and its runbook are now tracked: a gitignored generator makes
  no assertion reproducible from a clean checkout.
- `trials/transformer-memory/RUNBOOK.md` — 10 steps, 65 mechanical assertions, and **empty
  evaluation sections** for the author to fill before each step runs.

## 2026-09-22

### Changed — writing skills: MECE boundaries, tier structure, testable handoffs

- **Merged `frame-piece` and `frame-chapter` into one skill, `frame`, with two modes.** The two shared roughly 90% of their workflow — inventory the materials, build a ladder, disposition every source as `core`/`support`/`cut`/`gap`, emit `drafts/<slug>/brief.md` — and were already distinguished by a `brief-kind:` field the briefs carried. Two skills differing by a flag that already exists is one skill with a mode. `frame` now opens with an explicit **Step 0: pick the mode** (is there someone to argue against, or an order to walk?), which neither predecessor had and which is the question authors actually got wrong. Piece mode keeps the opponent hunt — external friction first, 议题 / 正方 / 反方 candidates, steelman and two-sided tests, the four load-bearing questions, the sharpen loop. Chapter mode keeps the coverage work — skeleton before materials, marker seeding from `learning/<slug>/notes.md`, the code-&-math gate, the coverage and residue checks. The three reference files (`brief-format.md`, `framing-questions.md`, `chapter-format.md`) now sit together under `frame/references/`, where `chapter-format.md`'s "everything else is `brief-format.md`" finally resolves to a sibling instead of a cross-skill path.
- **Deleted `write-content`'s Step 5 "Revise and deliver".** It ran the same `techniques.md` revision checklist that `review-draft`'s axis 2 runs, so either the drafter fixed everything and the reviewer was a no-op, or the reviewer was doing work the drafter claimed to have done. Drafting now ends at Step 4 and hands off; all review belongs to `review-draft`.
- **`grill`'s optional gate is now mechanical, and its output is machine-readable.** "Run it when the chapter carries a capability claim" required the caller to interpret the brief; the gate is now `brief-kind: chapter` **and** `教学目标` present — two field checks. Misses still route to exactly one of author gap or draft gap, but the two lists are written as separate files, `tasks-for-edit-unit.md` (in `edit-targeted`'s input format) and `gaps-for-learning.md`, alongside the human-readable `grill-log.md`.
- **Every writing skill now carries an `## Input Contract` and, for workflows, `## Completion Criteria`.** The framing skills' old termination condition was "loop until the author commits", which is not testable. `frame`'s completion is now enumerable: brief exists with the right `brief-kind`, selection map has ≥1 `cut` row, every inventoried source covered, spine in the author's words, plus per-mode conditions (piece: 议题 is a question, 正方/反方 non-empty, ≥2 pillars; chapter: `教学目标` present, every 二层 discharged or gapped, every code-&-math row placed, materials folder byte-identical).
- **Descriptions carry tier markers and time estimates.** Three tiers: **primitives** (atomic, under 20 min — `review-draft`, `edit-targeted`, `insert-inline-images`, `book-diagrams`), **workflows** (composite, 30–90 min, at least one author gate — `frame`, `write-content`, `grill`, `package-chapter`, `archive-materials`), **adapters** (derive from a finished draft, never edit back — `book-translator`, `create-tech-slides`, `build-skeleton`). The catalog had presented a 5-minute surgical edit and a 90-minute multi-round dialogue as peers.
- Added `skills/writing/brief-schema.json` — required fields per `brief-kind`, with the downstream check each one feeds.

### Removed

- **`check_image_refs.py` and the short-lived `verify-references` skill, both replaced by `skills/writing/scripts/verify_references.py`.** Three skills (`insert-inline-images`, `package-chapter`, `archive-materials`) were each invoking the same reference check, and `package-chapter` additionally carried seven inline greps for portability. That duplication was real, but a shared script is the fix for it — promoting the checker to a catalog entry solved a code problem with an abstraction the user has to navigate. The script now does both jobs: references by default, plus absolute paths, folder escapes, math delimiters, legacy renderer tags, unlanguaged fences and malformed `content:` links under `--portability`. One definition of "verified", one exit code, no catalog entry.

## 2026-09-06

### Changed — v3: HTML-first learning loop

- **The HTML course now carries the whole learning experience.** Reading, opening tasks, drills, quizzes, mini-cases, and spaced recall all complete inside the browser; chat is reserved for exactly two things — post-lesson bookkeeping (`done L<n>` + the lesson's completion manifest) and learner-initiated tutor Q&A. The learner's chat surface shrinks to four verbs: `/learn <slug>`, `done L<n>`, `/recall`, `sync recall`.
- **`/learn` runs three modes instead of one tutoring session.** `start` revises the next lesson against `notes.md` + `retrieval.md` and opens it (no tutoring); `done` parses the checkpoint manifest and does honest bookkeeping — attempt log, records, terms, node promotion, ledger rows, syllabus checkbox, refreshed recall queue — with at most one spot-probe when the manifest pattern is ambiguous; `tutor` is bounded Q&A whose corrected misconceptions land in `notes.md`. The segment-core teaching loop moves into the HTML lessons.
- **`/recall` stops firing in chat.** It plans (counts, courses, overflow order), refreshes `recall.html`'s embedded due queue, and applies the scheduling rules to the self-graded results the learner syncs back. Cold integrity is enforced by grading, not by chat discipline: an answer revealed before an attempt syncs as `walkthrough`.
- **`/curriculum` becomes orchestrator + builder.** Every lesson ends in a **checkpoint block** (completion-manifest button + next-step card); mini-cases get their own lesson files; `syllabus.md` carries the orchestration contract — a `Next:` pointer per lesson and optional recall `Gate:` conditions. New deliverable: `recall.html` (due items as flashcards: prompt alone, reveal, self-grade, sync block), linked from the shell.
- The checkpoint/recall **manifest** is the localStorage ↔ memory-file bridge: widgets persist state in the browser; the button packages it as JSON the learner pastes into chat. Assistance is inferred from the pattern (locked-correct-first-try → `none`; wrong-then-correct → `hint`; revealed-without-draft → `walkthrough`), not trusted blindly.
- Fixed the v2 doc drift in the same pass: `lesson-format.md`/`syllabus-format.md` no longer describe a `syllabus.html`; `notes-format.md` documents all eight consolidated sections; `framework-format.md` defines the Structural Memory *section* (with `notes.md#structural-memory:<node>` pointers in the ledger); curriculum evals updated to match; opening-task-first lesson order made consistent.
- Migrated `learning/herdr` as the v3 exemplar: checkpoint blocks on all lessons, `recall.html` + `assets/recall.js`, manifest packaging in `assets/quiz.js`, the Stage 2 mini-case promoted to `lessons/0004-mini-case-wait-and-read.html`, and `Next:`/`Gate:` fields in `syllabus.md`.

## 2026-09-03

### Added

- Added a second end-to-end runbook at [`trials/swe-basics/RUNBOOK.md`](trials/swe-basics/RUNBOOK.md): writing good code and design patterns at `--depth=quick`, two 30-minute sessions per day across three days, run against the learner's own repository inside a throwaway `git worktree`. Day 3 measures independence against a 6-item battery sealed on Day 0.
- The two trials are chosen to **fail differently**, not to repeat each other. herdr is bounded and its installed CLI settles every question, so it cannot catch a chain that lectures fluently from parametric memory. `swe-basics` has no ground truth and a literature that openly contradicts itself, so it gates on citation (every lesson claim links a real source), on argued SKIPs (≥3 — in an unbounded field what gets cut is the deliverable), and on refusing to flatten a live disagreement into a slogan.
- `swe-basics` covers `/synthesis-research`, which no trial reached before: entry gate, steelman of both positions, a located crux, insights citing ≥2 independent sources, HITL judgment the tutor may not ghost-write, and a negative check that a tension-free question (`what does the S in SOLID stand for`) is refused and routed rather than researched. This closes the `/synthesis-research` gap in [the learning execution plan](docs/exec-plans/learning.md) §7; the pipeline and writing skills remain uncovered.
- Running the two trials at **opposite ends of `--depth`** — herdr at `standard`, `swe-basics` at `quick` — is what establishes that the parameter is real. If both produce the same lesson lengths, `--depth` is a comment.
- Recorded that a rubric-graded battery fails differently from an answer-keyed one: generosity, not forgetting, is its default failure. The `swe-basics` runbook carries three literal grading questions (structural not cosmetic · cost stated · no pattern named without its problem) and scores an item 0 if any fails.

## 2026-09-02

### Added

- Added a `--depth` parameter to `/curriculum`: `quick` (~10 min lessons, 1–2 drills), `standard` (~20–30 min, 2–3 drills, the default), and `deep` (~60–90 min, 4–6 drills plus synthesis, multi-source reading with compare/contrast prompts, reference docs carrying edge cases and citations). Depth changes lesson length, drill count, and reading scope — not just prose length.
- Added an **Opening task** field to every lesson: a hands-on micro-task run in the real environment *before* any explanation. Do first, explain second.
- Added `[mini-case]` entries from Stage 2 onward — a simplified real scenario at walkthrough scaffolding, heavier than a drill and lighter than a Stage 4 transfer case. Pulls real practice earlier instead of reserving it for Stage 4–5. Optional at `quick` depth; required with multiple solution paths at `deep`.
- Added an end-to-end testing runbook at [`trials/herdr/RUNBOOK.md`](trials/herdr/RUNBOOK.md): herdr at `--depth=standard`, 60 minutes per day across three days, walking the whole chain — `/survey` → `/curriculum` → `/learn` → `/practice` → `/recall` → `/evaluate` → `/reflect`. Each step gives the learner the prompt to paste, what to watch for while it runs, a shell check, and numbered assertions. Day 3 measures independence against an 8-item battery sealed on Day 0 in a session that never saw a lesson.

### Changed

- Consolidated learner memory into `notes.md`. `framework.md` became its `## Structural Memory` section, `drills-*.md` became `## Micro-Skills`, and `playbook.md` became `## Playbook`. A topic now produces about ten artifacts rather than fourteen, and a skill reads one file where it previously read four.
- Removed `syllabus.html`. `syllabus.md` is the single source of truth for the plan and its progress; `index.html` renders it. Progress no longer has to stay synchronized across three files.
- Settled the format split: Markdown is internal memory, HTML is what a human reads. `notes.md`, `survey.md`, `syllabus.md`, `retrieval.md`, `case-*.md`, and `research-*.md` are Markdown; `index.html`, `lessons/`, and `reference/` are HTML.
- Updated all eight learning skills, their contract tests, and their handoff blocks for the consolidated files.

### Removed

- Removed the static `test-cases/` fixture tree. The fixtures duplicated contracts already stated in each skill's `## Contract test` block, and two of the four directories were written against the pre-consolidation file layout. The herdr runbook exercises those contracts live instead.
- Removed the `dp-stocks` trial and the earlier `herdr` cycle artifacts, both written against the v1 file layout. **The herdr cycle's `survey.md` and `RATING.md` were untracked and are unrecoverable.** The course output survives, archived at `learning/herdr-v1/`.

## 2026-09-01

### Added

- Added `recall`, the learning loop's return path and its eighth skill. It reads `retrieval.md`, selects everything due, tests it **cold** — the prompt is emitted alone and the turn ends there, so an answer can never share a message with its own question — scores on a correctness bit plus the existing assistance enum, and reschedules. It teaches nothing: a twice-lapsed item is flagged `re-tutor` and handed back to `/learn`. Runs in ten to fifteen minutes so it can actually be daily, and with no argument it unions the due items of every course under `learning/`.
- Added `retrieval.md` to `learning/<slug>/` — the retrieval ledger, one row per **item** (a schema or a term testable by a single cold prompt; a case is evidence, not an item). Rows open on **first successful demonstration** at assistance `none`/`hint`, never at exposure — a ledger seeded when a concept was introduced fails everything on its first firing and reads as a broken scheduler rather than as forgetting. Spec: `skills/learning/learn/references/retrieval.md`.
- Added the dogfood protocol, now maintained in the [learning execution plan](docs/exec-plans/learning.md), and the first trial artifacts under `trials/dp-stocks/cycle-1/`. Each improvement phase carries a mechanical acceptance criterion, validated by three-day dogfood cycles across three evidence layers — Layer 1 mechanical and gating, Layer 2 behavioral and gating only where the learner's ignorance is genuine, Layer 3 experiential and never gating.
- Recorded why there is no control arm and why a firing is scored on two axes rather than one; both decisions now live in [docs/adr.md](docs/adr.md).

### Changed

- `/learn` and `/practice` open ledger rows at the same moment they promote a framework node or earn an edge — first successful demonstration, `none`/`hint` only. `/learn` also re-tutors `re-tutor` rows before starting the next lesson and resets them, preserving the lapse count.
- **Attempt Log pruning is now gated on retention, not coverage.** The old trigger was lesson checkoff, which discarded per-item history exactly when a scheduler starts needing it — checkoff means "taught", not "retained". New trigger: `streak >= 2` on the matching ledger item, meaning two consecutive *unaided* cold recalls. If the section grows unwieldy, move it to its own file rather than discarding rows.
- **Interleaving is enforced rather than suggested.** Every `[S]` lesson carries an `Interleaves:` field naming at least one schema from a **non-adjacent** prior lesson — retrieving the lesson immediately before is fluency, since the material is still warm. `/curriculum`'s contract test rejects an `[S]` lesson whose field is absent, empty, or adjacent-only. A stated requirement no test checks is a suggestion.
- Rewrote `skills/learning/README.md` around the loop's new return path: `/recall` in the skills table and architecture diagram, `retrieval.md` in the file contracts, and the reason `/recall` sits outside the tier table — it owns no rung, because tiers describe how deep capability goes and retrieval describes whether it is still there.
- **Reworked `frame-piece` after its first real fixture run**, which exposed three defects. (1) It hunted for friction *inside* the corpus, so the 对立面 came out as the source's author and round one produced book-review candidates; added Hard Rule 4 — the material is evidence, not the opponent — and split friction into external (first) and internal (ammunition only). (2) 「为什么是现在」 was filed as configuration; promoted to the first load-bearing question, since a timeless corpus supplies no contestable question without an occasion. Candidates restructured from a single 对立面 into **议题 / 正方 / 反方** with steelman and two-sided tests. (3) The brief carried an angle and a flat selection map with nothing in between, leaving `write-content` to re-derive the argument from the corpus; added **Step 5 — build the argument ladder** (主题 → 一层论点 → 二层机制 → 三层具体展开) with sufficiency and independence tests, selection-map rows keyed to ladder nodes, author markers anchored to nodes, and 正方's strongest objection promoted to a pillar instead of buried in `gap`.
- `review-draft` axis 1 gained the matching checks — every pillar argued in order, every 二层 reaching its 三层, every author marker present at its anchor — plus a second paragraph test, *"would this paragraph mean anything to a reader who never saw the source?"*, which catches the book-review failure the flatness test misses.
- `llm-wiki-book` inherited the occasion-first and steelman patches (it references `framing-questions.md` rather than copying it); it still owes a book-scale 论点层级, tracked in the plan's build order.
- Synced the writing design to the shipped Stage 1 and Stage 3 behavior and replaced the hypothetical fixture walk-through with the actual 2026-09-01 run, which produced `tmp/learning-how-to-learn/drafts/ai-10x-and-taste/brief.md` (30 sections dispositioned: core 9 / support 5 / cut 18 / gap 1). Remaining verification is in [docs/exec-plans/writing.md](docs/exec-plans/writing.md).

## 2026-08-31

### Added

- Added `frame-piece`, the writing system's missing front end: it reads the materials, proposes contestable angle candidates — always including the corpus's own thesis, explicitly labelled so it can be rejected — asks the three questions that extract what a corpus cannot contain (what you want to argue back against, what the field believes that you don't, what you got wrong), and loops without a round cap until the author commits. Emits `brief.md`: angle, 对立面, reader, a selection map dispositioning every source section as `core` / `support` / `cut` / `gap`, the author's verbatim markers, and what the angle costs.
- Added `review-draft` and `edit-targeted`, the copilot pair. `review-draft` runs a depth gate against the brief before the craft checklist — a draft the source's author could have written gets "reframe or kill", not polish — and returns ranked findings, never rewrites. `edit-targeted` applies one finding to one location with a minimal diff and never volunteers adjacent improvements. Both run on any unit, from a paragraph up.
- Added depth techniques 15–17 to `write-content` (state the cost of your position; earned example over borrowed example; name the opponent) with matching revision-checklist gates.
- Added the writing-system diagnosis and five-stage design, now consolidated into [docs/adr.md](docs/adr.md) with unfinished adapter work in [docs/exec-plans/writing.md](docs/exec-plans/writing.md).

### Changed

- `write-content` is now brief-aware. With a brief it skips thesis derivation and the clarify round, drafts only `core` and `support` material, and weaves the author's markers instead of tension manufactured from the corpus. Without one it behaves as before, but names the failure at the point it occurs: when the derived thesis is one the materials already argue, it offers `/frame-piece` before proceeding.
- `llm-wiki-book` runs the same angle dialogue at book scale. Its spine is no longer derived from the wiki — a thesis the corpus supports is the sources' consensus with an arc — and its content-relation map became a selection map in the brief's vocabulary, so `build-skeleton` and per-chapter `write-content` consume it the same way.
- Rewrote `skills/writing/README.md` around the main line `frame-piece → write-content → review-draft ⇄ edit-targeted`, and documented the derive family (`book-translator`, `create-tech-slides`, and the planned per-medium adapters) that derives from a canonical draft and never edits back.

### Removed

- Retired `build-content-pipeline`: a project scaffold wearing a skill costume — it hard-coded one project's chapter list and mdBook conventions, and its `raw/wiki/book` layout contradicted the adopted `raw/notes/wiki/drafts` convention. Its layer conventions, promotion rule, and gitignore guidance moved into `skills/pipeline/README.md`.

## 2026-08-30

### Added

- Added `clean-notes`, the pipeline's process-stage skill: one raw capture becomes one cleaned, topic-clustered file — same-topic blocks moved together (confirmed with the user first), duplicates removed, headings and typos fixed. Chapter and page breakdown stays with `llm-wiki-ingest`.
- Added seven writing and document-organization skills: `build-skeleton`, `write-content`, `book-translator`, `insert-inline-images`, `book-diagrams`, `create-tech-slides`, and `organize-docs`.
- Added the writing workflow and its original design analysis, later consolidated into [docs/adr.md](docs/adr.md).

### Changed

- Restructured `skills/` into three system folders — `pipeline/` (gather → process → distill), `learning/` (the loop), `writing/` (output) — each with a co-located README contract. Flat symlink layers under `.claude-plugin/skills/` and the gitignored agent mirrors keep skill discovery working; skill names are unchanged.
- Split the monolithic README into a slim front door plus the three per-system contracts; `docs/WRITING.md` was absorbed into `skills/writing/README.md`.
- Updated the shared catalog to `sourcePattern: skills/{category}/{skill}/SKILL.md` with categories matching the system folders; reclassified `organize-docs` from writing to the information pipeline.
- Added the three-system roadmap, now consolidated into [docs/adr.md](docs/adr.md) and [docs/exec-plans/repository.md](docs/exec-plans/repository.md), and structured `tmp/` as the gitignored iteration corpus for pipeline and writing skills.
- Renamed the existing three-layer scaffold from `build-skeleton` to `build-content-pipeline` to keep its contract distinct from publication structure management.
- Extended the plugin and shared-catalog metadata from learning and wiki workflows into writing and publishing.

## 2026-07-26

### Added

- Added `framework.md` as structural learner memory for concepts, models, cross-mainline connections, and research frontiers.
- Added explicit cross-skill handoffs and evidence-gated course, loop, and research tiers.
- Added attempt logs, assistance metadata, retry results, and next-support-to-remove fields to learner evidence.

### Changed

- Reframed Learning OS around one shared, file-based learner memory under `learning/<slug>/`.
- Replaced one-dimensional survey triage with a 3–5 mainline by four-stage mastery matrix, behavioral milestones, target cells, and gap diagnosis.
- Limited curriculum authoring to knowledge and skill lessons; real-world Stage 4–5 work is now specified as `/practice` loop entries and closed by `/evaluate` evidence.
- Made `/learn` earn framework nodes, `/practice` earn framework edges, `/reflect` revise structure and advance its iteration, and `/research` extend the frontier.
- Made `/evaluate` assistance-aware: coached or unknown evidence is capped at `can-recall`, while higher mastery and tier transitions require low-assistance evidence.
- Updated README architecture and file contracts to document the shared-memory learning loop and strict boundary from the external wiki.
