
In Python object-oriented Programming (OOPs) is a programming paradigm
that uses objects and classes in programming. It aims to implement
real-world entities like inheritance, polymorphisms, encapsulation, etc.
in the programming. The main concept of object-oriented Programming
(OOPs) or oops concepts in Python is to bind the data and the functions
that work together as a single unit so that no other part of the code
can access this data.

**OOPs Concepts in Python**

1.  Class in Python

2.  Objects in Python

3.  Polymorphism in Python

4.  Encapsulation in Python

5.  Inheritance in Python

6.  Data Abstraction in Python



Python Class A class is a collection of objects. A class contains the
blueprints or the prototype from which the objects are being created. It
is a logical entity that contains some attributes and methods.




```python
#Simple Class in Python
class Dog:
    pass
```




**Python Objects** In object oriented programming Python, The object is
an entity that has a state and behavior associated with it. It may be
any real-world object like a mouse, keyboard, chair, table, pen, etc.
Integers, strings, floating-point numbers, even arrays, and
dictionaries, are all objects.


```python
obj = Dog()
```
This creates an instance for class Dog

**The Python **init** Method** 

The **init** method is similar to constructors in C++ and Java. It is
run as soon as an object of a class is instantiated. The method is
useful to do any initialization you want to do with your object.


```python
class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
```
In the above mentioned code, init method is used to initialize the name.

**Inheritance**

In Python object oriented Programming, Inheritance is the capability of
one class to derive or inherit the properties from another class. The
class that derives properties is called the derived class or child class
and the class from which the properties are being derived is called the
base class or parent class.

Types of Inheritances:

- Single Inheritance

- Multilevel Inheritance

- Multiple Inheritance

- Hierarchial Inheritance
 
```python
#Single Inheritance
# Parent class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        # Call the constructor of the parent class
        super().__init__(name, "Woof")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        # Call the constructor of the parent class
        super().__init__(name, "Meow")

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing methods of the parent class
dog.make_sound()
cat.make_sound()
```
The above code depicts the Single Inheritance, in case of single inheritance there's only a single base class and a derived class. Here, Dog and Cat are the derived classes with Animal as the parent class. They can access the methods of the base class or derive their own methods.



```python
#Multilevel Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

# Grandchild class inheriting from Dog
class GermanShepherd(Dog):
    def guard(self):
        print(f"{self.name} guards")

# Creating objects of the derived classes
german_shepherd = GermanShepherd("Rocky")

# Accessing methods from all levels of inheritance
german_shepherd.speak()  # Accessing method from the Animal class
german_shepherd.bark()   # Accessing method from the Dog class
german_shepherd.guard()  # Accessing method from the GermanShepherd class
```
Multilevel inheritance is a concept in object-oriented programming where a class inherits properties and behaviors from another class, which itself may inherit from another class. In other words, it involves a chain of inheritance where a subclass inherits from a superclass, and that subclass can then become a superclass for another subclass.Its similar to GrandFather ,Father and Son .In the above code,Animal class is the superclass, Dog is derived from Animal and Dog is the parent of GermanShepherd. GermenShepherd is the child class of Dog. GermenShepherd can access methods of both Animal and Dog.


```python
#Hierarchial Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks")

# Child class 1 inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

# Child class 2 inheriting from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows")

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing methods from the parent and child classes
dog.speak()  # Accessing method from the Animal class
dog.bark()   # Accessing method from the Dog class
cat.speak()  # Accessing method from the Animal class
cat.meow()   # Accessing method from the Cat class
```
Hierarchical inheritance is a type of inheritance in object-oriented programming where one class serves as a superclass for multiple subclasses. In this inheritance model, each subclass inherits properties and behaviors from the same superclass, creating a hierarchical tree-like structure.

```python
#Multiple Inheritance
# Parent class 1
class Herbivore:
    def eat_plants(self):
        print("Eating plants")

# Parent class 2
class Carnivore:
    def eat_meat(self):
        print("Eating meat")

# Child class inheriting from both Herbivore and Carnivore
class Omnivore(Herbivore, Carnivore):
    def eat(self):
        print("Eating everything")

# Creating an object of the Omnivore class
omnivore = Omnivore()

# Accessing methods from both parent classes
omnivore.eat_plants()  # Accessing method from Herbivore
omnivore.eat_meat()    # Accessing method from Carnivore
omnivore.eat()         # Accessing method from Omnivore
```
Multiple inheritance is a concept in object-oriented programming where a class can inherit properties and behaviors from more than one parent class. This means that a subclass can have multiple immediate parent classes, allowing it to inherit features from each of them. 

**Polymorphism** In object oriented Programming Python, Polymorphism
simply means having many forms

```python
class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
```
Poly stands for 'many' and morphism for 'forms'. In the above code, method flight() has many forms.

**Python Encapsulation**

In Python object oriented programming, Encapsulation is one of the
fundamental concepts in object-oriented programming (OOP). It describes
the idea of wrapping data and the methods that work on data within one
unit. This puts restrictions on accessing variables and methods directly
and can prevent the accidental modification of data. To prevent
accidental change, an object's variable can only be changed by an
object's method. Those types of variables are known as private
variables.


```python
class Car:
    def __init__(self, make, model, year):
        self._make = make  # Encapsulated attribute with single underscore
        self._model = model  # Encapsulated attribute with single underscore
        self._year = year  # Encapsulated attribute with single underscore
        self._odometer_reading = 0  # Encapsulated attribute with single underscore

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_odometer_reading(self):
        return self._odometer_reading

    def update_odometer(self, mileage):
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self._odometer_reading += miles

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2021)

# Accessing encapsulated attributes through methods
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Modifying encapsulated attribute through method
my_car.update_odometer(100)
print("Odometer Reading:", my_car.get_odometer_reading())

# Incrementing odometer reading
my_car.increment_odometer(50)
print("Odometer Reading after increment:", my_car.get_odometer_reading())
```


**Data Abstraction** It hides unnecessary code details from the user.
Also, when we do not want to give out sensitive parts of our code
implementation and this is where data abstraction came.

```python
from abc import ABC, abstractmethod

# Abstract class defining the interface for a Shape
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing the Shape interface for a Rectangle
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete class implementing the Shape interface for a Circle
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects of the derived classes
rectangle = Rectangle("Rectangle", 5, 4)
circle = Circle("Circle", 3)

# Accessing methods defined by the Shape interface
print(f"{rectangle.name}: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")
print(f"{circle.name}: Area = {circle.area()}, Perimeter = {circle.perimeter()}")
```
To implement Data Abstraction , we have to import abc . ABC stands for Abstract Base Class . All those classes which want to implement data abstraction have to inherit from ABC. 
@abstractmethod is a decorator provided by the abc module, which stands for "abstract method". It's used to define abstract methods within abstract base classes (ABCs). An abstract method is a method declared in a class, but it does not contain an implementation. Instead, it serves as a placeholder, and its concrete implementation must be provided by subclasses.
Abstract methods can be implemented by the derived classes.
