---
name: survey
description: Investment gate before learning a field. Use when the user wants to explore a new domain, decide what's worth learning, allocate learning time, or says "/survey <field>". Outputs a mainline × mastery-stage matrix — 3–5 learning mainlines (breadth) crossed with four mastery stages (depth), a behavioral milestone in every cell — plus investment triage, curated sources, a gap diagnosis, and a seeded framework.md v0 skeleton that /curriculum, /learn, /evaluate, and /reflect build on.
---

# Survey — Investment Gate

Last updated: 2026-07-24

Runs before any information enters the learning pipeline. The deliverable is an **investment decision on a two-dimensional matrix, not a textbook**:

- **Dimension 1 — breadth: learning mainlines.** A field is not the chapter list of whatever material is at hand, and not a scatter of concepts. It organizes into a few coherent through-lines — each answering one question the field keeps asking. RL's mainlines are value-based control, policy optimization, model-based planning — not "lecture 1..N". A nine-lecture engineering course may collapse into four mainlines (interface fluency / diagnosis / delivery / collaboration). Extracting these is the survey's first job.
- **Dimension 2 — depth: four mastery stages.** Human learning climbs stages: articulate the concepts → reproduce samples → transfer to unseen scenarios → synthesize and link. "Can explain DQN" and "can implement DQN" are different investments; so are "can implement" and "can adapt to a novel environment". Distinguishing these is the survey's second job.
- **The matrix is where they cross.** Mainlines are rows, stages are columns, every cell is a concrete behavioral milestone, and each mainline gets a marked **target stage**. Breadth and depth must genuinely intersect — parallel per-concept lists that never meet do not count.

Downstream indexes into this matrix: `/curriculum` sequences lessons cell by cell and sizes them to the gap, `/learn` scaffolds from the current stage, `/evaluate` measures achieved mastery against target cells, `/reflect` checks drift against both.

## The four stages (shared ladder)

Mapped onto the mastery ladder shared with `/evaluate` — never invent a parallel scale, never numeric scores:

1. **can-recall** (articulate) — recite the concepts and articulate them unprompted.
2. **can-apply** (samples) — reproduce **samples** hands-on: worked examples in the field's own medium — a coding exercise, a derivation, a model essay to imitate, a canonical problem set. Can answer standard questions about them.
3. **can-transfer** (adapt) — carry the skill into unseen scenarios with no recipe.
4. **can-generate** (synthesize) — synthesize: build links across mainlines, judge trade-offs, produce something the sources didn't contain. (`can-teach` sits just below this rung; at survey granularity the two merge — explaining a link *is* teaching it. `/evaluate` may still distinguish them.)

## Rules

- **~30-minute cap.** A survey is a map and a budget, not a dissertation.
- **Mainlines come from the field's own knowledge domains** — how practitioners carve the field, not the source material's chapter structure, not a course you remember. 3–5 of them, each stating the one question it answers. If two candidate mainlines answer the same question, merge them; if one answers two, split it.
- **Every cell is behavioral.** An observable act, not an adjective ("solid understanding" is banned). **can-apply cells MUST name samples** — the specific artifact to reproduce ("implement replay buffer + target network, train on CartPole"; "imitate the structure of essay X"), never "do some exercises".
- **Cross-links are mandatory: ≥3, labeled** (`bridges`, `prerequisite-of`, `contrasts-with`, `special-case-of`). They live in a compact mainline graph *and* naturally in the can-generate column — stage 4 is the linking stage. A matrix whose rows never touch is a table of contents, not a map.
- **The triage MUST be argued.** Every mainline's target has a why; a survey that cuts nothing is a reading list, not a gate — you MUST name at least one SKIP or stop-early.
- **Two entry paths, one output.** Existing material → deepen and reorganize it. Blank slate → full web research. Re-running `/survey` on a topic with an existing `survey.md` is a *deepening pass* — refine the mainlines and milestones against what `notes.md` now shows, don't start over.
- **You MUST NOT build models or teach here.** That is `/learn`'s job. Map the terrain, allocate the time, hand off.
- **Seed structure, never earn it.** You write `framework.md` v0 — `target` nodes and `hypothesized` edges only. Marking anything `earned` from a survey is confabulation; earning belongs to the loop.
- **Never write to `wiki/`.** The wiki is owned by the llm-wiki suite; the handoff is an offer, not an action.

