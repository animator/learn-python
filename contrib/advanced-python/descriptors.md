### Descriptors in Python
  
Descriptors are a powerful feature in Python that allow you to customize the behavior of attribute access. They enable you to define how an attribute is accessed, set, and deleted. Descriptors are used to manage the attributes of different classes using methods in a single class.

### What is a Descriptor?

A descriptor is any object that implements at least one of the following methods: `__get__()`, `__set__()`, and `__delete__()`. These methods are used to define the behavior of attribute access.

- `__get__(self, instance, owner)`: Defines behavior for accessing the attribute.
- `__set__(self, instance, value)`: Defines behavior for setting the attribute.
- `__delete__(self, instance)`: Defines behavior for deleting the attribute.

### Creating a Descriptor
  
Let's create a basic descriptor that manages a simple attribute.

```python
  class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Getting: {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Setting: {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting: {self.name}")
        del instance.__dict__[self.name]

class MyClass:
    attribute = Descriptor('attribute')

obj = MyClass()
obj.attribute = 42  # Setting: attribute to 42
print(obj.attribute)  # Getting: attribute \n 42
del obj.attribute  # Deleting: attribute
```

### How Descriptors Work

When you access an attribute on an instance of a class, Python will check if the attribute is a descriptor by looking for __get__, __set__, or __delete__ methods. If any of these methods are present, the corresponding descriptor method is called.

### Types of Descriptors

  - **Data Descriptors**: Implement both `__get__` and `__set__` (or `__delete__`). They have priority over instance dictionaries.
  
  - **Non-Data Descriptors**: Implement only `__get__`. They are used for methods and attributes where setting is not required.

### Data Descriptor Example

```python
class DataDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass:
    attribute = DataDescriptor('attribute')

obj = MyClass()
obj.attribute = 10
print(obj.attribute)  # Output: 10
```
### Non-Data Descriptor Example
```python
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "Non-Data Descriptor"

class MyClass:
    attribute = NonDataDescriptor()

obj = MyClass()
print(obj.attribute)  # Output: Non-Data Descriptor
obj.attribute = 10
print(obj.attribute)  # Output: 10 (Overridden by instance dictionary)
```

### Practical Uses of Descriptors

  - **Type of Checking and Validation:**
    
    Type checking and validation ensure that your program's data is of the correct type and meets specific rules. This prevents bugs and makes your code more reliable.

    ```python
    class Integer:
        def __init__(self, name):
            self.name = name
    
        def __get__(self, instance, owner):
            return instance.__dict__[self.name]
    
        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise ValueError(f"{self.name} must be an integer")
            instance.__dict__[self.name] = value
    
    class Point:
        x = Integer('x')
        y = Integer('y')
    
    p = Point()
    p.x = 5
    p.y = 'a'  # Raises ValueError: y must be an integer
    ```
    
  - **Lazy Attributes:**

    These are attributes that are only calculated when they are first needed. This saves resources by delaying the computation until necessary.

    ```python
    class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value

    class MyClass:
        @LazyProperty
        def expensive_operation(self):
            print("Computing...")
            return 42
    
    obj = MyClass()
    print(obj.expensive_operation)  # Computing... \n 42
    print(obj.expensive_operation)  # 42 (No recomputation)
    ```
  - **Computed Properties:**

    These are properties that are calculated each time they are accessed, based on other data in the object. They ensure the value is always current.
    ```python
    class Celsius:
        def __init__(self, temperature=0):
            self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

    c = Celsius()
    c.temperature = 37
    print(c.temperature)  # Output: 37
```
