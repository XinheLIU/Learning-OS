# The Writing System

Last updated: 2026-09-01

**Turn earned knowledge into published output — and let the writing show you what you haven't learned yet.**

Writing is the output stage of Learning OS, and its proof: a published article or chapter produced without assistance is the independent output the [learning loop](../learning/README.md) graduates against. The system optimizes for fast iteration — raw materials to reviewed draft in short cycles, not big batches.

## The main line

```text
frame-piece  →  write-content  →  review-draft  →  edit-targeted  →  [publish-adapt]
  angle +         draft from        depth gate       surgical         per medium
  selection       the brief         then craft       edits            (planned)
      ↑                                  │
      └────────── "reframe or kill" ─────┘
```

Every arrow is a gate the author walks through, not a handoff the agent performs. The design rationale is in [ADR-006](../../docs/adr.md#adr-006-frame-authored-writing-before-drafting).

**Why `frame-piece` comes first.** A thesis derived from the materials *is* the materials' thesis — that produces a faithful summary, never an authored piece. Angle and taste live in the author, not the corpus: what they disagree with, who they're arguing against, what they got wrong before. `frame-piece` is the conversation that extracts those and turns them into a `brief.md`.

It starts from an **occasion** — what changed outside the material — because a timeless corpus supplies no contestable question on its own; candidates are framed as 议题 / 正方 / 反方 so both sides have real adherents. The material is evidence, never the opponent: a piece whose target is the source's author is a book review. The brief carries a **论点层级** (主题 → 一层论点 → 二层机制 → 三层具体展开) that `write-content` uses as its outline, and a selection map dispositioning every source section as `core` / `support` / `cut` / `gap`, each `core`/`support` row keyed to the ladder node it discharges. Most content lands under `cut`; that is the point.

## Workflows

Real writing isn't linear. Different situations call for different patterns.

### Pattern 1: Authored piece (Materials → Argument)
The default. You have materials and need a piece with a point of view:
```
frame-piece → write-content → review-draft ⇄ edit-targeted → [enhance]
```
Gaps in the brief route to `synthesis-research` before drafting the sections that need them.

### Pattern 2: Faithful explainer (Notes → Prose)
Course notes into clean prose, where restating the source well *is* the goal:
```
write-content → review-draft ⇄ edit-targeted
```
`write-content` runs brief-less and says so — it will offer `/frame-piece` when it notices the thesis is the corpus's own. This path is supported, not deprecated; it just can't produce an angle.

### Pattern 3: Book or long-form (Wiki → Chapters)
```
llm-wiki-book → build-skeleton → write-content (per chapter) → review-draft ⇄ edit-targeted
```
`llm-wiki-book` runs the same angle dialogue at book scale; its plan is a book-scale brief.

### Pattern 4: Iterative refinement (Draft → Polish)
You have a rough draft that needs work:
```
review-draft → edit-targeted → review-draft → edit-targeted → ... → [enhance]
```

### Pattern 5: Copilot mode (Human + Agent collaboration)
Non-linear back-and-forth across any phase. `review-draft` and `edit-targeted` are the copilot primitives: both run on **any unit** — a paragraph, a section, a chapter — and neither batches. The loop review → edit → review must cycle in minutes; that cadence, not any single skill, is what human-in-the-loop cashes out to.

## Skills

| Task | Skill |
|------|-------|
| Find the angle; commit an angle and a cut-list; emit `brief.md` | `frame-piece` |
| Design file/navigation structure for publications | `build-skeleton` |
| Draft prose from a brief, or from raw materials | `write-content` |
| Review any unit and return ranked findings — never rewrites | `review-draft` |
| Apply one instruction to one location; minimal diff | `edit-targeted` |
| Translate chapters between English and Chinese | `book-translator` |
| Place existing images into documents | `insert-inline-images` |
| Hand-author SVG diagrams with coherent visual language | `book-diagrams` |
| Convert technical docs into dense HTML slide decks | `create-tech-slides` |

Skills the workflows lean on that live in other systems, referenced by name: `synthesis-research` (learning loop — judgment synthesis across conflicting sources, and the executor for brief `gap` entries), `organize-docs` and `clean-notes` (pipeline — the processed notes `frame-piece` consumes), `llm-wiki-book` (pipeline — book-scale framing).

### The derive family

`book-translator` and `create-tech-slides` derive a medium-specific artifact from a finished, medium-neutral draft and **never edit back** — one canonical source, many derivations. The planned per-medium adapters (`publish-wechat`, `publish-xhs`, …) join this family; each will own one medium's length norms, hook style, formatting, and audience profile. There is no universal adapter. `brief.md` already carries an optional `target-media:` line for them.


## Principles

All writing skills follow these shared principles:

The durable design decisions are recorded in [`docs/adr.md`](../../docs/adr.md); unfinished work is in [`docs/exec-plans/writing.md`](../../docs/exec-plans/writing.md).

### Heading Design
- Headings form a continuous narrative that communicates the main argument
- Each child heading develops its parent; adjacent headings form logical progression
- Express claims or reader tasks, not labels
- No headings merely for formatting (use bold run-in labels instead)

### Summary Writing
- Answers: What is this about? What problem? What's the core logic?
- Stands alone for readers who skip the body
- Explains relationships between ideas, not just lists them
- Includes practical conclusion or takeaway

### MECE Organization
- Every concept owned by exactly one section
- Collectively exhaustive coverage of the scope
- No redundant explanations or duplicate examples
