import mysql.connector

class DatabaseConnection:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.connection = None
    self.cursor = None

  def __enter__(self):
    self.connection = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.password,
      database = self.database
    )
    self.cursor = self.connection.cursor(dictionary=True)
    return self.cursor
  
  def __exit__(self, exc_type, exc_value, exc_traceback):
    self.connection.commit()
    if self.cursor:
      self.cursor.close()
    if self.connection:
      self.connection.close()

if __name__ == "__main__":
  db_connection = {
    "host": "localhost",
    "user": "root",
    "password": "root12",
    "database": "ALX_prodev"
  }

  with DatabaseConnection(**db_connection) as cursor:
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for row in users:
      print(row)
