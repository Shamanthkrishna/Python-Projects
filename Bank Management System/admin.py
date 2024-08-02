# admin.py
from database import get_db  # Import the function to get the database connection

def admin_login():
    """
    Handles the admin login process. Checks if the entered username and password match
    the predefined admin credentials.
    """
    # Simple admin credentials (for demonstration purposes only)
    admin_username = "admin"
    admin_password = "admin123"  # Consider hashing/admin security in a real application

    # Prompt for admin login
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    # Validate credentials
    if username == admin_username and password == admin_password:
        print("Admin Login Successful")
        admin_menu()  # Call the admin menu if credentials are correct
    else:
        print("Invalid credentials. Access denied.")  # Print error if credentials are incorrect

def admin_menu():
    """
    Displays the admin menu with options to view customer count, all customers,
    or all transactions. Handles user input to perform the selected action.
    """
    while True:
        # Display menu options
        print("\nAdmin Menu:")
        print("1. View Customer Count")
        print("2. View All Customers")
        print("3. View All Transactions")
        print("4. Exit")

        choice = input("Choose an option: ")  # Prompt user for menu choice

        if choice == '1':
            view_customer_count()  # Call function to view customer count
        elif choice == '2':
            view_all_customers()  # Call function to view all customers
        elif choice == '3':
            # Prompt for username to view transactions
            username = input("Enter the username to view transactions: ")
            view_all_transactions(username)  # Call function to view transactions for a specific user
        elif choice == '4':
            print("Exiting...")
            break  # Exit the menu loop
        else:
            print("Invalid choice. Please try again.")  # Print error for invalid menu choice

def view_customer_count():
    """
    Fetches and displays the total number of customers from the database.
    """
    db = get_db()  # Get the database connection
    customers = db['customers']  # Access the 'customers' collection
    count = customers.count_documents({})  # Count the number of documents (customers)
    print(f"Total number of customers: {count}")  # Print the total count

def view_all_customers():
    """
    Fetches and displays all customer details from the database.
    """
    db = get_db()  # Get the database connection
    customers = db['customers']  # Access the 'customers' collection
    # Fetch customer details excluding '_id'
    customer_list = customers.find({}, {"_id": 0, "username": 1, "name": 1, "account_number": 1, "age": 1, "city": 1})
    print("\nCustomer List:")
    for customer in customer_list:
        # Print each customer's details
        print(f"Username: {customer['username']}")
        print(f"Name: {customer['name']}")
        print(f"Account Number: {customer['account_number']}")
        print(f"Age: {customer['age']}")
        print(f"City: {customer['city']}")
        print("-" * 40)  # Separator for better readability

def view_all_transactions(username):
    """
    Fetches and displays all transactions for a specific user based on their username.
    
    Args:
        username (str): The username of the user whose transactions are to be fetched.
    """
    db = get_db()  # Get the database connection
    transactions = db['transactions']  # Access the 'transactions' collection
    
    # Count the number of transactions for the given username
    transaction_count = transactions.count_documents({"username": username})
    
    if transaction_count == 0:
        print("No transactions found for this user.")  # Print message if no transactions are found
        return
    
    # Print the transaction history
    print(f"\nTransaction History for Username: {username}")
    print(f"{'Date':<25} | {'Remarks':<20} | {'Amount':>10} | {'Balance':>10}")
    print("-" * 70)

    # Fetch and print all transactions for the given username
    user_transactions = transactions.find({"username": username})

    for transaction in user_transactions:
        # Format and print each transaction
        timedate = transaction.get("timedate").strftime("%Y-%m-%d %H:%M:%S")
        remarks = transaction.get("remarks", "")
        amount = transaction.get("amount", 0)
        balance = transaction.get("balance", 0)
        
        print(f"{timedate:<25} | {remarks:<20} | {amount:>10.2f} | {balance:>10.2f}")
