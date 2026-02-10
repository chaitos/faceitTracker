import asyncio

from crud import get_tracked_players, update_tracked_player
from services.faceit_client import get_last_match, calculate_player_status
from database import SessionLocal


from database import SessionLocal

async def track_players():
    while True:
        db = SessionLocal()
        try:
            players = get_tracked_players(db)

            if not players:
                await asyncio.sleep(10)
                continue

            tasks = [
                get_last_match(player.player_id)
                for player in players
            ]

            results = await asyncio.gather(*tasks, return_exceptions=True)

            for player, result in zip(players, results):
                if isinstance(result, Exception):
                    continue

                status = calculate_player_status(result)

                update_tracked_player(
                    db=db,
                    player=player,
                    last_activity_at=result["last_activity_at"],
                    last_match_id=result["last_match_id"],
                    status=status
                )

        finally:
            db.close()

        await asyncio.sleep(10)