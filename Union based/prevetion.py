import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest')")
conn.commit()


def secure_query(input_payload):
    try:

        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (input_payload,))
        result = cursor.fetchall()

        if result:
            return result
        else:
            return "No data found."
    except Exception as e:
        return f"Error: {e}"


input_payloads = [
    1,
    "1' UNION SELECT null, null, null--",
    "1' UNION SELECT username, password, null FROM users--",
]


print("Testing Secure Queries...\n")
for payload in input_payloads:
    result = secure_query(payload)
    print(f"Input: {payload}\nResult: {result}\n{'-'*50}")


conn.close()
