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


_Referred from: W3schools_

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
    # Size: int8, int16, int32, int64

    print(arr.dtype())

    # Output: int64
```

Way 2: Using `dtype()`
``` python
    import numpy as np

    arr = np.array([2,4,6], dtype='i4')
    # Size: i1, i2, i4, i8

    print(arr.dtype)

    # Output: int32
```

Note: `np.intc()` has the same function as `int32()`.
## Example for float type

Way 1: Using function `float_()`
``` python
    import numpy as np

    arr = np.float_(1)
    # Size: float8, float16, float32, float64

    print(arr)
    print(arr.dtype())

    # Output: 
    # 1.0
    # float64
```

Way 2: Using `dtype()`
``` python
    import numpy as np

    arr = np.array([2,4,6], dtype='f4')
    # Size: f1, f2, f4, f8

    print(arr)
    print(arr.dtype)

    # Output:
    # [1. 2. 3. 4.]
    # float32
```

Note: `np.single()` has the same function as `float32()`.

## Example for boolean type

``` python
    import numpy as np

    x = np.bool_(1)

    print(x)
    print(x.dtype)

    # Output: 
    # True
    # bool
```
## Example for unsigned integer type

``` python
    import numpy as np

    x = np.uintc(1)

    print(x)
    print(x.dtype)

    # Output: 
    # 1
    # uint32
```

## Example for complex type
Complex type is a combination of real number + imaginary number. The `complex_()` is used to define the complex type NumPy object.
``` python
    import numpy as np

    x = np.complex_(1)
    # Size: complex64, complex128

    print(x)
    print(x.dtype)

    # Output: 
    # (1+0j)
    # complex128
```

## Example for datetime type
The `datetime64()` is used to define the date, month and year.

``` python
    import numpy as np

    x = np.datetime64('2024-05')
    y = np.datetime64('2024-05-20')
    z = np.datetime64('2024')
    
    print(x,x.dtype)
    print(y,y.dtype)
    print(z,z.dtype)

    # Output: 
    # 2024-05 datetime64[M]
    # 2024-20-05 datetime64[D]
    # 2024 datetime64[Y]
```

## Example for string type
``` python
    import numpy as np

    arr = np.str_("roopa")

    print(arr.dtype)

    # Output: <U5
```

## Example for object type
``` python
    import numpy as np

    arr = np.object_([1, 2, 3, 4])

    print(arr)
    print(arr.dtype)

    # Output: 
    # [1, 2, 3, 4]
    # object
```
## Example for unicode string type
``` python
    import numpy as np

    arr = np.array(['apple', 'banana', 'cherry'])

    print(arr.dtype)

    # Output: <U6
```
## Example for timedelta type
The `timedelta64()` used to find the difference between the `datetime64()`. The arguments for timedelta64 are a number, to represent the number of units, and a date/time unit, such as (D)ay, (M)onth, (Y)ear, (h)ours, (m)inutes, or (s)econds. The timedelta64 data type also accepts the string “NAT” in place of the number for a “Not A Time” value.

``` python
    import numpy as np

    x = np.datetime64('2024-05-20')
    y = np.datetime64('2023-05-20')
    res = x - y

    print(res)
    print(res.dtype)

    # Output: 
    # 366 days
    # timedelta64[D]
```
## Additional Data Type (`longdouble`)
`longdouble` is a data type that provides higher precision than the standard double-precision floating-point (`float64`) type.

``` python
    import numpy as np

    arr = np.longdouble([1.222222, 4.44, 45.55])

    print(arr, arr.dtype)

    # Output: 
    # [1.222222 4.44 45.55] float128
```

# Data Type Conversion
`astype()` function is used to the NumPy object from one type to another type.

It creates a copy of the array and allows to specify the data type of our choice.

## Example 1

``` python
    import numpy as np

    x = np.array([1.2, 3.4, 5.6])
    y = x.astype(int)

    print(y,y.dtype)

    # Output: 
    # [1 3 5] int64
```

## Example 2

``` python
    import numpy as np

    x = np.array([1, 3, 0])
    y = x.astype(bool)

    print(y,y.dtype)

    # Output: 
    # [True True False] bool
```
