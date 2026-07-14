---
name: llm-wiki-book
description: "Karpathy's LLM Wiki: generate a book PLAN (not the book) from an existing wiki. Produces a thesis, narrative arc, chapter-by-chapter table of contents, a chapter↔wiki content-relation map, and a gap list of further research and writing needed. Use when the user wants to turn a wiki into a book, draft a book outline from a knowledge base, plan a book, or mentions 'book idea', 'book plan', 'book outline', or 'turn the wiki into a book'. Plan only — never drafts chapter prose."
license: MIT
metadata:
  hermes:
    tags: [wiki, knowledge-base, book, planning, mental-models, narrative]
    category: research
    related_skills: [llm-wiki, llm-wiki-init, llm-wiki-lint]
---

# Karpathy's LLM Wiki — Book Plan

Turn an existing wiki into a **book plan**. Output is a plan only: thesis, narrative
arc, table of contents, a chapter↔wiki content map, and the research/writing still
needed. **Never draft chapter prose** — that is a separate, later task.

**See also:** `llm-wiki` (ingest/query) · `llm-wiki-init` (setup) · `llm-wiki-lint` (audit)

## When This Skill Activates

- Asking to turn a wiki into a book, draft a book outline, or plan a book
- References to "book idea", "book plan", "book outline", "TOC from the wiki"

## Wiki vs. Book — the abstraction ladder

A wiki and a book sit at different rungs of the same ladder. The plan's entire job is
to lift the wiki up two rungs. Know which rung each page is on before planning.

| Rung | What it is | How it shows up in a wiki |
|------|-----------|---------------------------|
| **Representation** (表征) | Minimal building blocks: concepts, names, boundaries, indicators | A page defining one term (`opportunity-cost`, `GDP`) |
| **Schema** (图式) | A recognizable chunk: many representations glued into a pattern | A page describing a structure or category (`asset-types`, `cost-framework`) |
| **Mental model** (心智模型) | A schema that *runs* — has variables, causality, feedback, boundary conditions; lets you predict "if A under X, then B" | Rare in wikis. Usually latent across several pages, never made runnable |
| **Explanatory framework** (解释框架) | The full map of a domain: standard concepts, key models, major debates, what counts as a good explanation | Never in a wiki. This is the book's spine |

**The two differences that make a book a book:**

1. **Narrative.** The book *and each chapter* has a main theme that connects otherwise
   isolated concepts, entities, and examples. A wiki links pages; a book argues a
   through-line. The plan must name the spine and each chapter's connecting thread.
2. **Mental models & frameworks over facts.** A wiki stores representations and schemas.
   A book's value is elevating clusters of them into *runnable* mental models (causality,
   feedback, boundaries) and arranging those under one explanatory framework. The plan
   must say, per cluster, what it takes to make it run.

## Steps

### 1. Orient

Same orientation as every wiki operation:

① Read `SCHEMA.md` — domain, conventions, tag taxonomy.
② Read `index.md` — full page inventory with summaries.
③ Scan recent `log.md` — what's been ingested, what's contested.

Then build a working inventory: list every entity, concept, and comparison page with its
tags. For wikis over ~30 pages, read the pages in parallel (one sub-agent per cluster of
related pages) and have each return a 2-line digest: *core claim* + *what other pages it
truly depends on* (not just what it links to — the user has flagged that wiki links are
often loose; judge real dependency from content).

### 2. Diagnose each cluster on the ladder

Group pages into clusters by genuine conceptual dependency, not by existing `[[wikilinks]]`.
For each cluster, label its highest current rung:

- **Representation/Schema only** — defines and categorizes, but has no causality or
  prediction. Most wiki pages are here.
- **Latent mental model** — the causal/feedback structure is implied across pages but
  never stated as a runnable model with variables and boundaries. These are the gold:
  the book's job is to make them explicit.

Record, per cluster: the pages in it, its current rung, and the mental model it *could*
become if elevated.

### 3. Find the explanatory framework (the spine)

Articulate the book's central thesis in one paragraph — the "grand picture" of the domain
that the wiki only covers in pieces. This is the explanatory framework: the coherent system
view that says how the domain's models fit together and what counts as understanding it.

If the wiki supports more than one viable spine, present 2–3 ranked, with a one-line
trade-off each, and recommend one. Don't pick silently.

### 4. Design the narrative arc

State how the reader's mental model should evolve from chapter 1 to the end — what they
believe at the start, what each act overturns or builds, where they land. This is the
through-line that makes it a book rather than an encyclopedia. Name the arc explicitly
(e.g. "naïve intuition → why it fails → the running model → boundary conditions → mastery").

