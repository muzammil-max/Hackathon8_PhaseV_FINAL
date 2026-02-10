# Implementation Plan: AI Chatbot System

**Branch**: `004-ai-chatbot` | **Date**: 2026-02-05 | **Spec**: [specs/004-ai-chatbot/spec.md](spec.md)
**Input**: Feature specification from `/specs/004-ai-chatbot/spec.md`

## Summary

Implement a conversational AI interface using Gemini and MCP. The system will be fully stateless, reconstructing conversation history from the database for each request. Task management will be executed exclusively through MCP tools, ensuring strict separation between AI reasoning and database mutations.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Official MCP SDK, SQLModel, Better Auth
**Storage**: Neon PostgreSQL
**Testing**: pytest
**Target Platform**: Linux/Cloud (FastAPI)
**Project Type**: web
**Performance Goals**: < 3s p95 for chat responses
**Constraints**: Stateless server, no direct DB access by agent, JWT-based isolation
**Scale/Scope**: Multi-user support with persistent history

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Specs are authoritative: Plan derived directly from `spec.md`.
- [x] No hidden state: Server is stateless; history is DB-backed.
- [x] Tool-driven intelligence: Agent uses MCP tools for all task mutations.
- [x] Agents reason first, then act: Using OpenAI Agents SDK for guided reasoning.
- [x] Security First: JWT-based isolation and ownership checks.
- [x] Modern Stack Mandate: Using FastAPI, SQLModel, PostgreSQL, and Gemini.

## Project Structure

### Documentation (this feature)

```text
specs/004-ai-chatbot/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models.py        # Updated for Conversations/Messages
│   ├── database.py
│   ├── main.py          # /api/chat endpoint
│   ├── agents/          # New: Agent definitions
│   │   ├── chatbot.py
│   │   └── tools.py     # New: MCP Tool implementations
│   └── routes/
│       └── chat.py      # New: Chat route
└── tests/
    └── integration/
        └── test_chat.py

frontend/
├── src/
│   ├── app/
│   │   └── chat/        # New: Chat page/component
│   └── services/
│       └── chat.ts      # New: Chat API client
```

**Structure Decision**: Web application structure (Option 2) with backend/frontend separation.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |