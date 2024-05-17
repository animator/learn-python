# Pandas DataFrame

The Pandas DataFrame is a two-dimensional, size-mutable, and possibly heterogeneous tabular data format with labelled axes. A data frame is a two-dimensional data structure in which the data can be organised in rows and columns. Pandas DataFrames are comprised of three main components: data, rows, and columns.

In the real world, Pandas DataFrames are formed by importing datasets from existing storage, which can be a Excel file, a SQL database or CSV file. Pandas DataFrames may be constructed from lists, dictionaries, or lists of dictionaries, etc.


### Installation of libraries

`pip install pandas
 pip install xlrd`


Example for reading data from an Excel File:

```python
import pandas as pd

l = pd.read_excel('example.xlsx')
d = pd.DataFrame(l)
print(d)
```
Output:
'''python
    Name  Age
0   John   12
'''

- **Note:** The above program can also be used for loading/retrieving the data.


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
'''python
    Name  Age
0   Bob   12
1   John  28
'''

