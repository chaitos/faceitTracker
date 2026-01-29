import asyncio

from crud import get_tracked_players
from services.faceit_client import get_last_match
from services.faceit_client import calculate_player_status



async def track_players():
    while True:
        players = get_tracked_players()
        tasks = [get_last_match(player.nickname) for player in players]

        results = await asyncio.gather(*tasks)

        for last_match in results:
            calculate_player_status(last_match)

        await asyncio.sleep(10)