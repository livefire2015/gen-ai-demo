# Generative AI Training App

A FastAPI app using Pydantic AI's Agent to generate structured outputs from natural language prompts.

## Run locally
```bash
cp .env.local .env
uvicorn app.main:app --reload
```

## API

### `POST /generate`
Generate a task with title and priority from a description.
- Input: `{ "description": "something to organize" }`
- Output: `{ "title": "...", "priority": "..." }`

### `POST /forecast`
Stream a weather forecast response.
- Input: `{ "query": "weather question" }`
- Output: Server-sent events stream

### `POST /query`
Demonstrates pydantic-ai output functions with router/SQL agent pattern.
- Input: `{ "query": "natural language query" }`
- Output: List of rows or error response

Example queries:
- `"Select the names and countries of all capitals"` - Returns capital cities
- `"Select all pets"` - Returns SQL error (table not found)
- `"How do I fly from Amsterdam to Mexico City?"` - Returns router error (no appropriate agent)

Test with: `make query-success`, `make query-sql-fail`, or `make query-router-fail`