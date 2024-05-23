# Operations on Arrays

## NumPy Arithmetic Operations

NumPy offers a broad array of operations for arrays, including arithmetic functions.

The arithmetic operations in NumPy are popular for their simplicity and efficiency in handling array calculations.

**Addition**

we can use the `+` operator to perform element-wise addition between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 + array_2
print("Utilizing the + operator:", result_1) 
```

**Output:**
```
Utilizing the + operator: [10 13 16 19]
```

**Subtraction**

we can use the `-` operator to perform element-wise subtraction between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 - array_2
print("Utilizing the - operator:", result_1) 
```

**Output:**
```
Utilizing the - operator: [8 7 6 5]
```

**Multiplication**

we can use the `*` operator to perform element-wise multiplication between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 * array_2
print("Utilizing the * operator:", result_1) 
```

**Output:**
```
Utilizing the * operator: [9 30 55 84]
```

**Division**

we can use the `/` operator to perform element-wise division between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 / array_2
print("Utilizing the / operator:", result_1) 
```

**Output:**
```
Utilizing the / operator: [9. 3.33333333 2.2 1.71428571]
```

**Exponentiation**

we can use the `**` operator to perform element-wise exponentiation between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 ** array_2
print("Utilizing the ** operator:", result_1) 
```

**Output:**
```
Utilizing the ** operator: [9 1000 161051 35831808]
```

**Modulus**

We can use the `%` operator to perform element-wise modulus operations between two or more NumPy arrays.

**Code**
```python
import numpy as np
array_1 = np.array([9, 10, 11, 12])
array_2 = np.array([1, 3, 5, 7])
result_1 = array_1 % array_2
print("Utilizing the % operator:", result_1) 
```

**Output:**
```
Utilizing the % operator: [0 1 1 5]
```

<br>

## NumPy Comparision Operations

<br>

NumPy provides various comparison operators that can compare elements across multiple NumPy arrays.

**less than operator**

The `<` operator returns `True` if the value of operand on left is less than the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_1 = array_1 < array_2
print("array_1 < array_2:",result_1)
```
**Output:**
```
array_1 < array_2 : [True False False]
```    

**less than or equal to operator**

The `<=` operator returns `True` if the value of operand on left is lesser than or equal to the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_1 = array_1 <= array_2
print("array_1 <= array_2:",result_1)
```
**Output:**
```
array_1 <= array_2: [True True False]
``` 

**greater than operator**

The `>` operator returns `True` if the value of operand on left is greater than the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_2 = array_1 > array_2
print("array_1 > array_2:",result_2)    
```
**Output:**
```
array_1 > array_2 : [False False True]
```

**greater than or equal to operator**

The `>=` operator returns `True` if the value of operand on left is greater than or equal to the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_2 = array_1 >= array_2
print("array_1 >= array_2:",result_2)   
```
**Output:**
```
array_1 >= array_2: [False True True]
```

**equal to operator**

The `==` operator returns `True` if the value of operand on left is same as the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_3 = array_1 == array_2
print("array_1 == array_2:",result_3)
```
**Output:**
```
array_1 == array_2: [False True False]
```

**not equal to operator**

The `!=` operator returns `True` if the value of operand on left is not equal to the value of operand on right.

**Code**
```python
import numpy as np
array_1 = np.array([12,15,20])
array_2 = np.array([20,15,12])
result_3 = array_1 != array_2
print("array_1 != array_2:",result_3)    
```
**Output:**
```
array_1 != array_2: [True False True]
```

<br>

## NumPy Logical Operations

Logical operators perform Boolean algebra. A branch of algebra that deals with `True` and `False` statements.

It illustrates the logical operations of AND, OR, and NOT using np.logical_and(), np.logical_or(), and np.logical_not() functions, respectively.

**Logical AND**

Evaluates the element-wise truth value of `array_1` AND `array_2`

**Code**
```python
import numpy as np
array_1 = np.array([True, False, True])
array_2 = np.array([False, False, True])
print(np.logical_and(array_1, array_2))
```
**Output:**
```
[False False True]
```

**Logical OR**

Evaluates the element-wise truth value of `array_1` OR `array_2`

**Code**
```python
import numpy as np
array_1 = np.array([True, False, True])
array_2 = np.array([False, False, True])
print(np.logical_or(array_1, array_2))
```
**Output:**
```
[True False True]
```

**Logical NOT**

Evaluates the element-wise truth value of `array_1` NOT `array_2`

**Code**
```python
import numpy as np
array_1 = np.array([True, False, True])
array_2 = np.array([False, False, True])
print(np.logical_not(array_1)) 
```
**Output:**
```
[False True False]
```
