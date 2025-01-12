import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
conn.commit()


def vulnerable_login(username, password):

    query = f"SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing Query: {query}")

    cursor.execute(query,(username, password))
    result = cursor.fetchone()

    if result:
        return "Login successful!"
    else:
        return "Login failed!"



# print(vulnerable_login('admin', 'password123'))
# print(vulnerable_login("' OR 1=1--", ''))
# print(vulnerable_login("' OR 1=0--", ''))
# print(vulnerable_login("admin' OR '1'='1", ''))
