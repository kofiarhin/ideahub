# Context API

**Last updated:** 2026-07-21

## Snapshot

- **Lifecycle:** Active
- **Summary:** Centralized API for structured, reusable user, engineering, project, workflow, glossary, and learning context.
- **Repository:** https://github.com/kofiarhin/context-api
- **Live:** https://context-api-3b9dfadf403e.herokuapp.com
- **Product requirements:** https://github.com/kofiarhin/context-api/blob/main/docs/PRD.md
- **Technical specification:** https://github.com/kofiarhin/context-api/blob/main/docs/SPEC.md

## Links

- Repository: https://github.com/kofiarhin/context-api
- Live API: https://context-api-3b9dfadf403e.herokuapp.com
- PRD: https://github.com/kofiarhin/context-api/blob/main/docs/PRD.md
- Specification: https://github.com/kofiarhin/context-api/blob/main/docs/SPEC.md
- Public CRUD implementation: https://github.com/kofiarhin/context-api/commit/9f76f11356a80cd92e5f853e148df7f23b0c9340

## Current State

- The Node.js and Express API is backed by MongoDB through Mongoose and deployed to Heroku at the user-confirmed live URL.
- The API exposes profile, coding conventions, projects, tasks, instruction sets, Ideas Hub metadata, glossary entries, and durable learnings under `/api/v1`.
- Public unauthenticated CRUD is implemented on `main` through commit `9f76f11356a80cd92e5f853e148df7f23b0c9340`.
- Every domain supports `POST`, `GET`, `PATCH`, and soft-delete `DELETE`; `PUT` is intentionally excluded.
- Writes use client-provided stable identifiers, schema allowlists, immutable identifiers, conflict responses, and existing response envelopes.
- Delete is idempotent, archives records with `archivedAt`, and archived records can be restored through `PATCH`.
- Archived records are excluded from normal collection reads, explicitly queryable by status, and directly retrievable where the domain has an identifier route.
- Local project create and read requests were successfully exercised against the API.
- A private Custom GPT named **Zoro** was created as an AI project manager and connected to the deployed Context API through a GPT Action using an OpenAPI schema.
- Zoro successfully invoked the live `listProjects` action and retrieved current project data from the Context API.
- Zoro generated a ProjectOS report from live API data, clearly separating stored facts from inferred project-management observations and making no persistent changes without approval.
- The GPT Action currently exposes health, profile, project, and task operations, staying within the GPT Action operation limit.
- Full end-to-end write verification through Zoro is still pending for create, patch, and archive operations.
- Jest and Supertest CRUD coverage was added for every domain. Syntax, lint, formatting, model validation, and mocked service verification passed locally.
- The complete MongoDB-backed integration suite still needs an environment run because the local verifier could not download the MongoDB test binary due DNS resolution failure.

## Current Focus

Verify Zoro's project and task write operations against the deployed API, including create, update, soft delete, archived lookup, and refreshed collection reads.

## Brainstorming

- Semantic or vector search across context records
- A context-management dashboard
- Automatic learning ingestion with review and approval
- Event-driven synchronization with the Ideas Hub
- Context versioning and rollback
- Multi-user and project-scoped context
- Expand Zoro with additional Actions for coding conventions, instruction sets, glossary entries, Ideas Hub context, and learnings

## Decisions

- Context is divided into independently retrievable domains.
- API routes are versioned under `/api/v1`.
- The simplified MVP supports `POST`, `GET`, `PATCH`, and soft-delete `DELETE`; `PUT` is excluded.
- All endpoints are public and unauthenticated so AI agents can read and update context without credentials.
- Clients provide stable identifiers when creating records; duplicate active or archived identifiers return `409`.
- Stable identifiers and API-managed fields cannot be changed through `PATCH`.
- Delete archives records rather than permanently removing them, and restore uses `PATCH` with a non-archived status.
- Authentication, authorization, permanent deletion, audit history, dedicated restore routes, and upserts remain out of scope for this MVP.
- The public MVP must not store secrets or sensitive private context.
- The Ideas Hub remains the durable narrative source for project knowledge unless a later approved decision changes that responsibility.
- Zoro must retrieve Context API data before making project recommendations and must ask for approval before persistent writes.
- The GPT Action OpenAPI schema contains only health, profile, project, and task routes for the initial project-management integration.
- Jest and Supertest are the backend verification tools.

## Assumptions

- MongoDB remains suitable for the initial flexible context schemas.
- Clients benefit from retrieving and updating targeted context rather than loading the complete context set.
- Rate limiting, payload limits, explicit serializers, and schema validation provide basic operational guardrails but are not substitutes for authentication.
- The current Heroku deployment URL may change and should remain configuration-specific rather than becoming a reusable Agent System default.

## Open Questions

- How will Ideas Hub records be synchronized without creating competing sources of truth?
- What client authentication model should replace public writes when private or production-sensitive context is introduced?
- What approval workflow should govern promotion of observations into durable learnings?
- What precedence rules should apply when project-specific conventions conflict with global conventions?
- Should the OpenAPI schema be hosted by the Context API so GPT Actions can import and refresh it from a stable URL?

## Next Actions

- Use Zoro to archive the existing test project, then retrieve the default project collection and confirm the archived project is absent.
- Retrieve archived projects and confirm the soft-deleted test project remains available.
- Verify project creation and patch operations through Zoro.
- Verify task creation, retrieval, patch, and archive operations through Zoro.
- Run the complete Jest/Supertest suite in an environment with a working MongoDB test binary.
- Add authentication before storing private or sensitive records.
- Consider exposing a maintained OpenAPI document from the deployed API.
