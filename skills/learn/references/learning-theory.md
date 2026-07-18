# Learning Theory — The Five-Theory Engine

The single home for the Learning OS's theoretical foundations. Skills embed these as operationalized directives; this file holds the *why* behind those directives. Read it when a directive seems arbitrary or when adapting a skill.

Five theories answer orthogonal questions of one learning engine:

| Theory | Answers | Component(s) |
| :--- | :--- | :--- |
| Four Layers of Learning | What should be learned? | Knowledge Distillation, Knowledge Graph |
| Cognitive Load | How should knowledge be presented? | Course Designer, AI Tutor |
| ICAP | How should the learner engage? | AI Tutor, Continuous Feedback |
| Deliberate Practice | How should skill improve? | Practice Coach, Learning Evaluator |
| Synthesis Research | How is new knowledge created? | Research Companion |

---

## 1. Four Layers of Learning — what should be learned

Knowledge is not flat. It stratifies into four layers, each built from the one below:

1. **Representation** — names, terms, notation. Knowing what something is called. Cheap to acquire, near-zero transfer value on its own. Lives in `notes.md` under `## Terms`.
2. **Schema** — a small, reusable structure: a procedure, a pattern, a canonical example. The unit of fluency. Lives in `notes.md` records.
3. **Mental model** — a causal account: what drives what, under which conditions, and where it breaks. The unit of judgment. Lives in `notes.md` records.
4. **Framework** — an organization of models: when to reach for which, how they trade off. The unit of expertise. Lives in `syllabus.md`, `playbook.md`, `research-*.md`.

**Relation to Knowledge/Skill/Wisdom (the user-facing depth model):** K/S/W types *what kind of capability a lesson builds* — understanding from sources (K), durable retrieval under difficulty (S), judgment tested in the real world (W). The four layers grade *how deep a piece of knowledge sits*. They are orthogonal: a K-lesson may produce representations and schemas; an S-lesson drives schemas toward models; W and `/research` produce frameworks. The syllabus and lessons speak K/S/W; the layers stay internal — a lens for `/evaluate`'s depth gauge and for these design rules, not per-lesson bookkeeping.

**Operational consequences:**
- The depth distribution is a gauge — notes that are mostly terms are vocabulary, not understanding (`/evaluate` reports this).
- Layers are climbed, not skipped: no model without its schemas, no framework without its models. `/learn` never introduces a causal model before its component schemas are fluent.
- **A model the learner didn't construct isn't theirs.** Distillation into the learner's own layers happens through tutoring dialogue, not batch extraction — "don't write a model the user didn't earn." (External, source-faithful distillation belongs to the llm-wiki suite; that's the wiki/learning wall.)
- Direct answers are permitted for representations only — a term's name may be handed over; a schema or model must be constructed.

## 2. Cognitive Load Theory — how knowledge should be presented

