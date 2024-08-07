import mysql.connector


def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin123',
        database='phonebook'
    )

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            mobile_number VARCHAR(10) NOT NULL,
            email VARCHAR(30)
        )
    ''')
    connection.close()

def execute_query(query, params=None):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    connection.close()
