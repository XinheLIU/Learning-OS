---
name: survey
description: Investment gate before learning a field. Use when the user wants to explore a new domain, decide what's worth learning, allocate learning time, or says "/survey <field>". Reads the source registry and the archive's material map, then outputs a mainline × mastery-stage matrix — 3–5 learning mainlines (breadth) crossed with four mastery stages (depth), a behavioral milestone in every cell — plus investment triage, a Scope section dispositioning every source and setting every node's deep/connect mode, a gap diagnosis, and a seeded Structural Memory v0 skeleton in notes.md that /curriculum, /learn, /evaluate, and /reflect build on.
---

# Survey — Investment Gate

Last updated: 2026-09-28

## Preconditions — the two files this reads

Survey does not go looking for material. Two inputs must exist before it runs, and each is owned by
a skill that runs first:

| Input | Owner | Missing → |
| :--- | :--- | :--- |
| `sources/<domain>.md` — the tiered registry | `/curate-sources` | **stop** and route to `/curate-sources <domain>` |
| `<archive>/materials.md` — the material map | `/map-materials` | **stop** and route to `/map-materials <slug> <archive>` |

**Refuse rather than improvise.** A survey that discovers its own sources produces a per-topic
reading list that nothing downstream can check and nothing later can reuse — exactly the state
this split exists to end. Say which file is missing, name the skill that writes it, and stop.

Two narrowings, so the refusal does not become bureaucracy:

- **No archive at all** (a field the learner has no files for) is fine: `materials.md` is required
  only when an archive exists. Say so in the Scope section and continue with the registry alone.
- A **deepening pass** re-reads both files; if one has gained rows since the last run, the Scope
  section is re-derived, not patched.

The archive's location is the `archive:` line `/map-materials` wrote into `survey.md`. Never
hard-code a path, and never scan the archive directly — the map is the interface.

## Mission Contract intake

Before researching or building the matrix, run a required interview and persist a `## Mission
Contract` section in `survey.md`:

- **Desired change / output:** an observable real-world result. If the user says “understand”, ask
  what they will produce, diagnose, decide, or perform.
- **Current level evidence:** concrete work, reading, performance, or a short probe. Unsupported
  self-ratings are rounded down to the lowest evidenced rung.
- **Why now:** the present consequence or opportunity that makes the topic relevant.
- **Capability gap:** current state → desired state, stated so it can drive sequencing.
- **Constraints:** time, tools, budget, prior commitments, and learning preferences.
- **Non-goals:** explicit scope cuts.
- **Uncertainty:** unresolved answers or confidence limits; never silently guess.

Use adaptive follow-up questions when an answer is vague, unsupported, inconsistent, or overly broad.
Continue only when the outcome is observable, relevance is concrete, current level has evidence, and the
gap can guide the matrix.

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
- **You MUST NOT discover sources here.** Every source named anywhere in `survey.md` resolves to a
  registry `id`. A source you wish existed is a `gap` line naming what it would supply, routed to
  `/curate-sources` — never a citation.
- **Every node carries a mode.** `deep` or `connect`, each with a why. The mode partition is the
  scoping decision this skill exists to make; a survey whose nodes are all `deep` has not scoped.
- **The Roadmap has no critical path.** Ordering deep nodes into one thread is `/curriculum`'s
  `## Critical Path`. The Roadmap orients: whole field, what's in, what's cut, checkpoints.
- **Seed structure, never earn it.** You write the Structural Memory section of `notes.md` v0 — `target` nodes and `hypothesized` edges only. Marking anything `earned` from a survey is confabulation; earning belongs to the loop.
- **Never write to `wiki/`.** The wiki is owned by the llm-wiki suite; the handoff is an offer, not an action.

## Flow

### 1. Auto-init

If `learning/<slug>/` doesn't exist, create it. Don't ask permission.

### 2. Determine entry path

Read, in order: `sources/<domain>.md`, the `archive:` line in `learning/<slug>/survey.md` and the
`materials.md` it points at, then `notes.md` if it exists. The map answers "what material is there"
without asking — ask only what the files cannot say: "How much of this have you actually worked
through?"

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

### 7. Scope — what enters, and how deep

One section, two tables. Together they are the scoping decision: **which sources this mission
opens, and which concepts it will be able to *use* versus merely *place*.** Everything downstream
reads this section and nothing re-derives it.

#### 7a. Sources × disposition

Every row of `sources/<domain>.md` whose `domains` touch this field gets a disposition. Not a
ranking — a decision, tied to the mission:

