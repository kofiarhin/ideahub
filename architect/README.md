# Architect Command System

**Instruction version:** 1.1.0  
**Last updated:** 2026-07-23

## Purpose

Ideas Hub stores Architect's canonical detailed instructions, command workflows, durable run artifacts, indexed communication, and operational logs.

The live Architect Project instruction field should contain only [`BOOTSTRAP.md`](BOOTSTRAP.md). Architect now starts from the compact generated runtime under [`../runtime/`](../runtime/).

## Runtime And Canonical Sources

Hot path:

- [`../runtime/manifest.json`](../runtime/manifest.json)
- [`../runtime/architect.md`](../runtime/architect.md)

Canonical detailed sources:

- [`../AGENTS.md`](../AGENTS.md)
- [`../AGENT_COORDINATION.md`](../AGENT_COORDINATION.md)
- [`README.md`](README.md)
- [`INSTRUCTIONS.md`](INSTRUCTIONS.md)
- [`../logs/README.md`](../logs/README.md)

The runtime is generated output. Use:

```bash
node scripts/build-agent-runtime.mjs --check
```

to detect drift, and `--write` after intentionally updating both canonical sources and runtime templates.

## Startup

A fresh conversation loads:

1. `runtime/manifest.json`
2. `runtime/architect.md`

Fallback loads the five canonical detailed sources. Incomplete runtime and fallback means read-only operation.

## Command Registry

| Canonical command | Approved aliases | Workflow |
| --- | --- | --- |
| `good morning` | `morning audit` | [`commands/good-morning.md`](commands/good-morning.md) |
| `run all tasks` | `resume all tasks`, `continue all tasks` | [`commands/run-all-tasks.md`](commands/run-all-tasks.md) |

Only load the matching workflow.

## Indexed Communication

- [`../inboxes/zoro/open.json`](../inboxes/zoro/open.json)
- [`../inboxes/zoro/messages/`](../inboxes/zoro/messages/)
- [`../inboxes/architect/open.json`](../inboxes/architect/open.json)
- [`../inboxes/architect/messages/`](../inboxes/architect/messages/)

Legacy root inbox files remain cold compatibility history.

## Run Artifacts

Each run retains:

```text
architect/runs/<run-id>/
├── audit.md
├── tasks.md
├── tasks/
│   ├── index.json
│   └── <task-id>.md
└── report.md
```

`tasks.md` remains authoritative full detail. The task index and shards are a generated retrieval layer and must not create competing task state.

## Reconciliation

Before promotion to `ready`, verify authority, revisions, evidence, duplicates, work key, requirement key, acceptance criteria, verification requirements, and approvals.

A message, log entry, branch, commit, or pull request is not task completion evidence.

## Command Boundaries

`good morning` writes only its permitted run audit/task artifacts and matching generated task retrieval files.

`run all tasks` executes only eligible `ready` work and may perform only its documented run, indexed communication, repository, log, and verified context updates.

## Installation Verification

After installing the loader, start a fresh Architect conversation and ask it to report:

- runtime version;
- repository and branch;
- runtime files loaded;
- fallback files loaded, if any;
- command registry;
- indexed inbox paths;
- loading failures.

Do not describe version `1.1.0` as active in the live Project until this test passes.
