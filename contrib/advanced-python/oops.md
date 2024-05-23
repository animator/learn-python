# **Python OOPs Concepts**

Object-Oriented Programming (OOP) is a key idea in Python. It helps developers create organized, easy-to-understand, and flexible programs. By using classes, objects, inheritance, encapsulation, polymorphism, and abstraction, programmers can make their code more structured and powerful. This means they can build programs that are easier to manage and can grow without becoming messy or hard to understand.

## **What is Object-Oriented Programming?**
Object-Oriented Programming (OOP) in Python is a way of writing code that revolves around 'objects' and 'classes.' These objects represent real-world things, like a car or a person, and classes are like blueprints for creating those objects. OOP helps us organize our code better by grouping related data and functions together into these objects. It also allows us to use fancy concepts like inheritance (where one class can inherit features from another), polymorphism (which allows different objects to be treated in a similar way), and encapsulation (which keeps data safe from being accessed by other parts of the code).

## **OOPs Concepts in Python**
- Class in Python
- Objects in Python
- Polymorphism in Python
- Encapsulation in Python
- Inheritance in Python
- Data Abstraction in Python

## **Class in Python**
Class is a user defined prototype(datatype) from which objects can be creatred. It provides a means of binding data and functionality together.
New class means a new type of object that is defined by the user. Each class can have attributes attached to it for maintaining it's state.

### Some points on Python class:
- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: Createdclass.Createdattribute

### Class Definition Syntax:

'''python
class ClassName:
   Statement-1
   .
   .
   .
   Statement-N 

#### Example of an empty class:
'''
class DEMO:
  pass

## **Python Objects :**
Objects are instances of a class. They are created using the keyword class. Objects have attributes and methods. Attributes are the variables that belong to a class. CLass is like a blueprint while an instance is like a copy of class with actual values.

### An object consists of:
- **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
- **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
- **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

- Naming of class follows PascalCase.

### Creating Object
''' 
obj=DEMO()

## **The Python self**  
1. Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
2. If we have a method that takes no arguments, then we still have to have one argument.
3. This is similar to this pointer in C++ and this reference in Java.

When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

## **The Python __init__ Method**
The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. Now let us define a class and create some objects using the self and __init__ method.

'''python
class Dog:

    
    attr1 = "mammal"

    
    def __init__(self, name):
        self.name = name

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

### Output
Rodger is a mammal
Tommy is also a mammal
My name is Rodger
My name is Tommy

### **Creating Classes and objects with methods**
Here, The Dog class is defined with two attributes:

- attr1 is a class attribute set to the value “mammal“. Class attributes are shared by all instances of the class.
- __init__ is a special method (constructor) that initializes an instance of the Dog class. It takes two parameters: self (referring to the instance being created) and name (representing the name of the dog). The name parameter is used to assign a name attribute to each instance of Dog.
The speak method is defined within the Dog class. This method prints a string that includes the name of the dog instance.
The driver code starts by creating two instances of the Dog class: Rodger and Tommy. The __init__ method is called for each instance to initialize their name attributes with the provided names. The speak method is called in both instances (Rodger.speak() and Tommy.speak()), causing each dog to print a statement with its name.

'''python
class Dog:

    attr1 = "mammal"

    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()

**Output**
My name is Rodger
My name is Tommy

## **Python Inheritance**
In Python object oriented Programming, Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class. The benefits of inheritance are:

- It represents real-world relationships well.
- It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

### Types of Inheritance
- **Single Inheritance:** Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
- **Multilevel Inheritance:** Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
- **Hierarchical Inheritance:** Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
- **Multiple Inheritance:** Multiple-level inheritance enables one derived class to inherit properties from more than one base class.

Above, we have created two classes i.e. Person (parent class) and Employee (Child Class). The Employee class inherits from the Person class. We can use the methods of the person class through the employee class as seen in the display function in the above code. A child class can also modify the behavior of the parent class as seen through the details() method.

'''python
# parent class
class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
    
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")

a.display()
a.details()

**Output**
Rahul
886012
My name is Rahul
IdNumber: 886012
Post: Intern

Here is another code for better understanding
'''python
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()


## **Python Polymorphism**
In object oriented Programming Python, Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

### **Polymorphism in Python***
This code demonstrates the concept of Python oops inheritance and method overriding in Python classes. It shows how subclasses can override methods defined in their parent class to provide specific behavior while still inheriting other methods from the parent class.

'''python
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

**Output**
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.

## **Python Encapsulation**
Encapsulation is the process of binding data and code together into a single unit.In Python, encapsulation is a fundamental concept in object-oriented programming (OOP). It involves bundling data and the methods that operate on that data into a single unit, typically a class. Encapsulation restricts direct access to some of an object's components, which can help prevent accidental modifications and promote modularity.

By using encapsulation, you can control how the data within an object is accessed and modified. This is often achieved by making variables private, meaning they can only be changed through the object's methods. These private variables are not directly accessible from outside the class, thereby safeguarding the integrity of the data.

A class in Python is an example of encapsulation, as it encapsulates data (attributes) and functions (methods) that operate on that data within a single unit.

Here is an example to illustrate encapsulation:
'''python
class Car:
    def __init__(self, make, model, year):
        self.__make = make 
        self.__model = model 
        self.__year = year 

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def display_info(self):
        return f"{self.__year} {self.__make} {self.__model}"

my_car = Car("Toyota", "Corolla", 2020)

print(my_car.display_info())  
my_car.set_year(2021)
print(my_car.get_year()) 

## **Data Abstraction **
Data abstraction in Python hides unnecessary details from the user, focusing only on the essential features. This is especially useful when we want to shield sensitive parts of our code implementation. Data abstraction can be achieved through the use of abstract classes.

An abstract class is a class that cannot be instantiated and typically includes one or more abstract methods. These methods are declared, but contain no implementation. Subclasses of the abstract class must provide implementations for all abstract methods.

Here is an example to illustrate data abstraction using abstract classes in Python:
'''python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.make_sound())  
print(cat.make_sound())  

