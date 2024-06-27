# Magic Methods

Magic methods, also known as dunder (double underscore) methods, are special methods in Python that start and end with double underscores (`__`). 
These methods allow you to define the behavior of objects for built-in operations and functions, enabling you to customize how your objects interact with the 
language's syntax and built-in features. Magic methods make your custom classes integrate seamlessly with Python’s built-in data types and operations.

**Commonly Used Magic Methods**

1. **Initialization and Representation**
   - `__init__(self, ...)`: Called when an instance of the class is created. Used for initializing the object's attributes.
   - `__repr__(self)`: Returns a string representation of the object, useful for debugging and logging.
   - `__str__(self)`: Returns a human-readable string representation of the object.

**Example** :

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __repr__(self):
           return f"Person({self.name}, {self.age})"

       def __str__(self):
           return f"{self.name}, {self.age} years old"

   p = Person("Alice", 30)
   print(repr(p))
   print(str(p))  
   ```

**Output** :
```python
Person("Alice",30)
Alice, 30 years old
```

2. **Arithmetic Operations**
   - `__add__(self, other)`: Defines behavior for the `+` operator.
   - `__sub__(self, other)`: Defines behavior for the `-` operator.
   - `__mul__(self, other)`: Defines behavior for the `*` operator.
   - `__truediv__(self, other)`: Defines behavior for the `/` operator.


**Example** :

   ```python
   class Vector:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __add__(self, other):
           return Vector(self.x + other.x, self.y + other.y)

       def __repr__(self):
           return f"Vector({self.x}, {self.y})"

   v1 = Vector(2, 3)
   v2 = Vector(1, 1)
   v3 = v1 + v2
   print(v3)  
   ```

**Output** :

```python
Vector(3, 4)
```

3. **Comparison Operations**
   - `__eq__(self, other)`: Defines behavior for the `==` operator.
   - `__lt__(self, other)`: Defines behavior for the `<` operator.
   - `__le__(self, other)`: Defines behavior for the `<=` operator.

**Example** :

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def __eq__(self, other):
           return self.age == other.age

       def __lt__(self, other):
           return self.age < other.age

   p1 = Person("Alice", 30)
   p2 = Person("Bob", 25)
   print(p1 == p2) 
   print(p1 < p2)  
   ```

   **Output** :
   
   ```python
   False
   False
   ```

5. **Container and Sequence Methods**

   - `__len__(self)`: Defines behavior for the `len()` function.
   - `__getitem__(self, key)`: Defines behavior for indexing (`self[key]`).
   - `__setitem__(self, key, value)`: Defines behavior for item assignment (`self[key] = value`).
   - `__delitem__(self, key)`: Defines behavior for item deletion (`del self[key]`).

**Example** :

   ```python
   class CustomList:
       def __init__(self, *args):
           self.items = list(args)

       def __len__(self):
           return len(self.items)

       def __getitem__(self, index):
           return self.items[index]

       def __setitem__(self, index, value):
           self.items[index] = value

       def __delitem__(self, index):
           del self.items[index]

       def __repr__(self):
           return f"CustomList({self.items})"

   cl = CustomList(1, 2, 3)
   print(len(cl))
   print(cl[1])    
   cl[1] = 5
   print(cl)
   del cl[1]
   print(cl)      
   ```

**Output** :
```python
3
2
CustomList([1, 5, 3])
CustomList([1, 3])
```

Magic methods provide powerful ways to customize the behavior of your objects and make them work seamlessly with Python's syntax and built-in functions. 
Use them judiciously to enhance the functionality and readability of your classes.
