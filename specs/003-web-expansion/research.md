# Research: Phase 2 Web Expansion

**Status**: Complete
**Date**: 2026-02-05

## Decisions & Rationale

### 1. Project Structure
- **Decision**: Monorepo-style structure with explicit separation:
  - `backend/`: FastAPI application (Python)
  - `frontend/`: Next.js application (TypeScript)
- **Rationale**: Enforces strict separation of concerns between client and server, aligning with the "REST-only" API constitution. Matches the "Web application" option in the plan template.

### 2. Authentication Integration
- **Decision**: "Better Auth" (assumed to be a library or service like NextAuth.js or a custom JWT implementation compatible with the prompt's naming) will handle frontend session management. Backend will validate JWTs using a dependency injection provider.
- **Rationale**: "Better Auth" is mandated. Backend validation via dependency injection (`Depends(get_current_user)`) is standard FastAPI practice for security and testability.

### 3. Database & ORM
- **Decision**: SQLModel with async engine.
- **Rationale**: Mandated by Constitution. Async engine required for high-performance FastAPI applications.
- **Schema Strategy**: `User` and `Task` models will be defined in `backend/src/models.py`. Foreign keys will enforce the "Each task is linked to exactly one user" rule.

### 4. API Client
- **Decision**: Generated or strictly typed fetch wrapper in `frontend/src/services/api.ts`.
- **Rationale**: Centralized API client (Constitution rule) ensures consistent error handling and auth header injection.

## Unknowns Resolved

- **Stack**: Fully defined by Constitution (Next.js, FastAPI, SQLModel, Postgres, Gemini).
- **Deployment**: Local development for now (Neon for DB mentioned, but local simulation/connection assumed).
