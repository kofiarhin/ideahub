# Ideas Hub Reconciliation Contract

## Purpose

This contract keeps Ideas Hub records aligned with repository authority documents, implementation, pull requests, tests, CI, and Architect run history. It prevents stale project notes from generating duplicate or already-completed work.

## Authority Order

When sources disagree, resolve them in this order:

1. The user's latest explicit instruction.
2. An approved Shared Understanding Handoff.
3. Current implementation on the repository default branch.
4. Approved repository-local ORD, PRD, specification, or implementation plan.
5. The current Ideas Hub project record.
6. Other project documentation.
7. Architect run history.
8. Documented assumptions.

Code proves what currently exists. Approved authority documents define what should exist. The Ideas Hub records the reconciled relationship and must not duplicate either source in full.

## Project Reconciliation Metadata

A reconciled project record contains a `## Reconciliation` section with this exact field set:

```yaml
repository: owner/repository
default_branch: main
authority_document: path/to/authority.md | not_documented
authority_revision: git-sha | not_available
implementation_revision: git-sha
last_reconciled: YYYY-MM-DD
reconciliation_status: aligned | documentation_ahead | implementation_ahead | conflicted | unverified | repository_unavailable
```

### Status meanings

- `aligned` — authority documents, implementation evidence, and the project record agree.
- `documentation_ahead` — approved requirements exist but verified implementation is missing or incomplete.
- `implementation_ahead` — verified implementation exists but authority documentation or the project record has not caught up.
- `conflicted` — material sources disagree and user resolution is required.
- `unverified` — evidence is incomplete or has not been checked recently enough.
- `repository_unavailable` — the repository cannot be inspected.

Only evidence-backed fields may be recorded. Use `not_documented` or `not_available` instead of inventing values.

## Requirement Ledger

Projects with implementation work should maintain a concise requirement ledger in the project record or link to a repository-local ledger.

| Requirement ID | Requirement | Authority | Status | Implementation evidence | Verification |
| --- | --- | --- | --- | --- | --- |
| `PROJECT-AREA-001` | Concise requirement | `docs/PRD.md#section` | `approved_missing` | None found | Pending |

Allowed requirement statuses:

- `implemented_verified`
- `implemented_unverified`
- `approved_missing`
- `partially_implemented`
- `superseded`
- `rejected`
- `conflicted`
- `not_applicable`

Architect may generate implementation work only for a verified gap such as `approved_missing` or `partially_implemented`. Ambiguous requirements remain discovery or approval work.

## Permanent Work Identity

Every Architect task must include:

```yaml
task_id: <run-id>-<project-slug>-TNNN
work_key: <project-slug>:<stable-semantic-key>
requirement_key: <project-slug>:<requirement-id> | not_applicable
duplicate_of: null | <task-id-or-work-key>
supersedes: []
```

`task_id` identifies one run occurrence. `work_key` identifies the durable unit of work across every run.

Before creating or promoting a task, search:

- current and historical Architect task queues;
- project `Next Actions` and requirement ledgers;
- open pull requests;
- merged pull requests;
- relevant commits and implementation evidence.

Do not create or promote a task when the same `work_key` is active, completed, merged, or otherwise satisfied. Record it as `duplicate_of`, `superseded`, or `completed` with evidence instead.

## Readiness Gate

A task may become `ready` only when all applicable checks pass:

- repository and default branch are known;
- audited implementation revision is recorded and still current;
- approved source and source revision are recorded;
- requirement or change request is explicit;
- implementation gap is verified;
- no equivalent active or completed `work_key` exists;
- no equivalent open or merged pull request satisfies the work;
- acceptance criteria and verification requirements are explicit;
- authority and implementation are not materially conflicted;
- required approval, including direct-`main` authorization, is recorded.

Route failed checks as follows:

- unclear behavior or evidence → `needs_discovery`;
- missing or inadequate authority document → `needs_spec`;
- product, scope, migration, security, lifecycle, or direct-`main` decision → `needs_approval`;
- external dependency or inaccessible evidence → `blocked`.

## Evidence Rules

Implementation claims require traceable evidence such as:

- default-branch commit SHA;
- merged pull request;
- passing test, build, or CI run;
- deployment or manual verification evidence.

A merged pull request proves merge state, not deployment or runtime correctness. Record only what the evidence supports.

## Project Record Maintenance

After verified work:

1. Move completed work out of `Current Focus` and `Next Actions`.
2. Record the verified result under `Current State` or a concise `Accomplished` section.
3. Add evidence links or identifiers.
4. Update reconciliation metadata and `Last updated`.
5. Preserve unresolved conflicts under `Open Questions` or `Assumptions`.
6. Do not copy full ORD, PRD, or specification text into the Ideas Hub.

## Validation

Run:

```bash
python scripts/validate_ideahub.py
```

The validator checks reconciliation field structure, supported statuses, task identity fields, duplicate active `work_key` values, and common stale-action contradictions that can be detected from repository text.