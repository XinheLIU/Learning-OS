# Architecture Decision Records

Last updated: 2026-10-01

This file records durable decisions and why they were made. Current work belongs in
[`exec-plans/`](exec-plans/).

## ADR-001: Use three systems with strict artifact boundaries

**Status:** Accepted

**Decision:** Organize the repository as an information pipeline, a learning loop, and a writing
system. Pipeline artifacts may ground learning and writing, but never count as learner evidence.
Learning artifacts may feed writing. A finished draft is the canonical source for derived media.

**Why:** The original system handled comprehension but left raw-material preparation and
independent output implicit. Writing is useful as graduation evidence only when source processing,
assisted learning, and unaided output remain distinguishable.

**Consequences:** Skills live under `skills/{pipeline,learning,writing}/`. Each system README owns
its contract. Cross-system handoffs are file conditions, not hidden session state.

## ADR-002: Keep nested ownership and flat discovery layers

**Status:** Accepted

**Decision:** Keep the physical skill tree grouped by system and generate flat symlink layers under
`.claude-plugin/skills/`, `.claude/skills/`, `.codex/skills/`, and `.opencode/skills/`.

**Why:** System folders make ownership legible, while agent skill discovery requires
`skills/<name>/SKILL.md` at a flat depth and the Claude plugin manifest accepts one skill directory.
Copying skills into both layouts would create divergent sources of truth.

**Consequences:** Adding, moving, or renaming a skill requires regenerating all four layers and
updating `catalog/skill-set.json`. The tracked plugin layer is the install surface; the nested tree
is canonical.

## ADR-003: Use inspectable Markdown as the only shared state

**Status:** Accepted

**Decision:** Skills coordinate through explicit files. External knowledge lives in the pipeline or
wiki; earned learner knowledge lives under `learning/<slug>/`; progress and evidence each have one
canonical owner.

**Why:** Hidden memory, duplicated dashboards, numeric mastery scores, and auto-authored learner
notes make claims hard to audit and assisted fluency easy to mistake for capability. At a single
learner's scale, databases and retrieval services add complexity without improving provenance.

**Consequences:** Learner records require evidence pointers and assistance levels. AI-produced
source summaries are never learner evidence. Derived summaries cite canonical records rather than
copying their state.

## ADR-004: Validate mechanics with dogfood cycles, not a controlled comparison

**Status:** Accepted

**Decision:** Validate learning-system changes with repeated three-day dogfood cycles. Mechanical
assertions gate every cycle; uncontaminated behavioral evidence may gate it; experiential self-report
sets the next target but never determines PASS.

**Why:** A controlled comparison is not credible here: `n=1`, no washout is possible, the learner is
also the designer, and blinding is impossible. Contract checks alone prove that files obey rules but
not that a person can use the chain.

**Rejected:** A differential-content A/B test would cost roughly 20-30 learner-hours and remain
unblinded. Contract-only verification is retained as one evidence layer, not the whole verdict.

**Consequences:** Trials establish only that the chain runs and its mechanics match the contract.
They cannot support claims that Learning OS beats ordinary study or that its interval ladder is
pedagogically optimal. Sealed behavioral batteries are authored before teaching and stored outside
the repository.

## ADR-005: Score retrieval on correctness and assistance separately

**Status:** Accepted

**Decision:** Every retrieval firing records two orthogonal facts: whether the cold attempt was
correct, and the maximum assistance used. Correctness governs lapse/reset; assistance governs how
far a pass advances.

**Why:** Assistance alone cannot represent a failed cold attempt followed by recovery. Correctness
alone treats coached and unaided retrieval as equivalent. A blended numeric score would introduce a
second mastery ladder and obscure both meanings.

**Consequences:** A lapse resets to the first interval regardless of later help. A hinted pass holds
its interval. `streak` counts consecutive unaided passes, so Attempt Log pruning at `streak >= 2`
means two cold recalls. Ledger rows cannot later be re-derived under a different rule because they
store outcomes, not full transcripts.

## ADR-006: Frame authored writing before drafting

**Status:** Accepted

**Decision:** Authored nonfiction starts with an angle dialogue that commits a contestable position,
argument ladder, selection map, and cut list in `brief.md`. `write-content` consumes that brief;
`review-draft` reports ranked findings; `edit-targeted` applies one local change. Faithful explainers
may intentionally use the brief-less path.

**Why:** Deriving a thesis from a source corpus reproduces the corpus's argument in cleaner prose.
An angle alone is also insufficient: without an argument ladder, drafting silently re-derives the
structure. Review and editing must remain separate so the author chooses which findings to apply.

**Consequences:** `frame` owns framing, `build-skeleton` owns file/navigation mechanics, and
`write-content` owns prose. The material is evidence, not the opponent. `build-content-pipeline` was
retired because it duplicated existing owners and hard-coded one project's layout.

## ADR-007: Derive one canonical draft into medium-specific outputs

**Status:** Accepted

