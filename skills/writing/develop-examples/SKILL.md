---
name: develop-examples
description: Find, interview for, and verify examples and evidence for specific writing claims. Use for 找例子, 补案例, personal stories, industry comparisons, unsupported claims, or distinguishing an illustration from proof. Maintain evidence and source selection in the brief.
---

# Develop Examples

Last updated: 2026-10-01

Make each example do a named job in the reasoning. Read the
[brief contract](../frame/references/brief-format.md); work from its node IDs. For a standalone
request, identify the supplied claim and return evidence candidates without demanding a complete
writing workflow. Write the evidence sections only when a brief is in scope.

## Workflow

1. Read required logic nodes and existing evidence. Search supplied material and relevant learning
   cases first. An example can explain, support or challenge; decide its job before collecting more.
2. Prefer relevant personal experience for concreteness. Ask only for missing facts: situation,
   action, observed result, what changed the author's mind and what remains uncertain. Capture the
   author's words with a durable dialogue excerpt in Author's markers, or a record pointer. Already
   supplied facts need no reconfirmation. Never infer a private experience from a public example.
3. Use external cases to test scope or supply evidence the personal case lacks. Check original
   sources for numbers, quotations, circumstances and outcomes; preserve the URL/path and precise
   passage. Use available search/capture tools when external lookup is needed. If unavailable, mark
   the gap and continue work that does not depend on it. A synthesis of conflicting sources routes
   to `synthesis-research`; a factual lookup does not need a research report.
4. Record each item in Evidence, including its node, kind, role, verification and limits. Personal
   evidence has no automatic priority over stronger external evidence. One person's result may
   illustrate a mechanism while being insufficient for an industry-wide conclusion.
5. Complete Selection map for the declared material inventory. Reuse `materials.md` IDs and roles:
   only `key` rows can be core/support; name the canonical ID for `redundant-of`; route a disputed
   peripheral role or newly arrived file to `map-materials`. Without a map, use source passages or
   file paths; a bulk folder may share a disposition with an explicit reason. Inspect selected files
   before describing them. `inspect-on-demand` stays unselected until inspected. No minimum cut count.
6. For each required node, either provide suitable evidence/reasoning or an explicit gap row.
   Close a gap when replacing it with evidence. If evidence weakens the argument, send the affected
   node to `develop-argument`; if it changes the author's judgment, involve the author.

## Chapter branch

Maintain Code & math using [chapter-format.md](../frame/references/chapter-format.md): source,
node, placement and why the reader needs each item. Reuse existing author decisions. Prefer inline
minimal examples; long excerpts may live in local assets. Read-only originals and copied assets
preserve archive provenance. Link derivations as `reasoning` evidence, not as fictional events.

## Readiness

Done when evidence is attributable, bounds are explicit, source selection is accounted for and
required nodes have evidence or named gaps. Run
`python3 <learning-os>/skills/writing/scripts/verify_brief.py <brief> --stage examples`.
An illustrative scenario is labelled as such and cannot be used as factual support. Unverified
central facts can remain visible in a working draft, but prevent a `ship` verdict. An unresolved
research question may remain if the article promises exploration and makes no unsupported answer.

**Confirmation gate:** Present the examples and evidence to the author and ask: "Do these examples support the reasoning appropriately? Any evidence gaps or mismatches?" Only proceed to drafting after explicit author confirmation.

No personal anecdote is required. Do not fabricate one or call an evidence-based external case an
inferior substitute. Missing evidence can be addressed by research, narrower claims or a bounded
open question; extra anecdotes do not repair an invalid inference.

## Handoffs and contract test

Ready evidence → `write-content`. A missing warrant → `develop-argument`. A substantive revised
understanding → `snapshot-writing` when authorized. Leave sources, material roles and registry tiers
unchanged; `archive-materials` records actual use after delivery.

Test a vivid personal incident supporting a universal claim: report the scope mismatch. Test an
external-only explanation: allow it to proceed. Test an illustrative example passed off as factual
support: reject that evidence role. Report gap rows rather than manufacturing cases.
