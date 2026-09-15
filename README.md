# Mini Cursor

An autonomous AI coding agent built with Python.

## Features

- AI task planning
- Code generation
- File management
- Code execution
- Error correction

## Tech Stack

- Python
- LLM API
- Agent Architecture
-                   User
                    │
                    ▼
               main.py
                    │
                    ▼
          Agent Workflow
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Planner        Coder        Reviewer
      │             │             ▲
      └─────────────┼─────────────┘
                    ▼
                 AgentState
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   File Tool              Runner Tool
        │                       │
        ▼                       ▼
   workspace              Python Process
