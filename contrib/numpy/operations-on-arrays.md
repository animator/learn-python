# Operations on Arrays

## NumPy Arithmetic Operations

<br>

NumPy offers a broad array of operations for arrays, including arithmetic functions.

The arithmetic operations in NumPy are popular for their simplicity and efficiency in handling array calculations.

Here is a list of different arithmetic operations along with their corresponding operators:

| Element-wise Operation | Operator |
|------------------------|:--------:|
| Addition               | +        |
| Subtraction            | -        |
| Multiplication         | *        |
| Division               | /        |
| Exponentiation         | **       |
| Modulus                | %        |

#

### Code Initialization

```python
import numpy as np

array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
```

### Addition
```python
# Utilizing the + operator
result_1 = array_1 + array_2
print("Utilizing the + operator:", result_1) 
```

Output:
```
Utilizing the + operator: [10 13 16 19]
```

### Subtraction
```python
# Utilizing the - operator
result_1 = array_1 - array_2
print("Utilizing the - operator:", result_1) 
```

Output:
```
Utilizing the - operator: [8 7 6 5]
```

### Multiplication
```python
# Utilizing the * operator
result_1 = array_1 * array_2
print("Utilizing the * operator:", result_1) 
```

Output:
```
Utilizing the * operator: [9 30 55 84]
```

### Division
```python
# Utilizing the / operator
result_1 = array_1 / array_2
print("Utilizing the / operator:", result_1) 
```

Output:
```
Utilizing the / operator: [9. 3.33333333 2.2 1.71428571]
```

### Exponentiation
```python
# Utilizing the ** operator
result_1 = array_1 ** array_2
print("Utilizing the ** operator:", result_1) 
```

Output:
```
Utilizing the ** operator: [9 1000 161051 35831808]
```

### Modulus
```python
# Utilizing the % operator
result_1 = array_1 % array_2
print("Utilizing the % operator:", result_1) 
```

Output:
```
Utilizing the ** operator: [0 1 1 5]
```

<br>

## NumPy Comparision Operations

<br>

NumPy provides various comparison operators that can compare elements across multiple NumPy arrays.

| Operator | Description                                                                                                                   |
|:--------:|-------------------------------------------------------------------------------------------------------------------------------|
| <        | Evaluates to True if the element in the first array is less than the corresponding element in the second array                |
| <=       | Evaluates to True if the element in the first array is less than or equal to the corresponding element in the second array    |
| >        | Evaluates to True if the element in the first array is greater than the corresponding element in the second array             |
| >=       | Evaluates to True if the element in the first array is greater than or equal to the corresponding element in the second array |
| ==       | Evaluates to True if the element in the first array is equal to the corresponding element in the second array                 |
| !=       | Evaluates to True if the element in the first array is not equal to the corresponding element in the second array             |

#

### Code Initialization

```python
import numpy as np

array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
```

#### less than operator
```python
result_1 = array_1 < array_2
print("array_1 < array_2:",result_1)
```
Output:
```
array_1 < array_2 : [True False False]
```    

#### less than or equal to operator
```python
result_1 = array_1 <= array_2
print("array_1 <= array_2:",result_1)
```
Output:
```
array_1 <= array_2: [True True False]
``` 

#### greater than operator
```python
result_2 = array_1 > array_2
print("array_1 > array_2:",result_2)    
```
Output:
```
array_1 > array_2 : [False False True]
```

#### greater than or equal to operator
```python
result_2 = array_1 >= array_2
print("array_1 >= array_2:",result_2)   
```
Output:
```
array_1 >= array_2: [False True True]
```

#### equal to operator
```python
result_3 = array_1 == array_2
print("array_1 == array_2:",result_3)
```
Output:
```
array_1 == array_2: [False True False]
```

#### not equal to operator  
```python
result_3 = array_1 != array_2
print("array_1 != array_2:",result_3)    
```
Output:
```
array_1 != array_2: [True False True]
```

<br>

## NumPy Logical Operations

<br>

Logical operators perform Boolean algebra. A branch of algebra that deals with True and False statements.

| Operator      | Description                                         |
|---------------|-----------------------------------------------------|
| logical_and   | Evaluates the element-wise truth value of x1 AND x2 |
| logical_or    | Evaluates the element-wise truth value of x1 OR x2  |
| logical_not   | Evaluates the element-wise truth value of NOT x     |


It illustrates the logical operations of AND, OR, and NOT using np.logical_and(), np.logical_or(), and np.logical_not() functions, respectively.

#

### Code Initialization

```python
import numpy as np

array_1 = np.array([True, False, True])
array_2 = np.array([False, False, True])
```

#### Logical AND
```python
print(np.logical_and(array_1, array_2))
```
Output: 
```
[False False True]
```

#### Logical OR
```python
print(np.logical_or(array_1, array_2))
```
Output:
```
[True False True]
```

#### Logical NOT
```python
print(np.logical_not(array_1)) 
```
Output:
```
[False True False]
```
