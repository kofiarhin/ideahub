# Zoro

**Last updated:** 2026-07-24

## Snapshot

- **Lifecycle:** Active
- **Summary:** Forge Chief Orchestrator, governed GitHub operator, and Context API-connected Custom GPT with a local React/Express execution service.
- **Repository:** https://github.com/kofiarhin/zoro
- **Owner:** Kofi Arhin

## Links

- Repository: https://github.com/kofiarhin/zoro
- Forge: [forge.md](forge.md)
- Context API: [context-api.md](context-api.md)
- Zoro command center: [../zoro/README.md](../zoro/README.md)
- Canonical Zoro instructions: [../zoro/INSTRUCTIONS.md](../zoro/INSTRUCTIONS.md)
- GPT Builder bootstrap: [../zoro/BOOTSTRAP.md](../zoro/BOOTSTRAP.md)
- Generated runtime: [../runtime/zoro.md](../runtime/zoro.md)
- Runtime manifest: [../runtime/manifest.json](../runtime/manifest.json)
- Shared coordination policy: [../AGENT_COORDINATION.md](../AGENT_COORDINATION.md)
- Operational log policy: [../logs/README.md](../logs/README.md)
- Parallel orchestration documentation: https://github.com/kofiarhin/zoro/blob/main/docs/PARALLEL_ORCHESTRATION.md
- Context API GitHub Gateway specification: https://github.com/kofiarhin/context-api/blob/main/docs/GITHUB_GATEWAY_SPEC.md

## Current State

- A private Custom GPT named **Zoro** exists and is connected to the deployed Context API through OpenAI Actions.
- End-to-end Context API project CRUD and controlled GitHub repository operations have been exercised through Zoro.
- Zoro's canonical repository-backed instructions are stored in Ideas Hub and loaded through the generated runtime/bootstrap model.
- The live GPT must be tested in a fresh conversation before instruction version `1.4.0` is described as active.
- `kofiarhin/zoro` contains a React/Vite client, Express server, workspace-scoped file tools, allowlisted command execution, and an OpenAI-compatible chat proxy.
- `kofiarhin/zoro` `main` now contains a bounded parallel model-worker orchestration runtime under `server/orchestrator/`.
- The runtime supports request decomposition, validated dependency graphs, bounded fan-out/fan-in scheduling, specialist worker roles, repository/path conflict detection, partial-failure preservation, structured evidence aggregation, and in-memory run lookup.
- The orchestration API is exposed through `POST /api/orchestrations` and `GET /api/orchestrations/:runId`.
- The default configured maximum is four parallel workers, capped by server configuration.
- Nine Node tests passed locally before publication, covering parallel execution, dependency ordering, path conflicts, graph cycles, partial failures, and aggregate evidence.
- GitHub readback confirmed the scheduler and test suite on `main` at final implementation commit `9383afb58c698cc6e8d15293c20c8727b4d7088c`.
- No GitHub Actions workflow exists in the Zoro repository, so no CI result is available for this change.
- The current worker runtime performs parallel model tasks. It does not yet create isolated Git worktrees, apply patches automatically, persist runs across restarts, merge branches, or deploy software.
- Mutating worker output remains proposed work or evidence until a primary GitHub mutation is independently confirmed.
- Zoro and its workers cannot approve or complete their own Architect tasks.
- Ideas Hub presence still represents the supervising Zoro conversation, not every worker job.
- The existing Context API deletion-remediation and Heroku Gateway work remain separate governed workstreams and are not completed by this orchestration update.

## Current Focus

Verify Zoro instruction version `1.4.0` in a fresh GPT conversation, configure a reachable orchestration service for the live GPT, and run a harmless multi-worker demonstration using read-only research, review, QA, or documentation jobs. Do not enable concurrent code mutation until isolated worktrees or sandboxes and durable run persistence are implemented and verified.

## Brainstorming

