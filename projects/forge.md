# Forge

**Last updated:** 2026-07-24

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
- Zoro orchestration runtime: https://github.com/kofiarhin/zoro/blob/main/docs/PARALLEL_ORCHESTRATION.md

## Current State

- **Forge** is the approved name for the top-level AI software organization.
- Forge is distinct from Zoro: Forge is the organization, while Zoro is its Chief Orchestrator and user-facing supervisor.
- Context API is the shared organizational memory and structured system of record used by Forge agents.
- The approved MVP organization includes Zoro, Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO.
- Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO begin as Forge modules rather than separate top-level projects.
- The Forge repository contains an improved README, repository-local PRD, proposed technical specification, and codebase audit.
- The Forge repository still has no executable application, package manifest, tests, API contract, CI workflow, deployment configuration, data model, or runtime entry point.
- `kofiarhin/zoro` now contains the first executable bounded parallel-worker foundation associated with the Forge direction.
- The Zoro runtime can decompose requests into validated dependency graphs, run compatible model workers concurrently, preserve partial results, and aggregate structured evidence.
- The implemented Zoro slice is not the complete Forge organization. It has no durable orchestration persistence, isolated Git worktrees, automatic worker patch application, production deployment, or full specialist tool adapters.
- Proposed Forge components, integrations, security controls, agent execution, state transitions, and deployment behavior must not be described as implemented unless supported by repository and verification evidence.

## Current Focus

Use the bounded Zoro worker runtime as the first executable orchestration experiment. Verify a read-only multi-worker demonstration, then design durable run persistence and isolated worker execution before allowing parallel repository mutation. Keep the broader Forge repository as the product and architecture authority until an approved executable Forge slice is defined.

## Brainstorming

- Future specialist agents for product discovery, release operations, security, research, customer feedback, finance, sales, and support
- Promotion of mature Forge modules into independently versioned projects
- Event-driven synchronization between Forge workflow records, GitHub, Ideas Hub, and Context API
- Reusable Forge templates for other founders or software teams
- A shared worker adapter protocol usable by Zoro, Architect, and future Forge services
- Durable orchestration dashboards, approvals, leases, evidence, costs, and recovery controls

## Decisions

- The top-level project is named **Forge**.
- Forge is an AI-powered software organization, not merely an agent framework.
- Zoro is the Chief Orchestrator within Forge and is not the parent organization.
- Context API remains a separate infrastructure project and serves as Forge's shared memory and structured system of record.
- Zoro remains a separately maintained project because it has a distinct orchestration purpose and executable service repository.
- The MVP specialist roles are Architect, Builder, Reviewer, QA, Legal, Marketing, and SEO.
- Specialist roles other than Zoro start as Forge modules, not separate projects.
- Only tasks with status `ready` may be implemented or dispatched for governed implementation.
- One Builder may actively own one mutating task scope at a time.
- Parallel read-only workers are permitted when dependencies and authority are explicit.
- Parallel mutating workers require isolated worktrees or sandboxes and non-overlapping ownership.
- Builders cannot approve or complete their own work; Reviewer and QA provide independent verification.
- Every worker must retrieve current bounded context before acting and produce structured evidence.
- A required-stage failure blocks downstream work while preserving successful sibling evidence.
- Marketing and SEO may reference only QA-verified and released features.
- Human approval remains mandatory for implementation authority and material or sensitive decisions.
- Repository documentation must distinguish proposed architecture from verified implementation.
- The bounded Zoro runtime is an implemented experiment, not evidence that the full Forge organization exists.

## Assumptions

- Context API can represent Forge projects, linked projects, tasks, documentation, evidence, and relationships without immediate destructive schema changes.
- MongoDB can support durable orchestration runs, jobs, attempts, leases, approvals, and evidence.
- Git worktrees or sandboxes can provide safe isolation for future parallel mutating workers.
- Legal provides first-pass risk review and does not replace qualified legal counsel.

## Open Questions

- Which document is the final approved implementation authority for the first executable Forge slice?
- Should the Zoro runtime become Forge's initial run engine or remain an adapter behind a separate Forge service?
- Which Context API entities should hold Forge modules, documentation, evidence, relationships, and agent authority rules?
- How should Context API and Ideas Hub synchronization avoid competing sources of truth?
- Where should durable worker leases, approvals, costs, and artifacts live?
- Which runtime will execute sandboxed mutating specialists during the first end-to-end demonstration?
- What constitutes a formal release event for the Marketing and SEO gates?
- What credential scope, approval model, concurrency policy, recovery behavior, and audit-storage contract will govern execution?

## Next Actions

1. Verify Zoro runtime version `1.4.0` and a harmless read-only multi-worker orchestration run.
2. Record the orchestration service deployment and authentication decision.
3. Approve the durable run, job, lease, approval, evidence, and artifact model.
4. Implement MongoDB-backed resumable runs with deterministic state transitions.
5. Add isolated Git worktrees or sandboxes and scoped worker tool adapters.
6. Add independent executable Reviewer and QA checks.
7. Reconcile the Forge PRD and technical specification with the verified Zoro experiment without presenting the full organization as implemented.
8. Define and approve the smallest end-to-end Forge slice that moves one ready task through isolated implementation and independent verification.
