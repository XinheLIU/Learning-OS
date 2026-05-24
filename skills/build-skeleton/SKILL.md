---
name: build-skeleton
description: |
  Build and manage the mdBook skeleton for the Agent Learning book. Use this skill
  when the user wants to create chapter stubs, update the TOC, rename chapters,
  or modify the book structure. Trigger on "create a chapter", "add a chapter",
  "rename chapter", "update SUMMARY", "build the book", "book skeleton", or
  any request about the book's directory layout and navigation.
---

# Build Skeleton

The book lives in `./book/` and is built with [mdBook](https://rust-lang.github.io/mdBook/).

## Commands

```bash
mdbook serve ./book   # dev server → http://localhost:3000
mdbook build ./book   # static output → book/_book/
```

## Book Structure

```
book/
├── book.toml              # mdBook config
└── src/
    ├── SUMMARY.md         # Left-nav hierarchy (source of truth)
    ├── README.md          # Landing page
    ├── resources.md       # Curated reading list
    ├── AGENTS.md          # Content conventions
    ├── 0N-topic/          # One directory per chapter
    │   └── README.md      # Chapter entry point
    ├── assets/            # Images (PascalCase filenames)
    ├── code/              # Example scripts
    └── templates/         # Copy-paste artifacts
```

## Key Conventions

- **SUMMARY.md** controls the nav. When adding/renaming chapters, update it plus `README.md` and `resources.md`.
- **Chapter arc:** `# Level N: Title` → `##` major sections → `###` subsections. No `#####` or deeper.
- **Images** go in `assets/` with PascalCase names. Reference as `![Alt](../assets/Name.png)` from chapter dirs.
- **Resources** cited in articles must be listed under their chapter section in `resources.md`.
- **Audience:** Engineers who code. Direct, practical, opinionated voice.
- Run `mdbook build ./book` after any structural change to verify it compiles.
