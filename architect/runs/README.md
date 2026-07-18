# Architect Run Artifacts

## Purpose

Run artifacts provide durable operational history for Architect audits and execution. They support resumption, review, traceability, and reporting; they are not canonical project truth. Canonical project context remains in `PROJECTS.md`, relevant `projects/*.md` records, and repository-local authority documents.

## Run IDs

Each run directory uses `YYYY-MM-DD-NNN`, where `NNN` is a zero-padded sequence for that date. For example: `2026-07-18-001`.

## Runtime Structure

```text
architect/runs/<run-id>/
├── audit.md
├── tasks.md
└── report.md
```

- `audit.md` records the source fingerprint, portfolio scan, audit evidence, reconciliation, findings, risks, blockers, and task-generation rationale.
- `tasks.md` is the ordered durable task queue, including task status, evidence, approvals, verification requirements, and outcome.
- `report.md` records execution state, approvals, branches, commits, pull requests, verification, Ideas Hub updates, risks, and the exact resume point.

Completed historical runs must not be overwritten. No sample run in this repository is presented as real execution evidence; the first operational artifact is created only when an Architect command performs a real run.
