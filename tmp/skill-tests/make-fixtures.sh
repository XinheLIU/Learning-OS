#!/usr/bin/env bash
# Regenerate the synthetic fixtures for tmp/skill-tests/RUNBOOK.md.
# Idempotent: wipes and rebuilds everything except RUNBOOK.md and itself.
#
# Every planted defect is listed in the runbook's "What each fixture plants" table.
# Keep the two in sync — a fixture whose defect nothing asserts is dead weight.

set -euo pipefail
cd "$(dirname "$0")"

# Wipes and rebuilds everything it generates. It does NOT touch anything outside this
# directory — smoke-run output lives at tmp/<topic>/drafts/, deliberately out of reach, because
# an earlier Part-A run lost its draft to this line.
rm -rf materials materials-archive materials-map drafts
mkdir -p materials/images materials/01-Papers materials/11-Code materials/06-Vision
mkdir -p materials-map/images materials-map/01-Papers materials-map/11-Code materials-map/06-Vision
mkdir -p drafts/grill-case/assets drafts/pkg-clean/assets drafts/pkg-broken/assets
mkdir -p drafts/archive-case/assets

# ── tiny valid PNGs (1x1, so `Read`-ing one is cheap and legal) ───────────────
png() { printf '\211PNG\r\n\032\n\000\000\000\rIHDR\000\000\000\001\000\000\000\001\010\006\000\000\000\037\025\304\211\000\000\000\012IDATx\234c\000\001\000\000\005\000\001\r\n\055\262\000\000\000\000IEND\256B\140\202' > "$1"; }

# descriptive names — dispositionable from the filename alone
for n in "Self-Attention QKV.png" "Multi-Head Attention.png" "KV Cache.png" \
         "Positional Encoding.png" "Encoder Block.png"; do png "materials/images/$n"; done
# off-topic — must be cut (they belong to another project entirely)
for n in "Repo Hygiene Roadmap.png" "Sprint Burndown.png"; do png "materials/images/$n"; done
# cryptic — must get inspect-on-demand, never a guess
for n in "Screenshot 2026-03-11 at 14.22.08.png" "diagram-v2-final.png" "IMG_4471.png"; do
  png "materials/images/$n"; done

# ── notes: sectioned, with one off-topic section and one duplicate-ish pair ───
cat > materials/transformer-note.md <<'EOF'
# Transformer 笔记

Source: synthetic fixture · Captured: 2026-09-21 · Medium: course notes

## Tokenization

把文本切成 token，再查表成向量。BPE 是常见做法。

## Positional Encoding

自注意力本身没有顺序概念，所以要把位置信息加进去。这里只记了结论，没记推导。

![位置编码示意](images/Positional%20Encoding.png)

## Self Attention

QKV 三个投影。打分、softmax、加权求和。我一开始把 K 和 V 搞反了 —— 记一下。

## Multi-Head Attention

把 d_model 切成 h 份，各自做注意力，再拼回来。

## KV Cache

解码时把历史 K/V 缓存下来，每步只算新 token。

## 项目管理杂记

这段和 Transformer 无关，是当时顺手记的迭代流程。
EOF

cat > materials/reference.md <<'EOF'
https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html
https://arxiv.org/abs/1706.03762
EOF

# ── bulk folders: one per fate, each big enough to warrant a folder-level row ─
for i in 1 2 3 4; do echo "paper stub $i" > "materials/01-Papers/paper-$i.md"; done
for i in $(seq 1 24); do echo "cell $i" > "materials/11-Code/nb-$i.ipynb"; done
for i in 1 2 3; do echo "vision paper $i" > "materials/06-Vision/vit-$i.md"; done

echo "  materials/: $(find materials -type f | wc -l | tr -d ' ') files"

# ── materials-archive/: a copy for test 4, which WRITES to its materials folder ─
# Separate so test 4 never contaminates test 1's read-only fixture.
cp -R materials materials-archive
# plant an intra-folder reference to a cryptic image: renaming it must either
# update this line in the same batch or drop the rename. No real library the
# trial touches has one of these, so this is the only place it gets tested.
cat >> materials-archive/transformer-note.md <<'EOF'

