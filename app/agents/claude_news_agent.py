import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def run_claude_news_agent(query_text: str):
    options = ClaudeAgentOptions(
        allowed_tools=["WebSearch", "Read", "Bash"],  # we can expand later
        permission_mode="acceptAll"
    )
    
    async for message in query(
        prompt=f"Analyze NBA player news impact for props: {query_text}. "
               "Extract injury status, minutes restriction, sentiment score (-100 to +100), "
               "and a short reasoning. Return ONLY JSON.",
        options=options
    ):
        if message.type == "result":
            return message.content  # Claude returns structured JSON
    
    return {"error": "No result"}

# For sync FastAPI call
def run_claude_news_agent_sync(query_text: str):
    return asyncio.run(run_claude_news_agent(query_text))
