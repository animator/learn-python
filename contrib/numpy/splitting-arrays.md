# Splitting Arrays

Splitting a NumPy array refers to dividing the array into smaller sub-arrays. This can be done in various ways, along specific rows, columns, or even based on conditions applied to the elements.

There are several ways to split a NumPy array in Python using different functions. Some of these methods include:

- Splitting a NumPy array using `numpy.split()`
- Splitting a NumPy array using `numpy.array_split()`
- Splitting a NumPy array using `numpy.vsplit()`
- Splitting a NumPy array using `numpy.hsplit()`
- Splitting a NumPy array using `numpy.dsplit()`

## NumPy split()

The `numpy.split()` function divides an array into equal parts along a specified axis.

**Code**
```python
import numpy as np
array = np.array([1,2,3,4,5,6])
#Splitting the array into 3 equal parts along axis=0
result = np.split(array,3)
print(result)
```

**Output**
```
[array([1, 2]), array([3, 4]), array([5, 6])]
```

## NumPy array_split()

The `numpy.array_split()` function divides an array into equal or nearly equal sub-arrays. Unlike `numpy.split()`, it allows for uneven splitting, making it useful when the array cannot be evenly divided by the specified number of splits.

**Code**
```python
import numpy as np
array = np.array([1,2,3,4,5,6,7,8])
#Splitting the array into 3 unequal parts along axis=0
result = np.array_split(array,3)
print(result)
```

**Output**
```
[array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]
```

## NumPy vsplit()

The `numpy.vsplit()`, which is vertical splitting (row-wise), divides an array along the vertical axis (axis=0).

**Code**
```python
import numpy as np
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])
#Vertically Splitting the array into 2 subarrays along axis=0
result = np.vsplit(array,2)
print(result)
```

**Output**
```
[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]])]
```


## NumPy hsplit()

The `numpy.hsplit()`, which is horizontal splitting (column-wise), divides an array along the horizontal axis (axis=1).

**Code**
```python
import numpy as np
array = np.array([[1, 2, 3, 4],
                  [5, 7, 8, 9],
                  [11,12,13,14]])
#Horizontally Splitting the array into 4 subarrays along axis=1
result = np.hsplit(array,4)
print(result)
```

**Output**
```
[array([[ 1],
       [ 5],
       [11]]), array([[ 2],
       [ 7],
       [12]]), array([[ 3],
       [ 8],
       [13]]), array([[ 4],
       [ 9],
       [14]])]
```

## NumPy dsplit()

The`numpy.dsplit()` is employed for splitting arrays along the third axis (axis=2), which is applicable for 3D arrays and beyond.

**Code**
```python
import numpy as np
#3D array
array = np.array([[[ 1, 2, 3, 4,],
                   [ 5, 6, 7, 8,],
                   [ 9, 10, 11, 12]],
                   [[13, 14, 15, 16,],
                   [17, 18, 19, 20,],
                   [21, 22, 23, 24]]])
#Splitting the array along axis=2
result = np.dsplit(array,2)
print(result)
```

**Output**
```
[array([[[ 1,  2],
        [ 5,  6],
        [ 9, 10]],

       [[13, 14],
        [17, 18],
        [21, 22]]]), array([[[ 3,  4],
        [ 7,  8],
        [11, 12]],

       [[15, 16],
        [19, 20],
        [23, 24]]])]
```
