from pydantic import BaseModel


class AddTrackedPlayer(BaseModel):
    query: str

class TrackedPlayerResponse(BaseModel):
    status: str
    nickname: str
