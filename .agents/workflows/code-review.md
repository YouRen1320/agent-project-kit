# Code Review Workflow

Use this for code review, audit, regression analysis, or risk assessment.

## Default Behavior

- Review is read-only unless the user explicitly asks for fixes.
- Findings come first, ordered by severity.
- Every finding includes a precise file and line reference when available.
- Focus on behavior and risk, not personal style preferences.
- If there are no findings, say so and list residual risks or test gaps.

## Severity

| Severity | Meaning |
| --- | --- |
| Critical | Likely security breach, irreversible data loss, or broadly unavailable system |
| High | Broken core behavior, permission bypass, major regression, or unsafe migration |
| Medium | User-visible defect, inconsistent contract, or meaningful maintainability risk |
| Low | Limited-impact defect or concrete improvement that prevents future errors |

## Review Checklist

- Goal and behavior match the requested change.
- Authentication, authorization, tenant, ownership, and data-scope boundaries hold.
- API, event, schema, and generated-client contracts align.
- State transitions, retries, idempotency, and concurrency are safe.
- Migrations protect existing and historical data.
- Error handling is observable and guides the caller.
- Cross-component consumers are updated.
- Tests cover high-risk positive and negative paths.
- Deployment, configuration, and rollback assumptions are valid.
- Unrelated refactors or hidden compatibility behavior are not mixed in.

## Evidence Standard

Distinguish:

- Verified defect: demonstrated by code, test, or authoritative output.
- Likely risk: supported by evidence but not reproduced.
- Open question: cannot be resolved from available context.

Do not present judgment or speculation as a confirmed defect.

## Output

Use `../templates/review-report.md`.