```markdown
### Scope — sources

| id | tier | Disposition | Why, against the mission |
| :-- | :-- | :-- | :-- |
| vaswani-attention | 1 | DEEP | §3.2 is the only place the √d_k argument is made from scratch |
| d2l-attention | 1 | DEEP | the block anatomy, worked; the course's own notes skip the residual path |
| dlai-attention-pytorch | 2 | SKIM | one runnable implementation; the rest restates d2l |
| bert | 1 | SKIP | encoder-only branch; the mission's output is a decoder chapter |
| dodrio | 3 | SKIP | figures only, and the chapter authors its own diagrams |
```

- `DEEP` — read it through; lessons may teach from it.
- `SKIM` — one section or one excerpt, named. A SKIM with no named part is a DEEP that lost its
  nerve.
- `SKIP` — argued. **At least one SKIP, and a tier-1 SKIP is a good sign**, not a mistake: tier is
  what a source is worth in general, disposition is what it is worth *here*.

A source you needed and could not find in the registry is a **`gap` line**, never a citation:

```markdown
- gap — nothing registered covers RMSNorm's derivation → `/curate-sources machine-learning`
```

When `materials.md` exists, also state which of its `key` rows each DEEP source is realized by —
the registry names the source, the map names the files, and `/curriculum` needs both.

#### 7b. Nodes × mode

Every node you are about to seed into Structural Memory is `deep` or `connect`:

| Mode | The learner will be able to | Costs | Earned by |
| :--- | :--- | :--- | :--- |
| `deep` | **use** it — derive, implement, debug, choose between | a K/S lesson, drills, a ledger row | a construction at `none`/`hint` |
| `connect` | **place** it — say what it is, what it relates to, and why it is not the focus | one `[C]` lesson, ~10 min | one edge, stated in the learner's words |

```markdown
### Scope — nodes

| Node | Mainline | Mode | Why |
| :-- | :-- | :-- | :-- |
| self-attention / QKV | attention | deep | the chapter's load-bearing derivation |
| multi-head | attention | deep | the reader must choose h; that needs the trade-off |
| RNN encoder-decoder | sequence representation | connect | it explains why attention exists; nothing is built on it |
| mixture-of-experts | efficiency variants | connect | first pass only — a `deep` pass is a later mission |
```

Three rules:

- **Mode follows the mission's output, not the field's importance.** MoE is important and
  `connect` here, because the chapter does not teach it.
- **A `connect` node still has to be placed.** "Skip it entirely" is not `connect` — that is a SKIP
  and it appears in no node table at all.
- **A survey with no `connect` nodes has not scoped.** If everything is load-bearing, the mission
  is too big; say so and cut the matrix instead.

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

Write `learning/<slug>/survey.md`, preserving the `archive:` line `/map-materials` put at the top:
date, the Mission Contract, a short narrative section (history & people, current state &
controversies, trajectory), then **mainlines** (fold-in table + graph), **the matrix**, triage, the
**Scope** section from step 7, gap diagnosis, and a **Roadmap**.

The Roadmap orients; it does not sequence. It shows the whole field, what is in scope, what is
deferred or skipped, and 3–5 checkpoint outcomes phrased as observable `Before → After` changes.
**It carries no critical path** — ordering the `deep` nodes into one dependency thread is
`/curriculum`'s `## Critical Path`, written against the same Scope table. Two orderings written by
two skills is how a syllabus and a roadmap drift apart; there is one, and it lives downstream.

### 10. Seed Structural Memory v0

Initialize or update the **Structural Memory** section in `learning/<slug>/notes.md` per [../../learning/learn/references/notes-format.md](../../learning/learn/references/notes-format.md) — the skeleton the journey will converge on:

- Map: mainline subgraphs; the matrix's key concepts as `target` nodes; your ≥3 labeled cross-links as `hypothesized` edges (dashed).
- Layers: concepts and models listed with **their mode from Scope 7b** and status `target`, no
  gloss — the learner's words come later. Every node's mode matches its Scope row; a node in the
  Layers that is in no Scope row, or vice versa, is a contract violation.
- Frontier → Open tensions: the controversies from step 3, each tied to why it will matter.
- `Iteration: 0`.

If `notes.md` doesn't exist yet, create it with the Structural Memory section. Re-running `/survey` (deepening pass) revises `target`/`hypothesized` structure only; anything `earned` is the loop's and MUST NOT be touched here.

### 11. Append to the cross-topic index

