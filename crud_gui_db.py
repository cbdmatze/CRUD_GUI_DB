import mysql.connector


# Establish a connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ma-294022275",
    database="moviewebapp"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example: Execute a query
cursor.execute("SHOW TAABLES")

# Fetch the results
for table in cursor:
    print(table)

# Close the connection
conn.close()
