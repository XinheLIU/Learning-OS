# Elevate Draft

**Purpose:** Transform learning notes to teaching prose while preserving authenticity

**When to use:** After assess-readiness confirms graduation is appropriate. Before add-pedagogy. Converts the learner's artifact (raw notes, debugging traces, false starts) into a first teaching draft that preserves genuine insights while clarifying reasoning for readers.

**Inputs:**
- Learning artifact path (passed readiness check)
- Frame from brief.md (target audience, scope)
- Readiness report (quality gaps to address)

**Outputs:** First teaching draft containing:
- **Preserved authentic elements**: Real examples, debugging journey (edited for clarity), personal insights
- **Clarified reasoning**: Make implicit thinking explicit, connect steps, add "why this works"
- **Removed learning scaffolding**: False starts, repeated attempts, confusion traces that don't serve teaching
- **Added structure**: Topic sentences, transitions, clear progression

**Principle:** Transform the learner's voice into the teacher's voice. Do NOT rewrite from scratch (loses authenticity). Edit the artifact to serve readers while keeping what made the learning genuine.

## Instructions

[TO BE IMPLEMENTED - Phase 4]

This skill takes a learning artifact that achieved independent mastery and elevates it to teaching quality. The goal is transformation, not replacement.

Key transformations:
- **Keep authentic examples and insights**: The learner's real debugging moment, the "aha" realization, the concrete problem they solved — these are gold. Edit for clarity but preserve the authentic journey.
- **Make implicit reasoning explicit**: The learner knows why something works (they achieved can-transfer). The reader doesn't yet. Add the reasoning that's obvious to the learner but not the reader.
- **Remove unproductive false starts**: Learning has dead ends (tried approach A, it failed, tried B, worked). Teaching shows approach B with one sentence acknowledging A exists but doesn't work here.
- **Add structural clarity**: Topic sentences for each section, transitions between concepts, clear progression from simpler to more complex.

The output is still a draft. It has the authentic voice and the clarified reasoning, but not yet full pedagogical scaffolding (that's add-pedagogy's job).

## Example Usage

```bash
/elevate-draft
# Artifact: learning/transformer/attention-mechanism.md
# Readiness: GRADUATE with elevation (missing motivation, implicit matrix semantics)
```

**Before (learning artifact):**
```markdown
# Attention Mechanism

Tried implementing attention. First attempt used fixed weights but that didn't make sense because every position should attend differently based on content.

Then realized: need query and key to compute similarity, then use that to weight values.

```python
# This finally worked
scores = query @ key.T / sqrt(d_k)
weights = softmax(scores)
output = weights @ value
```

Wait why divide by sqrt(d_k)? Tested without it and gradients exploded. Asked about it - turns out prevents softmax saturation.
```

**After (elevated draft):**
```markdown
# Attention Mechanism: Dynamic Weighting by Content

The core insight of attention is that each position should attend to other positions differently based on **what** those positions contain, not their fixed location.

To achieve this, we need three components:
1. **Query**: What this position is looking for
2. **Key**: What each position offers
3. **Value**: The actual information to aggregate

## Computing Attention Weights

We compute similarity between the query and all keys using dot product, then use those similarities as weights for the values:

```python
scores = query @ key.T / sqrt(d_k)  # Similarity scores
weights = softmax(scores)            # Normalize to probabilities
output = weights @ value             # Weighted sum
```

The division by `sqrt(d_k)` is crucial: without it, the dot products grow large as dimension increases, pushing softmax into saturation where gradients vanish. Scaling keeps the variance stable.

[Note: I discovered this by testing without the scaling factor — gradients exploded during backprop. The scaling is not cosmetic; it's necessary for stable training.]
```

**What changed:**
- ✓ Kept authentic debugging insight ("discovered by testing without scaling")
- ✓ Made implicit reasoning explicit ("similarity between query and keys")
- ✓ Removed unproductive false start (fixed weights attempt)
- ✓ Added structural clarity (numbered components, section heading)
- ✓ Clarified matrix semantics ("dot product", "dimension increases")
