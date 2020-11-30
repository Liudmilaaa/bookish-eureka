import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pai = False
        self.butn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.pai:
            circl = QPainter()
            circl.begin(self)
            self.draw(circl)
            circl.end()

    def paint(self):
        self.pai = True
        self.repaint()

    def draw(self, circl):
        b = random.randint(20, 300)
        circl.setBrush(QColor(255, 255, 0))
        circl.drawEllipse(random.randint(0, 800), random.randint(0, 600), b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
