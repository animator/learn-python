# Pandas Series Vs NumPy ndarray

NumPy ndarray and Pandas Series are two fundamental data structures in Python for handling and manipulating data. While they share some similarities, they also have distinct characteristics that make them suitable for different tasks.

Both NumPy ndarray and Pandas Series are essential tools for data manipulation in Python, Choosing between them depends on the nature of your data and the specific tasks you need to perform.

## NumPy ndarray

NumPy is short form for Numerical Python, provides a powerful array object called `ndarray`, It is very important for many scientific and mathematical Python libraries. ndarray is also called n-dimensional array. Indexing in ndarray is integer based indexing (like arr[0], arr[3], etc.).

Features of NumPy `ndarray`:

- **Homogeneous Data**: All elements in a NumPy array are of the same data type, which allows for efficient storage and computation.
- **Efficient Computation and Performance**: NumPy arrays are designed for numerical operations and are highly efficient. They support vectorized operations, allowing you to perform operations on entire arrays rather than individual elements.
- **Multi-dimensional**: NumPy arrays can be multi-dimensional, making them suitable for representing complex numerical data structures like matrices and n-dimensional arrays.

Example of creating a NumPy array:

```python
import numpy as np

narr = np.array(['A', 'B', 'C', 'D', 'E'])
print(narr)
```
Output:
```python
['A' 'B' 'C' 'D' 'E']
```
### Usage of NumPy ndarray:

- When you need to perform mathematical operations on numerical data.
- When you’re working with multi-dimensional data.
- When computational efficiency is important.
- When you need to store data of same data type.

## Pandas Series

Pandas is a Python library used for data manipulation and analysis, introduces the `Series` data structure, which is designed for handling labeled one-dimensional data efficiently. Indexing in Pandas Series is Label-based. It effectively handles heterogeneous data.

Features of Pandas `Series`:

- **Labeled Data**: Pandas Series associates a label (or index) with each element of the array, making it easier to work with heterogeneous or labeled data.

- **Heterogeneous Data**: Unlike NumPy arrays, Pandas Series can hold data of different types (integers, floats, strings, etc.) within the same object.

- **Data Alignment**: One of the powerful features of Pandas Series is its ability to automatically align data based on label.

Example of creating a Pandas Series:

```python
import pandas as pd

series = pd.Series([1,'B', 5, 7, 6, 8], index = ['a','b','c','d','e','f'])
print(series)
```
Output:
```python
a    1
b    B
c    5
d    7
e    6
f    8
dtype: object
```

### Usage of Pandas Series:

- When you need to manipulate and analyze labeled data.
- When you’re dealing with heterogeneous data or missing values.
- When you need more high-level, flexible data manipulation functions.
- When you are dealing with One-dimensional data.
