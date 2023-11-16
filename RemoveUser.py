from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy

class Ui_RemoveUser(object):
    def setupUi(self, RemoveUser):
        RemoveUser.setObjectName("RemoveUser")
        RemoveUser.resize(426, 245)
        RemoveUser.setStyleSheet("background-color: rgb(247, 178, 146);")
        self.centralwidget = QtWidgets.QWidget(RemoveUser)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(80, 10, 251, 41))
        self.Heading.setStyleSheet("font: 75 16pt \"Verdana\";\n"
"color: rgb(0, 0, 127);")
        self.Heading.setObjectName("Heading")
        self.Field = QtWidgets.QLabel(self.centralwidget)
        self.Field.setGeometry(QtCore.QRect(90, 80, 81, 31))
        self.Field.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 127);")
        self.Field.setObjectName("Field")
        self.UserN = QtWidgets.QLineEdit(self.centralwidget)
        self.UserN.setGeometry(QtCore.QRect(210, 80, 161, 31))
        self.UserN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UserN.setObjectName("UserN")
        self.Removebutton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.Remove_User())
        self.Removebutton.setGeometry(QtCore.QRect(140, 150, 131, 41))
        self.Removebutton.setStyleSheet("background-color: rgb(18, 123, 221);\n"
"color: rgb(255, 255, 0);\n"
"font: 75 10pt \"Verdana\";")
        self.Removebutton.setObjectName("Removebutton")
        self.Invalid = QtWidgets.QLabel(self.centralwidget)
        self.Invalid.setGeometry(QtCore.QRect(210, 120, 161, 20))
        self.Invalid.setText("")
        self.Invalid.setObjectName("Invalid")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(80, 202, 271, 31))
        self.Output.setText("")
        self.Output.setObjectName("Output")
        RemoveUser.setCentralWidget(self.centralwidget)

        self.retranslateUi(RemoveUser)
        QtCore.QMetaObject.connectSlotsByName(RemoveUser)

    def Remove_User(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Assets=pd.read_sql_table("assets",engine)
        Recs= pd.read_sql_table("records",engine)
        UserID=Recs["User_ID"].to_numpy()
        UID=int(self.UserN.text())

        if UID in UserID:
            Recs.drop(Recs[Recs["User_ID"]==UID].index,inplace=True)
            Assets.drop(Assets[Assets["UserID"]==UID].index,inplace=True)
            Recs.to_sql(name="records",con=engine,if_exists="replace",index=False)
            Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False)
            self.Output.setText("Successfully Removed Record")
            return
        else:
            self.Invalid.setText("Invalid User ID")
            return

    def retranslateUi(self, RemoveUser):
        _translate = QtCore.QCoreApplication.translate
        RemoveUser.setWindowTitle(_translate("RemoveUser", "Delete User Record"))
        self.Heading.setText(_translate("RemoveUser", "REMOVE USER RECORD"))
        self.Field.setText(_translate("RemoveUser", "USER ID"))
        self.Removebutton.setText(_translate("RemoveUser", "REMOVE RECORD"))
        self.UserN.setPlaceholderText(_translate("RemoveUser","Enter User ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemoveUser = QtWidgets.QMainWindow()
    ui = Ui_RemoveUser()
    ui.setupUi(RemoveUser)
    RemoveUser.show()
    sys.exit(app.exec_())
