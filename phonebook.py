import re
from connector import *
import pandas as pd


def add_contact():
    name = input("Enter contact name: ")

    while True:
        mobile_number = input("Enter Mobile Number (10 Digits): ")
        if re.match(r"^[0-9]{10}$", mobile_number):
            break
        else:
            print("Invalid mobile number. It should be exactly 10 digits")

    while True:
        email = input("Enter Email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        else:
            print("Invalid email address.")
    
    print("\nReview the contact details:")
    print(f"Name:{name}\nMobile Number:{mobile_number} \nEmail:{email}")
    confirm = input("Do you want to submit? (Y/N):").upper()
    if confirm=='Y':
        query = '''
            INSERT INTO contacts (name, mobile_number, email)
            VALUES (%s, %s, %s)
            '''
        execute_query(query, (name, mobile_number, email))
        print("Contact added successfully!")
    
    else:
        print("Contact not added. Please re-enter the details.")

            
        

def view_contact():
    print("View Contacts By:")
    print("1. Name")
    print("2. Mobile Number")

    choice = int(input("Enter your choice: "))

    if choice==1:
        name = input("Enter the Name:")
        query = ' SELECT * FROM contacts WHERE name = %s'
        params = (name,)
    elif choice==2:
        mobile_number = input("Enter Mobile Number:")
        query = ' SELECT * FROM contacts WHERE mobile_number = %s'
        params = (mobile_number,)
    else:
        print("Invalid Choice")
        return
    
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    connection.close()

    if results:
        for row in results:
            print(f"\nID: {row[0]} \nName: {row[1]} \nMobile Number: {row[2]} \nEmail: {row[3]}")
    else:
        print("No Contact Found")


def load_to_csv(filename='contacts.csv'):
    query = 'SELECT * FROM  contacts'
    connection = create_connection()
    df = pd.read_sql(query, connection)
    connection.close()
    df.to_csv(filename, index=False)
    print(f"Data has been loaded into {filename}")

def import_from_csv():
    filename = input("Enter the path of the CSV file to import: ")
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"The file {filename} is empty.")
        return
    except pd.errors.ParserError:
        print(f"The file {filename} could not be parsed.")
        return

    connection = create_connection()
    cursor = connection.cursor()
    
    for index, row in df.iterrows():
        query = 'INSERT INTO contacts (name, mobile_number, email) VALUES (%s, %s, %s)'
        cursor.execute(query, (row['name'], row['mobile_number'], row['email']))
    
    connection.commit()
    connection.close()
    print(f"Data from {filename} has been imported into the database.")
    
