# Pandas DataFrame

The Pandas DataFrame is a two-dimensional, size-mutable, and possibly heterogeneous tabular data format with labelled axes. A data frame is a two-dimensional data structure in which the data can be organised in rows and columns. Pandas DataFrames are comprised of three main components: data, rows, and columns.

In the real world, Pandas DataFrames are formed by importing datasets from existing storage, which can be a Excel file, a SQL database or CSV file. Pandas DataFrames may be constructed from lists, dictionaries, or lists of dictionaries, etc.


Features of Pandas `DataFrame`:

- **Size mutable**: DataFrames are mutable in size, meaning that new rows and columns can be added or removed as needed.
- **Labeled axes**: DataFrames have labeled axes, which makes it easy to keep track of the data.
- **Arithmetic operations**: DataFrames support arithmetic operations on rows and columns.
- **High performance**: DataFrames are highly performant, making them ideal for working with large datasets.


### Installation of libraries

`pip install pandas` <br/>
`pip install xlrd`

- **Note**: The `xlrd` library is used for Excel operations.

Example for reading data from an Excel File:

```python
import pandas as pd

l = pd.read_excel('example.xlsx')
d = pd.DataFrame(l)
print(d)
```
Output:
```python
    Name  Age
0   John   12
```


Example for Inserting Data into Excel File:

```python
import pandas as pd

l = pd.read_excel('file_name.xlsx')
d = {'Name': ['Bob', 'John'], 'Age': [12, 28]}
d = pd.DataFrame(d)
L = pd.concat([l, d], ignore_index = True)
L.to_excel('file_name.xlsx', index = False)
print(L)
```

Output:
```python
    Name  Age
0   Bob   12
1   John  28
```

### Usage of Pandas DataFrame:

- Can be used to store and analyze financial data, such as stock prices, trading data, and economic data.
- Can be used to store and analyze sensor data, such as data from temperature sensors, motion sensors, and GPS sensors.
- Can be used to store and analyze log data, such as web server logs, application logs, and system logs
