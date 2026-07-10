# Distribution Model

Agent Project Kit uses different distribution methods for different scopes.

| Need | Recommended method | Why |
| --- | --- | --- |
| Start a new repository with the complete operating model | GitHub template | Copies root guidance, project-profile templates, workflows, runbooks, skills, docs, and validation without inheriting commit history |
| Adopt the model in an existing repository | Deliberate manual merge | Preserves existing instructions and forces conflicts to be reviewed |
| Share one task-specific workflow inside a repository | Repository skill | Loads only when relevant and stays versioned with the project |
| Distribute one or more standalone Codex capabilities | Codex plugin | Appropriate when the reusable unit is a skill or connector rather than an entire repository skeleton |
| Update an adopted project | Reviewed release-by-release merge | Prevents automation from overwriting project facts or local policy |

## Why The Whole Kit Is Not A Plugin

The kit contains repository-root files, human documentation, GitHub community files, project facts, validation, and agent-specific entry points. A skill or plugin is a good distribution unit for an on-demand workflow, but it is not a substitute for a repository's durable `AGENTS.md`, `CLAUDE.md`, contribution policy, or project profile.

The `api-contract` or `project-bootstrap` skill may later be published independently as a plugin. The repository template remains the authoritative distribution for the complete kit.

## Versioning

- The template version is stored in `.agent-kit-version`.
- New projects created from the template start with independent history.
- Existing and generated projects do not receive template changes automatically.
- Breaking changes include renamed skills, changed routing, changed profile fields, and changed validation expectations.
- Every upgrade must preserve project-owned facts and show a reviewed diff.

See [upgrading](upgrading.md) and the [publishing checklist](publishing.md).
