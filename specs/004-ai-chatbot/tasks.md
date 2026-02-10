# Tasks: AI Chatbot System

**Feature Branch**: `004-ai-chatbot`
**Implementation Plan**: [specs/004-ai-chatbot/plan.md](plan.md)

## Phase 1: Setup

- [x] T001 Initialize Phase 3 dependencies (openai-agents, mcp) in backend/pyproject.toml
- [x] T002 Create agent directory structure in backend/src/agents/
- [x] T003 Create chat route file at backend/src/routes/chat.py

## Phase 2: Foundational

- [x] T004 Define Conversation and Message models in backend/src/models.py
- [x] T005 [P] Create database migration for Conversation and Message tables
- [x] T006 [P] Implement base MCP Tool wrapper in backend/src/agents/tools.py
- [x] T007 Implement stateless Task MCP tools in backend/src/agents/tools.py

## Phase 3: [US1] Natural Language Task Creation (P1)

**Story Goal**: Users can create tasks using natural language via the chat interface.
**Independent Test Criteria**: Send "Add 'Buy milk'" to `/api/chat` and verify task creation in DB.

- [x] T008 [US1] Implement 'create_task' MCP tool in backend/src/agents/tools.py
- [x] T009 [US1] Define AI Chatbot agent with 'create_task' tool in backend/src/agents/chatbot.py
- [x] T010 [US1] Create POST /api/chat endpoint in backend/src/routes/chat.py (minimal for creation)
- [x] T011 [US1] Register chat router in backend/src/main.py
- [x] T012 [US1] Implement basic Chat UI component in frontend/src/app/chat/page.tsx
- [x] T013 [US1] Implement chat service in frontend/src/services/chat.ts

## Phase 4: [US2] Managing Tasks via Chat (P2)

**Story Goal**: Users can list, complete, and delete tasks via chat.
**Independent Test Criteria**: Send "Show my tasks" and "Complete buy milk" and verify updates.

- [x] T014 [US2] Implement 'list_tasks', 'update_task', 'delete_task' MCP tools in backend/src/agents/tools.py
- [x] T015 [US2] Update Chatbot agent to support new tools in backend/src/agents/chatbot.py
- [x] T016 [US2] Update /api/chat to handle diverse task intents in backend/src/routes/chat.py

## Phase 5: [US3] Persistent Conversational Context (P3)

**Story Goal**: Conversation history is stored and reconstructed for context.
**Independent Test Criteria**: Send two related messages and verify agent remembers first.

- [x] T017 [US3] Implement message persistence logic in backend/src/routes/chat.py
- [x] T018 [US3] Implement history reconstruction (last 10 messages) in backend/src/routes/chat.py
- [x] T019 [US3] Update Chatbot agent to process history context in backend/src/agents/chatbot.py

## Phase 6: Polish & Cross-cutting

- [x] T020 Implement error handling and clarification prompts in backend/src/agents/chatbot.py
- [x] T021 Add loading states and tool-call indicators to frontend/src/app/chat/page.tsx
- [x] T022 [P] Create integration tests for end-to-end chat flow in backend/tests/integration/test_chat.py

## Dependencies

1. US1 depends on Phase 2 (Foundational)
2. US2 depends on US1
3. US3 depends on US1

## Parallel Execution

- T005 and T006 can be done in parallel (DB vs Code).
- T012 and T013 can be done in parallel (UI vs Service).
- T022 can be started after T011.

## Implementation Strategy

1. **MVP**: Implement T001-T013 to achieve P1 (Task creation via chat).
2. **Incremental**: Add US2 (Management) followed by US3 (Context).
3. **Polish**: Finalize with error handling and UI enhancements.