`learning/index.md` is the only cross-topic learner state — the topics table plus the edges between
slugs. Schema: [learning README](../../learning/README.md#the-cross-topic-index).

1. **Topics table** — add or refresh this slug's row (`slug | domain | status | earned nodes |
   last evaluate`). At survey time `status` is `surveyed` and `earned nodes` is `0`.
2. **Cross-topic edges** — for every mainline that touches a concept another slug already holds,
   append **one `hypothesized` edge**, typed from the closed vocabulary (`bridges`,
   `prerequisite-of`, `contrasts-with`, `special-case-of`):

```markdown
| rl:policy-gradient | transformer:decoder-block | prerequisite-of | hypothesized (survey) | — |
```

Both endpoints are `<slug>:<node>` and both must already exist in their slug's Structural Memory —
check before writing; an edge to a node that does not exist is the one thing that makes this file
unreadable. You write `hypothesized` only. Flipping one to `earned` needs a case, and that is
`/reflect`'s.

If `learning/index.md` does not exist, create it with both tables and this slug's row.

### 12. Exit handoffs

- **Soft wiki handoff:** "Want me to feed the Read list into `llm-wiki-ingest` so these sources become wiki pages?" — offer, never force. The Learning OS works without a wiki.
- **Recommend next:** `/curriculum <slug>` to turn the matrix into a course.

## Contract test

**Preconditions:** with `sources/<domain>.md` absent the run stops and routes to `/curate-sources`;
with an archive present but no `materials.md` it stops and routes to `/map-materials`; neither
missing file is worked around by scanning or web search.

**Output:** `survey.md` contains a complete Mission Contract (goal/output, baseline evidence,
relevance, gap, constraints, non-goals, uncertainty); the `archive:` line is preserved; a Roadmap
with whole-field orientation, scope cuts, and 3–5 `Before → After` checkpoints **and no critical
path**; 3–5 mainlines each with its question and a fold-in table; ≥3 labeled cross-mainline links; a
full mainlines × four-stages matrix where every cell is behavioral, every can-apply cell names a
sample, and every mainline has a marked target stage; an argued investment table summing to ~100%
with ≥1 SKIP/stop-early; a gap diagnosis per mainline with current + target + evidence on the shared
ladder; wiki ingest offered, not forced.

**Scope:** every source named anywhere in `survey.md` resolves to a `sources/<domain>.md` `id`, and
every registry row touching the field has a `DEEP`/`SKIM`/`SKIP` disposition with a mission-tied
why; ≥1 argued SKIP; every SKIM names the part to read; a source that is needed and unregistered
appears as a `gap` line routed to `/curate-sources`, never as a citation. Every node has a `mode`,
each with a why, and **≥1 node is `connect`**; the node table and the Structural Memory Layers list
the same nodes with the same modes.

**Memory:** Structural Memory section in `notes.md` exists with only `target` nodes and
`hypothesized` edges, every node carrying its mode, seeded tensions, and `Iteration: 0`; a deepening
pass leaves `earned` structure untouched. `learning/index.md` has this slug's row and every
cross-topic edge it appended is `hypothesized` with both endpoints resolving to existing nodes; no
edge is written as `earned`.

## Handoffs

**In:** a field the user is considering investing in; **required** — `sources/<domain>.md` from
`/curate-sources`, and `<archive>/materials.md` from `/map-materials` when an archive exists;
optional prior `survey.md` / `notes.md` for a deepening pass.

**Out:**
- `survey.md` written → matrix + Scope + gap diagnosis → `/curriculum <slug>`.
- Scope 7a → the DEEP/SKIM sources `/curriculum` may cite and `frame` may select from.
- Scope 7b → the mode partition `/curriculum` turns into K/S lessons (`deep`) and `[C]` lessons
  (`connect`).
- Structural Memory section in `notes.md` v0 seeded, every node moded → skeleton for the loop
  skills to earn against.
- `learning/index.md` topics row + `hypothesized` cross-topic edges → `/reflect` earns them later.
- Unregistered sources needed → `gap` lines → `/curate-sources <domain>`.
- DEEP list → offer `llm-wiki-ingest` (soft, never forced).
- Controversies surfaced → logged in Structural Memory Frontier as `/synthesis-research` candidates — not resolved here.

## Boundaries

- vs `/curriculum`: survey is *strategic* triage (mainlines, target stages, source dispositions, node modes); curriculum is *tactical* sequencing (the critical path, what order, what load budget). Survey decides **what and how deep**; curriculum decides **in what order**. The matrix is deliberately coarser than a syllabus — mainline extraction and stage differentiation, not lesson plans.
- vs `/curate-sources`: that discovers and tiers sources across topics; this dispositions them for
  one mission. Survey never appends a registry row, and never cites a source that has none.
- vs `/map-materials`: that ranks the archive's files once; this reads the map. Survey never scans
  the archive and never writes `materials.md`.
- vs `/evaluate`: survey **sets the bar** (target cells) and makes the initial placement from probes; evaluate **measures achieved mastery** from evidence files. Same ladder, opposite directions — targets are survey's to change, measurements are evaluate's.
- vs `/research`: survey triages a field and *surfaces* controversies; research *resolves* one into judgment. "Should I learn X?" → survey. "Who's right about X?" → research.
