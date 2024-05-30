# Numpy Array Shape and Reshape
In NumPy, the primary data structure is the ndarray (N-dimensional array). An array can have one or more dimensions, and it organizes your data efficiently.

Code to create a 2D array
``` python
import numpy as np

numbers = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(numbers)

# Output:
# array([[1, 2, 3, 4],[5, 6, 7, 8]])
```

## Changing Array Shape using Reshape()
The `reshape()` function allows you to rearrange the data within a NumPy array.
It take 2 arguements, row and columns. The `reshape()` can add or remove the dimensions. For instance, array can convert a 1D array into a 2D array or vice versa.

``` python
arr_1d = np.array([1, 2, 3, 4, 5, 6]) # 1D array
arr_2d = arr_1d.reshape(2, 3) # Reshaping with 2rows and 3cols

print(arr_2d)

# Output:
# array([[1, 2, 3],[4, 5, 6]])

```

## Changing Array Shape using Resize()
The `resize()` function allows you to modify the shape of a NumPy array directly.
It take 2 arguements, row and columns.

``` python
import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5, 6])

arr_1d.resize((2, 3)) # 2rows and 3cols
print(arr_1d)

# Output:
# array([[1, 2, 3],[4, 5, 6]])

```

## Reshape() VS Resize()

| Reshape                                                | Resize |
| -----------                                            | ----------- |
| Does not modify the original array     | Modifies the original array in-place     |
| Creates a new array | Changes the shape of the array |
| Returns a reshaped array   | Doesn't return anything        |
| Compatibility between dimensions | Does not compatibility between dimensions |
| Syntax: reshape(row,col) | Syntax: resize((row,col)) |
