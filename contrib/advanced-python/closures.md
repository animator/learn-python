# Closures
In order to have complete understanding of this topic in python, one needs to be crystal clear with the concept of functions and the different types of them which are namely First Class Functions and Nested Functions.

### First Class Functions
These are the normal functions used by the programmer in routine as they can be assigned to variables, passed as arguments and returned from other functions.
### Nested Functions
These are the functions defined within other functions and involve thorough usage of **Closures**. It is also referred as **Inner Functions** by some books. There are times when it is required to prevent a function or the data it has access to from being accessed from other parts of the code, and this is where Nested Functions come into play. Basically, its usage allows the encapsulation of that particular data/function within another function. This enables it to be virtually hidden from the global scope.

## Defining Closures
In nested functions, if the outer function basically ends up returning the inner function, in this case the concept of closures comes into play.

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. There are certain neccesary condtions required to create a closure in python :
1. The inner function must be defined inside the outer function.
2. The inner function must refer to a value defined in the outer function.
3. The inner function must return a value.

## Advantages of Closures
* Closures make it possible to pass data to inner functions without first passing them to outer functions
* Closures can be used to create private variables and functions
* They also make it possible to invoke the inner function from outside of the encapsulating outer function.
* It improves code readability and maintainability

## Examples implementing Closures
### Example 1 : Basic Implementation
```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(9))
print(times5(3))
```
#### Output:
```
27
15
```
The **multiplier function** is defined inside the **make_multiplier_of function**. It has access to the n variable from the outer scope, even after the make_multiplier_of function has returned. This is an example of a closure.

### Example 2 : Implementation with Decorators
```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()
```
#### Output:  
```
 Wrapper executed before display
 Display function executed
```
The code in the example defines a decorator function: ***decorator_function*** that takes a function as an argument and returns a new function **wrapper_function**. The **wrapper_function** function prints a message to the console before calling the original function which appends the name of the called function as specified in the code.

The **@decorator_function** syntax is used to apply the decorator_function decorator to the display function. This means that the display function is replaced with the result of calling **decorator_function(display)**.

When the **display()** function is called, the wrapper_function function is executed instead. The wrapper_function function prints a message to the console and then calls the original display function.
### Example 3 : Implementation with for loop
```python
def create_closures():
    closures = []
    for i in range(5):
        def closure(i=i):  # Capture current value of i by default argument
            return i
        closures.append(closure)
    return closures

my_closures = create_closures()
for closure in my_closures:
    print(closure())

```
#### Output:
```
0
1
2
3
4
```
The code in the example defines a function **create_closures** that creates a list of closure functions. Each closure function returns the current value of the loop variable i.

The closure function is defined inside the **create_closures function**. It has access to the i variable from the **outer scope**, even after the create_closures function has returned. This is an example of a closure.

The **i**=*i* argument in the closure function is used to capture the current value of *i* by default argument. This is necessary because the ****i** variable in the outer scope is a loop variable, and its value changes in each iteration of the loop. By capturing the current value of *i* in the default argument, we ensure that each closure function returns the correct value of **i**. This is responsible for the generation of output 0,1,2,3,4.


For more examples related to closures, [click here](https://dev.to/bshadmehr/understanding-closures-in-python-a-comprehensive-tutorial-11ld).

## Summary
Closures in Python provide a powerful mechanism for encapsulating state and behavior, enabling more flexible and modular code. Understanding and effectively using closures enables the creation of function factories, allows functions to have state, and facilitates functional programming techniques
