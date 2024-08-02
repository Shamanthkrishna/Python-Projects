# Bank Management System

## Overview

The Bank Management System is a comprehensive banking application designed to manage customer accounts, transactions, and admin functionalities. This project serves as a backend system for a bank, allowing users to perform various banking operations such as deposits, withdrawals, transfers, and viewing transaction histories. The system is implemented using Python and MongoDB, which provides a scalable and flexible database solution.

## Features

### User Features
- **Sign Up**: Create a new account with a unique username, password, name, age, city, and account number.
- **Sign In**: Log into the system using a username and password.
- **Deposit**: Deposit funds into the account, updating the balance and recording the transaction.
- **Withdraw**: Withdraw funds from the account, updating the balance and recording the transaction.
- **Transfer**: Transfer funds to another account, updating balances and recording transactions for both sender and recipient.
- **View Balance**: Check the current account balance.
- **View Transaction History**: View a detailed list of all transactions, including deposits, withdrawals, and transfers.

### Admin Features
- **Admin Login**: Secure login for administrative access.
- **View Customer Count**: Get the total number of customers in the system.
- **View All Customers**: Display a list of all customers with their usernames, names, and account numbers.
- **View Transactions**: Fetch and display all transactions for a specific user based on their username.

## Working

1. **Database Setup**: The system uses MongoDB to store customer and transaction data. Ensure that MongoDB is running and properly connected to the application.
2. **Customer Management**: Users can sign up and sign in, while administrators can manage and view customer data.
3. **Transactions**: Customers can perform deposits, withdrawals, and transfers. Each transaction updates the database and maintains a transaction history.
4. **Admin Functionality**: Admins can log in to view statistics, customer details, and transaction histories for specific users.

## Project Adaptation and Database Choice

This project is based on a [guided tutorial](https://www.youtube.com/watch?v=KDIt2YO6euw) from YouTube, which originally used Python and SQL. I chose to adapt the project to use Python and MongoDB for several reasons:

- **Flexibility:** MongoDB's document-oriented database structure offers greater flexibility in handling varying data structures and schemas. This is particularly useful for evolving projects where the data model might change over time.

- **Scalability:** MongoDB is designed to scale out and handle large volumes of data across multiple servers, making it a suitable choice for projects that anticipate growth.

- **Ease of Use:** MongoDB's JSON-like documents provide a more intuitive way to store and query data compared to traditional relational databases. This simplifies development and maintenance.

- **Real-World Experience:** Working with MongoDB allowed me to gain practical experience with NoSQL databases, which are increasingly popular in modern web development.

By using MongoDB, I was able to tackle additional challenges and learn more about NoSQL databases while achieving a more adaptable and scalable solution for the banking system application.

## Future Plans

This project is currently in Phase 1. The next phase includes the development of a frontend using HTML/CSS, which will be connected to the backend to create a smooth and user-friendly interface. This will enhance the overall user experience and make the system more accessible.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**:
   Ensure you have Python and MongoDB installed.

3. **Setup MongoDB**:
   Ensure MongoDB is running and configured correctly.

4. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```
   
## Credits:

**[Guided Project]((https://www.youtube.com/watch?v=KDIt2YO6euw))**: This project is based on a guided tutorial from YouTube, which initially used Python and SQL. I adapted it to use Python and MongoDB, which introduced additional challenges and offered a more flexible database solution.
**ChatGPT**: For assistance with documentation, commenting code, and formatting the README file.

## Contributing

If you have any suggestions or would like to contribute to the project, please fork the repository and submit a pull request.
