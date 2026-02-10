# Research: AI Chatbot System

## Decision 1: OpenAI Agents SDK for Gemini
- **Decision**: Use `openai-agents` SDK (or equivalent wrapper) to orchestrate Gemini via the OpenAI-compatible API.
- **Rationale**: Provides a structured way to define agents, handoffs, and tool usage that aligns with the "Agents reason first" principle.
- **Alternatives considered**: Direct Gemini API calls. Rejected because orchestrating multi-turn chat with tool calls is more robust with a dedicated agents SDK.

## Decision 2: MCP Tooling Implementation
- **Decision**: Implement task management tools using the Official MCP SDK as a separate internal "server" or module that the Agent invokes.
- **Rationale**: Enforces the "MCP Tool Law" from the constitution, ensuring agents cannot bypass tool-based validation for database access.
- **Alternatives considered**: Direct function calling within the agent. Rejected to maintain strict "tool-driven intelligence" and modularity.

## Decision 3: Conversation History Reconstruction
- **Decision**: Fetch the last 10-20 messages from the database for the given `conversation_id` and inject them into the agent's prompt context for every request.
- **Rationale**: Satisfies the "Stateless Chat Processing" requirement. Since the server holds no memory, the DB is the only source of truth for context.
- **Alternatives considered**: Client-side history sending. Rejected because it's less secure and harder to manage for long conversations.

## Decision 4: Multi-User Isolation in Tools
- **Decision**: Pass the `user_id` (extracted from JWT) to every MCP tool call. The tool itself must include `WHERE user_id = :user_id` in its SQLModel queries.
- **Rationale**: Ensures "Security First" and "Multi-user isolation". The agent should not be able to "forget" the user context and access other users' data.
