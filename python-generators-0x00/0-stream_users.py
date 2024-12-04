import mysql.connector

def stream_users():
    """
    Streams user data from the ALX_prodev database.

    Connects to the 'user_data' table in the ALX_prodev database and yields each row as a dictionary.
    Closes the database connection and cursor after streaming the data.

    Yields:
        dict: A dictionary representing a row of user data.

    Raises:
        Exception: If an error occurs during database access or iteration.
    """
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root12',
        database='ALX_prodev'
    )
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
