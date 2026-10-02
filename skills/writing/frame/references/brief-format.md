# Writing Brief v2

Last updated: 2026-10-01

One working contract at `drafts/<piece>/brief.md`, relative to the user's working corpus. Shared
rules live here; the mechanical field/table definition is [brief-schema.json](../../brief-schema.json).
Do not place drafts inside the read-only material archive.

## Ownership and stage requirements

| Stage | Owner | Required content |
| :--- | :--- | :--- |
| frame | `frame` | metadata; Question, Reader, Gain, Answer, Scope; 教学目标 for chapters |
| argument | `develop-argument` | framing plus Logic nodes, Logic relations, Reading order, Logic map |
| examples | `develop-examples` | argument plus Evidence, Selection map; Code & math for chapters |
| ship | `review-draft` assesses, without writes | same structure, with required claims substantiated and no unresolved central factual gaps |

A skill edits its own sections; an upstream change names downstream rows and passages needing
recheck. Optional `Author's markers` are authored in framing, anchored in logic development, and
extended with attributed experience in example development. Preserve confirmed wording and origin.
Whole-workflow authorization covers these stages; no repeated approval of unchanged decisions.

## Framing template

```markdown
---
brief-version: 2
piece: <stable-slug>
brief-kind: piece
intent: explain
status: framed
target-media: blog
sources: [<source paths or URLs>]
---

# Brief: <working title>

Last updated: YYYY-MM-DD

## Question
<one concrete question; familiar situation, not just a subject label>

## Reader
<who, what they know, and the situation in which this matters>

## Gain
<what becomes clearer or changes after reading; why the author cares>

## Answer
<the author's current answer, confirmed wording, or an explicit unresolved question>

## Scope
<what this piece covers and leaves for another piece>
```

`brief-kind` remains `piece | chapter`; `intent` for pieces is `argue | explain | explore`.
`brief-version` is the artifact's version; `schemaVersion` belongs to the companion JSON contract.
`status` is a coarse authoring label, not a substitute for inspecting the sections. Only include
optional publication metadata that is known. Chapters omit `intent` and add `## 教学目标`.

Freshness is measured against the Reader's starting point, not a claim of worldwide originality.
An argumentative Answer can include a real opposing position, fairly stated. Explanations and
explorations do not require one. Uncertainty in Answer is content, not a blank field to fill for the author.

## Logic sections

```markdown
## Logic nodes

| ID | Statement | Kind | Need |
| :--- | :--- | :--- | :--- |
| n1 | <premise or teachable concept> | premise | required |
| n2 | <bounded conclusion> | conclusion | required |

## Logic relations

| From | Relation | To | Reason |
| :--- | :--- | :--- | :--- |
| n1 | supports | n2 | <why this premise warrants this conclusion> |

## Reading order

| Section | Nodes | Reader task |
| :--- | :--- | :--- |
| <heading> | n1, n2 | <what the reader understands or can do here> |

## Logic map

<none, with a reason; or a Mermaid block derived from the relations>
```

Node kinds: `claim | premise | concept | question | conclusion`; need: `required | context`.
Use stable `n<number>` IDs, never positional headings as IDs. Keep every required node in reading
order; add sections only to serve the Question. There is no minimum number of pillars or edges.

Relations: `supports` (reason → conclusion), `depends-on` (dependent → prerequisite), `limits`
(condition → bounded claim), `contrasts` or `alternative-to` (explicit comparison). Direction and
Reason matter: `depends-on` arrows run opposite to the teaching order. An empty relations table is
valid for one self-contained point; disconnected multi-node logic needs explanation or revision.

For a derived Logic map, use only these lines inside one `mermaid` fence: `flowchart LR` (or `TB`),
node declarations `n1["<statement copied from the table>"]`, and `n1 -->|supports| n2`. Include every
node and relation exactly once. Escape quotes as `&quot;` and pipes in tables as `&#124;`.
This deliberately small *brief* diagram format permits exact comparison; publication diagrams may
use richer layouts through `book-diagrams`, with semantic review against the same table.

## Evidence and selection sections

```markdown
## Evidence

| ID | Nodes | Kind | Role | Account | Source | Verification | Limits |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| e1 | n1 | external | supports | <observed finding> | <path or URL and passage> | verified | <population/conditions; what this does not establish> |
| e2 | n2 | gap | supports | <what would substantiate this claim> | — | gap | <what cannot yet be concluded> |

## Selection map

| Material | Disposition | Nodes | Note |
| :--- | :--- | :--- | :--- |
| <m001 + path, or source + passage> | core | n1 | <why selected> |
| <another source> | cut | — | <off scope> |
```

Evidence kinds: `personal | external | illustration | reasoning | gap`. Roles: `supports | explains
| challenges`. Verification: `verified | author-confirmed | illustrative | unverified | gap`.
`personal` uses author-confirmed or unverified; `illustration` uses illustrative and explains;
`gap` uses gap. External facts and explicit derivations use verified or unverified. Verification
means the cited account was checked, not that the inference is automatically valid.

Every required non-question node has evidence or a gap. Claims, premises and conclusions require
support; a concept may be explained with a labelled illustration. Challenges are valuable but are
not positive support. A gap or unverified row on a required non-question node prevents ship until resolved or the
claim is narrowed. Open-question nodes may retain gaps naming future evidence without pretending
the article has supplied an answer.

Personal source pointers identify the author's record, or `brief.md#authors-markers` with a dated,
verbatim excerpt from supplied dialogue. Keep assistance/earned pointers when using learner records.
Reasoning entries link an inspectable derivation or code and expose assumptions. Label invented
numbers or scenarios as illustrations; never attribute them to a real person or company.

Selection dispositions: `core | support | cut | gap | inspect-on-demand`. Core/support must name
nodes; the other rows can name nodes or use `—`. Declare the inventory covered (provided sources,
material map or specified folders); every item in that inventory gets a row or a justified ancestor
folder row. A gap row uses `—` for Material. No forced cut, no cold scan of a mapped archive.
Evidence carries exact provenance; the selection map records choices, not duplicate case accounts.
`develop-examples` resolves stale evidence and selection references when logic changes.

## Existing briefs (read compatibility)

Without `brief-version`, read as v1; never rewrite a historical brief just to inspect or draft from it.

| Legacy field | v2 meaning |
| :--- | :--- |
| 议题 / Angle / 反方 | Question / Answer; piece intent defaults to argue |
| 正方 | real objection, relevant only to argue |
| Reader | Reader; explain implied gain explicitly in the working discussion |
| Cost paid | Scope |
| 论点层级 / skeleton / 二层 → 三层 | logic, reading order and initial evidence pointers |
| Selection map / 支撑节点 | selected sources and their legacy node references |
| 教学目标 / Code & math | chapter capability and selected teaching material |

If `brief-kind` is missing, a teaching goal alone identifies chapter; an explicit opposing/author
position pair alone identifies piece. Both or neither is ambiguous: report and clarify. A v1 chapter
needs no opponent. Keep legacy node IDs in read-only use; when explicitly updating to v2, assign
stable IDs and update all evidence, marker and map references together. No bulk migration.

The checker reports legacy compatibility separately from v2 validation. Legacy evidence sufficiency,
source truth and reader gain still require human/agent review; a legacy structural pass is not a ship verdict.
