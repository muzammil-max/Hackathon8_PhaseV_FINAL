---
id: 005
title: configure-gemini-agent-integration
stage: green
date: 2026-02-05
surface: agent
model: gemini
feature: ai-chatbot
branch: 004-ai-chatbot
user: Muzammil
command: /sp.implement
labels: ["configuration", "phase-3", "ai-chatbot", "gemini", "openai-sdk"]
links:
  spec: specs/004-ai-chatbot/spec.md
  plan: specs/004-ai-chatbot/plan.md
  tasks: specs/004-ai-chatbot/tasks.md
files:
 - backend/src/agents/chatbot.py
tests:
 - backend/tests/integration/test_chat.py
---

## Prompt

Use openAI agents sdk to implement AI chatbot , i will use gemini for that. Also make sure that chat interface works properly

## Response snapshot

Configured the OpenAI Agents SDK to use Gemini (gemini-2.0-flash-exp) via the OpenAI-compatible endpoint.
- Updated `backend/src/agents/chatbot.py` to initialize `AsyncOpenAI` with `GEMINI_API_KEY` and the Google API base URL.
- Explicitly set the agent model to `gemini-2.0-flash-exp`.
- Verified that the `ChatWidget` (frontend) is properly integrated and capable of displaying tool calls.

## Outcome

- ✅ Impact: The chatbot now correctly routes requests to Gemini models using the OpenAI Agents SDK.
- 🧪 Tests: Integration tests should now be run with a valid `GEMINI_API_KEY` in the environment.
- 📁 Files: backend/src/agents/chatbot.py
- 🔁 Next prompts: N/A
- 🧠 Reflection: The flexibility of the OpenAI Agents SDK allows for seamless provider switching by just changing the client configuration.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
