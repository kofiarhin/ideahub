# Zoro Command Center

**Instruction version:** 1.4.0  
**Last updated:** 2026-07-24

## Purpose

This directory stores Zoro's canonical detailed instructions. The live Custom GPT instruction field should contain only the loader in [`BOOTSTRAP.md`](BOOTSTRAP.md).

Zoro starts from the compact generated runtime under [`../runtime/`](../runtime/) and loads detailed canonical sources only when required.

## Runtime And Canonical Sources

Hot path:

- [`../runtime/manifest.json`](../runtime/manifest.json) — runtime version and source fingerprints.
- [`../runtime/zoro.md`](../runtime/zoro.md) — compact startup and operating instructions.

Canonical detailed sources:

- [`../AGENTS.md`](../AGENTS.md)
- [`../AGENT_COORDINATION.md`](../AGENT_COORDINATION.md)
- [`README.md`](README.md)
- [`INSTRUCTIONS.md`](INSTRUCTIONS.md)
- [`../logs/README.md`](../logs/README.md)

The runtime is generated output, not a competing source of truth. Run:

```bash
node scripts/build-agent-runtime.mjs --check
```

to detect source/runtime drift, or:

```bash
node scripts/build-agent-runtime.mjs --write
```

after intentionally updating the runtime templates and canonical instruction sources.

## Startup

A fresh conversation loads:

1. `runtime/manifest.json`
2. `runtime/zoro.md`

If either fails, Zoro falls back to the canonical detailed files in the documented order. If fallback is incomplete, Zoro remains read-only.

## Parallel Orchestration Runtime

The executable bounded worker runtime lives in [`kofiarhin/zoro`](https://github.com/kofiarhin/zoro) under `server/orchestrator/`.

Implemented runtime capabilities:

- request decomposition into a validated dependency graph;
- specialist roles for architecture, backend, frontend, review, QA, research, and documentation;
- bounded fan-out/fan-in execution;
- dependency-aware scheduling;
- repository and path ownership conflict detection;
- partial-result preservation through `Promise.allSettled` behavior;
- structured worker evidence and aggregate run reporting;
- in-memory run lookup.

Current boundaries:

- workers are model tasks, not separate approval authorities;
- isolated Git worktrees, durable run persistence, automatic patch application, merge, and deployment are not implemented;
- Zoro must not claim parallel execution unless the orchestration service actually returned a run record;
- mutating worker output is proposed work or evidence unless primary GitHub readback proves a repository mutation.

The initial service contract is:

- `POST /api/orchestrations`
- `GET /api/orchestrations/:runId`

## Shared Presence

Presence protocol:

- [`../coordination/presence/README.md`](../coordination/presence/README.md)
- [`../coordination/presence/zoro.json`](../coordination/presence/zoro.json)

Before starting or resuming meaningful implementation, Zoro reads the current record, reconciles conflicts, and establishes a 60-minute lease. Zoro has narrow standing direct-`main` authority only for presence transitions in `coordination/presence/zoro.json`; it must use the current blob SHA, avoid force updates, increment the record revision, and verify readback.

Presence represents the supervising Zoro session. Worker-run state belongs in the orchestration runtime and does not become Architect task state, project truth, approval, or completion evidence.

## Indexed Inbox

Primary hot-path inbox:

- [`../inboxes/zoro/open.json`](../inboxes/zoro/open.json)
- [`../inboxes/zoro/messages/`](../inboxes/zoro/messages/)
- [`../inboxes/zoro/archive/`](../inboxes/zoro/archive/)

Return channel:

- [`../inboxes/architect/open.json`](../inboxes/architect/open.json)
- [`../inboxes/architect/messages/`](../inboxes/architect/messages/)
- [`../inboxes/architect/archive/`](../inboxes/architect/archive/)

Legacy compatibility history remains in:

- [`../zoro-inbox.md`](../zoro-inbox.md)
- [`../architect-inbox.md`](../architect-inbox.md)
- [`messages/`](messages/)

New workflow logic must prefer the indexed inbox and load only selected messages.

## Architect Task Lookup

When a message references a run:

1. read `architect/runs/<run-id>/tasks/index.json` when present;
2. read only `architect/runs/<run-id>/tasks/<task-id>.md` when present;
3. fall back to the legacy run `tasks.md` only when detailed content is unavailable from the shard.

Authoritative task state remains in the Architect run. Parallel workers cannot change it.

## Authority

Repository access, orchestration access, and presence are not approval. Zoro must preserve user authority, Architect task state, branch isolation, repository protection, security, verification, operational-log boundaries, and current runtime limitations.

## Installation Verification

After the loader is installed, start a fresh Zoro conversation and ask it to report:

- runtime version;
- repository and branch;
- runtime files loaded;
- fallback files loaded, if any;
- indexed inbox path;
- presence path and interpreted status;
- parallel orchestration capability and current limitations;
- loading failures.

Then test:

```text
Check your Ideas Hub inbox.
```

Do not describe version `1.4.0` as active in the live GPT until the fresh-conversation test passes.
