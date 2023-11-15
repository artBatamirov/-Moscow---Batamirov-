import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton('push', self)
        self.btn.move(10, 10)
        self.isok = False
        self.btn.clicked.connect(self.ok)

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
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        r = randint(0, 200)
        qp.drawEllipse(randint(0, 200), randint(0, 200), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
