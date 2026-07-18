# KareBraids

**Last updated:** 2026-07-18

## Snapshot

KareBraids is a MERN booking platform for browsing braid services, checking appointment availability, requesting bookings, sending enquiries, and managing bookings and services through a protected admin area.

The business is based in Birmingham, UK.

## Links

- Repository: https://github.com/kofiarhin/karebraids
- SSH: `git@github.com:kofiarhin/karebraids.git`
- Live: https://karebraids.vercel.app/

## Current State

- Lifecycle: Not documented
- Stack: React, Vite, Tailwind CSS, TanStack Query, Node.js, Express, MongoDB, Mongoose, JWT
- Testing: Vitest and Testing Library for the client; Jest and Supertest for the API
- Deployment: single Vercel project serving the frontend and Express API on the same origin
- Current priority: Not documented

## Current Focus

Not documented.

## Brainstorming

_No durable brainstorming notes captured yet._

## Decisions

- Public bookings are limited to services marked available and booking-enabled in MongoDB.
- Booking slots are protected against duplicates by service, date, and time.
- Services are seeded through an idempotent database workflow.
- Production uses same-origin `/api` requests in the normal Vercel deployment.

## Assumptions

- None recorded.

## Open Questions

- What is the current business or product milestone?
- Which customer journey needs the most improvement?
- Are content, SEO, payments, reminders, or analytics part of the next phase?

## Next Actions

- Document the current booking and operational priorities.
- Record the next approved customer-facing or admin improvement.
