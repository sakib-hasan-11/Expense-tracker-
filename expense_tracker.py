import pandas as pd 
import os
from datetime import datetime 
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
import numpy as np


data = pd.DataFrame(columns=["date","category","amount","description"])
data.to_csv("expence.csv",index=False)

def add_expences():
       if os.path.exists("expence.csv"): 
           data=pd.read_csv("expence.csv")
       else :
           data = pd.DataFrame(columns=["date","category","amount","description"])
           

       new_data = pd.DataFrame([{
       "date":  input("enter the date(YYYY-MM-DD): "),
       "category": input ("enter the category (food,transport): "),
       "amount": int (input("enter total amount of money: ")),
       "description":input("enter the description (optional): ")}])


       data["date"]=pd.to_datetime(data["date"])
       data = pd.concat([data,new_data], ignore_index=True )
       data.to_csv("expence.csv", index=False)
       print("your data is added successfully ")


def view_summry ():
     data = pd.read_csv("expence.csv")
     grp_data = data.groupby(["category"])["amount"].sum()
     print(grp_data)
     total_amount = data["amount"].sum()
     print(f"Your total expence is {total_amount}")


def view_expences(): 
           data = pd.read_csv("expence.csv")
           print(data)


def reset_data(): 
       reset_data = pd.DataFrame(columns=["date","catagory","amount","description"])
       reset_data.to_csv("expence.csv",index=False)
       print("your previous data is deleted")
       return reset_data

def view_statistics(): 
       print(" 1 = view expense per category \n 2 = view monthly expence statistics ")
       user_input = int(input("your input here: "))
       if user_input == 1 : 
              plt.plot(data["category"],data["amount"], label="expense per category",color="#8bbaf8")
              plt.xlabel("category")
              plt.ylabel("amount of money")
              plt.legend()
              plt.title("expense per category")
              plt.show()
       if user_input == 2 : 
              plt.pie(data["amount"],autopct="%1,1f%%",labels=data["category"])
              plt.title("expense per category")
              plt.show()




def main_menu(): 
    while True:
              print("your expence")
              print("1. add new expence \n2. view data \n3. view summery \n4. exit \n5. reset data \n6. view statistics ")
              choise =int(input("enter your choise here: "))
              if choise == 1: 
                     add_expences()
              elif choise == 4:
                     break
              elif choise == 3: 
                     view_summry()
              elif choise == 2: 
                     view_expences()
              elif choise == 5: 
                     reset_data()
              elif choise == 6: 
                     view_statistics()
              else : 
                     print("invalid input")
main_menu()

    