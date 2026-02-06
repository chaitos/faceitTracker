import asyncio
from datetime import datetime, timedelta


from enums import PlayerStatus
from crud import get_tracked_player
from config import FACEIT_API_KEY




async def get_last_match(nickname):
    await asyncio.sleep(1)
    last_match = {
        "nickname":nickname,
        "last_activity_at": datetime.utcnow() - timedelta(minutes=5),
        "last_match_id": 1
                  }
    return last_match

def calculate_player_status(last_match):
    now = datetime.utcnow()
    diff = now - last_match["last_activity_at"]

    if diff < timedelta(minutes=0):
        return PlayerStatus.IN_MATCH

    if diff <= timedelta(minutes=15):
        return PlayerStatus.SEARCHING
    return PlayerStatus.OFFLINE
