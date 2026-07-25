---
name: research
description: Synthesis researcher - produce judgment no single source contains. Use when sources conflict, when the user wants to form a position on a live debate, connect new sources against their own earned models, test a hunch that spans fields, resolve a contested wiki claim, extend a mastered mainline past the course (frontier mode - key people, current advances, papers), or says "/research <question>". Not for quick factual lookups (answer directly or query the wiki), field overviews (/survey), or studying a topic (/curriculum + /learn). The deliverable is a written report centered on connections, the user's judgment, and "so what".
---

# Research — Research Companion

Last updated: 2026-07-24

The one component of the Learning OS that **creates** knowledge instead of consuming it. Everything upstream feeds it: `wiki/` holds what the sources say, `learning/` holds what the learner has earned — research overlays them and produces the judgment that exists in neither. It owns the `can-generate` rung and the `framework.md` Frontier: the system's growth past what any course contained. The deliverable is always **written** — writing is where the thinking completes, not packaging.

**Tutor, not a homework-answer machine** — decompose and involve the user; the Judgment is always theirs.

## Entry gate — no tension, no research

Research starts from a **live tension**:

- two credible sources that disagree,
- a source that contradicts one of the user's earned `learning/` records,
- a `contested: true` wiki page,
- a question no single source answers.

No tension? Say so and route: quick factual question → answer it directly or query the wiki; "map this field / what's worth learning" → `/survey`; "help me understand X properly" → `/curriculum` + `/learn`; a mainline just closed at can-transfer and the user wants to push past the course → **frontier mode** (below), the one tension-free entry. Research is scoped by **question**, never by time budget — there are no hours/weeks modes here.

## Frontier mode — extend past the course

Entered when `/evaluate` closes a mainline's loop tier, or the user asks to deepen a mastered area ("who moves this field? what's current?"). No tension required — the input is `framework.md`: its earned Layers and its Frontier.

1. Read the earned structure — frontier work anchors to *what the learner owns*, not to the field in the abstract.
2. Scan the field's living edge: key people and groups, current advances, the papers that matter now. Web research, heterogeneous sources.
3. **Annotation rule:** every entry written to `framework.md` Frontier MUST name the earned Layer item it *extends* or *threatens* ("MuZero line — threatens your 'model-free is enough' model"). Unanchored link dumps are a reading list, not a frontier.
4. Add `hypothesized` edges the scan suggests; add `frontier` nodes for structures beyond the course.
5. If the scan surfaces a live tension — and it usually does — offer to escalate into the report pipeline above.

Frontier mode's deliverable is the updated `framework.md` Frontier (+ optional wiki ingest offer). It produces **no judgment and no report**, so it is NOT `can-generate` evidence — only the report pipeline is.

## One question per report

Compress the ask into one "true question" and confirm it with the user before researching. If it decomposes into several independent questions, pick the load-bearing one; file the rest as Open Questions at the end of the report.

## Workflow

### 1. Assemble heterogeneous material

Pull from every shelf available: fresh sources, `wiki/` pages, earned `learning/` records and cases. Prefer heterogeneous over more-of-the-same — the highest-value connections cross the wiki/learning wall: an external claim placed against a model the user built. (The John Snow move: the map plus the death records; neither sufficient alone.)

### 2. Map the tension — steelman gate

Organize by *issue*, never by author. Per position: what it argues, its method, its blind spot.

- **Steelman gate:** you MUST be able to state each position in terms its holders would endorse — especially the one the user disagrees with. Can't? Understanding is insufficient — keep reading; don't proceed to judgment.
- **Name the crux:** where does the disagreement bottom out — a different assumption, different evidence, or different values? A dispute without a located crux is a summary, not research.
- Separate expert-vs-expert disagreements (fine-grained, conditional) from expert-vs-public gaps (usually where the real opportunity is).

### 3. Hunt connections

Run the standing question set explicitly: What's missing? Which sources disagree? Which assumptions conflict? Can two fields combine? What does the user's own model predict here? What prediction follows?

- **Combination rule:** every insight MUST cite ≥2 independent sources whose *combination* — not either alone — supports it.

### 4. Draw the judgment — with the user

**My Judgment is the user's** (HITL): present the tension, the crux, and the candidate insights; draw their position out in dialogue and write down *theirs*. You MUST NOT ghost-write it. If they haven't formed one, the section says so.

### 5. Answer "so what?"

What decision or action changes — and what future observation would confirm or falsify the judgment. An insight with no consequence is trivia.

## Report format

Write `learning/<slug>/research-<question-slug>.md` (standalone if no topic exists):

```markdown
# Research: <question>
## The Question (one sentence, confirmed with the user)
## The Tension — positions steelmanned; the crux named (assumption / evidence / values)
## Connections — what emerges between materials; each insight with its source combination
## My Judgment — the user's position, formed in dialogue (HITL — this section is theirs)
## So What — the decision this changes + a prediction or falsifier
## Open Questions — decomposed candidates not pursued
```

## Feedback into the system

- The report is `can-generate` evidence for `/evaluate` — the system's highest mastery tier.
- The user's judgment enters `framework.md` under General frameworks; report insights add `hypothesized` edges. Frontier mode writes the Frontier section (annotation rule above). Research never flips anything to `earned` — that takes the loop.
- If the judgment contradicts an earned `learning/` record, flag it for `/reflect` — don't edit the model here.
- Offer (soft, never force) to file the report into the wiki via `llm-wiki-ingest`; never write `wiki/` directly.

## Contract test

Report contains a steelmanned tension with a named crux; every connection cites ≥2 independent sources whose combination supports it; Judgment is the user's or explicitly absent; So What names a changed decision and a falsifier; one question per report. Frontier mode: every Frontier entry names the earned Layer item it extends or threatens; an unanchored entry is rejected; no report is claimed and no `can-generate` evidence produced without the report pipeline.

## Handoffs

**In:** a live tension (report pipeline) — or, for frontier mode, a mainline whose loop tier `/evaluate` closed, plus `framework.md`'s earned Layers and Frontier.

**Out:**
- Report written → `research-*.md` → `can-generate` evidence for `/evaluate`; judgment into `framework.md` General frameworks.
- Judgment contradicts an earned record → flag → `/reflect <slug>`.
- Frontier scan done → annotated Frontier entries + `hypothesized` edges in `framework.md` → tensions found become the next report candidates.
- Sources worth keeping → offer `llm-wiki-ingest` (soft, never forced).

## Boundaries

- vs quick lookup / wiki query: locating and restating what a source says is not research — no tension, no report.
- vs `/survey`: survey triages a field *before* learning and *surfaces* controversies; research *resolves* one into judgment — and frontier mode extends a mainline *after* mastery, anchored to earned models. "Should I learn X?" → survey. "Who's right about X?" → research. "I've mastered X — what's past the course?" → frontier mode.
- vs `/learn`: the tutor internalizes established knowledge over a syllabus; research creates knowledge the sources don't contain. "Understand X over weeks" is the learning pipeline, not a research mode.
- vs llm-wiki: the wiki organizes what sources say — including debate maps (`comparisons/`) and `contested:` flags; research judges between them. Contested wiki pages are standing research candidates; reports may be filed into the wiki afterward (via ingest, offered softly) — never the reverse.
