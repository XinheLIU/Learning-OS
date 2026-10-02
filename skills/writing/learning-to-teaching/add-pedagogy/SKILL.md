# Add Pedagogy

Last updated: 2026-10-02

**Purpose:** Add scaffolding and teaching tools to transform elevated learning draft into pedagogically complete chapter

**When to use:** After elevate-draft produces first teaching draft. Before write-content produces final prose. Adds the teaching infrastructure that helps readers learn effectively, not just read about a concept.

**Inputs:**
- Elevated draft (learning artifact transformed to teaching prose)
- Frame from brief.md (audience, target capability, completion evidence)
- Teaching sequence (if from explanatory track)

**Outputs:** Pedagogically complete draft containing:
- **Opening task or motivating question**: Concrete problem that makes the concept immediately relevant
- **Check-yourself moments**: Pause points where reader predicts, tests understanding, or compares approaches
- **Common misconceptions addressed**: Where learners typically go wrong, with correction
- **Practice opportunities**: Exercises tied to specific capabilities from the outcome
- **Connection to prior/next chapters**: Bridge from prerequisite concepts, preview of what comes next

**Principle:** From learning evidence to teaching tool. The learner proved they achieved mastery; now add the scaffolding that helps someone else reach the same point.

## Instructions

[TO BE IMPLEMENTED - Phase 4]

This skill adds the pedagogical infrastructure that makes a chapter teachable. The elevated draft has authentic content and clear reasoning, but teaching requires more: it needs to anticipate where readers will struggle, provide practice at the right moments, and connect concepts to what the reader already knows.

Key additions:
- **Opening task**: Start with a concrete problem or question, not an abstract definition. "How does a model decide which words to pay attention to?" beats "Attention is a mechanism for..."
- **Check-yourself moments**: Before revealing the answer or technique, let the reader pause and think. "What would happen if we used fixed weights instead of learned weights? Try to predict." This active engagement deepens understanding.
- **Common misconceptions**: Address the typical wrong turns. "You might think scaling is optional—I did too. Here's why it's necessary." Naming the misconception prevents it.
- **Practice opportunities**: Don't batch all exercises at the end. Place practice immediately after introducing a capability. Teach query-key-value → practice computing attention scores → teach multiple heads → practice multi-head attention.
- **Connections**: Link to prerequisite concepts ("Remember from Chapter 3 when we covered softmax?") and preview what's next ("In the next chapter we'll see how attention enables transformers to parallelize").

The goal is a chapter that not only explains but actively teaches—where the reader works through the concept, catches their own misconceptions, and practices the capability before moving forward.

## Example Usage

```bash
/add-pedagogy
# Draft: elevated-transformer-attention.md
# Audience: ML practitioners who understand feedforward networks but not attention
# Outcome: Implement attention mechanism from scratch
```

**Before (elevated draft without pedagogy):**
```markdown
# Attention Mechanism: Dynamic Weighting by Content

The core insight of attention is that each position should attend to other positions differently based on what those positions contain, not their fixed location.

To achieve this, we need three components:
1. Query: What this position is looking for
2. Key: What each position offers
3. Value: The actual information to aggregate

```python
scores = query @ key.T / sqrt(d_k)
weights = softmax(scores)
output = weights @ value
```
```

**After (with pedagogy):**
```markdown
# Attention Mechanism: Dynamic Weighting by Content

## Opening Task
You're building a translation model. The word "bank" appears in your input. Should it mean "financial institution" or "river edge"? The answer depends on **other words in the sentence**—"money" vs. "river". How can the model use surrounding context to decide?

[Pause: Take 30 seconds to think about how you'd design this. What does the model need to compare?]

## The Core Insight
Attention solves this by letting each word look at every other word and decide which ones are relevant. Unlike fixed positional encodings, attention weights are **computed dynamically** based on content similarity.

## Three Components
To achieve this, we need:
1. **Query**: What this position is looking for ("show me words about finance")
2. **Key**: What each position offers ("I'm the word 'money'")
3. **Value**: The actual information to aggregate (the embedding of "money")

### Check Yourself
Before looking at the code, predict: How would you measure similarity between query and key? What mathematical operation compares two vectors?

<details>
<summary>Reveal approach</summary>
Dot product: high when vectors point in similar directions, low when orthogonal.
</details>

## Computing Attention Weights

```python
scores = query @ key.T / sqrt(d_k)  # Similarity scores
weights = softmax(scores)            # Normalize to probabilities
output = weights @ value             # Weighted sum
```

### Common Misconception
**"The division by sqrt(d_k) is just for numerical stability, right?"**

Not quite. Without scaling, as dimension `d_k` increases, the variance of dot products grows. This pushes softmax into saturation where gradients vanish. The scaling isn't cosmetic—it's necessary for stable training.

[I discovered this by removing the scaling factor during training. Gradients exploded and the model failed to converge. Try it yourself if you're curious—the failure is immediate and instructive.]

## Practice: Implement Single-Head Attention
Before moving to multi-head attention, implement this single-head version:

**Task**: Write a function `attention(Q, K, V)` that returns the weighted output.
- Input shapes: Q, K, V are all `(seq_len, d_k)`
- Output shape: `(seq_len, d_k)`
- Don't forget the scaling factor

<details>
<summary>Solution</summary>

```python
def attention(Q, K, V):
    d_k = Q.shape[-1]
    scores = Q @ K.T / math.sqrt(d_k)
    weights = softmax(scores, dim=-1)
    return weights @ V
```
</details>

**Test your implementation**: With `d_k=64`, random inputs, does softmax sum to 1.0 across each row?

## Connection to Next Chapter
This single-head attention looks at one type of relationship. In Chapter 7, we'll extend this to **multi-head attention**, where the model learns multiple parallel attention patterns (one for syntax, one for semantics, one for coreference, etc.).
```

**What changed:**
- ✓ Added opening task (translation ambiguity) before definition
- ✓ Added "Check Yourself" prediction moment before revealing dot product
- ✓ Addressed common misconception (scaling is not optional)
- ✓ Added practice opportunity (implement attention) with solution
- ✓ Connected to next chapter (multi-head attention preview)
