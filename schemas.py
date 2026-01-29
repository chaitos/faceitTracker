from pydantic import BaseModel

from enums import PlayerStatus

class AddTrackedPlayer(BaseModel):
    query: str



class TrackedPlayerResponse(BaseModel):
    id: int
    nickname: str
    status: PlayerStatus
    last_activity_at: str
    last_match_id: str

    class Config:
        from_attributes = True