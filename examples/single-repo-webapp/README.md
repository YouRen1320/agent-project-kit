# Example: Single-Repository Web Application

This fully fictional example shows a completed minimum project profile for a web application. None of its names or commands come from a private project.

## Overview

- Product: Pine Notes
- Repository: one application containing API and web UI
- Stack: TypeScript, React, Fastify, and PostgreSQL
- Environments: local, test, production
- Maintainer: Product Engineering

## Components

| Component | Path | Responsibility |
| --- | --- | --- |
| Web UI | `src/web/` | Pages, forms, and client-side state |
| API | `src/api/` | HTTP endpoints and authorization |
| Data | `src/data/` | Persistence and migrations |

## Commands

| Purpose | Command |
| --- | --- |
| Install | `pnpm install --frozen-lockfile` |
| Lint | `pnpm lint` |
| Test | `pnpm test` |
| Build | `pnpm build` |

## Example Contract

The UI and API share `/api/notes`. A note response contains `id`, `title`, `body`, `updatedAt`, and `revision`. User identity is derived from authenticated server context, never from a client-provided user identifier. A write with a stale `revision` returns a conflict response and does not overwrite newer content.

Use this level of specificity when filling `.agents/project/`: real commands, clear component boundaries, named ownership, and contract behavior that agents can verify.
