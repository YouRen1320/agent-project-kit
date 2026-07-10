# Decision Records

Store long-lived architecture, migration, contract, data-model, and policy decisions in this directory.

## When To Add A Record

Add a decision record when a choice:

- Changes architecture, repository boundaries, APIs, data models, or status semantics.
- Introduces or removes compatibility behavior.
- Establishes a production, security, data, or release policy.
- Requires phased migration or has meaningful rollback consequences.
- Is likely to be questioned again after the original task context is gone.

Do not use decision records as incident logs, task diaries, or a copy of implementation details.

## Naming

Use:

`YYYY-MM-DD-short-title.md`

Start from `../templates/decision-record.md`.

## Lifecycle

- `PROPOSED`: options are under review; no implementation approval implied.
- `ACCEPTED`: decision and completion criteria are approved.
- `SUPERSEDED`: a newer record replaces it; link both records.
- `REJECTED`: retained to explain why the option was not chosen.

## Maintenance

- Link implementation and migration work when available.
- Record verified evidence separately from assumptions.
- Include compatibility compromises, non-goals, rollback, and removal criteria.
- Update status rather than rewriting historical reasoning after the fact.
- Never store secrets, credentials, personal data, or sensitive operational logs.
