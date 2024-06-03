# Protocols in Python
Python can establish informal interfaces using protocols In order to improve code structure, reusability, and type checking. Protocols allow for progressive adoption and are more flexible than standard interfaces in other programming languages like JAVA, which are tight contracts that specify the methods and attributes a class must implement.

>Before going into depth of this topic let's understand another topic which is pre-requisite od this topic \#TypingModule

## Typing Module
This is a module in python which provides
1. Provides classes, functions, and type aliases.
2. Allows adding type annotations to our code.
3. Enhances code readability.
4. Helps in catching errors early.

### Type Hints in Python:
Type hints allow you to specify the expected data types of variables, function parameters, and return values. This can improve code readability and help with debugging.

Here is a simple function that adds two numbers:
```python
def add(a,b):
    return a + b
add(10,20)
```
>Output: 30

While this works fine, adding type hints makes the code more understandable and serves as documentation:

```python
def add(a:int, b:int)->int:
    return a + b
print(add(1,10))
```
>Output: 11    

In this version, `a` and `b` are expected to be integers, and the function is expected to return an integer. This makes the function's purpose and usage clearer.

#### let's see another example

The function given below takes an iterable (it can be any off list, tuple, dict, set, frozeset, String... etc) and print it's content in a single line along with it's type.

```python
from typing import Iterable
# type alias

def print_all(l: Iterable)->None:
    print(type(l),end=' ')
    for i in l:
        print(i,end=' ')
    print()

l = [1,2,3,4,5] # type: List[int]
s = {1,2,3,4,5} # type: Set[int]
t = (1,2,3,4,5) # type: Tuple[int]

for iter_obj in [l,s,t]:
    print_all(iter_obj)

```
Output:
> <class 'list'> 1 2 3 4 5   
> <class 'set'> 1 2 3 4 5   
> <class 'tuple'> 1 2 3 4 5  

and now lets try calling the function `print_all` using a non-iterable object `int` as argument.

```python
a = 10
print_all(a) # This will raise an error
```
Output:
>TypeError: 'int' object is not iterable

This error occurs because `a` is an `integer`, and the `integer` class does not have any methods or attributes that make it work like an iterable. In other words, the integer class does not conform to the `Iterable` protocol.

**Benefits of Type Hints**  
Using type hints helps in several ways:

1. **Error Detection**: Tools like mypy can catch type-related problems during development, decreasing runtime errors.
2. **Code Readability**: Type hints serve as documentation, making it easy to comprehend what data types are anticipated and returned.
3. **Improved Maintenance**: With unambiguous type expectations, maintaining and updating code becomes easier, especially in huge codebases.

Now that we have understood about type hints and typing module let's dive deep into protocols.

## Understanding Protocols

In Python, protocols define interfaces similar to Java interfaces. They let you specify methods and attributes that an object must implement without requiring inheritance from a base class. Protocols are part of the `typing` module and provide a way to enforce certain structures in your classes, enhancing type safety and code clarity.

### What is a Protocol?

A protocol specifies one or more method signatures that a class must implement to be considered as conforming to the protocol.  
 This concept is often referred to as "structural subtyping" or "duck typing," meaning that if an object implements the required methods and attributes, it can be treated as an instance of the protocol.

Let's write our own protocol:

```python
from typing import Protocol

# Define a Printable protocol
class Printable(Protocol):
    def print(self) -> None:
        """Print the object"""
        pass

# Book class implements the Printable protocol
class Book:
    def __init__(self, title: str):
        self.title = title
    
    def print(self) -> None:
        print(f"Book Title: {self.title}")

# print_object function takes a Printable object and calls its print method
def print_object(obj: Printable) -> None:
    obj.print()

book = Book("Python Programming")
print_object(book)
```
Output:  
> Book Title: Python Programming

In this example:

1. **Printable Protocol:** Defines an interface with a single method print.     
2. **Book Class:** Implements the Printable protocol by providing a print method.     
3. **print_object Function:** Accepts any object that conforms to the Printable protocol and calls its print method.     

