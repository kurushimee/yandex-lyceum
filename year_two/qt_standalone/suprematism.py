import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPoint, Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.circle = False
        self.square = False
        self.triangle = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 640, 512)
        self.setWindowTitle('Супрематизм')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.paint("triangle")

    def mousePressEvent(self, event):
        self.x = int(event.x())
        self.y = int(event.y())
        if (event.button() == Qt.LeftButton):
            self.paint("circle")
        elif (event.button() == Qt.RightButton):
            self.paint("square")

    def paint(self, type):
        if type == "circle":
            self.circle = True
        elif type == "square":
            self.square = True
        elif type == "triangle":
            self.triangle = True
        self.repaint()

    def paintEvent(self, event):
        if self.circle or self.square or self.triangle:
            qp = QPainter()
            qp.begin(self)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            size = randint(0, 100)
            qp.setBrush(color)
            if self.circle:
                self.draw_a_circle(qp, size)
                self.circle = False
            elif self.square:
                self.draw_a_square(qp, size)
                self.square = False
            elif self.triangle:
                self.draw_a_triangle(qp, size)
                self.triangle = False
            qp.end()

    def draw_a_circle(self, qp, size):
        qp.drawEllipse(self.x, self.y, size, size)

    def draw_a_square(self, qp, size):
        qp.drawRect(self.x, self.y, size, size)

    def draw_a_triangle(self, qp, size):
        x = self.x
        y = self.y
        polygon = QPolygon([
            QPoint(x - 5, y + 5),
            QPoint(x, y),
            QPoint(x + 5, y),
        ])
        qp.drawPolygon(polygon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
