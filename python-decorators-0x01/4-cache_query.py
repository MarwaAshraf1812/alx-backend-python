import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    """
    A decorator that automatically connects and closes a database connection for a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def cache_query(func):
    """
    A decorator that caches the results of database queries based on the SQL query string.
    """
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
      if query in query_cache:
          print(f"Using cached result for query: {query}")
          return query_cache[query]
      else:
          result = func(conn, query, *args, **kwargs)
          query_cache[query] = result
          return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")