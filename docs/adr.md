# Architecture Decision Records

Last updated: 2026-09-01

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

**Consequences:** `frame-piece` owns framing, `build-skeleton` owns file/navigation mechanics, and
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
