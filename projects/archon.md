# Archon

**Last updated:** 2026-07-18

## Snapshot

Archon is an AI-powered software architecture studio that turns a product idea into a structured, implementation-ready engineering blueprint.

Lifecycle: `Exploring`

## Links

- Repository: https://github.com/kofiarhin/archon
- Documentation PR: https://github.com/kofiarhin/archon/pull/1
- Live application: Not deployed
- PRD: Proposed in `kofiarhin/archon` pull request #1

## Current State

The repository has been created and initialized. A draft repository-local PRD, proposed system architecture, development roadmap, security baseline, and initial architecture decision record are available in pull request #1. These documents are reviewable proposals and are not yet approved or merged.

## Current Focus

Review and approve the repository-local product definition before implementation begins.

## Brainstorming

Potential future capabilities include:

- Product requirements generation
- Recommended technology stacks
- System and infrastructure architecture
- Database schema and ERD generation
- API design and OpenAPI export
- Authentication and authorization flows
- Mermaid architecture diagrams
- Security and scalability reviews
- Architecture decision records
- Delivery roadmaps and coding-agent prompts
- Starter code and GitHub repository bootstrapping
- Visual architecture editing and team collaboration

These remain ideas unless explicitly approved in the repository-local PRD or another accepted specification.

## Decisions

- The product name is **Archon**.
- The product category is an AI software architecture and developer-tooling platform.
- The initial value proposition is: **From idea to architecture.**
- The first release should focus on architecture documentation and implementation planning rather than full application code generation.
- The application repository is `kofiarhin/archon`.

## Assumptions

- Primary early users may include developers, freelancers, startup founders, students, and small engineering teams.
- The initial interface may be web-based.
- AI-generated output will require structured schemas, validation, and clear human review rather than being treated as automatically correct.
- Technology choices in pull request #1 remain proposed until approved and merged.

## Open Questions

- Should the MVP support one opinionated stack or recommend multiple stacks?
- What usage limits, data retention rules, and billing model should apply?
- Which AI provider and model strategy should be approved?
- What quality benchmark and evaluation dataset should be used?
- Which export formats beyond Markdown should be supported?

## Next Actions

1. Review `kofiarhin/archon` pull request #1.
2. Resolve the PRD's open decisions and amend its acceptance criteria where needed.
3. Merge the documentation PR only when the MVP scope and proposed architecture are approved.
4. Convert the approved roadmap into isolated implementation tasks.
5. Begin implementation only after explicit approval.
