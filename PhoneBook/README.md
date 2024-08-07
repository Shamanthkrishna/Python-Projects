# PhoneBook Application

This is a simple command-line PhoneBook application written in Python. It allows users to add contacts, view contact details, load contacts to a CSV file, and import contacts from a CSV file.

## Features

- Add Contact: Save contact information including name, mobile number, and email address.
- View Contact Details: View saved contact details by name or mobile number.
- Load Contacts to CSV: Export all contacts to a CSV file.
- Import Contacts from CSV: Import contacts from a CSV file into the phonebook.

## Prerequisites

- Python 3.x
- MySQL
- `mysql-connector-python` package
- `pandas` package

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/phonebook.git
cd phonebook
```

2. **Install required packages:**

```bash
pip install mysql-connector-python pandas
```

3. **Set up MySQL Database:**

   - Open MySQL command line or any MySQL client.
   - Create a database named `phonebook`:

```sql
CREATE DATABASE phonebook;
```

   - Update the `connector.py` file with your MySQL credentials if they are different from the default.

## Usage

1. **Run the application:**

```bash
python main.py
```

2. **Menu Options:**

   - `1. Add Contact`: Enter the contact details when prompted.
   - `2. View Contact Details`: Choose to view by name or mobile number, then enter the corresponding value.
   - `3. Load Contacts to CSV`: Exports all contacts to `contacts.csv` file in the current directory.
   - `4. Import Contacts to PhoneBook from CSV`: Enter the path to the CSV file to import contacts from.
   - `5. Exit`: Exit the application.

## Files

- `main.py`: Main entry point for the application.
- `phonebook.py`: Contains functions to add, view, load to CSV, and import from CSV.
- `connector.py`: Handles MySQL database connection and table creation.
- `README.md`: This file.

## Example CSV File

Here's an example of a CSV file (`contacts_sample.csv`) to use for importing contacts:

```plaintext
name,mobile_number,email
John Doe,1234567890,john@example.com
Jane Smith,2345678901,jane@example.com
Alice Johnson,3456789012,alice@example.com
Bob Brown,4567890123,bob@example.com
Charlie Davis,5678901234,charlie@example.com
```

## Future Features

I have planned to add the following features in future releases:

- **Edit Contact:** Allow users to update the details of an existing contact.
- **Delete Contact:** Provide an option to delete a contact from the phonebook.
- **Search Contacts:** Allow users to search for contacts by partial name or partial mobile number.
- **Validate Email Uniqueness:** Ensure that no two contacts have the same email address.
- **Backup and Restore Database:** Provide functionality to back up the entire database to a file and restore it from a backup.
- **Advanced Search:** Allow searching for contacts using multiple criteria (e.g., name and email).
- **Sort Contacts:** Provide options to sort the contacts list by name, mobile number, or email.
- **Display All Contacts:** Add a feature to display all contacts in a paginated view.
- **Login System:** Implement a simple user authentication system to protect access to the phonebook.
- **Command-line Arguments:** Allow certain operations to be performed directly through command-line arguments (e.g., adding a contact).

## Notes

- Ensure the mobile number is exactly 10 digits.
- The email should follow the standard email format.
- Make sure the CSV file used for import has the columns: `name`, `mobile_number`, and `email`.
