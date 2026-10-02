# The Writing System

Last updated: 2026-10-02

**Answer one worthwhile question, make the reasoning visible, and keep what changes your understanding.**

Writing serves a reader first. It can argue, explain, explore or teach. An independently produced
chapter can also be learner evidence, but prose quality and mastery remain separate judgments.

## Three Writing Tracks

The writing system supports three distinct output types through a shared foundation:

| Track | Purpose | Entry signal | Key skills |
| :--- | :--- | :--- | :--- |
| **Analytical** | Original argument, explanation or exploration | A thesis or synthesis to develop from materials | pre-write-grill → develop-argument → develop-examples |
| **Explanatory** | Teaching, tutorials, courses | Concept to teach, audience unclear | define-audience → outcome-design → sequence-design |
| **Learning-to-teaching** | Graduate learning artifacts to book chapters | Raw notes from learning loop | assess-readiness → elevate-draft → add-pedagogy |

**Track selection** is driven by `brief-kind` field in the brief:
- `analytical-piece` — Opinion/analysis that needs argument development
- `explanatory-chapter` — Teaching content requiring audience-first design
- `graduated-chapter` — Learning artifact (from `/learn`, `/practice`) promoting to published content
- (implicit) — Faithful summary or direct explanation without track-specific development

All tracks reach a complete draft before final review and targeted editing. Analytical preparation
uses the two checkpoints below; teaching tracks retain their own preparation contracts.

## The writing workflow

```text
ANALYTICAL TRACK:
source reconnaissance → frame + pre-write-grill + develop-argument
                       → checkpoint 1: logical framework
                       → develop-examples: excerpts, treatment, section budgets
                       → checkpoint 2: material plan
                       → write-content → final review-draft → edit-targeted → delivery

EXPLANATORY TRACK:
concept → frame → define-audience → outcome-design → sequence-design → develop-examples
        → write-content → review-draft → edit-targeted

LEARNING-TO-TEACHING TRACK:
learning artifact → frame → assess-readiness → elevate-draft → add-pedagogy → write-content
                  → review-draft → edit-targeted

SHARED:
understanding changes → snapshot-writing → the next frame
agreed logic → book-diagrams (when a finished SVG is useful)
delivered piece → archive-materials (actual material use and source verdicts)
```

Most analytical writing decisions happen before prose. First, develop a thesis-centered framework
with enough reasoning to earn a defensible synthesis beyond source restatement. Grill the author
against a concrete presentation of section claims, dependencies, alternatives and boundaries.
Complexity serves the argument; there is no section or dimension quota.

After framework agreement, consider the whole material inventory and choose precise excerpts.
Plan which cases deserve full development, which merit a brief citation, which sources stay out,
and how each section's target length supports its inferential task. Research only named gaps.
Discuss the evidence and length allocation together before drafting; no article paragraphs are
written during either preparation stage.

Markdown is the default presentation and `brief.md` the source of truth. Derive an HTML view when
requested or useful. Each checkpoint needs actual confirmation or explicit delegation covering its
decisions; reuse existing agreement. There is no separate specification document or approval at
every skill handoff. Changes reopen affected decisions, not the entire conversation.

An original analytical task follows this path even if its materials are one file. A faithful
summary can proceed from clear source instructions, and a standalone edit stays local. An existing
draft can be reviewed directly. Teaching tracks need reader gain and sound explanation, without
an analytical originality requirement. No track needs an invented opponent or worldwide novelty.

Enter at the stage the task needs. A single-skill request ends at its result; an authorized workflow
continues through missing preparation. Final editing fixes bounded defects. A fundamental flaw
returns to its upstream decision and affected checkpoint before dependent prose is rewritten.

## Skills and ownership

| Skill | Owns | Completion |
| :--- | :--- | :--- |
| `pre-write-grill` | focused questions against the evolving framework | consequential intent and reasoning decisions resolved |
| `frame` | question, reader, gain, current answer, scope | author intent is settled enough to develop |
| `map-materials` | cataloged sources, themes, material roles | materials categorized by relevance to confirmed topic |
| `develop-argument` | logic, original contribution, reading order, derived map | analytical framework checkpoint settled; evidence needs named |
| `develop-examples` | excerpts, selection, section treatment/budgets, chapter code/math | analytical material-plan checkpoint settled; central evidence ready |
| `write-content` | canonical prose | reader promise developed within scope, uncertainty visible |
| `review-draft` | findings only | quoted, ranked defects with repair conditions and routes |
| `edit-targeted` | one requested prose repair | target changed; dependencies rechecked when affected |
| `snapshot-writing` | writing memory and its derived index | substantive delta recorded, or no-change reported |
| `book-diagrams` | new SVG diagrams | visual relationships trace to agreed logic and render legibly |
| `insert-inline-images` | placement of existing art | local assets and references resolve |
| `grill` | chapter self-test log | misses routed to draft or author gaps |
| `package-chapter` | delivery verification/frontmatter | final content and copied assets are portable |
| `book-translator` | translated derivation | meaning/structure preserved; canonical source unchanged |
| `create-tech-slides` | slide derivation | deck follows the source without editing back |
| `build-skeleton` | destination publication structure | files/navigation follow destination contract |

