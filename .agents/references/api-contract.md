# API Contract Review Reference

Use this reference when changing an endpoint, request or response field, event, schema, upload, status value, authentication behavior, or client API wrapper.

Project-specific conventions live in `../project/api-conventions.md`.

## Required Inventory

For every changed contract, identify:

- Authoritative producer and source location.
- Every direct and indirect consumer.
- Transport method, path or topic, authentication, and authorization.
- Request, response, event, or file schema.
- Error semantics, pagination, retries, and idempotency.
- Versioning, rollout order, and removal criteria.

## Contract Difference Table

| Contract | Producer actual | Consumer expected | Difference | Impact | Fix side | Migration |
| --- | --- | --- | --- | --- | --- | --- |
| `<METHOD_AND_PATH_OR_EVENT>` | `<ACTUAL>` | `<EXPECTED>` | `<DIFFERENCE>` | `<IMPACT>` | `<PRODUCER_CONSUMER_OR_BOTH>` | `<PLAN>` |

## Safety Rules

- Derive identity, tenant, ownership, role, privileged status, and authorization from trusted server-side context.
- Validate required fields, ranges, formats, file types, and business invariants at the authoritative producer.
- Define null, omitted, default, and unknown-enum behavior.
- Preserve idempotency for retried writes and event delivery where required.
- Ensure errors let consumers distinguish authentication, authorization, validation, conflict, rate limit, and server failure.
- Update generated schemas or clients through the authoritative generation process.
- Do not silently reinterpret an existing field with a different business meaning.

## Compatibility Decision

Choose explicitly:

| Strategy | Use when | Required evidence |
| --- | --- | --- |
| Additive | Existing consumers can safely ignore the addition | Consumer checks and schema behavior |
| Breaking coordinated release | All consumers can migrate together | Complete consumer inventory and rollout order |
| Phased migration | Consumers need independent rollout | Temporary compatibility design, telemetry, deadline, and removal owner |

Backward compatibility is not the default. If retained, document its cost, duration, rollback role, and deletion criteria.

## Verification

- Producer compile, tests, and runtime route or handler checks.
- Consumer static checks, tests, builds, and relevant smoke scenarios.
- Positive, validation, authorization, conflict, retry, and unknown-value cases.
- Old and new version interoperability during the approved rollout window.
- Contract documentation and module registry updated.

## Required Review Output

Include summary, differences, must-fix items, optional improvements, chosen migration strategy, verification, unverified risks, and next decision.
