import pandas as pd 
import os
from datetime import datetime 

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
       " description":input("enter the description (optional): ")}])

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

def main_menu(): 
    while True:
              print("your expence")
              print("1. add new expence \n2. view data \n3. view summery \n4. exit \n5. reset data")
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
              else : 
                     print("invalid input")
main_menu()

    