"""
My first ATM code on python. Sat, Aug 5 2023. At North American University. Can be updated!
"""

# A = "123123"
# a = "0000"
# B = "123456"
# b = "1230"
# C = "789456"
# c = "7777"

# Balance_of_user_A = 1000000
# Balance_of_user_B = 999999.8
# Balance_of_user_C = 100.256

current_user = ""

Users = {
    "User_A" : {
        "Account_No" : "123123",
        "PIN" : "0000",
        "Balance" : 1000000,
        "Name" : "Tom",
        "Mobile No" : "+996700123123"
    },
    "User_B" : {
        "Account_No" : "123456",
        "PIN" : "1230",
        "Balance" : 999999.8,
        "Name" : "Alice",
        "Mobile No" : "+996777111444"
    },
    "User_C" : {
        "Account_No" : "789456",
        "PIN" : "7777",
        "Balance" : 100.256,
        "Name" : "Jhonatan",
        "Mobile No" : "+996777555555"
    }
}

print("**** Welcome to ATM ****\n")

print("Enter your Account No: ", end="")
acc = input()

if(acc == Users["User_A"]["Account_No"]):
    current_user = "User_A"
elif(acc == Users["User_B"]["Account_No"]):
    current_user = "User_B"
elif(acc == Users["User_C"]["Account_No"]):
    current_user = "User_C"
else: 
    print("ERROR")
    quit()

pin = input("Enter your PIN: ")

def start_page() -> None:
    """Welcome start page UI"""
    print("\n**Select Options**\n")
    print("1) Check Balance")
    print("2) Cash Withdraw")
    print("3) Deposite cash")
    print("4) Show User Details")
    print("5) Update Mobile No")
    print("6) Exit")

def check_balance(Balance) -> None:
    """Prints user's balance"""
    print(f"Your current balance: {float(Balance)}")

def cash_withdraw(withdraw) -> None:
    """subtracts user's balance"""
    x = float(input("Enter wish amount: "))
    if(x <= float(withdraw) and x > 0):
        print("Please collect your cash")
        print(f"Available Balance: {float(withdraw) - x}")
        Users[current_user]["Balance"] -= x
    else:
        print("ERROR")

def deposite_cash(deposite) -> None:
    """Adds money to user's balance"""
    v = float(input("Amount to deposite: "))
    print(f"Done. Your current balance: {float(deposite) + v}")
    Users[current_user]["Balance"] += v

def details_of_user(details) -> None:
    """Shows information of current user"""
    print("*** Your details are: -")
    print("-> Account no: " + details["Account_No"])
    print("-> Name -", details["Name"])
    print("-> Balance:", details["Balance"])
    print("-> Mobile No: " + details["Mobile No"])

def update_mobile(mobile) -> None:
    """Change user's phone number"""
    n = input("Please enter your old Mobile Number: ")
    if(n == mobile["Mobile No"]):
        new_number = input("Enter new number phone: ")
        print("Your Mobile No has succesfully updated to " + new_number)
        Users[current_user]["Mobile No"] = new_number
    else: 
        print("Wrong number")

# def exit():
#     print("Thanks for using our bank. \nSee you later")

if(acc == Users[current_user]["Account_No"] and pin == Users[current_user]["PIN"]):
    start_page()
    z = int(input())
    while(z != 6):
        if(z == 1): 
            check_balance(Users[current_user]["Balance"]) 
        if(z == 2): 
            cash_withdraw(Users[current_user]["Balance"]) 
        if(z == 3):
            deposite_cash(Users[current_user]["Balance"])
        if(z == 4):
            details_of_user(Users[current_user])
        if(z == 5):
            update_mobile(Users[current_user])
        start_page()
        z = int(input())
    else:
        print("Thanks for using our bank. \nSee you later")
        quit()      