# Brief Format

Last updated: 2026-09-01

The pipeline's central artifact. Written by `frame-piece`, consumed by `write-content`, checked against by `review-draft`, cited by `edit-targeted`.

**Path:** `drafts/<piece-slug>/brief.md` (within the corpus folder — e.g. `tmp/learning-how-to-learn/drafts/overlearning-self-deception/brief.md`).

## Template

```markdown
---
piece: <slug>
status: framed | drafting | reviewed
target-media: <optional — blog | wechat | xhs | book-chapter; adapters read this later>
sources: [<paths to the materials this rests on>]
---

# Brief: <working title>

Last updated: YYYY-MM-DD

## 议题

<The live question, stated as a question. Someone must be able to answer it both ways.>

**为什么是现在：** <the change outside the material that makes this contestable now>

## 正方 / 反方

- **正方（要反驳的一方）:** <the opposing position at full strength, and who holds it — a named person, book, or community>
- **反方（本文的立场）:** <one contestable sentence, in the author's own words after the final round>

## Angle

<反方 restated as the piece's thesis — the sentence the draft has to earn.>

## 论点层级

> 主题在上，证据在下。每一条 `二层` 必须有 `三层` 兜底；没有的就是 `gap`。

### 论点 1 — <one contestable sentence>

- **二层 1.1** <mechanism> → *三层:* `<source § section>` / *作者事例* / `gap`
- **二层 1.2** <mechanism> → *三层:* `<source § section>`

### 论点 2 — <one contestable sentence>

- **二层 2.1** <mechanism> → *三层:* `<source § section>`

### 论点 3 — <正方 的最强追问，正面回答>

- **二层 3.1** <the criterion that answers it> → *三层:* `gap` — <what must be decided before drafting>

**充分性检查：** 读者接受论点 1–N，主题是否成立？<yes / what's missing>

## Reader

- **Who:** <>
- **Currently believes:** <>
- **Should change:** <what they do differently after reading>
- **Register:** technical | business

## Selection map

| Source section | Disposition | 支撑节点 | Note |
| :--- | :--- | :--- | :--- |
| `02-memory-system.md` § 工作记忆 | core | 二层 2.1 | arms 反方 — bandwidth ceiling |
| `03-brain-biology.md` § 睡眠 | core | 二层 2.2 | arms 反方 — the constraint AI can't compress |
| `04-chunking.md` § 自上而下 | core | 二层 1.1 | arms 正方 — the honest concession |
| `06-practice-strategy.md` § 交错练习 | support | 二层 1.2 | the one worked example |
| `01-thinking-modes.md` (whole) | cut | — | true, off-mainline |
| — | gap | 二层 3.1 | 正方's strongest question; not in materials |

## Author's markers

> <verbatim quote from the dialogue — the disagreement> — **锚在** 二层 X.Y

> <verbatim quote — the past mistake> — **锚在** 二层 X.Y

- **Vocabulary:** <words the author actually uses for this; write-content must not "improve" them>

## Cost paid

<What this angle explicitly declines to cover. Scope creep during drafting is a contract
violation against this line, not a judgment call.>
```

## Field rules

| Field | Rule |
| :--- | :--- |
| **议题** | A question, not a topic. If it can only be answered one way, it is a fact and there is no piece. |
| **为什么是现在** | Names a change *outside* the material. "The source is inconsistent" is not an occasion — it is a book review. |
| **正方** | Stated so its believers would sign it, and attributed to someone who actually holds it. An unnamed or weakened opponent is a strawman. |
| **反方 / Angle** | One sentence, contestable. If a reasonable practitioner couldn't disagree with it, it isn't an angle. |
| **论点层级** | 2–4 pillars, each contestable. Sufficiency stated explicitly. Every 二层 line carries a 三层 or is labelled `gap`. 正方's strongest objection is a pillar, never a buried gap. |
| **Selection map** | Covers **every** section of every source, each `core`/`support` row keyed to a ladder node and to the side it arms. A section supporting no node is decoration — demote to `cut`. Nothing under `cut` means the angle is still the corpus's own thesis. |
| **Author's markers** | Verbatim, and **anchored to a ladder node**. An unanchored quote gets used as decoration; anchored, its absence from that spot in the draft is a reviewable defect. |
| **Cost paid** | Non-empty. An angle that throws nothing away isn't a selection. |
| **`gap`** | Each entry is a research question — route to `/synthesis-research` or another capture round before drafting the section that needs it. |

## How downstream skills read it

- **`write-content`** takes the **论点层级 as the outline** — pillars become sections, 二层 become the claims inside them, 三层 supplies the evidence. It does not re-derive structure from the corpus. It drafts from `core` + `support` only; `cut` is out of bounds. It mines *Author's markers* for the opening tension and for examples, preferring them over anything in the sources.
- **`review-draft`** runs axis 1 against 议题, 正方/反方, Angle, Selection map, and Cost paid — including the check that 正方 is a real outside position, not the source itself.
- **`edit-targeted`** cites brief lines when justifying a diff ("the brief's cost line rules this section out").
- **`publish-adapt` family** (later) reads `target-media`. The brief and the canonical draft stay medium-neutral; adapters derive, never edit back.
