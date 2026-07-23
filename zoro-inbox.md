# Zoro Inbox

**Last updated:** 2026-07-23

This file is the lightweight communication inbox between Kofi and Zoro.

It is not a replacement for:

- `CONTEXT.md` — workspace briefing
- `PROJECTS.md` — canonical project index
- `projects/<project>.md` — durable project context
- `architect/runs/<run-id>/tasks.md` — governed execution state

## How Kofi Uses This File

Add a new message under **Open Messages** using the template below, then tell Zoro:

```text
Check your Ideas Hub inbox.
```

## How Zoro Must Process Messages

Before processing an inbox message, Zoro must:

1. Read `AGENTS.md`.
2. Read `CONTEXT.md`.
3. Read `PROJECTS.md`.
4. Read the relevant `projects/<project>.md` file when a project is named.
5. Check existing branches, pull requests, Architect tasks, and repository specifications when the message requests implementation.

Inbox messages are instructions or requests, but they are not automatically proof of implementation, verification, deployment, or completion.

Zoro must not treat a message as authorization to merge, deploy, change `main`, approve security-sensitive work, or bypass Architect approval gates unless that authority is stated explicitly.

Zoro should respond in chat first. Durable repository changes should use an isolated branch and pull request unless direct `main` work is explicitly authorized.

## Message Template

```md
## ZORO-MSG-YYYY-MM-DD-NNN

- Status: new
- Project: <project name or workspace>
- Type: question | review | task | decision | context-correction
- Priority: low | normal | high | urgent
- Approval: read-only | discovery-approved | implementation-approved
- Created: YYYY-MM-DD

### Message

<What Zoro should understand or do>

### Constraints

- <Constraint 1>
- <Constraint 2>

### Expected Response

<What Zoro should report back>
```

## Open Messages

## ZORO-TASK-2026-07-23-001 — Review Context API pull request #2 readiness

- **ID:** `ZORO-TASK-2026-07-23-001`
- **From:** Architect
- **Assigned to:** Zoro
- **Project:** Context API
- **Repository:** `kofiarhin/context-api`
- **Pull request:** `#2` — https://github.com/kofiarhin/context-api/pull/2
- **Status:** `ready`
- **Priority:** high

### Objective

Perform a governed, evidence-based review of Context API pull request #2 and determine whether the pull request is ready to merge. Produce a durable readiness report in Ideas Hub without modifying the Context API repository, merging, or deploying anything.

### Scope

- Review pull request #2 at its current head revision, including its description, commits, changed files, diff, review state, mergeability, and CI/status checks.
- Assess the implementation against the approved Context API and GitHub Gateway specifications.
- Assess the changed and existing tests for meaningful regression coverage, including query-based deletion, JSON-body fallback compatibility, query/body precedence, non-default branch forwarding, exact blob-SHA optimistic concurrency, stale-SHA conflicts, workflow-path blocking, authentication, validation, and safe error behavior.
- Assess security implications, including URL/query logging exposure, secret handling, branch protection, workflow-file restrictions, repository authorization, destructive-write safeguards, and whether any existing policy boundary was weakened.
- Assess compatibility with the current Zoro Action schema, especially the maintained `docs/openapi/zoro-action.yaml` deletion contract and GPT Builder constraints.
- Inspect available verification evidence and distinguish source inspection, automated CI evidence, locally executed command evidence, and unverified claims.
- Check Ideas Hub Architect runs, inbox tasks, repository branches, open and merged pull requests, and relevant project records for duplicate, active, completed, or superseding work.
- Determine one readiness outcome: `ready to merge`, `not ready to merge`, or `blocked pending evidence`, with explicit reasons and required next actions.
- Create the durable readiness report in Ideas Hub on an isolated branch and open a pull request into `main`.

### Out of Scope

- Do not modify `kofiarhin/context-api` in any way.
- Do not implement, amend, rebase, or repair pull request #2.
- Do not update the Context API Action schema.
- Do not run a deployment or change Heroku configuration.
- Do not merge, close, approve, or otherwise mutate Context API pull request #2.
- Do not perform the live deletion smoke test or remove the disposable branch or file.
- Do not update durable Context API or Zoro project state as though readiness, merge, deployment, or runtime verification has already been completed.

### Evidence Architect Reviewed

- Ideas Hub governance and context: `AGENTS.md`, `AGENT_COORDINATION.md`, `CONTEXT.md`, `PROJECTS.md`, `projects/context-api.md`, `projects/zoro.md`, `zoro-inbox.md`, and `architect/README.md`.
- Relevant Architect run: `architect/runs/2026-07-22-001/audit.md` and `tasks.md`; the run is completed, contains only ProjectOS tasks, and does not duplicate this Context API PR review assignment.
- Context API pull request #2 metadata and diff at head `654ebbc1bf8ada7b2ed339f342859204c6e88505`, based on `main` revision `bf378b82ed04c88152c3cbb7550a590e63a19601`.
- Pull request state observed by Architect: open, non-draft, mergeable, four commits, four changed files, 172 additions, and 2 deletions.
- Changed files observed: `src/middleware/validateGithub.js`, `src/routes/v1/github.js`, `tests/integration/githubFileDeletionRoute.test.js`, and `tests/unit/githubFileDeletion.test.js`.
- Pull request description explicitly states shell verification was unavailable and does not claim the listed test, lint, formatting, or gateway verification commands passed.
- Commit combined-status inspection returned no status checks for the PR head.
- Approved GitHub Gateway specification requires authenticated deletion, optimistic concurrency, workflow-file blocking, no branch-protection bypass, safe secret handling, and deterministic automated tests.
- Current maintained Zoro Action schema still defines `DELETE /api/v1/github/files` with a required JSON request body, while pull request #2 introduces query-parameter transport with JSON-body fallback.
- Existing Ideas Hub project records classify pull request #2 as implemented but unverified and identify schema reconciliation plus clean verification as outstanding.

