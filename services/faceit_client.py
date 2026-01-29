import asyncio

from enums import PlayerStatus
from crud import get_tracked_player


async def get_last_match(nickname):
    await asyncio.sleep(1)
    last_match = {
        "nickname":nickname,
        "last_activity_at": '20.01.2026',
        "last_match_id": 1
                  }
    return last_match

def calculate_player_status(last_match):

    if last_match["last_activity_at"]:
        return PlayerStatus.IN_MATCH
    return PlayerStatus.OFFLINE
