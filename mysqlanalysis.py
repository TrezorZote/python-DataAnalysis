#pip install mysql-connector-python  # For MySQL
#pip install sqlite3  # For SQLite
import mysql.connector

# Step 1: Establish the connection
connection = mysql.connector.connect(
    host='localhost:3306',
    user="root",
    password="myPassword",
    database="mydatabase"
)

# Step 2: Create a cursor object
# Create a Cursor to Execute SQL Queries: After establishing a connection, you can create a cursor to execute SQL queries
cursor = connection.cursor()

# Step 3 : Execute SQL queries to fetch data from the database.
cursor.execute("SELECT * customer")



# Step 4: Fetch all the rows
rows = cursor.fetchall()

# You can also fetch one row at a time using cursor.fetchone()
#  or a limited number of rows with cursor.fetchmany(size).

# Step 5: Perform Python operations on the data
for row in rows:
    print(f"Processing row: {row}")
    # Example of processing the data
    # You can perform calculations, filtering, transformations, etc.


cursor.execute("SELECT MAX(price) FROM product")

# Step 4: Fetch the result
max_value = cursor.fetchone()[0]

# Step 5: Print the maximum value
print(f"The maximum value in the column is: {max_value}")
# Step 6: Close the connection
cursor.close()
connection.close()
