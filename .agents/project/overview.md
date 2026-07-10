# Project Overview

Complete this profile before relying on the procedure library for implementation or operations.

## Identity

| Item | Value |
| --- | --- |
| Project name | `<PROJECT_NAME>` |
| One-sentence purpose | `<PROJECT_PURPOSE>` |
| Primary users | `<PRIMARY_USERS>` |
| Maintainer group | `<MAINTAINER_GROUP>` |
| Documentation home | `<DOCUMENTATION_PATH_OR_URL>` |

## Product Scope

- In scope: `<IN_SCOPE_CAPABILITIES>`
- Explicitly out of scope: `<OUT_OF_SCOPE_CAPABILITIES>`
- Critical user journeys: `<CRITICAL_USER_JOURNEYS>`
- Regulated or sensitive data: `<DATA_CLASSIFICATION_OR_NONE>`

## Architecture Summary

| Layer or component | Responsibility | Source location | Main dependencies |
| --- | --- | --- | --- |
| `<COMPONENT_ID>` | `<RESPONSIBILITY>` | `<REPOSITORY_OR_PATH>` | `<DEPENDENCIES>` |

Architecture style: `<MONOREPO_MULTI_REPO_SERVICE_OR_OTHER>`

Primary data flow:

`<CLIENT>` -> `<API_OR_SERVICE>` -> `<DATA_STORE_OR_EXTERNAL_SYSTEM>`

## Critical Invariants

- Authorization decisions are derived from trusted server-side identity.
- `<PROJECT_INVARIANT>`
- `<PROJECT_INVARIANT>`

Any change that weakens an invariant is a major change and requires explicit option review, migration impact, and rollback planning.

## Delivery Expectations

- Default development branch policy: `<BRANCH_POLICY>`
- Required checks: `<REQUIRED_CHECKS>`
- Release mechanism: `<RELEASE_MECHANISM>`
- Evidence retained for delivery: `<EVIDENCE_REQUIREMENTS>`

## Project-Level Completion Criteria

A change is complete only when:

- Its agreed goal and scope are satisfied.
- All affected components and consumers are accounted for.
- Required checks and business scenarios pass.
- Migration, rollback, compatibility, and deployment status are documented where relevant.
- Verified results are separated from unverified items.
- Intentional non-goals are stated.
