import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsRectItem,
    QGraphicsEllipseItem,
)
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QColor
from action import ActionType, QuoridorAction

from board import QuoridorBoard


class QuoridorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.board = QuoridorBoard()
        self.BOARD_SIZE = self.board.size
        self.board.action_player(
            player=1,
            action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=0, y=0),
        )
        self.board.action_player(
            player=2,
            action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=0, y=7),
        )
        self.board.action_player(
            player=1,
            action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=3, y=0),
        )
        self.board.action_player(
            player=2,
            action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=1, y=1),
        )
        self.board.action_player(
            player=1,
            action=QuoridorAction(action_type=ActionType.MOVE, x=5, y=0),
        )
        self.board.action_player(
            player=2,
            action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=2, y=0),
        )
        self.board.action_player(
            player=1,
            action=QuoridorAction(action_type=ActionType.WALL_HORIZONTAL, x=5, y=0),
        )

        for action in QuoridorAction.all_actions():
            print(action, self.board.is_valid_action(player=1, action=action))

        # print(
        #     self.board.is_valid_action(
        #         player=1,
        #         action=QuoridorAction(action_type=ActionType.WALL_VERTICAL, x=6, y=0),
        #     ),
        # )

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Quoridor Game")

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        self.drawBoard()
        self.drawPlayers()
        self.drawWalls()

    def drawBoard(self):
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                rect = QGraphicsRectItem(x * 50, y * 50, 50, 50)
                rect.setBrush(QBrush(Qt.white))
                self.scene.addItem(rect)

    def drawPlayers(self):
        player_colors = {1: Qt.red, 2: Qt.blue}
        for player, position in self.board.player_positions.items():
            x, y = position
            player_circle = QGraphicsEllipseItem(
                x * 50 + 5, (self.BOARD_SIZE - y - 1) * 50 + 5, 40, 40
            )
            player_circle.setBrush(QBrush(player_colors[player]))
            self.scene.addItem(player_circle)

    def drawWalls(self):
        wall_color = Qt.black
        for wall_x, wall_y in self.board.vertical_walls:
            wall_rect = QGraphicsRectItem(
                (wall_x + 1) * 50 - 2, (self.BOARD_SIZE - wall_y - 2) * 50, 4, 100
            )
            wall_rect.setBrush(QBrush(wall_color))
            self.scene.addItem(wall_rect)

        for wall_x, wall_y in self.board.horizontal_walls:
            wall_rect = QGraphicsRectItem(
                wall_x * 50, (self.BOARD_SIZE - wall_y - 1) * 50 - 2, 100, 4
            )
            wall_rect.setBrush(QBrush(wall_color))
            self.scene.addItem(wall_rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QuoridorGUI()
    ex.show()
    sys.exit(app.exec_())
