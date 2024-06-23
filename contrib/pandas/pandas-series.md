# Pandas Series

A series is a Panda data structures that represents a one dimensional array-like object containing an array of data and an associated array of data type labels, called index.

## Creating a Series object:

### Basic Series
To create a basic Series, you can pass a list or array of data to the `pd.Series()` function.

```python
import pandas as pd

s1 = pd.Series([4, 5, 2, 3])
print(s1)
```

#### Output
```
0    4
1    5
2    2
3    3
dtype: int64
```

### Series from a Dictionary

If you pass a dictionary to `pd.Series()`, the keys become the index and the values become the data of the Series. 
```python
import pandas as pd

s2 = pd.Series({'A': 1, 'B': 2, 'C': 3})
print(s2)
```

#### Output
```
A    1
B    2
C    3
dtype: int64
```


## Additional Functionality


### Specifying Data Type and Index
You can specify the data type and index while creating a Series.
```python
import pandas as pd

s4 = pd.Series([1, 2, 3], index=['a', 'b', 'c'], dtype='float64')
print(s4)
```

#### Output
```
a    1.0
b    2.0
c    3.0
dtype: float64
```

### Specifying NaN Values:
* Sometimes you need to create a series object of a certain size but you do not have complete data available so in such cases you can fill missing data with a NaN(Not a Number) value. 
* When you store NaN value in series object, the data type must be floating pont type. Even if you specify an integer type , pandas will promote it to floating point type automatically because NaN is not supported by integer type.

```python
import pandas as pd
s3=pd.Series([1,np.Nan,2])
print(s3)
```

#### Output
```
0  1.0
1  NaN
2  2.0
dtype: float64
```


### Creating Data from Expressions
You can create a Series using an expression or function.

`<series_object>`=np.Series(data=<function|expression>,index=None)

```python
import pandas as pd
a=np.arange(1,5)  # [1,2,3,4]
s5=pd.Series(data=a**2,index=a)
print(s5)
```

#### Output
```
1  1
2  4
3  9
4  16
dtype: int64
```

## Series Object Attributes

| **Attribute**            | **Description**                                   |
|--------------------------|---------------------------------------------------|
| `<series>.index`         | Array of index of the Series                      |
| `<series>.values`        | Array of values of the Series                     |
| `<series>.dtype`         | Return the dtype of the data                      |
| `<series>.shape`         | Return a tuple representing the shape of the data |
| `<series>.ndim`          | Return the number of dimensions of the data       |
| `<series>.size`          | Return the number of elements in the data         |
| `<series>.hasnans`       | Return True if there is any NaN in the data       |
| `<series>.empty`         | Return True if the Series object is empty         |

- If you use len() on a series object then it return total number of elements in the series object whereas <series_object>.count() return only the number of non NaN elements.

##  Accessing a Series object and its elements

### Accessing Individual Elements 
You can access individual elements using their index.
'legal' indexes arte used to access individual element.
```python
import pandas as pd

s7 = pd.Series(data=[13, 45, 67, 89], index=['A', 'B', 'C', 'D'])
print(s7['A'])
```

#### Output
```
13
```

### Slicing a Series

- Slices are extracted based on their positional index, regardless of the custom index labels.
- Each element in the Series has a positional index starting from 0 (i.e., 0 for the first element, 1 for the second element, and so on).
- `<series>[<start>:<end>]` will return the values of the elements between the start and end positions (excluding the end position).

#### Example

```python
import pandas as pd

s = pd.Series(data=[13, 45, 67, 89], index=['A', 'B', 'C', 'D'])
print(s[:2])
```

#### Output
```
A    13
B    45
dtype: int64
```

This example demonstrates that the first two elements (positions 0 and 1) are returned, regardless of their custom index labels.

## Operation on series object

### Modifying elements and indexes 
*  <series_object>[indexes]=< new data value >
*  <series_object>[start : end]=< new data value >
*  <series_object>.index=[new indexes]

```python
import pandas as pd

s8 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s8['a'] = 100
s8.index = ['x', 'y', 'z']
print(s8)
```

#### Output
```
x    100
y     20
z     30
dtype: int64
```

**Note: Series object are value-mutable but size immutable objects.**

### Vector operations
We can perform vector operations such as `+`,`-`,`/`,`%` etc.

#### Addition
```python
import pandas as pd

s9 = pd.Series([1, 2, 3])
print(s9 + 5)
```

#### Output
```
0    6
1    7
2    8
dtype: int64
```

#### Subtraction
```python
print(s9 - 2)
```

#### Output
```
0   -1
1    0
2    1
dtype: int64
```

### Arthmetic on series object

#### Addition
```python
import pandas as pd

s10 = pd.Series([1, 2, 3])
s11 = pd.Series([4, 5, 6])
print(s10 + s11)
```

#### Output
```
0    5
1    7
2    9
dtype: int64
```

#### Multiplication

```python
print("s10 * s11)
```

#### Output
```
0     4
1    10
2    18
dtype: int64
```

Here one thing we should keep in mind that both the series object should have same indexes otherwise it will return NaN value to all the indexes of two series object .


### Head and Tail Functions

| **Functions**            | **Description**                                   |
|--------------------------|---------------------------------------------------|
| `<series>.head(n)`       | return the first n elements of the series         |
| `<series>.tail(n)`       | return the last n elements of the series          |

```python
import pandas as pd

s12 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(s12.head(3))
print(s12.tail(3))
```

#### Output
```
0    10
1    20
2    30
dtype: int64
7     80
8     90
9    100
dtype: int64
```

If you dont provide any value to n the by default it give results for `n=5`.

### Few extra functions

| **Function**                           | **Description**                                                        |
|----------------------------------------|------------------------------------------------------------------------|
| `<series_object>.sort_values()`        | Return the Series object in ascending order based on its values.       |
| `<series_object>.sort_index()`         | Return the Series object in ascending order based on its index.        |
| `<series_object>.sort_drop(<index>)`   | Return the Series with the deleted index and its corresponding value.  |

```python
import pandas as pd

s13 = pd.Series([3, 1, 2], index=['c', 'a', 'b'])
print(s13.sort_values())
print(s13.sort_index())
print(s13.drop('a'))
```

#### Output
```
a    1
b    2
c    3
dtype: int64
a    1
b    2
c    3
dtype: int64
c    3
b    2
dtype: int64
```

## Conclusion 
In short, Pandas Series is a fundamental data structure in Python for handling one-dimensional data. It combines an array of values with an index, offering efficient methods for data manipulation and analysis. With its ease of use and powerful functionality, Pandas Series is widely used in data science and analytics for tasks such as data cleaning, exploration, and visualization.
