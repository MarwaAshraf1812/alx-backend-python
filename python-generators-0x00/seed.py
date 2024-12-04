import mysql.connector
import uuid
import os
import csv

# Connect to MySQL server
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root12",
    )

# Create database if it does not exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Connect to ALX_prodev database
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root12",
        database="ALX_prodev"
    )

# Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5,2) NOT NULL,
            INDEX (user_id)
        )
    """)
    cursor.close()

# Insert data into user_data table
def insert_data(connection, file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist")
        return
    try:
        cursor = connection.cursor()
        with open(file_path, 'r') as f:
            # DictReader for field access by name
            readFile = csv.DictReader(f)
            for row in readFile:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    name = VALUES(name),
                    email = VALUES(email),
                    age = VALUES(age)""",
                    (str(uuid.uuid4()), row['name'], row['email'], row['age']))
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error: {e}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
