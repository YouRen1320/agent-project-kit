# Getting Started With A New Project

## 1. Create The Repository

Create a new repository from the GitHub template. A repository created from a template starts with its own history, which is appropriate for a new product.

Do not place this kit beside another project and assume agents will load it. The instruction files must exist inside the target repository, or the workflows must be installed through an agent-supported distribution mechanism.

## 2. Fill The Project Profile

Invoke `$project-bootstrap` in Codex or `/project-bootstrap` in Claude Code to guide the evidence inventory and profile setup.

Complete these files using repository evidence:

1. `.agents/project/overview.md`
2. `.agents/project/repositories.md`
3. `.agents/project/commands.md`
4. `.agents/project/environments.md`
5. `.agents/project/api-conventions.md`
6. `.agents/project/ownership.md`

Do not guess commands, deployment targets, or owners. Mark an item as unknown and assign a follow-up owner when it cannot be verified.

## 3. Adapt The Router

Review `AGENTS.md`:

- Keep rules that apply to every task.
- Add only high-risk or frequently used routes.
- Move detailed procedures into `.agents/`.
- Add nested instructions only where a subtree genuinely needs different behavior.

Keep `CLAUDE.md` importing `@AGENTS.md`. Add only Claude-specific behavior below that import.

## 4. Select Workflows

Remove workflows that cannot apply to the project. If deployment or persisted-data changes are possible, keep the relevant safety runbooks even when the exact platform is not configured yet.

Never replace an abstract runbook with live credentials or unrestricted target details. Store operational commands in an approved private operations system and reference it by non-secret identifier.

## 5. Validate

First require the adopted project profile to be complete:

```sh
./scripts/validate-project-profile.sh
```

Then run the reusable kit checks:

```sh
./scripts/validate.sh
```

Then verify agent loading:

- Ask Codex to list the project instruction sources and available API contract skill.
- In Claude Code, inspect `/memory` and `/skills`.

## 6. Replace Template Documentation

Update the project README with its real product purpose, setup, architecture, and support path. Retain a short link to `AGENTS.md` or `.agents/index.md` so contributors can find the operating model.

Replace inherited maintainer material as well: code owners, security reporting, conduct reporting, supported versions, and release ownership must name the new project rather than the template repository.

## 7. Protect The Repository

Before inviting contributors:

- Add real code owners for trusted instruction and CI paths.
- Require review and validation checks on the default branch.
- Enable secret scanning, push protection, and private vulnerability reporting.
- Publish the chosen license and security policy.

The template's `validate-publish-readiness.py` is for publishing Agent Project Kit itself. An adopted product should customize or remove that script after defining its own publication policy.
