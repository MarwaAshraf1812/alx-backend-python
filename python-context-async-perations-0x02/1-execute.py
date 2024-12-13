import mysql.connector

class ExecuteQuery:
    def __init__(self, db_connection, query, params=None):
        self.db_connection = db_connection
        self.query = query
        self.params = params if params is not None else ()
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Establishes the database connection and executes the query.
        """
        self.connection = mysql.connector.connect(**self.db_connection)
        self.cursor = self.connection.cursor(dictionary=True)
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Ensures cleanup of the cursor and the connection.
        """
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
    query = "SELECT * FROM user_data WHERE age > %s"
    params = (25, )

    with ExecuteQuery(db_connection, query, params) as users:
        for row in users:
            print(row)
