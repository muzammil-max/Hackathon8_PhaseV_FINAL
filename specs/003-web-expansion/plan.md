# Implementation Plan: Phase 2 Web Expansion

**Branch**: `003-web-expansion` | **Date**: 2026-02-05 | **Spec**: [specs/003-web-expansion/spec.md](spec.md)
**Input**: Feature specification from `specs/003-web-expansion/spec.md`

## Summary

Convert the CLI Todo app into a secure, multi-user full-stack web application.
**Approach**:
- **Backend**: Python/FastAPI with SQLModel/PostgreSQL for persistence and JWT auth.
- **Frontend**: Next.js (App Router) for the user interface.
- **Architecture**: Strict separation of frontend and backend communicating via REST API.

## Technical Context

**Language/Version**: Python 3.10+ (Backend), TypeScript/Node 18+ (Frontend)
**Primary Dependencies**:
- Backend: FastAPI, SQLModel, Pydantic, Uvicorn, Python-Jose (or similar for JWT)
- Frontend: Next.js 14+ (App Router), TailwindCSS (implied for "modern/responsive"), Better Auth (or equivalent auth integration)
**Storage**: PostgreSQL (Neon)
**Testing**:
- Backend: Pytest, Httpx
- Frontend: Jest, React Testing Library
**Target Platform**: Web (Modern Browsers)
**Project Type**: Web Application
**Performance Goals**: <500ms API response, instant client-side interactions
**Constraints**: Strict user isolation, no data leaks, preservation of Phase 1 logic.
**Scale/Scope**: Multi-user, foundational architecture for future growth.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Single Source of Truth**: Plan is derived strictly from Spec 003. ✅
- **Stability & Preservation**: Logic from Phase 1 is reimplemented/wrapped, not discarded. ✅
- **Deterministic & Auditable**: Gemini used for generation. ✅
- **Security First**: JWT auth and user isolation are central to the design. ✅
- **Modern Stack Mandate**: Plan uses Next.js, FastAPI, SQLModel, Postgres. ✅
- **API Constitution**: Endpoints match the immutable list. ✅

## Project Structure

### Documentation (this feature)

```text
specs/003-web-expansion/
├── plan.md              # This file
├── research.md          # Technology integration decisions
├── data-model.md        # DB Schema (User, Task)
├── quickstart.md        # Setup guide
├── contracts/           # API definitions
│   └── api.md           # REST contract
└── tasks.md             # Implementation tasks (next step)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models.py        # SQLModel entities
│   ├── main.py          # App entry point
│   ├── auth.py          # JWT logic
│   ├── database.py      # DB connection
│   └── routes/
│       ├── tasks.py     # Task endpoints
│       └── auth.py      # Auth endpoints
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_tasks.py
├── requirements.txt
└── .env.example

frontend/
├── src/
│   ├── app/             # Next.js App Router
│   │   ├── page.tsx     # Landing/Dashboard
│   │   ├── login/
│   │   └── signup/
│   ├── components/      # UI Components
│   ├── lib/             # Utilities (API client)
│   └── types/           # TypeScript interfaces
├── package.json
└── .env.local.example
```

**Structure Decision**: Split repository into `backend/` and `frontend/` directories at the root to maintain clean separation of concerns as required by the "Web Application" pattern.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Monorepo Split | Mandated by "Web App" nature | Single folder mixes concerns (JS vs Py) |
| Async SQLModel | Performance/Mandate | Sync is simpler but blocks event loop |