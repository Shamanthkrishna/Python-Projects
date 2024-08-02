# Bank Services
from database import *
from datetime import datetime

db = get_db()

class Bank:
    def __init__(self, username, account_number):
        """
        Initializes the Bank class with the given username and account number.
        Sets up the database connections for customers and transactions.

        Args:
            username (str): The username of the account holder.
            account_number (int): The account number of the account holder.
        """
        self.__username = username
        self.__account_number = account_number
        self.__db = get_db()
        self.__customers = self.__db['customers']
        self.__transactions = self.__db['transactions']

    def createTransactionDoc(self, remarks, amount, balance):
        """
        Creates and inserts a transaction document into the transactions collection.

        Args:
            remarks (str): Description of the transaction.
            amount (float): Amount of the transaction. Positive for deposits and negative for withdrawals.
            balance (float): Account balance after the transaction.
        """
        transactionDoc = {
            "username": self.__username,
            "account_number": self.__account_number,
            "timedate": datetime.utcnow(),
            "remarks": remarks,
            "amount": amount,
            "balance": balance
        }

        self.__db["transactions"].insert_one(transactionDoc)

    def getCurrentBalance(self):
        """
        Retrieves the current balance of the account from the customers collection.

        Returns:
            float: The current balance of the account.
        """
        customer = self.__customers.find_one({"username": self.__username})
        return customer.get("balance", 0)
    
    def updateCustomerBalance(self, username, new_balance):
        """
        Updates the balance of a customer in the customers collection.

        Args:
            username (str): The username of the customer whose balance is to be updated.
            new_balance (float): The new balance to be set.
        """
        self.__customers.update_one(
            {"username": username},
            {"$set": {"balance": new_balance}}
        )

    def deposit(self, amount):
        """
        Deposits a specified amount into the account. Updates the balance and records the transaction.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        # Get the current balance and calculate the new balance
        current_balance = self.getCurrentBalance()
        new_balance = current_balance + amount

        # Record the transaction and update balance in both collections
        self.createTransactionDoc(remarks="Deposit", amount=amount, balance=new_balance)
        self.updateCustomerBalance(self.__username, new_balance)
        print(f"Deposited {amount} successfully. New balance: {new_balance}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account. Updates the balance and records the transaction.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        # Get the current balance
        current_balance = self.getCurrentBalance()

        if current_balance >= amount:
            new_balance = current_balance - amount

            # Record the transaction and update balance in both collections
            self.createTransactionDoc(remarks="Withdrawal", amount=-amount, balance=new_balance)
            self.updateCustomerBalance(self.__username, new_balance)
            print(f"Withdrew {amount} successfully. New balance: {new_balance}")
        else:
            print("Insufficient balance.")

    def checkBalance(self):
        """
        Prints the current balance of the account.
        """
        current_balance = self.getCurrentBalance()
        print(f"Current balance: {current_balance}")

    def transfer(self, recipient_account_number, amount):
        """
        Transfers a specified amount to another account. Updates balances and records transactions for both accounts.

        Args:
            recipient_account_number (int): The account number of the recipient.
            amount (float): The amount to transfer. Must be positive.
        """
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        # Get the sender's current balance
        sender_balance = self.getCurrentBalance()

        # Check if sender has sufficient balance
        if sender_balance < amount:
            print("Insufficient balance for transfer.")
            return

        # Check if recipient account exists
        recipient = self.__customers.find_one({"account_number": recipient_account_number})
        if not recipient:
            print("Recipient account number not found.")
            return

        # Update sender's balance
        new_sender_balance = sender_balance - amount
        self.updateCustomerBalance(self.__username, new_sender_balance)
        self.createTransactionDoc(
            remarks=f"Transfer to {recipient_account_number}",
            amount=-amount,
            balance=new_sender_balance
        )

        # Update recipient's balance
        recipient_username = recipient['username']
        recipient_balance = recipient.get("balance", 0)
        new_recipient_balance = recipient_balance + amount
        self.__customers.update_one(
            {"username": recipient_username},
            {"$set": {"balance": new_recipient_balance}}
        )
        self.__transactions.insert_one(
            {
                "username": recipient_username,
                "account_number": recipient_account_number,
                "timedate": datetime.utcnow(),
                "remarks": f"Transfer from {self.__account_number}",
                "amount": amount,
                "balance": new_recipient_balance
            }
        )

        print(f"Transferred {amount} to account {recipient_account_number}. New balance: {new_sender_balance}")


    def getAccountDetails(self):
        """
        Prints the account details including username, name, age, city, account number, and balance.

        This method fetches the details from the customers collection and displays them.
        """
        customer = self.__customers.find_one({"username": self.__username})
        if customer:
            print("Account Details:")
            print(f"Username: {customer.get('username')}")
            print(f"Name: {customer.get('name')}")
            print(f"Age: {customer.get('age')}")
            print(f"City: {customer.get('city')}")
            print(f"Account Number: {customer.get('account_number')}")
            print(f"Balance: {self.getCurrentBalance()}")
        else:
            print("Account not found.")

    def getTransactionHistory(self):
        """
        Prints the transaction history in a formatted manner.

        Transactions are sorted by date in ascending order. Each transaction is displayed with its
        date, remarks, credit, debit, and balance. The formatting includes vertical lines to separate
        each section.
        """
        history = self.__transactions.find({"username": self.__username}).sort("timedate", 1)
        print("Transaction History:")
        header_format = "{:<20} | {:<30} | {:>10} | {:>10} | {:>10}"
        print(header_format.format("Date", "Particulars", "Credit", "Debit", "Balance"))
        print("-" * 100)

        for record in history:
            date = record.get("timedate").strftime("%d-%m-%Y %H:%M:%S")
            remarks = record.get("remarks", "")
            amount = record.get("amount", 0)
            balance = record.get("balance", 0)
            credit = f"{amount:.2f}" if amount > 0 else ""
            debit = f"{-amount:.2f}" if amount < 0 else ""
            
            print(header_format.format(date, remarks, credit, debit, f"{balance:.2f}"))
