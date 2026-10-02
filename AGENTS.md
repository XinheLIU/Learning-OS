# Agent Instructions

Last updated: 2026-10-02

## Repository boundary

- This repository owns the Learning OS learning, knowledge-base, writing, and document-organization skills, plus their architecture, tests, and releases.
- It publishes shared-catalog metadata through `catalog/skill-set.json`.
- The common frontend is owned by the sibling `../agent-skills` repository; do not copy or recreate it here.

## Skill layout

- Skills live at `skills/{pipeline,learning}/<name>/SKILL.md` and `skills/writing/<group>/<name>/SKILL.md`, grouped by system; each system folder carries a `README.md` contract, and the root `README.md` is the front door.
- Skill discovery requires flat directories, so flat symlink layers point into the nested tree: `.claude-plugin/skills/` (tracked, the plugin install path) and the gitignored `.claude/skills/`, `.codex/skills/`, `.opencode/skills/` mirrors. After adding, renaming, or moving a skill, regenerate all four layers:

  ```bash
  for layer in .claude-plugin .claude .codex .opencode; do
    rm -rf "$layer/skills" && mkdir -p "$layer/skills"
    rg --files skills -g SKILL.md | while IFS= read -r skill; do
      d="${skill%/SKILL.md}"
      ln -sfn "../../$d" "$layer/skills/$(basename "$d")"
    done
  done
  ```

- A skill change also means updating `catalog/skill-set.json` (category IDs map to folders, including `writing/analytical` and the other writing groups via `sourcePattern: skills/{category}/{skill}/SKILL.md`).
- `tmp/` is the gitignored iteration corpus for pipeline and writing skills; `tmp/README.md` defines its convention. Durable rationale lives in `docs/adr.md`; unfinished work lives in `docs/exec-plans/`.

## Shared frontend

When the user asks to launch, run, open, preview, or test the frontend locally from this repository:

1. Run `node scripts/build-catalog.mjs --local` in `../agent-skills`.
2. Start `python3 -m http.server 4174 -d docs` in `../agent-skills`. If port `4174` is occupied, choose the next available port without terminating an unknown process.
3. Verify the local catalog loads, then give the user the exact `http://127.0.0.1:<port>/` URL and keep the server running.

Do not edit files under `skills/` for catalog or frontend work unless the user explicitly requests a skill change.
