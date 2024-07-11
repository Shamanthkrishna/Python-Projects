import getpass

database = {"shamanth.krishna": "123456", "krishna.shamanth": "654321", "abc.abc": "123"}

def login():
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        username = input("Enter Your Username : ")
        if username not in database:
            print("Username not found. Please Try Again")
            continue

        password = getpass.getpass("Enter Your Password : ")

        if database[username] == password:
            print("Verified")
            return True
        else:
            attempts+=1
            print(f"Incorrect Password. Attempts left: {max_attempts - attempts}")
    
    print("Too many attempts, Access denied.")
    return False

while True:
    if login():
        break

    try_again = input("Do you want to try again? (y/n): ").lower()
    if try_again != "y":
        break

print("Thank you for using the login system.")
input("Press any key to exit....")
    
