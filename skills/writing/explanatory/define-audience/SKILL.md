# Define Audience

**Purpose:** Answer "给谁学" (who is learning) before building course outline

**When to use:** When creating explanatory content (tutorials, courses, teaching chapters) where the audience's current knowledge state and obstacles will shape the entire teaching approach.

**Inputs:**
- Topic or concept to teach
- Tentative scope (what will be covered)
- Any known constraints (time, prerequisites, target outcome)

**Outputs:** Audience profile section in `brief.md` containing:
- **Current knowledge state**: What the audience already knows and can do
- **Main obstacles**: Technical difficulty vs. path complexity vs. tool complexity
- **Target independent capability**: Concrete outcome the audience should achieve
- **Completion evidence**: How to verify they've reached the capability

**Contract:** "人群越清晰，课程边界越清晰；边界越清晰，主线越稳定" (Clearer audience → clearer boundaries → more stable main thread)

## Instructions

[TO BE IMPLEMENTED - Phase 3]

This skill defines the audience profile before building explanatory content. It ensures teaching is designed for a specific learner state, not dumping the instructor's full knowledge tree.

Key questions:
- Who exactly is learning this? (Role, current abilities, context)
- What can they already do independently?
- What's blocking them from the next level? (Technical gaps, conceptual confusion, overwhelming choices)
- What specific capability marks completion?

The profile guides every downstream choice: what to include/exclude, what order to teach, where to add scaffolding, how much practice to include.

## Example Usage

```bash
/define-audience
# Topic: Building REST APIs with FastAPI
# Context: For Python developers who've never built APIs before
```

Expected output in brief:
```markdown
## Audience

**Current knowledge state:**
- Can write Python functions and classes
- Understand basic web concepts (URLs, HTTP verbs)
- Have not built web services or APIs before

**Main obstacles:**
- Path complexity: Overwhelmed by choices (Flask vs FastAPI vs Django, sync vs async, ORMs)
- Technical difficulty: Don't understand request/response cycle, routing, validation

**Target capability:**
- Build and deploy a working REST API with 3-5 endpoints
- Handle validation, error responses, and basic auth
- Write automated tests for API endpoints

**Completion evidence:**
- Deployed API running on a server
- Can explain what each endpoint does and why
- API passes automated test suite
```