Working memory is small; long-term memory (schemas) is what makes hard things feel easy. Load comes in three kinds: **intrinsic** (the material's inherent complexity — managed by sequencing), **extraneous** (presentation waste — eliminated), **germane** (schema-building effort — protected).

**Operational consequences:**
- **Source-level load management:** `/survey`'s mainline kills extraneous load before it's ever read — SKIP rows are load that never enters the pipeline.
- **Chunking:** one new concept per exchange (`/learn`) and per Stage-2 lesson (`/curriculum`). Two new concepts at once splits working memory and neither becomes a schema.
- **Parts before wholes:** automate component schemas before integrating them (curriculum Stages 1–3); let the learner stand firm on one step before showing the next.
- **Worked examples first for novices:** a novice given an open problem burns working memory on search instead of schema-building. Direct instruction, closed questions, small steps.
- **Expertise reversal:** the same scaffolding that helps a novice *hurts* a practitioner — for them, drop the support: transfer tasks, open problems, boundary probing. This is why the survey diagnosis is load-bearing: scaffolding level is set per subtopic, from evidence.
- **No extraneous load in dialogue:** no tangents, no stacked analogies, no decorative theory.

## 3. ICAP — how the learner should engage

Engagement modes form a hierarchy by learning yield: **Passive** (receiving) < **Active** (manipulating — highlighting, copying, running) < **Constructive** (generating something not in the material — self-explanation, own examples, predictions) < **Interactive** (constructing under challenge — defending, revising against an attacking partner).

**Operational consequences:**
- **Never end a segment at P/A.** Every chunk in `/learn` closes with learner construction: a self-explanation or the learner's *own* example — the tutor's example doesn't count as the learner's construction.
- **Escalate to I periodically:** the tutor attacks the learner's construction; the learner defends or revises. `/reflect`'s adversarial defense gate is the same move applied to playbook positions.
- **The ceiling rises with schemas:** novice P/A → C; intermediate A → C; advanced C → I. Never skip schemas to force interactivity — I-mode on a schema-less learner is just P-mode with anxiety.
- **Tutor, not a homework-answer machine:** handing over an answer converts a C-opportunity into P. Decompose and hint instead.
- Every syllabus lesson carries an explicit ICAP target so tutor and learner know the intended engagement mode before starting.

## 4. Deliberate Practice — how skill should improve

Experience alone plateaus. Improvement requires: decomposition into trainable micro-skills, one high-resolution goal at a time, work at the edge of ability (the learning zone), immediate feedback, and error tracking over time.

**Operational consequences:**
- **Decompose first:** the first `/practice` session on a skill produces `drills-<skill>.md` — micro-skills with failure modes, success criteria, difficulty curves. Sessions then target one micro-skill.
- **Micro-goals, not vibes:** "identify the bottleneck within 3 questions", not "get better at profiling". One per session.
- **Calibrate the zone, out loud:** cruising → harder variant; panic → shrink scope. The coach announces the adjustment so calibration is visible and learnable.
- **Immediate feedback:** errors corrected the moment they occur, named precisely.
- **Errors are the curriculum:** case files record errors; `/reflect` compresses recurring errors into the next micro-goals. The loop closes through files, not memory.
- **Evidence before claims:** mastery is what the case files show (`/evaluate`'s rubric), never a self-report or a percentage.

## 5. Synthesis Research — how new knowledge is created

Three levels of working with sources, by ambition:

1. **Positioning** (hours): locate and restate what reliable sources say about a question. Knowledge located.
2. **Structural** (weeks+): internalize a field's live structure — organize by *issue*, not author; per issue know the schools, their methods, their blind spots, who holds discourse power. Understanding is proven by the **steelman test**: summarize the school you disagree with in terms it would endorse. Knowledge organized.
3. **Generative** (advanced): produce judgment no single source contains — overlay heterogeneous materials and read the answer *between* them (the John Snow move: the map plus the death records, neither sufficient alone). Every generative claim needs ≥2 independent sources whose *combination* supports it, and must answer "so what?". Knowledge created.

**Operational consequences:**
- **`/research` owns only the top of this ladder.** Positioning — locating knowledge — is served by a direct answer, a wiki query, or `/survey`; it never warrants a research report. The skill's entry gate is a **live tension** (disagreeing sources, a source vs an earned model, a contested wiki page), and every report runs the full arc: structural mapping of the tension (steelman + crux) as the floor, generative synthesis (connections + judgment) as the deliverable.
- **The crux must be named:** a mapped disagreement bottoms out in a different assumption, different evidence, or different values — a dispute without a located crux is a summary, not research.
- Distinguish expert-vs-expert disagreements (fine-grained, conditional — usually fine) from expert-vs-public gaps (usually where the real knowledge gap, and the opportunity, is).
- **Writing is where thinking completes** — the `/research` deliverable is always a written report, not a chat transcript.
- The user's judgment section is theirs (HITL) — formed in dialogue, never ghost-written — and must answer "so what?" with a changed decision and a falsifier.

---

## How the theories interlock

Survey (CLT at the source level) decides what enters. Curriculum (CLT + ICAP) sequences it. The tutor (CLT pacing, ICAP escalation) turns sources into the learner's own four-layer structures. Practice and evaluation (deliberate practice) turn structures into skill, with evidence. Reflection (ICAP-I on the learner's own positions) redirects the loop. Research (synthesis) is where the loop starts producing knowledge instead of consuming it.
