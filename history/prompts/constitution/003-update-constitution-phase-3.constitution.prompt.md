---
id: 003
title: update-constitution-phase-3
stage: constitution
date: 2026-02-05
surface: agent
model: gemini
feature: none
branch: main
user: Muzammil
command: /sp.constitution
labels: ["governance", "phase-3", "ai-chatbot"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 null
---

## Prompt

/sp.constitution Phase 3
## MyTodoApp · AI Chatbot System (Gemini)

## Role
You are an **AI systems engineer** building a **stateless, tool-driven Todo chatbot** using Gemini reasoning, MCP architecture, and agent-based execution.

---

## Constitutional Principles
- Specs are authoritative
- No hidden state in memory or server
- All intelligence flows through tools
- Conversation state persists only in database
- Agents reason first, then act
- Every action must be explainable and auditable

---

## Objective
Introduce a **natural-language chatbot interface** that allows users to manage todos conversationally, while preserving strict backend control through MCP tools.

---

## Core Capabilities
- Natural language task management
- Stateless chat processing
- Persistent conversation history
- Tool-based task execution
- Multi-user isolation
- Authentication-enforced access

---

## Architecture Law
- Frontend communicates only with `/api/chat`
- Backend holds no in-memory session state
- AI agents **cannot directly modify database**
- All task mutations occur via MCP tools
- MCP tools are stateless and deterministic

---

## Technology Mandate
| Component | Required Stack |
|--------|----------------|
| Frontend | OpenAI ChatKit |
| Backend | FastAPI |
| AI Logic | OpenAI Agents SDK |
| Tool Layer | Official MCP SDK |
| ORM | SQLModel |
| Database | Neon PostgreSQL |
| Auth | Better Auth |
| AI Reasoning | Gemini |

No substitutions or bypasses allowed.

---

## Security Constitution
- JWT required for all chat requests
- User identity derived only from token
- Agent never trusts user-provided user_id
- Tool calls validated against authenticated user
- Cross-user access is forbidden

---

## Agent Law
- Agent must infer intent before acting
- Agent must choose correct MCP tool
- Agent may chain tools if required
- Agent must confirm completed actions
- Agent must handle ambiguity safely
- Agent must fail gracefully

---

## MCP Tool Law
- Tools expose **only task operations**
- Tools accept validated parameters
- Tools return structured results
- Tools never contain business logic outside scope
- Tools do not store memory

---

## Conversation Law
- Each request is independent
- History is reconstructed from database
- Messages are stored before and after agent run
- Server restart must not affect continuity

---

## Non-Negotiables
- No direct DB access by agent
- No implicit memory
- No silent tool calls
- No user data leakage
- No deviation from specs

---

## Success Criteria
- Users manage tasks via natural language
- Agent reliably maps intent → tool
- Conversations resume after restart
- Server remains fully stateless
- System behaves deterministically and securely

## Response snapshot

Updated project constitution to v3.0.0.
- Replaced core principles with AI/Agent-centric laws.
- Updated technology stack to include OpenAI ChatKit, Agents SDK, and MCP.
- Established strict security and conversation state rules.
- Validated dependent templates (compatible).

## Outcome

- ✅ Impact: Updated constitution to v3.0.0 for Phase 3
- 🧪 Tests: N/A
- 📁 Files: Modified constitution.md
- 🔁 Next prompts: /sp.specify (to build the spec for Phase 3)
- 🧠 Reflection: Constitution updated to reflect AI Chatbot focus.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
