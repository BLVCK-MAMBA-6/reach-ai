# Security Policy

## Supported version

Reach AI is under active pre-release development. Security fixes currently
apply to the latest commit on the default branch.

## Reporting a vulnerability

Do not disclose a suspected vulnerability through a public issue. Contact the
repository owner privately through their GitHub profile with a description,
reproduction steps, potential impact, and a suggested mitigation if known.

Do not include real credentials or unnecessary personal data.

## Security principles

- Secrets are loaded through environment variables.
- Real secrets must never be committed.
- Logs must redact credentials and sensitive personal data.
- PostgreSQL is authoritative for verified facts.
- Model-generated data must pass schema validation.
- Inferred memories cannot override confirmed profile facts.
- External writes require the appropriate user approval.
- Email sending is outside the MVP.
- OAuth permissions should use the narrowest practical scopes.
- Scheduled jobs must be idempotent.

Use synthetic or sanitized development data.
