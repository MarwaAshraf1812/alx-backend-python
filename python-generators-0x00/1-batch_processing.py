import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Streams user data from the ALX_prodev database in batches.

    Args:
        batch_size (int): The number of rows of user data to include in each batch.

    Yields:
        list of dict: A list of dictionaries, each representing a row of user data.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root12',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(size=batch_size)
            if not batch:
                break
            yield batch
        return
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes and prints batches of user data from the ALX_prodev database.

    Args:
        batch_size (int): The number of rows of user data to include in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user.get('age') > 25]
        if filtered_users:
            print(filtered_users)
        else:
            print("No users over the age of 25 in this batch.")
