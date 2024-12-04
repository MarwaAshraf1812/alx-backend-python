#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Retrieves a batch of user data from the ALX_prodev database.

    Args:
        page_size (int): The number of rows of user data to include in each batch.
        offset (int): The row number to start the batch from.

    Returns:
        list of dict: A list of dictionaries, each representing a row of user data.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size: int):
    """
    A generator that yields batches of user data from the ALX_prodev database.

    Args:
        page_size (int): The number of rows of user data to include in each batch.

    Yields:
        list of dict: A list of dictionaries, each representing a row of user data.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
