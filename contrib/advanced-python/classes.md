**Python Classes and Objects**

A class is a user-defined blueprint or prototype from which objects are created. Classes provides a means of bundling for data and functionality. Object is the instance of the class. A class can have any number of objects.

**Syntax :** Class Definition
  class ClassName:
     #statements

**Syntax:**  Object Definition 
  obj=ClassName()
The class creates a user-defined data structure, which holds its own data members and member functions which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

**Some points on Python class:**
->Classes are created by keyword class.
->Attributes are the variables that belong to a class.
->Attributes are always public and can be accessed using the dot (.) operator.
  Eg.: My class.attribute

**Example of Python Class and object**
Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation. 
**Example:** 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
**Output :**
   Hello my name is John.
**The __init__() Function**
All classes have a function called __init__(), which is always executed when the class is being initiated.We use the __init__() function to assign values to object properties.
**Example:**
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
  Here when we created the p1 object with values "john" and 36 that are assigned to name ,age of __init__ function.
**The self Parameter**
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
**Example:**
class Person:
  def __init__(self, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
         When we call a method of this object as myobject.method(arg1, arg2), this is automatically
converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about. 
**Concepts of Classes**
  Main principles of OOPs in Python are abstraction, encapsulation, inheritance, and polymorphism.
  ->Abstraction
  ->Encapsulation
  ->Inheritence
  ->Polymorphism
**Abstraction** 
    Data abstraction in Python is a programming concept that hides complex implementation details while
exposing only essential information and functionalities to users. In Python, we can achieve data abstraction by using abstract classes and abstract classes can be created using abc (abstract base class) module and abstractmethod of abc module.
**Abstract Method:** 
    In Python, abstract method feature is not a default feature. To create abstract method and abstract classes we have to import the “ABC” and “abstractmethod” classes from abc (Abstract Base Class) library. Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class. If we do not implement the abstract methods of base class in the child class then our code will give error. In the below code method_1 is a abstract method created using @abstractmethod decorator.
**Syntax:**
from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body 
**Implementation of Data Abstraction in Python**
In the below code, we have implemented data abstraction using abstract class and method. Firstly, we import the required modules or classes from abc library then we create a base class ‘Car’ that inherited from ‘ABC’ class that we have imported. Inside base class we create init function, abstract function and non-abstract functions. To declare abstract function printDetails we use “@abstractmethod” decorator. After that we create child class hatchback and suv. Since, these child classes inherited from abstract class so, we need to write the implementation of all abstract function declared in the base class. We write the implementation of abstract method in both child class. We create an instance of a child class and call the printDetails method. In this way we can achieve the data abstraction.  
**Example:**
  # Import required modules 
from abc import ABC, abstractmethod 

# Create Abstract base class 
class Car(ABC): 
def __init__(self, brand, model, year): 
	self.brand = brand 
	self.model = model 
	self.year = year 
	
# Create abstract method	 
@abstractmethod
def printDetails(self): 
	pass
	
# Create concrete method 
def accelerate(self): 
	print("speed up ...") 
	
def break_applied(self): 
	print("Car stop") 
	
# Create a child class 
class Hatchback(Car): 
	
def printDetails(self): 
	print("Brand:", self.brand); 
	print("Model:", self.model); 
	print("Year:", self.year); 
	
def Sunroof(self): 
	print("Not having this feature") 
	
# Create a child class 
class Suv(Car): 
	
def printDetails(self): 
	print("Brand:", self.brand); 
	print("Model:", self.model); 
	print("Year:", self.year); 
	
def Sunroof(self): 
	print("Available") 

	
car1 = Hatchback("Maruti", "Alto", "2022"); 

car1.printDetails() 
car1.accelerate() 
# OUtput
 Brand: Maruti
 Model: Alto
 Year: 2022
 speed up ...
**Encapsulation**
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is memberfunctions, variables, etc. The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.
**Encapsulation in Python**
     class=Methods + Variables
Encapsulating the methods and variables in class i.e that methods and variables are related and they are written in a class.Encapsulation reduces the code and one can create any number of objects and use them.

**Protected Members**
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
**Example:**
  
# Creating a base class 
class Base: 
	def __init__(self): 

		# Protected member 
		self._a = 2

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling protected member of base class: ", 
			self._a) 

		# Modify the protected variable: 
		self._a = 3
		print("Calling modified protected member outside class: ", 
			self._a) 


obj1 = Derived() 

obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 
# output
  Calling protected member of base class:  2
  Calling modified protected member outside class:  3
  Accessing protected member of obj1:  3
  Accessing protected member of obj2:  2 
   
**Private Members**
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”.
**Example:**
class Base: 
	def __init__(self): 
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling private member of base class: ") 
		print(self.__c) 


# Driver code 
obj1 = Base() 
print(obj1.a) 

# Uncommenting print(obj1.c) will 
# raise an AttributeError 

# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 


**Inheritence**
->Inheritance allows us to define a class that inherits all the methods and properties from another class.

->Parent class is the class being inherited from, also called base class.

->Child class is the class that inherits from another class, also called derived class.

**Creating of Parent Class**
 Any class can be a parent class, so the syntax is the same as creating any other class:
 **Example**
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
# output
 John Doe

**Creating of Child Class** 
 To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
**Example**
  class Student(Person):
     pass
**Super Function**
    Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
   **Example:** 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
# output:
 Mike Olsen
**Types of Inheritances**
  Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance in Python.
  They are:
  ->Single Inheritance
  ->Multiple Inheritance
  ->Multilevel Inheritance
  ->Hierarchical Inheritance
  ->Hybrid Inheritance
**Single Inheritance**
Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.
                            **Single Inheritance**
                                    class A
                                       |
                                       V
                                    class B 
**Example**  
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")
# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")
# Driver's code
object = Child()
object.func1()
object.func2()
# output
  This function is in parent class.
  This function is in child class.
**Multiple Inheritance**
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.
                        **Multiple Inheritance**
                          class A      Class B
                              \          /
                               \        /
                                 Class C
**Example** 
class Mother:
	mothername = ""
  def mother(self):
		print(self.mothername)
class Father:
	fathername = ""
  def father(self):
		print(self.fathername)
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
# output:
Father : RAM
Mother : SITA
**Multilevel Inheritance**
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.
                             **Multilevel Inheritance**
                                     class A
                                        |
                                        V
                                     class B
                                        |
                                        V
                                     class C     
**Example:**  
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
# output
Lal mani
Grandfather name : Lal mani
Father name : Rampal
Son name : Prince
**Polymorphism**
The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
**Example of python built in functions**

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))
# output
5
3
**Polymorphism with class methods:** 
 Polymorphism with class methods means different classes may have the methods with same method names.So here the polymorphism applies when the object is created for a particular class,the method related to that is invoked.
 **Example**
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()
# Output:
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
**Polymorphism with Inheritance**
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding. 
**Example:** 
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
# ouput:
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.

                           


	

       