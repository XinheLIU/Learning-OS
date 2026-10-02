---
name: review-draft
description: Review a paragraph, section, article or chapter for reader gain, reasoning, evidence and expression. Return ranked findings with quoted passages and a repair route; never rewrite. Use for 审稿, review this draft, checking logic or readiness to ship.
---

# Review Draft

Last updated: 2026-10-02

Perform the final review of the completed requested draft. Judge whether the text delivers its
reader promise and realizes the agreed framework/material plan. A standalone partial review still
inspects only the requested span; it does not reconstruct preparation history. Read the brief using
the [shared format and compatibility rules](../../foundations/frame/references/brief-format.md). Without one, review
visible logic, evidence and expression; state that intended gain/scope cannot be fully checked.
An absent brief does not disable reasoning review or justify inventing author intent.

## Review order

| Dimension | Check | Route |
| :--- | :--- | :--- |
| 定题 | one question, recognizable reader situation and a specific gain delivered by the text | `frame` |
| 逻辑 | conclusions follow from stated reasons; prerequisites, comparisons and limits are clear | `develop-argument` |
| 例证 | facts are traceable; examples do their stated job; evidence supports the actual scope | `develop-examples` |
| 表达 | readers can follow sentences, terms, transitions and relevant diagrams | `edit-targeted` |

Inspect the unit actually requested. Whole-piece gain/opening/conclusion tests do not apply to an
isolated paragraph. For a missing step quote the two passages surrounding the gap. Each finding
names the relevant brief node/field or craft criterion and the condition that would resolve it.

For analytical work with a preparation plan, compare the delivered synthesis, framework application,
selected excerpts, developed/brief treatment, section lengths and transitions against it. Run the
brief's `--stage draft` check as well as the ship check for a whole-piece review. Missing historical
preparation does not prevent reviewing an existing draft; report only the decisions needed to
resolve actual defects. A structurally valid plan does not establish that its inference is sound.

### Purpose-specific reasoning

- **argue:** strongest relevant objection, premises, warranted conclusion, conditions and real costs
  of the proposed action. An opponent need not be a named person; the opposing belief needs evidence.
- **explain:** an accurate mechanism, helpful examples and the promised change in understanding.
  Settled knowledge can be valuable. Do not demand opposition or a novel research result.
- **explore:** plausible alternatives, fair comparison, what evidence distinguishes them, what
  remains unknown. Penalize false certainty, not a deliberately bounded unanswered question.
- **chapter:** the stated capability, prerequisite order, worked explanations and selected code/math.
  Skip opponent checks. A skillful draft is not proof of author mastery; that remains `grill`/`evaluate`.

### Evidence and diagram checks

Compare prose claims to the actual cited passage and the evidence's Limits. An anecdote may explain
without proving prevalence or causation. Author-confirmed experience establishes what the author
reported, not a universal law. No personal example is required; an illustrative scenario stays
explicitly hypothetical and never becomes factual support.

For a whole-piece v2 review, run
`python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage ship`.
A partial review checks only the relevant nodes; unrelated brief gaps do not fail a paragraph.
A structural pass does not establish truth: read key sources and assess inference strength. Check
`[VERIFY]` markers in the draft as well as brief gaps. Compare publication figures to the logic
relations; the figure cannot silently introduce a cause, omit a limiting condition or reverse a
prerequisite. Report affected node IDs and passages for a stale brief/figure.

Read [techniques.md](../../analytical/write-content/references/techniques.md) for expression checks, applying only
those relevant to the unit and purpose. No forced objection, example cadence or diagram quota.

## Verdict and report

```markdown
## Review: <unit>

**Verdict:** ship / edit / reframe or kill
<reason and scope of the verdict; a paragraph verdict is not whole-article approval>

### Findings

**1. <defect>** — <brief node/field or criterion>; route: <skill>
> <offending passage, or passages surrounding a missing step>

<why it fails and what would resolve it; no replacement prose>

### No findings on
<units reviewed without defects>
```

Rank question/gain failures, then inference, evidence and expression. `reframe or kill` means the
reader promise or central question is unsupported/misdirected; return the closest viable material
as evidence for framing, not a new authored position. For analytical work, `reframe or kill` also
covers a changed premise or section structure: name the preparation owner and affected checkpoint
before prose changes. `edit` covers bounded factual or expression repairs. Existing teaching and
standalone review routes remain purpose-aware. `ship` requires no unresolved central factual claims
and delivery of the agreed gain. When the question must change, stop polishing text likely to be discarded.

Finish the review without editing. Under a review-only request, stop; in an authorized improvement
workflow, pass each finding to its owner. Analytical writing uses this as the final editorial pass,
not its main engine of development. Local repairs re-review the changed span; a changed premise requires re-review of affected conclusions, examples and diagrams too.

## Contract test

The same checklist must accept a supported explanation and an honest exploration, reject an
anecdote used to prove a universal claim, and find an inference gap even without a brief. Every
finding quotes text, gives a repair condition and a route. No replacement paragraph is produced.
