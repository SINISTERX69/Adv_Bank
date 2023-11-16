from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
import numpy as np
import sqlalchemy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 361)
        MainWindow.setStyleSheet("background-color: rgb(194, 255, 193);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(80, 10, 321, 61))
        self.Heading.setStyleSheet("font: 75 16pt \"Palatino Linotype\";\n"
"color: rgb(132, 157, 171);")
        self.Heading.setObjectName("Heading")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 123, 123);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.Invalid = QtWidgets.QLabel(self.centralwidget)
        self.Invalid.setGeometry(QtCore.QRect(250, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Invalid.setFont(font)
        self.Invalid.setStyleSheet("color: rgb(255, 123, 123);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.Invalid.setText("")
        self.Invalid.setObjectName("Invalid")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(76, 130, 181);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.calc())
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(60, 260, 331, 41))
        self.Output.setStyleSheet("color: rgb(200, 133, 0);\n"
"font: 75 14pt \"Times New Roman\";")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(260, 190, 141, 51))
        self.EXIT.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(76, 130, 181);")
        self.EXIT.setObjectName("EXIT")
        self.EXIT.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Credit Score Calculator"))
        self.Heading.setText(_translate("MainWindow", "CREDIT SCORE CALCULATOR"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter User ID"))
        self.label.setText(_translate("MainWindow", "User ID"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.EXIT.setText(_translate("MainWindow", "RETURN"))

    def calc(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Recs=pd.read_sql_table("records",engine)
        Assets=pd.read_sql_table("assets",engine)
        assets=Assets[["UserID","Land_Area","Cows","Goats","Chicken"]].to_numpy()
        Records=Recs[["User_ID","Balance","Income"]].to_numpy()
        
        self.Invalid.setText("")
        self.Output.setText("")
        UID=int(self.lineEdit.text())
        if UID not in Records:
            self.Invalid.setText("Invalid User ID")
            return
        for i in Records:
            if UID==i[0]:
                Bal,Inc=i[1],i[2]
                break
        Area,Cows,Goats,Chickens=0,0,0,0
        for j in assets:
            if UID==j[0]:
                Area,Cows,Goats,Chickens=j[1],j[2],j[3],j[4]
                break
        
        Score=0
        if Inc<=100000:
            Score+=10
        elif Inc>=100000:
            Score+=20
        
        if Bal<=250000:
            Score+=10
        elif Bal>250000 and Bal<=370000:
            Score+=20
        elif Bal>370000:
            Score+=30

        if Area==0:
            Score+=0
        elif Area<108000:
            Score+=5
        elif Area<200000 and Area>=108000:
            Score+=10
        elif Area>=200000 and Area<250000:
            Score+=15
        elif Area>=250000:
            Score+=20

        if Cows==0:
            Score+=0
        elif Cows<5:
             Score+=3
        elif Cows>=5 and Cows<10:
            Score+=5
        elif Cows>=10 and Cows<20:
            Score+=8
        elif Cows>=20:
            Score+=10
        
        if Goats==0:
            Score+=0    
        elif Goats<10:
            Score+=3
        elif Goats>=10 and Goats<50:
            Score+=5
        elif Goats>=50:
            Score+=10

        if Chickens==0:
            Score+=0    
        elif Chickens<20:
            Score+=3
        elif Chickens>=20 and Chickens<60:
            Score+=5
        elif Chickens>=60:
            Score+=10
        self.Output.setText(f"Calculated Credit Score is {Score}/100")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())