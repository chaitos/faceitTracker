import asyncio

from crud import get_tracked_players
from services.faceit_client import get_last_match
from services.faceit_client import calculate_player_status
from database import SessionLocal


from database import SessionLocal

async def track_players():
    while True:
        db = SessionLocal()
        try:
            players = get_tracked_players(db)

            tasks = [
                get_last_match(player.nickname)
                for player in players
            ]

            results = await asyncio.gather(*tasks)

            for player, last_match in zip(players, results):
                status = calculate_player_status(
                    last_match["last_activity_at"]
                )

                player.status = status.value
                player.last_activity_at = last_match["last_activity_at"]
                player.last_match_id = last_match["last_match_id"]

            db.commit()
        finally:
            db.close()

        await asyncio.sleep(10)

