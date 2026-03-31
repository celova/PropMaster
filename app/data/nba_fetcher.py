from nba_api.live.endpoints import scoreboard
from nba_api.stats.static import teams
import json

def get_todays_games():
    board = scoreboard.ScoreBoard()
    games = board.get_dict()["scoreboard"]["games"]
    return [
        {
            "game_id": g["gameId"],
            "home": g["homeTeam"]["teamTricode"],
            "away": g["awayTeam"]["teamTricode"],
            "status": g["gameStatusText"]
        } for g in games
    ]