## Flow

### 1. Auto-init

If `learning/<slug>/` doesn't exist, create it. Don't ask permission.

### 2. Determine entry path

If `learning/<slug>/survey.md` or `notes.md` already exists, read it first — it is Path A material. Otherwise ask: "How much do you already know about <field>? Any notes, projects, or reading you want me to build on?"

- **Path A — material exists** (prior survey, notes, user context): organize and deepen what's there, research only the gaps.
- **Path B — user knows little:** full web research, searches in parallel where possible.

Either path feeds the same analysis below.

### 3. Research the landscape

Cover, in either path:
- **History & key people** — who built the field, what they contributed, what problems they were solving. Narrative, not timeline.
- **Current state** — SOTA, key people/groups now, open problems.
- **Controversies** — what practitioners argue about, schools of thought. (These are `/research` candidates — note them.)
- **Trajectory** — what changed in the last ~5 years, where money and attention are going.

If sources conflict, note the conflict — don't pick a winner silently.

### 4. Extract the mainlines (Dimension 1)

- Identify the 3–5 through-lines the field actually splits into, each with the one question it answers.
- Build a **fold-in table**: which concepts/topics from the material belong to which mainline. Source chapters will cross-cut mainlines — that's expected and is the evidence you extracted rather than copied.
- Render a compact Mermaid `graph` of the mainlines with the ≥3 labeled cross-edges (dashed).

```markdown
| Mainline | The question it answers | What folds into it |
| :--- | :--- | :--- |
| Value-based control | How do I act well by estimating how good states are? | TD learning, SARSA, DQN + tricks |
| Policy optimization | How do I improve behavior directly? | REINFORCE, A2C, TRPO/PPO, DDPG/SAC |
| Model-based planning | What if I learn the world and plan in it? | Dyna-Q, MCTS, MuZero |
```

Present the mainlines before the matrix, so the triage argument can point at them.

### 5. Build the matrix (Dimension 1 × Dimension 2)

Mainlines × the four stages. Every cell: 1–3 terse behavioral milestones. Mark each mainline's **target stage** with ◀ — cells right of ◀ document what stopping there costs, so still fill them (one line is enough).

```markdown
| | can-recall (articulate) | can-apply (samples) | can-transfer (adapt) | can-generate (synthesize) |
| :-- | :-- | :-- | :-- | :-- |
| **Value-based control** | State what Q-learning estimates; why the target network exists. | Implement replay buffer + target network; reproduce DQN on CartPole. | **◀** Adapt DQN to a novel env — choose the tricks (frame stacking, reward shaping) unprompted. | Connect TD targets to critic baselines; judge when value-based beats policy-gradient. |
| **Policy optimization** | Explain what PPO's clip objective protects against. | Reproduce PPO on a Gym benchmark from a reference implementation. | **◀** Tune PPO on a custom env; diagnose divergence from the curves. | Derive why actor-critic bridges both mainlines; design a hybrid for a given problem. |
```

Constraints:
- Targets differ per mainline — that is where "how deep" lives. Not every mainline deserves can-transfer.
- can-apply samples must be in the field's own medium (code for RL, derivations for math, model texts for writing).
- The can-generate cells should carry the cross-mainline links; if a can-generate cell mentions only its own row, look for the missing edge.

### 6. Triage: investment & cuts

```markdown
| Mainline | Investment | Target | Why this deep and no deeper |
| :--- | :--- | :--- | :--- |
| Value-based control | 35% | can-transfer | mission needs working agents, not papers |
| Policy optimization | 40% | can-transfer | the workhorse; everything at work runs on it |
| Model-based planning | 25% | can-apply | rising fast, but mission doesn't need planning yet |
```

Plus a **stop-early / SKIP list** for items *within* mainlines:

```markdown
- SKIP — MuZero internals: not on the mission's critical path; revisit if mission shifts.
- Stop at can-recall — TRPO: superseded by PPO; needed only to read older papers.
```

Constraints:
- Investment percentages MUST roughly sum to 100.
- At least one SKIP or stop-early, argued.
- The why-column MUST tie target to mission: *why this deep and no deeper*.

### 7. Curate sources

