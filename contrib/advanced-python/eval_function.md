# Understanding the `eval` Function in Python
## Introduction

The `eval` function in Python allows you to execute a string-based Python expression dynamically. 

## Syntax
```python 
eval(expression, globals=None, locals=None)
```

### Parameters:

* expression: String is parsed and evaluated as a Python expression
* globals [optional]: Dictionary to specify the available global methods and variables.
* locals [optional]: Another dictionary to specify the available local methods and variables.

## Examples
Example 1:
```python
result = eval('2 + 3 * 4')
print(result)  # Output: 14
```
Example 2:

```python
x = 10
expression = 'x * 2'
result = eval(expression, {'x': x})
print(result)  # Output: 20
```
Example 3:
```python
x = 10
def multiply(a, b):
    return a * b
expression = 'multiply(x, 5) + 2'
result = eval(expression)
print(result)  # Output: 52
```
Example 4:
```python
expression = input("Enter a Python expression: ")
result = eval(expression)
print("Result:", result)
#input= "3+2"
#Output: Result: 5
example 5:
```pyhton
import numpy as np
a=np.random.randint(1,9)
b=np.random.randint(1,9)
operations=["*","-","+"]
op=np.random.choice(operations)

expression=str(a)+op+str(b)
correct_answer=eval(expression)
given_answer=int(input(str(a)+" "+op+" "+str(b)+" = "))

if given_answer==correct_answer:
    print("Correct")
else:
    print("Incorrect")
    print("correct answer is :" ,correct_answer)

#2 * 1 = 8
#Incorrect
#correct answer is : 2
#or
#3 * 2 = 6
#Correct
```
