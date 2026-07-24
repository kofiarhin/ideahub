# Agent Presence

**Last updated:** 2026-07-24

## Purpose

This directory provides advisory, Git-backed presence for agents that share Ideas Hub but run in separate ChatGPT conversations.

The first supported presence record is [`zoro.json`](zoro.json). Architect reads it through the configured GitHub integration when Architect is active. ChatGPT does not continuously push one conversation's state into another.

## Source-Of-Truth Boundary

Presence answers: "What did Zoro most recently say it was doing, and is that lease still current?"

Presence does not:

- approve work;
- assign work;
- change Architect task state;
- prove implementation, verification, merge, deployment, or completion;
- replace indexed inbox messages, Architect run files, project records, operational logs, or repository evidence.

Missing, unreadable, conflicting, or expired presence means `unknown` or `stale`, not proof that Zoro is offline and not automatic authority to reassign work.

## Record

`zoro.json` contains one current session with these fields:

- `schemaVersion` — record format version.
- `agent` — `zoro`.
- `revision` — monotonically increasing presence revision.
- `status` — `working`, `waiting`, `blocked`, or `inactive`.
- `activity` — concise current phase such as `planning`, `implementing`, `verifying`, `waiting_for_approval`, `waiting_for_user`, `waiting_for_tool`, `blocked`, `reported`, or `idle`.
- `sessionId` — unique identifier for the current work session.
- `project`, `repository`, `summary`, `runId`, `taskId`, and `workKey` — overlap and traceability fields when applicable.
- `startedAt`, `updatedAt`, `expiresAt`, and `endedAt` — UTC ISO-8601 timestamps.
- `waitingOn`, `lastAction`, and `lastResult` — concise advisory context without secrets.

## Lease Rules

- A normal lease is 60 minutes.
- Architect treats `working`, `waiting`, or `blocked` as current only while `expiresAt` is later than the current time.
- An expired active record is `stale`.
- `inactive` is released even when an old `expiresAt` remains.
- Zoro cannot run a background heartbeat after its ChatGPT conversation stops. The lease therefore represents recent authenticated activity, not a continuously connected process.

## Zoro Write Workflow

Zoro must:

1. Read the current file and blob SHA before every update.
2. Refuse to overwrite an unexpired different session without reconciling the conflict.
3. Create a unique `sessionId` and mark `working` before the first meaningful implementation write.
4. Renew the lease when the activity changes or when fewer than 15 minutes remain.
5. Mark `waiting` or `blocked` with a concise `waitingOn` reason when applicable.
6. Mark `inactive` with `activity: reported` or `activity: idle` when its work session ends.
7. Increment `revision`, use current UTC timestamps, perform a non-force update, and verify the GitHub readback.
8. Report presence-write failure or uncertainty instead of claiming reliable presence.

Zoro has standing direct-`main` authority only to create or replace `coordination/presence/zoro.json` for these presence transitions. This authority does not extend to any other file or grant task, merge, deployment, migration, security, verification, or completion authority.

## Architect Read Workflow

Architect reads `zoro.json`:

- near the start of project-work conversations;
- before assigning work to Zoro;
- before starting or resuming work that may overlap Zoro;
- before processing matching Zoro reports;
- during `good morning` and `run all tasks` duplicate checks;
- whenever Kofi asks about Zoro's current activity.

Architect compares repository, run ID, task ID, and work key with proposed work. It avoids duplicate implementation while an overlapping lease is current, but still checks indexed inbox messages and primary evidence. Architect is read-only for `zoro.json` unless Kofi explicitly authorizes a repair or reconciliation write.

## Logging

Routine presence start, renewal, waiting, blocked, release, and stale observations are operational coordination noise and are not appended to repository-activity logs. Changes to this protocol, its permissions, schema, or recovery rules are system changes and should be logged after verification.

## Security

Never store secrets, credentials, private keys, tokens, sensitive tool payloads, or unnecessary private conversation content in a presence record.
