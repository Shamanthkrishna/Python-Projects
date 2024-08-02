# Database Management
from pymongo import MongoClient

def get_db():
    """
    Connects to the MongoDB database and returns the database object.
    
    This function establishes a connection to the MongoDB server running 
    locally on the default port (27017) and retrieves the 'bank' database.
    This database object can be used to interact with collections within 
    the 'bank' database.

    Returns:
        db (pymongo.database.Database): The MongoDB database object for 'bank'.
    """
    # Create a client instance connected to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')
    
    # Access the 'bank' database
    db = client['bank']
    
    # Return the database object
    return db

# Example document structure for user data (commented out):
# This is an example structure of a document that could be stored in 
# the 'customers' collection. Each field represents an attribute of 
# the customer.
#
# docStructure = {
#     "username": None,           # The username of the customer
#     "password": None,           # The hashed password of the customer
#     "name": None,               # The full name of the customer
#     "age": None,                # The age of the customer
#     "city": None,               # The city where the customer resides
#     "account_number": None,     # The unique account number of the customer
#     "status": None,             # The status of the account (e.g., active, inactive)
#     "balance": None             # The current balance in the customer's account
# }
