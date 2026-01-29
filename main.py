import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


from schemas import TrackedPlayerResponse, AddTrackedPlayer
from crud import add_tracked_player
from deps import get_db




app = FastAPI()


trackedPlayers = []

@app.post("/tracked-players/", response_model=TrackedPlayerResponse)
def addTrackedPlayer(player: AddTrackedPlayer):
    status = 'ok'
    nickname = parse_query(player.query)


    return {
        'status':status,
        "nickname": nickname
    }

def parse_query(query: str):
    query = query.strip().rstrip("/")  # убираем пробелы и завершающий слеш
    nickname = query.split("/")[-1]  # берём последний сегмент
    return nickname


@app.get("/ping/{something}/")
def hi(something):
    return {"message" : something}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)