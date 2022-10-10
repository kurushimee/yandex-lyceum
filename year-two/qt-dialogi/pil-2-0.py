import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QFileDialog,
    QPushButton,
)

SCREEN_SIZE = [400, 400]


class W_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle("PIL 2.0")

        self.fname = QFileDialog.getOpenFileName(
            self, "Open", "", "*.jpg;;*.png;;*.bmp;;All Files (*.*)"
        )[0]
        self.ename = f"edit.{self.fname[-3:]}"
        self.image = QLabel(self)
        self.image.move(100, 15)
        self.image.resize(300, 300)
        self.set_color()
        self.update_pixmap()

        self.R = QPushButton("R", self)
        self.G = QPushButton("G", self)
        self.B = QPushButton("B", self)
        self.RGB = QPushButton("RGB", self)
        self.counterclockwise = QPushButton("Counterclockwise", self)
        self.clockwise = QPushButton("Clockwise", self)

        self.R.resize(100, 30)
        self.G.resize(100, 30)
        self.B.resize(100, 30)
        self.RGB.resize(100, 30)
        self.counterclockwise.resize(200, 30)
        self.clockwise.resize(200, 30)

        self.R.move(0, 30)
        self.G.move(0, 90)
        self.B.move(0, 150)
        self.RGB.move(0, 210)
        self.counterclockwise.move(0, 330)
        self.clockwise.move(200, 330)

        self.R.clicked.connect(self.color_button)
        self.G.clicked.connect(self.color_button)
        self.B.clicked.connect(self.color_button)
        self.RGB.clicked.connect(self.color_button)
        self.counterclockwise.clicked.connect(self.rotate_button)
        self.clockwise.clicked.connect(self.rotate_button)

    def color_button(self):
        if self.sender().text() == "R":
            self.set_color((1, 0, 0))
        if self.sender().text() == "G":
            self.set_color((0, 1, 0))
        if self.sender().text() == "B":
            self.set_color((0, 0, 1))
        if self.sender().text() == "RGB":
            self.set_color()
        self.update_pixmap()

    def rotate_button(self):
        if self.sender().text() == "Counterclockwise":
            self.rotate(-90)
        if self.sender().text() == "Clockwise":
            self.rotate(90)
        self.update_pixmap()

    def update_pixmap(self):
        self.pixmap = QPixmap(self.ename)
        self.image.setPixmap(self.pixmap)

    def set_color(self, color=(1, 1, 1)):
        with Image.open(self.fname) as im:
            if color != (1, 1, 1):
                pixels = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        if im.mode == "RGBA":
                            r, g, b, a = pixels[i, j]
                            pixels[i, j] = (
                                r * color[0],
                                g * color[1],
                                b * color[2],
                                a,
                            )
                        else:
                            r, g, b = pixels[i, j]
                            pixels[i, j] = (
                                r * color[0],
                                g * color[1],
                                b * color[2],
                            )
            im.save(self.ename)

    def rotate(self, angle: int):
        with Image.open(self.ename) as im:
            im = im.rotate(angle, Image.Resampling.NEAREST, expand=1)
            im.save(self.ename)
        with Image.open(self.fname) as im:
            im = im.rotate(angle, Image.Resampling.NEAREST, expand=1)
            im.save(self.fname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = W_MainWindow()
    ex.show()
    sys.exit(app.exec_())