## 补充图

![旧截图](images/Screenshot%202026-03-11%20at%2014.22.08.png)
EOF
echo "  materials-archive/: $(find materials-archive -type f | wc -l | tr -d ' ') files (+1 inbound ref)"

# ── drafts/grill-case: a chapter brief + a draft with ONE planted teaching gap ─
cat > drafts/grill-case/brief.md <<'EOF'
---
piece: attention
brief-kind: chapter
status: reviewed
target-media: book-chapter
sources: [tmp/skill-tests/materials/]
---

# Brief: 注意力机制

Last updated: 2026-09-21

## 教学目标

**主题（能力句）:** 读者能手推一次 scaled dot-product attention，并说明每一步为什么在那里。

- **Reader:** 会线性代数、没实现过 attention — **已知:** 矩阵乘法 — **未知:** QKV 的分工
- **Register:** technical

## 论点层级（skeleton）

### 一层 1 — 纵向概念拆解

- **二层 1.1** QKV 三个投影各自的角色 → *三层:* `transformer-note.md § Self Attention`
- **二层 1.2** 打分为什么要除以 √d_k → *三层:* `transformer-note.md § Self Attention`
- **二层 1.3** 多头为什么拼接而不是平均 → *三层:* `transformer-note.md § Multi-Head Attention`

**覆盖性检查：** yes

## Code & math

| Item | Kind | Source | Placement | Why it earns the space |
| :--- | :--- | :--- | :--- | :--- |
| scaled dot-product + √d_k | derivation | `transformer-note.md § Self Attention` | inline | the scaling argument |

## Selection map

| Material | Disposition | 支撑节点 | Note |
| :--- | :--- | :--- | :--- |
| `transformer-note.md § Self Attention` | core | 二层 1.1, 1.2 | |
| `transformer-note.md § Multi-Head Attention` | core | 二层 1.3 | |
| `images/Self-Attention QKV.png` | core | 二层 1.1 | |

## Author's markers

> 我一开始把 K 和 V 搞反了 — **锚在** 二层 1.1

- **Vocabulary:** 打分（not 相似度计算）

## Cost paid

不讲 masking、不讲 KV cache，留给下一章。
EOF

# The draft: 1.1 and 1.2 are taught properly; 1.3 is ASSERTED, never explained.
# grill must find 1.3 as a DRAFT gap, and 1.1/1.2 misses as AUTHOR gaps.
# Images are in assets/ (content-local) — grill tests the text, not portability.
png drafts/grill-case/assets/qkv.png
cat > drafts/grill-case/attention.md <<'EOF'
# 注意力机制

Last updated: 2026-09-21

## QKV 三个投影

同一个输入向量乘三个不同的权重矩阵，得到 Q、K、V。分工是这样的：Q 是"我在找什么"，
K 是"我能被什么找到"，V 是"找到我之后拿走什么"。Q 和 K 只用来算打分，真正被加权求和
带到下一层的是 V —— 这也是我一开始搞错的地方，把 K 和 V 当成了一回事。

![QKV 投影：一个输入，三个不同的权重矩阵](./assets/qkv.png)

## 打分为什么要除以 √d_k

Q 和 K 点积之后，数值随维度增长。d_k 越大，点积的方差越大，softmax 的输入就越容易
落到饱和区 —— 梯度趋近于零，训练停滞。除以 $\sqrt{d_k}$ 把方差拉回常数量级：

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

注意除的是 $\sqrt{d_k}$ 而不是 $d_k$：点积是 $d_k$ 个乘积之和，方差正比于 $d_k$，
所以标准差正比于 $\sqrt{d_k}$。要抵消的是标准差。

## 多头注意力

把 d_model 切成 h 份，每个头独立做一次上面的注意力，然后把 h 个头的输出拼接起来，
再过一个输出投影。多头比单头效果好。
EOF

