# Advanced Python
## Functions as First class objects
Functions in Python are so called first class objects, which means they can be treated as variables, viz. functions can be used as arguments or they can be returned using the return keyword. 

**Example**

```python
def func1():
  def func2():
    print("Printing from the inner function, func2")
  return func2

```
Assigning func1 to function_call object
```python
function_call=func1()
```
Calling the function
```python
>> function_call()
```
**Output**
```
Printing from the inner function, func2
```
Here we have seen the use of function as a first class object, func2 was returned as the result of the execution of the outer function, func1.

## *args
\* is an iterating operator used to unpack datatypes such as lists, tuples etc.
**For example**
```python
tuple1=(1,2,4,5,6,7)
print(tuple1)
print(*tuple1)
```
In the above we have defined a tuple called tuple1 with the items (1,2,4,5,6,7).
First we print normally and the output for that is:
```
(1, 2, 4, 5, 6, 7)

```
Then we print with the \* operator, where we will get the output as:
```
1 2 4 5 6 7
```

Here the \* operator has unpacked the tuple, tuple1.

Now that you have understood why \* is used, we can take a look at *args. *args is used in functions so that positional arguments are stored in the variable args. *args is just a naming convention, *anything can be used
*args makes python functions flexible to handle dynamic arguments.
```python
def test1(*args):
  print(args)
  print(f"The number of elements in args = {len(args)}")
a=list(range(0,10))
test1(*a)
```
In the above snippet, we are sending a list of numbers to the test function which returns the following output:
```
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
The number of elements in args = 10
```
If in the test1 we do not use \* in the argument

```python
def test1(*args):
  print(args)
  print(f"The number of elements in args = {len(args)}")
a=list(range(0,10))
test1(a)
```
we get the following result. This is a tuple containing a list.
```
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],)
The number of elements in args = 1
```
## **kwargs
**kwargs stands for keyword arguments. This is used for key and value pairs and similar to *args, this makes functions flexible enough to handle dynamic key value pairs in arguments.
```python
def test2(**kwargs):
  print(kwargs)
  print(f"The number of elements in kwargs = {len(kwargs)}")
test2(a=1,b=2,c=3,d=4,e=5)
```
The above snippet uses some key-value pairs and out test2 function gives the following output:
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
The number of elements in kwargs = 5
```
A dictionary with keys and values is obtained.

## Decorators (@decorators)
Now that we understand what first class object, *args, **kwargs is, we can move to decorators.
