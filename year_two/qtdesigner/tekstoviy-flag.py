import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 658, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget
        )
        self.horizontalLayout.setContentsMargins(25, 25, 25, 25)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.blue1 = QtWidgets.QRadioButton(self.verticalWidget)
        self.blue1.setChecked(True)
        self.blue1.setObjectName("blue1")
        self.color1 = QtWidgets.QButtonGroup(MainWindow)
        self.color1.setObjectName("color1")
        self.color1.addButton(self.blue1)
        self.verticalLayout.addWidget(self.blue1)
        self.red1 = QtWidgets.QRadioButton(self.verticalWidget)
        self.red1.setObjectName("red1")
        self.color1.addButton(self.red1)
        self.verticalLayout.addWidget(self.red1)
        self.green1 = QtWidgets.QRadioButton(self.verticalWidget)
        self.green1.setObjectName("green1")
        self.color1.addButton(self.green1)
        self.verticalLayout.addWidget(self.green1)
        self.blue1.raise_()
        self.green1.raise_()
        self.label1.raise_()
        self.red1.raise_()
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.verticalWidget_2 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label2 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout_2.addWidget(self.label2)
        self.blue2 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.blue2.setChecked(True)
        self.blue2.setObjectName("blue2")
        self.color2 = QtWidgets.QButtonGroup(MainWindow)
        self.color2.setObjectName("color2")
        self.color2.addButton(self.blue2)
        self.verticalLayout_2.addWidget(self.blue2)
        self.red2 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.red2.setObjectName("red2")
        self.color2.addButton(self.red2)
        self.verticalLayout_2.addWidget(self.red2)
        self.green2 = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.green2.setObjectName("green2")
        self.color2.addButton(self.green2)
        self.verticalLayout_2.addWidget(self.green2)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalWidget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label3 = QtWidgets.QLabel(self.verticalWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout_3.addWidget(self.label3)
        self.blue3 = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.blue3.setChecked(True)
        self.blue3.setObjectName("blue3")
        self.color3 = QtWidgets.QButtonGroup(MainWindow)
        self.color3.setObjectName("color3")
        self.color3.addButton(self.blue3)
        self.verticalLayout_3.addWidget(self.blue3)
        self.red3 = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.red3.setObjectName("red3")
        self.color3.addButton(self.red3)
        self.verticalLayout_3.addWidget(self.red3)
        self.green3 = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.green3.setObjectName("green3")
        self.color3.addButton(self.green3)
        self.verticalLayout_3.addWidget(self.green3)
        self.horizontalLayout.addWidget(self.verticalWidget_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(-1, 179, 651, 71)
        )
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2
        )
        self.horizontalLayout_2.setContentsMargins(250, 0, 250, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 268, 300, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый флаг"))
        self.label1.setText(_translate("MainWindow", "Цвет №1"))
        self.blue1.setText(_translate("MainWindow", "Синий"))
        self.red1.setText(_translate("MainWindow", "Красный"))
        self.green1.setText(_translate("MainWindow", "Зелёный"))
        self.label2.setText(_translate("MainWindow", "Цвет №2"))
        self.blue2.setText(_translate("MainWindow", "Синий"))
        self.red2.setText(_translate("MainWindow", "Красный"))
        self.green2.setText(_translate("MainWindow", "Зелёный"))
        self.label3.setText(_translate("MainWindow", "Цвет №3"))
        self.blue3.setText(_translate("MainWindow", "Синий"))
        self.red3.setText(_translate("MainWindow", "Красный"))
        self.green3.setText(_translate("MainWindow", "Зелёный"))
        self.pushButton.setText(_translate("MainWindow", "Сделать флаг"))
        self.label.setText(_translate("MainWindow", "Цвета: "))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.hide()

        self.col1 = "Синий"
        self.col2 = "Синий"
        self.col3 = "Синий"

        self.color1.buttonClicked.connect(self.col1_change)
        self.color2.buttonClicked.connect(self.col2_change)
        self.color3.buttonClicked.connect(self.col3_change)

        self.pushButton.clicked.connect(self.color)

    def col1_change(self, object):
        self.col1 = object.text()

    def col2_change(self, object):
        self.col2 = object.text()

    def col3_change(self, object):
        self.col3 = object.text()

    def color(self):
        self.label.setText(f"Цвета: {self.col1}, {self.col2} и {self.col3}")
        self.label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
