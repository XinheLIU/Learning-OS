# Components — create-tech-slides

Last updated: 2026-07-18

Copy-paste patterns. All classes exist in `assets/template.html`.

## Slide shell

```html
<section class="slide" data-eyebrow="03 · WHAT" data-accent="teal">
  <header class="s-head">
    <h2>三层架构 = 三个层层递进的<em>问题</em></h2>
    <p class="lead">语义层回答"世界是什么"，行为层回答"我们能做什么"，动态层回答"世界如何演化"。</p>
  </header>
  <div class="s-body cols-2">
    <div class="col"><!-- text / tables --></div>
    <div class="col"><!-- figure --></div>
  </div>
  <footer class="s-foot">来源：《Why create an Ontology?》【官方】</footer>
</section>
```

`data-accent`: `acc` (default) | `teal` | `violet` | `sand` | `red`. Sets `--a` used by
em/callout/diagram-highlight. `data-eyebrow` renders top-left; page number auto.

Body grids: `cols-2` (+ optional `.w7`/`.w5` on children), `cols-3`, `grid-2x2`, `rows`.

### Vertical fill (the `.slide` is a flex column)

`.s-body` is `flex:1; min-height:0` — it fills all remaining canvas below the header.
Use these to distribute content vertically:

- **`.s-body.vcenter`** — center the content block (one big figure).
- **`.s-body.vspread`** — distribute children evenly top-to-bottom.
- **`.grow`** on a child — that child expands to fill remaining space.
- **`.push-b`** on a child — push it to the bottom (verdict callout, footnote).

### Figures in columns: wrap in `.figbox` (hard rule)

A bare `svg.fig` sets its own height from viewBox ratio × column width and WILL overflow
a wide column. Always:

```html
<div class="s-body cols-2 r57">
  <div style="display:flex;flex-direction:column;justify-content:space-between">
    <!-- text / tables / callouts -->
  </div>
  <div class="figbox">
    <svg class="fig" viewBox="0 0 520 460"><!-- … --></svg>
  </div>
</div>
```

The figbox takes the column height from the grid; the SVG letterboxes inside it and can
never push the slide past 1080. `svg.fig.fill` is only for a full-width figure that is
the sole child of `.s-body`.

The `?check=1` audit flags slides where content bottom is above y=880 (see design-system.md).

## Comparison table

```html
<table class="cmp">
  <thead><tr><th>维度</th><th>OWL</th><th>知识图谱</th><th class="hl">Palantir Ontology</th></tr></thead>
  <tbody>
    <tr><td class="k">生命周期</td><td>线性：查询→推理→终止</td><td>线性：检索→补全</td>
        <td class="hl"><strong>循环：执行→写回→学习</strong></td></tr>
  </tbody>
</table>
```

`.k` = dim row-key; `.hl` = accent-tinted column; `.good`/`.bad` tint cells teal/red.
Keep EVERY source row. >8 rows → split slide, not rows.

## Callout / verdict strip

```html
<div class="callout">
  <span class="c-tag">结论</span>
  <p>它把生命周期从直线掰成了圆圈——这是它一切独特性的源头。</p>
</div>
```

Variants: `callout warn` (sand), `callout risk` (red). Use for each section's "所以…结论是" and evidence-grade warnings.

## Evidence tag (inline)

```html
<span class="ev">官方</span> <span class="ev ind">独立</span> <span class="ev doubt">存疑</span>
<span class="ev comp">竞品</span> <span class="ev sap">SAP</span>
```

Every number from the source keeps its tag. Never strip.

## Spec list (bracket rail rows — also used beside iso stacks)

```html
<ul class="spec">
  <li><span class="s-k">OMS</span><span class="s-v">全局 Schema 真相源——类型注册·版本化·验证</span></li>
  <li><span class="s-k">OSS</span><span class="s-v">读取层 / 查询主网关——搜索·过滤·聚合</span></li>
</ul>
```

## Step / timeline strip

```html
<ol class="steps">
  <li><span class="n">①</span><b>定义 Object</b><small>books.csv → 图书；自动荐主键 book_id</small></li>
  <li><span class="n">②</span><b>添加 Property</b><small>书名·价格·库存状态（枚举）</small></li>
</ol>
```

