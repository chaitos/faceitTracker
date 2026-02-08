from sqlalchemy import Integer, String, Column, DateTime
from database import Base

from enums import PlayerStatus


class TrackedPlayer(Base):
    __tablename__ = "tracked_players"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    player_id = Column(String, nullable=False, unique=True)
    status = Column(String, default=PlayerStatus.OFFLINE.value, nullable=False)
    last_activity_at = Column(DateTime, nullable=True)
    last_match_id = Column(String, nullable=True)

