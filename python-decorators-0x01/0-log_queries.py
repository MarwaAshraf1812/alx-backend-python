import sqlite3
import functools

#### decorator to lof SQL queries
def log_queries(func):
    """
    A decorator that logs the SQL query being executed by the function.

    It works by getting the query from either the first positional argument
    or the keyword argument named 'query'. If the query is not None, it
    prints it out with a message before executing the function.

    :param func: The function whose first argument is the SQL query.
    :return: A new function that logs the query before executing the
        original function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or args[0]
        if query:
            print(f"Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
