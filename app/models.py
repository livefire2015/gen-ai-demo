from pydantic import BaseModel

class TaskInput(BaseModel):
    description: str

class TaskOutput(BaseModel):
    output: str

class ForecastInput(BaseModel):
    query: str

class QueryInput(BaseModel):
    query: str