**Decision:** Keep a medium-neutral canonical draft and use one adapter per publication medium.
Adapters derive outputs and never edit back into the canonical draft.

**Why:** WeChat, Xiaohongshu, books, and slide decks have different length, hook, formatting, and
audience constraints. A universal adapter would hide those differences and make round-tripping
ambiguous.

**Consequences:** `book-translator` and `create-tech-slides` are existing members of this derive
family. Future adapters follow the same rule, and `brief.md` may carry `target-media` as a routing
hint.

## ADR-008: Split the output into a large mapped archive and a small earned core

**Status:** Accepted

**Decision:** Everything the system produces belongs to one of two layers. The **archive** holds
raw materials plus one map (`<archive>/<topic>/materials.md`); it is large, unversioned, synced to
cloud storage, and read-only to every skill except the two that write `materials.md`. The **core**
holds plans, learner evidence, and drafts — `sources/`, `learning/`, `drafts/` — and is small and
versioned. Flow is one-way: archive → core, through the loop and the writing system. The only
write-back into the archive is `used-in` and confirmed renames. The chapter leaves the core by a
manual move into the writing repository.

**Why:** Mixing them made both worse. Putting 266 PDFs where the learner's evidence lives makes the
evidence unreviewable and the repository unclonable; keeping no map of the PDFs makes every skill
re-scan them and reach its own private conclusion. Separating them by *size and durability* rather
than by topic lets the core stay inspectable — the property [ADR-003](#adr-003-use-inspectable-markdown-as-the-only-shared-state)
depends on — while the archive stays complete.

**Consequences:** Learning skills locate the archive through one `archive:` line in
`learning/<slug>/survey.md`; no skill hard-codes a path. The learning record is kept after a
chapter ships — it is the proof of how the chapter was earned. A skill that wants to reorganize the
archive is out of bounds; that is `organize-docs`, an explicit author decision.

## ADR-009: Layer the memory in Markdown, one owner per layer

**Status:** Accepted

**Decision:** Memory is six layers, each a Markdown file with exactly one writing owner and named
readers: raw materials, the material map, the source registry, the plan, per-topic learner memory,
and one cross-topic learner index (`learning/index.md`). No skill reads or writes a database. A derived,
gitignored SQLite index may be added later when a stated trigger fires — a `/recall` across three
or more topics, or an edge lookup that needs more than one grep — rebuilt from the Markdown by one
stdlib script, never canonical. Semantic recall stays in synapse, which indexes this repository
through `.learning-manifest.json` and never writes it.

**Why:** A graph database for one learner buys queries nobody runs and costs the property that
makes the claims auditable. Markdown-canonical keeps every tier change, every earned edge, and
every source verdict reviewable in a diff. Making SQL *derived* rather than rejected means the
option stays open without any skill acquiring a dependency on a script.

**Consequences:** Cross-topic queries are greps until the trigger fires. `learning/index.md` is the
only cross-topic learner state, and its node ids (`<slug>:<node>`) are name references — a rename in one
slug can dangle an edge in another, which is an accepted cost recorded as an open question.

## ADR-010: Planning belongs to the pipeline; the loop is what iterates

**Status:** Accepted

**Supersedes:** the placement (not the content) of `/survey` and `/curriculum` in
[ADR-001](#adr-001-use-three-systems-with-strict-artifact-boundaries)'s learning system.

**Decision:** `/survey` and `/curriculum` move to `skills/pipeline/`. The pipeline's stages become
gather → process → scope → build. The learning loop contains only the skills that run again and
again over one topic's memory: `/learn`, `/recall`, `/practice`, `/evaluate`, `/reflect`,
`/synthesis-research`.

**Why:** The division that matters is *runs once* versus *iterates*. Survey and curriculum decide
what enters the system and in what order; they do not iterate, and keeping them beside skills that
run fifty times made the loop's boundary unreadable — most visibly in `/survey` quietly acquiring
source discovery, which is a gather-stage job.

**Consequences:** Category counts are pipeline 11, learning 6, writing 11. A mainline, target
stage, or node mode that looks wrong during the loop goes back to a pipeline skill; no loop skill
re-derives them.

## ADR-011: Rank sources and materials once, with evidence-gated changes

**Status:** Accepted

**Decision:** Four separate skills own four separate jobs. `/curate-sources` discovers sources and
owns `sources/<domain>.md`, where every new row enters `unrated` and a `tier` cell moves only by
applying a verdict. `/map-materials` ranks one archive's files once as `key`, `redundant-of`, or
`peripheral`. `/survey` reads both and scopes them for one mission. `archive-materials` and
`/reflect` write the verdicts that make the tiers move — from a shipped chapter and from error
clusters respectively — and neither may edit a tier.

**Why:** A per-topic reading list that is forgotten after the survey is the reason every topic
starts from the same guess. Ranking once, cross-topic, with evidence-gated changes, is what makes
the registry worth keeping. Separating *observing* from *deciding* keeps the skill that changes a
tier the one that read the whole file, and makes an unjustified tier change visible as a tier
change with no verdict.

**Consequences:** No verdict, no tier change — enforced by `/curate-sources`'s contract test.
Opposing verdicts on one row are normal and both apply in id order; a source that carried a chapter
and mis-taught a step is exactly the row worth looking at. `/survey` refuses to run when the
registry or the map is missing, rather than improvising either.

## ADR-012: Every node has a learning mode

**Status:** Accepted

**Decision:** `/survey` assigns every Structural Memory node a mode: `deep` (the learner will
*use* it) or `connect` (the learner will *place* it). A `deep` node gets K/S lessons, a place on
`/curriculum`'s `## Critical Path`, and a `retrieval.md` row when it is earned. A `connect` node
gets one `[C]` lesson of about ten minutes and is earned by **one edge** stated in the learner's
own words — it opens no ledger row, appears on no critical path, and is reported by `/evaluate` as
`placed`/`unplaced` rather than on the mastery rubric. Only a `/survey` deepening pass changes a
mode; `/reflect` may propose one.

**Why:** Shallow-versus-deep was the scoping decision the system kept making implicitly, in three
places at once (per-source triage, per-mainline target stage, and whatever `/curriculum` inferred).
Making it a property of the node states it once. The ledger rule is the load-bearing half: a
`connect` node was never a claim to be able to use anything, so a retrieval row for it fails on its
first firing and reads as a broken scheduler rather than as forgetting.

**Consequences:** A survey whose nodes are all `deep` has not scoped, and is rejected. `/practice`
may touch a `connect` node only as an edge endpoint; a case whose *subject* is one is reported as a
mode error rather than worked around. `frame` may use a `connect` node as a transition sentence,
never as a section.

## ADR-013: A shipped chapter at assistance ≤ hint is Independent evidence

**Status:** Accepted

**Decision:** `/evaluate` may claim the `Independent` rung from a packaged draft when four
conditions hold: `package-chapter` stamped it with zero BROKEN references; the assistance level is
declared and at most `hint`; every author marker in its `brief.md` traces to an `earned` node or
edge; and the grill log shows no `peeked` answer. `frame` seeds those markers from `earned`
Structural Memory only, and refuses a marker traced to a `target` node.

**Why:** `Independent` was defined in the evidence model and evidenceable by nothing, because every
loop artifact is assisted by construction. The writing system already produces the natural
independent output. The marker-tracing condition is what makes it evidence rather than fluency: a
chapter can be articulate about things its author never learned, and a marker pointing at a
`target` node is precisely that chapter.

**Consequences:** `/evaluate` reads `drafts/` as learner evidence, and `frame` reads `notes.md` —
the two links [`docs/exec-plans/repository.md`](exec-plans/repository.md) §1 said were missing. A
chapter drafted above `hint` is recorded as `can-apply` evidence and said so. Craft quality remains
`review-draft`'s judgment and never becomes a mastery level.

## ADR-014: Separate writing decisions, reasoning and evidence

**Status:** Accepted — 2026-10-01. Supersedes ADR-006's mandatory opponent and per-arrow manual gates.

**Decision:** `frame` owns question, reader gain, author answer and scope. `develop-argument` owns
logic and its derived map; `develop-examples` owns evidence and selection. They share a staged v2
brief. Articles can argue, explain or explore; chapters retain capability and dependency checks.
Readers accept legacy briefs without bulk migration. Authorized workflows continue across stages;
only unresolved author decisions or facts require another dialogue gate.

**Why:** A useful article can clarify a settled mechanism or narrow an open question. Requiring an
opponent, a minimum pillar count or a compulsory cut misclassifies those pieces. Evidence must be
checked for what it warrants, independently of how personal or vivid it is.

**Consequences:** Review ranks reader promise, reasoning, evidence and expression. Graphs derive
from justified relations; they do not create claims. Personal cases are preferred where useful,
not required. A targeted prose edit also updates the required Last updated metadata.

## ADR-015: Keep writing snapshots separate from earned learning state

**Status:** Accepted — 2026-10-01. Clarifies ADR-009's cross-topic state as learner state.

**Decision:** `snapshot-writing` alone appends numbered Markdown snapshots under `writing-memory/`
and derives its index from latest valid snapshots. Record substantive judgment, grounds, relations
or question changes at any stage; retries and wording changes add nothing. `frame` reads this
memory when developing a related piece. Previous snapshots remain immutable.

**Why:** Provisional understanding is useful writing material before it is mastered or published.
Mixing it into earned learning edges would hide the difference between author judgment and tested
capability. Keeping source/material pointers avoids duplicate registries.

**Consequences:** Source tiers and material usage retain their existing owners. No writing skill
writes mastery. Relations are attributed candidate/confirmed editorial connections, not earned
learner edges. No database, new search service, publishing adapter or workflow controller is added.
