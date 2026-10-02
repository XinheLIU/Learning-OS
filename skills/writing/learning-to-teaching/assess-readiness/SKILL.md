# Assess Readiness

**Purpose:** Check if learning artifact qualifies for graduation to teaching material

**When to use:** After completing the learning loop (learn → practice → evaluate) and reaching tier ≥ can-transfer. Before elevating learning notes to book chapter. Ensures only high-quality, independently-achieved learning artifacts become teaching material.

**Inputs:**
- Path to learning artifact (notes, practice code, explanations)
- Mastery evidence from `/evaluate` (tier, assistance level, evidence)
- Target brief (if chapter is already framed)

**Outputs:** Readiness report containing:
- **Independence level**: none / hint / coached (from mastery snapshot)
- **Quality gaps for teaching use**: Missing context, implicit reasoning, false starts, debugging traces
- **Missing pedagogy elements**: Opening task, practice opportunities, common misconceptions
- **Recommendation**: graduate / needs-rework / stay-in-learning

**Gate:** Only artifacts at `assistance: none` or `assistance: hint` with tier ≥ can-transfer should graduate. The four-condition Independent gate (packaged chapter + assistance ≤ hint + brief markers to earned nodes + grill passed) is the gold standard.

## Instructions

[TO BE IMPLEMENTED - Phase 4]

This skill checks whether a learning artifact meets the bar for becoming teaching material. Not every learning artifact should graduate - only those where the learner achieved independent mastery with authentic understanding.

Key checks:
- **Independence:** Can the learner reproduce this without assistance? (Mastery tier and assistance level from `/evaluate`)
- **Completeness:** Does the artifact cover the concept end-to-end, or only fragments?
- **Quality:** Is the explanation clear, or does it contain debugging traces, false starts, and confusion?
- **Authenticity:** Does it show genuine understanding, or is it copy-paste from source material?

The assessment prevents premature graduation. Learning artifacts with `assistance: solution-shown` or tier < can-transfer should stay in the learning loop - they're evidence of exposure, not mastery.

## Example Usage

```bash
/assess-readiness
# Artifact: learning/transformer/attention-mechanism.md
# Mastery snapshot: tier=can-transfer, assistance=hint
```

Expected output:
```markdown
## Readiness Report: attention-mechanism.md

**Independence level:** hint (needed clarification on scaled dot-product, completed rest independently)

**Quality for teaching use:**
✓ Complete explanation of query-key-value mechanism
✓ Working implementation with authentic debugging journey
✗ Missing motivation (why attention vs. fixed weights?)
✗ Implicit assumption that reader knows matrix multiplication semantics

**Missing pedagogy:**
✗ No opening task or concrete scenario
✗ No common misconceptions addressed (e.g., "attention = looking at all positions equally")
✗ No practice opportunities between concept and implementation

**Recommendation:** GRADUATE with elevation

**Reasoning:**
- Learner achieved can-transfer independently (wrote attention from scratch after one hint)
- Core explanation is solid and authentic
- Gaps are pedagogical (missing scaffolding for reader), not understanding gaps
- Elevation phase can add motivation, practice, and misconceptions

**Next step:** /elevate-draft with focus on adding opening scenario and clarifying matrix semantics
```
