# ATM Project README

This project is a basic ATM simulator written in Python. The code allows users to interact with the ATM by entering their account number and PIN to access various banking functionalities. The project was created on Sat, Aug 5, 2023, at North American University. It is a simple implementation and can be further updated and improved.

## Features

1. **User Authentication**: Users can enter their account number and PIN to log in to the ATM system.

2. **Check Balance**: After successful login, users can check their account balance.

3. **Cash Withdrawal**: Users can withdraw cash from their account, provided they have sufficient funds.

4. **Cash Deposit**: Users can deposit cash into their account, and their balance will be updated accordingly.

5. **View User Details**: Users can view their account details, including account number, name, balance, and mobile number.

6. **Update Mobile Number**: Users can change their registered mobile number associated with their account.

7. **Exit**: Users can exit the ATM system when they are done with their transactions.

## User Accounts

The project includes pre-defined user accounts stored in a dictionary named `Users`. Each user account contains the following information:

- Account_No: Account number (string)
- PIN: Personal Identification Number (string)
- Balance: Account balance (float)
- Name: User's name (string)
- Mobile No: User's mobile number (string)

## How to Use

1. Run the Python script to start the ATM system.

2. The system will prompt you to enter your Account No. Provide the account number associated with your account.

3. Once you enter the Account No, you will be asked to enter your PIN. Provide the correct PIN to log in successfully.

4. After successful login, you will be presented with a list of options to choose from:

    - 1) Check Balance
    - 2) Cash Withdraw
    - 3) Deposit cash
    - 4) Show User Details
    - 5) Update Mobile No
    - 6) Exit

5. Enter the number corresponding to the desired option to perform the corresponding action.

6. For options like Cash Withdraw, Deposit Cash, and Update Mobile No, you will be prompted to provide additional information as necessary.

7. To exit the system, choose option 6.

## Note

- The project is a simple implementation and does not involve actual banking transactions or authentication methods. It is intended for educational purposes only.

- The initial account balances and details are hardcoded in the script. For a real-world application, the account details should be stored securely in a database.

- This project can be further improved and expanded by adding more functionalities such as fund transfers, account statements, transaction history, etc.

- Use this project responsibly and do not use it for any illegal or unethical purposes.

## Acknowledgments

- The project was created by [Your Name] as a part of [Course Name/Personal Project/etc.] at North American University.

- The project may have been inspired by various online resources and tutorials, and credit goes to the respective authors for their contributions to the learning community.