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
from config import BOARD_SIZE, WALL_COUNT


class QuoridorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.board = QuoridorBoard(size=BOARD_SIZE, wall_count=WALL_COUNT)
        self.BOARD_SIZE = self.board.size

        for action in QuoridorAction.all_actions():
            if self.board.is_valid_action(player=1, action=action):
                print(action)

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
        state = self.board.state()

        x, y = state["my_position"]
        player_circle = QGraphicsEllipseItem(
            x * 50 + 5, (self.BOARD_SIZE - y - 1) * 50 + 5, 40, 40
        )
        player_circle.setBrush(QBrush(player_colors[1]))
        self.scene.addItem(player_circle)

        enemy_x, enemy_y = state["enemy_position"]
        enemy_circle = QGraphicsEllipseItem(
            enemy_x * 50 + 5, (self.BOARD_SIZE - enemy_y - 1) * 50 + 5, 40, 40
        )
        enemy_circle.setBrush(QBrush(player_colors[2]))
        self.scene.addItem(enemy_circle)

    def drawWalls(self):
        wall_color = Qt.black
        for wall_x, wall_y in self.board.state()["vertical_walls"]:
            wall_rect = QGraphicsRectItem(
                (wall_x + 1) * 50 - 2, (self.BOARD_SIZE - wall_y - 2) * 50, 4, 100
            )
            wall_rect.setBrush(QBrush(wall_color))
            self.scene.addItem(wall_rect)

        for wall_x, wall_y in self.board.state()["horizontal_walls"]:
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
