# Ideas Hub

**Last updated:** 2026-07-18

## Snapshot

Ideas Hub is this Markdown-first repository for brainstorming, project context, and durable reference notes across tools.

## Links

- Repository: https://github.com/kofiarhin/ideas
- SSH: `git@github.com:kofiarhin/ideas.git`
- Live: Not documented

## Current State

- Lifecycle: Not documented
- Stack: Markdown
- Current priority: Not documented

## Current Focus

Not documented.

## Architect Command System

### Structure

- [`architect/README.md`](../architect/README.md)
- [`architect/commands/good-morning.md`](../architect/commands/good-morning.md)
- [`architect/commands/run-all-tasks.md`](../architect/commands/run-all-tasks.md)
- `architect/runs/<run-id>/`

### Decisions

- Architect project settings remain global governance.
- Detailed workflows live in Ideas Hub.
- `good morning` performs lightweight portfolio scans and selective deep audits.
- Tasks require traceable approved intent or verified evidence.
- `good morning` writes only run-scoped audit/task files.
- `run all tasks` implements only `ready` tasks.
- Discovery/specification work pauses for approval.
- Repositories are isolated by branch, commit, and pull request.
- Ideas Hub project truth updates only after verified work.
- Commands never silently approve scope, direction, migrations, security-sensitive changes, lifecycle changes, or direct-main work.

### Current State

- Initial command definitions are documented.
- No operational Architect run has been executed yet.

### Next Actions

1. Add the compact command-resolution instructions to the ChatGPT Architect project settings.
2. Invoke `good morning`.
3. Review generated classifications and approval gates.
4. Invoke `run all tasks` on the durable queue.
5. Refine workflows based on the first completed run.


## Brainstorming

_No durable brainstorming notes captured yet._

## Decisions

- GitHub is the source of truth for this workspace.
- `PROJECTS.md` is the only canonical project index.

## Assumptions

- None recorded.

## Open Questions

- What maintenance cadence should this hub follow?
- Which project notes need the next documentation pass?

## Next Actions

- Keep project context and links current as approved project information changes.
