# Memory Sequence Game

**Last updated:** 2026-07-18

## Snapshot

- **Lifecycle:** Exploring
- **Product name:** Memory Game
- **Repository:** https://github.com/kofiarhin/memory-game
- **Default branch:** `main`
- **Type:** Responsive browser game
- **Audience:** General players aged 8+
- **Status:** MVP implemented and audited; fixes merged; CI passing; deployment pending.

## Links

- **Repository:** https://github.com/kofiarhin/memory-game
- **Product requirements:** https://github.com/kofiarhin/memory-game/blob/main/PRD.md
- **MVP implementation:** https://github.com/kofiarhin/memory-game/commit/324d276bb6e6f3df3c62c7366cf63fa5ae73146a
- **Audit fix PR:** https://github.com/kofiarhin/memory-game/pull/1
- **Audit fix merge:** https://github.com/kofiarhin/memory-game/commit/3073edad00666fd8538af68ada4727639050aa16
- **Live application:** Not deployed
- **Ideas Hub:** [Project index](../PROJECTS.md)

## Current State

The MVP is implemented on `main`. Players choose colours, shapes, or familiar icons, watch cards appear one at a time, then rebuild the sequence from a shuffled pool.

Core behaviour:

- sequence starts at three cards;
- each correct round adds one card;
- first incorrect answer consumes the retry;
- second incorrect answer ends and records the run;
- score is `sequence length² × 10` per correct round;
- progress and settings are stored locally;
- touch, mouse, keyboard, reduced motion, and optional sound are supported.

The complete PRD is committed as `PRD.md`.

## Audit Completed

A focused audit covered reducer transitions, persistence timing, repeated-card handling, playback input locking, feedback accessibility, tests, and CI.

### Bugs found and fixed

1. **Completed-run loss** — a run was only counted after the player clicked through the second-mistake feedback screen. Leaving that screen lost the completed-run statistic.
2. **Weak accessible result feedback** — correct and incorrect cards were visually styled, but their accessible names did not include the result and the visual indicator relied too heavily on colour.

### Fixes

- Completed runs are now recorded immediately when the second incorrect answer is submitted.
- Continuing to the game-over screen no longer risks double-counting the run.
- Feedback cards now include `correct` or `incorrect` in their accessible names.
- Feedback cards now show visible check/cross badges in addition to colour.
- Regression tests cover both fixes.
- GitHub Actions now runs dependency installation, tests, lint, and production build on pull requests and pushes to `main`.

Application PR #1 was squash-merged after CI passed.

## Decisions

- React 19, TypeScript, Vite, and Tailwind CSS.
- Reducer-driven game session state.
- Pure domain functions for sequence generation, scoring, and validation.
- Browser persistence behind a storage adapter.
- Vitest and React Testing Library for automated tests.
- No backend, accounts, Redux Toolkit, or TanStack Query for the MVP.
- Cards remain unique through length five; repeats are allowed from length six.
- Playback remains one second per card with a 300 ms gap.
- Result state must not rely on colour alone.

## Implemented Scope

- Category selection
- Endless sequence progression
- Timed playback
- Ordered recall slots
- Shuffled recall pool
- Undo and submission locking
- Position-level validation
- Sequence reveal
- Retry and game-over flow
- Progressive scoring
- Local records and settings
- Responsive touch, mouse, and keyboard support
- Reduced-motion handling
- Optional sound
- Automated tests
- GitHub Actions CI
- README and PRD

## Validation

Original MVP validation:

- 6 test files and 19 tests passed
- lint passed with 0 warnings and 0 errors
- TypeScript and Vite production build passed

Audit validation:

- GitHub Actions run #2 completed successfully
- dependency installation passed
- 7 test files and 21 tests passed
- lint passed
- production build passed

## Remaining Risks

- Manual browser testing is still needed across representative mobile and desktop devices.
- A dedicated keyboard and screen-reader review is still needed.
- Very long runs create long playback durations.
- Emoji appearance varies by operating system.
- Local progress has no cloud backup.
- Sound depends on browser Web Audio policies.
- Production hosting has not been verified.
- No lockfile is committed; CI currently uses `npm install` rather than `npm ci`.

## Next Actions

1. Deploy `main` to a static host.
2. Record the production URL here and in `PROJECTS.md`.
3. Complete manual mobile, desktop, keyboard, screen-reader, and reduced-motion testing.
4. Add a lockfile or define a deliberate dependency-locking workflow.
5. Collect player feedback before selecting post-MVP scope.
