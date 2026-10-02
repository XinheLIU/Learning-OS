---
name: develop-argument
description: Develop and stress-test the logical framework of an article or chapter. Use for 理逻辑, framework alignment, original synthesis, reasoning gaps or explanatory chains. Present analytical reasoning for agreement before selecting excerpts or drafting prose.
---

# Develop Argument

Last updated: 2026-10-02

Earn the thesis before writing its sentences. Read the
[brief contract](../../foundations/frame/references/brief-format.md). A supplied draft or outline can
be inspected directly; create a brief only when artifact creation is in scope.

## Workflow

1. Read framing, the supplied material inventory and any existing logic/evidence. Reuse material
   maps and relevant source passages; distinguish inspected support from provisional assumptions.
   Work with `frame` for an unclear reader/question and `pre-write-grill` for unresolved judgments.
2. Build the reasoning needed to answer the central question:

   | Purpose | Structure to test |
   | :--- | :--- |
   | argue | conclusion, reasons, premises, strongest relevant objection and boundaries |
   | explain | phenomenon, mechanism, conditions and what the explanation enables |
   | explore | possible answers, comparison criteria, distinguishing evidence and unknowns |
   | chapter | teachable units in prerequisite order, ending at the promised capability |

   State claims as sentences and explain why each relation holds. Test missing premises, causal
   leaps, circular proof, interactions and limiting cases. Complexity must earn explanatory power:
   a flat topic list is insufficient, but there is no quota for dimensions, pillars or edges.
3. **For analytical writing, identify the original contribution.** Separate what the sources already
   say from the article's derived distinction, mechanism, connection or judgment. Name the reasoning
   that earns it and its limits. Useful organization alone is not a synthesis; worldwide novelty
   is not required. An exploration may contribute discriminating criteria without choosing an
   answer. If the contribution is absent, revise the framework before polishing its presentation.
4. Write Logic nodes, Logic relations and Reading order. Every section advances the thesis or a
   necessary boundary, and each required node appears in reading order. Show where any introduced
   framework is actually applied. Preserve node IDs for wording changes; changed meanings get new
   IDs, never recycled ones. Name the evidence needed for each required node without finalizing
   excerpt choices or editing the Evidence table.
5. Present the framework in the Markdown brief: thesis, contribution, section claims, reasoning
   path, alternatives and unresolved evidence needs. Derive a Mermaid map from the tables when
   useful. An HTML view may clarify complex relationships or satisfy a request; it derives from
   this same brief. No article paragraphs are written at this stage.
6. **Checkpoint 1 — framework.** Grill the consequential weaknesses with the author. Once the
   framework is ready, obtain or reuse confirmation/delegation and record its scope and basis in
   Checkpoints. Follow the shared checkpoint rules; drafting permission alone does not settle an
   unresolved thesis. Only then hand off to material selection and section planning.

## Chapter and inspection branches

Chapters use [chapter-format.md](../../foundations/frame/references/chapter-format.md). Develop
prerequisite order from the promised capability; preserve author markers and their evidence.
Teaching a settled mechanism needs no original synthesis or analytical checkpoints.

A standalone logic inspection returns the extracted reasoning, defects and evidence needs. An
existing draft does not require reconstructing its entire preparation history to diagnose a gap.

## Completion and handoffs

Run `python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage argument` when a
v2 brief is in scope. This checks references and graph consistency, not originality or inference.
For analytical workflow completion, the contribution must be defensible and checkpoint 1 settled.

- Agreed framework → `develop-examples` for excerpts, treatment and budgets.
- Changed question or author answer → `frame`; genuinely unresolved decisions → `pre-write-grill`.
- Evidence contradicts a premise → revise the affected logic and identify dependent sections,
  evidence and figures. Reopen affected checkpoints using the shared rules, not the entire interview.
- Agreed relationships needing a finished SVG → `book-diagrams`.

## Contract test

Reject headings joined by unexplained arrows and a framework that only paraphrases source claims.
Accept a supported synthesis or an exploration with new discriminating criteria. Preserve a teaching
chapter's different purpose. A presentation cannot add a relationship absent from the logic table.
