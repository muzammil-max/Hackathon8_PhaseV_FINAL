---
id: 013
title: Fix Null Bytes SyntaxError and Restore CLI Handlers
stage: refactor
date: 2026-01-01
surface: agent
model: gemini
feature: cli-todo-advanced
branch: 002-cli-todo-advanced
user: Muzammil
command: "Fix SyntaxError"
labels: ["bug-fix", "encoding", "refactor"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/todo.py
 - src/cli.py
 - src/models.py
 - src/services.py
 - src/storage.py
 - src/utils.py
 - tests/integration/test_crud.py
tests:
 - tests/unit/
 - tests/integration/
---

## Prompt

Traceback (most recent call last):
 File "C:\Users\Muzammil\Desktop\Hackathon08\src\todo.py", line 11, in <module>
 from src import cliSyntaxError: source code string cannot contain null bytes

## Response snapshot

Resolved `SyntaxError: source code string cannot contain null bytes` by rewriting all source files in `src/` to ensure clean UTF-8 encoding. Restored missing `handle_done` and `handle_delete` functions in `src/cli.py` that were accidentally omitted during the rewrite. Updated `test_crud.py` to match the current CLI argument contract.

## Outcome

- ✅ Impact: Application is runnable again and all tests pass.
- 🧪 Tests: 19 unit tests and 6 integration tests passing.
- 📁 Files: All `src/*.py` files cleaned and verified.
- 🔁 Next prompts: None.
- 🧠 Reflection: Windows PowerShell and text redirection can sometimes introduce null bytes or incompatible encodings (UTF-16 BOM). Explicitly using `write_file` with clean strings is safer.

## Evaluation notes (flywheel)

- Failure modes observed: `SyntaxError` due to encoding; `NameError` due to missing functions; Test mismatch with CLI contract.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
