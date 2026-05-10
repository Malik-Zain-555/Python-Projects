import random
import string
from pathlib import Path
import json

class Bank:
    
    Datafile = Path("data.json")
    data = []
    
    try:
        if Datafile.exists():
            with open(Datafile) as file:
                data = json.loads(file.read())
        else:
            with open(Datafile, "w") as file:
                json.dump([], file) #changed the line according to 'GPT' before:- data = json.loads(file.read())
    except Exception as err:
        print(f"Getting an error as {err}")
    
    @staticmethod
    def update():
        with open(Bank.Datafile, "w") as file:
            file.write(json.dumps(Bank.data))
    
    @classmethod
    def accountNumberGenerater(cls):
            num = random.choices(string.digits,k=2)
            low_alpha = random.choices(string.ascii_lowercase,k=3)
            upper_alpha = random.choices(string.ascii_uppercase,k=3)
            sepChar = random.choices("!@#$%^&*",k=1)
            id = num+low_alpha+upper_alpha+sepChar
            random.shuffle(id)
            return "".join(id)
    
    def Create_account(self):
        info = {
            "name":input("Enter your name: "),
            "age":int(input("Enter your age: ")),
            "email":input("Enter your email: "),
            "pin":int(input("Enter your pin(4-digit): ")),
            "accountNo.": Bank.accountNumberGenerater(),
            "balance": 0,
        }
        
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry we can't proceed according to your info.")
        else:
            print("Account created successfully!")
            for i in info:
                print(f"{i}: {info[i]}")

        Bank.data.append(info)
        
        Bank.update()
    
    def Deposite_money(self):
        accNo = input("Enter Account Number:- ")
        pin = int(input("Enter Pin:- "))
        
        userDetails = [i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin]
        
        if userDetails == False:
            print("Something Went Wrong!")
        else:
            print("Account Found!")
            print(f"Welcome Back {userDetails[0]["name"]}!")
            userDopistedMoney = int(input("How much you want to deposit? \nEnter your money:- "))
            userDetails[0]["balance"] += userDopistedMoney
            Bank.update()
            print(f"The {userDopistedMoney} of money has been deposited successfully in your Bank!")

user = Bank()

print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

userResponse = int(input("Enter your option: "))

if userResponse == 1:
    user.Create_account()
if userResponse == 2:
    user.Deposite_money()