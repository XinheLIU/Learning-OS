---
name: build-skeleton
description: Design and maintain file and navigation structure for Markdown-based publications in the destination repository. Never touches the draft source folder — that is package-chapter's scope. Tier 3: adapter, ~30 min. Use for creating structure, adding chapters, updating TOC, or renaming/moving/reordering sections while keeping navigation consistent.
---

Last updated: 2026-09-22

# Build Skeleton

Build the smallest coherent structure a publication needs, then keep structural representations synchronized. Derive conventions from the project instead of imposing fixed patterns.

## Scope Boundary

This skill operates **in the destination publication repository** (the book repo, the site, the wiki). It never touches a draft source folder.

- **Source folder portability** → `package-chapter`
- **Destination navigation** → this skill

The canonical handoff: `package-chapter` produces manifest stub data (id, locale, suggested path); the author moves the folder by hand; this skill writes the actual navigation entry.

## Establish the Contract

Before editing, inspect the repository and determine context for the current task:

| Concern | Evidence |
| --- | --- |
| Content root | Existing chapters, source directories, site config |
| Publishing engine | `book.toml`, `book.json`, `.gitbook.yaml`, `mkdocs.yml`, `docusaurus.config.*` |
| Navigation source | `SUMMARY.md`, sidebar config, index files, or generated navigation |
| Hierarchy | Parts, chapters, sections, appendices, ordering rules |
| Naming | Numbered/unnumbered paths, case, slug style, landing-page filenames |
| Languages/editions | Independent trees, mirrored trees, locale mappings, or single source |
| Supporting indexes | Resource lists, roadmaps, status trackers, root landing pages |
| Local rules | `AGENTS.md`, `CLAUDE.md`, contribution guides, nearby examples |
| Verification | Build, link-check, lint, or preview commands |

Prefer explicit configuration over inference from single examples. When evidence conflicts, ask which artifact is authoritative.

## Choose the Operation

### Initialize a Publication

1. Create only directories and files required by the selected publishing engine.
2. Add one content root, one authoritative navigation file or config, one landing page.
3. Create asset/code directories only when publication will use them.
4. Add language/edition trees only when requested.
5. Keep stubs minimal: title, purpose or scope, optional child links. No prose.
6. Use placeholder copy only when engine requires non-empty pages; label it clearly.

### Add a Part or Chapter

1. Choose the path from the existing naming and ordering rules.
2. Create the stub at that path.
3. Add it to the authoritative navigation in the intended position.
4. Update the parent landing page and explicit previous/next links, if present.
5. Mirror the structural change across declared language or edition trees. Do not translate prose unless requested.
6. Update supporting indexes only when they encode the changed structure.
7. Keep unpublished stubs out of published navigation when that is the project's established convention.

### Rename or Move Content

1. Identify the old path, new path, navigation entries, inbound links, asset references, path-derived IDs or slugs, locale or version mappings, and generated aliases or redirects.
2. Move the content without rewriting unrelated prose.
3. Update every reference to the old path, including references outside the content root.
4. Preserve a redirect or alias only when the publishing platform supports it and existing public links require compatibility.
5. Apply the same structural move to mirrored trees when they are contractually synchronized.
6. Confirm that no stale path remains except intentional compatibility entries such as redirects or aliases.

### Reorder Content

1. Change the authoritative navigation first.
2. Update explicit numbering in paths, titles, landing pages, resource indexes, or status files only where ordering is encoded.
3. Update previous/next links and mirrored navigation.
4. Avoid renaming files when order is controlled only by navigation.

## Maintain Structural Invariants

For every operation, derive applicable invariants from the project:

- Every published navigation entry resolves to an existing file.
- Every intended published chapter appears exactly once in navigation.
- Parent landing pages agree with authoritative navigation.
- Explicit previous/next links follow published order.
- Mirrored languages/editions have equivalent structure when required.
- Internal links and asset references remain valid after moves.
- Supporting indexes use current chapter names, paths, and numbering.
- Unpublished drafts remain excluded from publication when required.

Update an artifact only when it represents the changed structure.

## Verify

1. Search for old paths or titles after rename/move.
2. Compare navigation entries with files on disk; report missing targets and unlisted publishable files.
3. Check internal links and asset paths with repository's existing checker when available.
4. Run documented build command for detected publishing engine.
5. If no automated build/checker exists, inspect affected navigation and links directly and state limitation.
6. Report structural files changed, invariant checks performed, any intentionally unpublished stubs.

Never install a publishing engine or add dependency without user approval.
