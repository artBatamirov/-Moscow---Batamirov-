from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Circles(object):
    def setupUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton('push', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.ok)
