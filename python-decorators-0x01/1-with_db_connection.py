import sqlite3 
import functools

def with_db_connection(func):
  """
  A decorator that automatically connects and closes a database connection for a function.

  It works by connecting to the database before calling the function and closing
  the connection after the function has finished. If an exception is raised, the
  connection is also closed.

  The function being decorated is expected to take a connection object as its first
  argument.

  :param func: The function whose first argument is a connection object.
  :return: A new function that connects to the database before calling the original
      function and closes the connection afterwards.
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

@with_db_connection 
def get_user_by_id(conn, user_id): 
  """
  Fetches a user by their ID from the database.

  The function is decorated with with_db_connection, so it automatically
  connects to the database and closes the connection afterwards.

  :param conn: The database connection. This is automatically provided by the
      with_db_connection decorator.
  :param user_id: The ID of the user to fetch.
  :return: The user with the given ID, or None if no such user exists.
  """
  cursor = conn.cursor() 
  cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
  return cursor.fetchone()

#### Fetch user by ID with automatic connection handling 
user = get_user_by_id(user_id=1)
print(user)