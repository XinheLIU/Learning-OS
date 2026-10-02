---
name: develop-argument
description: Develop or inspect the logic of an article or chapter. Use for 理逻辑, 论证结构, reasoning gaps, explanatory chains, comparing possible answers, or turning an outline into a relationship diagram. Maintain stable logic nodes and justified relations in the brief.
---

# Develop Argument

Last updated: 2026-10-01

Make the reasoning inspectable before refining its sentences. Read the brief using the shared
[format and compatibility rules](../frame/references/brief-format.md). A supplied draft or outline
can be analyzed directly: report the extracted structure, and ask only if the central question or
attributed judgment is ambiguous. Store a brief only when artifact creation is in scope.

## Workflow

1. Read the framing, any existing logic and evidence. Preserve useful node IDs. A changed meaning
   gets a new ID; editing wording alone keeps the ID. Never reuse a removed ID for another claim.
2. Build the smallest structure that delivers the reader's gain:

   | Purpose | Structure to test |
   | :--- | :--- |
   | argue | conclusion, reasons, necessary premises, strongest relevant objections and limits |
   | explain | phenomenon, mechanism, conditions and what the explanation enables |
   | explore | possible answers, comparison criteria, evidence that distinguishes them, remaining unknowns |
   | chapter | teachable units in prerequisite order, ending at the promised capability |

   State claims as sentences. For each relation, explain *why* it holds; adjacent headings and
   arrows alone are not reasoning. Check sufficiency, missing premises, causal leaps, scope and
   circular explanation. A causal feedback loop may be real; a circular proof is not evidence.
3. Write Logic nodes, Logic relations and Reading order in the brief. Each node belongs to the
   central question or a needed limitation. Mark central claims/teaching units `required`; contextual
   nodes are `context`. Reading order records sections with the IDs they discharge.
4. For each required node, state what would substantiate or explain it. Existing evidence can be
   linked; missing evidence becomes a named handoff to `develop-examples`. Do not invent evidence
   or overwrite its table here. New counterevidence may require changing the argument, not merely
   adding another anecdote.
5. Regenerate Logic map from the tables when a diagram makes relationships clearer. Use the
   constrained Mermaid form in the shared format. A simple chain may stay prose (`none` in Logic
   map). Both the table's relation and its reason remain authoritative; an arrow is never extra proof.

## Chapter branch

Read [chapter-format.md](../frame/references/chapter-format.md). Start from the capability and
prerequisites, using its suggested skeleton only where it helps. A subsection based solely on a
materials folder is not justified. Learning `connect` nodes can provide transitions, not stand-alone
teaching sections. Retain evidence pointers on confirmed author markers and anchor them to nodes.

## Completion and handoffs

Done when every node serves the question, every relation has a stated reason, reading order covers
all required nodes, and unresolved reasoning/evidence needs are explicit. Run
`python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage argument`.
This detects malformed references and graph drift, not whether a premise is true.

**Confirmation gate:** Present the logic structure to the author and ask: "Does this reasoning path make sense? Any gaps or issues before we develop examples?" Only proceed to evidence development after explicit author confirmation.

- Evidence work → `develop-examples`; a synthesis requiring a new judgment → `synthesis-research`.
- Changed question or reader gain → `frame` with the specific conflict.
- SVG requested → `book-diagrams`, consuming the agreed relations.
- On revision, list affected evidence rows and draft sections for recheck. Resolve dangling
  references before reporting the brief ready for the next stage.

## Contract test

Given headings with an unsupported causal leap, identify the missing premise instead of merely
connecting boxes. Given an exploratory brief, compare answers without attributing a final judgment
to the author. A map containing a relation absent from the table fails verification.
