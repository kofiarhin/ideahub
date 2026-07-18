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