### 5. Draft the table of contents

One entry per chapter. Each chapter **must** declare all four:

- **Theme / connecting thread** — the single idea this chapter argues; the thread tying
  its concepts, entities, and examples together. If you can't name it in one sentence, the
  chapter isn't a chapter yet.
- **Mental models taught** — the runnable model(s) the reader walks away able to *use*.
  Tie each to its cluster from step 2.
- **Wiki pages drawn on** — the `[[pages]]` this chapter is built from (content relation).
- **Examples / entities / case studies** — concrete material (often the `entities/` pages
  and `case-study`-tagged content) that grounds the model.

Order chapters to serve the narrative arc from step 4, not the wiki's alphabetical index.

### 6. Build the content-relation map

A table mapping the wiki to the book, in both directions — this is what makes the plan
auditable:

- **Chapter → pages**: which wiki pages feed each chapter.
- **Coverage status** per page: `core` (chapter is built on it) / `supporting` /
  `unused` (page exists but no chapter needs it — flag for the user; may signal a missing
  chapter or out-of-scope content).
- **Chapters with thin or no wiki backing**: chapters the narrative demands but the wiki
  can't yet support — these become the top of the gap list.

### 7. Gap list — further research & writing needed

The most useful part of the plan. Separate into:

- **Elevate to mental models** — clusters stuck at representation/schema that the book
  needs runnable. State what's missing: variables, the causal mechanism, feedback loops,
  or boundary conditions ("works when X, breaks when Y").
- **Missing connective tissue** — narrative/argument the wiki has no page for, because a
  wiki stores nodes, not through-lines. This is expected, not a wiki defect.
- **Thin pages** — pages too shallow to carry a chapter; note what depth is missing.
- **Missing examples/entities** — chapters whose model has no concrete case to anchor it;
  suggest what to find or ingest.
- **New sources to ingest** — external research the book needs that the wiki lacks; route
  through the `llm-wiki-ingest` flow.

### 8. Write the plan to the wiki

- Default path: `queries/book-plan-<topic>.md` (no new top-level dir; stays within SCHEMA
  conventions). Confirm the path with the user first.
- Frontmatter: `type: query`, tags from the taxonomy, `sources:` listing the wiki pages
  the plan rests on.
- Use `[[wikilinks]]` for every page referenced so the plan stays navigable and the lint
  skill can check it.
- Append to `log.md`: `## [YYYY-MM-DD] book-plan | <topic> (filed: yes)`.
- Report to the user: the chosen spine, chapter count, unused-page count, and the top 3
  gaps.

## Output Template

```markdown
# Book Plan: <Working Title>

## Thesis (the explanatory framework)
<one paragraph — the grand picture the book argues>

## Narrative Arc
<how the reader's mental model evolves, start to finish>

## Table of Contents

### Ch 1 — <Title>
- **Theme:** <one-sentence connecting thread>
- **Mental models:** <runnable model(s) taught>
- **Built on:** [[page-a]], [[page-b]]
- **Examples:** [[entity-x]], <case study>

### Ch 2 — ...

## Content-Relation Map
| Chapter | Core pages | Supporting | 
|---------|-----------|------------|
| 1 | [[page-a]] | [[page-b]] |

**Unused pages:** [[page-z]] — <why; missing chapter or out of scope?>
**Thin-backing chapters:** Ch N — <what the wiki can't yet support>

## Gaps — Further Research & Writing
- **Elevate to mental model:** <cluster> needs <variables / mechanism / feedback / boundaries>
- **Connective tissue:** Ch N needs <narrative the wiki has no node for>
- **Thin pages:** [[page]] — <missing depth>
- **Missing examples:** Ch N — <case to find>
- **Ingest:** <external source the book needs>
```

## Pitfalls

- **Plan only — never write chapter prose.** If the user wants drafting, that's a separate
  pass after the plan is approved.
- **Don't trust `[[wikilinks]]` as the dependency graph.** The user has flagged that wiki
  links are often loosely related. Judge real conceptual dependency from page *content*
  when clustering.
- **Don't let the TOC mirror the index.** Alphabetical concept pages are not chapters. The
  order must serve the narrative arc; a chapter without a one-sentence theme is not a chapter.
- **Name the spine before the chapters.** No explanatory framework → it's a wiki dump with
  headings, not a book.
- **Treat "missing connective tissue" as expected.** A wiki has no narrative nodes by design;
  the gap list surfacing them is the plan working, not the wiki failing.
- **Surface unused pages.** They either reveal a missing chapter or content outside the
  book's scope — both are decisions for the user.
- **Orient first.** SCHEMA + index + recent log before planning, same as any wiki operation.
