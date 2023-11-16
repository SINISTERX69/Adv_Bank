from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy
from FUNCTIONS import *

class Ui_Advice(object):
    def setupUi(self, Advice):
        Advice.setObjectName("Advice")
        Advice.resize(479, 284)
        Advice.setStyleSheet("background-color: rgb(218, 192, 44);")
        self.centralwidget = QtWidgets.QWidget(Advice)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(130, 30, 211, 31))
        self.Heading.setStyleSheet("font: 63 italic 16pt \"Lucida Bright\";\n"
"color: rgb(0, 85, 255);")
        self.Heading.setObjectName("Heading")
        self.FIELD = QtWidgets.QLabel(self.centralwidget)
        self.FIELD.setGeometry(QtCore.QRect(120, 90, 81, 31))
        self.FIELD.setStyleSheet("color: rgb(26, 41, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.FIELD.setObjectName("FIELD")
        self.Userid = QtWidgets.QLineEdit(self.centralwidget)
        self.Userid.setGeometry(QtCore.QRect(220, 89, 171, 31))
        self.Userid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Userid.setObjectName("Userid")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.advanced_adv())
        self.pushButton.setGeometry(QtCore.QRect(160, 150, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(240, 244, 23);\n"
"font: 75 10pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.Advise = QtWidgets.QTextBrowser(self.centralwidget)
        self.Advise.setGeometry(QtCore.QRect(25, 211, 431, 61))
        self.Advise.setObjectName("Advise")
        Advice.setCentralWidget(self.centralwidget)

        self.retranslateUi(Advice)
        QtCore.QMetaObject.connectSlotsByName(Advice)
    
    def advanced_adv(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Recs= pd.read_sql_table("records",engine)
        UserID=Recs["User_ID"].to_numpy()
        self.Advise.setText("")
        UID=int(self.Userid.text())
        if UID in UserID:

            Adv=FINAL(UID)
            self.Advise.setText(Adv)
        else:
            self.Advise.setText("Invalid User ID")

    def retranslateUi(self, Advice):
        _translate = QtCore.QCoreApplication.translate
        Advice.setWindowTitle(_translate("Advice", "Advicer"))
        self.Heading.setText(_translate("Advice", "FINANCIAL ADVICE"))
        self.FIELD.setText(_translate("Advice", "USER ID"))
        self.pushButton.setText(_translate("Advice", "SUGGEST ADVICE"))
        self.Advise.setHtml(_translate("Advice", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Advice = QtWidgets.QMainWindow()
    ui = Ui_Advice()
    ui.setupUi(Advice)
    Advice.show()
    sys.exit(app.exec_())
