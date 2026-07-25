# Changelog

Last updated: 2026-07-26

## 2026-07-26

### Added

- Added `framework.md` as structural learner memory for concepts, models, cross-mainline connections, and research frontiers.
- Added explicit cross-skill handoffs and evidence-gated course, loop, and research tiers.
- Added attempt logs, assistance metadata, retry results, and next-support-to-remove fields to learner evidence.

### Changed

- Reframed Learning OS around one shared, file-based learner memory under `learning/<slug>/`.
- Replaced one-dimensional survey triage with a 3–5 mainline by four-stage mastery matrix, behavioral milestones, target cells, and gap diagnosis.
- Limited curriculum authoring to knowledge and skill lessons; real-world Stage 4–5 work is now specified as `/practice` loop entries and closed by `/evaluate` evidence.
- Made `/learn` earn framework nodes, `/practice` earn framework edges, `/reflect` revise structure and advance its iteration, and `/research` extend the frontier.
- Made `/evaluate` assistance-aware: coached or unknown evidence is capped at `can-recall`, while higher mastery and tier transitions require low-assistance evidence.
- Updated README architecture and file contracts to document the shared-memory learning loop and strict boundary from the external wiki.
