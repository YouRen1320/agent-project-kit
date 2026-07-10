# Agent Project Kit

[中文说明](README.zh-CN.md)

Agent Project Kit is a repository-local operating guide for people, Codex, and Claude Code. It provides durable project instructions, decision gates, reusable workflows, safety-oriented runbooks, report templates, and cross-agent skills without embedding private project data.

Current version: **0.1.0**

## What It Solves

- Gives contributors one clear place to learn how a project works.
- Routes coding agents to the right workflow before they edit or operate systems.
- Requires option review for architecture, contracts, data models, and destructive changes.
- Separates reusable policy, project facts, and machine-local private material.
- Keeps Codex and Claude Code aligned through separate entry points and one authoritative procedure library.

## Quick Start

### New project

1. Create a repository from this GitHub template.
2. Invoke `$project-bootstrap` in Codex or `/project-bootstrap` in Claude Code, then replace the placeholders under [`.agents/project/`](.agents/project/) using repository evidence.
3. Review [`AGENTS.md`](AGENTS.md) and keep only rules that should apply to every task.
4. Replace the generated project's README with its actual product documentation while retaining a link to the agent guidance.
5. Run `./scripts/validate-project-profile.sh`, then `./scripts/validate.sh`.

See [Getting started](docs/getting-started.md).

### Existing project

Do not overwrite existing agent instructions. Invoke `$project-bootstrap` in Codex or `/project-bootstrap` in Claude Code, merge the kit deliberately, preserve project-specific rules, and validate the combined result. See [Adopting the kit in an existing project](docs/existing-project.md).

## How Agents Discover It

- **Codex** reads the repository `AGENTS.md` and discovers repository skills under `.agents/skills/`.
- **Claude Code** reads `CLAUDE.md`; this kit imports `@AGENTS.md` and exposes matching project skills under `.claude/skills/`.
- Detailed procedures remain under `.agents/` so the two entry points do not duplicate policy.

See [How agent loading works](docs/how-agents-load-rules.md).

## Included Skills

| Skill | Codex | Claude Code | Purpose |
| --- | --- | --- | --- |
| Project bootstrap | `$project-bootstrap` | `/project-bootstrap` | Configure or merge the kit and verify project guidance |
| API contract | `$api-contract` | `/api-contract` | Review producers, consumers, compatibility, migration, and verification |

## Repository Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Small, durable router for Codex and compatible agents |
| `CLAUDE.md` | Claude Code entry point that imports shared guidance |
| `.agents/project/` | Facts and commands the adopting project must complete |
| `.agents/workflows/` | Review and delivery processes |
| `.agents/runbooks/` | Safety gates for data, deployment, and rollback |
| `.agents/templates/` | Reusable reports, decisions, and module registries |
| `.agents/skills/` | Codex project skills |
| `.claude/skills/` | Claude Code project skills |
| `.agents/local/` | Ignored machine-local material; never a secret archive |
| `examples/` | Fictional adoption examples |
| `scripts/` | Offline validation, tests, and publication-readiness checks |

## Safety Model

The public kit must never contain real credentials, personal data, production dumps, private infrastructure, or target-specific deployment commands. Prefer a secret manager or environment injection for secrets. Keep operational facts in approved private systems and record only non-secret references here.

Before publishing or changing the kit itself:

```sh
./scripts/validate.sh
./scripts/test.sh
```

Local validation requires Bash, Python 3, and ripgrep (`rg`).

To reject private project identifiers during a clean-room migration, supply a private regular expression without committing it:

```sh
EXTRA_DENY_PATTERN='<PRIVATE_PATTERN>' ./scripts/check-public-safety.sh
```

The public kit intentionally contains project-profile placeholders. A generated application must make `./scripts/validate-project-profile.sh` pass before treating the profile as authoritative.

Also enable the hosting platform's secret scanning, push protection, protected default branch, and private vulnerability reporting.

Before making the repository public, complete the [publishing checklist](docs/publishing.md). It deliberately requires real code owners and monitored private reporting routes; this template does not invent them.

After the maintainer configuration, initial commit, and private `origin` exist, run:

```sh
python3 scripts/validate-publish-readiness.py
```

This local gate does not replace verification of GitHub settings or remote CI.

## Documentation

- [Getting started](docs/getting-started.md)
- [Existing-project adoption](docs/existing-project.md)
- [Customization](docs/customization.md)
- [Agent loading](docs/how-agents-load-rules.md)
- [Upgrading](docs/upgrading.md)
- [Distribution model](docs/distribution.md)
- [Publishing checklist](docs/publishing.md)
- [Single-repository example](examples/single-repo-webapp/README.md)
- [Multi-application example](examples/multi-app-platform/README.md)

## Contributing And Security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Report security issues privately according to [SECURITY.md](SECURITY.md).

Licensed under the [MIT License](LICENSE).
