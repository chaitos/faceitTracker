from datetime import datetime

from sqlalchemy.orm import Session
from models import TrackedPlayer
from enums import PlayerStatus



MAX_PLAYERS = 20

def add_tracked_player(
        db:Session, nickname: str,
        player_id: str,
        last_activity_at: str | None = None,
        last_match_id: str | None = None,):
    if db.query(TrackedPlayer).filter_by(player_id=player_id).first():
        return None, "такой игрок уже добавлен"

    if db.query(TrackedPlayer).count() >= MAX_PLAYERS:
        return None, "Лимит игроков превышен, удалите кого-то прежде чем добавить"

    player = TrackedPlayer(
        nickname=nickname,
        status=PlayerStatus.OFFLINE.value,
        player_id=player_id,
        last_activity_at=last_activity_at,
        last_match_id=last_match_id
    )
    db.add(player)
    db.commit()
    db.refresh(player)

    return player, None


def get_tracked_players(db: Session):

    players = db.query(TrackedPlayer).all()
    return players

def get_tracked_player(db: Session, nickname: str):
    player = db.query(TrackedPlayer).filter_by(nickname=nickname).first()
    return player


def delete_tracked_player(db: Session, player_id):
    if not db.query(TrackedPlayer).get(player_id):
        return None, "игрока с таким айди нет в бд"
    player_to_delete = db.query(TrackedPlayer).get(player_id)
    db.delete(player_to_delete)
    db.commit()
    return None


def update_tracked_player(db: Session, player: TrackedPlayer, last_activity_at: datetime, last_match_id: int, status: PlayerStatus):
    player.last_activity_at = last_activity_at
    player.last_match_id = last_match_id
    player.status = status.value

    db.commit()
