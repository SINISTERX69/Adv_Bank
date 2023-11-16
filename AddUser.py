from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sqlalchemy
import random

class Ui_NEWUSER(object):
    def setupUi(self, NEWUSER):
        NEWUSER.setObjectName("NEWUSER")
        NEWUSER.resize(395, 347)
        NEWUSER.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(NEWUSER)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(130, 30, 121, 41))
        self.Heading.setStyleSheet("font: 75 italic 16pt \"Verdana\";\n"
"color: rgb(255, 255, 127);")
        self.Heading.setObjectName("Heading")
        self.field = QtWidgets.QLabel(self.centralwidget)
        self.field.setGeometry(QtCore.QRect(80, 100, 91, 31))
        self.field.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.field.setObjectName("field")
        self.fiels = QtWidgets.QLabel(self.centralwidget)
        self.fiels.setGeometry(QtCore.QRect(80, 150, 91, 31))
        self.fiels.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.fiels.setObjectName("fiels")
        self.field_2 = QtWidgets.QLabel(self.centralwidget)
        self.field_2.setGeometry(QtCore.QRect(80, 200, 91, 31))
        self.field_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 250, 99);")
        self.field_2.setObjectName("field_2")
        self.AddUSER = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Add())
        self.AddUSER.setGeometry(QtCore.QRect(130, 260, 121, 51))
        self.AddUSER.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 12pt \"Times New Roman\";")
        self.AddUSER.setObjectName("AddUSER")
        self.UserN = QtWidgets.QLineEdit(self.centralwidget)
        self.UserN.setGeometry(QtCore.QRect(210, 99, 151, 31))
        self.UserN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UserN.setObjectName("UserN")
        self.Balance = QtWidgets.QLineEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(210, 150, 151, 31))
        self.Balance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Balance.setObjectName("Balance")
        self.Income = QtWidgets.QLineEdit(self.centralwidget)
        self.Income.setGeometry(QtCore.QRect(210, 200, 151, 31))
        self.Income.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Income.setObjectName("Income")
        NEWUSER.setCentralWidget(self.centralwidget)

        self.retranslateUi(NEWUSER)
        QtCore.QMetaObject.connectSlotsByName(NEWUSER)
    
    def Add(self):
        engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
        Recs=pd.read_sql_table("records",engine)
        Assets=pd.read_sql_table("assets",engine)
        UserID=Recs["User_ID"].to_numpy()
        Account_No=Recs["Account_Number"].to_numpy()
        
        while True:
            UID=random.randint(1000,1999)
            Acc_No=random.randint(13469000,13469999)
            if UID not in UserID and Acc_No not in Account_No:
                break

        Name=str(self.UserN.text())
        Bal=int(self.Balance.text())
        Inc=int(self.Income.text())
        
        record=[{"User_ID": UID,"Account_Number":Acc_No,"Name": Name,"Income": Inc,"Balance": Bal}]
        Recs=Recs.append(record,ignore_index=True)
        asset=[{"UserID": UID,"Land_Area":0,"Cows": 0,"Goats": 0,"Chicken":0}]
        Assets=Assets.append(asset,ignore_index=True)
        Assets.to_sql(name="assets",con=engine,if_exists="replace",index=False)
        Recs.to_sql(name="records",con=engine,if_exists="replace",index=False)
        

    def retranslateUi(self, NEWUSER):
        _translate = QtCore.QCoreApplication.translate
        NEWUSER.setWindowTitle(_translate("NEWUSER", "Add New User"))
        self.Heading.setText(_translate("NEWUSER", "NEW USER"))
        self.field.setText(_translate("NEWUSER", "USER NAME"))
        self.fiels.setText(_translate("NEWUSER", "BALANCE"))
        self.field_2.setText(_translate("NEWUSER", "INCOME"))
        self.AddUSER.setText(_translate("NEWUSER", "ADD USER"))
        self.UserN.setPlaceholderText(_translate("NEWUSER", "Enter User Name"))
        self.Balance.setPlaceholderText(_translate("NEWUSER", "Enter Balance of User"))
        self.Income.setPlaceholderText(_translate("NEWUSER", "Enter Income of the User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEWUSER = QtWidgets.QMainWindow()
    ui = Ui_NEWUSER()
    ui.setupUi(NEWUSER)
    NEWUSER.show()
    sys.exit(app.exec_())
