# Numpy Data Types
In NumPy, data types play a crcial role in representing and manipulating numerical data.

Numpy supports the following data types:

- `i` - integer 
- `b` - boolean
- `u` - unsigned integer
- `f` - float
- `c` - complex float
- `m` - timedelta
- `M` - datetime
- `O` - object
- `S` - string
- `U` - unicode string

## dtype() Function
The `dtype()` function returns the type of the NumPy array object.

Example 1
``` python
    import numpy as np

    arr = np.array([1, 2, 3, 4])

    print(arr.dtype)

    # Output: int64
```

Example 2
``` python
    import numpy as np

    arr = np.array(['apple', 'banana', 'cherry'])

    print(arr.dtype)

    # Output: <U6
```
## Example for integer type
The NumPy integer array can be defined in two ways.

Way 1: Using function `int_()`
``` python
    import numpy as np

    arr = np.int_([2,4,6])
    
    print(arr.dtype())
    # Output: int64
```

Way 2: Using `dtype()`
``` python
    import numpy as np

    arr = np.array([2,4,6], dtype='i4')

    print(arr.dtype)

    # Output: int8
```
## Example for float type

## Example for boolean type

## Example for unsigned integer type

## Example for complex type

## Example for datetime type

## Example for string type

## Example for object type

## Example for unicode string type

## Example for timedelta type

# Data Type Conversion

