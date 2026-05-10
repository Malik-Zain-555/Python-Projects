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
                content = file.read()

                if content:
                    data = json.loads(content)
                else:
                    data = []

        else:
            with open(Datafile, "w") as file:
                json.dump([], file)

    except Exception as err:
        print(f"Getting an error as {err}")

    @staticmethod
    def update():
        with open(Bank.Datafile, "w") as file:
            json.dump(Bank.data, file, indent=4)

    @classmethod
    def accountNumberGenerater(cls):

        while True:

            num = random.choices(string.digits, k=2)
            low_alpha = random.choices(string.ascii_lowercase, k=3)
            upper_alpha = random.choices(string.ascii_uppercase, k=3)
            sepChar = random.choices("!@#$%^&*", k=1)

            id = num + low_alpha + upper_alpha + sepChar

            random.shuffle(id)

            accNo = "".join(id)

            existing = [
                i for i in cls.data if i["accountNo."] == accNo
            ]

            if not existing:
                return accNo

    def Create_account(self):

        try:

            info = {
                "name": input("Enter your name: "),
                "age": int(input("Enter your age: ")),
                "email": input("Enter your email: "),
                "pin": int(input("Enter your pin(4-digit): ")),
                "accountNo.": Bank.accountNumberGenerater(),
                "balance": 0,
            }

            if info["age"] < 18 or len(str(info["pin"])) != 4:
                print("Sorry we can't proceed according to your info.")
                return

            print("\nAccount created successfully!\n")

            for i in info:
                print(f"{i}: {info[i]}")

            Bank.data.append(info)

            Bank.update()

        except ValueError:
            print("Invalid Input!")

    def Deposite_money(self):

        try:

            accNo = input("Enter Account Number:- ")
            pin = int(input("Enter Pin:- "))

            userDetails = [
                i for i in Bank.data
                if i["accountNo."] == accNo and i["pin"] == pin
            ]

            if not userDetails:
                print("Something Went Wrong!")
                return

            print("Account Found!")
            print(f"Welcome Back {userDetails[0]['name']}!")

            userDopistedMoney = int(
                input("How much you want to deposit? \nEnter your money:- ")
            )

            if userDopistedMoney < 0 or userDopistedMoney > 10000:
                print(
                    "Please deposit in between this given range( 0 - 10000 ) | Try again!"
                )

            else:
                userDetails[0]["balance"] += userDopistedMoney

                Bank.update()

                print(
                    f"The {userDopistedMoney} of money has been deposited successfully in your Bank!"
                )

        except ValueError:
            print("Invalid Input!")

    def Withdraw_money(self):

        try:

            accNo = input("Enter Account Number:- ")
            pin = int(input("Enter Pin:- "))

            userDetails = [
                i for i in Bank.data
                if i["accountNo."] == accNo and i["pin"] == pin
            ]

            if not userDetails:
                print("Something Went Wrong!")
                return

            print("Account Found!")
            print(f"Welcome Back {userDetails[0]['name']}!")

            userWithdrawMoney = int(
                input("How much you want to withdraw? \nEnter your money:- ")
            )

            if userWithdrawMoney < 0 or userWithdrawMoney > 10000:
                print(
                    "Please withdraw in between this given range( 0 - 10000 ) | Try again!"
                )

            else:

                if userWithdrawMoney > userDetails[0]["balance"]:
                    print("You don't have enough money to withdraw!")

                else:

                    userDetails[0]["balance"] -= userWithdrawMoney

                    Bank.update()

                    print(
                        f"The {userWithdrawMoney} of money has been withdraw successfully in your Bank!"
                    )

        except ValueError:
            print("Invalid Input!")

    def Account_details(self):

        try:

            accNo = input("Enter Account Number:- ")
            pin = int(input("Enter Pin:- "))

            userDetails = [
                i for i in Bank.data
                if i["accountNo."] == accNo and i["pin"] == pin
            ]

            if not userDetails:
                print("Something Went Wrong!")

            else:

                print("\nAccount Found!\n")

                for keys, values in userDetails[0].items():
                    print(f"{keys}: {values}")

        except ValueError:
            print("Invalid Input!")

    def Update_account(self):

        try:

            accNo = input("Enter Account Number:- ")
            pin = int(input("Enter Pin:- "))

            userDetails = [
                i for i in Bank.data
                if i["accountNo."] == accNo and i["pin"] == pin
            ]

            if not userDetails:
                print("Something Went Wrong!")
                return

            print("Account Found!")

            print(
                "Enter your new Details Below or Press 'Enter key' for skip: "
            )

            new_name = input("Enter your new name: ")
            new_email = input("Enter your new email: ")
            new_pin = input("Enter your new pin: ")

            if new_name:
                userDetails[0]["name"] = new_name

            if new_email:
                userDetails[0]["email"] = new_email

            if new_pin:

                if not new_pin.isdigit() or len(new_pin) != 4:
                    print(
                        "Invalid pin. Pin must be 4 digits. Keeping old pin."
                    )

                else:
                    userDetails[0]["pin"] = int(new_pin)

            Bank.update()

            print("Account updated successfully!")

        except ValueError:
            print("Invalid Input!")

    def Delete_account(self):

        try:

            accNo = input("Enter Account Number:- ")
            pin = int(input("Enter Pin:- "))

            userDetails = [
                i for i in Bank.data
                if i["accountNo."] == accNo and i["pin"] == pin
            ]

            if not userDetails:
                print("Something Went Wrong!")
                return

            userConfirmation = input(
                "Enter 'Y' for deleting this account and 'N' for Stop it: "
            )

            if userConfirmation == "N" or userConfirmation == "n":
                return

            Bank.data.remove(userDetails[0])

            Bank.update()

            print("Account has been deleted successfully!")

        except ValueError:
            print("Invalid Input!")


user = Bank()

print("\n====== Welcome To Bank System ======\n")

print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

try:

    userResponse = int(input("\nEnter your option: "))

    if userResponse == 1:
        user.Create_account()

    elif userResponse == 2:
        user.Deposite_money()

    elif userResponse == 3:
        user.Withdraw_money()

    elif userResponse == 4:
        user.Account_details()

    elif userResponse == 5:
        user.Update_account()

    elif userResponse == 6:
        user.Delete_account()

    else:
        print("Invalid Option!")

except ValueError:
    print("Please enter numbers only!")