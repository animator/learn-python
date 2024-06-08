# Introduction to MySQL Queries
MySQL is a widely-used open-source relational database management system (RDBMS) that utilizes SQL (Structured Query Language) for managing and querying data. In Python, the **mysql-connector-python** library allows you to connect to MySQL databases and execute SQL queries, providing a way to interact with the database from within a Python program.

## Prerequisites
* Python and MySQL Server must be installed and configured.
* The library: **mysql-connector-python** must be installed.

## Establishing connection with server
To establish a connection with the MySQL server, you need to import the **mysql.connector** module and create a connection object using the **connect()** function by providing the prompt server details as mentioned.

```python
import mysql.connector
 
con = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="12345"
)

print((con.is_connected()))
```
Having established a connection with the server, you get the following output :
``` 
True 
```
## Creating a Database [CREATE]
To create a database, you need to execute the **CREATE DATABASE** query. The following code snippet demonstrates how to create a database named **GSSOC**.
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)

# Create a cursor object
cursor = conn.cursor()

# Execute the query to show databases
cursor.execute("SHOW DATABASES")

# Fetch and print the databases
databases = cursor.fetchall()
for database in databases:
    print(database[0])

# Execute the query to create database GSSOC
cursor.execute("CREATE DATABASE GSSOC")

print("\nAfter creation of the database\n")

# Execute the query to show databases
cursor.execute("SHOW DATABASES")
# Fetch and print the databases
databases = cursor.fetchall()
for database in databases:
    print(database[0])

cursor.close()
conn.close()
```
You can observe in the output below, after execution of the query a new database named **GSSOC** has been created.
#### Output:
```
information_schema
mysql
performance_schema
sakila
sys
world

After creation of the database

gssoc
information_schema
mysql
performance_schema
sakila
sys
world
```
## Creating a Table in the Database [CREATE]
Now, we will create a table in the database. We will create a table named **example_table** in the database **GSSOC**. We will execute **CREATE TABLE** query and provide the fields for the table as  mentioned in the code below:
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()

# Execute the query to show tables
cursor.execute("USE GSSOC")
cursor.execute("SHOW TABLES")

# Fetch and print the tables
tables = cursor.fetchall()
print("Before creation of table\n")
for table in tables:
    print(table[0])

create_table_query = """
CREATE TABLE example_table (
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255)
)
"""
# Execute the query
cursor.execute(create_table_query)

# Commit the changes
conn.commit()
    
print("\nAfter creation of Table\n")
# Execute the query to show tables in GSSOC
cursor.execute("SHOW TABLES")

# Fetch and print the tables
tables = cursor.fetchall()
for table in tables:
    print(table[0])

cursor.close()
conn.close()
```
#### Output:
```
Before creation of table


After creation of Table

example_table
```
## Inserting Data [INSERT]
To insert data in an existing table, the **INSERT INTO** query is used, followed by the name of the table in which the data needs to be inserted. The following code demonstrates the insertion of multiple records in the table by **executemany()**.
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()
cursor.execute("USE GSSOC")
# SQL query to insert data
insert_data_query = """
INSERT INTO example_table (name, age, email)
VALUES (%s, %s, %s)
"""

# Data to be inserted
data_to_insert = [
    ("John Doe", 28, "john.doe@example.com"),
    ("Jane Smith", 34, "jane.smith@example.com"),
    ("Sam Brown", 22, "sam.brown@example.com")
]

# Execute the query for each data entry
cursor.executemany(insert_data_query, data_to_insert)

conn.commit()
cursor.close()
conn.close()
```
## Displaying Data [SELECT]
To display the data from a table, the **SELECT** query is used. The following code demonstrates the display of data from the table.
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()
cursor.execute("USE GSSOC")

# SQL query to display data
display_data_query = "SELECT * FROM example_table"

# Execute the query for each data entry
cursor.execute(display_data_query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the column names
column_names = [desc[0] for desc in cursor.description]
print(column_names)

# Print the rows
for row in rows:
    print(row)

cursor.close()
conn.close()
```
#### Output :
```
['name', 'age', 'email']
('John Doe', 28, 'john.doe@example.com')
('Jane Smith', 34, 'jane.smith@example.com')
('Sam Brown', 22, 'sam.brown@example.com')
```
## Updating Data [UPDATE]
To update data in the table, **UPDATE** query is used. In the following code, we will be updating the email and age of the record where the name is John Doe.
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()
cursor.execute("USE GSSOC")

# SQL query to display data
display_data_query = "SELECT * FROM example_table"

# SQL Query to update data of John Doe
update_data_query = """
UPDATE example_table
SET age = %s, email = %s
WHERE name = %s
"""

# Data to be updated
data_to_update = (30, "new.email@example.com", "John Doe")

# Execute the query
cursor.execute(update_data_query, data_to_update)

# Commit the changes
conn.commit()

# Execute the query for each data entry
cursor.execute(display_data_query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the column names
column_names = [desc[0] for desc in cursor.description]
print(column_names)

# Print the rows
for row in rows:
    print(row)

cursor.close()
conn.close()
```
#### Output:
```
['name', 'age', 'email']
('John Doe', 30, 'new.email@example.com')
('Jane Smith', 34, 'jane.smith@example.com')
('Sam Brown', 22, 'sam.brown@example.com')
```

## Deleting Data [DELETE]
In this segment, we will Delete the record named "John Doe" using the **DELETE** and **WHERE** statements in the query. The following code explains the same and the observe the change in output.
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()
cursor.execute("USE GSSOC")

# SQL query to display data
display_data_query = "SELECT * FROM example_table"

# SQL query to delete data
delete_data_query = "DELETE FROM example_table WHERE name = %s"

# Data to be deleted
data_to_delete = ("John Doe",)

# Execute the query
cursor.execute(delete_data_query, data_to_delete)

# Commit the changes
conn.commit()

# Execute the query for each data entry
cursor.execute(display_data_query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the column names
column_names = [desc[0] for desc in cursor.description]
print(column_names)

# Print the rows
for row in rows:
    print(row)

cursor.close()
conn.close()
```
#### Output:
```
['name', 'age', 'email']
('Jane Smith', 34, 'jane.smith@example.com')
('Sam Brown', 22, 'sam.brown@example.com')
```
## Deleting the Table/Database [DROP]
For deleting a table, you can use the **DROP** query in the following manner: 
```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)
# Create a cursor object
cursor = conn.cursor()
cursor.execute("USE GSSOC")

# SQL query to delete the table
delete_table_query = "DROP TABLE IF EXISTS example_table"

# Execute the query
cursor.execute(delete_table_query)

# Verify the table deletion
cursor.execute("SHOW TABLES LIKE 'example_table'")
result = cursor.fetchone()

cursor.close()
conn.close()

if result:
    print("Table deletion failed.")
else:
    print("Table successfully deleted.")    
```
#### Output:
```
Table successfully deleted.
```
Similarly, you can delete the database also by using the **DROP** and accordingly changing the query to be executed.




