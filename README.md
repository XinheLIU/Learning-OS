# Learn & Wiki Platform

Last updated: 2026-07-13

<div align="center">
  <a href="../../README.md">Home</a> &bull;
  <a href="../../product-planning/README.md">Product Planning</a> &bull;
  <a href="../../architecture-design/README.md">Architecture Design</a> &bull;
  <a href="../../feature-delivery/README.md">Feature Delivery</a> &bull;
  <a href="../../visualization/README.md">Visualization</a> &bull;
  <a href="../README.md">Knowledge Management</a> &bull;
  <a href="../../team-collaboration/README.md">Collaboration</a> &bull;
  <a href="../../user-setup/README.md">User Setup</a>
</div>
<br>

A capability domain for personal knowledge, built as a **Learning OS**: a set of atomic components — knowledge distillation, knowledge graph, tutoring, deliberate practice, evaluation, and research — wired together through a shared file-based memory. Per this repo's maturity model, the Learning OS is a **Power** — multiple skills composed into a self-coordinating domain capability.

> **Status:** First version of all seven Learning OS skills is **implemented** under [skills/](skills/) — `survey`, `curriculum`, `learn` (+ `references/learning-theory.md`), `practice`, `evaluate`, `reflect`, `research` — each per its inline contract test (see [Implementation Order](#implementation-order)). The LLM Wiki Suite (Knowledge Distillation + Knowledge Graph) is live.



---

## Vision: One Engine, Five Questions

Five learning theories answer orthogonal questions of a single learning engine:

| Theory | Answers | Component(s) |
| :--- | :--- | :--- |
| Four Layers of Learning | What should be learned? | Knowledge Distillation, Knowledge Graph |
| Cognitive Load | How should knowledge be presented? | Curriculum Designer, AI Tutor |
| ICAP | How should the learner engage? | AI Tutor, Continuous Feedback |
| Deliberate Practice | How should skill improve? | Practice Coach, Learning Evaluator |
| Synthesis Research | How is new knowledge created? | Research Companion |

Each skill embeds its theory as operationalized directives (no theory essays in SKILL.md bodies); the full five-theory writeup lives once, in `skills/learn/references/learning-theory.md`.

## Architecture

Every box is one atomic component, implemented by exactly one skill (or, for the Knowledge Graph, the llm-wiki suite):

```text
                    Information  (sources, feeds, questions)
                         │
                         ▼
                    ┌─ /survey ─┐              investment gate: what deserves time
                         │
                         ▼
              Knowledge Distillation           llm-wiki (two-pass ingest)
                         │
                         ▼
                 Knowledge Graph               llm-wiki-init · llm-wiki · llm-wiki-lint → wiki/
                         │
         ┌───────────────┼────────────────┐
         ▼               ▼                ▼
    Curriculum        AI Tutor      Research Companion
    Designer          /learn           /research
    /curriculum
         │               │                │
         └───────────────┼────────────────┘
                         ▼
             Deliberate Practice Coach         /practice
                         │
                         ▼
                Learning Evaluator             /evaluate
                         │
                         ▼
                 Learning Memory               topics/<slug>/memory/  (convention, not a skill)
                         ▲
                         │
                Continuous Feedback            /reflect
```

### Atomic Skills, File Contracts

The design principle that makes this testable: **every skill is a function over files.** Each component declares what it reads and what it writes; components communicate only through those files, never through shared session state. Any skill can therefore be tested in isolation with fixture files — no upstream session required.

| Component | Skill | Reads | Writes |
| :--- | :--- | :--- | :--- |
| Investment Gate | `/survey` | web + user context | `memory/survey.md` |
| Knowledge Distillation | `llm-wiki` (ingest) | curated sources | `wiki/raw/`, `wiki/entities/`, `concepts/`, … |
| Knowledge Graph | `llm-wiki-init` / `llm-wiki` / `llm-wiki-lint` | `wiki/` | `wiki/index.md`, `log.md`, audit reports |
| Curriculum Designer | `/curriculum` | `survey.md`, `wiki/` | `memory/syllabus.md` |
| AI Tutor | `/learn` | `syllabus.md`, `survey.md`, `wiki/` | `model-*.md`, `schema-*.md`, `terms.md`, `_models.md` |
| Research Companion | `/research` | `wiki/`, `memory/`, fresh sources | `research-*.md` |
| Practice Coach | `/practice` | `_models.md`, `drills-*.md` | `drills-*.md`, `case-*.md` |
| Learning Evaluator | `/evaluate` | models + cases | `mastery:` frontmatter, `_models.md` summary |
| Continuous Feedback | `/reflect` | cases, `survey.md`, models | model edits, next micro-goals, `playbook.md` |
| Learning Memory | convention (not a skill) | — | `topics/<slug>/memory/` |

**The wiki/memory wall:** `wiki/` stores what the sources say (external, source-faithful); `memory/` stores what the learner has earned (constructed in dialogue). Learning OS skills never write to `wiki/`; llm-wiki never writes to `topics/`. Handoffs are soft — `/survey` offers to feed its curated source list into llm-wiki ingest, and downstream skills use `wiki/` pages as material *when present*. The Learning OS works without a wiki, but compounds with one.

Distillation into the learner's own four-layer structures happens **through tutoring**, not batch extraction — a model the learner didn't construct isn't theirs ("don't write a model the user didn't earn").

---

## 1. Learning OS Components

### 1.1 `/survey <field>` — Investment Gate

Runs before any information enters the pipeline. The deliverable is an investment decision, not a textbook: where does time go, and which sources deserve ingestion. This is cognitive-load management applied at the source-selection level — extraneous load is eliminated before it is ever consumed. Auto-inits `topics/<slug>/`; supports Path A/B entry (user has context vs full web research); covers history, key people, current state and controversies; ~30-minute cap.

Primary outputs, written to `topics/<slug>/memory/survey.md`:

**a) Learning mainline — time-allocation triage.** Every major subtopic classified:

```markdown
## Learning Mainline
| Subtopic | Investment | Why |
| :--- | :--- | :--- |
| <subtopic> | DEEP — 60% | foundational; everything else composes from it |
| <subtopic> | SKIM — 10% | need vocabulary only; low transfer value |
| <subtopic> | SKIP | overhyped relative to impact / not on the critical path |
```

The triage MUST be argued (why-column mandatory), and MUST name at least one SKIP — a mainline that cuts nothing is a reading list, not a gate.

**b) Curated sources — what to read, what to skip.**

