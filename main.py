import uvicorn, asyncio
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager


from schemas import TrackedPlayerResponse, AddTrackedPlayer
from deps import get_db
from crud import add_tracked_player, get_tracked_players, delete_tracked_player
from services.tracker import track_players
from services.faceit_client import get_player_by_nickname

# фоновый процесс
@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(track_players())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)



@app.post("/tracked-players/", response_model=TrackedPlayerResponse)
async def addTrackedPlayer(player: AddTrackedPlayer, db: Session = Depends(get_db)):
    status = 'ok'

    nickname = parse_query(player.query)
    faceit_player = await get_player_by_nickname(nickname)


    trackedPlayer, error = add_tracked_player(db, nickname=faceit_player['nickname'], player_id=faceit_player["player_id"])

    if error:
        raise HTTPException(status_code=400, detail=error)

    return trackedPlayer

# делает из ссылки профиля ник игрока
def parse_query(query: str):
    query = query.strip().rstrip("/")  # убираем пробелы и завершающий слеш
    nickname = query.split("/")[-1]  # берём последний сегмент
    return nickname


@app.get('/tracked-players/', response_model=list[TrackedPlayerResponse])
def getTrackedPlayers(db: Session = Depends(get_db)):
    return  get_tracked_players(db)



@app.delete('/tracked-players/{player_id}')
def deletTrackedPlayer(player_id: int, db: Session = Depends(get_db)):
    delete_tracked_player(player_id, db)
    return {
        f"игрок удален"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)