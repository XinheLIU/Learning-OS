---
name: develop-examples
description: Select and verify source excerpts for agreed writing claims, plan example depth and section lengths, and research named gaps. Use for 素材取舍, 摘选, 详略安排, 字数分配, evidence selection or unsupported claims. Settle the material plan before analytical drafting.
---

# Develop Examples

Last updated: 2026-10-02

Choose what deserves space and how it advances the reasoning. Read the
[brief contract](../../foundations/frame/references/brief-format.md). For an analytical workflow,
start from the settled framework checkpoint. A standalone evidence request needs only the supplied
claim; it does not require the entire workflow.

## Workflow

1. **Consider the inventory, then select passages.** Reuse the supplied material map or declare
   the source files/folders considered. Account for the whole inventory, including contrary and
   peripheral material, without inserting every source into the article. Inspect promising files
   and counterevidence; unread material stays `inspect-on-demand`, with a reason. A map is an index,
   not permission to describe a passage without reading it.
2. **Give each excerpt a job.** Link its exact path/URL and section, page, timestamp or other passage
   locator to a logic node. Evidence Account holds the chosen short excerpt or faithful paraphrase,
   clearly distinguished, with enough context to preserve its meaning. Record whether it supports,
   explains or challenges the claim, its verification and what it cannot establish.
3. **Resolve necessary gaps.** Search existing material first. Research only a named missing fact,
   warrant or counterexample that matters to the framework. Verify numbers and quotations against
   originals. Use `synthesis-research` when resolving sources requires a new judgment; ordinary
   lookup needs no research report. If lookup is unavailable, retain the gap and work on independent
   preparation. Narrow or remove unsupported claims, or retain a bounded exploratory question.
   Counterevidence may require `develop-argument` and renewed agreement on affected decisions.
4. **Complete Selection map.** Preserve material IDs and canonical map roles: only `key` rows can
   be core/support; identify `redundant-of` through its canonical ID. Route a disputed role to
   `map-materials`. Every inventory item gets a disposition or a justified ancestor-folder row;
   annotate excluded duplicates and off-scope passages. No forced cut and no forced inclusion.
5. **For analytical writing, compose the Section plan before prose.** Read
   [techniques.md](../write-content/references/techniques.md) for choices that affect selection and
   pacing. Follow Reading order and give every section:
   - A target length within the agreed total and counting unit.
   - Evidence IDs marked `developed` or `brief`: fully work through cases needed to establish a
     mechanism or decisive inference; cite secondary corroboration briefly.
   - The craft choice and its purpose: contrast, mechanism walkthrough, abstraction-to-case,
     counterexample, or research narrative only when it earns its space.
   - A transition explaining what the section establishes and why the next question follows.

   Allocate length by reasoning difficulty and contribution to the thesis. Do not distribute equal
   space by source count or repeat concept/research/examples for every dimension. Ensure the plan
   leaves room for the author's inference between excerpts. Introduced frameworks must be applied,
   not merely named. Read the research-narrative reference only if choosing that technique.
6. **Checkpoint 2 — material plan.** Present selected excerpts with their limits and the section
   budgets/treatment beside them. Explain substantial cuts, thinly supported sections and the
   reasoning behind unequal depth. Settle any unresolved choices with the author; reuse prior
   confirmation or explicit delegation. Record the checkpoint only when required factual support
   is ready and the planned evidence actually discharges the required nodes.

## Evidence boundaries

Relevant personal accounts can supply specificity and voice; stronger external evidence takes
precedence for factual support. Ask only for missing personal facts, never invent an incident.
Preserve a dated dialogue excerpt or record pointer in Author's markers. Illustrations remain
labelled and can explain a concept without proving a real event, prevalence or causation.

Source truth and selection remain distinct: verification checks the cited account; the inference
must still be justified. Leave source files, registry tiers and actual-use history unchanged.
`archive-materials` records what appeared after delivery.

## Chapter branch and readiness

Chapters keep their teaching sequence and [Code & math contract](../../foundations/frame/references/chapter-format.md).
Maintain source, node, placement and purpose; use inline minimal examples or local assets as needed.
The analytical originality, budget and checkpoint requirements do not become teaching gates.

Run `verify_brief.py <brief> --stage examples` from the shared scripts directory for evidence work
in progress. Before analytical drafting, run `--stage draft` and assess the reasoning semantically.
The examples stage permits gaps; it is not permission to draft an unsupported analytical thesis.
An open question can retain a gap if the piece makes the uncertainty explicit.

## Handoffs and contract test

Settled material plan → `write-content`. Changed premise → `develop-argument`; changed author
judgment → `frame`. Significant understanding changes may go to `snapshot-writing` within scope.

Given many sources, choose precise passages and account for omissions. Given two relevant cases,
justify developing one and citing the other briefly instead of padding both. A vivid anecdote
cannot support a universal claim. A pending central fact prevents draft readiness; absent personal
experience does not. No article prose is produced in this stage.