```markdown
## Sources
### Read (ranked, with what each is FOR)
- <source> — best single explanation of <X>; read for the mental model, skip the appendix
### Don't read (with why)
- <source> — popular but derivative of <other>; <source> — outdated since <development>
```

**c) Prior-knowledge diagnosis** — per-subtopic table (novice / practitioner / expert with evidence), read downstream by `/curriculum` and `/learn` to set scaffolding level.

**Exit handoffs:** offer to feed the Read-list into llm-wiki ingest (soft — skippable); recommend `/curriculum` next.

> **Contract test:** `survey.md` contains an argued DEEP/SKIM/SKIP table with ≥1 SKIP; Read/Don't-read lists with reasons; diagnosis table present; wiki ingest offered, not forced.

### 1.2 Knowledge Distillation + Knowledge Graph — the llm-wiki suite

The distillation and graph components are owned entirely by the existing [LLM Wiki Suite](#2-karpathys-llm-wiki-suite-compounding-second-brain): `llm-wiki` performs two-pass extraction of curated sources into layer-tagged pages (distillation), and the vault itself — `entities/`, `concepts/`, `comparisons/`, `queries/`, interlinked and indexed — is the knowledge graph. There is **no separate `/distill` skill**; the Learning OS consumes the graph, it doesn't build it.

### 1.3 `/curriculum <topic>` — Curriculum Designer

A standalone planner (cognitive load + ICAP as design inputs). Reads `survey.md` (mainline + diagnosis; runs a 3-question mini-diagnosis if absent) and any ingested `wiki/` pages. Generates `topics/<slug>/memory/syllabus.md` covering the DEEP subtopics only:

```markdown
---
layer: framework
---
# Syllabus: <topic>
## Stage 1 — Prerequisite schemas   (warm-up, automate parts)
## Stage 2 — Small chunks            (one new concept per lesson)
## Stage 3 — Combine schemas         (integration only after parts are fluent)
## Stage 4 — Real task               (whole-task, reduced support)
## Stage 5 — Transfer                (new domain, no support)

Each lesson: Objectives · Prerequisites · Warm-up · Examples · Exercise ·
Reflection prompt · ICAP target (P/A → C → I) · Load note (what is deliberately deferred)
```

The syllabus is resumable — `/learn` sessions pick up at the first unchecked lesson.

**Boundary vs `/survey`:** the mainline is *strategic* triage — which subtopics get deep time, skim, skip, and which sources. The syllabus is *tactical* sequencing — in what order, with what load budget, lesson by lesson. Survey decides **what**; curriculum decides **how**.

> **Contract test:** given a fixture `survey.md`, the syllabus covers DEEP rows only; every lesson carries ICAP target and load note; stage order respects prerequisites-before-integration.

### 1.4 `/learn <topic>` — AI Tutor

Pure tutoring — no planning. Requires `syllabus.md` (offers to run `/curriculum` if missing). The loop per lesson: `estimate current schemas → identify missing schema → pose optimal next challenge → feedback`. Wiki pages, when present, serve as teaching material (worked examples, source quotes) — never as answers to hand over.

Calibration rules (teach to the learner, from the survey diagnosis):
- **Novice on this subtopic:** direct instruction — worked examples first, closed questions, small steps. You MUST NOT use discovery-style open prompts on a novice.
- **Practitioner+:** low support — transfer tasks, open problems, boundary probing.
- Re-assess per subtopic, not per session; move the ICAP ceiling up as schemas form (novice P/A→C, intermediate A→C, advanced C→I). Never skip schemas.

Load-management rules (hard constraints):
- One chunk per exchange; never two new concepts at once.
- Verify prerequisites by asking, not telling, before each new chunk.
- Components before integration; local structure before the whole — let the learner stand firm on one step before showing the next.
- No extraneous load: no tangents, no stacked analogies.

ICAP escalation (hard constraints):
- Never end a segment at P/A. Each chunk closes with learner construction: self-explanation or the learner's *own* example (the tutor's example doesn't count).
- Periodically escalate to I: tutor attacks the construction; learner defends or revises.
- **Prime directive: tutor, not a homework-answer machine.** Never hand over an answer the learner should construct — decompose and hint. Direct answers only for representations, never for schemas or models.

Output: `model-*.md` / `schema-*.md` in the learner's own words, layer-tagged, indexed in `_models.md`; representations accumulate in `terms.md`.

> **Contract test:** a novice run uses worked examples and one-chunk pacing; every segment ends with learner-generated construction; direct-answer requests get decomposed instead.

### 1.5 `/research <question>` — Research Companion

The one component that **creates** knowledge instead of consuming it. Everything upstream feeds it: `wiki/` holds what the sources say, `memory/` holds what the learner has earned — research overlays them and produces the judgment that exists in neither. The deliverable is always **written** — writing is where the thinking completes, not packaging.

**Entry gate — no tension, no research.** Research starts from a live tension: two credible sources that disagree, a source contradicting an earned `memory/` model, a `contested: true` wiki page, or a question no single source answers. Anything else is routed away: quick factual question → direct answer or wiki query; field overview → `/survey`; "understand X properly" → `/curriculum` + `/learn`. Scoped by **question**, never by time budget — one question per report.

The workflow, always the full arc:
- **Assemble heterogeneous material** — fresh sources, `wiki/` pages, earned `memory/` models and cases. The highest-value connections cross the wiki/memory wall: an external claim placed against a model the user built (the John Snow move — the map plus the death records, neither sufficient alone).
- **Map the tension.** Organize by *issue*, never by author. **Steelman gate:** state each position in terms its holders would endorse — can't? keep reading. **Name the crux:** where the disagreement bottoms out — assumption, evidence, or values.
- **Hunt connections.** Standing question set: What's missing? Which assumptions conflict? Can two fields combine? What does the user's own model predict? **Combination rule:** every insight cites ≥2 independent sources whose *combination* — not either alone — supports it.
- **Draw the judgment with the user** (HITL — never ghost-written), then answer **"so what?"** — the decision that changes, plus a prediction or falsifier.

**Report format** — `memory/research-<question-slug>.md`:

```markdown
---
layer: framework
---
# Research: <question>
## The Question (one sentence, confirmed with the user)
## The Tension — positions steelmanned; the crux named (assumption / evidence / values)
## Connections — what emerges between materials; each insight with its source combination
## My Judgment — the user's position, formed in dialogue (HITL — this section is theirs)
## So What — the decision this changes + a prediction or falsifier
## Open Questions — decomposed candidates not pursued
```

**Feedback into the system:** the report is `can-generate` evidence for `/evaluate` — the highest mastery tier; a judgment that contradicts an earned model is flagged for `/reflect`; reports may be filed into the wiki via ingest (soft, never forced).

**MECE boundaries:** locating and restating what sources say → wiki query or direct answer, not research; field triage and controversy *surfacing* → `/survey`; internalizing established knowledge over weeks → `/curriculum` + `/learn`. Research *resolves* surfaced controversies into judgment.

> **Contract test:** report contains a steelmanned tension with a named crux; every connection cites ≥2 independent sources whose combination supports it; Judgment is the user's or explicitly absent; So What names a changed decision and a falsifier; one question per report.

### 1.6 `/practice <skill-or-scenario>` — Deliberate Practice Coach

Real cases only; model-mapping against `_models.md`; "no model fits" is signal, not failure; 60-second case files. The deliberate-practice pipeline:

- **Micro-skill decomposition** (first time a skill is practiced). Decompose the target skill into trainable micro-skills, each with failure modes, success criteria, and a difficulty curve. Persisted as `memory/drills-<skill-slug>.md`; sessions then target one micro-skill at a time. (E.g. presentation → story / slide design / voice / timing.)
- **Micro-goal opening.** Every session sets one high-resolution goal tied to a micro-skill ("identify the bottleneck within 3 questions", not "get better at profiling").
- **Learning-zone calibration, announced.** Cruising → harder variant; panic → shrink scope. The coach states the adjustment out loud so calibration is visible.
- **Immediate feedback.** Errors corrected the moment they occur, named precisely.
- **Error recording** — case-file fields feeding `/reflect`'s compression:

  ```markdown
  **Micro-goal:** <this session's target>
  **Errors made:** <error> — <recurring? link prior case>
  ```

> **Contract test:** drills file created on first use; every case file has micro-goal + errors fields; difficulty adjustment announced mid-session.

### 1.7 `/evaluate <topic>` — Learning Evaluator

A standalone, read-mostly assessor: a snapshot of **how deep mastery actually is**, separate from the feedback loop. Per knowledge node, an evidence-backed rubric level — a level may only be claimed with a pointer to evidence:

| Level | Evidence required |
| :--- | :--- |
| can-recall | correct restatement in session |
| can-apply | a `case-*.md` where the model was used successfully |
| can-transfer | a case from a *different* domain |
| can-teach | learner explanation that survived tutor challenge (ICAP-I) |
| can-generate | a `/research` report (judgment + so-what) or novel model |

Written into each node's frontmatter (`mastery: can-apply`) and summarized in `_models.md`. Layer distribution (how much is representation vs framework) reported as a depth gauge. **No numeric scores, ever** — "Schemas 92%" is LLM confabulation.

> **Contract test:** given fixture models + cases, every claimed mastery level cites an evidence file; nodes without evidence stay at the lowest supportable level; output contains no percentages.

### 1.8 `/reflect <topic>` — Continuous Feedback

The loop-closer: **what should change next**, consuming `/evaluate`'s snapshot rather than duplicating it. Keeps: three questions, minimal model edits, archive-don't-delete. Adds:

- **Error compression.** Scan all `case-*.md` **Errors made** fields; surface patterns ("variant of this error in 3 of 5 cases"). Recurring errors become the next `/practice` micro-goals — closing the deliberate-practice loop.
- **Mainline drift check.** Compare time actually spent (cases, models) against `survey.md`'s learning mainline; flag drift ("your mainline says DEEP on X but all 5 cases are on skim-tier Y — recalibrate the mainline or the habit?").
- **Adversarial defense gate before playbook synthesis (ICAP-I).** At the 5+ case threshold, the agent steelmans 2–3 objections to the user's positions; the playbook is written only for positions that survive or are revised — keep positions defensible from both sides, and guard against self-congratulation.

**Boundary vs `/evaluate`:** evaluate measures state (mastery snapshot); reflect changes trajectory (model edits, next micro-goals, playbook). Reflect may recommend running `/evaluate` first but never writes mastery levels itself.

> **Contract test:** recurring error surfaced across ≥2 cases; drift vs mainline reported; playbook refused until positions survive the steelman.

---

## 2. Karpathy's LLM Wiki Suite (Compounding Second Brain)

An elegant, low-overhead suite modeled on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). By consolidating complex pipelines into a cohesive triad, this suite enables agents to build a compounding, self-indexing knowledge base of interlinked markdown pages while preserving taxonomic tag consistency, absolute source immutability, and human-in-the-loop takeaways. Within the Learning OS it implements the **Knowledge Distillation** and **Knowledge Graph** components.

