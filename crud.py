
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


def get_tracked_players(db: Session):
    players = db.query(TrackedPlayer).all()
    return players



def delete_tracked_player(player_id, db: Session):
    if not db.query(TrackedPlayer).get(player_id):
        return None, "игрока с таким айди нет в бд"
    player_to_delete = db.query(TrackedPlayer).get(player_id)
    db.delete(player_to_delete)
    db.commit()
    return None