import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')


cursor.execute("INSERT INTO users (name, age) VALUES ('Mike', 20)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Jane', 27)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Tom', 31)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Jenny', 18)")

connection.commit()
connection.close()


print("Database and table created, with sample data inserted.")