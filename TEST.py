import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import sqlalchemy
from datetime import date as dt
from sklearn.cluster import KMeans


"""
employee={"EmpID":[1212,1111],"PIN":[2003,1234],"Name":["Aniket","Admin"]}
df=pd.DataFrame(employee,index=[x for x in range(1,2+1)])
df.to_csv("employee.csv")
"""
"""
Recs=pd.read_csv("Records1.csv")
UserID=Recs["User_ID"].to_numpy()
User_Data=Recs[["User_ID","Account_Number","Name","Balance","Income"]].to_numpy()

def Add():
	for i in range(2):
		while True:
			global Recs
			UID=random.randint(1000,1999)
			Acc_No=random.randint(13469000,13469999)
			if UID not in Recs and Acc_No not in Recs:
				break
		Name=input("Enter Name of the User")
		Balance=int(input("Enter Amount Deposited by the User"))
		Income=int(input("Enter income of the User"))
		record=[{"User_ID": UID,"Account_Number":Acc_No,"Name": Name,"Income": Income,"Balance": Balance}]
		Recs=Recs.append(record,ignore_index=True)
	Recs.to_csv("Records1.csv",index=False)

def Remove():
	global Recs
	UID=int(input("Enter User ID"))
	if UID in UserID:
		Recs.drop(Recs[Recs["User_ID"]==UID].index,inplace=True)
		Recs.to_csv("Records1.csv",index=False)
	else:
		print("No")

def Update():
	global Recs
	global UserID
	UID=int(input("Enter User ID"))
	if UID in UserID:
		for i in User_Data:
			if UID==i[0]:
				Bal=i[3]
		print("What operation would u like to perform?","{1} Update Income of the User","{2} Update Balance of the User",sep="\n")
		Ans=int(input())
		if Ans==1:
			New_Inc=int(input("Enter new Income of the User"))
			Recs.loc[Recs["User_ID"]==UID, "Income"]=New_Inc
			Recs.to_csv("Records1.csv",index=False)
			print("Changes were made Successfully")
		elif Ans==2:
			Amt=eval(input("Enter the Amount Deposited/Withdrawn by the user [Use -ve sign if amount is withdrawn]"))
			Recs.loc[Recs["User_ID"]==UID, "Balance"]= (Bal - Amt)
			Recs.to_csv("Records1.csv",index=False)
			print("Changes were made Successfully")
	else:
		print("User ID does not exist")
"""
"""
engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")
Recs=pd.read_sql_table("records",engine)
Records=Recs["User_ID"].to_numpy()

def reroll():		#sample data creation
	global Records
	d={"UserID": [],"Land_Area":[],"Cows": [],"Goats": [],"Chicken":[]}
	for i in Records:
		d["UserID"].append(i)
		Area=int((round(random.random()*random.randint(0,3),2))*10000)
		d["Land_Area"].append(Area)
		d["Cows"].append(random.randint(0,20))
		d["Goats"].append(random.randint(0,70))
		d["Chicken"].append(random.randint(0,80))
	df=pd.DataFrame(d,index=[x for x in range(500)])
	global engine
	df.to_sql(name="assets",con=engine,if_exists="replace",index=False)
reroll()
"""
