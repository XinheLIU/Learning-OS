# Writing Memory Format

Last updated: 2026-10-01

Paths are relative to the active writing workspace, not the installed skill repository:
`writing-memory/<topic>/0001.md`, `0002.md`, …; one derived `writing-memory/index.md`.
Use at least four digits and increase the numeric maximum by one. Topic slugs are stable kebab-case.
These artifacts are private user data; this skill repository ignores `/writing-memory/`.

## Snapshot

```markdown
---
topic: <slug>
snapshot: 0001
previous: none
---

# <topic>: <short description of this change>

Last updated: YYYY-MM-DD

## Question
<question family this snapshot belongs to>

## Judgment
<current author position or explicit uncertainty; attribute proposals separately>

## Change
<what changed since Previous and why; first snapshot says initial position>

## Grounds

- <observation or finding> — <path/URL and passage; verification or author-report status>

## Relations

| Topic | Relation | Status | Reason | Basis |
| :--- | :--- | :--- | :--- | :--- |
| <existing topic slug> | extends | candidate | <why this connection helps> | <snapshot or other source pointer> |

## Open questions

- <what still cannot be answered, and what would help; or explicitly none>

## Pieces

- <workspace-relative brief/draft path or published URL>
```

`previous` is `none` for the first snapshot, otherwise the previous snapshot's filename in this
folder. Required sections are Question, Judgment, Change, Grounds, Relations, Open questions and
Pieces. Empty relationship tables and explicit `none` for Pieces are valid during early thinking.
Grounds must attribute the judgment, even if it is only an author statement with a dated excerpt.

Relations: `extends | contrasts | depends-on` (延伸、对照、依赖); status: `candidate | confirmed`.
A row expresses *this topic* relative to the target. Targets must be existing topics; prospective
unwritten themes stay under Open questions until they have a grounded first snapshot. Reasons and
basis pointers are mandatory even for candidates. Confirmed means the author accepts the relation,
not that learning mastery has been established.

Use workspace-relative paths for local sources outside the snapshot folder and state that convention
in the index. A source URL should include a passage/section or quoted observation. Do not copy raw
materials or complete draft versions. Future article moves can be recorded in a new snapshot's
Pieces; historical pointers are preserved, with the newer snapshot supplying the current location.

## Derived index

```markdown
# Writing Memory

Last updated: YYYY-MM-DD

Local pointers inside snapshots are relative to this writing workspace. Latest means the highest
numbered complete snapshot, not the newest filesystem timestamp.

## Topics

| Topic | Current judgment | Latest | Pieces |
| :--- | :--- | :--- | :--- |
| <slug> | <concise faithful extract> | [0002](<slug>/0002.md) | <links to associated pieces> |

## Relations

| From | Relation | To | Status | Reason | Snapshot |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <slug> | extends | <other-slug> | candidate | <extract> | [0002](<slug>/0002.md) |
```

Derive rows only from latest valid snapshots; sort topic rows by slug and relation rows by
From/Relation/To. Rebuild links relative to the index location. Do not union all historical
relations: a later snapshot can retract one by leaving it out and explaining the change. If content
is unchanged, preserve the existing index bytes/date. This keeps retries and no-change runs quiet.
