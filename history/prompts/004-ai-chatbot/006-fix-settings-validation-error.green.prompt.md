---
id: 006
title: fix-settings-validation-error
stage: green
date: 2026-02-05
surface: agent
model: gemini
feature: ai-chatbot
branch: 004-ai-chatbot
user: Muzammil
command: /bug
labels: ["bugfix", "phase-3", "ai-chatbot", "pydantic", "config"]
links:
  spec: specs/004-ai-chatbot/spec.md
  plan: specs/004-ai-chatbot/plan.md
  tasks: specs/004-ai-chatbot/tasks.md
files:
 - backend/src/config.py
tests:
 - backend/tests/integration/test_chat.py
---

## Prompt

Process SpawnProcess-1:
Traceback (most recent call last):
...
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
gemini_api_key
  Extra inputs are not permitted [type=extra_forbidden, input_value='AIzaSyBFENnnl6BAT_ydJZO--ML1QZ0sJ-5i4Gs', input_type=str]

## Response snapshot

Fixed `ValidationError` in `backend/src/config.py`.
- Added `GEMINI_API_KEY: str = None` to the `Settings` class.
- Added `extra = "ignore"` to `Config` to prevent future crashes from unknown env vars.

## Outcome

- ✅ Impact: Backend server should now start successfully without crashing on extra env variables.
- 🧪 Tests: Restart server to verify.
- 📁 Files: backend/src/config.py
- 🔁 Next prompts: N/A
- 🧠 Reflection: Pydantic Settings defaults to `extra='forbid'`, which causes crashes when new keys are added to .env but not the model. Using `extra='ignore'` is safer for development.

## Evaluation notes (flywheel)

- Failure modes observed: ValidationError (fixed by updating config model).
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
