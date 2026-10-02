# Writing Techniques for Expository Blog Posts

> Last updated: 2026-10-02

Choose structural techniques during material selection, before drafting: they determine which
passages deserve space, which cases need development and how the reader moves between sections.
Record the choice and its purpose in Section plan. Apply sentence-level techniques while drafting
and check their execution at final review. They are craft choices, not a fixed article shape.

Techniques 1–14 help communicate an idea. Techniques 15–17 apply when the article makes a recommendation, uses personal experience or engages a real disagreement; none is a universal entry gate.

## Contents

1. [Structure blueprint](#structure-blueprint)
2. [Core techniques](#core-techniques)
3. [Framework-driven explanation](#18-framework-driven-explanation-框架式展开)
4. [Final review checklist](#final-review-checklist)

## Structure blueprint

One useful arc, adapted to the purpose:

1. **Tension opening** — challenge a default belief the target reader holds, or pose a concrete problem they recognize. Never open with a definition or "In this post I will...".
2. **Ladder** — the body is a chain of question → answer → new question. Each section resolves one question and raises the next. The reader should never wonder "why am I reading this paragraph?"
3. **Payoff** — deliver the promised gain: an explanation, a decision criterion, a capability or a sharper open question.
4. **Close** — state what follows and any remaining uncertainty. An exploration can end with what evidence would distinguish its possible answers.

## Core techniques

### 1. Plain words first, term second (先讲人话，再讲概念)

Explain the idea in everyday language, then attach the formal term.

> Weak: "Idempotency means f(f(x)) = f(x)."
> Strong: "Run it once or run it five times — the result is the same. That property is called idempotency."

### 2. Examples where understanding needs them (难点处举例)

Use a concrete case where the reader needs one to understand or evaluate the claim. Distinguish a sourced event from a labelled illustrative scenario. The latter can explain but cannot prove that a real-world result occurred; missing factual evidence is a `[VERIFY]` gap.

**Different scales serve different questions.** Select another case only when it tests a boundary,
explains a different part of the mechanism or supplies independent support. Similar anecdotes at
several scales do not by themselves establish generality. Develop the decisive case and briefly
cite corroborating cases when their mechanics add nothing new.

### 3. Analogy wherever one fits (能类比的地方就类比)

Map new concepts onto familiar objects: dead-end vs. open road, one-way vs. two-way doors, map vs. territory. One analogy per concept; don't stack them. Drop the analogy once it stops fitting — say where it breaks.

### 4. Pre-empt the reader's objection (预判读者的疑问)

Address relevant objections at the step where they matter, fairly and with evidence. Explanations may instead address a likely confusion; explorations compare live alternatives. There is no objection quota.

### 5. One cognitive step at a time (一次只推进一个认知台阶)

Give each section a clear reader task. Sequence its necessary concepts so the reader can follow the inference; a difficult argument may need several connected steps. Split a paragraph when it asks the reader to resolve two unrelated questions at once.

### 6. Alternate abstract and concrete (抽象与具体交替)

Theory → case → refined theory. A post that stays abstract reads academic; one that stays anecdotal proves nothing. The rhythm is the argument.

**Plan the alternation where it matters.** Put the detailed case beside the inferential step it
clarifies. Another section may need only a short citation or a comparison. Technique 18 connects
framework application with selected evidence; it does not give every section the same filling.

### 7. Map across knowledge systems (概念之间建立映射)

Restate the core idea in the reader's other vocabularies: "In economics terms this is X; an engineer would call it Y." Use only mappings you can defend — a loose mapping damages trust more than no mapping.

### 8. Define by contrast pairs (正反对照)

The fastest way to bound a concept is its near-miss neighbor: risk vs. uncertainty, delegation vs. abdication, caching vs. memoization. Name both sides explicitly and state the one dimension that separates them.

### 9. Stress-test with the extreme case (用极端情况检验观点)

To show a principle is necessary, push its negation to the limit: "Suppose you optimized only for latency — what breaks?" This replaces pages of justification with one thought experiment. (A thought experiment about consequences is analysis, not fiction — keep it mechanical, not narrative.)

### 10. Keep answering "so what?" (不断回答"所以呢")

Each major point should change what the reader understands, can do or still needs to investigate. Cut or merge sections that do not serve that gain.

### 11. Staged compression (阶段性总结)

After each major stretch of argument, compress it into one sentence before moving on: "So the point is: ...". These are the sentences skimmers read — they must carry the whole argument on their own.

### 12. Close with a compressed line (结尾金句)

End on one sentence with contrast or parallel structure that a reader could quote to summarize the post. It must be earned by the argument, not decorative — if it would work pasted onto a different post, it's too generic.

### 13. Anchor with hard specifics (技术细节给硬锚点)

In technical register, a claim earns trust through its anchors: name the actual component (not "a service"), give the real number (not "at scale"), state the version or date boundary.

> Weak: "The system scales to very large datasets and supports batch edits."
> Strong: "A single object type holds tens of billions of objects; one Action edits at most 10,000 of them; v1 was deprecated on 2026-06-30."

Anchors that only flatter the subject read as marketing — state limits, caps, costs, and deprecations with the same precision as capabilities. Every anchor traces to the selected materials; if the materials come from a biased source (vendor docs, competitor comparisons), say so in the text.

### 14. Diagram the load-bearing structure (关键结构配图)

When prose walks through something genuinely spatial — an architecture of components, a pipeline, a cycle, a decision flow, two designs in contrast — add a Mermaid diagram immediately after that prose.

- The diagram restates the text; it must not introduce facts the text doesn't state.
- Place it directly after the paragraph it illustrates, so text and graph read as one unit.
- Use standard `flowchart` syntax (renders on GitHub, Obsidian, VS Code): `LR` for pipelines and cycles, `TB` for layered architectures, `subgraph` for the two sides of a contrast; solid arrows for the main path, dotted for feedback or secondary paths; label edges with the mechanism, not just direction.
- Diagram only where structure is spatial: parallel paths, cycles, layers, branching. A linear point stays prose; short enumerable facts stay a table. Use as many diagrams as the relationships need, including none. Derive logical relationships from the brief, not from decorative layout.

## Depth techniques (15–17)

These are conditional techniques. Use the relevant judgment, objection or incident recorded in the brief; do not invent one to satisfy a checklist.

### 15. State the cost of your position (说明主张的代价)

For a recommendation, state material tradeoffs and conditions. Do not manufacture a cost for an explanation or a question the author has not resolved.

> Weak: "Active recall is more effective than rereading."
> Strong: "Active recall is more effective than rereading — which means most of the study time that felt productive was not. If you adopt this, you lose the sensation of progress that kept you at the desk."

The cost is usually one of: time already invested, a comfortable habit, a defensible-but-wrong default, or a second goal the position sacrifices. Name which. Put it near the payoff, where the reader is deciding whether to act.

### 16. Earned example over borrowed example (自己的经历优于二手案例)

Prefer a relevant author incident for specificity and voice, then assess what it establishes. Stronger external evidence takes precedence for factual support. A personal event does not establish industry-wide frequency or causation.

- Use the author's incident at the load-bearing point — the moment the reader most doubts the claim.
- Keep it dated and specific: what was believed, what was done, what it cost, what changed the mind.
- Never invent or embellish an incident. Without a personal incident, use an appropriate external case or labelled illustration. This is not a quality downgrade.

### 17. Name the opponent (指名对手)

When arguing against a belief, establish that it is actually held and represent its strongest relevant version. The brief's Answer/objections or legacy 对立面 field supplies it. Explanations and explorations do not require an opponent.

> Weak: "Some people think effort is what matters."
> Strong: "The 'one more hour' school — every study-hard guide, every parent who counted your desk time — holds that effort is the input and results are the output."

- Keep objections tied to the same central question; several objections can belong in one piece.
- The opponent must be steelmanned before being answered: state their best version, then the specific condition under which it fails (technique 4 does the local work; this one sets the frame).
- If there is no evidence that the opposing belief is held, remove the attribution or return to framing; a named individual is not required.

## Advanced structural techniques

### 18. Framework-driven explanation (框架式展开)

Use an agreed framework to derive insight, then allocate material to the reasoning that earns it.
The framework is more than labels: show how its dimensions interact, what it predicts or explains,
where it fails and how applying it changes the answer to the central question.

During framework development, test whether the distinctions and relations support the thesis.
During material planning, decide where the reader needs a definition, a worked mechanism, a
contrasting case, research support or a short reminder. Every dimension need not receive all five.

An illustrative 1800-word plan (lengths demonstrate a choice, not a default):

| Section task | Words | Material treatment | Why this much space |
| :--- | ---: | :--- | :--- |
| Pose the puzzle and thesis | 200 | One short sourced observation | Establish the problem without retelling its history |
| Explain and apply the decisive mechanism | 850 | Develop one case; unpack the inference | This is the difficult step carrying the thesis |
| Test the boundary against an alternative | 500 | Compare a counterexample; briefly cite corroboration | Establish where the mechanism holds and fails |
| Derive the resulting judgment | 250 | Synthesize the established evidence | Earn the payoff without introducing another case |

Choose a different allocation if the argument needs it. Reader continuity comes from a question
answered and a next question made necessary, not a repeated section template. Material density
includes the explanation between citations; compressed evidence without its warrant is too dense.
If a source contributes only one useful sentence, take that passage rather than its entire account.

Use research narrative only when the development of an idea helps establish the claim. See
[research-narrative-patterns.md](research-narrative-patterns.md) for that conditional choice. Source
count, date range and researcher biography do not determine how much space a claim deserves.

## Final review checklist

Apply to the requested unit and purpose, in this order:

- [ ] The text answers the agreed question and delivers a specific gain to its reader.
- [ ] Each conclusion has reasons and appropriate evidence; uncertainty and conditions stay visible.
- [ ] Explanations follow dependencies; explorations compare answers without forcing a winner.
- [ ] Relevant objections are represented fairly where the piece makes a contested judgment.
- [ ] Examples teach, support or challenge a named point; anecdotes and analogies do not overprove.
- [ ] Facts, quotations and personal accounts retain attribution; unresolved facts carry `[VERIFY]`.
- [ ] The agreed synthesis is actually derived, and introduced frameworks are applied.
- [ ] Selected excerpts receive their planned depth; section lengths and transitions realize the material plan.
- [ ] Selected sources serve the logic; excluded material has not widened the scope.
- [ ] Terms, transitions and concrete detail match the reader's starting knowledge.
- [ ] Diagrams clarify a relationship already established in the brief and text.
- [ ] The ending delivers the gain or clearly states the remaining question.
- [ ] Confirmed author wording and experience have not been replaced with invented positions.
- [ ] `Last updated: YYYY-MM-DD` is present near the top.
