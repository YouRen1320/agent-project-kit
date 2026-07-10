# Repository And Component Map

This file is the authoritative inventory for source repositories and independently delivered components.

## Repository Inventory

| ID | Repository or path | Responsibility | Stack | Default branch | Build artifact | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| `<REPO_ID>` | `<REPOSITORY_PATH_OR_URL>` | `<RESPONSIBILITY>` | `<STACK>` | `<DEFAULT_BRANCH>` | `<ARTIFACT_OR_NONE>` | `<OWNER>` |

## Dependency Map

| Producer | Contract or artifact | Consumers | Compatibility requirement |
| --- | --- | --- | --- |
| `<PRODUCER_ID>` | `<API_EVENT_SCHEMA_PACKAGE_OR_ASSET>` | `<CONSUMER_IDS>` | `<REQUIREMENT>` |

## Cross-Repository Change Rules

- Identify every producer and consumer before changing a shared contract.
- Review, verify, commit, and report each affected repository independently.
- Do not assume repositories share branch names, package managers, release cadence, or deployment policy.
- If one consumer cannot migrate in the same delivery, choose an explicit phased migration or declare the release blocked.
- Record each repository's commit, verification, publication, and deployment status in the final report.

## Discovery Checklist

Before implementation, confirm:

- Active repository root and applicable nested instructions.
- Current branch, upstream, and remote divergence.
- User-owned or unrelated working-tree changes.
- Shared schemas, generated clients, events, queues, storage objects, and configuration keys.
- Components that are deployed separately.
- Owners required for review or approval.

## Known Boundaries

- Repository not managed by this project: `<EXTERNAL_REPOSITORY_OR_NONE>`
- Generated or vendored source: `<GENERATED_PATHS_OR_NONE>`
- Components intentionally excluded from coordinated releases: `<EXCLUDED_COMPONENTS_OR_NONE>`
