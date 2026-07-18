# Brain

**Last updated:** 2026-07-18

## Snapshot

Brain OS v2 is a full-stack MERN personal operating system where MongoDB stores durable memory, Codex CLI provides the AI workflow layer, and React provides the interface.

The application covers notes, tasks, plans, reviews, goals, projects, ideas, context, deliverables, generated posts, and day plans.

## Links

- Repository: https://github.com/kofiarhin/brain
- SSH: `git@github.com:kofiarhin/brain.git`
- Live: https://brain-pi-black.vercel.app/

## Current State

- Lifecycle: Not documented
- Stack: React, Vite, Node.js, Express, MongoDB, Mongoose
- AI workflow: Codex CLI reads and updates MongoDB-backed context
- Chat access: authenticated read-only conversational route backed by application context
- Current priority: Not documented

## Current Focus

Verify Brain PR #9 separately. Superseded PR cleanup is complete.

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

## Open Questions

- Which Brain workflow is the current priority?
- What should remain inside Brain versus this GitHub Ideas Hub?
- Which data should other agents be allowed to read or update?

## Next Actions

- Verify PR #9 against current `main` and record a merge or changes-needed recommendation.
- Document the current production status and immediate milestone.