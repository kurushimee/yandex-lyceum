import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QLineEdit, QMainWindow


class W_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        edit1 = QLineEdit(self)
        edit1.move(50, 15)

        check1 = QCheckBox(self)
        check1.move(15, 15)
        check1.stateChanged.connect(self.on_checked)

    def on_checked(self, checked):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = W_MainWindow()
    ex.show()
    sys.exit(app.exec_())
