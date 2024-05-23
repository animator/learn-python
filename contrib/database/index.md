# Interacting With Databases

In this section we are going to learn how to  interact with MySQL Databases through Python.     
<br>  
## Starting with MySQL Connector
In order to connect MySQL with Python we need to fulfill the following prerequisites:
+ Python  should be installed in the system
+ MySQL should be installed in the system

After you are done installing the above mentioned softwares, open command prompt & type the following code:
```
pip install mysql-connector-python
pip install pymysql

```
After you are done installing, restart the system and open your desired platform upon which you want to work on your python project.
<br>
Here I will be using **IDLE PYTHON 3.12**
<br>
## Steps for Creating Database Connectivity Applications
+ **STEP 1:** Start Python
+ **STEP 2:** Import Packages
+ **STEP 3:** Open a connection to Database
+ **STEP 4:** Create a cursor object
+ **STEP 5:** Execute a Query
+ **STEP 6:** Extract data
+ **STEP 7:** Clean up Environment
<br>
### Starting Python
> Open your Python editor in which you will be creating your project.
<br>
Here I will be using **IDLE PYTHON 3.12**

### Importing mysql.connector package
In order to connect MySQL and Python, we need to import the <mark>mysql.connector</mark> package.
We can do this by :
```
import mysql.connector
```
We can also assign this to an identifier for ease in future actions. For example :
```
import mysql.connector as mys
```
### Opening a connection to Database
We can connect to a database using **connect()** function which comes under **mysql.connector** package.
This function establishes a connection with the desired database and requires only four parametes i.e. *user, password, host-name & database*.
> Here specifying *database* is optional.

Here is an example showcasing the connection procedure with mycon taken as the connection variable :
```python
import mysql.connector as mys
      mycon=mys.connect(host="localhost",user="root",password="***",database="student")
```
To check whether we have succesfully connected to the database or not, we can use the function **is_connected()** with the connection variable. For instance, look below :
```python
if mycon.is_connected():
    print("Connected Succesfully!")
```
### Creating a Cursor Object
To get the full control of the data existing in a Database, cursor works as a vital instrument to process an retrieve data.
It facilitates row by row processing of records in a resultset.
<br>
We can create a cursor using the **cursor()** function.
```python
cursor = mycon.cursor()
```
### Execute a query
We can execute a query through python by using **execute()** function with cursor object.
```python
<cursorobject>.execute(<sql query string>)
```
For instance, take a look at the following example:
```python
cursor.excute("SELECT * FROM info")
```
### Extract data from Resultset
After you have performed certain operations in MySQL, you have to extract the data stored at the database at some point of time.
<br>
In order to do that, we use **fetch()** functions to fetch the desired data from our database.
<br>
1. **fetchall()**: It returns all the records retrieved before in tuple format.
<br>
Syntax :
```python
<data>=<cursor>.fetchall
```
2. **ftechone()**: It returns one record from a resultset at a time in list or tuple format.
Syntax :
```python
<data>=<cursor>.fetchone()
```
3. **fetchmany()**: The no. of records needed to fetch from resultset is passed through this function and it returns data in tuple format.
<br>
Syntax :
```python
<data>=<cursor>.fetchmany(<n>)
```
In order to know the number of rows of data thus retrieved from the resultset, we use another function called **rowcount**.
```python
<var>=<cursor>.rowcount 
```
### Clean up Environment
After you are done proceesing, it is important to clean up the environment to reduce buffering and unnecessary memory usage.
<br>
In order to do that, we close the connection thus established before.
```
<connectionobject>.close()
or
mycon.close() 
```