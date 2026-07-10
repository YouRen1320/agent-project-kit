---
name: api-contract
description: Review and plan API contract changes across producers and consumers. Use for endpoint paths, methods, request or response fields, pagination, errors, uploads, status values, authentication context, or frontend/backend contract mismatches such as 404 and undefined fields.
---

# API Contract

1. Read `../../references/api-contract.md` completely.
2. Read `../../project/api-conventions.md` for repository-specific conventions.
3. Identify every producer and consumer of the affected contract.
4. Record the current and expected path, method, request, response, errors, authentication, idempotency, and compatibility behavior.
5. For breaking contracts and cross-component changes, read `../../workflows/module-delivery.md`, compare options, and wait for confirmation before implementation.
6. Verify producer and consumer tests or builds, then report unverified consumers explicitly.