Pipeline `archive-materials` records actual use after delivery. `synthesis-research` handles
questions whose answers require combining or resolving sources; ordinary factual lookup belongs
to evidence development. `llm-wiki-book` plans the book-scale question, arc and chapter selection.

## Shared contract

One `drafts/<piece>/brief.md` carries the working state. The authoritative writing instructions are
[brief-format.md](foundations/frame/references/brief-format.md), with mechanical definitions in
[brief-schema.json](brief-schema.json). Each stage writes only its owned sections.

- **Framing:** Question, Reader, Gain, Answer, Scope; `brief-kind` identifies the analytical or teaching track (legacy `piece | chapter` remains readable); article
  `intent: argue | explain | explore`; chapters add `教学目标`.
- **Logic:** stable node IDs, sentences, relations with reasons, reading order and a derived Mermaid
  map when useful. There is no pillar count or graph quota.
- **Evidence:** each item names a node, role, source, verification and limits. Distinguish facts,
  author accounts, reasoning and labelled illustrations. Personal examples are preferred where
  useful, not mandatory and not intrinsically stronger evidence.
- **Selection:** preserve material-map IDs, canonical roles and full coverage of the declared
  inventory. Only `key` material is core/support; a justified cut is useful, a forced cut is not.
- **Section plan:** target lengths sum to the agreed total; evidence IDs carry developed/brief treatment, with a craft purpose and transition per section.
- **Checkpoints:** framework and material plan record confirmation/delegation and its basis.
- **Revisions:** changed meaning gets a new node ID; update dependent examples, passages and figures.
  A new premise reopens the framework and dependent material plan; local wording alone does not.

V1 briefs remain readable without migration. Infer a missing kind only from unambiguous teaching
or opposition fields. Legacy chapter ladders need no opponent; keep legacy IDs until explicitly
converting the brief. A book plan may provide equivalent inputs without an article-format rewrite.

## Writing memory

`writing-memory/<topic>/<number>.md` stores an immutable sequence of current judgments, changes,
grounds, topic relations, open questions and piece pointers. `writing-memory/index.md` is derived
from the latest valid snapshots. See [memory-format.md](foundations/snapshot-writing/references/memory-format.md).

`snapshot-writing` is the only writer; `frame` reads it before proposing another related piece.
Save on a meaningful change at any stage, including before publication. Rewording or retrying does
not create a snapshot. A new judgment can contradict an earlier one while preserving its history.
Topics and article series emerge from these questions and evidenced relationships.

Writing memory is editorial state. It references `learning/` without writing mastery, `sources/`
without changing tiers, and material maps without changing usage. Learning's cross-topic index
continues to own earned learner edges. Snapshots introduce no new database or retrieval service.

## Common paths

- **Analytical article:** agreed framework → agreed excerpts/treatment/budgets → draft → final review/repair. Reuse settled preparation.
- **Faithful explanation or summary:** direct `write-content` with clear intent and material;
  source agreement is not grounds for rejection.
- **Existing draft:** review or inspect logic/examples directly, without reconstructing every stage.
- **Concept chapter:** framing → teaching logic → examples/code/math → draft → illustrate as needed
  → review/repair → requested grill → package → material archive feedback.
- **Book:** `llm-wiki-book` → `build-skeleton` → chapter writing/review. The book plan supplies scope
  and reading order; chapter evidence still needs checking.
- **New understanding:** snapshot at the point of change; a related next piece starts from it.

Chapter capability, assistance and earned evidence remain `/evaluate`'s criteria for Independent.
AI-assisted writing does not establish mastery. Publication and deployment stay with the destination
workflow; `package-chapter` proves portability without publishing.

## Verification and maintenance

`python3 skills/writing/scripts/verify_brief.py <brief> --stage frame|argument|examples|draft|ship` checks
stage completeness, node references, evidence states and agreement between the logic table and its
map. The draft stage additionally checks analytical planning, budget arithmetic, selected evidence
and checkpoint records. Existing stages preserve compatibility; an examples pass is not analytical
draft readiness. Legacy readiness requires manual assessment of equivalent preparation. No checker
establishes truth, originality, reader value or the authenticity of author agreement.
`verify_references.py` checks delivered asset links; `--portability` adds delivery-format checks.

Mechanical regression tests live beside those scripts. Behavioral scenarios and the real-corpus
walkthrough are in [the writing trial](../../trials/writing/RUNBOOK.md). Durable rationale lives in
[the ADRs](../../docs/adr.md); pending validation stays in
[the writing execution plan](../../docs/exec-plans/writing.md).

Every edited Markdown artifact updates a near-top Last updated date. For targeted edits this is the
one explicit metadata exception to the unchanged-surroundings rule. Derivations preserve the
canonical draft; diagrams cannot add relationships that the text and agreed logic do not support.
