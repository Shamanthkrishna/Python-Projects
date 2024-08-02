# Main Entry Point for SKB Bank Project
from register import *  # Import functions for user registration and login
from admin import admin_login  # Import the admin login function

print("Welcome to SKB Bank Project")  # Welcome message for the user

while True:
    try:
        # Display menu options to the user
        print("1. Sign Up\n"
              "2. Sign In\n"
              "3. Admin Login\n"
              "4. Exit\n")
        choice = input("Choose an option: ")  # Prompt user to choose an option

        if choice == '1':
            signUp()  # Call sign-up function to register a new user
        elif choice == '2':
            signIn()  # Call sign-in function to allow user login
        elif choice == '3':
            admin_login()  # Call admin login function for admin access
        elif choice == '4':
            print("Exiting...")  # Print message and exit the loop
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choices

    except ValueError:
        # Handle non-integer inputs
        print("Invalid Input, Try Again")  # Print error message for invalid input
