# Architect Task Queue — 2026-07-19-002

## Queue Summary

| Status | Count |
| --- | ---: |
| `ready` | 3 |
| `needs_approval` | 1 |
| `blocked` | 1 |
| `skipped` | 1 |

## 2026-07-19-002-agent-system-T001 — Deliver v1.0.1 MVP safety hardening

- **Project:** Agent System
- **Repository:** `kofiarhin/agent-system`
- **Task type:** Security, reliability, tests, CI, and documentation
- **Priority:** Critical
- **Priority rationale:** Addresses backup durability, rollback correctness, unsafe-path defenses, manifest integrity, and missing Windows CI evidence.
- **Status:** `ready`
- **Source document:** `projects/agent-system.md`; `docs/PRD.md`
- **Source section or requirement:** Approved v1.0.1 MVP Hardening Task; FR-9 through FR-16; MVP Hardening Backlog
- **Audited revision:** Ideas record `5e28ff371c9e144be57aa536ab745a410d2546df`; PRD `564604563e392654e575155ad90e960ae2e74f36`; repository head `a341d8ed5fe24c233fa4181402a2b95029df1e69`
- **Evidence:** The project record marks the nine-part backlog approved and `ready`; the PRD still lists the corresponding limitations as outstanding.
- **Scope:** Persist and validate backup manifests before target modification; add verified restore rollback; enforce restore destination identity; harden runtime path validation including traversal, sibling-prefix, target reparse-point, and parent reparse-point defenses; validate required manifest fields and backup-directory containment; correct replacement wording; add Windows PowerShell 5.1 and current PowerShell 7 CI; add targeted failure tests; align PRD, installation, and operations documentation.
- **Out of scope:** Transaction journals, multi-runtime transactions, recovery engines, dashboards, enterprise deployment, signing, retention management, or unrelated runtime expansion.
- **Dependencies:** Existing v1.0.0 scripts, adapters, temporary-directory test harness, and approved PRD.
- **Required approval:** None; direction and acceptance criteria are already approved. Breaking or materially expanded scope requires new approval.
- **Acceptance criteria:** All acceptance criteria under the nine approved hardening items and Definition of Done in `projects/agent-system.md` pass.
- **Verification required:** Deterministic build check; strict verification; complete test suite; targeted failure-path tests; Windows PowerShell 5.1 and PowerShell 7 GitHub Actions; no access to real runtime directories; documentation review; isolated branch and pull request.
- **Branch:** Not created
- **Pull request:** Not created
- **Verification evidence:** Pending
- **Outcome:** Pending

## 2026-07-19-002-brain-T002 — Verify merged Brain PR #9 and reconcile drift

- **Project:** Brain
- **Repository:** `kofiarhin/brain`
- **Task type:** Post-merge verification and context reconciliation
- **Priority:** High
- **Priority rationale:** The merged changes affect shared rendering, Dashboard failure states, and Europe/London date calculations; the original PR environment did not execute the suite.
- **Status:** `ready`
- **Source document:** `projects/brain.md`; GitHub PR #9
- **Source section or requirement:** Current Focus and Next Actions; PR #9 test and audit notes
- **Audited revision:** Project record `695a9926b337a4912f7fae484541d00997a2460d`; merge commit `1302ad67912091ab806f0b08b607e8c14d4f3d93`
- **Evidence:** PR #9 is merged while the durable record still says it needs verification. The PR states its test suite was not run in the original environment.
- **Scope:** Revalidate current `main`; install dependencies cleanly; run relevant client tests, lint, type/build checks; add only missing focused regression coverage needed to verify structured List rendering, Dashboard loading/error/empty states, and Europe/London date/time boundaries; document evidence and reconcile the stale project record only after verification.
- **Out of scope:** New Brain features, product redesign, write-enabled chat, unrelated refactoring, or direct production data changes.
- **Dependencies:** Dependency-capable checkout and current repository instructions.
- **Required approval:** None for verification and minimal missing regression tests. Product behavior changes require approval.
- **Acceptance criteria:** Current `main` passes the repository’s required checks; focused behaviors are covered and pass; no `[object Object]` rendering regression; Dashboard states are visible; Europe/London boundary behavior is verified; durable project context is updated only after verified evidence.
- **Verification required:** Relevant Vitest suite, lint, build/type checks, clean checkout evidence, and review of merged behavior.
- **Branch:** Not created
- **Pull request:** Not created
- **Verification evidence:** Pending
- **Outcome:** Pending

## 2026-07-19-002-devkofi-T003 — Add server CI coverage for backend changes

- **Project:** DevKofi
- **Repository:** `kofiarhin/devkofi`
- **Task type:** CI and backend regression hardening
- **Priority:** High
- **Priority rationale:** Carry-forward evidence indicates backend Telegram behavior can change without root/server Jest validation in the current workflow.
- **Status:** `ready`
- **Source document:** Prior run `2026-07-19-001` audit and task queue
- **Source section or requirement:** DevKofi server CI finding
- **Audited revision:** Carry-forward from audited repository head `3c42e10712b3c60a0ee24e855823039be027e617`; must be revalidated before mutation
- **Evidence:** Prior audit found server changes on `main` while workflow validation was client-path focused.
- **Scope:** Revalidate repository state; add CI coverage for root/server Jest checks on backend-relevant changes; add minimal controller-level best-effort notification integration coverage where supported by current authority documents.
- **Out of scope:** Production Telegram credential configuration, broader notification redesign, unrelated client work, or deployment activation.
- **Dependencies:** Revalidation of current workflow and repository test commands.
- **Required approval:** None if the prior approved scope remains current; pause if authority documents or implementation materially changed.
- **Acceptance criteria:** Backend-only changes trigger appropriate server checks; relevant server tests pass in CI; notification failure behavior remains best-effort and does not break the primary request path.
- **Verification required:** Jest/server checks, workflow trigger validation, lint/build checks required by the repository, isolated branch and pull request.
- **Branch:** Not created
- **Pull request:** Not created
- **Verification evidence:** Pending
- **Outcome:** Pending

