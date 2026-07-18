# Piano360

**Last updated:** 2026-07-18

## Snapshot

Piano360 is a MongoDB-backed course MVP for guided piano learning. It uses a `Course -> Lesson -> Step` content model, an Express API, and a React/Vite client. Learner progress is stored locally in the browser.

## Links

- Repository: https://github.com/kofiarhin/piano360
- SSH: `git@github.com:kofiarhin/piano360.git`
- Live: Not documented

## Current State

- Lifecycle: Not documented
- Stack: React, Vite, Node.js, Express, MongoDB, Mongoose
- Testing: Vitest and React Testing Library for the client; Jest, Supertest, and `mongodb-memory-server` for the API
- Current priority: Not documented

## Current Focus

Not documented.

## Brainstorming

_No durable brainstorming notes captured yet._

## Decisions

- Course content follows a `Course -> Lesson -> Step` model.
- Learner progress remains local to the browser for the MVP.
- Course content is deliberately published through the seed workflow rather than during application startup.

## Assumptions

- None recorded.

## Open Questions

- What is the current product milestone?
- Is a public deployment planned or already available?
- Which course or learner experience should be improved next?

## Next Actions

- Document the current lifecycle state and milestone.
- Record the next learner-facing improvement when confirmed.
