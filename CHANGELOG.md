# Changelog

All notable changes are recorded here. Versions follow semantic versioning.

## [未发布]

### 变更

- GitHub 默认 README 改为中文，英文说明保留在 `README.en.md`。
- 新增采用场景速查和 Agent Memory Starter 对比，明确占位符不是产品承诺。

### 新增

- 已有项目增量接入示例，以及保留原规则并完成整套校验的回归测试。

## [0.1.0] - 2026-07-10

### Added

- Repository-level guidance for Codex and Claude Code.
- Project profiles for components, commands, environments, APIs, and ownership.
- Workflows for module delivery, code review, UI changes, and Git releases.
- Safety-oriented runbooks for persisted data, deployment, and rollback.
- Reusable report, decision, and module-registry templates.
- Cross-agent API contract skill entry points with one authoritative reference.
- Cross-agent project-bootstrap skill for evidence-based new-project setup and existing-project adoption.
- Fictional single-repository and multi-application examples.
- Offline structure, link, and public-safety validation.
- Automated positive and negative tests for validation behavior.
- Deterministic validation for Codex and Claude instruction imports, skill metadata, and shared references.
- A local publication-readiness gate for maintainer, Git, version, and reporting prerequisites.
- Monthly dependency updates for pinned GitHub Actions and a bounded CI timeout.
- Explicit CI provisioning for the documented ripgrep validation dependency.
- Node.js 24-based pinned GitHub Actions for warning-free validation runs.
- Open-source onboarding, contribution, conduct, security, and upgrade documentation.

### Security

- Public content was rebuilt from a whitelist and excludes private project operations, credentials, database backups, personal data, and real infrastructure identifiers.
