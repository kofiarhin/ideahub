# Agent Instructions

This repository is Kofi's persistent brainstorming workspace and cross-tool knowledge base.

These rules apply to ChatGPT, Architect, Codex, Claude, Copilot, local agents, and any other tool with repository access.

## Read Order

Before answering workspace-wide questions:

1. Read `CONTEXT.md` for the quick briefing.
2. Read `PROJECTS.md` for the canonical project index.
3. Open only the relevant files under `projects/`.
4. Read `INBOX.md` only when raw or unprocessed ideas are relevant.

For a single-project request, still check `CONTEXT.md` and `PROJECTS.md` before opening that project's file.

## Write Permission

- Reading is allowed whenever context is needed.
- Do not create, update, move, or delete files without explicit user approval.
- Brainstorming in chat is not approval to save.
- Before writing, state which files will change and summarize the intended update.
- Treat commands such as `capture this`, `save to <project>`, `update the hub`, `commit these notes`, or a direct implementation request as approval for the described change.
- Keep writes scoped to the approved content.

## Source-of-Truth Rules

- `PROJECTS.md` is the only canonical project index.
- `CONTEXT.md` is the current high-level briefing, not a full archive.
- `INBOX.md` contains unprocessed thoughts and must not be treated as committed plans.
- `projects/<project>.md` contains durable project-specific context.
- Do not recreate competing project indexes.

## Information Quality

Keep these categories distinct:

- **Fact** — confirmed information with a clear source.
- **Decision** — an explicitly approved choice.
- **Idea** — a possibility being explored.
- **Assumption** — an unverified belief that may affect work.
- **Question** — something unresolved.

Never silently convert an idea or assumption into a fact or decision.

When information conflicts:

1. Preserve both versions temporarily.
2. Mark the conflict clearly.
3. Ask for resolution when it materially affects the work.
4. Update the durable note only after resolution is approved.

## Ideas Hub Update Routing

Requests such as `update Ideas Hub`, `update the hub`, `save to <project>`, or `record this` are normal governed write requests unless they exactly match a registered Architect command.

Resolve the target context in this order:

1. Recognized Architect command.
2. Explicitly named Architect run.
3. Explicitly named project or idea.
4. Active project established by an approved handoff or current workflow.
5. Referenced repository, file, issue, pull request, task, or work item.
6. Best matching entry in `PROJECTS.md` and its project record.
7. One focused clarification question when the destination remains materially ambiguous.

Inspect available sources before asking a question. Do not ask for information already available in the repository, active run, referenced work item, or approved handoff.

After resolving the project, route information by meaning:

- **Current State** — verified implementation, deployment, lifecycle, stack, or other confirmed current fact.
- **Current Focus** — explicitly confirmed work being pursued now.
- **Brainstorming** — unapproved features, possibilities, approaches, and product ideas.
- **Decisions** — explicitly approved product, architecture, workflow, or policy choices.
- **Assumptions** — relevant beliefs that remain unverified.
- **Open Questions** — unresolved choices, missing information, and material ambiguities.
- **Next Actions** — concrete approved follow-up work that has not yet been completed.
- **INBOX.md** — raw information whose project or meaning is still unclear and whose capture has been approved.

Split a statement across sections when it contains multiple information types. Do not place an unapproved feature in `Decisions`, an unverified implementation claim in `Current State`, or a speculative action in `Next Actions`.

### Feature Request Lifecycle

Use the existing project record and Architect task lifecycle rather than creating a competing feature tracker:

1. Record a proposed feature under the project's `Brainstorming` section.
2. Record an explicitly approved direction under `Decisions`.
3. Record approved follow-up work under `Next Actions`.
4. During an applicable Architect run, classify unclear work as `needs_discovery`, `needs_spec`, or `needs_approval`.
5. Mark work `ready` only when approved scope and acceptance criteria are sufficient for implementation.
6. Implement only `ready` tasks through the permitted Architect execution workflow.
7. After verification, update `Current State`, durable `Decisions`, and remaining `Next Actions` as needed.
8. Remove or condense the original brainstorming entry only after its useful context has been preserved.

GitHub Issues are optional. Create or link one only when the user requests it or the target project already uses Issues as its execution tracker. An issue may support delivery, but it does not replace the durable project record.

Claims about implemented or deployed behavior require user-confirmed verification or traceable evidence before they become durable current state. If verification is unavailable, preserve the claim as an assumption, open question, blocker, or run finding as appropriate.

### Root File Boundaries

- Update `projects/<project>.md` for normal project knowledge changes.
- Update `PROJECTS.md` only when a project's name, summary, repository, live URL, or lifecycle state changes.
- Update `CONTEXT.md` only when the broad workspace landscape, priorities, or cross-project context changes.
- Update `INBOX.md` only for approved raw capture whose durable destination is not yet clear.
- Keep Architect audit, task, execution, and verification history under `architect/runs/`.

Do not update every root file for a routine project change.

## Editing Rules

- Preserve useful existing context unless removal is explicitly approved.
- Prefer concise summaries and links over copying large documents.
- Use relative links between files in this repository.
- Update the `Last updated` field in any durable context file you materially change.
- Keep project files consistent with the standard section structure.
- Record meaningful approved choices under `Decisions`.
- Put speculative thoughts under `Brainstorming` or `Ideas`.
- Do not store secrets, tokens, passwords, private keys, or production credentials.
- Use focused commit messages that describe the knowledge change.

## Project File Structure

Use this structure unless a project needs a justified extension:

```md
# Project Name

## Snapshot

## Links

## Current State

## Current Focus

## Brainstorming

## Decisions

## Assumptions

## Open Questions

## Next Actions
```

A project file may start small. Do not invent missing descriptions, priorities, deadlines, or status. Mark unknown information as `Not documented`.

## Workspace Maintenance

When a project is added:

1. Add one entry to `PROJECTS.md`.
2. Create `projects/<project-slug>.md`.
3. Update `CONTEXT.md` only if the new project changes the broad workspace overview.

When a project changes materially:

1. Update its project file.
2. Update `PROJECTS.md` if its name, repository, live URL, or lifecycle state changed.
3. Update `CONTEXT.md` only when the change matters at workspace level.

When capturing a raw thought:

1. Add it to `INBOX.md` with a date and short label.
2. Do not force it into a project prematurely.
3. Move or summarize it into a project file after its destination is clear and the move is approved.

## Useful Agent Commands

Interpret these phrases consistently:

- `load hub` — read the root context and relevant project notes.
- `hub overview` — summarize tracked work, priorities, blockers, and unresolved questions without writing.
- `capture this` — propose an `INBOX.md` entry, then write only when approval is explicit.
- `save to <project>` — update the named project file with the approved outcome.
- `update hub` — refresh affected project notes plus root context/index files when necessary.

## Architect Command Workflows

The ChatGPT Architect project settings remain the global governance layer. Command workflows are command-specific and scoped; they cannot bypass discovery, approval, security, source-of-truth, isolation, or verification rules.

- [`architect/README.md`](architect/README.md) is the canonical command registry.
- [`architect/commands/good-morning.md`](architect/commands/good-morning.md) defines `good morning`, which writes only run-scoped audit and task files.
- [`architect/commands/run-all-tasks.md`](architect/commands/run-all-tasks.md) defines `run all tasks`, which executes only eligible `ready` work.
- Project records update only after verification.
- Run artifacts live under `architect/runs/<run-id>/` and do not replace canonical project records or repository-local authority documents.
