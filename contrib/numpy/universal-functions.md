# Universal functions (ufunc)

---

A `ufunc`, short for "`universal function`," is a fundamental concept in NumPy, a powerful library for numerical computing in Python. Universal functions are highly optimized, element-wise functions designed to perform operations on data stored in NumPy arrays. 



## Uses of Ufuncs in NumPy

Universal functions (ufuncs) in NumPy provide a wide range of functionalities for efficient and powerful numerical computations. Below is a detailed explanation of their uses:

### 1. **Element-wise Operations**
Ufuncs perform operations on each element of the arrays independently.

```python
import numpy as np

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])

# Element-wise addition
np.add(A, B)  # Output: array([ 6,  8, 10, 12])
```

### 2. **Broadcasting**
Ufuncs support broadcasting, allowing operations on arrays with different shapes, making it possible to perform operations without explicitly reshaping arrays.

```python
C = np.array([1, 2, 3])
D = np.array([[1], [2], [3]])

# Broadcasting addition
np.add(C, D)  # Output: array([[2, 3, 4], [3, 4, 5], [4, 5, 6]])
```

### 3. **Vectorization**
Ufuncs are vectorized, meaning they are implemented in low-level C code, allowing for fast execution and avoiding the overhead of Python loops.

```python
# Vectorized square root
np.sqrt(A)  # Output: array([1., 1.41421356, 1.73205081, 2.])
```

### 4. **Type Flexibility**
Ufuncs handle various data types and perform automatic type casting as needed.

```python
E = np.array([1.0, 2.0, 3.0])
F = np.array([4, 5, 6])

# Addition with type casting
np.add(E, F)  # Output: array([5., 7., 9.])
```

### 5. **Reduction Operations**
Ufuncs support reduction operations, such as summing all elements of an array or finding the product of all elements.

```python
# Summing all elements
np.add.reduce(A)  # Output: 10

# Product of all elements
np.multiply.reduce(A)  # Output: 24
```

### 6. **Accumulation Operations**
Ufuncs can perform accumulation operations, which keep a running tally of the computation.

```python
# Cumulative sum
np.add.accumulate(A)  # Output: array([ 1,  3,  6, 10])
```

### 7. **Reduceat Operations**
Ufuncs can perform segmented reductions using the `reduceat` method, which applies the ufunc at specified intervals.

```python
G = np.array([0, 1, 2, 3, 4, 5, 6, 7])
indices = [0, 2, 5]
np.add.reduceat(G, indices)  # Output: array([ 1,  9, 18])
```

### 8. **Outer Product**
Ufuncs can compute the outer product of two arrays, producing a matrix where each element is the result of applying the ufunc to each pair of elements from the input arrays.

```python
# Outer product
np.multiply.outer([1, 2, 3], [4, 5, 6])  
# Output: array([[ 4,  5,  6],
#                [ 8, 10, 12],
#                [12, 15, 18]])
```

### 9. **Out Parameter**
Ufuncs can use the `out` parameter to store results in a pre-allocated array, saving memory and improving performance.

```python
result = np.empty_like(A)
np.multiply(A, B, out=result)  # Output: array([ 5, 12, 21, 32])
```

# Create Your Own Ufunc

You can create custom ufuncs for specific needs using np.frompyfunc or np.vectorize, allowing Python functions to behave like ufuncs.

Here, we are using `frompyfunc()` which takes three argument:

1. function - the name of the function.
2. inputs - the number of input  (arrays).
3. outputs - the number of output arrays.

```python
def my_add(x, y):
    return x + y

my_add_ufunc = np.frompyfunc(my_add, 2, 1)
my_add_ufunc(A, B)  # Output: array([ 6,  8, 10, 12], dtype=object)
```
# Some Common Ufunc are

Here are some commonly used ufuncs in NumPy:

- **Arithmetic**: `np.add`, `np.subtract`, `np.multiply`, `np.divide`
- **Trigonometric**: `np.sin`, `np.cos`, `np.tan`
- **Exponential and Logarithmic**: `np.exp`, `np.log`, `np.log10`
- **Comparison**: `np.maximum`, `np.minimum`, `np.greater`, `np.less`
- **Logical**: `np.logical_and`, `np.logical_or`, `np.logical_not`

For more such Ufunc, address to  [Universal functions (ufunc) — NumPy](https://numpy.org/doc/stable/reference/ufuncs.html)