## 2026-07-19-002-archon-T004 — Approve the first isolated Phase 1 implementation slice

- **Project:** Archon
- **Repository:** `kofiarhin/archon`
- **Task type:** Scope and approval
- **Priority:** High
- **Priority rationale:** Phase 1 is the next approved product phase, but the current project record explicitly requires creation and approval of the first implementation task before execution.
- **Status:** `needs_approval`
- **Source document:** `projects/archon.md`; approved `docs/specs/IMPLEMENTATION_PLAN.md`
- **Source section or requirement:** Current Focus and Next Actions
- **Audited revision:** Project record `497c0b9a8cc35b7c8791162cfea18a6750ac5acb`; repository head `f89140062b069487c35319b525cc15aae100dc8b`
- **Evidence:** Approved authority documents exist, but the project record requires the first Phase 1 implementation task to be created and approved.
- **Scope:** Define one reviewable first slice, recommended as workspace/application boundaries plus baseline formatting, linting, type-checking, tests, build, and CI; preserve later configuration, Docker services, and database work as separate tasks unless the approved plan explicitly makes them inseparable.
- **Out of scope:** Full Phase 1 implementation, authentication, AI workflows, artifact generation, production hosting, billing, or post-MVP work.
- **Dependencies:** User approval of normalized task scope and acceptance criteria.
- **Required approval:** Explicit approval required before status can become `ready`.
- **Acceptance criteria:** A single implementation-ready task maps to exact approved plan sections, has clear repository boundaries, verification commands, branch/PR strategy, and no unresolved scope conflict.
- **Verification required:** Approval recorded in the run before implementation.
- **Branch:** Not created
- **Pull request:** Not created
- **Verification evidence:** Pending
- **Outcome:** Pending

## 2026-07-19-002-memory-sequence-game-T005 — Deploy and complete production acceptance

- **Project:** Memory Sequence Game
- **Repository:** `kofiarhin/memory-game`
- **Task type:** Deployment and manual acceptance
- **Priority:** Medium
- **Priority rationale:** MVP and CI are complete, but production hosting and representative accessibility/device behavior remain unverified.
- **Status:** `blocked`
- **Source document:** `projects/memory-sequence-game.md`
- **Source section or requirement:** Remaining Risks and Next Actions
- **Audited revision:** Project record `4be662b8fad08fe062032a121365e88a4f747986`; repository head `3073edad00666fd8538af68ada4727639050aa16`
- **Evidence:** Record states production hosting is unverified, manual testing remains, and no lockfile is committed.
- **Scope:** Create Vercel deployment from `main`; verify production build and routing; test representative mobile/desktop, keyboard, screen-reader, and reduced-motion behavior; choose and implement a deliberate dependency-locking workflow; record production URL only after verification.
- **Out of scope:** Backend, accounts, cloud saves, gameplay redesign, or post-MVP feature selection.
- **Dependencies:** Vercel project access and a suitable manual browser/device/accessibility test environment.
- **Required approval:** No product-scope approval required for the recorded deployment direction; dependency-locking choice must follow repository conventions.
- **Acceptance criteria:** Production URL is live and verified; required manual checks are recorded; CI remains passing; dependency installation is reproducible or the deliberate alternative is documented.
- **Verification required:** Production smoke test, representative device/accessibility checklist, CI/build confirmation, and URL evidence.
- **Branch:** Not created
- **Pull request:** Not created
- **Verification evidence:** Pending
- **Outcome:** Blocked on external deployment and manual-test access

## 2026-07-19-002-projectos-T006 — Preserve archived credential risk without execution

- **Project:** ProjectOS
- **Repository:** `kofiarhin/projectos`
- **Task type:** Security risk preservation
- **Priority:** Critical but deferred
- **Priority rationale:** Previously recorded credential exposure is material, but the user explicitly archived the project and deferred remediation until reactivation.
- **Status:** `skipped`
- **Source document:** `projects/projectos.md`
- **Source section or requirement:** Decisions; Risks and Open Questions; Next Actions
- **Audited revision:** `4918a545a498b4575f10f1dd1abe6b2e715f9e20`
- **Evidence:** Project record says to ignore the credential-rotation task while archived and require a fresh security review before reactivation.
- **Scope:** Preserve the finding and require reassessment upon reactivation.
- **Out of scope:** Credential rotation, repository changes, Phase 1 work, or verification while archived.
- **Dependencies:** Explicit project reactivation.
- **Required approval:** Reactivation approval required before any work.
- **Acceptance criteria:** No mutation occurs while archived; risk remains visible in run history.
- **Verification required:** None in this run.
- **Branch:** Not applicable
- **Pull request:** Not applicable
- **Verification evidence:** Not applicable
- **Outcome:** Skipped by explicit archive decision

## Execution Order

1. `2026-07-19-002-agent-system-T001`
2. `2026-07-19-002-brain-T002`
3. `2026-07-19-002-devkofi-T003`
4. Resolve approval for `2026-07-19-002-archon-T004`
5. Unblock `2026-07-19-002-memory-sequence-game-T005`

Tasks must be revalidated against current repository state before implementation. Only `ready` tasks may proceed through `run all tasks`.
