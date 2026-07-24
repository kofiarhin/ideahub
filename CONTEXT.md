# Workspace Context

**Last updated:** 2026-07-24

## Purpose

This repository is Kofi's persistent brainstorming workspace and broad reference layer across software, business, content, photography, and AI-assisted work.

It exists so any GitHub-enabled AI agent can quickly understand the current project landscape without depending on old chat history.

## How To Use This Context

- Read this file for the broad overview.
- Use `PROJECTS.md` for the authoritative project list.
- Open project files for deeper context.
- Treat `INBOX.md` as unprocessed brainstorming, not confirmed direction.
- Use indexed inboxes under `inboxes/` for active Zoro and Architect communication.
- Follow `AGENT_COORDINATION.md` for shared access, authority, communication, verification, and write policy.
- Do not write changes without explicit approval or an approved workflow that authorizes the scoped change.
- Use `architect/README.md` to resolve registered Architect commands.
- Treat `architect/runs/` as authoritative operational audit, task, and report history, not canonical project truth.
- Treat operational logs and presence as supporting evidence, not approval or completion state.

## Working Profile

Kofi works across full-stack software development, content creation, photography, product thinking, and business tooling.

Default engineering preferences unless a project says otherwise:

- React with the latest Vite
- Node.js and Express
- MongoDB and Mongoose
- Tailwind CSS by default
- TanStack Query for server state
- Redux Toolkit only for shared client state
- Vitest for frontend tests
- Jest and Supertest for backend tests
- Environment variables for secrets and environment-specific configuration

## Recent Accomplishments

- Implemented a bounded parallel model-worker runtime directly on `kofiarhin/zoro` `main`.
- Added request decomposition, dependency graph validation, specialist roles, bounded concurrency, path ownership conflict detection, partial-failure preservation, structured evidence aggregation, and in-memory run lookup.
- Added `POST /api/orchestrations` and `GET /api/orchestrations/:runId` to the Zoro Express server.
- Added nine Node tests covering parallel execution, dependencies, conflicts, cycles, partial failures, and evidence aggregation; all passed locally before publication.
- Confirmed the remote scheduler and test suite through GitHub readback at Zoro commit `9383afb58c698cc6e8d15293c20c8727b4d7088c`.
- Updated Zoro's canonical instructions and generated runtime to version `1.4.0` with governed parallel-worker behavior and explicit capability limits.
- Corrected the durable Zoro record to identify `kofiarhin/zoro` as its implementation repository.
- Preserved the distinction between bounded model-worker orchestration and future isolated parallel repository mutation.
- Deployed Context API to Heroku and confirmed release `v14` from `main` revision `bf378b82ed04c88152c3cbb7550a590e63a19601` started successfully and connected to MongoDB.
- Completed the authenticated GitHub Gateway foundation for Zoro with repository, branch, UTF-8 file, and pull-request operations plus branch protection, optimistic concurrency, non-force updates, workflow-file blocking, and optional repository allowlisting.
- Produced a GPT Builder-compatible OpenAPI copy preserving all 27 Context API and GitHub operations.
- Configured the private Zoro GPT with Bearer authentication and verified live repository listing through the deployed Context API.
- Established Ideas Hub as the shared durable project brain for Zoro and Architect, with indexed communication, advisory presence, governed task state, and operational logs.

## Project Landscape

### Personal systems and AI workflows