| Skill | Trigger Commands / Keywords | Purpose & Description | Output / Target |
| :--- | :--- | :--- | :--- |
| **[llm-wiki-init](skills/llm-wiki-init/)** | `llm-wiki-init`, `create a wiki`, `start a knowledge base` | Scaffold directory structures, configure `SCHEMA.md` conventions, define taxonomic tag taxonomy, and initialize `index.md` and git tracking. | `wiki/SCHEMA.md`, `index.md`, `log.md` |
| **[llm-wiki](skills/llm-wiki/)** | `llm-wiki`, `ingest source`, `query wiki`, `wiki-query` | Captures raw sources (`raw/`), performs two-pass parallel extraction & page generation, automatically manages indexing, handles updates/contradictions, and files valuable query results. | `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `index.md` |
| **[llm-wiki-lint](skills/llm-wiki-lint/)** | `llm-wiki-lint`, `wiki lint`, `audit wiki`, `health-check` | Runs a comprehensive 12-point health audit covering broken links, orphan nodes, frontmatter compliance, raw source SHA-256 drift, contested claims, and stale pages. | `log.md`, `log-YYYY.md` (rotation), detailed reports |

---

## Core Conventions

### Learning Memory (a convention, not a skill)

`topics/<slug>/memory/` is the Learning OS's **earned-knowledge** graph (`wiki/` holds external knowledge and is owned by the llm-wiki suite):

```text
topics/<slug>/
├── README.md            # slug, dates, model count, mastery summary line
└── memory/
    ├── survey.md        # gate output: learning mainline + curated sources + diagnosis + map
    ├── terms.md         # representations (one-liners)
    ├── schema-*.md      # layer: schema
    ├── model-*.md       # layer: mental-model
    ├── _models.md       # index grouped by layer, with mastery levels
    ├── syllabus.md      # /curriculum output, resumable by /learn
    ├── drills-*.md      # /practice micro-skill decompositions
    ├── case-*.md        # practice cases with micro-goals + errors
    ├── research-*.md    # /research reports (tension → connections → judgment)
    └── playbook.md      # defended framework (after /reflect gate)
