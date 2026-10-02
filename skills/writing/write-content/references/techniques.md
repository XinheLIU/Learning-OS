# Writing Techniques for Expository Blog Posts

> Last updated: 2026-10-02

Use these techniques while drafting and reviewing, according to the brief's purpose and reader. They are craft choices, not a fixed article shape.

Techniques 1–14 help communicate an idea. Techniques 15–17 apply when the article makes a recommendation, uses personal experience or engages a real disagreement; none is a universal entry gate.

## Contents

1. [Structure blueprint](#structure-blueprint)
2. [The 17 techniques](#the-17-techniques)
3. [Revision checklist](#revision-checklist)

## Structure blueprint

One useful arc, adapted to the purpose:

1. **Tension opening** — challenge a default belief the target reader holds, or pose a concrete problem they recognize. Never open with a definition or "In this post I will...".
2. **Ladder** — the body is a chain of question → answer → new question. Each section resolves one question and raises the next. The reader should never wonder "why am I reading this paragraph?"
3. **Payoff** — deliver the promised gain: an explanation, a decision criterion, a capability or a sharper open question.
4. **Close** — state what follows and any remaining uncertainty. An exploration can end with what evidence would distinguish its possible answers.

## The 17 techniques

### 1. Plain words first, term second (先讲人话，再讲概念)

Explain the idea in everyday language, then attach the formal term.

> Weak: "Idempotency means f(f(x)) = f(x)."
> Strong: "Run it once or run it five times — the result is the same. That property is called idempotency."

### 2. Examples where understanding needs them (难点处举例)

Use a concrete case where the reader needs one to understand or evaluate the claim. Distinguish a sourced event from a labelled illustrative scenario. The latter can explain but cannot prove that a real-world result occurred; missing factual evidence is a `[VERIFY]` gap.

**Multi-scale triangulation**: For complex mechanisms, give 2-3 examples at different scales (individual → team → organization → industry) that converge on the same principle. This "zoom" effect shows the mechanism is general, not cherry-picked. Sample 3 (组织资本): organizational capital appears in surgeon performance (individual) + Wall Street analyst careers (professional) + surgery team coordination (group) + company culture (organizational) — four scales, one principle. The reader sees the same dynamic repeated across contexts, each reinforcing the others.

### 3. Analogy wherever one fits (能类比的地方就类比)

Map new concepts onto familiar objects: dead-end vs. open road, one-way vs. two-way doors, map vs. territory. One analogy per concept; don't stack them. Drop the analogy once it stops fitting — say where it breaks.

### 4. Pre-empt the reader's objection (预判读者的疑问)

Address relevant objections at the step where they matter, fairly and with evidence. Explanations may instead address a likely confusion; explorations compare live alternatives. There is no objection quota.

### 5. One cognitive step at a time (一次只推进一个认知台阶)

Each section adds exactly one new idea. If a paragraph needs two new concepts to make its point, split it and sequence them. Test: could you title every section with the single question it answers?

### 6. Alternate abstract and concrete (抽象与具体交替)

Theory → case → refined theory. A post that stays abstract reads academic; one that stays anecdotal proves nothing. The rhythm is the argument.

**Systematic alternation at scale**: At the paragraph level, alternate claim and illustration. At the section level, use the framework-driven pattern (Technique 18): each major part gets concept + research + examples before moving to the next part. The samples demonstrate this at both scales — theory and practice interleave within paragraphs AND within major sections. Sample 2 (系统思维) introduces each analytical layer (基本归因谬误 → 人因/系统视角 → 显性失误/潜在条件 → 三类错误), then immediately grounds it with the Boeing 737 MAX case analyzed through those same layers. The alternation is structural, not decorative.

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

Anchors that only flatter the subject read as marketing — state limits, caps, costs, and deprecations with the same precision as capabilities. Every anchor traces to the materials (hard rule 2); if the materials come from a biased source (vendor docs, competitor comparisons), say so in the text.

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
- Never invent or embellish one (hard rule 1). Without a personal incident, use an appropriate external case or labelled illustration. This is not a quality downgrade.

### 17. Name the opponent (指名对手)

When arguing against a belief, establish that it is actually held and represent its strongest relevant version. The brief's Answer/objections or legacy 对立面 field supplies it. Explanations and explorations do not require an opponent.

> Weak: "Some people think effort is what matters."
> Strong: "The 'one more hour' school — every study-hard guide, every parent who counted your desk time — holds that effort is the input and results are the output."

- Keep objections tied to the same central question; several objections can belong in one piece.
- The opponent must be steelmanned before being answered: state their best version, then the specific condition under which it fails (technique 4 does the local work; this one sets the frame).
- If there is no evidence that the opposing belief is held, remove the attribution or return to framing; a named individual is not required.

## Advanced structural techniques

### 18. Framework-driven explanation (框架式展开)

When explaining a complex concept with multiple dimensions or types, build a multi-part logical framework and systematically fill each part with: (1) sub-concept definition, (2) research establishing it, (3) examples at 2-3 different scales, (4) transition to next part.

Structure:
```
Opening (concrete puzzle/case)
  ↓
Concept definition (plain words → formal term)
  ↓
Framework introduction (3-5 dimensions/types/stages)
  ↓
Dimension 1:
  - What it is (concept)
  - Who established it (research narrative)
  - How it appears (2-3 examples at different scales)
  - Why it matters (implication)
  ↓
Dimension 2: [same pattern]
  ↓
Dimension 3: [same pattern]
  ↓
Synthesis (connects back to opening)
```

Example from Sample 3 (组织资本):
- Opens: "2025 年夏天，随着自家的大模型表现不及预期，Meta 面临从 AI 第一集团掉队的局面。扎克伯格再也坐不住了，直接导演了一出昂贵的人才版《复仇者联盟》。他先是花 143 亿美元投资 Scale AI...又从 OpenAI、Google DeepMind、Anthropic 重金挖了几十个研发主力...那你说巨星云集，要钱有钱，要算力有算力，要数据有数据，Meta 就算不立即登顶，是不是也应该重返第一集团呢？并没有。"
- Concept: "组织资本（organization capital）：人力资本长在人身上，组织资本长在人与人之间。"
- Framework: "1998 年...珍妮·纳哈皮特和苏曼特拉·戈沙尔的一篇论文提出，组织资本的好坏，关键在于你这个公司是怎么让知识流动的。他们把组织的知识流动拆解成了认知、结构和关系三个维度"
- Dimension 1 (cognitive capital): Define "认知资本的关键是协调多样性" → research anchor "W·罗斯·阿什比的'必要多样性定律（law of requisite variety）'" → NASA Mars failure example (unit mismatch) + hospital medical terminology → implication "你们的坐标系必须对齐"
- Dimension 2 (structural capital): Define "结构资本的关键是任何人有问题都知道该找谁" → research "交易记忆系统（transactive memory system）" → 2005 surgery team study (team experience matters beyond individual experience) → OpenAI/Anthropic Slack culture → implication "这个地图是在配合中长出来的"
- Dimension 3 (relational capital): Define "关系资本的关键，则是团队心理安全" → research "艾米·埃德蒙森（Amy C. Edmondson）" nursing study → better teams report MORE errors because they feel safe → implication "如果你听不到坏消息，那你就要感到危险了"
- Synthesis: "领导力不是亲自去当公司里那个最强大脑；领导力是创造一个场，让许多大脑，组合成一个更大的大脑。组织有它自己的智力。1 + 1 > 2，是人类文明的基础。"

The power: Each dimension gets the full treatment (concept + research + examples), creating a **repeatable filling pattern** that readers can follow. Not "theory section then examples section" but continuous weaving at each logical node.

**Multi-scale example triangulation**: Within each dimension, use 2-3 examples at different scales (individual → team → company → industry) that converge on the same principle. Sample 1 shows rent appearing across five scales: land (physical) → certificates (legal) → information (knowledge) → relationships (social) → platforms (digital). Sample 3: organizational capital appears in surgeon performance (individual) + Wall Street analysts (professional) + surgery teams (group) + company culture (organizational) — four scales, one principle.

**Research as narrative**: Present research chronologically as an unfolding story of deepening understanding, not isolated citations. Sample 1: "经济学家早就在研究'租'，越研究就越感到...早在祖师爷亚当·斯密 1776 年出版的《国富论》一书中，就已经直觉地提出...到了 19 世纪初，古典经济学家李嘉图把这个直觉系统化...然后是 19 世纪末，马歇尔搞了个观念跃迁...至此经济学家已经意识到...1967 年，公共选择理论经济学家戈登·塔洛克提出...那么 1974 年，国际贸易与发展经济学家安妮·克鲁格进一步指出...至此你可能觉得'租'就是不劳而获……但学者们在 1990 年代又有了一次观念跃迁。" This traces intellectual evolution through 6+ researchers across 200+ years, making the citations read as one coherent discovery arc rather than footnotes.

When to use: Complex explanations with 3+ distinct aspects, research-backed arguments, teaching material that needs both conceptual clarity and practical grounding.

When to skip: Simple how-tos, personal essays, pure arguments (no framework to fill), short posts (<2000 words where the pattern would dominate).

## Revision checklist

Apply to the requested unit and purpose, in this order:

- [ ] The text answers the agreed question and delivers a specific gain to its reader.
- [ ] Each conclusion has reasons and appropriate evidence; uncertainty and conditions stay visible.
- [ ] Explanations follow dependencies; explorations compare answers without forcing a winner.
- [ ] Relevant objections are represented fairly where the piece makes a contested judgment.
- [ ] Examples teach, support or challenge a named point; anecdotes and analogies do not overprove.
- [ ] Facts, quotations and personal accounts retain attribution; unresolved facts carry `[VERIFY]`.
- [ ] Selected sources serve the logic; excluded material has not widened the scope.
- [ ] Terms, transitions and concrete detail match the reader's starting knowledge.
- [ ] Diagrams clarify a relationship already established in the brief and text.
- [ ] The ending delivers the gain or clearly states the remaining question.
- [ ] Confirmed author wording and experience have not been replaced with invented positions.
- [ ] `Last updated: YYYY-MM-DD` is present near the top.
