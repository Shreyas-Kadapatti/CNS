import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest')")
conn.commit()


def safe_query(input_payload):
    try:
        # Using parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE id = ?"
        print(f"Executing Query: {query} with input {input_payload}")
        cursor.execute(query, (input_payload,))
        result = cursor.fetchall()

        if result:
            return "Query executed successfully!"
        else:
            return "No data found."
    except Exception as e:
        return f"Error: {e}"


# # List of payloads to test safe query
# payloads = ["1", "2", "3"]  # Only valid IDs for demonstration

# payloads = [
#     "1 OR 1=1",  # Always true condition
#     "1 OR 1/0",  # Division by zero error
#     "1 OR CAST('abc' AS INT)",  # Invalid cast error
#     "1 OR FLOOR(1/0)",  # Division by zero using a function
#
# ]

print("Testing Safe Queries...\n")
for payload in payloads:
    result = safe_query(payload)
    print(f"Payload: {payload}\nResult: {result}\n{'-' * 50}")
