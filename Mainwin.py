from PyQt5 import QtCore, QtGui, QtWidgets
from Calculator import *
from Adviser import *
from Updater import *

class Ui_Adviser(object):
    def setupUi(self, Adviser):
        Adviser.setObjectName("Adviser")
        Adviser.resize(593, 332)
        Adviser.setStyleSheet("background-color: rgb(83, 210, 238);")
        self.centralwidget = QtWidgets.QWidget(Adviser)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(190, 20, 221, 51))
        self.Heading.setStyleSheet("font: 75 16pt \"Verdana\";\n"
"color: rgb(255, 255, 0);")
        self.Heading.setObjectName("Heading")
        self.Description = QtWidgets.QTextBrowser(self.centralwidget)
        self.Description.setGeometry(QtCore.QRect(50, 80, 491, 91))
        self.Description.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 255, 255);\n"
"font: 75 12pt \"Rockwell Condensed\";")
        self.Description.setObjectName("Description")
        self.updatebutton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.Updaterr())
        self.updatebutton.setGeometry(QtCore.QRect(30, 210, 141, 61))
        self.updatebutton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(5, 105, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.updatebutton.setObjectName("updatebutton")
        self.advicebutton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.Advice())
        self.advicebutton.setGeometry(QtCore.QRect(210, 210, 151, 61))
        self.advicebutton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(5, 105, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.advicebutton.setObjectName("advicebutton")
        self.calculatebutton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.Calculator())
        self.calculatebutton.setGeometry(QtCore.QRect(390, 210, 171, 61))
        self.calculatebutton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(5, 105, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.calculatebutton.setObjectName("calculatebutton")
        self.Thnx = QtWidgets.QLabel(self.centralwidget)
        self.Thnx.setGeometry(QtCore.QRect(180, 280, 221, 41))
        self.Thnx.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(223, 91, 68);")
        self.Thnx.setObjectName("Thnx")
        Adviser.setCentralWidget(self.centralwidget)

        self.retranslateUi(Adviser)
        QtCore.QMetaObject.connectSlotsByName(Adviser)

    def Calculator(self):
        self.calculator = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.calculator)
        self.calculator.show()
    
    def Advice(self):
        self.adv= QtWidgets.QMainWindow()
        self.ui = Ui_Advice()
        self.ui.setupUi(self.adv)
        self.adv.show()
    
    def Updaterr(self):
        self.upd= QtWidgets.QMainWindow()
        self.ui = Ui_Updation()
        self.ui.setupUi(self.upd)
        self.upd.show()


    def retranslateUi(self, Adviser):
        _translate = QtCore.QCoreApplication.translate
        Adviser.setWindowTitle(_translate("Adviser", "Financial Adviser"))
        self.Heading.setText(_translate("Adviser", "FINANCIAL ADVISER "))
        self.Description.setHtml(_translate("Adviser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell Condensed\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; color:#ffffff;\">This application is designed to function in rural India and provide appropriate financial advice to farmers and other village dwellers on the basis of their assets.It application is also capable of calculating a Custom Credit Score of the user by taking into account their land holdings, livestock, balance etc. The credit score is calculated out of 100.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; color:#ffffff;\">Developed by Aniket Das</span></p></body></html>"))
        self.updatebutton.setText(_translate("Adviser", "UPDATE USER DATA"))
        self.advicebutton.setText(_translate("Adviser", "GET FINANCIAL ADVICE"))
        self.calculatebutton.setText(_translate("Adviser", "CALCULATE CREDIT SCORE"))
        self.Thnx.setText(_translate("Adviser", "Thank You for using our Application!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Adviser = QtWidgets.QMainWindow()
    ui = Ui_Adviser()
    ui.setupUi(Adviser)
    Adviser.show()
    sys.exit(app.exec_())
