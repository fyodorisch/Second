import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.nazh)
        self.proverka = False

    def paintEvent(self, event):
        if self.proverka is True:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            a = random.randint(40, 200)
            qp.drawEllipse(280, 180, a, a)
            a = random.randint(40, 200)
            qp.drawEllipse(150, 80, a, a)
            a = random.randint(40, 200)
            qp.drawEllipse(220, 400, a, a)
            a = random.randint(40, 200)
            qp.drawEllipse(500, 20, a, a)
            a = random.randint(40, 200)
            qp.drawEllipse(445, 390, a, a)
            qp.end()

    def nazh(self):
        self.proverka = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myW = Main()
    myW.show()

    sys.exit(app.exec())