Rank what to read — and say what each is *for* — and name what to skip:

```markdown
## Sources
### Read (ranked, with what each is FOR)
- <source> — best single explanation of <X>; read for the mental model, skip the appendix
### Don't read (with why)
- <source> — popular but derivative of <other>
- <source> — outdated since <development>
```

### 8. Diagnose the gap

Place the user per mainline on the same four columns, **with evidence** (from Path A material, or 2–3 quick probe questions per mainline). Split placements within a mainline are fine — call them out.

```markdown
## Gap Diagnosis
| Mainline | Current | Target | Evidence |
| :--- | :--- | :--- | :--- |
| Value-based control | can-recall | can-transfer | explained target network unprompted; never trained one |
| Policy optimization | none | can-transfer | couldn't say what the clip objective protects against |
```

The **gap (current → target) is the supervision signal**: `/curriculum` front-loads lessons on big-gap cells; `/learn` scaffolds from the current stage (`none`/`can-recall` → novice treatment, worked samples; `can-apply`+ → practitioner treatment, transfer tasks); `/evaluate` closes a mainline when evidence reaches its target cell. A wrong placement mis-tutors every later session — when in doubt, round down.

### 9. Write survey.md

Write `learning/<slug>/survey.md`: date + sources consulted, a short narrative section (history & people, current state & controversies, trajectory), then **mainlines** (fold-in table + graph), then **the matrix**, then triage, sources, gap diagnosis.

### 10. Seed framework.md v0

Write `learning/<slug>/framework.md` per [../learn/references/framework-format.md](../learn/references/framework-format.md) — the skeleton the journey will converge on:

- Map: mainline subgraphs; the matrix's key concepts as `target` nodes; your ≥3 labeled cross-links as `hypothesized` edges (dashed).
- Layers: concepts and models listed with status `target`, no gloss — the learner's words come later.
- Frontier → Open tensions: the controversies from step 3, each tied to why it will matter.
- `Iteration: 0`.

Re-running `/survey` (deepening pass) revises `target`/`hypothesized` structure only; anything `earned` is the loop's and MUST NOT be touched here.

### 11. Exit handoffs

- **Soft wiki handoff:** "Want me to feed the Read list into `llm-wiki-ingest` so these sources become wiki pages?" — offer, never force. The Learning OS works without a wiki.
- **Recommend next:** `/curriculum <slug>` to turn the matrix into a course.

## Contract test

`survey.md` contains: 3–5 mainlines each with its question and a fold-in table; ≥3 labeled cross-mainline links; a full mainlines × four-stages matrix where every cell is behavioral, every can-apply cell names a sample, and every mainline has a marked target stage; an argued investment table summing to ~100% with ≥1 SKIP/stop-early; a gap diagnosis per mainline with current + target + evidence on the shared ladder; Read/Don't-read lists with reasons; wiki ingest offered, not forced. `framework.md` v0 exists with only `target` nodes and `hypothesized` edges, seeded tensions, and `Iteration: 0`; a deepening pass leaves `earned` structure untouched.

## Handoffs

**In:** a field the user is considering investing in; optional prior material (`survey.md`, `notes.md`, user notes) for a Path A / deepening pass.

**Out:**
- `survey.md` written → matrix + gap diagnosis + sources → `/curriculum <slug>`.
- `framework.md` v0 seeded → skeleton for the loop skills to earn against.
- Read list curated → offer `llm-wiki-ingest` (soft, never forced).
- Controversies surfaced → logged in `framework.md` Frontier as `/research` candidates — not resolved here.

## Boundaries

- vs `/curriculum`: survey is *strategic* triage (mainlines, target stages, sources); curriculum is *tactical* sequencing (what order, what load budget). Survey decides **what and how deep**; curriculum decides **how**. The matrix is deliberately coarser than a syllabus — mainline extraction and stage differentiation, not lesson plans.
- vs `/evaluate`: survey **sets the bar** (target cells) and makes the initial placement from probes; evaluate **measures achieved mastery** from evidence files. Same ladder, opposite directions — targets are survey's to change, measurements are evaluate's.
- vs `/research`: survey triages a field and *surfaces* controversies; research *resolves* one into judgment. "Should I learn X?" → survey. "Who's right about X?" → research.
