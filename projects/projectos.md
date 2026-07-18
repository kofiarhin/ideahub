# ProjectOS

**Last updated:** 2026-07-18

## Snapshot

ProjectOS is an autonomous development operating system for managing the software-development lifecycle across one local workspace containing multiple repositories.

The human provides intent and approvals. ProjectOS coordinates discovery, specification, planning, task generation, execution, verification, reporting, and maintenance through explicit agent roles and persisted operational state.

## Links

- Repository: https://github.com/kofiarhin/projectos
- SSH: `git@github.com:kofiarhin/projectos.git`
- Live: Not applicable for the current local MVP

## Current State

- Lifecycle: Active
- Current phase: Phase 0 — CLI foundation and repository architecture
- Stack: TypeScript, Node.js, Commander, MongoDB/Mongoose, Zod, Pino, Jest, Vitest
- Runtime model: Local, CLI-first, in-process application
- Operational source of truth: MongoDB
- Source-code source of truth: Local filesystem
- AI provider direction: Local Codex CLI through a provider adapter; no OpenAI API key required
- Parallelism target: Up to five builder agents

## Current Focus

Complete and formally close Phase 0 before beginning Domain and Persistence work.

The local foundation currently includes:

- npm workspace monorepo;
- one CLI application under `apps/cli`;
- reusable packages for core, database, workspace, orchestrator, scheduler, builders, verification, context, providers, reporting, and shared utilities;
- `projectos --help` and `projectos --version`;
- a working `projectos doctor` command;
- environment validation;
- lint, type-check, test, build, and CI scripts;
- a committed npm lockfile.

Locally confirmed checks:

- `npm ci` passes;
- lint passes;
- type-check passes;
- all current tests pass;
- `projectos doctor` passes every required readiness check.

Before Phase 1 begins, run the final build and clean-working-tree verification and record the Phase 0 completion report.

## Product Direction

ProjectOS is **CLI-first, not necessarily CLI-only**.

The CLI is the primary workflow and execution interface:

- `projectos init`
- `projectos morning`
- `projectos run`
- `projectos report`
- `projectos request`
- `projectos status`
- `projectos reset`
- `projectos doctor`

A future Mission Control UI may provide administrative oversight for approvals, status, reports, agents, activity, pause, retry, and recovery. The UI must reuse the same application services and must not contain separate orchestration or domain logic.

If a browser-based UI is implemented, it will require a thin local control adapter. That adapter is not the primary product interface and must not become a second implementation of the business rules.

## Core Roles

### Orchestrator

Audits projects, reconciles implementation against approved specifications, generates plans and tasks, prioritizes work, and produces reports. It never writes production code.

### Builder

Implements one assigned task within one project. It does not change approved product scope.

### Verifier

Checks acceptance criteria, automated tests, and implementation evidence before completion.

### Reporter

Generates workspace, project, audit, run, and daily reports from persisted state.

## Decisions

- Manage one local workspace in the MVP.
- Support multiple repositories inside that workspace.
- Keep the CLI as the primary workflow interface.
- Invoke TypeScript application services directly in-process.
- Keep MongoDB as operational memory and the filesystem as source-code state.
- Keep provider-specific behavior behind adapters.
- Use local Codex CLI authentication instead of requiring an AI API key.
- Do not allow filesystem operations outside the registered workspace root.
- Reset and recovery operations must never delete user source code.
- Require verification evidence before marking work complete.
- Preserve idempotency for initialization and morning-audit workflows.
- Implement one approved phase at a time.

## Assumptions

- The MVP runs locally for one operator.
- MongoDB may be local or hosted, but credentials remain in the uncommitted `.env` file.
- The current CLI commands other than `doctor`, help, and version are placeholders until their implementation phases.
- Administrative UI behavior is planned oversight functionality and must be reconciled into the canonical ProjectOS documents before implementation.

## Risks and Open Questions

- The canonical ProjectOS documents currently need to remain synchronized with the clarified “CLI-first with future admin oversight UI” direction.
- The thin local control adapter for a browser UI has not yet been specified.
- Parallel task conflict rules require conservative enforcement before builder execution.
- MongoDB credentials previously visible in a screenshot should be rotated.
- Dependency audit findings should be reviewed without applying forced breaking upgrades.

## Next Actions

1. Run `npm run build` and confirm success.
2. Run `git status` and confirm the working tree is clean.
3. Review `npm audit` findings without using `npm audit fix --force`.
4. Produce and persist the final Phase 0 verification report.
5. Update the canonical ProjectOS documentation to explicitly define CLI-first execution plus future administrative UI oversight before implementing that UI.
6. Begin Phase 1 — Domain and Persistence only after Phase 0 is formally complete.
7. Phase 1 scope: Mongoose models, domain enums, transition validators, repositories/services, activity logging, and database indexes.