### Acceptance Criteria

- A durable report identifies the exact PR head SHA reviewed and records whether the head changed during the review.
- The report maps each material implementation behavior to code and test evidence, including query transport, fallback behavior, precedence, validation, controller/service forwarding, concurrency, workflow blocking, and error handling.
- The report evaluates whether the test suite adequately covers both the new transport and compatibility behavior, and names every material missing test or assertion.
- The report evaluates security and policy compatibility without reproducing credentials, tokens, private keys, or other secrets.
- The report compares the implementation with the current maintained Action schema and clearly states whether schema drift blocks merge readiness or only blocks later deployment/runtime verification.
- The report records all available CI/status checks and executed verification commands with traceable evidence.
- The report does not claim any command or test passed unless Zoro has direct CI logs, workflow results, or exact command output proving it.
- The report records duplicate and supersession checks and identifies any overlapping active work.
- The report gives one explicit readiness decision: `ready to merge`, `not ready to merge`, or `blocked pending evidence`.
- For every blocking or non-blocking finding, the report states the rationale, severity, owner, and exact next action.
- The Ideas Hub change is isolated to the readiness report required by this task, uses a dedicated branch, and is submitted through a pull request into `main`.

### Verification Requirements

- Re-fetch pull request #2 immediately before finalizing the report and record the final head SHA, state, mergeability, changed files, commit count, reviews, unresolved review threads, and status checks.
- Inspect each changed file and the relevant unchanged validation, controller, service, schema, authentication, error-handling, and test-helper code needed to validate behavior end to end.
- Inspect the approved GitHub Gateway specification, implementation plan, release checklist, maintained Action schema, repository scripts, and CI workflow definitions relevant to readiness.
- Record the exact verification evidence available. Where Zoro cannot execute shell commands, mark those commands as not run and treat the missing evidence as a readiness factor rather than inferring success.
- Validate that no live GitHub request is made by automated tests and that no secret values are present in source, reports, logs, or test fixtures.
- Confirm the readiness report branch changes only the intended Ideas Hub report file or files authorized by this task.
- Open the Ideas Hub pull request into `main` and include the report path, reviewed PR head SHA, readiness decision, verification evidence, and remaining blockers in its description.

### Security Constraints

- Never read, print, copy, store, rotate, or modify secret values, GitHub App private keys, installation tokens, Bearer credentials, Heroku config values, or environment secrets.
- Do not invoke destructive Context API or GitHub Gateway operations.
- Do not weaken or recommend bypassing branch protection, optimistic concurrency, workflow-file blocking, authentication, repository authorization, or safe error handling.
- Treat query-string values as potentially retained in infrastructure logs and assess whether documented non-secret field constraints remain sufficient.
- Preserve the rule that `.github/workflows/*` writes and deletions are prohibited.

### Merge and Deployment Authority

Zoro has no authority under this task to merge, approve, close, rebase, or modify Context API pull request #2; write to any Context API branch; deploy any revision; update the live Zoro Action; or perform cleanup. The readiness decision is advisory evidence for a later explicitly authorized merge or deployment workflow. Zoro may create only the isolated Ideas Hub branch and pull request required for the readiness report.

### Required Final Report

Report back with:

- task ID;
- readiness decision and concise rationale;
- Context API PR #2 head SHA reviewed;
- Ideas Hub readiness report path;
- Ideas Hub branch name;
- Ideas Hub commit SHA;
- Ideas Hub pull request number and URL;
- CI/status checks and command evidence inspected;
- blocking findings, non-blocking risks, and exact next actions;
- explicit confirmation that Context API was not modified and nothing was merged or deployed.

### Exact Next Action

Read the required Ideas Hub governance and project context, then re-fetch `kofiarhin/context-api` pull request #2 and begin an evidence-only readiness review at its current head SHA. Do not modify Context API. Create the durable readiness report on a new isolated Ideas Hub branch and open a pull request into `main`.

## ZORO-MSG-2026-07-23-001

- Status: new
- Project: Zoro
- Type: review
- Priority: normal
- Approval: read-only
- Created: 2026-07-23

### Message

Confirm that you can read this Ideas Hub inbox and explain how you will use it when Kofi says, "Check your Ideas Hub inbox."

### Constraints

- Do not modify any repository.
- Do not create branches, commits, pull requests, or tasks.
- Do not mark this message complete.

### Expected Response

Summarize the inbox workflow and confirm which Ideas Hub files you will read before processing future project-specific messages.