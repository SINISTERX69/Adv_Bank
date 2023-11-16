import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random
import names
import sqlalchemy
from datetime import date as dt
from sklearn.cluster import KMeans


#Functions for Kmeans Data Analysis

"""
def reroll(N):		#sample data creation
	d={"User_ID": [],"Account_Number":[],"Name": [],"Income": [],"Balance":[],"Loan": []}
	UID=list(range(1000,1000+N))
	Acc_No=list(range(13469000,13469000+N))
	for i in range(N):
		name=names.get_full_name()
		Uid=random.choice(UID)
		UID.remove(Uid)
		Acc=random.choice(Acc_No)
		Acc_No.remove(Acc)
		d["User_ID"].append(Uid)
		d["Account_Number"].append(Acc)
		d["Name"].append(name)
		d["Income"].append(random.randint(20000,200000))
		d["Balance"].append(random.randint(100000,500000))
		d["Loan"].append(random.randint(50000,150000))
	df=pd.DataFrame(d,index=[x for x in range(1,N+1)])
	global engine
	df.to_sql(name="records",con=engine,if_exists="replace",index=False)
"""

engine=sqlalchemy.create_engine("mysql+pymysql://BANK:Benk@localhost:3306/BANK")

Recs= pd.read_sql_table("records",engine)

Data=Recs[["Balance","Income","User_ID"]].to_numpy()
points=Recs[["Balance","Income"]].to_numpy()
User_Data=Recs[["User_ID","Account_Number","Name","Balance","Income"]].to_numpy()
UserID=Recs["User_ID"].to_numpy()
Account_No=Recs["Account_Number"].to_numpy()

kmeans=KMeans(n_clusters=6,init="k-means++")
kmeans.fit(points)	#Fitting data in kmeans object
centers = kmeans.cluster_centers_	#Get cluster centers
clusters=kmeans.fit_predict(points)	#Assigning Numbers to points according to their clusters [index in both lists is same]


def kmean_graph(Data,clusters,user=None):		#To show clustered graph
	plt.scatter(Data[clusters==0,0],Data[clusters==0,1],c="red")
	plt.scatter(Data[clusters==1,0],Data[clusters==1,1],c="green")
	plt.scatter(Data[clusters==2,0],Data[clusters==2,1],c="blue")
	plt.scatter(Data[clusters==3,0],Data[clusters==3,1],c="yellow")
	plt.scatter(Data[clusters==4,0],Data[clusters==4,1],c="purple")
	plt.scatter(Data[clusters==5,0],Data[clusters==5,1],c="brown")
	if user is not None:
		plt.scatter(user[0],user[1],c="black",marker="D")
	plt.xlabel("Balance")
	plt.ylabel("Income")
	plt.show()

def graph():
	UID=int(input("Enter UserID [1000-1500] "))
	if 1000<UID<1500: 
		rec=get_rec(UID)
		kmean_graph(Data,clusters,rec)
	elif UID==0:
		kmean_graph(Data,clusters)
	else:
		print("Invalid UserID")

def get_rec(UID):	#Read name obvio
	rec=[]
	for i in Data:
		if UID==i[2]:
			rec.append(i[0])
			rec.append(i[1])
	return rec

def Find_centre(rec,centers):	#find nearest centre 
	mini=100000000000
	x,y=int(rec[0]),int(rec[1])
	req_center=[]
	for c in centers:
		x1,y1=int(c[0]),int(c[1])
		distance=m.sqrt((x1-x)**2+(y1-y)**2)
		if distance<mini:
			mini=distance
			req_center=[x1,y1]
	return req_center


def Output_process(Center):		#advice on the basis of nearest centre
	l1=["FD of rupees 50000 with 6% interest per annum.","Create a PPF at 8.7% interest rate for 15 yrs "]
	l2=["FD of rupees 75000 with 6.4% interest per annum.","Create a PPF at 9% interest rate for 10yrs"]
	l3=["FD of rupees 80000 with 6.3% interest per annum","Take Gold Loans at low interest rates to invest in Gold easily"]
	l4=["FD of rupees 90000 with 6.3% interest per annum.","Take Gold Loans at low interest rates to invest in Gold easily"]
	l5=["FD of rupees 95000 with 6.4% interest per annum.","Issue loans at 13% interest rate to establish a local industry"]
	l6=["Open demat account and start investing in stocks through our local branch broker","Take loans at 15% interest rate to buy plots and start a real estate business"]
	
	if Center[1]<100000:
		if Center[0]<225000: 
			return(random.choice(l1))	
		elif 225000<Center[0]<375000:
			return(random.choice(l2)) 
		elif 375000<Center[0]:
			return(random.choice(l3)) 
	if Center[1]>100000:
		if Center[0]<225000: 
			return(random.choice(l4))	
		elif 225000<Center[0]<375000:
			return(random.choice(l5)) 
		elif 375000<Center[0]:
			return(random.choice(l6))

def FINAL(UID):		#All in one function
	rec=get_rec(UID)
	Center=Find_centre(rec,centers)
	return Output_process(Center)

def advanced_adv(UID):
	if 1000<UID<1500:
		return FINAL(UID)
	else:
		print("Invalid UserID")





