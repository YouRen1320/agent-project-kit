# How Agents Load The Rules

## Codex

Codex starts from repository guidance in `AGENTS.md`. This file routes task-specific work into `.agents/` and should remain concise.

Repository skills live under `.agents/skills/`. Codex scans repository skill directories from the working directory up to the repository root. Invoke `$project-bootstrap` for adoption and `$api-contract` for contract review; either skill may also load when a request matches its description.

Nested agent files may narrow behavior for a subtree. Avoid conflicting global and nested instructions.

## Claude Code

Claude Code loads `CLAUDE.md`. Claude Code does not load `AGENTS.md` directly, so the root file imports:

```md
@AGENTS.md
```

This gives Claude the same durable router without duplicating it. Claude project skills live under `.claude/skills/` and point to the same `.agents/` references as Codex skills.

Use `/memory` to inspect loaded project guidance. Invoke `/project-bootstrap` or `/api-contract` directly to test skill discovery.

## Single-Source Rule

Maintain detailed policy once:

```text
Shared policy       .agents/workflows, runbooks, references, templates
Codex entry         AGENTS.md and .agents/skills
Claude Code entry   CLAUDE.md and .claude/skills
```

Tool-specific files may explain discovery or invocation differences, but should not restate the business or safety policy.

## Smoke-Test Prompts

Use sanitized prompts to verify routing:

- “Review this change for regressions.” Expected: read-only review workflow.
- “Change a shared API response field.” Expected: contract inventory and option approval before edits.
- “Adjust spacing on one page.” Expected: UI scope and visual verification.
- “Repair persisted production data.” Expected: environment, backup, impact, verification, and rollback gate.
- “Deploy this revision.” Expected: target, artifact, health, and rollback confirmation before commands.

## Authoritative Product References

- [OpenAI: AGENTS guidance](https://developers.openai.com/codex/concepts/customization#agents-guidance)
- [OpenAI: build and locate Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Anthropic: CLAUDE.md loading and AGENTS.md imports](https://code.claude.com/docs/en/memory)
- [Anthropic: Claude Code project skills](https://code.claude.com/docs/en/slash-commands)

These links describe discovery behavior. Repository validation confirms file structure, while a real client smoke test confirms the installed client and authenticated environment actually load it.
