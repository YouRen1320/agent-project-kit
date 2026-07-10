# Project API Conventions

Use this file for project-specific API decisions. Use `../references/api-contract.md` for the review workflow.

## Consumer Path Rules

| Consumer | Source path style | Request-layer behavior | Final request example |
| --- | --- | --- | --- |
| `<CONSUMER_ID>` | `<PATH_STYLE>` | `<PREFIX_REWRITE_OR_NONE>` | `https://api.example.com/<PATH>` |

## Request And Response Conventions

| Concern | Convention |
| --- | --- |
| Success envelope | `<SUCCESS_ENVELOPE>` |
| Error envelope | `<ERROR_ENVELOPE>` |
| Pagination | `<PAGINATION_FIELDS>` |
| Dates and time zones | `<DATE_TIME_FORMAT>` |
| Identifier format | `<IDENTIFIER_FORMAT>` |
| Null and omitted fields | `<NULLABILITY_RULE>` |
| File upload | `<UPLOAD_CONTRACT>` |
| Idempotency | `<IDEMPOTENCY_RULE>` |
| Rate limits | `<RATE_LIMIT_BEHAVIOR>` |

## Authentication And Authorization

- Authentication mechanism: `<AUTHENTICATION_MECHANISM>`
- Authorization source: `<SERVER_SIDE_IDENTITY_AND_POLICY_SOURCE>`
- Tenant or organization scope: `<SCOPE_RULE>`
- Public endpoints: `<PUBLIC_ENDPOINT_POLICY>`

Never trust client-provided user, tenant, role, privileged status, ownership, or monetary fields as authorization evidence.

## Versioning And Compatibility

- Versioning strategy: `<VERSIONING_STRATEGY>`
- Deprecation window: `<DEPRECATION_POLICY>`
- Client rollout order: `<ROLLOUT_ORDER>`
- Schema or client generation: `<GENERATION_PROCESS_OR_NONE>`

Breaking changes require an approved migration plan, consumer inventory, compatibility decision, rollback plan, and removal criteria. Backward compatibility is an explicit option, not an automatic default.

## Error Semantics

| Error category | Transport status | Application code | Client action |
| --- | --- | --- | --- |
| `<CATEGORY>` | `<STATUS>` | `<CODE>` | `<ACTION>` |
