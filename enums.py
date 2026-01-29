from enum import Enum

class PlayerStatus(str, Enum):
    OFFLINE = "offline"
    SEARCHING = "searching"
    IN_MATCH = "in_match"