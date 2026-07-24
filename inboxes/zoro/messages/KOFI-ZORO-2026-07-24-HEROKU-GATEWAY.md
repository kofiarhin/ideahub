# KOFI-ZORO-2026-07-24-HEROKU-GATEWAY

- **Status:** `new`
- **From:** Kofi
- **To:** Zoro
- **Type:** task-assignment
- **Priority:** critical
- **Project:** Context API
- **Run:** none
- **Task:** none
- **Work key:** `context-api:full-heroku-gateway`
- **Task status:** `ready`
- **Approval:** full-implementation-approved
- **Created:** 2026-07-24

## Objective

Fully implement the Heroku Gateway in `kofiarhin/context-api` using the approved specification and implementation plan. This is one complete delivery, not a phased subset. Continue through source implementation, automated tests, documentation, OpenAPI generation, release validation, pull request, review fixes, verification, and reporting. Do not report the feature as complete merely because source code or a pull request exists.

## Authoritative Documents

Read these files from current Context API `main` before implementation:

```text
docs/HEROKU_GATEWAY_SPEC.md
docs/HEROKU_GATEWAY_IMPLEMENTATION_PLAN.md
```

Specification commits created under Kofi's explicit direct-main documentation authority:

```text
docs/HEROKU_GATEWAY_SPEC.md — f63aadb953eb0ab535b03e63c46e5c95024025b3
docs/HEROKU_GATEWAY_IMPLEMENTATION_PLAN.md — 90d86d4ee221bbf2a96a36f429078e753746de30
```

Re-read current source, tests, documentation, open branches, and pull requests. The repository may have changed after these documentation commits.

## Required Branch Workflow

1. Resolve the latest Context API `main` revision.
2. Check for equivalent active branches or pull requests.
3. Create a separate feature branch from current `main`.
4. Recommended branch:

```text
feat/full-heroku-gateway
```

5. Perform all runtime implementation on that branch.
6. Use focused commits.
7. Push the branch and open one focused pull request.
8. Do not write runtime implementation directly to `main`.
9. Do not force-push shared work.

## Scope

Implement the complete required feature defined by the specification, including:

- Heroku environment validation;
- dedicated Zoro-to-Context-API Bearer authentication;
- Heroku Platform API v3 client;
- resource allowlists;
- operation classification and approval enforcement;
- self-app protections;
- account, rate-limit, region, and stack operations;
- complete app lifecycle operations;
- app features, buildpacks, and stack changes;
- redacted config-var metadata and controlled mutations;
- dyno and formation reads, restarts, and scaling;
- sources, builds, slugs, releases, and rollback;
- bounded log-session querying;
- domains and SNI endpoints;
- add-ons and attachments;
- collaborators and app permissions;
- pipelines, couplings, promotions, and pipeline config;
- review apps and review-app configuration;
- app and pipeline webhooks and delivery inspection;
- teams, members, invitations, usage, and minimized invoice reads;
- conditional Private Space, access, topology, NAT, and VPN operations;
- explicit serializers and safe error translation;
- complete unit, service, integration, contract, security, regression, and release-validation coverage;
- canonical and generated Builder-compatible OpenAPI schemas;
- README, deployment documentation, and release checklist;
- preservation of existing Context API, GitHub Gateway, and Vercel Gateway behavior.

Do not reduce this assignment to a read-only MVP or optional phases.

## Authority

Approved now:

- read `kofiarhin/ideahub` as required for this assignment;
- read and modify `kofiarhin/context-api` on the isolated feature branch;
- create the isolated branch;
- add source, tests, scripts, schemas, and documentation required by the approved specification;
- run local verification;
- push focused commits;
- open and update a focused pull request;
- address review and verification findings on the same branch;
- report through the indexed Architect inbox.

Not pre-authorized by this assignment:

- direct runtime writes to Context API `main`;
- merging the pull request;
- deployment;
- changing live Heroku config or secret values;
- changing the live GPT Builder configuration;
- running paid, destructive, access-administration, production-sensitive, or Private Space mutations against live resources;
- disclosing tokens, config values, private keys, certificate keys, webhook secrets, or temporary source/log URLs.

When merge, deployment, live configuration, billing, destructive, access-admin, or production mutation authority is required, report the exact gate with completed evidence. Continue all unaffected implementation and verification work before waiting.

## Full-Delivery Rule

Do not stop after:

- scaffolding;
- a partial endpoint group;
- read-only operations;
- unit tests only;
- source implementation without verification;
- opening the pull request;
- receiving review comments;
- one failing verification run.

Continue correcting implementation and tests until the full specified source feature passes clean verification or a concrete external blocker prevents further progress.

A Custom GPT cannot continue asynchronously after its conversation ends. Therefore, while processing this assignment, complete as much of the continuous workflow as current authority and tooling permit in the active session, preserve every durable result, and report only genuine remaining external gates.

## Verification Requirements

At minimum, run from a clean checkout:

```bash
npm ci
npm test
npm run lint
npm run format:check
npm run verify:github-gateway
npm run verify:vercel-gateway
npm run verify:heroku-gateway
npm run verify
node scripts/generate-heroku-action-schemas.js --check
```

Also verify:

- no automated test performs a live Heroku call;
- no secret or real credential is committed;
- every required route is mounted and authenticated;
- sensitive routes have policy and approval enforcement;
- config values remain redacted;
- self-app deletion and scale-to-zero are blocked;
- required self-app config removal is blocked;
- canonical and generated OpenAPI schemas validate;
- Builder schemas remain within operation limits;
- existing Context API, GitHub, and Vercel contracts remain green;
- changed files are scoped to the approved feature and necessary shared infrastructure.

## Pull Request Requirements

The pull request must include:

- assignment ID `KOFI-ZORO-2026-07-24-HEROKU-GATEWAY`;
- work key `context-api:full-heroku-gateway`;
- exact base and head revisions;
- links to both approved documents;
- endpoint completion matrix;
- changed files;
- verification commands and exact outcomes;
- security and self-protection summary;
- schema generation summary;
- unperformed live checks and why;
- explicit statement that merge and deployment remain pending unless separately authorized.

## Required Response

Report through the indexed Architect inbox. Include:

- originating assignment ID;
- work key;
- acknowledged scope;
- base revision;
- feature branch;
- commits;
- pull request;
- complete changed-file list;
- endpoint completion matrix;
- implementation summary;
- verification performed and exact results;
- verification not performed;
- review findings and fixes;
- merge status;
- deployment status;
- live Action configuration status;
- live smoke-test and cleanup status;
- entitlement-dependent operations not live-tested;
- security, billing, destructive-operation, and self-management risks;
- confirmation that no secrets were committed or exposed;
- blockers and exact required Kofi/Architect action.

Do not mark an Architect task completed and do not claim the Heroku Gateway is fully completed until independent verification, authorized merge, exact-revision deployment, Action configuration, controlled live verification, and cleanup have all succeeded.
