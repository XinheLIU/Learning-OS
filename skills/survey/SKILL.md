---
name: survey
description: Investment gate before learning a field. Use when the user wants to explore a new domain, decide what's worth learning, allocate learning time, or says "/survey <field>". Outputs a learning mainline (DEEP/SKIM/SKIP triage), curated sources (read / don't read), and a prior-knowledge diagnosis — the inputs /curriculum and /learn build on.
---

# Survey — Investment Gate

Runs before any information enters the learning pipeline. The deliverable is an **investment decision, not a textbook**: where does the user's time go, and which sources deserve ingestion. This is cognitive-load management applied at the source-selection level — extraneous load is eliminated before it is ever consumed.

## Rules

- **~30-minute cap.** A survey is a map and a budget, not a dissertation.
- **The triage MUST be argued.** Every mainline row has a why. A mainline that cuts nothing is a reading list, not a gate — you MUST name at least one SKIP.
- **Two entry paths, one output.** User has context → organize and fill gaps. User knows little → full web research.
- **You MUST NOT build models or teach here.** That is `/learn`'s job. Map the terrain, allocate the time, hand off.
- **Never write to `wiki/`.** The wiki is owned by the llm-wiki suite; the handoff is an offer, not an action.

## Flow

### 1. Auto-init

If `topics/<slug>/` doesn't exist, create it with a `memory/` subdirectory and a minimal `README.md` (slug, started date). Don't ask permission.

### 2. Determine entry path

Ask: "How much do you already know about <field>? Any notes, projects, or reading you want me to build on?"

- **Path A — user has context:** organize what they have, research only the gaps.
- **Path B — user knows little:** full web research, searches in parallel where possible.

### 3. Research the landscape

Cover, in either path:
- **History & key people** — who built the field, what they contributed, what problems they were solving. Narrative, not timeline.
- **Current state** — SOTA, key people/groups now, open problems.
- **Controversies** — what practitioners argue about, schools of thought. (These are `/research` candidates — note them.)
- **Trajectory** — what changed in the last ~5 years, where money and attention are going.

If sources conflict, note the conflict — don't pick a winner silently.

### 4. Triage into the learning mainline

Classify every major subtopic by investment level. This is the core deliverable.

```markdown
## Learning Mainline
| Subtopic | Investment | Why |
| :--- | :--- | :--- |
| <subtopic> | DEEP — 60% | foundational; everything else composes from it |
| <subtopic> | SKIM — 10% | need vocabulary only; low transfer value |
| <subtopic> | SKIP | overhyped relative to impact / not on the critical path |
```

Constraints:
- Percentages on DEEP/SKIM rows MUST roughly sum to 100.
- At least one SKIP row, argued.
- The why-column is mandatory on every row.

### 5. Curate sources

Rank what to read — and say what each is *for* — and name what to skip:

```markdown
## Sources
### Read (ranked, with what each is FOR)
- <source> — best single explanation of <X>; read for the mental model, skip the appendix
### Don't read (with why)
- <source> — popular but derivative of <other>
- <source> — outdated since <development>
```

### 6. Diagnose prior knowledge

Per DEEP/SKIM subtopic, assess the user's level **with evidence** (from Path A conversation, or 2–3 quick probe questions):

```markdown
## Prior-Knowledge Diagnosis
| Subtopic | Level | Evidence |
| :--- | :--- | :--- |
| <subtopic> | novice | couldn't define <core term> |
| <subtopic> | practitioner | has shipped <X>; shaky on <Y> |
```

Levels: `novice` / `practitioner` / `expert`. Downstream, `/curriculum` uses this to set stage depth and `/learn` uses it to set scaffolding — a wrong level here mis-tutors every later session.

### 7. Write survey.md

Write `topics/<slug>/memory/survey.md`: date + sources consulted, a short narrative section (history & people, current state & controversies, trajectory), then the three tables above, then a rough domain map (Mermaid — rough is fine).

### 8. Exit handoffs

- **Soft wiki handoff:** "Want me to feed the Read list into `llm-wiki-ingest` so these sources become wiki pages?" — offer, never force. The Learning OS works without a wiki.
- **Recommend next:** `/curriculum <slug>` to turn the mainline into a syllabus.

Update `topics/<slug>/README.md` (surveyed date, last session).

## Contract test

`survey.md` contains: an argued DEEP/SKIM/SKIP table with ≥1 SKIP; Read/Don't-read lists with reasons; a diagnosis table with evidence; wiki ingest offered, not forced.

## Boundaries

- vs `/curriculum`: survey is *strategic* triage (what gets time, which sources); curriculum is *tactical* sequencing (what order, what load budget). Survey decides **what**; curriculum decides **how**.
- vs `/research`: survey triages a field and *surfaces* controversies; research *resolves* one into judgment. "Should I learn X?" → survey. "Who's right about X?" → research.
