# Concatenation of Arrays

Concatenation of arrays in NumPy refers to combining multiple arrays into a single array, either along existing axes or by adding new axes. NumPy provides several functions for this purpose.

# Functions of Concatenation

## 1) np.concatenate 

Joins two or more arrays along an existing axis.

### Syntax
```python
numpy.concatenate((arr1, arr2, ...), axis)
```
- arr1, arr2, ...: Sequence of arrays to concatenate.
- axis: Axis along which the arrays will be joined. Default is 0.

### Example
```python
import numpy as np
#creating 2 arrays
arr1 = np.array([1 2 3],[7 8 9])
arr2 = np.array([4 5 6],[10 11 12])

#concatenate along axis 0
result_1 = np.concatenate((arr1, arr2), axis=0)
print("Concatenation along axis 0:")
print(result_1)
""" Output- Concatenation along axis 0:
[[ 1  2  3]
 [ 7  8  9]
 [ 4  5  6]
 [10 11 12]] """

#concatenate along axis 1
result_2 = np.concatenate((arr1, arr2), axis=1)
print("Concatenation along axis 1:")
print(result_2)
""" Output- Concatenation along axis 1:
[[ 1 2 3 4 5 6 ]
 [ 7 8 9 10 11 12]] """

```
## 2) np.vstack

Vertical stacking of arrays (row-wise).

### Syntax
```python
numpy.vstack(arrays)
```
- arrays: Sequence of arrays to stack.

### Example
```python
import numpy as np
#create arrays
arr1= np.array([1 2 3], [7 8 9])
arr2 = np.array([4 5 6],[10 11 12])

result = np.vstack((arr1, arr2))
print(result)
"""output-
[[ 1  2  3]
 [ 7  8  9]
 [ 4  5  6]
 [10 11 12]] """
```
## 3) np.hstack

Stacks arrays horizontally (column-wise).

### Syntax
```python
numpy.hstack(arrays)
```
- arrays: Sequence of arrays to stack.

### Example
```python
import numpy as np
#create arrays
arr1= np.array([1 2 3], [7 8 9])
arr2 = np.array([4 5 6],[10 11 12])

result = np.hstack((arr1, arr2))
print(result)
"""output-
[[ 1  2  3] [ 4  5  6]
 [ 7  8  9] [10 11 12]]  """
```
## 4) np.dstack 

Stacks arrays along the third axis (depth-wise).

### Syntax
```python
numpy.dstack(arrays)
```
- arrays: Sequence of arrays to stack.

### Example
```python
import numpy as np
#create arrays
arr1= np.array([1 2 3], [7 8 9])
arr2 = np.array([4 5 6],[10 11 12])

result = np.dstack((arr1, arr2))
print(result)
""" output-
[[[ 1  4]
  [ 2  5]
  [ 3  6]]

 [[ 7 10]
  [ 8 11]
  [ 9 12]]] """
```
## 5) np.stack

Joins a sequence of arrays along a new axis.
```python
numpy.stack(arrays, axis)
```
- arrays: Sequence of arrays to stack.

### Example
```python
import numpy as np
#create arrays
arr1= np.array([1 2 3], [7 8 9])
arr2 = np.array([4 5 6],[10 11 12])

result = np.stack((arr1, arr2), axis=0)
print(result)
""" output-
[[[ 1  2  3]
  [ 7  8  9]]

 [[ 4  5  6]
  [10 11 12]]] """
```
# Concatenation with Mixed Dimensions

When concatenating arrays with different shapes, it's often necessary to reshape them to have compatible dimensions.

## Example
```python
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([7, 8, 9])

# Concatenate along axis 0
result_0= np.concatenate((arr1, arr2[np.newaxis, :]), axis=0)
print("Concatenation along axis 0:")
print(result_0)
""" output-
Concatenation along axis 0:
[[1 2 3]
 [4 5 6]
 [7 8 9]] """

# Concatenate along axis 1
result_1 = np.concatenate((arr1, arr2[:, np.newaxis]), axis=1)
print("\nConcatenation along axis 1:")
print(result_1)
""" output-
Concatenation along axis 1:
[[1 2 3 7]
 [4 5 6 8]] """
```


