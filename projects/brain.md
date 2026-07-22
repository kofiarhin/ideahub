# Brain

**Last updated:** 2026-07-22

## Snapshot

Brain OS v2 is a full-stack MERN personal operating system where MongoDB stores durable memory, Codex CLI provides the AI workflow layer, and React provides the interface.

The application covers notes, tasks, plans, reviews, goals, projects, ideas, context, deliverables, generated posts, and day plans.

## Links

- Repository: https://github.com/kofiarhin/brain
- SSH: `git@github.com:kofiarhin/brain.git`
- Live: https://brain-pi-black.vercel.app/

## Reconciliation

```yaml
repository: kofiarhin/brain
default_branch: main
authority_document: not_documented
authority_revision: not_available
implementation_revision: 1302ad67912091ab806f0b08b607e8c14d4f3d93
last_reconciled: 2026-07-22
reconciliation_status: unverified
```

The repository and pull-request state were reconciled. Product-authority documentation, test execution, deployment state, and runtime behavior still require separate verification.

## Current State

- Lifecycle: Not documented
- Stack: React, Vite, Node.js, Express, MongoDB, Mongoose
- AI workflow: Codex CLI reads and updates MongoDB-backed context
- Chat access: authenticated read-only conversational route backed by application context
- Current priority: Not documented
- PR #9, `Audit app brain data flow and UX states`, merged into `main` on 2026-07-18 as commit `1302ad67912091ab806f0b08b607e8c14d4f3d93`.
- PR #9 reports fixes for structured list rendering, Dashboard loading/error/empty states, and Europe/London day calculations. Its description states that the test suite was not run in the implementation environment, so those behaviors remain implementation evidence rather than verified runtime state.

## Current Focus

Document the current production status, authoritative product documentation, and immediate milestone.

## Requirement Ledger

| Requirement ID | Requirement | Authority | Status | Implementation evidence | Verification |
| --- | --- | --- | --- | --- | --- |
| `BRAIN-UX-001` | Render structured list items as readable text | PR #9 | `implemented_unverified` | PR #9; commit `1302ad67912091ab806f0b08b607e8c14d4f3d93` | Test execution not recorded |
| `BRAIN-UX-002` | Show Dashboard loading, error, and empty states | PR #9 | `implemented_unverified` | PR #9; commit `1302ad67912091ab806f0b08b607e8c14d4f3d93` | Test execution not recorded |
| `BRAIN-TIME-001` | Use Europe/London day calculations for Dashboard state | PR #9 | `implemented_unverified` | PR #9; commit `1302ad67912091ab806f0b08b607e8c14d4f3d93` | Test execution not recorded |

## Brainstorming

_No durable brainstorming notes captured yet._

## Decisions

- MongoDB is the application source of truth for personal operating-system data.
- Codex-command workflows perform AI-assisted updates.
- The authenticated chat interface is read-only unless write behavior is explicitly implemented later.
- Day planning is separate from the memory-only `update brain` workflow.
- PR #10 was closed without merging because its chat direction is superseded by current `main`.
- PR #6 was closed without merging because its modular agent-instruction proposal is superseded.

## Assumptions

- Closing PRs #10 and #6 does not remove any current behavior already present on `main`.
- The PR #9 merge commit remains the current default-branch head as of the reconciliation date.

## Open Questions

- Which Brain workflow is the current priority?
- What should remain inside Brain versus this GitHub Ideas Hub?
- Which data should other agents be allowed to read or update?
- Which repository-local ORD, PRD, or specification is authoritative for Brain?
- Has commit `1302ad67912091ab806f0b08b607e8c14d4f3d93` passed the full test suite and been deployed to the linked production environment?

## Next Actions

- Identify and record the authoritative ORD, PRD, or specification.
- Run or obtain test and CI evidence for the current `main` revision.
- Verify the deployed production revision and the PR #9 behaviors.
- Document the current production status and immediate milestone.