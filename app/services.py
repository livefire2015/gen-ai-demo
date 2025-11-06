import asyncio
import sys
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP
import time
from app.models import TaskOutput

# Load environment variables
load_dotenv()

mcp_server_url = os.getenv('MCP_SERVER_URL', 'http://localhost:8080/mcp')
server = MCPServerStreamableHTTP(mcp_server_url)

agent = Agent(
    'openai:gpt-5',
    output_type=[TaskOutput, str],
    # mcp_servers=[server],
    system_prompt=('Generate a task title and priority based on the description.'),
)

async def generate_task(prompt: str) -> TaskOutput | str:
    result = await agent.run(prompt)
    return result.output
