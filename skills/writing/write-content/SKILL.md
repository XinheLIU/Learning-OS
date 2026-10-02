---
name: write-content
description: Draft nonfiction articles and teaching chapters from a brief or supplied materials. Use when ready to write prose, including arguments, explanations and open-ended explorations. Reuse settled framing, logic and evidence; fill only the missing preparation.
---

# Write Content

Last updated: 2026-10-03

Turn the agreed reader promise, reasoning and evidence into prose. Read
[brief-format.md](../frame/references/brief-format.md) for stage ownership and v1 compatibility;
read [techniques.md](references/techniques.md) while drafting.

## Workflow

1. **Find the working contract.** Read the supplied brief, or look beside the draft and under
   `drafts/<piece>/`. Resolve kind and intent using the compatibility rules. Read selected evidence
   and source passages, not every cut source. A book plan may supply the equivalent question,
   chapter order and evidence without requiring conversion to an article brief.

2. **Check if brief is required.** For original articles synthesizing scattered author materials into
   an argued position or exploration: **brief is required**. Call `/pre-write-grill` → `/frame` if
   missing. For faithful summaries of a single external source: brief remains optional.
   
   **Distinction:** Transforming the author's materials requires upfront shared understanding (topic,
   scope, length, material priorities, examples). Summarizing one document does not.

3. **Fill only missing preparation.** With a brief, use its reading order and settled author answer.
   Missing question/gain → `frame`; missing logic → `develop-argument`; missing examples or facts →
   `develop-examples`. Continue those stages within an authorized writing task, asking only for
   decisions or facts not already supplied. Do not ask to approve the same outline again.

4. **Confirm argument density allocation** (for original argued/explained pieces only, skip for
   faithful summaries). Before drafting, explicitly confirm with the user:
   - What is the core thesis or main claim?
   - Which sections carry the primary argument/explanation? (e.g., "Section 2 establishes framework,
     Section 3 provides multi-dimensional evidence")
   - If an analytical framework was introduced (e.g., D/N/S curves, five-stage model, three-phase
     evolution), in which section(s) will it be systematically applied to analyze the subject?
   - Does the planned argument density match the thesis importance? (e.g., if thesis is "opportunity
     window is opening," do the "why it's opening" sections carry 50%+ of the analytical weight?)
   
   **Why this matters:** Avoid introducing frameworks in one section without applying them in depth
   later, or front-loading debate logic without maintaining that depth through supporting sections.
   
   Example confirmation:
   ```
   Core thesis: "AI/Agent opportunity window is just beginning"
   Primary argument sections: Section 2 (theoretical frameworks) + Section 3 (D/N/S evidence)
   Framework application: Section 2 introduces three-stage model + D/N/S curves → Section 3 applies
   D/N/S to analyze Demand/Narrative/Supply status + maps to five-stage model
   Density check: Sections 2-3 should constitute 50%+ of analytical depth
   ```

5. **Without a brief** (faithful summary path only): Establish the reader, question and scope from
   the request/materials, proposing an outline only if structure is still undecided. Source agreement
   is not a failure.

6. **Draft one reader outcome.** Follow the agreed logic; use personal markers in their actual role,
   alongside the strongest appropriate evidence. Keep the author's words where they carry voice or
   judgment. An exploration can end with narrowed uncertainty and a discriminating next question;
   it need not pick a winner. A chapter follows prerequisites toward its capability.
6. **Check and deliver.** Write `<piece>.md` beside the brief, or to the supplied destination, with
   `Last updated: YYYY-MM-DD` near the top. State the reader gain and unresolved facts. For v2 run
   `verify_brief.py <brief> --stage examples` from the shared scripts directory; this checks the
   working contract, not whether the prose deserves a ship verdict.

## Evidence and presentation

- Real events, quotations and numbers carry source pointers. Clearly labelled illustrative
  scenarios can teach a mechanism but cannot prove real-world outcomes. No invented personal history.
- Keep unresolved factual claims marked `[VERIFY: ...]` in working prose. Block a ship recommendation
  while central facts are unresolved; write independent sections where useful.
- Respect Scope and the source selection. New evidence can change the reasoning; route it back to
  the owning stage and involve the author for a changed judgment, rather than silently widening it.
- Match the requested language and audience. Technical prose needs exact mechanisms and constraints;
  business prose needs consequences and decisions. Diagrams serve relationships, with no count quota.
  Derive them from the logic; request `book-diagrams` for SVG and `insert-inline-images` for existing art.
- For complex frameworks with research, see Technique 18 (Framework-driven explanation) in
  techniques.md; for research narrative voice see research-narrative-patterns.md.
- A supplied valid outline is input, not something to re-invent. Local restructuring that changes a
  logical dependency belongs in the brief as well as the draft, through `develop-argument`.

## Completion and handoffs

Done when the requested draft exists, serves one question, preserves attribution, respects excluded
scope and distinguishes supported conclusions from remaining uncertainty. No claim of independent
mastery is made by drafting. `review-draft` evaluates the result; `edit-targeted` handles specific
findings. Significant understanding changes can go to `snapshot-writing` within the authorized task.

## Contract test

Draft an explanation without an opponent, an exploration without a settled answer and a chapter
without novelty-to-the-field. Reuse an existing outline without a redundant approval gate. Evidence
from the brief appears where it serves the claim; cut material and fabricated experiences do not.