we got our output because the class `Book` confirms to the protocols `printable`.
similarly When you pass an object to `print_object` that does not conform to the Printable protocol, an error will occur. This is because the object does not implement the required `print` method.   
Let's see an example:  
```python
class Team:
    def huddle(self) -> None:
        print("Team Huddle")

c = Team()
print_object(c)  # This will raise an error
```
Output:  
>AttributeError: 'Team' object has no attribute 'print'

In this case:  
- The `Team` class has a `huddle` method but does not have a `print` method.  
- When `print_object` tries to call the `print` method on a `Team` instance, it raises an `AttributeError`.  

> This is an important aspect of using protocols: they ensure that objects provide the necessary methods, leading to more predictable and reliable code.

**Ensuring Protocol Conformance**  
To avoid such errors, you need to ensure that any object passed to `print_object` implements the `Printable` protocol. Here's how you can modify the `Team` class to conform to the protocol:
```python
class Team:
    def __init__(self, name: str):
        self.name = name

    def huddle(self) -> None:
        print("Team Huddle")
    
    def print(self) -> None:
        print(f"Team Name: {self.name}")

c = Team("Dream Team")
print_object(c)
```
Output:
>Team Name: Dream Team

The `Team` class now implements the `print` method, conforming to the `Printable` protocol. and hence, no longer raises an error.

### Protocols and Inheritance:  
Protocols can also be used in combination with inheritance to create more complex interfaces.
we can do that by following these steps:
**Step 1 - Base protocol**: Define a base protocol that specifies a common set of methods and attributes.    
**Step 2 - Derived Protocols**: Create derives protocols that extends the base protocol with addition requirements  
**Step 3 - Polymorphism**: Objects can then conform to multiple protocols, allowing for Polymorphic behavior.

Let's see an example on this as well:

```python
from typing import Protocol

# Base Protocols
class Printable(Protocol):
    def print(self) -> None:
        """Print the object"""
        pass
    
# Base Protocols-2
class Serializable(Protocol):
    def serialize(self) -> str:
        pass

# Derived Protocol
class PrintableAndSerializable(Printable, Serializable):
    pass

# class with implementation of both Printable and Serializable
class Book_serialize:
    def __init__(self, title: str):
        self.title = title

    def print(self) -> None:
        print(f"Book Title: {self.title}")

    def serialize(self) -> None:
        print(f"serialize: {self.title}")

# function accepts the object which implements PrintableAndSerializable
def test(obj: PrintableAndSerializable):
  obj.print()
  obj.serialize()

book = Book_serialize("lean-in")
test(book)
```
Output:  
> Book Title: lean-in
serialize: lean-in

In this example:

**Printable Protocol:**  Specifies a `print` method.  
**Serializable Protocol:**   Specifies a `serialize` method.  
**PrintableAndSerializable Protocol:**  Combines both `Printable` and `Serializable`.  
**Book Class**:  Implements both `print` and `serialize` methods, conforming to `PrintableAndSerializable`.  
**test Function:**  Accepts any object that implements the `PrintableAndSerializable` protocol.

If you try to pass an object that does not conform to the `PrintableAndSerializable` protocol to the test function, it will raise an `error`. Let's see an example:

```python
class Team:
    def huddle(self) -> None:
        print("Team Huddle")

c = Team()
test(c) # This will raise an error
```
output:  
> AttributeError: 'Team' object has no attribute 'print'

In this case:  
The `Team` class has a `huddle` method but does not implement `print` or `serialize` methods.  
When test tries to call `print` and `serialize` on a `Team` instance, it raises an `AttributeError`.  

**In Conclusion:**  
>Python protocols offer a versatile and powerful means of defining interfaces, encouraging the decoupling of code, improving readability, and facilitating static type checking. They are particularly handy for scenarios involving file-like objects, bespoke containers, and any case where you wish to enforce certain behaviors without requiring inheritance from a specific base class. Ensuring that classes conform to protocols reduces runtime problems and makes your code more robust and maintainable.