import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from app import Circles


class Project(QMainWindow, Circles):
    def __init__(self):
        super().__init__()
        self.isok = False
        self.setupUI()

    def paintEvent(self, event):
        if self.isok:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.isok = False

    def ok(self):
        self.isok = True
        self.update()

    def draw(self, qp):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        r = randint(0, 200)
        qp.drawEllipse(randint(0, 200), randint(0, 200), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
