from config import BOARD_SIZE
from enum import Enum


class ActionType(Enum):
    MOVE = "move"
    WALL_VERTICAL = "wall_vertical"
    WALL_HORIZONTAL = "wall_horizontal"


class QuoridorAction:
    def __init__(self, action_type: ActionType, x: int, y: int):
        self.action_type = action_type
        self.x = x
        self.y = y
