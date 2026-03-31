from fastapi import FastAPI
from app.data.nba_fetcher import get_todays_games
from app.agents.claude_news_agent import run_claude_news_agent

app = FastAPI(title="NBA Props Predictor")

@app.get("/")
async def root():
    return {"message": "🚀 NBA Props Predictor API is live. Phase 0 complete!"}

@app.get("/test-claude")
async def test_claude():
    result = run_claude_news_agent("LeBron James ankle injury news today")
    return {"claude_agent_result": result}

@app.get("/todays-games")
async def todays_games():
    games = get_todays_games()
    return {"games": games}
