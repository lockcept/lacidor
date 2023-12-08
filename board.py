from action import ActionType, QuoridorAction
from config import BOARD_SIZE, WALL_COUNT


class QuoridorBoard:
    def __init__(self):
        self.size = BOARD_SIZE
        self.player_positions = {
            1: (self.size // 2, 0),
            2: (self.size // 2, self.size - 1),
        }
        self.player_wall_counts = {1: WALL_COUNT, 2: WALL_COUNT}
        self.vertical_walls = set()
        self.horizontal_walls = set()

    def is_valid_action(self, player, action: QuoridorAction):
        if player not in (1, 2):
            raise ValueError("플레이어 번호는 1 또는 2여야 합니다.")

        if action.action_type == ActionType.MOVE:
            x, y = action.x, action.y
            if not (0 <= x < self.size) or not (0 <= y < self.size):
                return False

            if (x, y) == self.player_positions[player]:
                return False
            if (x, y) == self.player_positions[3 - player]:
                return False

            old_x, old_y = self.player_positions[player]
            if (abs(old_x - x) + abs(old_y - y)) != 1:
                return False
                # todo: 사실 뛰어넘기가 가능함

            if x != old_x:
                if (min(old_x, x), y) in self.vertical_walls:
                    return False
                if (min(old_x, x), y - 1) in self.vertical_walls:
                    return False

            if y != old_y:
                if (x, min(old_y, y)) in self.horizontal_walls:
                    return False
                if (x - 1, min(old_y, y)) in self.horizontal_walls:
                    return False

        elif action.action_type == ActionType.WALL_VERTICAL:
            if self.player_wall_counts[player] == 0:
                return False
            x, y = action.x, action.y
            if not (0 <= x < self.size - 1) or not (0 <= y < self.size - 1):
                return False

            if (x, y) in self.horizontal_walls:
                return False
            if (
                (x - 1, y) in self.vertical_walls
                or (x, y) in self.vertical_walls
                or (x + 1, y) in self.vertical_walls
            ):
                return False

        elif action.action_type == ActionType.WALL_HORIZONTAL:
            if self.player_wall_counts[player] == 0:
                return False
            x, y = action.x, action.y
            if not (0 <= x < self.size - 1) or not (0 <= y < self.size - 1):
                return False

            if (x, y) in self.vertical_walls:
                return False
            if (
                (x - 1, y) in self.horizontal_walls
                or (x, y) in self.horizontal_walls
                or (x + 1, y) in self.horizontal_walls
            ):
                return False

        # todo: 사실 벽으로 길을 막으면 안 됨

        return True

    def action_player(self, player: int, action: QuoridorAction):
        if self.is_valid_action(player, action):
            if action.action_type == ActionType.MOVE:
                self.player_positions[player] = (action.x, action.y)
            elif action.action_type == ActionType.WALL_VERTICAL:
                self.vertical_walls.add((action.x, action.y))
                self.player_wall_counts[player] -= 1
            elif action.action_type == ActionType.WALL_HORIZONTAL:
                self.horizontal_walls.add((action.x, action.y))
                self.player_wall_counts[player] -= 1

    def state(self, player=1):
        enemy_player = 3 - player
        state = {
            "my_position": self.player_positions[player],
            "enemy_position": self.player_positions[enemy_player],
            "my_wall_count": self.player_wall_counts[player],
            "enemy_wall_count": self.player_wall_counts[enemy_player],
            "vertical_walls": list(self.vertical_walls),
            "horizontal_walls": list(self.horizontal_walls),
        }
        return state
