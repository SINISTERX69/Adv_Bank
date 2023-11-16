from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy
from Mainwin import *

engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 290)
        MainWindow.setStyleSheet("background-color: rgb(202, 202, 202)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(110, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        D=self.login.clicked.connect(lambda: self.check())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(17, 41, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(17, 41, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 0)")
        self.label_3.setObjectName("label_3")
        self.emp_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.emp_ID.setGeometry(QtCore.QRect(210, 70, 231, 31))
        self.emp_ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emp_ID.setObjectName("emp_ID")
        self.Pass = QtWidgets.QLineEdit(self.centralwidget)
        self.Pass.setGeometry(QtCore.QRect(210, 130, 231, 31))
        self.Pass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass.setObjectName("Pass")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 170, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(17, 41, 255)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def next(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Adviser()
        self.ui.setupUi(self.Window)
        self.Window.show()
        MainWindow.close()


    def check(self):
        self.empID=int(self.emp_ID.text())
        self.Pas=int(self.Pass.text())
        self.employee=pd.read_sql_table("employee",engine)
        self.emp=self.employee[["EmpID","PIN"]].to_numpy()
        for k in self.emp:
            if k[0]==self.empID and k[1]==self.Pas:
                self.next()
                return True
            else:
                self.label_4.setText("Invalid Password or Emplyee ID")
                break
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "Employee ID  "))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "FINANCIAL ADVICER SOFTWARE"))
        self.emp_ID.setPlaceholderText(_translate("MainWindow", "Enter User ID"))
        self.Pass.setPlaceholderText(_translate("MainWindow", "Enter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

