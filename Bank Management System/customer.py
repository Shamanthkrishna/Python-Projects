# Customer Details
from database import *

class Customer:
    """
    Represents a customer in the banking system.

    Attributes:
        __username (str): The username of the customer.
        __password (str): The password of the customer (should be hashed).
        __name (str): The full name of the customer.
        __age (int): The age of the customer.
        __city (str): The city where the customer resides.
        __account_number (int): The unique account number assigned to the customer.
    """

    def __init__(self, username, password, name, age, city, account_number):
        """
        Initializes a new Customer instance with the provided details.

        Args:
            username (str): The username of the customer.
            password (str): The password of the customer (should be hashed).
            name (str): The full name of the customer.
            age (int): The age of the customer.
            city (str): The city where the customer resides.
            account_number (int): The unique account number assigned to the customer.
        """
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createUser(self):
        """
        Creates a new user document in the 'customers' collection of the database.

        This method inserts a document representing the customer into the 'customers' 
        collection in the database. The document includes the customer's username, 
        password, name, age, city, account number, and an active status.

        The 'status' field is set to True, indicating that the account is active.

        The document structure:
        {
            "username": str,              # The customer's username
            "password": str,              # The customer's hashed password
            "name": str,                  # The customer's full name
            "age": int,                   # The customer's age
            "city": str,                  # The customer's city of residence
            "account_number": int,        # The unique account number
            "status": bool                # Indicates if the account is active
        }
        """
        # Access the database and the 'customers' collection
        db = get_db()
        customers = db['customers']

        # Create a dictionary with customer data
        customer_data = {
            "username": self.__username,
            "password": self.__password,
            "name": self.__name,
            "age": self.__age,
            "city": self.__city,
            "account_number": self.__account_number,
            "status": True  # Account status is set to active
        }

        # Insert the customer data into the collection
        customers.insert_one(customer_data)
