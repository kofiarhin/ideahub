# Operational Logs

**Last updated:** 2026-07-24

## Purpose

The `logs/` directory is the shared operational memory layer for Ideas Hub. It preserves a concise chronological history of meaningful repository activity, verified system changes, and reusable evidence-supported learnings.

Logs support investigation, reporting, reconciliation, and future work. They do not replace current project truth, repository evidence, Architect task state, agent communication, or advisory presence.

## Source-of-Truth Boundaries

- `projects/<project>.md` stores verified durable project knowledge.
- `architect/runs/<run-id>/tasks.md` stores authoritative governed task state.
- `architect/runs/<run-id>/report.md` stores authoritative Architect execution and verification reporting.
- Indexed Zoro and Architect inboxes carry agent assignments, reports, and feedback.
- `coordination/presence/zoro.json` stores advisory recent Zoro activity and lease state.
- Source repositories, pull requests, checks, releases, and deployment systems remain the primary evidence for repository and runtime state.
- `logs/` stores chronological supporting evidence and reusable lessons.

A presence record or log entry never grants approval, changes task state, proves deployment, or marks work completed by itself.

## Categories

### [`repository-activity/`](repository-activity/)

Append-only monthly journals of meaningful repository writes and state transitions, including:

- branch creation or deletion;
- meaningful commits;
- pull request creation, material updates, closure, or merge;
- CI transitions to passed or failed when relevant to active work;
- releases, deployments, rollbacks, and post-deployment verification;
- repository configuration changes;
- verified security remediation.

Do not log read-only inspection, searches, repeated unchanged status checks, routine presence start/renewal/waiting/blocked/release transitions, ordinary comments, or other noise.

### [`learnings/`](learnings/)

Monthly records of reusable lessons supported by evidence from completed or verified work. Examples include repository conventions, recurring failure patterns, successful verification methods, coordination lessons, and implementation constraints.

Do not store raw ideas, unsupported guesses, or secrets.

### [`system-changes/`](system-changes/)

Monthly records of verified changes to Zoro, Architect, Ideas Hub governance, command workflows, Context API coordination, presence protocol, logging policy, and other shared operating systems.

## Read Rules

- Zoro loads this index at the start of every fresh conversation after its four canonical instruction files.
- Architect loads this index before repository execution, Zoro-report processing, reconciliation, or log maintenance.
- Load only the monthly log files relevant to the active request, date range, project, repository, task, or system component.
- Logs may be used to discover missing or stale records, but important claims must be checked against primary evidence when practical.

## Repository Activity Write Rule

After a successful meaningful repository write or state transition performed by Zoro or Architect, append a verified entry to the current UTC monthly file under `logs/repository-activity/`.

The append is part of the authorized repository workflow when the underlying repository action is authorized and the active workflow permits Ideas Hub maintenance. If a command explicitly forbids the log write, record the exact missing entry in its authoritative report instead.

Write the entry only after confirming the action succeeded. Never pre-log intended work.

For a series of tightly related writes performed as one atomic operation, one summary entry may cover the operation. Separate later state transitions such as CI completion, merge, deployment, rollback, or runtime verification require separate entries.

Operational-log maintenance commits are not recursively logged. Mailbox, report-only, and routine presence-only updates are also excluded unless they represent a material shared-system change, recovery incident, or protocol correction.

## Required Repository Activity Fields

Use this structure when applicable:

```md
## YYYY-MM-DD HH:MM UTC — <event>

- **Repository:** `owner/name`
- **Project:** <project or Not documented>
- **Action:** <branch created, commit pushed, PR opened, CI passed, merged, deployed, etc.>
- **Actor:** <Zoro, Architect, Kofi, or verified GitHub actor>
- **Authority:** <user instruction, approved task, assignment ID, or workflow>
- **Branch:** `<branch>`
- **Commit:** `<sha>`
- **Pull request:** <number or URL>
- **Result:** <succeeded, failed, open, merged, deployed, verified, etc.>
- **Evidence:** <GitHub or operational readback>
- **Related run:** <run ID when applicable>
- **Related task:** <task ID when applicable>
- **Work key:** <work key when applicable>
- **Unverified:** <remaining uncertainty or None>
```

Omit fields that genuinely do not apply. Preserve identifiers whenever available.

## Reconciliation Of External Activity

Actions performed manually in GitHub or by tools that do not follow this policy are not guaranteed to be logged immediately.

When Zoro or Architect later discovers a meaningful unlogged event:

1. verify it against GitHub or operational evidence;
2. check that an equivalent entry does not already exist;
3. append a clearly labelled reconciled historical entry;
4. distinguish the original actor from the agent that recorded it;
5. preserve the event time and the later detection time when available.

## Feedback Loop

Repository logs and presence are not mailboxes.

For Architect-governed work:

1. Architect checks current Zoro presence and assigns approved `ready` work through the indexed Zoro inbox.
2. Zoro acknowledges, establishes or reconciles presence, and performs only authorized work.
3. Zoro appends confirmed repository activity and reports progress, blockers, approval requests, or implementation evidence through the indexed Architect inbox; routine presence-only transitions are not logged.
4. Architect matches the report to the message ID, run ID, task ID, work key, and applicable presence session.
5. Architect independently verifies primary repository and operational evidence, using presence and logs only as supporting context.
6. Architect updates authoritative run files when permitted.
7. Architect sends acceptance, rejection, questions, or follow-up instructions through the indexed Zoro inbox.
8. Zoro updates or releases presence as the work session changes.
9. The loop repeats until Architect verifies completion and required durable updates succeed.

## Append-Only And Correction Rules

- Add new entries at the end of the applicable monthly file.
- Do not silently rewrite history.
- Correct a material error with a new correction entry that references the original entry.
- Avoid duplicate entries for unchanged states.
- Do not recursively log commits whose only purpose is appending or correcting operational logs.
- Use UTC monthly files named `YYYY-MM.md`.
- Create the next monthly file when the first qualifying event occurs.

## Security And Quality

Never log:

- secrets, tokens, passwords, private keys, credentials, or sensitive values;
- unsupported completion, deployment, or verification claims;
- raw private content that is not necessary for traceability;
- speculative accusations or unverified security claims;
- routine API calls, presence heartbeats, or read-only noise.

Keep facts, evidence, inference, assumptions, and recommendations distinct.
