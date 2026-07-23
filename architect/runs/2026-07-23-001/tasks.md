# Architect Tasks — 2026-07-23-001

## Queue Summary

- **Ready:** 1
- **Running:** 0
- **Verifying:** 0
- **Completed:** 0
- **Blocked:** 0
- **Assigned to Zoro:** 1
- **Source implementation performed by Architect:** No

## 2026-07-23-001-context-api-T001 — Reconcile Zoro Action deletion with query transport

- **Work key:** `context-api:zoro-action-query-deletion`
- **Requirement key:** `github-gateway:delete-file-query-transport`
- **Project:** Context API
- **Repository:** `kofiarhin/context-api`
- **Default branch:** `main`
- **Assigned to:** Zoro
- **Task type:** OpenAPI schema maintenance
- **Priority:** high
- **Priority rationale:** The maintained Action schema blocks live verification of the open deletion transport fix in pull request #2.
- **Status:** `ready`
- **Originating assignment:** `ARCH-ZORO-2026-07-23-001`
- **Source documents:** Explicit approved workflow request; `projects/context-api.md`; `projects/zoro.md`; Context API pull request #2; `docs/openapi/zoro-action.yaml`; `src/validation/github.schemas.js`
- **Source section or requirement:** Context API Next Actions item 3; Zoro Task 6A; verified implementation/schema drift
- **Audited implementation revision:** `654ebbc1bf8ada7b2ed339f342859204c6e88505`
- **Audited base revision:** `bf378b82ed04c88152c3cbb7550a590e63a19601`
- **Audited schema blob:** `9cc6c1210b319e02647a48b4c1daca8d496d2141`
- **Evidence:** Pull request #2 accepts deletion data from query parameters whenever any query parameter is present and otherwise falls back to the existing JSON body. The unchanged backend validator allows and requires exactly `owner`, `repo`, `branch`, `path`, `sha`, and `message`. The maintained schema still defines deletion through a required JSON request body.
- **Duplicate check:** Existing Architect run `2026-07-22-001` contains no equivalent work key. Repository pull-request inspection found PR #2, which explicitly leaves the schema update outstanding, and no separate schema reconciliation pull request was identified.

### Scope

- Create an isolated branch in `kofiarhin/context-api` from an appropriate current base after revalidating repository and pull-request state.
- Update `docs/openapi/zoro-action.yaml` so `DELETE /api/v1/github/files` describes the query-based request accepted by pull request #2.
- Define these six deletion query parameters as required: `owner`, `repo`, `branch`, `path`, `sha`, and `message`.
- Match existing backend constraints where the maintained schema already expresses them, including the 40-character hexadecimal SHA pattern, path limit, and commit-message limits.
- Preserve the backend JSON-body fallback; do not remove or change it unless separately approved.
- Preserve the production server URL.
- Preserve all existing authentication and security definitions.
- Preserve the complete 27-operation set and every non-deletion operation.
- Update directly related schema validation tests, release validation, or documentation only when required for the schema change.
- Run verification available through Zoro's connected tools and distinguish inspection from executable checks.
- Open a focused pull request into `kofiarhin/context-api` `main`.
- Write a durable completion or blocker report to `architect-inbox.md`.

### Out Of Scope

- Merging Context API pull request #2.
- Merging the new schema pull request.
- Deploying Context API.
- Updating or republishing the live GPT Action.
- Running shell commands that Zoro cannot actually execute.
- Modifying unrelated routes, schemas, tests, scripts, or documentation.
- Removing the JSON-body fallback.
- Changing secrets, Bearer authentication policy, security definitions, server URL, operation IDs, or operation count.
- Direct writes to `kofiarhin/context-api` `main`.

### Dependencies

- Context API pull request #2 must remain available for implementation-contract inspection.
- No merge or deployment dependency is required to create the schema pull request.

### Authority And Approvals

- Read Ideas Hub: approved.
- Read Context API: approved.
- Create an isolated Context API branch: approved.
- Modify the maintained schema and directly related validation or documentation: approved.
- Open a pull request into Context API `main`: approved.
- Append the required report to `architect-inbox.md`: approved.
- Direct Context API `main` writes: not approved.
- Merge: not approved.
- Deploy: not approved.
- Live GPT Action update: not approved.
- Secret or authentication-policy changes: not approved.

### Acceptance Criteria

1. The deletion Action uses query parameters matching the implementation in pull request #2.
2. `owner`, `repo`, `branch`, `path`, `sha`, and `message` are all required, matching backend behavior.
3. Existing Bearer authentication remains unchanged.
4. The production Context API server URL remains unchanged.
5. Existing non-deletion operations remain present and the complete operation set is preserved.
6. The schema remains acceptable to the repository validator, or any inability or failure is reported honestly without claiming success.
7. Zoro opens a focused Context API pull request into `main` from an isolated branch.
8. Zoro reports durably to `architect-inbox.md` with the originating assignment ID, Architect run ID, Architect task ID, work key, branch, commit SHA, pull request URL, files changed, verification actually performed, verification not performed, risks and blockers, recommendation, and exact required Architect action.

### Verification Requirements

- Re-read pull request #2 and confirm its current head revision before editing.
- Inspect the final deletion operation and confirm each parameter name, location, requiredness, and schema constraint.
- Confirm `deleteGithubFile` remains the operation ID.
- Confirm `security: [{ bearerAuth: [] }]` remains on the deletion operation and existing GitHub operations.
- Confirm the production server URL is unchanged.
- Confirm exactly 27 operation IDs remain and all 12 expected GitHub operation IDs remain.
- Inspect the final diff for unrelated changes.
- Run `npm run verify:github-gateway` only if Zoro has a real command-execution capability; otherwise explicitly report it as not performed.
- Run any additional available repository validation without inventing shell output.
- Report CI status only when actually observed.
- Do not mark this task completed. Architect must independently inspect the branch, commit, pull request, diff, and verification evidence.

### Delivery State

- **Branch:** To be created by Zoro
- **Commit:** Pending
- **Pull request:** Required; pending
- **Verification evidence:** Pending Zoro report and independent Architect review
- **Outcome:** Pending
- **Next authoritative transition:** `ready` remains until Zoro acknowledges or starts work; Architect will later record `running`, `verifying`, or another status only after durable evidence is received and independently checked.