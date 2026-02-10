from xmlrpc.client import DateTime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from enums import PlayerStatus

class AddTrackedPlayer(BaseModel):
    query: str




class TrackedPlayerResponse(BaseModel):
    id: int
    nickname: str
    player_id : str
    status: PlayerStatus
    last_activity_at: Optional[datetime] = None
    last_match_id: Optional[str] = None

    class Config:
        from_attributes = True