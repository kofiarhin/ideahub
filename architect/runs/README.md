# Architect Run Artifacts

Run artifacts provide durable operational history for Architect audits, task governance, execution, verification, and resumption. They are not canonical project truth.

## Structure

```text
architect/runs/<run-id>/
├── audit.md
├── tasks.md
├── tasks/
│   ├── index.json
│   └── <task-id>.md
└── report.md
```

## Authority

- `audit.md` records the source fingerprint, portfolio scan, reconciliation, findings, risks, blockers, and task-generation rationale.
- `tasks.md` is the authoritative full task queue and task state.
- `tasks/index.json` is a lightweight retrieval index.
- `tasks/<task-id>.md` is a lightweight selected-task summary.
- `report.md` records execution, verification, feedback, branches, commits, pull requests, checks, deployments, risks, and the exact resume point.

The index and task shards never create competing task state. If they conflict with `tasks.md`, `tasks.md` wins and the retrieval files must be regenerated.

## Run IDs

Use `YYYY-MM-DD-NNN`. Never overwrite a completed historical run.

## Loading

Agents should:

1. resolve the run;
2. read `tasks/index.json` when present;
3. load only the selected task shard;
4. load the matching full section from `tasks.md` before implementation or authoritative state changes;
5. load `audit.md` and `report.md` only when required.

Historical runs without retrieval files continue to use `tasks.md`.
