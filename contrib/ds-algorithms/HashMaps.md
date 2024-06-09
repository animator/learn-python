# HashMaps (Dictionary)

### Definition
A HashMap, often called a dictionary in Python, is a data structure that stores key-value pairs. It allows for fast retrieval of values based on their associated keys. Under the hood, HashMaps use a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

## Properties
**Dictionaries are mutable**: That means that we can change, add or remove items after the dictionary has been created.

**Keys are immutable**: That means that keys are always data types that cannot be changed. In other words, dictionaries will only allow data types that are hashable, like strings, numbers, and tuples. On the contrary, keys can never be a mutable data type, such as a list.

**Keys are unique**: Keys are unique within a dictionary and can not be duplicated inside a dictionary. If it is used more than once, subsequent entries will overwrite the previous value.

## Operations
**Insertion**: Add a key-value pair to the HashMap.

**Deletion**: Remove a key and its associated value.

**Lookup**: Retrieve the value associated with a key.

**Update**: Change the value associated with a key.


## Creating a Dictionary

```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with initial values
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## Adding and Updating Elements

```python
# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating an existing key-value pair
my_dict["age"] = 31
```

## Accessing Values

```python
# Accessing a value by key
name = my_dict["name"]
print(name)  # Output: Alice

# Using the get method to avoid KeyError if the key does not exist
email = my_dict.get("email", "Not Provided")
print(email)  # Output: alice@example.com
```

## Deleting Elements

```python
# Removing a key-value pair using del
del my_dict["city"]

# Using pop method to remove and return the value
age = my_dict.pop("age")
print(age)  # Output: 31
```

## Iterating Over a Dictionary

```python
# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

## Checking for Existence of Keys

``` python
# Using the in keyword
if "name" in my_dict:
    print("Name is present in the dictionary")
```

## Example Code:

```python
# Initialize a dictionary with some values
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Carol": "555-8765"
}

# Add a new contact
phone_book["David"] = "555-4321"

# Update Bob's phone number
phone_book["Bob"] = "555-9999"

# Retrieve Carol's phone number
carol_number = phone_book.get("Carol")
print(f"Carol's number is {carol_number}")

# Remove Alice from the phone book
del phone_book["Alice"]

# Check if David is in the phone book
if "David" in phone_book:
    print("David's contact is in the phone book")

# Print all contacts
for name, number in phone_book.items():
    print(f"{name}: {number}")
```

### Output:
```
Carol's number is 555-8765
David's contact is in the phone book
Bob: 555-9999
Carol: 555-8765
David: 555-4321
```

## Applications

**Databases**: Indexing data for quick retrieval. 

**Caching**: Storing frequently accessed data to speed up applications.

**Configuration Settings**: Managing application settings where settings names are keys and their values are the settings' values.

**Symbol Tables in Compilers**: Mapping variable names to information about their data types and scopes.


## Real-Life Examples

**Contact List**: Storing contacts in a phone where each contact name is a key, and the phone number is the value.

**Library Catalog**: Managing books in a library with book titles as keys and their details (author, publication year, etc.) as values.

**User Information**: Storing user profiles in a web application with usernames as keys and user details as values.
