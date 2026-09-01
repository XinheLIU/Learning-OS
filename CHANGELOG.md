# Changelog

Last updated: 2026-09-01

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
