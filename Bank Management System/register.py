# User Registration Sign In & Sign Up
from database import *
from customer import *
from bank import *
import random 

db = get_db()
customers = db['customers']

def signUp():
    """
    Handles user registration by allowing a new user to create an account.
    This function prompts the user for a username, password, name, age, and city.
    It generates a unique account number and initializes the user's balance to 0.
    If the username already exists, it asks the user to create a new username.
    """
    username = input("Create Username: ")
    checkUser = customers.find_one({"username": username})
    
    if checkUser:
        print("Username Already Exists")
        signUp()  # Recursively call signUp to retry with a new username
    else:
        print("Username is Available, Please Proceed...")
        password = input("Enter your Password: ")
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")
        city = input("Enter your City: ")
        
        # Generate a unique account number
        while True:
            account_number = random.randint(10000000, 99999999)
            checkAcNo = customers.find_one({"account_number": account_number})
            if checkAcNo:
                continue  # Generate a new account number if the current one is already taken
            else:
                print(f"Your Issued Account number: {account_number}")
                break
        
        # Create a Customer object and initialize the user
        cObj = Customer(username, password, name, age, city, account_number)
        cObj.createUser()  # Save the customer details to the database
        
        # Create a Bank object for the new user and set initial balance to 0
        bObj = Bank(username, account_number)
        bObj.updateCustomerBalance(0)  # Set the initial balance to 0

def signIn():
    """
    Handles user login and provides access to various banking services.
    This function verifies the user's credentials and presents a menu for 
    transactions such as deposit, withdrawal, transfer, account details, 
    and transaction history. Allows the user to log out.
    """
    username = input("Enter your Username: ")
    User = customers.find_one({"username": username})

    if User:
        while True:
            print(f"Welcome {username.capitalize()}")
            entered_password = input("Enter your Password: ")
            stored_password = User["password"]

            if entered_password == stored_password:
                print("Sign-In Successful")
                bank = Bank(username, User["account_number"])
                
                while True:
                    # Display options menu
                    print("\nOptions:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer Money to another A/c")
                    print("4. Check Account Details")
                    print("5. View Transaction History")
                    print("Type 'exit' to Log out")

                    action = input("Choose an option: ")

                    if action == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        bank.deposit(amount)

                    elif action == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        bank.withdraw(amount)
                    
                    elif action == '3':
                        recipient_account_number = int(input("Enter recipient account number: "))
                        amount = float(input("Enter the amount to transfer: "))
                        bank.transfer(recipient_account_number, amount)

                    elif action == '4':
                        bank.getAccountDetails()

                    elif action == '5':
                        bank.getTransactionHistory()
                    
                    elif action.lower() == 'exit':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Please try again.")
                break
            else:
                print("Incorrect Password. Please Try Again")
    else:
        print("Username Not Found...")
