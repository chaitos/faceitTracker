from datetime import datetime, timedelta
from fastapi import HTTPException

import httpx

from backend.enums import PlayerStatus
from backend.config import FACEIT_API_KEY




async def get_last_match(player_id: str) -> dict:
    headers = {"Authorization": f"Bearer {FACEIT_API_KEY}"}

    async with httpx.AsyncClient(
        base_url="https://open.faceit.com/data/v4",
        headers=headers,
        timeout=10.0
    ) as client:

        r = await client.get(
            f"/players/{player_id}/history",
            params={"game": "cs2", "limit": 1}
        )

        if r.status_code != 200:
            raise Exception("Failed to get match history")

        items = r.json().get("items", [])

        if not items:
            return {
                "last_activity_at": None,
                "last_match_id": None,
                "match_status": None
            }

        match = items[0]
        match_id = match["match_id"]

        # ⬇️ ВТОРОЙ ЗАПРОС
        match_resp = await client.get(f"/matches/{match_id}")
        if match_resp.status_code != 200:
            raise Exception("Failed to get match details")

        match_data = match_resp.json()

        return {
            "last_activity_at": datetime.utcfromtimestamp(
                match["finished_at"] or match["started_at"]
            ),
            "last_match_id": match_id,
            "match_status": match_data["status"]  # ONGOING / FINISHED
        }


def calculate_player_status(last_match: dict) -> PlayerStatus:
    if not last_match["last_activity_at"]:
        return PlayerStatus.OFFLINE

    if last_match["match_status"] == "ONGOING":
        return PlayerStatus.IN_MATCH

    now = datetime.utcnow()
    diff = now - last_match["last_activity_at"]

    if diff <= timedelta(minutes=15):
        return PlayerStatus.RECENT_MATCH

    if diff <= timedelta(hours=1):
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
