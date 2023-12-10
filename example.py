from action import ActionType, QuoridorAction
from board import QuoridorBoard


def example_actions_1(board: QuoridorBoard):
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=0, y=0),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=0, y=7),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=3, y=0),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=1, y=1),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=0),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=2, y=0),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=5, y=0),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=8),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=7),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=6),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=5),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=4),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=3),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=2),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=1),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=6, y=1),
    )
    board.action_player(
        player=2,
        action=QuoridorAction(action_type=ActionType.MOVE, x=7, y=1),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.MOVE, x=6, y=0),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.MOVE, x=7, y=0),
    )
    board.action_player(
        player=1,
        action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=6, y=1),
    )
