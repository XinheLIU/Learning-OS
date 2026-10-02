# Outcome Design

**Purpose:** Work backwards from target result to define what the course actually delivers

**When to use:** After defining audience, before building the teaching sequence. Ensures the course aims for a concrete deliverable, not "learn about X."

**Inputs:**
- Audience profile (from define-audience)
- Topic or concept to teach

**Outputs:** Outcome specification in `brief.md` containing:
- **Concrete deliverable**: What the learner builds/ships (not "understand X" but "deploy X")
- **Quality bar**: How good it needs to be (working? production-ready? optimized?)
- **Capability checklist**: Reverse-engineered from outcome (what must they be able to do?)
- **What to deliberately exclude**: Out of scope (prevents knowledge dumping)

**Principle:** "从终点倒推" (Work backwards from the end) - avoids dumping the instructor's entire knowledge tree

## Instructions

[TO BE IMPLEMENTED - Phase 3]

This skill defines the concrete outcome before planning the path. It prevents courses that "teach everything I know about X" and ensures every lesson serves a deliverable.

Key questions:
- What will they build/ship at the end? (Specific, concrete, verifiable)
- What quality bar? (MVP? Production-ready? Performant?)
- What capabilities are required to achieve that outcome?
- What can we deliberately exclude and still hit the outcome?

The outcome specification constrains scope and guides sequencing. If a concept doesn't serve the outcome, it's out of scope.

## Example Usage

```bash
/outcome-design
# Topic: REST APIs with FastAPI
# Audience: Python developers, never built APIs
```

Expected output in brief:
```markdown
## Outcome

**Deliverable:**
- A working REST API with 5 endpoints (CRUD for one resource + auth)
- Deployed to a cloud platform (Railway/Render)
- Passes automated test suite (20+ tests)
- Returns proper HTTP status codes and JSON responses

**Quality bar:**
- Handles validation errors gracefully
- Uses proper HTTP verbs and status codes
- Basic security (API key auth)
- NOT production-scale (no rate limiting, no advanced auth)

**Required capabilities (reverse-engineered):**
1. Define route handlers with path/query parameters
2. Validate request bodies with Pydantic
3. Return structured JSON responses
4. Handle errors and return appropriate status codes
5. Add middleware for authentication
6. Write automated API tests
7. Deploy to a platform

**Deliberately excluded:**
- Advanced auth (OAuth, JWT)
- Database optimization
- GraphQL
- WebSockets
- Async/await deep dive
```
