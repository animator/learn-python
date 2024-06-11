## Introduction to Magic Methods

Magic methods in Python, also known as dunder (double underscore) methods, are special methods that begin and end with double underscores (__). 
They allow you to define the behavior of your objects in specific contexts, such as when they are created, represented as strings, compared, or used in arithmetic operations. These methods make classes more powerful and flexible.

## List of Common Magic Methods

__init__(self, ...): Constructor method, called when an instance is created.
__str__(self): Defines the string representation of an object.
__repr__(self): Defines the "official" string representation of an object.
__len__(self): Returns the length of the object.
__getitem__(self, key): Allows indexing using square brackets.
__setitem__(self, key, value): Assigns a value to the specified key.
__delitem__(self, key): Deletes the specified key-value pair.
__iter__(self): Returns an iterator for the object.
__next__(self): Returns the next item from an iterator.
__call__(self, ...): Makes an instance callable like a function.
__eq__(self, other): Defines behavior for the equality operator (==).
__add__(self, other): Defines behavior for the addition operator (+).


## Examples

__init__ and __str__

## code

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 30)
print(p)  # Output: Alice, 30 years old
__repr__

## code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

p = Person("Alice", 30)
print(repr(p))  # Output: Person(name='Alice', age=30)
__getitem__ and __setitem__

## code
class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

clist = CustomList([1, 2, 3])
print(clist[1]) 

# Output: 2

clist[1] = 42
print(clist[1])  
# Output: 42
__len__


# code

class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

clist = CustomList([1, 2, 3])
print(len(clist))  
# Output: 3

By implementing these magic methods, you can customize how your classes and objects interact with built-in Python functions and operators, making them more intuitive and versatile.