# The Writing System

Last updated: 2026-10-01

**Answer one worthwhile question, make the reasoning visible, and keep what changes your understanding.**

Writing serves a reader first. It can argue, explain, explore or teach. An independently produced
chapter can also be learner evidence, but prose quality and mastery remain separate judgments.

## The working loop

```text
materials → pre-write-grill → frame → develop-argument ⇄ develop-examples → write-content
              ↓ confirmation                    ↑                              ↓
         map-materials                          └──── review-draft ⇄ edit-targeted

understanding changes → snapshot-writing → the next frame
agreed logic → book-diagrams (when a finished SVG is useful)
delivered piece → archive-materials (actual material use and source verdicts)
```

**Confirmation gates:** For original articles from scattered materials, `pre-write-grill` establishes
shared understanding (topic, scope, length, material priorities, examples, structure) before
downstream work. Faithful summaries of single sources may skip directly to `write-content`.

Enter at the stage the task needs. A single-skill request ends at that skill's result. An authorized
writing/improvement workflow continues across stages, asking only for an unresolved judgment,
scope choice or personal fact. Reuse confirmed decisions and valid outlines without repeat gates.

**Familiar + fresh.** Familiar means a recognizable reader situation and an author stake. Fresh
means a concrete gain in explanation, evidence, connection, judgment or boundary for that reader.
Neither an opponent nor worldwide novelty is required. An exploration can make progress by
showing which answers remain possible and what evidence would distinguish them.

## Skills and ownership

| Skill | Owns | Completion |
| :--- | :--- | :--- |
| `pre-write-grill` | confirmed topic, scope, length, material priorities, examples, structure | author explicitly confirms specification |
| `frame` | question, reader, gain, current answer, scope | author intent is settled enough to develop |
| `map-materials` | cataloged sources, themes, material roles | materials categorized by relevance to confirmed topic |
| `develop-argument` | logic nodes, justified relations, reading order, derived map | inference/dependencies are inspectable; gaps named |
| `develop-examples` | evidence, selection map, chapter code/math | required points have attributable evidence or explicit gaps |
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
[brief-format.md](frame/references/brief-format.md), with mechanical definitions in
[brief-schema.json](brief-schema.json). Each stage writes only its owned sections.

- **Framing:** Question, Reader, Gain, Answer, Scope; `brief-kind: piece | chapter`; article
  `intent: argue | explain | explore`; chapters add `教学目标`.
- **Logic:** stable node IDs, sentences, relations with reasons, reading order and a derived Mermaid
  map when useful. There is no pillar count or graph quota.
- **Evidence:** each item names a node, role, source, verification and limits. Distinguish facts,
  author accounts, reasoning and labelled illustrations. Personal examples are preferred where
  useful, not mandatory and not intrinsically stronger evidence.
- **Selection:** preserve material-map IDs, canonical roles and full coverage of the declared
  inventory. Only `key` material is core/support; a justified cut is useful, a forced cut is not.
- **Revisions:** changed meaning gets a new node ID; update dependent examples, passages and figures.
  A new premise can require more than re-reviewing its sentence.

V1 briefs remain readable without migration. Infer a missing kind only from unambiguous teaching
or opposition fields. Legacy chapter ladders need no opponent; keep legacy IDs until explicitly
converting the brief. A book plan may provide equivalent inputs without an article-format rewrite.

## Writing memory

`writing-memory/<topic>/<number>.md` stores an immutable sequence of current judgments, changes,
grounds, topic relations, open questions and piece pointers. `writing-memory/index.md` is derived
from the latest valid snapshots. See [memory-format.md](snapshot-writing/references/memory-format.md).

`snapshot-writing` is the only writer; `frame` reads it before proposing another related piece.
Save on a meaningful change at any stage, including before publication. Rewording or retrying does
not create a snapshot. A new judgment can contradict an earlier one while preserving its history.
Topics and article series emerge from these questions and evidenced relationships.

Writing memory is editorial state. It references `learning/` without writing mastery, `sources/`
without changing tiers, and material maps without changing usage. Learning's cross-topic index
continues to own earned learner edges. Snapshots introduce no new database or retrieval service.

**Current topics:** Framework-driven explanation (Technique 18 integration from Chinese expository samples).

## Common paths

- **Article:** frame → logic ⇄ evidence → draft → review/repair. Skip stages already satisfied.
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

`python3 skills/writing/scripts/verify_brief.py <brief> --stage frame|argument|examples|ship` checks
stage completeness, node references, evidence states and agreement between the logic table and its
map. It reports legacy read compatibility separately. It does not establish truth or reader value.
`verify_references.py` checks delivered asset links; `--portability` adds delivery-format checks.

Mechanical regression tests live beside those scripts. Behavioral scenarios and the real-corpus
walkthrough are in [the writing trial](../../trials/writing/RUNBOOK.md). Durable rationale lives in
[the ADRs](../../docs/adr.md); pending validation stays in
[the writing execution plan](../../docs/exec-plans/writing.md).

Every edited Markdown artifact updates a near-top Last updated date. For targeted edits this is the
one explicit metadata exception to the unchanged-surroundings rule. Derivations preserve the
canonical draft; diagrams cannot add relationships that the text and agreed logic do not support.
