# Contributing

Contributions should improve reusable project guidance without importing private project facts.

## Before Opening A Change

1. Read `AGENTS.md` and `.agents/index.md`.
2. Define the problem, scope, and explicit non-goals.
3. For architecture, contract, directory, or cross-agent changes, compare viable options before implementation.
4. Use fictional and sanitized examples only.

## Content Rules

- Keep root agent files small and route details into `.agents/`.
- Put project-specific facts in `.agents/project/` templates, not generic workflows.
- Maintain one authoritative rule; use thin Codex and Claude entry points.
- Do not add credentials, personal data, real infrastructure, database dumps, internal incident history, or private repository names.
- Do not add executable production targets to the generic deployment runbook.
- Update `.agents/index.md` when adding shared guidance.
- Add or update examples when behavior is otherwise ambiguous.

## Verification

Run:

```sh
./scripts/validate.sh
./scripts/test.sh
```

For skill changes, also validate the affected `SKILL.md` with a compatible Agent Skills validator and test a realistic sanitized prompt.

## Pull Requests

Describe:

- Outcome and affected files.
- Decisions and alternatives considered.
- Verification performed and unverified areas.
- Compatibility compromises.
- Intentional non-goals.

Changes to `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, validation scripts, or CI should receive maintainer review because they change trusted agent behavior.
