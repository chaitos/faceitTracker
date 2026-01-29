import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


from schemas import TrackedPlayerResponse, AddTrackedPlayer
from deps import get_db
from crud import add_tracked_player, get_tracked_players, delete_tracked_player



app = FastAPI()



@app.post("/tracked-players/", response_model=TrackedPlayerResponse)
def addTrackedPlayer(player: AddTrackedPlayer, db: Session = Depends(get_db)):
    status = 'ok'
    nickname = parse_query(player.query)

    trackedPlayer, error = add_tracked_player(db, nickname)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        'status':status,
        "nickname": trackedPlayer.nickname
    }

# делает из ссылки профиля ник игрока
def parse_query(query: str):
    query = query.strip().rstrip("/")  # убираем пробелы и завершающий слеш
    nickname = query.split("/")[-1]  # берём последний сегмент
    return nickname


@app.get('/tracked-players/')
def getTrackedPlayers(db: Session = Depends(get_db)):
    return {
        "players" : get_tracked_players(db)
    }


@app.delete('/tracked-players/{player_id}')
def deletTrackedPlayer(player_id: int, db: Session = Depends(get_db)):
    delete_tracked_player(player_id, db)
    return {
        f"игрок удален"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)