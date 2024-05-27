# Sorting NumPy Arrays
- Sorting arrays is a common operation in data manipulation and analysis.
- NumPy provides various functions to sort arrays efficiently.
- The primary methods are `numpy.sort`,`numpy.argsort`, and `numpy.lexsort`

### 1. numpy.sort()

The `numpy.sort` function returns a sorted copy of an array.

#### Syntax :

```python
numpy.sort(arr, axis=-1, kind=None, order=None)
```
- **arr** : Array to be sorted.
- **axis** : Axis along which to sort. (By Default is -1)
- **kind** : Sorting algorithm. Options are 'quicksort', 'mergesort', 'heapsort', and 'stable'. (By Default 'quicksort')
- **order** : When arr is an array with fields defined, this argument specifies which fields to compare first.

#### Example :

```python
import numpy as np

arr = np.array([1,7,0,4,6])
sarr = np.sort(arr)
print(sarr)
```

**Output** :
```python
[0 1 4 6 7]
```

### 2. numpy.argsort()

The `numpy.argsort` function returns the indices that would sort an array. Using those indices you can sort the array.

#### Syntax :

```python
numpy.argsort(a, axis=-1, kind=None, order=None)
```
- **arr** : Array to be sorted.
- **axis** : Axis along which to sort. (By Default is -1)
- **kind** : Sorting algorithm. Options are 'quicksort', 'mergesort', 'heapsort', and 'stable'. (By Default 'quicksort')
- **order** : When arr is an array with fields defined, this argument specifies which fields to compare first.

#### Example :

```python
import numpy as np

arr = np.array([2.1,7,4.2,4.3,6])
indices = np.argsort(arr)
print(indices)
s_arr = arr[indices]
print(s_arr)
```

**Output** :
```python
[0 2 3 4 1]
[2.1 4.2 4.3 6. 7. ]
```

### 3. np.lexsort()

The np.lexsort function performs an indirect stable sort using a sequence of keys.

#### Syntax :

```python
numpy.lexsort(keys, axis=-1)
```
- **keys**: Sequence of arrays to sort by. The last key is the primary sort key.
- **axis**: Axis to be indirectly sorted.(By Default -1)

#### Example :

```python
import numpy as np

a = np.array([5,4,3,2])
b = np.array(['a','d','c','b'])
indices = np.lexsort((a,b))
print(indices)

s_arr = a[indices]
print(s_arr)

s_arr = b[indices]
print(s_arr)
```

**Output** :
```python
[0 3 2 1]
[2 3 4 5]
['a' 'b' 'c' 'd']
```

NumPy provides powerful and flexible functions for sorting arrays, including `np.sort`, `np.argsort`, and `np.lexsort`. 
These functions support sorting along different axes, using various algorithms, and sorting by multiple keys, making them suitable for a wide range of data manipulation tasks.
