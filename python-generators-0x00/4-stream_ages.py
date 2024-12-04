#!/usr/bin/python3
seed = __import__('seed')
import mysql.connector

def stream_user_ages():
    """
    Streams the ages of users in the user_data table from the ALX_prodev database.

    Yields:
        float: The age of a user.

    Raises:
        mysql.connector.Error: If an error occurs during database access.
    """
    try:
        connection = seed.connect_to_prodev()
        # create a dictionary cursor to return rows as dictionaries
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row['age']

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        # locals() returns a dictionary of the current local symbol table
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()

def generate_average_age():
    """
    Calculates and prints the average age of all users in the user_data table in the ALX_prodev database.

    Prints "No users in the dataset." if the dataset is empty. Otherwise, prints the average age rounded to 2 decimal places.
    """

    total_ages = 0
    count = 0

    for age in stream_user_ages():
        total_ages += age
        count += 1

    if count == 0:
        print("No users in the dataset.")
    else:
        average_age = total_ages / count
        print(f"Average age: {average_age:.2f}")

if __name__ == '__main__':
    generate_average_age()
