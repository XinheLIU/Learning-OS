# Writing System Execution Plan

Last updated: 2026-09-01

The writing workflow is implemented. This file contains only its remaining verification and
extension work. Durable design rationale lives in [`docs/adr.md`](../adr.md).

## 1. Finish the book-scale framing contract

Add a book-scale argument ladder to `llm-wiki-book`. It already inherits occasion-first framing,
steelman tests, a selection map, and gaps from `frame-piece`, but it currently commits a spine and
jumps directly to chapter mapping.

Acceptance: a wiki-to-book plan contains topic -> primary claims -> mechanisms -> concrete chapter
developments, and every selected wiki page supports a named ladder node.

## 2. Run the pending corpus fixtures

Use `tmp/learning-how-to-learn/` and the existing `brief.md`:

1. Run brief-aware `write-content`; confirm `cut` material is absent and author markers are present.
   Run brief-less mode once and confirm the flat-thesis warning fires.
2. Run `review-draft` on the real draft and a deliberately flattened version. The flat version must
   receive `reframe`; findings on the real draft must quote passages and rank fixes.
3. Apply one finding with `edit-targeted`; verify only the named span changes. Complete two short
   review/edit cycles.
4. Run the revised `llm-wiki-book` against the corpus wiki and verify the book-scale ladder,
   selection map, and gaps.

## 3. Add medium-specific adapters only when demanded

- Create one skill per medium, such as `publish-wechat` or `publish-xhs`; do not create a universal
  adapter.
- Each adapter owns its medium's length, hook, formatting, and audience constraints.
- Derive from the medium-neutral canonical draft and never edit back.
- Defer a durable `writing-profile.md` until several real briefs expose recurring preferences.

Acceptance for each adapter: the derived artifact follows its medium contract, the canonical draft
is byte-for-byte unchanged, and the adapter has a focused fixture.
