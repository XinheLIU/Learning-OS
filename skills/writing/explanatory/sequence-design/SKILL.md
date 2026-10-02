# Sequence Design

**Purpose:** Order content for human absorption, not knowledge structure

**When to use:** After defining audience and outcome. Before developing examples or writing content. Ensures the teaching sequence follows how humans learn, not how experts organize knowledge.

**Inputs:**
- Outcome specification (from outcome-design)
- Capability checklist (reverse-engineered from outcome)
- Audience profile (from define-audience)

**Outputs:** Teaching sequence in `brief.md` Logic section containing:
- **Progression**: scenario → minimal result → principle → gradual complexity
- **Predicted friction points**: Where learners typically struggle, with mitigation strategies
- **Practice tasks**: Each tied to a specific capability goal
- **Transition scaffolding**: How to bridge between modules

**Principle:** "顺序比内容更容易决定成败" (Sequence determines success more than content does) - experts organize by abstraction, learners need intuition first

## Instructions

[TO BE IMPLEMENTED - Phase 3]

This skill designs the learning path after the outcome is clear. It orders concepts for absorption, not logical dependency.

Key principles:
- Start with a concrete scenario or problem, not definitions
- Build to minimal working result before explaining why
- Introduce complexity gradually (one new thing at a time)
- Predict where confusion happens (too fast? too many options? implicit prerequisite?)
- Add practice at the moment a capability is needed, not batched at the end

The sequence is not a knowledge tree. It's a path through the tree that lets someone who doesn't have the map yet make steady progress.

## Example Usage

```bash
/sequence-design
# Topic: REST APIs with FastAPI
# Outcome: Deploy working API with 5 endpoints
# Audience: Python developers, never built APIs
```

Expected output in brief Logic section:
```markdown
## Logic (Teaching Sequence)

### Module 1: First endpoint (30min)
**Goal:** See "Hello World" API running locally, understand request/response

**Progression:**
1. Scenario: "Your function needs to be called from another service"
2. Minimal result: One GET endpoint returns JSON
3. Principle: HTTP request → your function → HTTP response
4. Practice: Add `/status` endpoint that returns `{"status": "ok"}`

**Predicted friction:**
- "Where does the data come from?" → Show request object before explaining routing
- "Why FastAPI not Flask?" → Defer to Module 5; either works for learning

### Module 2: Accept input (45min)
**Goal:** Handle path params and query params

**Progression:**
1. Scenario: "Endpoint needs to vary by user ID"
2. Minimal result: `/users/{user_id}` returns different JSON per ID
3. Principle: URL parts become function arguments
4. Complexity: Add query params for filtering
5. Practice: Add `/items/{item_id}?include_details=true`

**Predicted friction:**
- "What types?" → Introduce Pydantic here (type safety becomes immediately useful)

### Module 3: POST and validation (60min)
**Goal:** Create resources with validated input

[continues...]
```
