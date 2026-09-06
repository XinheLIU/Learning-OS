# Structural Memory Format (notes.md section)

Last updated: 2026-09-06

> **v2 consolidation:** structural memory lives in `learning/<slug>/notes.md` as the `## Structural Memory` section — the separate `framework.md` file is retired. This document defines that section's schema; everything else about it (statuses, growth rules, ownership) is unchanged. Where older files say `framework.md#<node>`, the pointer is now `notes.md#structural-memory:<node>`.

`## Structural Memory` in `learning/<slug>/notes.md` is the topic's **structural memory** — the general framework linking knowledge, skills, and wisdom that the whole journey converges on. The other sections of `notes.md` hold *evidence* (linear: records, attempts, terms); this section holds *structure* (a graph: concepts, models, connections, frontier). It is the core output of every learning cycle: `/survey` seeds a top-down skeleton (a hypothesis), each loop pass earns pieces of it bottom-up, and the section records how far the learner's owned structure has converged toward — and grown past — the survey's map.

## Full template

```markdown
## Structural Memory

### Map

{One Mermaid `graph`. Subgraphs = mainlines from survey.md. Node class = status
(earned / target / frontier). Edge labels = the survey vocabulary; solid = earned,
dashed = hypothesized. REGENERATED from the tables below — never hand-drifted.}

### Layers

#### Representations
Canonical terms and notation live in notes.md `## Terms` — pointer only, no duplication.
{List only notation conventions that aren't terms, if any.}

#### Concepts
- **{concept}** · {mainline} · {target | earned | frontier} · {evidence pointer [assistance] | —}
  {one line, in the learner's words once earned}

#### Models
- **{model}** · {mainline} · {status} · {evidence pointer [assistance] | —}
  Holds when: {boundary}. Breaks when: {boundary}.

#### General frameworks
- **{framework}** · cross-mainline · {status} · {playbook position | research-*.md | —}
  {the structure it imposes — the learner's own design, defended or judged}

### Connections

| From | To | Type | Status | Earned by |
| :-- | :-- | :-- | :-- | :-- |
| {node} | {node} | bridges | earned | case-{slug} [assistance: hint] |
| {node} | {node} | special-case-of | hypothesized (survey v0) | — |

### Frontier

#### Open tensions
- {tension} — {why it matters to an earned model} → `/synthesis-research` candidate

#### People & papers
- {who/what} — {what it extends or threatens in the Layers above}   <!-- written by /synthesis-research -->

#### Missing links
- {node} ↔ {node} — should connect, no earned edge yet

### Iteration: {N}        <!-- /reflect bumps by 1 per pass that changed structure -->
```

## Statuses

- **Node:** `target` (survey says it matters; not yet earned) → `earned` (evidence exists) · `frontier` (beyond the course's scope; added by `/synthesis-research` or surfaced in practice).
- **Edge:** `hypothesized` (proposed by survey or research) → `earned` (a case or construction demonstrated it).
- **Edge types** are the survey's closed vocabulary: `bridges` | `prerequisite-of` | `contrasts-with` | `special-case-of`.

## Growth rules

- **Seed.** `/survey` writes v0: mainline subgraphs, matrix concepts as `target` nodes, cross-links as `hypothesized` edges, controversies into `### Open tensions`. Nothing in v0 is `earned`.
- **Earn.** A node or edge flips to `earned` only with an evidence pointer — a notes.md record, a `case-*.md`, or a `research-*.md` — produced at assistance `none` or `hint`. Coached evidence (`walkthrough`, `solution-shown`, `assistance-unknown`) never earns structure. Same construction-before-storage rule as Terms: the one-line gloss is in the learner's words, and AI MUST NOT pre-fill it.
- **Grow.** Nodes and edges the survey never predicted are added as `earned` (from the loop) or `frontier` (from research) — divergence from v0 is signal, not error.
- **Revise, don't delete.** Dead nodes and edges get `(archived: {reason})`; the history of wrong structure is valuable.
- **Iteration counter.** `/reflect` bumps it once per pass that changed structure — it is the convergence gauge, not a session count.
- **The Map is derived.** Regenerate the Mermaid graph from the Layers and Connections tables whenever they change; the tables are the source of truth.

## Section ownership

| Sub-section | Written by | Others |
| :-- | :-- | :-- |
| Map | whoever changed the tables (regenerate) | — |
| Layers | `/learn` promotes after a construction closes | `/reflect` revises minimally, archives |
| Connections | `/practice` earns edges from cases | `/survey` and `/synthesis-research` add hypothesized rows; `/reflect` revises |
| Frontier | `/synthesis-research` owns | `/survey` seeds Open tensions; `/practice`/`/reflect` may append candidates |
| Iteration | `/reflect` only | — |

`/curriculum` and `/evaluate` read the section; they never write it.

## Contract test

Given a fixture journey: v0 contains only `target` nodes and `hypothesized` edges plus seeded tensions; a node flips to `earned` only when its pointer cites `none`/`hint` evidence and carries a learner-worded gloss; an edge earned by a cross-mainline case cites that case; frontier entries name the earned Layer item they extend or threaten; archived structure keeps its reason; the Map matches the tables; Iteration only changes via `/reflect`.
