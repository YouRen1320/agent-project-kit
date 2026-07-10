# Customization

## Keep Three Layers Separate

### Reusable core

Use `.agents/workflows/`, `.agents/runbooks/`, `.agents/templates/`, and `.agents/references/` for guidance that can apply across projects.

### Project profile

Use `.agents/project/` for verified facts such as component paths, commands, environments, API conventions, ownership, and release policy.

### Local private material

Use `.agents/local/` only for non-shareable machine notes. Prefer secret managers and environment injection for credentials. Never place database dumps or personal data in the repository tree.

## Adding A Workflow

Add a workflow when a recurring development task needs decisions, implementation order, or verification. Register it in `.agents/index.md` and add a root route only when the trigger is high risk or frequent.

## Adding A Runbook

Add a runbook for an operational procedure with prerequisites, safety checks, execution phases, verification, and rollback. Public runbooks should remain abstract and must not include live targets or credentials.

## Adding A Skill

Use a skill when an agent should load a focused workflow or reference only for matching tasks.

- Give the skill a concise name and trigger-rich description.
- Keep the skill body small.
- Link detailed rules from one authoritative reference.
- Provide both Codex and Claude project entry points when the workflow should work in both tools.
- For data mutation or deployment, require explicit invocation and approval rather than broad automatic execution.

Repository skills are appropriate for workflows tied to one codebase. Package a standalone reusable skill as a plugin only when it should be installed independently of the repository skeleton. See [distribution](distribution.md).

## Technology Profiles

Framework-specific rules should be optional profiles rather than universal policy. A profile may describe language conventions, package-manager commands, migration tooling, UI frameworks, or mobile verification, but must not silently change the core safety gates.

## Placeholders

Use uppercase angle-bracket placeholders such as `<PROJECT_NAME>` in template content. Explain each placeholder near its use. In an adopted project, replace or explicitly mark every relevant placeholder before relying on the guidance operationally.

Use `./scripts/validate-project-profile.sh` as the readiness gate for `.agents/project/`. It is expected to fail in the public template repository and to pass only after adoption is complete.
