from fastapi import APIRouter
from app.models import TaskInput, TaskOutput, ForecastInput, QueryInput
from app.services import generate_task
from app.streaming import generate_forecast
from app.router_agent import execute_query
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/generate", response_model=TaskOutput)
async def generate(data: TaskInput):
    return await generate_task(data.description)

@router.post("/forecast")
async def forecast(data: ForecastInput):
    return StreamingResponse(
        generate_forecast(data.query),
        media_type="text/event-stream"
    )

@router.post("/query")
async def query(data: QueryInput):
    return await execute_query(data.query)
