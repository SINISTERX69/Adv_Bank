from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy

class Ui_Update_Data(object):
    def setupUi(self, Update_Data):
        Update_Data.setObjectName("Update_Data")
        Update_Data.resize(496, 404)
        Update_Data.setStyleSheet("background-color: rgb(157, 206, 177);")
        self.centralwidget = QtWidgets.QWidget(Update_Data)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(150, 20, 201, 41))
        self.Heading.setStyleSheet("font: 75 14pt \"Verdana\";\n"
"color: rgb(243, 231, 68);")
        self.Heading.setObjectName("Heading")
        self.Field = QtWidgets.QLabel(self.centralwidget)
        self.Field.setGeometry(QtCore.QRect(90, 140, 111, 41))
        self.Field.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field.setObjectName("Field")
        self.Field_2 = QtWidgets.QLabel(self.centralwidget)
        self.Field_2.setGeometry(QtCore.QRect(90, 200, 111, 41))
        self.Field_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_2.setObjectName("Field_2")
        self.Balance = QtWidgets.QLineEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(280, 150, 171, 31))
        self.Balance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Balance.setObjectName("Balance")
        self.Income = QtWidgets.QLineEdit(self.centralwidget)
        self.Income.setGeometry(QtCore.QRect(280, 200, 171, 31))
        self.Income.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Income.setObjectName("Income")
        self.Action = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Update_User())
        self.Action.setGeometry(QtCore.QRect(180, 280, 121, 51))
        self.Action.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"color: rgb(3, 111, 252);")
        self.Action.setObjectName("Action")
        self.Field_3 = QtWidgets.QLabel(self.centralwidget)
        self.Field_3.setGeometry(QtCore.QRect(90, 90, 111, 41))
        self.Field_3.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.Field_3.setObjectName("Field_3")
        self.Userid = QtWidgets.QLineEdit(self.centralwidget)
        self.Userid.setGeometry(QtCore.QRect(280, 100, 171, 31))
        self.Userid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Userid.setObjectName("Userid")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(60, 350, 391, 41))
        self.Output.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        Update_Data.setCentralWidget(self.centralwidget)

        self.retranslateUi(Update_Data)
        QtCore.QMetaObject.connectSlotsByName(Update_Data)

    def Update_User(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Recs= pd.read_sql_table("records",engine)
        UserID=Recs["User_ID"].to_numpy()
        UID=int(self.Userid.text())
        
        if UID in UserID:
                if self.Income.text():
                        New_Inc=int(self.Income.text())
                        Recs.loc[Recs["User_ID"]==UID, "Income"]=New_Inc
                        Recs.to_sql(name="records",con=engine,if_exists="replace",index=False)
                if self.Balance.text():       
                        Amt=int(self.Balance.text())
                        Recs.loc[Recs["User_ID"]==UID, "Balance"]=Amt
                        Recs.to_sql(name="records",con=engine,if_exists="replace",index=False)
                
                self.Output.setText("Database Successfully Updated")
                return
        else:
                self.Output.setText("User ID not found")
                return

    def retranslateUi(self, Update_Data):
        _translate = QtCore.QCoreApplication.translate
        Update_Data.setWindowTitle(_translate("Update_Data", "Update User Data"))
        self.Heading.setText(_translate("Update_Data", "UPDATE USER DATA"))
        self.Field.setText(_translate("Update_Data", "New Balance"))
        self.Field_2.setText(_translate("Update_Data", "New Income"))
        self.Balance.setPlaceholderText(_translate("Update_Data", "Leave empty if no change"))
        self.Income.setPlaceholderText(_translate("Update_Data", "Leave empty if no change"))
        self.Action.setText(_translate("Update_Data", "UPDATE"))
        self.Field_3.setText(_translate("Update_Data", "USER ID"))
        self.Userid.setPlaceholderText(_translate("Update_Data", "Enter User ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_Data = QtWidgets.QMainWindow()
    ui = Ui_Update_Data()
    ui.setupUi(Update_Data)
    Update_Data.show()
    sys.exit(app.exec_())
