# Chapter Brief

Last updated: 2026-10-01

Use [brief-format.md](brief-format.md) with `brief-kind: chapter`, no `intent`, and a `教学目标`
section stating one capability and its prerequisites. `target-media: book-chapter` and `book:` are
optional known destination metadata; they do not grant permission to publish.

## Ownership

- `frame`: reader, question, gain, current answer, scope and 教学目标.
- `develop-argument`: the teaching order and logic nodes; confirmed earned markers anchored to IDs.
- `develop-examples`: evidence, full material selection and Code & math.

## Teaching structure

Choose sections because they serve the capability. This menu is useful for technical concept
chapters, not a five-section requirement:

| Possible section | Reason to include |
| :--- | :--- |
| Concept decomposition | explain each component using only prerequisites already introduced |
| Development history | show what limitation motivated each change |
| Code and mathematics | enable the reader to compute or implement the promised operation |
| Recent developments | describe a concrete change against the established model |
| Connections and next questions | locate this capability and its limits |

An opinion inside a chapter does not force splitting it into two pieces. Split only when there are
two independent outcomes. Where learner memory exists, `connect` nodes provide transitions rather
than teaching sections; preserve the source/assistance of earned markers. Without a learning run,
use the author's supplied experience and external evidence without claiming earned mastery.

## Code & math

Add this section at the examples stage. `none — <reason>` is valid if the capability requires
neither code nor mathematics; otherwise account for each considered item:

```markdown
## Code & math

| Item | Nodes | Kind | Source | Placement | Why |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Scaled dot product | n3 | derivation | <source and section> | inline | explains the scale factor |
| Multi-head split | n4 | code | <source and section> | assets/code/mha.py | a runnable excerpt too long for prose |
| Training notebook | — | code | <source path> | cut | outside the capability |
```

Keep source and placement together. Default to inline minimal examples; consider a local asset for
blocks longer than roughly 30 lines. Use `$…$`/`$$…$$` for math. Select a runnable excerpt rather than
shipping an entire notebook. Reuse known author choices, asking only when a tradeoff is unresolved.

## Downstream checks

`write-content` follows the agreed teaching order. `review-draft` checks capability, prerequisites,
explanations and evidence, without opponent or novelty-to-the-field requirements. `grill` quizzes
the taught nodes after a ship review, when requested or part of the authorized chapter workflow.
`package-chapter` checks the final draft and copied assets, not the brief's archival source pointers.
`archive-materials` records what actually appeared in the delivered chapter. A chapter itself never
automatically establishes Independent mastery; `/evaluate` retains its evidence and assistance gate.
