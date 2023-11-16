from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy


class Ui_Assets(object):
    def setupUi(self, Assets):
        Assets.setObjectName("Assets")
        Assets.resize(494, 481)
        Assets.setStyleSheet("background-color: rgb(145, 169, 208);")
        self.centralwidget = QtWidgets.QWidget(Assets)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(140, 20, 231, 51))
        self.Heading.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"color: rgb(243, 231, 68);")
        self.Heading.setObjectName("Heading")
        self.Field_3 = QtWidgets.QLabel(self.centralwidget)
        self.Field_3.setGeometry(QtCore.QRect(50, 90, 111, 41))
        self.Field_3.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_3.setObjectName("Field_3")
        self.Userid = QtWidgets.QLineEdit(self.centralwidget)
        self.Userid.setGeometry(QtCore.QRect(250, 100, 171, 31))
        self.Userid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Userid.setObjectName("Userid")
        self.Field_4 = QtWidgets.QLabel(self.centralwidget)
        self.Field_4.setGeometry(QtCore.QRect(50, 140, 181, 41))
        self.Field_4.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_4.setObjectName("Field_4")
        self.Land = QtWidgets.QLineEdit(self.centralwidget)
        self.Land.setGeometry(QtCore.QRect(250, 150, 171, 31))
        self.Land.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Land.setObjectName("Land")
        self.Cow = QtWidgets.QLineEdit(self.centralwidget)
        self.Cow.setGeometry(QtCore.QRect(250, 220, 171, 31))
        self.Cow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cow.setObjectName("Cow")
        self.Chicken = QtWidgets.QLineEdit(self.centralwidget)
        self.Chicken.setGeometry(QtCore.QRect(250, 320, 171, 31))
        self.Chicken.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Chicken.setObjectName("Chicken")
        self.Goat = QtWidgets.QLineEdit(self.centralwidget)
        self.Goat.setGeometry(QtCore.QRect(250, 270, 171, 31))
        self.Goat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Goat.setObjectName("Goat")
        self.Field_5 = QtWidgets.QLabel(self.centralwidget)
        self.Field_5.setGeometry(QtCore.QRect(20, 180, 181, 41))
        self.Field_5.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"color: rgb(255, 255, 0);")
        self.Field_5.setObjectName("Field_5")
        self.Field_6 = QtWidgets.QLabel(self.centralwidget)
        self.Field_6.setGeometry(QtCore.QRect(50, 220, 111, 31))
        self.Field_6.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_6.setObjectName("Field_6")
        self.Field_7 = QtWidgets.QLabel(self.centralwidget)
        self.Field_7.setGeometry(QtCore.QRect(50, 270, 141, 31))
        self.Field_7.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_7.setObjectName("Field_7")
        self.Field_8 = QtWidgets.QLabel(self.centralwidget)
        self.Field_8.setGeometry(QtCore.QRect(50, 320, 141, 31))
        self.Field_8.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_8.setObjectName("Field_8")
        self.Action = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.Update_Assets())
        self.Action.setGeometry(QtCore.QRect(170, 370, 131, 51))
        self.Action.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(3, 111, 252);")
        self.Action.setObjectName("Action")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(40, 430, 411, 31))
        self.Output.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        Assets.setCentralWidget(self.centralwidget)

        self.retranslateUi(Assets)
        QtCore.QMetaObject.connectSlotsByName(Assets)


    def Update_Assets(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Assets=pd.read_sql_table("assets",engine)
        UserID=Assets[["UserID"]].to_numpy()
        UID=int(self.Userid.text())

        if UID in UserID:
                if self.Land.text():
                        Area=int(self.Land.text())
                        Assets.loc[Assets["UserID"]==UID, "Land_Area"]= Area
                        Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False)
                if self.Cow.text():
                        C=int(self.Cow.text())
                        Assets.loc[Assets["UserID"]==UID, "Cows"]= C
                        Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False)
                if self.Goat.text():
                        G=int(self.Goat.text())
                        Assets.loc[Assets["UserID"]==UID, "Goats"]= G
                        Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False) 
                if self.Chicken.text():
                        Ch=int(self.Chicken.text())
                        Assets.loc[Assets["UserID"]==UID, "Chicken"]= Ch
                        Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False)
                self.Output.setText("Assets Successfully Updated")
                return
        else:
                self.Output.setText("Invalid User ID")
                return

    def retranslateUi(self, Assets):
        _translate = QtCore.QCoreApplication.translate
        Assets.setWindowTitle(_translate("Assets", "Update User Assets"))
        self.Heading.setText(_translate("Assets", "UPDATE USER ASSETS"))
        self.Field_3.setText(_translate("Assets", "USER ID"))
        self.Userid.setPlaceholderText(_translate("Assets", "Enter User ID"))
        self.Field_4.setText(_translate("Assets", "Total Land (in sq. metres)"))
        self.Land.setPlaceholderText(_translate("Assets", "Leave empty if no change"))
        self.Cow.setPlaceholderText(_translate("Assets", "Leave empty if no change"))
        self.Chicken.setPlaceholderText(_translate("Assets", "Leave empty if no change"))
        self.Goat.setPlaceholderText(_translate("Assets", "Leave empty if no change"))
        self.Field_5.setText(_translate("Assets", "Cattle Data"))
        self.Field_6.setText(_translate("Assets", "Number of Cows"))
        self.Field_7.setText(_translate("Assets", "Number of Goats"))
        self.Field_8.setText(_translate("Assets", "Number of Chickens"))
        self.Action.setText(_translate("Assets", "UPDATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Assets = QtWidgets.QMainWindow()
    ui = Ui_Assets()
    ui.setupUi(Assets)
    Assets.show()
    sys.exit(app.exec_())
