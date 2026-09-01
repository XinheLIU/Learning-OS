# Writing Techniques for Expository Blog Posts

> Last updated: 2026-09-01

Distilled from analyzing high-performing explanatory writing. Apply during Step 3 (structure) and Step 4 (drafting). The revision checklist at the bottom is used in Step 5.

Techniques 1–14 make an idea land. Techniques 15–17 decide whether there was an idea worth landing — they apply whenever a brief is present, and their absence is what "不够深度" describes.

## Contents

1. [Structure blueprint](#structure-blueprint)
2. [The 17 techniques](#the-17-techniques)
3. [Revision checklist](#revision-checklist)

## Structure blueprint

Every post follows this arc:

1. **Tension opening** — challenge a default belief the target reader holds, or pose a concrete problem they recognize. Never open with a definition or "In this post I will...".
2. **Ladder** — the body is a chain of question → answer → new question. Each section resolves one question and raises the next. The reader should never wonder "why am I reading this paragraph?"
3. **Payoff** — convert the argument into something usable: steps, a 2×2, a decision rule, criteria, a checklist.
4. **Compressed close** — one sentence that restates the whole post with contrast or rhythm. Written last, after the argument is settled.

## The 17 techniques

### 1. Plain words first, term second (先讲人话，再讲概念)

Explain the idea in everyday language, then attach the formal term.

> Weak: "Idempotency means f(f(x)) = f(x)."
> Strong: "Run it once or run it five times — the result is the same. That property is called idempotency."

### 2. Example immediately after every hard point (难点处立即举例)

The moment an abstract claim lands, follow with a concrete case from business, engineering, or history — never more than one paragraph away. If no real example exists in the materials, that's a `[VERIFY]` gap, not a license to invent one.

### 3. Analogy wherever one fits (能类比的地方就类比)

Map new concepts onto familiar objects: dead-end vs. open road, one-way vs. two-way doors, map vs. territory. One analogy per concept; don't stack them. Drop the analogy once it stops fitting — say where it breaks.

### 4. Pre-empt the reader's objection (预判读者的疑问)

At each step, voice the pushback a smart skeptic would raise, then answer it: "You might object that...", "But doesn't this just mean...". This is the main device that makes an argument feel airtight instead of preachy. 2–4 per post is typical.

### 5. One cognitive step at a time (一次只推进一个认知台阶)

Each section adds exactly one new idea. If a paragraph needs two new concepts to make its point, split it and sequence them. Test: could you title every section with the single question it answers?

### 6. Alternate abstract and concrete (抽象与具体交替)

Theory → case → refined theory. A post that stays abstract reads academic; one that stays anecdotal proves nothing. The rhythm is the argument.

### 7. Map across knowledge systems (概念之间建立映射)

Restate the core idea in the reader's other vocabularies: "In economics terms this is X; an engineer would call it Y." Use only mappings you can defend — a loose mapping damages trust more than no mapping.

### 8. Define by contrast pairs (正反对照)

The fastest way to bound a concept is its near-miss neighbor: risk vs. uncertainty, delegation vs. abdication, caching vs. memoization. Name both sides explicitly and state the one dimension that separates them.

### 9. Stress-test with the extreme case (用极端情况检验观点)

To show a principle is necessary, push its negation to the limit: "Suppose you optimized only for latency — what breaks?" This replaces pages of justification with one thought experiment. (A thought experiment about consequences is analysis, not fiction — keep it mechanical, not narrative.)

### 10. Keep answering "so what?" (不断回答"所以呢")

Every theoretical point must cash out into a decision, a step, a classification, or a criterion by the end. If a section changes nothing about what the reader would do, cut it or merge it.

### 11. Staged compression (阶段性总结)

After each major stretch of argument, compress it into one sentence before moving on: "So the point is: ...". These are the sentences skimmers read — they must carry the whole argument on their own.

### 12. Close with a compressed line (结尾金句)

End on one sentence with contrast or parallel structure that a reader could quote to summarize the post. It must be earned by the argument, not decorative — if it would work pasted onto a different post, it's too generic.

### 13. Anchor with hard specifics (技术细节给硬锚点)

In technical register, a claim earns trust through its anchors: name the actual component (not "a service"), give the real number (not "at scale"), state the version or date boundary.

> Weak: "The system scales to very large datasets and supports batch edits."
> Strong: "A single object type holds tens of billions of objects; one Action edits at most 10,000 of them; v1 was deprecated on 2026-06-30."

Anchors that only flatter the subject read as marketing — state limits, caps, costs, and deprecations with the same precision as capabilities. Every anchor traces to the materials (hard rule 2); if the materials come from a biased source (vendor docs, competitor comparisons), say so in the text.

### 14. Diagram the load-bearing structure (关键结构配图)

When prose walks through something genuinely spatial — an architecture of components, a pipeline, a cycle, a decision flow, two designs in contrast — add a Mermaid diagram immediately after that prose.

- The diagram restates the text; it must not introduce facts the text doesn't state.
- Place it directly after the paragraph it illustrates, so text and graph read as one unit.
- Use standard `flowchart` syntax (renders on GitHub, Obsidian, VS Code): `LR` for pipelines and cycles, `TB` for layered architectures, `subgraph` for the two sides of a contrast; solid arrows for the main path, dotted for feedback or secondary paths; label edges with the mechanism, not just direction.
- Diagram only where structure is spatial: parallel paths, cycles, layers, branching. A linear point stays prose; short enumerable facts stay a table. A long technical post carries roughly 3–8 diagrams; a business post rarely needs more than one simple flow or 2×2.

## Depth techniques (15–17)

These three are why the piece exists. They need a brief — the positions, opponents, and incidents they draw on live in `brief.md`, not in the materials.

### 15. State the cost of your position (说明主张的代价)

Say what the reader gives up by agreeing with you. A position that costs nothing is not a position — it's a platitude with citations.

> Weak: "Active recall is more effective than rereading."
> Strong: "Active recall is more effective than rereading — which means most of the study time that felt productive was not. If you adopt this, you lose the sensation of progress that kept you at the desk."

The cost is usually one of: time already invested, a comfortable habit, a defensible-but-wrong default, or a second goal the position sacrifices. Name which. Put it near the payoff, where the reader is deciding whether to act.

### 16. Earned example over borrowed example (自己的经历优于二手案例)

When the brief's *Author's markers* carry a real incident, it outranks anything in the sources. A borrowed example proves the claim is publishable; an earned one proves the author paid for it.

- Use the author's incident at the load-bearing point — the moment the reader most doubts the claim.
- Keep it dated and specific: what was believed, what was done, what it cost, what changed the mind.
- Never invent or embellish one (hard rule 1). No incident in the brief means the section leans on a borrowed example, and that's an honest downgrade, not a license.

### 17. Name the opponent (指名对手)

Write against a belief someone actually holds, and say who holds it — a named book, community, teacher, or the reader's own former self. The brief's 对立面 field supplies this.

> Weak: "Some people think effort is what matters."
> Strong: "The 'one more hour' school — every study-hard guide, every parent who counted your desk time — holds that effort is the input and results are the output."

- One opponent per piece. Two opponents make two pieces.
- The opponent must be steelmanned before being answered: state their best version, then the specific condition under which it fails (technique 4 does the local work; this one sets the frame).
- If you cannot name anyone who holds the belief, it's a strawman — go back to `frame-piece` rather than writing against a phantom.

## Revision checklist

Run against the finished draft; fix every failure:

- [ ] Opening states a tension or problem within the first 3 sentences — no throat-clearing, no "in this post"
- [ ] The post argues exactly one thesis, statable in one sentence
- [ ] Every formal term is preceded or immediately followed by a plain-language explanation
- [ ] No abstract claim goes more than one paragraph without an example or analogy
- [ ] At least two reader objections are voiced and answered
- [ ] Each section answers one question and raises the next (check by titling each section as a question)
- [ ] Key concepts are bounded by an explicit contrast pair
- [ ] The payoff section is actionable: steps, rules, criteria, or a classification
- [ ] Each major part ends with a one-sentence compression; reading only those sentences reproduces the argument
- [ ] The closing line summarizes the thesis with contrast/rhythm and couldn't be pasted onto another post
- [ ] (technical register) Claims carry concrete anchors — component names, numbers, limits, dates — and limits are stated with the same precision as capabilities
- [ ] Every architecture, pipeline, cycle, or contrast the prose walks through has a Mermaid diagram immediately after it; no diagram introduces facts absent from the prose
- [ ] Zero fabricated examples, numbers, or quotes; all unresolved claims carry `[VERIFY]` markers
- [ ] Register is consistent (technical or business) and matches the audience chosen in Step 2
- [ ] `Last updated: YYYY-MM-DD` present near the top

### Depth checks (brief-driven pieces)

Run these first — craft polish on a flat piece is wasted motion. A failure here is a rewrite, not an edit.

- [ ] The thesis is the brief's angle, not a claim the source materials already argue
- [ ] The 对立面 is named as a specific person, book, or community — and is still engaged past the opening section
- [ ] The reader is told what agreeing costs them (technique 15), stated near the payoff
- [ ] Where the brief carries an author incident, it is used at the load-bearing point rather than a borrowed example (technique 16)
- [ ] No material dispositioned `cut` in the brief appears in the draft
- [ ] The *Cost paid* line still holds — the piece did not quietly widen back to covering everything
- [ ] At least one paragraph could not have been written by the source's author