- **Forge** — active AI-powered software organization with repository-local PRD/spec/audit. The full Forge runtime is not implemented; Zoro's bounded worker service is the first executable orchestration experiment.
- **Zoro** — Forge Chief Orchestrator, governed GitHub operator, Context API-connected Custom GPT, and local React/Express service. Parallel model-worker orchestration is implemented; live GPT/service integration, persistence, and isolated mutating workers remain unverified or unimplemented.
- **Context API** — Forge's shared structured memory and system of record; public CRUD and authenticated GitHub Gateway are deployed. Deletion remediation, gateway verification, redeployment, and final cleanup evidence remain separate active work.
- **Brain** — MERN personal operating system with MongoDB-backed memory and AI-assisted workflows; repository-local PRD, technical specification, and audit exist, while test and deployed-revision evidence remain outstanding.
- **Codex Workflow Kit** — reusable AI engineering workflow system with PRD, technical specification, and audit; legacy artifact-path documentation reconciliation remains next.
- **Agent System** — active runtime-agnostic agent instruction system; setup and synchronization are implemented and user-verified across Codex, Claude Code, and Gemini CLI, with Windows CI, compatibility evidence, and release tagging next.
- **Ideas Hub** — this repository; shared durable project context, indexed communication, presence, runtime instructions, and operational memory.
- **Zoro–Architect Coordination** — Architect governs discovery, approval, authoritative task state, independent verification, and durable truth. Zoro executes or orchestrates approved work and reports evidence.
- **Architect Command System** — Ideas Hub-backed workflows for portfolio auditing, durable task queues, approval-aware execution, verification, reporting, and context maintenance.
- **Archon** — paused AI-powered architecture studio with approved MVP specifications; no work should resume until explicit reactivation.

### Learning and mentorship

- **Piano360** — guided piano-learning course application.
- **DevKofi** — MERN mentorship and learning platform.

### Games and interactive experiences

- **Memory Sequence Game** — exploring responsive browser game where players memorize and reconstruct increasingly long visual card sequences.

### Business and product projects

- **KareBraids** — braid-service browsing and booking platform based in Birmingham, UK.
- **Amas Kitchen** — premium Ghanaian kitchen ordering and services application; homepage design direction awaits approval.
- **Taxify** — archived until explicitly reactivated.
- **Kflix**, **Banging Prices**, and **MoggOff** — details need further documentation.
- **ProjectOS** — archived autonomous development operating system requiring a fresh review before reactivation.

## Known Live Products

- Brain: https://brain-pi-black.vercel.app/
- KareBraids: https://karebraids.vercel.app/
- DevKofi: https://devkofi.com/
- Context API: https://context-api-3b9dfadf403e.herokuapp.com/

## Current Priorities

1. Verify Zoro runtime version `1.4.0` in a fresh Custom GPT conversation.
2. Configure or deploy a secure reachable Zoro orchestration service and connect its endpoints through a maintained GPT Action schema.
3. Run and retain a harmless two-to-four worker read-only orchestration demonstration.
4. Add MongoDB persistence for orchestration runs, jobs, attempts, approvals, leases, evidence, and artifacts.
5. Add isolated Git worktrees or sandboxes before enabling parallel mutating workers.
6. Add scoped worker tools and independent executable Reviewer/QA verification.
7. Continue Context API GitHub Gateway and deletion-remediation work within its separate recorded authority.
8. Complete remaining repository and deployed-revision evidence for Brain and Agent System.
9. Reconcile Codex Workflow Kit legacy documentation with its current run-scoped artifact model.

## Workspace Gaps

- Zoro instruction version `1.4.0` is committed but not yet verified as active in a fresh live GPT conversation.
- The Zoro orchestration API is implemented in the repository but has no recorded hosted deployment or live GPT Action connection.
- Orchestration runs are in-memory and disappear when the server restarts.
- Worker execution currently consists of bounded model tasks; isolated worktrees, automatic patch application, and durable worker tools are not implemented.
- The Zoro repository has no GitHub Actions workflow, so the orchestration tests have local evidence and GitHub readback but no CI evidence.
- The first live multi-worker demonstration has not been recorded.
- Context API pull request #2 and related deletion cleanup remain outstanding unless superseded by newer verified evidence.
- Forge remains a documented product and architecture scaffold rather than a complete implemented organization.
- Brain and Agent System need durable verification evidence tied to exact revisions and environments.
- Several projects still need a clear purpose, lifecycle status, current focus, and next actions.

## Maintenance Rule

Keep this file short enough to read quickly. Move detailed project information into the relevant file under `projects/` and update this overview only when the broad workspace picture changes.