- MongoDB-backed orchestration runs, worker jobs, leases, approvals, evidence, and artifacts
- One Git worktree or sandbox per mutating worker
- Scoped worker tool adapters for repository reads, patches, commands, and tests
- Cancellation, retries, resumable approvals, and dead-letter handling
- Worker dashboards, dependency graphs, cost tracking, and run timelines
- Context API synchronization for durable cross-session orchestration records
- Additional specialists for security, legal, marketing, SEO, release operations, and product research
- Generated GPT Action schemas for the Zoro orchestration service

## Decisions

- Zoro is a separately maintained project within Forge, not the top-level organization.
- Forge is the organization; Zoro is its Chief Orchestrator and user-facing supervisor.
- Zoro's executable service repository is `kofiarhin/zoro`.
- Zoro's canonical operating instructions live in Ideas Hub under `zoro/README.md` and `zoro/INSTRUCTIONS.md`; GPT Builder retains only the minimal loader from `zoro/BOOTSTRAP.md`.
- Repository instruction changes and live GPT activation are separate states and require fresh-conversation verification.
- The initial parallel runtime is bounded to model-worker fan-out/fan-in, not autonomous parallel repository mutation.
- The default maximum is four concurrent workers.
- Initial worker roles are Architect, backend Builder, frontend Builder, general Builder, Reviewer, QA, Research, and Documentation.
- Every worker job must have a stable identity, objective, dependencies, authority, owned paths, acceptance criteria, and structured result.
- Read-only workers may run concurrently.
- Jobs with overlapping repository or path ownership must be serialized unless verified isolation exists.
- `Promise.allSettled`-style behavior preserves successful sibling results when one worker fails.
- Worker `completed` means the delegated job returned a result; it is not authoritative task or project completion.
- Worker output cannot grant approval, verify itself, merge, deploy, migrate, or change Architect task state.
- Primary repository, CI, deployment, and runtime evidence remains authoritative for implementation claims.
- Human approval remains mandatory for material scope, migrations, destructive operations, security-sensitive changes, direct-main work unless explicitly authorized, merges, deployments, and production configuration.
- Context API remains the structured machine context service; Ideas Hub remains durable human-readable project context.
- Operational logs remain supporting chronology and cannot replace primary evidence or verification.

## Assumptions

- The configured OpenAI-compatible provider can handle several concurrent chat-completion requests within its own limits.
- A hosted or locally reachable Zoro orchestration API can later be exposed to the live Custom GPT through a governed Action.
- MongoDB is suitable for the next durable orchestration persistence step.
- Git worktrees or sandboxes can provide the required isolation for future mutating workers.

## Open Questions

- Where will the orchestration service be deployed and how will the live GPT authenticate to it?
- Should orchestration persistence live directly in Zoro's MongoDB database or be exposed through Context API?
- Which tool protocol should mutating workers use for iterative reads, patches, commands, and verification?
- How should worker leases, cancellation, retries, and interrupted-run recovery work?
- How should integration branches combine independently verified worker branches?
- Which jobs may be preauthorized and which always require a human approval interruption?
- When should the single Zoro presence record evolve into a supervisor record plus durable worker-run records?
- Has live GPT runtime version `1.4.0` been verified in a fresh conversation?

## Next Actions

1. Start a fresh Zoro GPT conversation and verify runtime version `1.4.0`, source loading, indexed inbox paths, presence interpretation, and orchestration limitations.
2. Configure or deploy the Zoro Express service so the live GPT can reach the orchestration endpoints securely.
3. Add the orchestration endpoints to a maintained GPT Action schema with explicit authentication.
4. Run a harmless two-to-four worker read-only demonstration and retain the returned run record.
5. Add MongoDB persistence for runs, jobs, attempts, approvals, evidence, leases, and artifacts.
6. Add isolated Git worktrees or sandboxes before enabling concurrent mutating workers.
7. Add scoped tool adapters and independent executable Reviewer/QA verification.
8. Add CI for the Zoro repository and verify the orchestration suite from a clean checkout.
9. Continue existing Context API GitHub Gateway and deletion-remediation work only within its separate recorded authority.
