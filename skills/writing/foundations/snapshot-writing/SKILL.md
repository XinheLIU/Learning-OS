---
name: snapshot-writing
description: Preserve a substantive change in writing understanding, with evidence, topic relations and open questions. Use for 沉淀, 写作快照, recording a revised judgment, connecting related articles or keeping questions for a later piece. Creates no snapshot when only wording changed.
---

# Snapshot Writing

Last updated: 2026-10-01

Capture what changed in understanding, whenever it changes: framing, reasoning, evidence work or
after a draft. Publication is not a prerequisite. A snapshot is the author's current position with
its uncertainty; it is not a mastery assessment or a frozen copy of an article.

## Workflow

1. Resolve the writing workspace from the active corpus or the user's specified root. Read
   `writing-memory/index.md`, then the relevant topic's latest numbered snapshot and the changed
   brief, draft, research or supplied dialogue. Reuse the existing topic slug when it is the same
   question family; shared keywords alone do not establish a relationship.
2. Compare four things: judgment, grounds, topic relations and open questions. State the substantive
   delta. Rephrasing, changed timestamps and a duplicate invocation produce **no new snapshot**.
   On the first run, a clearly attributed current understanding is sufficient.
3. Separate confirmed author judgments from AI proposals. Quote supplied author wording where
   possible; ask only if the new position would be attributed to the author without their support.
   Candidate topic connections may be stored as `candidate`; each needs a reason and a source pointer.
4. Append the next numbered file using [memory-format.md](references/memory-format.md). Preserve all
   older snapshots byte-for-byte. A correction is a new snapshot with Previous pointing at the old
   one; never rewrite history or silently merge two contrary positions. Include enough of the
   observation to understand it later, with pointers for the supporting details.
5. Rebuild the index from each topic's highest numbered valid snapshot, per the same reference.
   The snapshot is canonical; the index is navigation. If interrupted after appending, the next run
   finds the unchanged latest understanding, creates no duplicate and repairs the index. If a latest
   file is incomplete, report it and retain the last valid snapshot; do not overwrite that file.

## Ownership and limits

- This skill alone writes `writing-memory/`. `frame` reads it before proposing another piece.
- Source quality remains in `sources/`; material use in `materials.md`; learner evidence and
  mastery remain in `learning/`. Reference those files, preserving earned/assistance labels,
  without copying their status or writing back to them.
- A snapshot's grounds can include the author's report of an experience; mark its provenance.
  An external claim is not verified merely because the draft says it.
- Keep current uncertainty visible. Linking a topic does not establish a learner's earned edge.
- Leave the canonical draft unchanged. End with the changed judgment, snapshot link and next open
  question; do not create a reading list or a publishing task that was not requested.

## Completion and contract test

Done when the new understanding is attributable, its change and grounds are explicit, older files
are unchanged, and the index reflects the latest valid snapshots; or when the no-change result is
reported and any stale index repaired. Test duplicate invocation, wording-only change, revised
judgment, a candidate relationship and recovery after snapshot creation but before index refresh.
The second article's `frame` must retrieve the first article's grounds and unresolved question.
