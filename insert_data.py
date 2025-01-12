import sqlite3

# Create a connection to the SQLite database
connection = sqlite3.connect("blind/users.db")
cursor = connection.cursor()

# Create the 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Create the 'employees' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL
)
""")

# Insert sample data into 'users' table
users_data = [
    ("admin", "password123"),
    ("user1", "secret456"),
    ("user2", "test789")
]

cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users_data)

# Insert sample data into 'employees' table
employees_data = [
    ("admin@example.com",),
    ("employee1@example.com",),
    ("employee2@example.com",)
]

# Correctly inserting the email values as tuples
cursor.executemany("INSERT INTO employees (email) VALUES (?)", employees_data)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Tables created and sample data inserted successfully.")
