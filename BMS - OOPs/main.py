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
        
        if not userDetails:
            print("Something Went Wrong!")
            return
        print("Account Found!")
        print(f"Welcome Back {userDetails[0]["name"]}!")
        userDopistedMoney = int(input("How much you want to deposit? \nEnter your money:- "))
        if userDopistedMoney < 0 and userDopistedMoney > 10000:
            print("Please deposite in between this given range( 0 - 10000 ) | Try again!")
        else:
            userDetails[0]["balance"] += userDopistedMoney
            Bank.update()
            print(f"The {userDopistedMoney} of money has been deposited successfully in your Bank!")
    
    def Withdraw_money(self):
        accNo = input("Enter Account Number:- ")
        pin = int(input("Enter Pin:- "))
        
        userDetails = [i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin]
        
        if not userDetails:
            print("Something Went Wrong!")
            return
        print("Account Found!")
        print(f"Welcome Back {userDetails[0]["name"]}!")
        userWithdrawMoney = int(input("How much you want to withdraw? \nEnter your money:- "))
        if userWithdrawMoney < 0 and userWithdrawMoney > 10000:
            print("Please withdraw in between this given range( 0 - 10000 ) | Try again!")
        else:
            if userWithdrawMoney > userDetails[0]["balance"]:
                print("You don'tave enough money to withdraw!")
            else:
                userDetails[0]["balance"] -= userWithdrawMoney
                Bank.update()
                print(f"The {userWithdrawMoney} of money has been withdraw successfully in your Bank!")
    
    def Account_details(self):
        accNo = input("Enter Account Number:- ")
        pin = int(input("Enter Pin:- "))
        
        userDetails = [i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin]
        
        if userDetails == False:
            print("Something Went Wrong!")
        else:
            print("\nAccount Found!\n\n")
            for keys,values in userDetails[0].items():
                print(f"{keys}: {values}")
    
    def Update_account(self):
        accNo = input("Enter Account Number:- ")
        pin = int(input("Enter Pin:- "))
        
        userDetails = [i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin]
        
        if not userDetails:
            print("Something Went Wrong!")
            return
        
        print("Account Found!")
    
        print("Enter your new Details Below or Press 'Enter key' for skip: ")
        
        new_name = input("Enter your new name: ")
        new_email = input("Enter your new email: ")
        new_pin = input("Enter your new pin: ")
        
        if new_name:
            userDetails[0]["name"] = new_name
        if new_email:
            userDetails[0]["email"] = new_email
        if new_pin:
            if new_pin.isdigit() and len(new_pin) != 4:
                print("Invalid pin. Pin must be 4 digits. Keeping old pin.")
            else:
                userDetails[0]["pin"] = int(new_pin)

        Bank.update()

    def Delete_account(self):
        accNo = input("Enter Account Number:- ")
        pin = int(input("Enter Pin:- "))
        
        userDetails = [i for i in Bank.data if i["accountNo."] == accNo and i["pin"] == pin]
        
        if not userDetails:
            print("Something Went Wrong!")
            return
        
        userConfirmation = input("Enter 'Y' for deleting this account and 'N' for Stop it: ")
        
        if userConfirmation == "N" or userConfirmation == "n":
            return
        
        # print(userDetails)
        # print(Bank.data)
        Bank.data.remove(userDetails[0])
        Bank.update()
        
        print("Account has been deleted successfully!")

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
if userResponse == 3:
    user.Withdraw_money()
if userResponse == 4:
    user.Account_details()
if userResponse == 5:
    user.Update_account()
if userResponse == 6:
    user.Delete_account()