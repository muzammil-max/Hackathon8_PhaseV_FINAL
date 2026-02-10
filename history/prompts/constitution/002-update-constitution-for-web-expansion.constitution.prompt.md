---
id: 002
title: update constitution for web expansion
stage: constitution
date: 2026-02-05
surface: agent
model: gemini
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["governance", "web-expansion"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution ## MyTodoApp — Web Expansion

## Role
You are an **expert full-stack engineer** operating under a **strict spec-driven workflow** using **Gemini**.  
You must evolve MyTodoApp from a CLI tool into a **secure, multi-user web application**.

---

## Constitutional Law
- Specs are the **single source of truth**
- No implementation without spec reference
- No breaking changes to Phase 1 logic
- Deterministic, auditable behavior
- Gemini must reason before generating code

---

## Objective
Transform the existing CLI Todo app into a **modern full-stack web app** with authentication, persistence, and a stable API—while preserving core task semantics.

---

## Mandatory Capabilities
- Multi-user support
- JWT-based authentication
- Persistent database storage
- RESTful API
- Responsive web interface
- All Phase 1 Todo features preserved

---

## Technology Mandate
| Layer | Stack |
|-----|------|
| Frontend | Next.js (App Router) |
| Backend | FastAPI |
| ORM | SQLModel |
| Database | PostgreSQL (Neon) |
| Auth | Better Auth (JWT) |
| AI | Gemini |

No substitutions allowed.

---

## API Constitution (Immutable)
- REST-only
- Stateless
- User-scoped resources

Endpoints:
- `GET    /api/tasks`
- `POST   /api/tasks`
- `GET    /api/tasks/{id}`
- `PUT    /api/tasks/{id}`
- `DELETE /api/tasks/{id}`
- `PATCH  /api/tasks/{id}/complete`

API shapes must not change across phases.

---

## Security Constitution
- JWT required for all routes
- Token via `Authorization: Bearer <token>`
- User identity derived **only** from JWT
- Server enforces task ownership
- Missing or invalid token → `401`

---

## Backend Rules
- Stateless FastAPI
- No session storage
- SQLModel for all DB access
- Strict user isolation
- No hardcoded secrets

---

## Frontend Rules
- Next.js App Router
- Auth-aware routing
- Centralized API client
- Clear loading and error states

---

## Data Integrity
- Each task belongs to exactly one user
- No cross-user data access
- Deletions are permanent unless archived

---

## Non-Negotiables
- No silent failures
- No undocumented behavior
- No shared user data
- No deviation from spec

---

## Success Criteria
- Secure multi-user Todo web app
- Stable REST API
- Persistent PostgreSQL storage
- Clean separation of concerns
- Fully spec-compliant Gemini output

## Response snapshot

Updated project constitution to v2.0.0 for Web Expansion, defining new principles, stack mandates (Next.js/FastAPI), and security rules.

## Outcome

- ✅ Impact: Constitution updated to v2.0.0.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Major version bump due to shift from CLI to Web App.
- 🚧 Failure modes: none
- 📝 Grader results: PASS
- 🔄 Prompt variant: default
- 🧪 Next experiment: none
