# Contributing to Reach AI

Thank you for helping build Reach AI.

Reach AI is currently being developed for the Personal AI track of the
Nebius × NVIDIA Global AI Hackathon.

## Development principles

- Protect user privacy.
- Keep verified facts separate from model inferences.
- Keep deterministic eligibility rules outside LLM prompts.
- Require evidence for important opportunity claims.
- Require approval before external actions.
- Prefer a tested vertical slice over disconnected features.
- Never present mock behavior as a live sponsor integration.

## Getting started

1. Fork or clone the repository.
2. Create a focused feature branch.
3. Copy `.env.example` to `.env`.
4. Add development credentials only to `.env`.
5. Implement the smallest coherent change.
6. Add or update tests.
7. Run all relevant validation commands.
8. Open a pull request with evidence of the result.

## Branch naming

Use a descriptive prefix such as `feat/opportunity-schema`,
`fix/deadline-timezone`, `test/extraction-conflicts`, or
`docs/update-architecture`.

## Data safety

Do not commit API keys, `.env` files, private résumés, real emails, OAuth
credentials, or personally identifiable test data. Use synthetic or sanitized
fixtures.

## Roadmap discipline

Only check a roadmap item after the implementation has been verified.
Partially completed work must remain unchecked.
