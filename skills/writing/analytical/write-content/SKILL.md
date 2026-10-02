---
name: write-content
description: Draft nonfiction from an agreed framework and material plan, or produce a faithful summary. Use when ready for article or chapter prose. For original analytical writing, resolve missing framework, excerpt selection and section budgets before drafting.
---

# Write Content

Last updated: 2026-10-02

Realize the decisions made before drafting. Read the
[brief contract](../../foundations/frame/references/brief-format.md) and relevant
[writing techniques](references/techniques.md).

## Workflow

1. **Identify the task, not the file count.** An original analytical article needs framing, a
   defensible synthesis and both pre-draft checkpoints even if its source material is one file.
   A faithful summary or explanation of supplied content can proceed directly from clear reader,
   scope and source instructions. Chapters retain their teaching track and capability contract.
   Standalone edits belong to `edit-targeted`.
2. **Read the agreed preparation.** Find the supplied brief or `drafts/<piece>/brief.md`. For an
   analytical piece, inspect the framework, original contribution, selected passages, section plan
   and checkpoint basis. Existing outlines and confirmed/delegated decisions remain valid; resolve
   only missing preparation through its owner. Equivalent preparation in an older brief or author
   instructions is usable without migration or repeat approval; check the same readiness criteria
   manually and record missing decisions in the working brief or a companion note.
3. **Check before drafting.** Run
   `python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage draft` for a v2
   analytical brief. A structural pass does not establish inference quality or author agreement.
   Required claims need verified, appropriately bounded support, and the section plan must use it.
   An unresolved central fact returns to `develop-examples`; an unsupported thesis returns to
   `develop-argument`. An explicitly open exploratory question can remain open.
4. **Draft the complete requested unit.** Follow the agreed reading order, section budgets and
   developed/brief treatments. Connect evidence with the article's reasoning rather than stacking
   quotations. Preserve confirmed author wording, attribution, uncertainty and excluded scope.
   Keep transitions aligned with the planned progression. Local sentence choices belong here;
   structural experimentation belongs before the draft. Complete the requested draft before its
   editorial pass rather than polishing each section into a new argument.
5. **Deliver for final review.** Write `<piece>.md` beside the brief or at the supplied destination,
   with `Last updated: YYYY-MM-DD` near the top. Report actual section lengths against targets using
   the agreed counting unit and explain material deviations. Correct local excess within the plan;
   a material change to scope, emphasis or evidence returns to the affected checkpoint.

## Other routes

For faithful summaries, keep source meaning and scope; no originality test or analytical checkpoint
is required. For chapters, follow the agreed teaching sequence and selected examples/code/math;
check the existing examples-stage contract. Neither route fabricates opposition or author mastery.
Unverified facts in these working drafts remain visibly marked `[VERIFY: ...]` and prevent ship
when central. That working-draft allowance does not bypass analytical draft readiness.

A book plan can supply equivalent chapter preparation without conversion to an article brief.
Diagrams derive from agreed relationships; use `book-diagrams` for new SVGs or
`insert-inline-images` for existing art when needed.

## Completion and handoffs

The draft exists, answers the reader's question, realizes the agreed synthesis and treatment where
applicable, and retains attribution and uncertainty. `review-draft` performs the final substantive
and expression check; `edit-targeted` applies named local repairs. If review discovers a fundamental
flaw, identify the upstream decision and affected sections before revising it. Do not silently
rebuild the piece through repeated polishing. A review-only request still authorizes no editing.

## Contract test

A request to draft an original article from one notes file enters preparation if its framework or
material plan is missing. Confirmed preparation is reused without another approval request. A
faithful summary and teaching chapter retain their direct routes. Selected cases receive their
agreed depth, cut material stays out, and article prose starts only after analytical readiness.
