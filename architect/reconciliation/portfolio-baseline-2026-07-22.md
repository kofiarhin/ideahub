# Portfolio Reconciliation Baseline — 2026-07-22

## Purpose

Establish the first evidence-aware portfolio baseline after introducing the Ideas Hub reconciliation contract. This document is an audit artifact, not canonical project truth. Project records and repository-local authority documents remain authoritative within their defined boundaries.

## Source Fingerprint

- Ideas Hub repository: `kofiarhin/ideahub`
- Ideas Hub baseline before framework changes: `0cf5577e2875a54f448351f5ec05801464829948`
- Canonical project index inspected: `PROJECTS.md`, updated 2026-07-22
- Reconciliation contract: `architect/RECONCILIATION.md`
- Audit date: 2026-07-22

## Portfolio Inventory

| Project | Repository | Baseline classification | Reason |
| --- | --- | --- | --- |
| Piano360 | `kofiarhin/piano360` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| Brain | `kofiarhin/brain` | `unverified` | Repository and PR #9 reconciled; authority, tests, deployment, and runtime evidence remain incomplete |
| KareBraids | `kofiarhin/karebraids` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| Amas Kitchen | `kofiarhin/amas-kitchen` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| DevKofi | `kofiarhin/devkofi` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| Memory Sequence Game | `kofiarhin/memory-game` | `unverified` | Index claims merged fixes and passing CI require revision-linked evidence in the project record |
| Ideas Hub | `kofiarhin/ideahub` | `implementation_ahead` | Reconciliation framework is implemented; its own project record has not yet been reconciled to the new contract |
| Forge | Not recorded | `repository_unavailable` | No repository is listed in the canonical project index |
| Zoro | Not recorded | `repository_unavailable` | No repository is listed in the canonical project index |
| Context API | `kofiarhin/context-api` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| Codex Workflow Kit | `kofiarhin/codex-workflow-kit` | `unverified` | Repository-to-authority reconciliation not yet recorded |
| Agent System | `kofiarhin/agent-system` | `unverified` | Detailed implementation and verification claims require revision-linked reconciliation |
| Archon | `kofiarhin/archon` | `documentation_ahead` | Index states an approved MVP specification exists and Phase 1 implementation is next; repository evidence still requires reconciliation |
| Taxify | `kofiarhin/taxify` | `unverified` | Archived; inspect only before explicit reactivation |
| Kflix | `kofiarhin/kflix` | `unverified` | Project overview and current status are not documented |
| Banging Prices | `kofiarhin/banging-prices` | `unverified` | Project overview and current status are not documented |
| MoggOff | `kofiarhin/moggedoff` | `unverified` | Project details and repository naming require reconciliation |
| ProjectOS | `kofiarhin/projectos` | `unverified` | Archived; inspect only before explicit reactivation |

## Confirmed Drift

### Brain

The Brain project record previously instructed Architect to verify PR #9. GitHub evidence shows PR #9 merged into `main` on 2026-07-18 as commit `1302ad67912091ab806f0b08b607e8c14d4f3d93`.

The project record was reconciled to:

- remove PR #9 verification from unfinished work;
- record the merge and exact implementation revision;
- distinguish merged implementation from unverified test, deployment, and runtime state;
- add a requirement ledger for the three PR #9 outcomes; and
- retain only evidence-backed next actions.

## Systemic Findings

1. Most project records do not yet contain reconciliation metadata.
2. The project index contains implementation, CI, deployment, and planning claims that are not consistently tied to repository revisions.
3. Architect task IDs were run-scoped and did not previously require a permanent semantic work identity.
4. Task generation did not explicitly require searches of historical runs plus open and merged pull requests before promotion to `ready`.
5. A merged pull request could be mistaken for test, deployment, or runtime verification unless evidence categories remain separate.
6. Archived and repository-unavailable projects need hard guards against accidental task generation.

## Controls Implemented

- Added `architect/RECONCILIATION.md`.
- Added project reconciliation metadata and supported status definitions.
- Added requirement-ledger statuses and evidence rules.
- Added permanent `work_key` and `requirement_key` conventions.
- Added duplicate and supersession rules.
- Added a mandatory readiness gate to Architect documentation and `run all tasks`.
- Added `scripts/validate_ideahub.py`.
- Added GitHub Actions validation for Python compilation and repository validation.
- Completed the Brain pilot reconciliation.

## Remaining Portfolio Work

The baseline intentionally does not claim that uninspected repositories are aligned. Each active project still needs a repository-specific reconciliation that records:

- default-branch revision;
- authority document and revision;
- open and merged relevant pull requests;
- requirement-to-code evidence;
- test, CI, deployment, and runtime evidence where applicable;
- stale or duplicate next actions; and
- explicit conflicts requiring approval.

Until that evidence exists, Architect must treat the affected project as `unverified`, `documentation_ahead`, `repository_unavailable`, or `conflicted` rather than generate speculative `ready` implementation tasks.