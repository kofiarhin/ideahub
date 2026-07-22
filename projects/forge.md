# Forge

**Last updated:** 2026-07-22

## Snapshot

- **Lifecycle:** Active
- **Summary:** AI-powered software organization that coordinates specialist agents to move software from idea through implementation, verification, release preparation, and launch.
- **Repository:** https://github.com/kofiarhin/forge
- **Owner:** Kofi Arhin

## Links

- Repository: https://github.com/kofiarhin/forge
- Product requirements: https://github.com/kofiarhin/forge/blob/main/docs/PRD.md
- Technical specification: https://github.com/kofiarhin/forge/blob/main/docs/TECHNICAL_SPEC.md
- Codebase audit: https://github.com/kofiarhin/forge/blob/main/docs/CODEBASE_AUDIT.md
- Context API: [context-api.md](context-api.md)
- Zoro: [zoro.md](zoro.md)

## Current State

- **Forge** is the approved name for the top-level AI software organization.
- Forge is distinct from Zoro: Forge is the organization, while Zoro is its Chief Orchestrator.
- The Context API is the shared organizational memory and system of record used by Forge agents.
- The approved MVP organization includes Zoro, Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO.
- Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO begin as Forge modules rather than separate top-level projects.
- A Forge repository now exists on `main` with an improved README, a repository-local PRD, a proposed technical specification, and a codebase audit.
- The audit found no executable application, package manifest, tests, API contract, CI workflow, deployment configuration, data model, or runtime entry point before the documentation work.
- Forge is therefore a documented product and architecture scaffold, not an implemented orchestration system.
- Proposed components, integrations, security controls, agent execution, state transitions, and deployment behavior must not be described as implemented until repository evidence and verification exist.

## Current Focus

Approve the smallest executable Forge MVP slice and its authority boundaries before beginning implementation. The first slice should establish deterministic task state, one-repository coordination, isolated GitHub interaction, evidence capture, and verification without attempting the full multi-agent organization.

## Brainstorming

- Future specialist agents for product discovery, release operations, security, research, customer feedback, finance, sales, and support
- Promotion of mature Forge modules into independently versioned projects
- Event-driven synchronization between Forge workflow records, GitHub, and the Ideas Hub
- Reusable Forge templates for other founders or software teams

## Decisions

- The top-level project is named **Forge**.
- Forge is an AI-powered software organization, not merely an agent framework.
- Zoro is the Chief Orchestrator within Forge and is not the parent organization.
- Context API remains a separate infrastructure project and serves as Forge's shared memory and system of record.
- Zoro remains a separately maintained project because it has a distinct orchestration purpose and can evolve independently.
- The MVP specialist roles are Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO.
- Specialist roles other than Zoro start as Forge modules, not separate projects.
- Only tasks with status `ready` may be implemented.
- One Builder may actively own a task at a time.
- Builders cannot approve or complete their own work; Reviewer and QA provide independent verification.
- Every agent must retrieve current context before acting and must produce evidence for its work.
- A required-stage failure stops downstream execution and results in a `blocked` or `failed` state.
- Marketing and SEO may reference only QA-verified and released features.
- Human approval remains mandatory for implementation and other material or sensitive decisions.
- Repository documentation must distinguish proposed architecture from verified implementation.

## Assumptions

- The Context API can represent the Forge project, linked projects, tasks, and documentation records without immediate schema changes.
- The first Forge implementation can coordinate one repository and one active Builder per task.
- Legal provides first-pass risk review and does not replace qualified legal counsel.

## Open Questions

- Which document is the final approved implementation authority for the first executable slice?
- Which Context API entities should hold Forge modules, documentation, evidence, relationships, and agent authority rules?
- How should Context API and Ideas Hub synchronization avoid competing sources of truth?
- Which runtime will execute specialist agents during the first end-to-end demonstration?
- What constitutes a formal release event for the Marketing and SEO gates in the MVP?
- What credential scope, approval model, concurrency policy, recovery behavior, and audit-storage contract will govern execution?

## Next Actions

1. Review and approve the repository-local PRD and proposed technical specification as implementation authority, or record required changes.
2. Define the minimum executable slice, acceptance criteria, task state transitions, evidence schema, and agent authority boundaries.
3. Create implementation work only after the slice is approved and marked `ready`.
4. Build a small executable foundation with deterministic state transitions, isolated GitHub integration, and automated tests.
5. Verify the first end-to-end demonstration and reconcile the repository documentation and this project record against the verified revision.
6. Complete and verify the Forge and Zoro project records and relationships in Context API.