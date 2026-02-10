# Feature Specification: AI Chatbot System

**Feature Branch**: `004-ai-chatbot`  
**Created**: 2026-02-05  
**Status**: Draft  
**Input**: User description: "Phase 3 ## MyTodoApp · AI Chatbot ## Scope This specification defines **what the AI chatbot must do** in Phase 3. It does not define implementation details. --- ## Goal Enable users to **manage todos via natural language** through an AI chatbot while maintaining a **stateless server**, **tool-based execution**, and **persistent conversation history**. --- ## In-Scope Capabilities ### 1. Conversational Interface - Users interact using natural language - Single chat endpoint handles all messages - Responses are human-readable and action-confirming --- ### 2. Stateless Chat Processing - Server holds no session memory - Conversation context is rebuilt from database per request - Conversations survive server restarts --- ### 3. Task Management via Conversation The chatbot must support: - Creating tasks - Listing tasks (all, pending, completed) - Updating task title or description - Completing tasks - Deleting tasks All operations are user-scoped. --- ### 4. MCP Tool Invocation - AI agent must use MCP tools for all task operations - Agent cannot directly modify database - Each user intent maps to one or more tool calls - Tool outputs are returned to the user as confirmations --- ### 5. Conversation Persistence - Each chat belongs to a conversation - Messages are stored with role and timestamp - Conversation ID is returned with every response --- ### 6. Authentication & Authorization - JWT required for all chat requests - User identity derived from token only - Chatbot actions restricted to authenticated user --- ## Chat API Contract ### Endpoint `POST /api/chat` ### Request - `conversation_id` (optional) - `message` (required, natural language) ### Response - `conversation_id` - `response` (assistant message) - `tool_calls` (list of invoked tools) --- ## Natural Language Understanding The chatbot must correctly interpret: - Add / create / remember → create task - Show / list / view → list tasks - Done / complete / finished → complete task - Delete / remove / cancel → delete task - Change / update / rename → update task --- ## Error Handling - Gracefully handle invalid tasks - Ask for clarification on ambiguity - Never crash or expose internal errors --- ## Out of Scope - AI-generated task suggestions - Task sharing - Voice input - Notifications - Long-term agent memory beyond database --- ## Constraints - No deviation from Phase 1 & 2 task semantics - No hidden state - Spec-driven execution only --- ## Completion Criteria Phase 3 is complete when: - Users manage todos via natural language - All task actions go through MCP tools - Conversation state persists reliably - Server remains stateless - Behavior matches this specification exactly"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Natural Language Task Creation (Priority: P1)

As a user, I want to create a task using natural language so that I can quickly record my todos without using a form.

**Why this priority**: Core value proposition of the chatbot interface. It's the most common entry point for users.

**Independent Test**: Can be tested by sending a message like "Remind me to buy milk" and verifying a new task is created for the user.

**Acceptance Scenarios**:

1. **Given** an authenticated user, **When** they send "Add 'Buy milk' to my list", **Then** the system creates a task titled "Buy milk" and confirms it to the user.
2. **Given** an authenticated user, **When** they send "I need to finish the report by tomorrow", **Then** the system creates a task and extracts relevant details from the sentence.

---

### User Story 2 - Managing Tasks via Chat (Priority: P2)

As a user, I want to view, complete, and delete my tasks through the chat interface so that I have a consistent conversational experience for all task management.

**Why this priority**: Completes the CRUD cycle via chat, allowing users to stay within the conversational context.

**Independent Test**: Can be tested by asking "What are my tasks?" and then saying "Complete the first one" or "Delete buy milk".

**Acceptance Scenarios**:

1. **Given** a user has existing tasks, **When** they ask "Show my todos", **Then** the system lists their current tasks.
2. **Given** a user has a task "Buy milk", **When** they say "I've bought the milk", **Then** the system marks that specific task as completed.
3. **Given** a user has a task "Buy milk", **When** they say "Remove buy milk from my list", **Then** the system deletes the task.

---

### User Story 3 - Persistent Conversational Context (Priority: P3)

As a user, I want the chatbot to remember our conversation history so that I can refer back to previous messages or continue a multi-step task management flow.

**Why this priority**: Essential for a natural "chat" feel and supporting multi-turn interactions.

**Independent Test**: Can be tested by starting a conversation, sending several messages, and verifying that the system can still reference earlier parts of the chat (reconstructed from history).

**Acceptance Scenarios**:

1. **Given** a multi-turn conversation, **When** the user sends a message, **Then** the agent's response reflects the context of previous messages in that `conversation_id`.
2. **Given** a server restart, **When** a user continues an existing `conversation_id`, **Then** the history is preserved and the chat continues seamlessly.

---

### Edge Cases

- **Ambiguous Intent**: If a user says "Do it", the system should ask for clarification rather than guessing or failing.
- **Unauthorized Access**: If a message is sent without a valid JWT or to a conversation the user doesn't own, it must be rejected with a 401/403.
- **Invalid Conversation ID**: If a non-existent `conversation_id` is provided, the system should either start a new one or return an appropriate error.
- **Tool Failure**: If an MCP tool fails (e.g., database error), the agent should inform the user gracefully without exposing technical stack traces.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a `POST /api/chat` endpoint that accepts a natural language message and an optional `conversation_id`.
- **FR-002**: The chatbot MUST use an AI agent that maps user intent to specific task management actions (Create, List, Update, Complete, Delete).
- **FR-003**: The AI agent MUST NOT directly modify the database; it MUST use stateless MCP tools for all mutations.
- **FR-004**: The system MUST persist every message (user and assistant) in the database, associated with a `conversation_id` and `user_id`.
- **FR-005**: For every request, the system MUST reconstruct the conversation history from the database to provide context to the AI agent.
- **FR-006**: The system MUST return the `conversation_id` and the list of `tool_calls` made by the agent in the API response.
- **FR-007**: The system MUST derive the user's identity exclusively from a valid JWT provided in the request headers.
- **FR-008**: The system MUST ensure strict isolation, preventing users from accessing or modifying tasks or conversations belonging to others.

### Key Entities *(include if feature involves data)*

- **Conversation**: Represents a chat session. Contains multiple Messages. Linked to a User.
- **Message**: An individual entry in a conversation. Attributes: Role (User/Assistant), Content, Timestamp, Conversation ID.
- **Task**: The existing task entity from Phase 1/2, now also manageable via the chatbot.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully create a task via chat on the first attempt 95% of the time.
- **SC-002**: The average response time for the chat endpoint (including AI reasoning and tool calls) is under 3 seconds.
- **SC-003**: 100% of task mutations requested via chat are executed through the defined MCP tools.
- **SC-004**: Conversation history is 100% recoverable after a server restart using the `conversation_id`.
- **SC-005**: Zero instances of cross-user data leakage occur during chat interactions.

## Assumptions

- The AI model (Gemini) is capable of accurately mapping natural language to the provided MCP tool schemas.
- The existing MCP tools from previous phases are available or will be adapted to be stateless as per the constitution.
- The frontend (ChatKit) is compatible with the specified `/api/chat` contract.