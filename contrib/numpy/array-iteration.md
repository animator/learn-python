# NumPy Array Iteration

Iterating over arrays in NumPy is a common task when processing data. NumPy provides several ways to iterate over elements of an array efficiently. 
Understanding these methods is crucial for performing operations on array elements effectively.

## 1. Basic Iteration

- Iterating using basic `for` loop.
  
### Single-dimensional array

Iterating over a single-dimensional array is straightforward using a basic `for` loop

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
for i in arr:
    print(i)
```

#### Output

```python
1
2
3
4
5
```

### Multi-dimensional array

Iterating over multi-dimensional arrays, each iteration returns a sub-array along the first axis.

```python
marr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for arr in marr:
    print(arr)
```

#### Output

```python
[1 2 3]
[4 5 6]
[7 8 9]
```

## 2. Iterating with `nditer`

- `nditer` is a powerful iterator provided by NumPy for iterating over multi-dimensional arrays.
- In each interation it gives each element.

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in np.nditer(arr):
    print(i)
```

#### Output

```python
1
2
3
4
5
6
```

## 3. Iterating with `ndenumerate`

- `ndenumerate` allows you to iterate with both the index and the value of each element.
- It gives index and value as output in each iteration

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
for index,value in np.ndenumerate(arr):
    print(index,value)
```

#### Output

```python
(0, 0) 1
(0, 1) 2
(1, 0) 3
(1, 1) 4
```

## 4. Iterating with flat

- The `flat` attribute returns a 1-D iterator over the array.

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
for element in arr.flat:
    print(element)
```

#### Output

```python
1
2
3
4
```

Understanding the various ways to iterate over NumPy arrays can significantly enhance your data processing efficiency.

Whether you are working with single-dimensional or multi-dimensional arrays, NumPy provides versatile tools to iterate and manipulate array elements effectively.