echo "  drafts/grill-case/: brief + draft (planted draft gap at 二层 1.3)"

# ── drafts/pkg-clean: must PASS package-chapter unchanged ──────────────────────
png drafts/pkg-clean/assets/qkv.png
cat > drafts/pkg-clean/attention.md <<'EOF'
---
id: attention
locale: zh-CN
title: 注意力机制
status: draft
created: 2026-09-20
updated: 2026-09-21
---

# 注意力机制

行内公式 $\sqrt{d_k}$，块公式：

$$\text{softmax}(QK^\top/\sqrt{d_k})V$$

![QKV 投影](./assets/qkv.png)

```python
scores = q @ k.transpose(-2, -1) / math.sqrt(d_k)
```

```mermaid
flowchart LR
    Q --> Score --> Softmax --> Weighted
```

见 [多头注意力](content:multi-head-attention)。
EOF

# ── drafts/pkg-broken: one violation per check, so a silent check is visible ────
png drafts/pkg-broken/assets/ok.png
cat > drafts/pkg-broken/attention.md <<'EOF'
---
id: Attention_Bad
locale: zh
status: wip
created: 2026-09-22
updated: 2026-09-20
route: /attention/
---

# 注意力机制

![ok](./assets/ok.png)
![缺图](./assets/missing.png)
![绝对路径](/Users/xhl/nonexistent-pic.png)
![越界](../nonexistent-dir/KV%20Cache.png)

行内 \(x^2\) 和块 \[y\]。

{% mermaid %}
flowchart LR
    A --> B
{% endmermaid %}

```
scores = q @ k.T
```

见 [坏链接](content:Bad_Id)。
EOF

echo "  drafts/pkg-clean/ + pkg-broken/: portability fixtures"

# ── drafts/archive-case: complete case for archive-materials ──────────────────
# A shipped chapter that used some images, left others in the brief but not draft,
# and never used the off-topic ones.
png drafts/archive-case/assets/qkv.png
png drafts/archive-case/assets/kv-cache.png
cat > drafts/archive-case/brief.md <<'EOF'
---
piece: attention
brief-kind: chapter
status: reviewed
target-media: book-chapter
sources: [tmp/skill-tests/materials-archive/]
---

# Brief: 注意力机制

Last updated: 2026-09-21

## Selection map

| Material | Disposition | 支撑节点 | Note |
| :--- | :--- | :--- | :--- |
| `transformer-note.md § Self Attention` | core | 二层 1.1 | |
| `transformer-note.md § Multi-Head Attention` | core | 二层 1.3 | |
| `transformer-note.md § 项目管理杂记` | cut | — | off-topic |
| `images/Self-Attention QKV.png` | core | 二层 1.1 | placed |
| `images/KV Cache.png` | core | 二层 1.7 | placed |
| `images/Positional Encoding.png` | core | 二层 1.2 | planned, not used |
| `images/Encoder Block.png` | support | 二层 1.5 | planned, not used |
| `images/Multi-Head Attention.png` | core | 二层 1.3 | placed |
| `images/Repo Hygiene Roadmap.png` | cut | — | off-topic |
| `images/Sprint Burndown.png` | cut | — | off-topic |
| `images/Screenshot 2026-03-11 at 14.22.08.png` | inspect-on-demand | — | cryptic |
| `images/diagram-v2-final.png` | inspect-on-demand | — | cryptic |
| `images/IMG_4471.png` | inspect-on-demand | — | cryptic |
| `01-Papers/**` | support | 二层 2.5 | |
| `11-Code/**` | cut | — | too large for this chapter |
| `06-Vision/**` | cut | — | different chapter |
| `reference.md` | support | §5 | |
EOF

# The shipped draft: actually used 3 images; the other 2 core ones never made it
cat > drafts/archive-case/attention.md <<'EOF'
---
id: attention
locale: zh-CN
title: 注意力机制
status: draft
created: 2026-09-20
updated: 2026-09-21
---

