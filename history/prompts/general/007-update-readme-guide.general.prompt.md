---
id: 007
title: Update README Guide
stage: general
date: 2026-01-01
surface: agent
model: gemini
feature: cli-todo-app
branch: 001-cli-todo-app
user: Muzammil
command: "Update README"
labels: ["docs", "readme", "guide"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - README.md
tests:
 - none
---

## Prompt

Update the readme.md file showing steps that how to use this application.It will serve as a guide

## Response snapshot

Updated README.md with a comprehensive user guide, including sections for installation, command usage (add, list, done, update, delete), global options, and testing instructions.

## Outcome

- ✅ Impact: Improved user onboarding and documentation
- 🧪 Tests: N/A
- 📁 Files: README.md
- 🔁 Next prompts: None
- 🧠 Reflection: Detailed guides help users understand CLI syntax more quickly.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard
- Next experiment (smallest change to try): None
