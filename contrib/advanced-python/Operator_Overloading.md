                                     #Operator Overloading in Python

   >>Introduction
    Operator overloading in Python allows you to define custom behavior for operators (such as +, -, *, and /) for your own classes. This enables you to create more intuitive and readable code when working with objects.

   >>What is Operator Overloading?
    Operator overloading is a feature in Python that allows the same operator to have different meanings based on the context, particularly the types of the operands. For example, the + operator can add two numbers, concatenate two strings, or merge two lists.

    >>Special Methods
    To overload an operator, you need to define special methods in your class. These methods are also known as magic methods or dunder methods (because they start and end with double underscores, __).

 Implementing Operator Overloading
   Here is a basic example of how to implement operator overloading in a Python class.

  **Example: Overloading the + Operator

 class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

 p1 = Point(1, 2)
 p2 = Point(3, 4)
 p3 = p1 + p2

 print(p3)  # Output: Point(4, 6)

   **Examples of Operator Overloading
   >>Arithmetic Operators
 __add__(self, other): +
 __sub__(self, other): -
 __mul__(self, other): *
 __truediv__(self, other): /
 __floordiv__(self, other): //
 __mod__(self, other): %
 __pow__(self, other): **
  **Example: Overloading Arithmetic Operators 
 class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

 v1 = Vector(2, 3)
 v2 = Vector(4, 5)
 v3 = v1 + v2
 v4 = v1 - v2
 v5 = v1 * 3

 print(v3)  # Output: Vector(6, 8)
 print(v4)  # Output: Vector(-2, -2)
 print(v5)  # Output: Vector(6, 9)

 >>Comparison Operators
 __eq__(self, other): ==
 __ne__(self, other): !=
 __lt__(self, other): <
 __le__(self, other): <=
 __gt__(self, other): >
 __ge__(self, other): >=
  ** Example: Overloading Comparison Operators

 class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self):
        return f'Book({self.title}, {self.price})'

 b1 = Book('Book A', 29.99)
 b2 = Book('Book B', 39.99)
 b3 = Book('Book C', 29.99)

 print(b1 == b2)  # Output: False
 print(b1 == b3)  # Output: True
 print(b1 < b2)   # Output: True

  >>Other Operators
 
 __str__(self): str()
 __repr__(self): repr()
 __len__(self): len()
 __getitem__(self, key): indexing
  
  ** Example: Overloading __str__ and __repr__

 class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} years old'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

 person = Person('Alice', 30)
 print(str(person))  # Output: Alice, 30 years old
 print(repr(person)) # Output: Person(name=Alice, age=30)

   >>Common Use Cases
     Mathematical Objects: Vectors, complex numbers, matrices, etc.
     Data Containers: Custom collections that need element-wise operations.
     Domain-Specific Objects: Objects that benefit from intuitive operations, like dates, times, and financial figures. 
  
  >>Conclusion
    Operator overloading in Python allows you to create intuitive and readable code by defining custom behavior for operators in your own classes. By implementing special methods, you can enable your objects to interact using standard operators.
