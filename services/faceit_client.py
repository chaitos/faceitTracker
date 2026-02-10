import asyncio
from datetime import datetime, timedelta
from fastapi import HTTPException

import httpx

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


async def get_player_by_nickname(nickname: str) -> dict:
    headers = {
        "Authorization": f"Bearer {FACEIT_API_KEY}"
    }

    async with httpx.AsyncClient(base_url="https://open.faceit.com/data/v4", headers=headers, timeout=10.0) as client:
        response = await client.get("/players", params={"nickname": nickname})
        print(FACEIT_API_KEY)
        if response.status_code != 200:
            raise Exception(
                f"Faceit API error {response.status_code}: {response.text}"
            )

        data = response.json()

        if "player_id" not in data:
            raise HTTPException(
                status_code=404,
                detail="Faceit player not found"
            )

        return data
