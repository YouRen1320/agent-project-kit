---
name: project-bootstrap
description: Configure Agent Project Kit in a new or existing repository. Use when initializing or adopting the kit, filling `.agents/project`, reconciling existing AGENTS.md or CLAUDE.md files, replacing template ownership, or verifying Codex and Claude Code project guidance. Do not use for ordinary product feature implementation.
---

# Project Bootstrap

1. Read `../../../.agents/references/project-bootstrap.md` completely.
2. Classify the repository as a new template, an existing project with guidance, an existing project without guidance, or the kit repository itself.
3. Inspect repository evidence and existing agent files before proposing edits; do not guess commands, owners, environments, or contracts.
4. Define scope, non-goals, unresolved decisions, and completion criteria. For a conflicting or structural adoption, compare viable merge options and wait for approval.
5. Populate or merge the project profile and entry points according to the reference while preserving unrelated user work.
6. Run project-profile and repository validation, then smoke-test Codex and Claude Code discovery where the clients are available.
7. Report verified evidence, unverified items, compatibility compromises, and intentional non-goals.
