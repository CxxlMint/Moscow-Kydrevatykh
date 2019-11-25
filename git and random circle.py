import sys, math, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QMouseEvent, QImage
from PyQt5.QtCore import Qt
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
global CJ, gosha
CJ = 0
gosha = ''


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.flag2 = False
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.initUI()

    def initUI(self):
        self.resize(500,500)
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255,255,255))
        self.button = QtWidgets.QPushButton("Click", self)
        self.button.move(40, 40)
        self.paint = QPainter(self.image)
        self.button.clicked.connect(self.ellips)
        self.show()
        self.update()

    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)
        paint.begin(self)
        paint.end()

    def ellips(self):
        x = random.randint(1, 450)
        y = random.randint(1, 450)
        h = random.randint(6, 50)
        ch = random.randint(0, 4)
        snoop = ['purple', 'red', 'yellow', 'black', 'green']
        for i in range(2):
            self.update()
            self.paint.setBrush(QColor(snoop[ch]))
            self.paint.drawEllipse(x, y, h, h)
            self.update()


app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())