# 注意力机制

## QKV

![QKV 投影：三个权重矩阵，同一个输入](./assets/qkv.png)

## KV Cache

解码加速的关键。

![KV Cache：把历史键值缓存下来](./assets/kv-cache.png)

## 多头

![多头注意力：h 个头并行，结果拼接](./assets/multi-head.png)
EOF

png drafts/archive-case/assets/multi-head.png   # placed; map it back to Multi-Head Attention.png

echo "  drafts/archive-case/: brief + shipped draft (3 images used, 2 planned-unused, inbound ref to test rename safety)"
# ── materials-map/: the 12-file fixture for /map-materials ───────────────────
# Exactly 12 files. Planted: one byte-identical duplicate pair in 01-Papers/,
# and one off-topic folder (06-Vision/, 3 files) that must collapse to ONE
# peripheral row. Deliberately small — the map's contract is coverage and
# duplicate detection, and both are checkable by counting.

# distinct bytes on purpose: the ONLY byte-identical pair in this fixture must be
# the duplicate paper, so `shasum | uniq -d` is a clean single-hit check.
python3 - <<'PNG'
import zlib, struct
def png(path, rgb):
    raw = b'\x00' + bytes(rgb)
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d))
    open(path, 'wb').write(
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
        + chunk(b'IDAT', zlib.compress(raw))
        + chunk(b'IEND', b''))
png('materials-map/images/Self-Attention QKV.png', (200, 40, 40))
png('materials-map/images/KV Cache.png', (40, 90, 200))
PNG

cat > materials-map/reference.md <<'EOF'
https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html
https://arxiv.org/abs/1706.03762
EOF

cat > materials-map/transformer-note.md <<'EOF'
# Transformer 笔记（fixture）

Source: synthetic fixture · Captured: 2026-09-28 · Medium: course notes

## Self Attention

QKV 三个投影。打分、softmax、加权求和。

## KV Cache

解码时缓存历史 K/V，每步只算新 token。
EOF

# the duplicate pair — byte-identical, two filenames, two folders' worth of confusion
cat > materials-map/01-Papers/attention-is-all-you-need.md <<'EOF'
# Attention Is All You Need (stub)

Vaswani et al., 2017. Scaled dot-product attention, multi-head, positional encoding.
EOF
cp materials-map/01-Papers/attention-is-all-you-need.md \
   materials-map/01-Papers/"09 - Attention Is All You Need.md"

cat > materials-map/01-Papers/bert.md <<'EOF'
# BERT (stub)

Devlin et al., 2019. Bidirectional encoder, masked language modeling.
EOF

for i in 1 2; do
  printf '{"cells":[{"cell_type":"markdown","source":["# DLAI notebook %s — attention from scratch"]}]}\n' "$i" \
    > "materials-map/11-Code/nb-$i.ipynb"
done

# off-topic folder — one peripheral row, never three
for i in 1 2 3; do echo "ViT stub $i — vision branch, another chapter" > "materials-map/06-Vision/vit-$i.md"; done

echo "  materials-map/: $(find materials-map -type f | wc -l | tr -d ' ') files (expect 12; 1 dup pair, 1 off-topic folder)"

echo ""
echo "Fixture summary:"
echo "  Test 1 (frame-chapter): materials/ — $(find materials -type f | wc -l | tr -d ' ') files"
echo "  Test 2 (grill):         drafts/grill-case/ — planted draft gap at 二层 1.3"
echo "  Test 3 (package-chapter):"
echo "    pkg-clean/  — must pass all checks unchanged"
echo "    pkg-broken/ — plants all 7 mechanical violations"
echo "  Test 4 (archive-materials): materials-archive/ + drafts/archive-case/"
echo "    planted: 3 inspect-on-demand rows, 2 planned-unused core images,"
echo "    1 inbound ref to test rename safety"
echo "  Test 5 (map-materials):     materials-map/ — 12 files, 1 dup pair, 1 off-topic folder"