```

Frontmatter carries the graph: `layer:`, `mastery:`, `[[links]]`. Every skill reads memory before acting and writes evidence after — every future lesson starts from there, with zero new infrastructure.

### Wiki Storage Hierarchy (LLM Wiki Vault)

```text
wiki/
├── SCHEMA.md               # Rules, conventions, domain tags, & thresholds
├── index.md                # Automatically regenerated catalog root (with summaries)
├── log.md                  # Chronological append-only action record
├── raw/                    # Layer 1: Immutable source material
│   ├── articles/           # Captured web posts and notes
│   ├── papers/             # Academic pdfs and summaries
│   ├── transcripts/        # Video/audio text captures
│   └── assets/             # Raw images and supplemental files
├── entities/               # Layer 2: People, products, orgs, models
├── concepts/               # Layer 2: Ideas, algorithms, methodologies, patterns
├── comparisons/            # Layer 2: Side-by-side analyses
└── queries/                # Layer 2: Preserved high-value query answers
```

> [!IMPORTANT]
> **Contested Claim Tracking**: If a new source contradicts an existing page, the agent does not silently overwrite it. Instead, both positions are documented with dates and sources, and the target page's frontmatter is marked with `contested: true` and `contradictions: [other-page-slug]`. The `llm-wiki-lint` tool actively audits these flags to surface contested content for human resolution.

### Cross-Cutting Rules

- **Tutor, not a homework-answer machine** — identical one-sentence rule in `/learn`, `/practice`, and `/research` (the one deliberate redundancy; it guards the suite's core value).
- **Handoff chain:** survey mainline/sources → llm-wiki ingest (soft) + `/curriculum`; survey diagnosis → tutor scaffolding level; case errors → reflect compression → next practice micro-goal; evaluate snapshot → reflect trajectory changes; defended positions → playbook; controversies surfaced anywhere (survey, tutoring, contested wiki pages) → `/research` candidates; research judgments that contradict earned models → `/reflect`.
- **Evidence before claims:** mastery levels, generative claims, and playbook positions all require pointers to evidence files. No self-reported competence.
- **wiki/memory wall:** Learning OS skills never write `wiki/`; llm-wiki never writes `topics/`.
- **Files are the only interface:** no skill depends on another skill's session state — only on its written outputs. This is what keeps every component independently testable and replaceable.

---

## Inspiration & Comparative Analysis

The **LLM Wiki Suite** is directly inspired by [Andrej Karpathy's `llm-wiki` design pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). We have taken Karpathy's high-level concept of a persistent, compounding, LLM-maintained second brain and instantiated it into a suite of production-grade agent skills.

### Key Differences & Extension Points

While the core philosophy remains aligned—offloading the tedious bookkeeping of a knowledge base to an LLM—our implementation introduces several critical extension points to handle real-world agentic execution:

| Architectural Component | Karpathy's Concept (`llm-wiki.md`) | Our Implementation (`llm-wiki-*` Suite) |
| :--- | :--- | :--- |
| **Wiki Organization** | Generic directory of markdown files. | Formalized two-layer schema: Layer 1 (`raw/` sources) and Layer 2 (`entities/`, `concepts/`, `comparisons/`, `queries/`). |
| **Ingestion Protocol** | Single-pass ingestion. | **Two-Pass Parallel Ingest** for long files (Pass 1: Extract, Pass 2: Write) + Socratic discussion of takeaways before filing. |
| **Incremental Ingest** | Full re-processing of inputs. | **Differential Ingest** with skip logic using body-only SHA-256 signatures and chronological logs. |
| **Linter & Cleanup** | General advice to audit files. | Automated **12-point health linter (`llm-wiki-lint`)** grouped by severity (Critical to Info) with safe auto-fixes and human-review flags. |
| **Index & Navigation** | Continuous index rewriting. | Fast, programmatic index updates (`index.md`) using strict structural thresholds to split/map topics as the vault scales. |
| **Contradiction Management** | Manual resolution. | Active **Contradiction Handling**: frontmatter marking (`contested: true`, `contradictions: [...]`) with dedicated auditing in the linter report. |

---

## Implementation Order

Each step is verified against its component's contract test (inline above) using fixture files — no upstream session needed:

```text
1. skills/survey/       (rework: mainline triage + curated sources + diagnosis + soft wiki handoff)
2. skills/curriculum/   (new: standalone syllabus generator from survey.md)
3. skills/learn/        (rebuild: pure tutor over syllabus.md + references/learning-theory.md)
4. skills/practice/     (upgrade: decomposition + micro-goal + zone + errors)
5. skills/evaluate/     (new: evidence-backed mastery snapshot)
6. skills/reflect/      (upgrade: error compression + drift check + defense gate)
7. skills/research/     (rework: tension-gated synthesis — connections, judgment, so-what)
```

Steps 1–3 first: the survey → curriculum → tutor handoff (`survey.md` → `syllabus.md` → sessions) is the OS's most load-bearing seam, and each link can be fixture-tested before the next is built.

## Out of Scope / Explicit Non-Goals

- **No `/distill` skill** — distillation belongs to llm-wiki ingest (soft handoff only).
- **No numeric mastery scores** — rubric levels with evidence only.
- **No graph database / MCP memory store** — the markdown vault is the graph.
- **No hard llm-wiki dependency** — the loop must work wiki-less for casual topics.
- **No shared session state between skills** — files are the only interface.
- **`build-skeleton` stays retired**; the llm-wiki suite is untouched (boundary docs only).

## Future Possibilities & Roadmap (LLM Wiki Suite)

To expand further on our implementation and address edge-case friction points uncovered in actual day-to-day use, we have laid out the following roadmap for upcoming iterations:

### 1. Triage-First Ingestion (`llm-wiki-triage`)
* **Goal**: Prevent LLMs from writing directly to the vault before confirmation.
* **Mechanism**: Develop a front-facing dry-run mode that scans incoming raw material, generates a structural diff showing proposed page creations or edits, and displays a report of any potential contradictions *before* writing to disk.

### 2. Walk-Up Path Discovery
* **Goal**: Allow tools to resolve the wiki path from any subdirectory within the workspace.
* **Mechanism**: Enable recursive upward directory discovery (scanning for `wiki/SCHEMA.md`) so that agents can execute wiki commands regardless of their current working directory context.

### 3. Local Hybrid Search MCP Integration
* **Goal**: Scale beyond simple index-file parsing when vaults grow to thousands of pages.
* **Mechanism**: Integrate specialized local markdown search engines (such as `qmd` or lightweight BM25/vector search CLI utilities) via a Model Context Protocol (MCP) server, allowing the agent to perform instant, high-relevance hybrid queries.
