# Reduce Function

## Definition:
The reduce() function is part of the functools module and is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an iterable (e.g., a list, tuple, or string). It reduces the iterable to a single value by successively combining elements.

**Syntax**:
```python
from functools import reduce
reduce(function, iterable, initial=None)
```
**Parameters**:<br>
*function* : The binary function to apply. It takes two arguments and returns a single value.<br>
*iterable* : The sequence of elements to process.<br>
*initial (optional)*: An initial value. If provided, the function is applied to the initial value and the first element of the iterable. Otherwise, the first two elements are used as the initial values.

## Working:
- Intially , first two elements of iterable are picked and the result is obtained.
- Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
- This process continues till no more elements are left in the container.
- The final returned result is returned and printed on console.

## Examples:

**Example 1:**
```python
numbers = [1, 2, 3, 4, 10]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 20
```
**Example 2:**
```python
numbers = [11, 7, 8, 20, 1]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 20
```
**Example 3:**
```python
# Importing reduce function from functools  
from functools import reduce  
  
# Creating a list  
my_list = [10, 20, 30, 40, 50]  
  
# Calculating the product of the numbers in my_list  
# using reduce and lambda functions together  
product = reduce(lambda x, y: x * y, my_list)  
  
# Printing output  
print(f"Product = {product}") # Output : Product = 12000000
```

## Difference Between reduce() and accumulate():
- **Behavior:**
    - reduce() stores intermediate results and only returns the final summation value.
    - accumulate() returns an iterator containing all intermediate results. The last value in the iterator is the summation value of the list.

- **Use Cases:**
    - Use reduce() when you need a single result (e.g., total sum, product) from the iterable.
    - Use accumulate() when you want to access intermediate results during the reduction process.

- **Initial Value:**
    - reduce() allows an optional initial value.
    - accumulate() also accepts an optional initial value since Python 3.8.

- **Order of Arguments:**
    - reduce() takes the function first, followed by the iterable.
    - accumulate() takes the iterable first, followed by the function.

## Conclusion:
Python's Reduce function enables us to apply reduction operations to iterables using lambda and callable functions. A 
function called reduce() reduces the elements of an iterable to a single cumulative value. The reduce function in 
Python solves various straightforward issues, including adding and multiplying iterables of numbers.