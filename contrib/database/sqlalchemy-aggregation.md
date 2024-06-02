# SQLAlchemy
SQLAlchemy is a powerful and flexible SQL toolkit and Object-Relational Mapping (ORM) library for Python. It is a versatile library that bridges the gap between Python applications and relational databases.

SQLAlchemy allows the user to write database-agnostic code that can work with a variety of relational databases such as SQLite, MySQL, PostgreSQL, Oracle, and Microsoft SQL Server. The ORM layer in SQLAlchemy allows developers to map Python classes to database tables. This means you can interact with your database using Python objects instead of writing raw SQL queries.

## Setting up the Environment
* Python and MySQL Server must be installed and configured.
* The library: **mysql-connector-python** and **sqlalchemy** must be installed.
 
```bash
pip install sqlalchemy mysql-connector-python
```

* If not installed, you can install them using the above command in terminal,

## Establishing Connection with Database

* Create a connection with the database using the following code snippet:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+mysqlconnector://root:12345@localhost/gssoc'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
```

* The connection string **DATABASE_URL** is passed as an argument to **create_engine** function which is used to create a connection to the database. This connection string contains the database credentials such as the database type, username, password, and database name.
* The **sessionmaker** function is used to create a session object which is used to interact with the database
* The **declarative_base** function is used to create a base class for all the database models. This base class is used to define the structure of the database tables.

## Creating Tables

* The following code snippet creates a table named **"products"** in the database:
```python
from sqlalchemy import Column, Integer, String, Float

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    price = Column(Float)
    quantity = Column(Integer)

Base.metadata.create_all(engine)
```

* The **Product class** inherits from **Base**, which is a base class for all the database models.
* The **Base.metadata.create_all(engine)** statement is used to create the table in the database. The engine object is a connection to the database that was created earlier.

## Inserting Data for Aggregation Functions

* The following code snippet inserts data into the **"products"** table:
```python
products = [
    Product(name='Laptop', category='Electronics', price=1000, quantity=50),
    Product(name='Smartphone', category='Electronics', price=700, quantity=150),
    Product(name='Tablet', category='Electronics', price=400, quantity=100),
    Product(name='Headphones', category='Accessories', price=100, quantity=200),
    Product(name='Charger', category='Accessories', price=20, quantity=300),
]

session.add_all(products)
session.commit()
```

* A list of **Product** objects is created. Each Product object represents a row in the **products table** in the database.
* The **add_all** method of the session object is used to add all the Product objects to the session. This method takes a **list of objects as an argument** and adds them to the session.
* The **commit** method of the session object is used to commit the changes made to the database.

## Aggregation Functions

SQLAlchemy provides functions that correspond to SQL aggregation functions and are available in the **sqlalchemy.func module**.

### COUNT

The **COUNT** function returns the number of rows in a result set. It can be demonstrated using the following code snippet:
```python
from sqlalchemy import func

total_products = session.query(func.count(Product.id)).scalar()
print(f'Total products: {total_products}')
```

### SUM

The **SUM** function returns the sum of all values in a column. It can be demonstrated using the following code snippet:
```python
total_price = session.query(func.sum(Product.price)).scalar()
print(f'Total price of all products: {total_price}')
```

### AVG 

The **AVG** function returns the average of all values in a column. It can be demonstrated by the following code snippet:
```python
average_price = session.query(func.avg(Product.price)).scalar()
print(f'Average price of products: {average_price}')
```

### MAX

The **MAX** function returns the maximum value in a column. It can be demonstrated using the following code snippet :
```python
max_price = session.query(func.max(Product.price)).scalar()
print(f'Maximum price of products: {max_price}')
```

### MIN

The **MIN** function returns the minimum value in a column. It can be demonstrated using the following code snippet:
```python
min_price = session.query(func.min(Product.price)).scalar()
print(f'Minimum price of products: {min_price}')
```

In general, the aggregation functions can be implemented by utilising the **session** object to execute the desired query on the table present in a database using the **query()** method. The **scalar()** method is called on the query object to execute the query and return a single value
