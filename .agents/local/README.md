# Local-Only Material

This directory is reserved for machine-local notes that must never be committed.

- Prefer a password manager, environment variables, or a managed secret store for real credentials.
- Do not keep production database dumps, personal data, private keys, or long-lived tokens in the repository tree.
- The root `.gitignore` ignores every item in this directory except this README.
- Use sanitized `.example` files outside this directory when contributors need configuration guidance.
