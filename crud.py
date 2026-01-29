
from sqlalchemy.orm import Session
from models import TrackedPlayer




MAX_PLAYERS = 20

def add_tracked_player(db:Session, nickname: str):
    if db.query(TrackedPlayer).filter_by(nickname=nickname).first():
        return None, "игрок с этим ником уже добавлен"

    if db.query(TrackedPlayer).count() > MAX_PLAYERS:
        return None, "Лимит игроков превышен, удалите кого-то прежде чем добавить"

    player = TrackedPlayer(
        nickname=nickname,
        status="unknown",
        last_activity_at="unknown",
        last_match_id="unknown"
    )
    db.add(player)
    db.commit()
    db.refresh(player)

    return player, None