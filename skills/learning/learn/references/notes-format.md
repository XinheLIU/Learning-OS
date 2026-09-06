# notes.md Format

Last updated: 2026-09-06

`learning/<slug>/notes.md` is the single working file for earned knowledge: learning records, the topic's attempt log, canonical terms, structural memory, micro-skill decomposition, the playbook, teaching preferences, and the mastery snapshot. `/learn` owns it; `/evaluate` appends the Mastery Snapshot; `/reflect` edits records minimally and bumps the Iteration counter; `/practice` writes Micro-Skills entries and Structural Memory edges; `/survey` seeds Structural Memory v0. Append; don't restructure.

## Full template

```markdown
# Notes: {Topic}

## Records

### 0001 — {Short title of what was learned or established}  ({date})
{1–3 sentences: what was learned (or what prior knowledge was established),
and why it matters for future sessions.}
**Evidence:** {how the learner demonstrated the understanding}
**Assistance:** none | hint | walkthrough | solution-shown

### 0002 — {title}  ({date})  (superseded by 0005)
…

## Attempt Log

- {date} {lesson-id} {task}: predicted {X} → {right | wrong: Y} → retry {resolved | narrowed: Z | failed} [assistance: {none | hint | walkthrough | solution-shown}]

## Terms

{One or two sentence description of the domain this vocabulary covers.}

- **{Term}** — {tight 1–2 line definition: what it IS, not what it does}
  _Avoid:_ {loose synonyms this workspace doesn't use}

## Operational Memory

Use this section for the syllabus Memory Budget only:

| id | item | class | mode | target fluency | evidence | latency / errors | palace cue |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| {id} | {command / shortcut / pattern / recovery action} | core | recognition / recall / execution | {observable target} | {lesson or case pointer [assistance]} | {attempt history} | {optional learner-authored cue} |

Imagery or palace placement is a retrieval cue, not evidence above `can-recall`. Execution fluency
requires repeated contextual demonstrations.

## Structural Memory

{The topic's structural memory (was framework.md): Map, Layers, Connections,
Frontier, Iteration counter. Full schema: framework-format.md, with the
sections below living here instead of a separate file.}

### Map
{Mermaid graph regenerated from the Layers/Connections tables}

### Layers
- **{concept|model|framework}** · {mainline} · {target | earned | frontier} · {evidence pointer [assistance] | —}

### Connections
| From | To | Type | Status | Earned by |

### Frontier
#### Open tensions
#### People & papers
#### Missing links

### Iteration: {N}          <!-- /reflect bumps by 1 per pass that changed structure -->

## Micro-Skills

{Decomposition per skill area (was drills-*.md). Written by /practice on first use.}

### {skill}: {micro-skill-name}
- Cell: {mainline × stage — omit when no survey exists}
- Failure modes: {how this specifically goes wrong}
- Success criteria: {observable — what "did it right" looks like}
- Difficulty curve: {easy variant → hard variant}

## Playbook

{The learner's repeatable method and defended positions (was playbook.md).
Written by /reflect only, behind the adversarial defense gate.}

### {procedure-name}
{the defended procedure; each position notes the objection it survived}

## Preferences

- {How the user wants to be taught — pacing, formats, opt-outs}

## Mastery Snapshot — {date}          <!-- written by /evaluate only -->
…
```

## Records — ADR-style learning records

Records are the teaching equivalent of architecture decision records: decision-grade insights that steer future sessions. They are how the tutor locates the zone of proximal development.

**Write a record when any of these is true:**

1. **Demonstrated understanding of something non-trivial** — not exposure; evidence the user can use the concept correctly. Sets a new floor for what to teach next.
2. **Disclosed prior knowledge** — "I already know X." Record it (and the *depth* claimed) so future sessions don't re-teach it.
3. **A misconception was corrected** — highest value: corrected misconceptions predict future stumbling blocks in related topics.
4. **The mission shifted** — the user discovered they care about something different. Confirm, record, and send back to `/curriculum`.

**What does not qualify:**

- Material merely covered. Coverage is not learning — wait for evidence.
- Anything already captured as a term. Don't duplicate.
- Session activity logs. Records are not a journal.

**Format rules:**

- Sequential numbering: scan for the highest number, increment. Title + 1–3 sentences is the whole format — the value is *that* it's known and *why* it changes what to teach next, not filled-out sections.
- Optional, only when they genuinely add value: an **Evidence** line (how the user demonstrated it) and an **Implications** line (what this unlocks or rules out).
- A record that documents demonstrated understanding MUST include both **Evidence** and **Assistance**. `Assistance` is exactly one of `none`, `hint`, `walkthrough`, or `solution-shown`, using the most-assisted level from the demonstration. Records of disclosed prior knowledge, mission shifts, or preferences do not require this field unless they also claim demonstrated understanding.
- **Supersede, don't delete.** When understanding deepens past an earlier record, mark the old one `(superseded by 000N)`. How understanding evolved is itself signal.

## Attempt Log — compact retry evidence

Append one line after every `/learn` attempt cycle:

```markdown
- <date> <lesson-id> <task>: predicted <X> → <right | wrong: Y> → retry <resolved | narrowed: Z | failed> [assistance: <none | hint | walkthrough | solution-shown>]
```

Use the maximum assistance received during that cycle. The assistance tag is a closed enum; free text is invalid. `narrowed:` must name the precise remaining error, and `failed` opens another reduced-step cycle rather than closing the segment.

Keep this section compact: never expand a line into a multi-line block.

**Pruning is gated on retention, not on coverage.** A task's log lines MAY be pruned to the single worst-assistance line per task — ordered `none < hint < walkthrough < solution-shown` — only once the matching `retrieval.md` item has reached `streak >= 2`: two consecutive unassisted cold-recall passes. Until then the lines stay, however long the section grows.

A checked lesson box is not the trigger. Checkoff means "taught", and pruning on it discards the per-item attempt history exactly when the scheduler starts needing it — before anything has been retained. A task whose item has never been fired, or has lapsed since, keeps its full log.

If the section becomes genuinely unwieldy, move it to its own file. Never discard rows to shorten it.

## Terms — the canonical language

The Terms section is the workspace's glossary: all lessons, reference docs, and records adhere to it. Building it is itself learning — compressing a concept into a tight definition is evidence the user understands it.

- **Add a term only when the user has earned it.** This is a record of compressed knowledge, not a dictionary read to learn. Wait until they can use the term correctly.
- **Be opinionated.** When several words exist for one concept, pick the best and list the rest under `_Avoid:_`. This is how language compresses.
- **Tight definitions.** 1–2 sentences; what the term IS.
- **Use the terms everywhere.** Once a term is in, prefer it in every lesson, reference doc, and definition of other terms — this is what makes complex material graspable later.
- **Flag ambiguities.** If the wider field uses a term loosely, note the resolution: "here, 'set' always means a working set."
- **Revise in place** as understanding deepens; no stale entries. Promote the mature Terms section into a `reference/glossary.html` when it's big enough to want print-quality form.

## Preferences

Teaching preferences the user has expressed: pacing, lesson style, community opt-outs, formats to avoid. Read before authoring every lesson. One bullet each; remove when withdrawn.