Horizontal, connector line auto-drawn. 3–6 stations.

## Matrix cards

```html
<div class="grid-2x2">
  <div class="card"><h4>语义鸿沟</h4><p>同一概念在 ERP/MES/CRM 表述不一…</p><small>根源：无统一语义层</small></div>
  ...
</div>
```

## SVG flow diagram (mermaid replacement)

```html
<svg class="fig" viewBox="0 0 880 520">
  <defs><marker id="ar" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
    <path d="M0 0L8 4L0 8z" fill="var(--ink3)"/></marker></defs>
  <g class="node"><rect x="40" y="40" width="200" height="64" rx="6"/>
    <text x="140" y="66" class="t">Object Data Funnel</text>
    <text x="140" y="86" class="s">OSv2 索引主干</text></g>
  <path class="edge" d="M240 72 H 340" marker-end="url(#ar)"/>
  <text class="elabel" x="290" y="64">增量索引</text>
  <g class="grp"><rect x="20" y="20" width="420" height="200" rx="8"/>
    <text x="36" y="44" class="glabel">写入路径</text></g>
</svg>
```

CSS classes `.node rect`, `.node .t`, `.node .s`, `.edge`, `.edge.flow` (dashed),
`.elabel`, `.grp rect`, `.glabel` are pre-styled. Datastore: use `<ellipse>` caps.
Highlight a node: add `class="node hi"` (accent stroke + tinted fill).
Add `class="fill"` to the `<svg>` to make it fill the available height of its container.

## Isometric helpers (JS, run at load; see template)

```html
<svg class="fig iso" viewBox="0 0 900 640" data-iso></svg>
<script>
// Slide part-files run BEFORE the engine script — always wrap ISO calls in a
// load listener so window.ISO exists:
addEventListener('load', () => ISO.stack('[data-iso]', {
  cx: 300, topY: 70, w: 240, gap: 150,
  layers: [
    {label:'FOUNDRY DECISION ORCHESTRATION', kind:'options'},
    {label:'FOUNDRY DYNAMIC ONTOLOGY',      kind:'graph', accent:true},
    {label:'YOUR DATA PLATFORM',            kind:'grid',  items:['AWS','AZURE','SNOWFLAKE']},
    {label:'YOUR OPERATIONAL SYSTEMS',      kind:'scatter', items:['S3','SAP','KAFKA','ORACLE']},
  ],
  rail: {x: 620, w: 260}   // bracket labels drawn on the right
}));
</script>
```

`kind`: `plain` | `grid` (cube matrix on the plane) | `graph` (nodes+dashed edges) |
`options` (mini flow boxes) | `scatter` (loose cubes/cylinders below, no plane).
`ISO.cube(svg,x,y,s,{accent})` and `ISO.plane(svg,cx,cy,w,{label})` for custom art.
Layers are rendered bottom-up automatically; arrows between layers via
`ISO.arrow(svg, x1,y1,x2,y2,{dashed})`.

## Loop diagram (决策飞轮 / lifecycle circle)

```html
<svg class="fig" viewBox="0 0 520 420" data-loop
     data-nodes="用数据做决策|捕获决策·写回系统|评估决策影响"
     data-center="决策数据 / 决策谱系"></svg>
```

Renders 3–5 nodes on a circle with arrowed arcs + optional center datastore.

## Section cover

```html
<section class="slide cover-section" data-accent="teal">
  <div class="ghost">02</div>
  <h2>What · 它到底是什么</h2>
  <p class="thesis">不是"更好的 OWL"，而是本体演化到操作阶段长出的新物种。</p>
  <ul class="mini-agenda"><li>命名之争</li><li>四十年四阶段</li><li>三种世界观对照</li></ul>
</section>
```

## Print & nav (engine, do not re-implement)

- ←/→/space/Home/End navigate; `#12` deep-links; `O` overview grid; `P` opens print view (all slides stacked, `@media print` one per page).
- `?check=1` runs the overflow audit: every `.slide` is measured; result to `document.title` (`CHECK-OK` / `CHECK-FAIL n`) and `<pre id="check-report">` (JSON: slide index, scrollW/H, offending element hint) plus an `OVERFLOW-REPORT:` line for grep.
