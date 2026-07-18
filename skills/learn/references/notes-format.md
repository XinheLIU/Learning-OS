# notes.md Format

`learning/<slug>/notes.md` is the single working file for earned knowledge: learning records, the topic's canonical terms, and teaching preferences. `/learn` owns it; `/evaluate` appends the Mastery Snapshot; `/reflect` edits records minimally. Append; don't restructure.

## Full template

```markdown
# Notes: {Topic}

## Records

### 0001 — {Short title of what was learned or established}  ({date})
{1–3 sentences: what was learned (or what prior knowledge was established),
and why it matters for future sessions.}

### 0002 — {title}  ({date})  (superseded by 0005)
…

## Terms

{One or two sentence description of the domain this vocabulary covers.}

- **{Term}** — {tight 1–2 line definition: what it IS, not what it does}
  _Avoid:_ {loose synonyms this workspace doesn't use}

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
- **Supersede, don't delete.** When understanding deepens past an earlier record, mark the old one `(superseded by 000N)`. How understanding evolved is itself signal.

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
