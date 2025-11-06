dev:
	uvicorn app.main:app --reload

demo:
	curl -X POST http://localhost:8000/generate \
	  -H "Content-Type: application/json" \
	  -d '{"description": "find all users emails"}'

forecast:
	curl -X POST http://localhost:8000/forecast \
	  -H "Content-Type: application/json" \
	  -d '{"query": "What will the weather be like in Beijing on Friday?"}'

query-success:
	curl -X POST http://localhost:8000/query \
	  -H "Content-Type: application/json" \
	  -d '{"query": "Select the names and countries of all capitals"}'

query-sql-fail:
	curl -X POST http://localhost:8000/query \
	  -H "Content-Type: application/json" \
	  -d '{"query": "Select all pets"}'

query-router-fail:
	curl -X POST http://localhost:8000/query \
	  -H "Content-Type: application/json" \
	  -d '{"query": "How do I fly from Amsterdam to Mexico City?"}'
