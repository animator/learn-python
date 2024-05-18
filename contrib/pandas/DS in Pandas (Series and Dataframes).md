
# Data Structures in Pandas Library

Pandas generally provide two data structures for manipulating data. They are:

 1. Series
 2. DataFrame

# Pandas Series

A Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects, etc.). The axis labels are collectively called indexes.

The Pandas Series is nothing but a column in an Excel sheet. Labels need not be unique but must be of a hashable type.

The object supports both integer and label-based indexing and provides a host of methods for performing operations involving the index.


## Creating a Series:

Pandas Series is created by loading the datasets from existing storage (which can be a SQL database, a CSV file, or an Excel file).

Pandas Series can be created from lists, dictionaries, scalar values, etc.

```python
import pandas as pd  
import numpy as np 
  
# Creating empty series  
ser = pd.Series()  
print("Pandas Series: ", ser)  
  
# simple array  
data = np.array(['g', 'e', 'e', 'k', 's'])  
    
ser = pd.Series(data)  
print("Pandas Series:\n", ser)
```
### Output:
Pandas Series: Series([], dtype: float64)

Pandas Series:

0    g 

1    e

2    e

3    k

4    s

dtype: object

# Pandas DataFrame
Pandas DataFrame is a two-dimensional data structure with labeled axes (rows and columns).

## Creating Dataframe
Pandas DataFrame is created by loading the datasets from existing storage (which can be a SQL database, a CSV file, or an Excel file).

Pandas DataFrame can be created from lists, dictionaries, a list of dictionaries, etc.
Example: Creating a DataFrame Using the Pandas Library

```python
import pandas as pd 
	
# Calling DataFrame constructor 
df = pd.DataFrame() 
print(df) 

# list of strings 
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
	
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df)
```

### Output:
Empty DataFrame
Columns: []
Index: []
        0

0   Geeks

1     For

2   Geeks

3      is

4  portal

5     for

6   Geeks

## Running Pandas programs in Python.

The Pandas program can be run from any text editor(Python or VS code), but it is recommended to use Jupyter Notebook, as Jupyter gives you the ability to execute code in a particular cell rather than the entire file.

Jupyter also provides an easy way to visualize Pandas DataFrame and plots.

