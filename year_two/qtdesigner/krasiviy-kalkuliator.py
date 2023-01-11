from math import factorial, sqrt
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)

        self.expr = ""
        self.res = ""
        self.digits = ""
        self.update_lcd(0)
        self.buttonGroup_digits.buttonClicked.connect(self.act_digit)
        self.buttonGroup_binary.buttonClicked.connect(self.act_binary)
        self.btn_clear.clicked.connect(self.act_action)
        self.btn_dot.clicked.connect(self.act_action)
        self.btn_eq.clicked.connect(self.act_action)
        self.btn_fact.clicked.connect(self.act_action)
        self.btn_sqrt.clicked.connect(self.act_action)

    def act_digit(self, object):
        digit = object.objectName()[-1]
        self.expr += digit
        self.digits += digit
        self.res = self.digits
        self.update_lcd(float(self.res))

    def act_binary(self, object):
        cond = object.objectName()
        if cond == "btn_div":
            self.expr += "/"
        if cond == "btn_minus":
            self.expr += "-"
        if cond == "btn_mult":
            self.expr += "*"
        if cond == "btn_plus":
            self.expr += "+"
        if cond == "btn_pow":
            self.expr += "**"
        self.res = ""
        self.digits = ""

    def act_action(self):
        cond = self.sender().objectName()
        if cond == "btn_clear":
            self.expr = ""
            self.res = ""
            self.digits = ""
            self.update_lcd(0)
        if cond == "btn_dot":
            self.expr += "."
            self.res += "."
            self.digits += "."
        if cond == "btn_eq":
            self.expr = str(eval(self.expr))
            self.res = self.expr
            self.digits = ""
            self.update_lcd(float(self.expr))
        if cond == "btn_fact":
            self.expr = str(factorial(float(self.res)))
            self.res = self.expr
            self.digits = ""
            self.update_lcd(float(self.expr))
        if cond == "btn_sqrt":
            self.expr = str(sqrt(float(self.res)))
            self.res = self.expr
            self.digits = ""
            self.update_lcd(float(self.expr))

    def update_lcd(self, number):
        self.table.display(number)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
