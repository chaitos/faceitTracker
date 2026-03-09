import uvicorn, asyncio
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from pathlib import Path
from fastapi.staticfiles import StaticFiles




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


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"

if FRONTEND_DIST.exists():
    app.mount(
        "/assets",
        StaticFiles(directory=FRONTEND_DIST / "assets"),
        name="assets"
    )


@app.post("/api/tracked-players/", response_model=TrackedPlayerResponse)
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


@app.get("/api/tracked-players/", response_model=list[TrackedPlayerResponse])
def getTrackedPlayers(db: Session = Depends(get_db)):
    return  get_tracked_players(db)



@app.delete("/api/tracked-players/{player_id}", status_code=204)
def deletTrackedPlayer(player_id: str, db: Session = Depends(get_db)):
    delete_tracked_player(db, player_id)

    return {"detail": "Игрок удалён"}




from fastapi.responses import FileResponse


@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_path = FRONTEND_DIST / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    raise HTTPException(status_code=404)



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True
    )



