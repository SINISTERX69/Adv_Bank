from PyQt5 import QtCore, QtGui, QtWidgets
from AddUser import *
from RemoveUser import *
from UpdateUser import *
from UpdateAssets import *

class Ui_Updation(object):
    def setupUi(self, Updation):
        Updation.setObjectName("Updation")
        Updation.resize(481, 237)
        Updation.setStyleSheet("background-color: rgb(121, 139, 145);")
        self.centralwidget = QtWidgets.QWidget(Updation)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(110, 20, 281, 41))
        self.Heading.setStyleSheet("color: rgb(15, 255, 247);\n"
"font: 75 16pt \"Magneto\";")
        self.Heading.setObjectName("Heading")
        self.NEW_USER = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Add())
        self.NEW_USER.setGeometry(QtCore.QRect(20, 100, 131, 41))
        self.NEW_USER.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.NEW_USER.setObjectName("NEW_USER")
        self.Update_USER = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Updatedata())
        self.Update_USER.setGeometry(QtCore.QRect(170, 100, 141, 41))
        self.Update_USER.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Update_USER.setObjectName("Update_USER")
        self.Remove_User = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Remove())
        self.Remove_User.setGeometry(QtCore.QRect(330, 100, 131, 41))
        self.Remove_User.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Remove_User.setObjectName("Remove_User")
        self.Assets = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Update_Asset())
        self.Assets.setGeometry(QtCore.QRect(160, 170, 161, 41))
        self.Assets.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Assets.setObjectName("Assets")
        Updation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Updation)
        QtCore.QMetaObject.connectSlotsByName(Updation)

    def Add(self):
        self.Adduser= QtWidgets.QMainWindow()
        self.ui = Ui_NEWUSER()
        self.ui.setupUi(self.Adduser)
        self.Adduser.show()

    def Remove(self):
        self.Removeuser=QtWidgets.QMainWindow()
        self.ui = Ui_RemoveUser()
        self.ui.setupUi(self.Removeuser)
        self.Removeuser.show()
    
    def Updatedata(self):
        self.updater=QtWidgets.QMainWindow()
        self.ui = Ui_Update_Data()
        self.ui.setupUi(self.updater)
        self.updater.show()

    def Update_Asset(self):
        self.updateA=QtWidgets.QMainWindow()   
        self.ui= Ui_Assets()
        self.ui.setupUi(self.updateA)
        self.updateA.show() 

    def retranslateUi(self, Updation):
        _translate = QtCore.QCoreApplication.translate
        Updation.setWindowTitle(_translate("Updation", "Financial Advisor"))
        self.Heading.setText(_translate("Updation", "UPDATE DATABASE"))
        self.NEW_USER.setText(_translate("Updation", "ADD NEW USER"))
        self.Update_USER.setText(_translate("Updation", "UPDATE USER DATA"))
        self.Remove_User.setText(_translate("Updation", "REMOVE USER"))
        self.Assets.setText(_translate("Updation", "UPDATE USER ASSETS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Updation = QtWidgets.QMainWindow()
    ui = Ui_Updation()
    ui.setupUi(Updation)
    Updation.show()
    sys.exit(app.exec_())
