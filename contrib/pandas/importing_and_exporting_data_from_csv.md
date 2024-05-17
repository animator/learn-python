# Importing and Exporting Data with Pandas

Pandas is a powerful data manipulation library in Python that provides data structures and functions needed to work on structured data seamlessly. One of the most common tasks in data analysis is importing data from external sources and exporting data after manipulation. This guide covers the basics of importing and exporting data using Pandas.

## Table of Contents
1. [Importing Data from CSV](#importing-data-from-csv)
2. [Exporting Data to CSV](#exporting-data-to-csv)

## Importing Data from CSV

CSV (Comma-Separated Values) is one of the most common data formats. Pandas provides a convenient function `read_csv` to load data from a CSV file into a DataFrame.

### Syntax

import pandas as pd<br>
df = pd.read_csv('path_to_your_file.csv')

### Example

import pandas as pd<br>
df = pd.read_csv('data.csv')<br>
print(df.head())

### Additional Parameters

- `sep`: Specify a different delimiter (default is comma).
- `header`: Row number(s) to use as the column names.
- `names`: List of column names to use.
- `index_col`: Column(s) to set as index (make sure the index column is unique).
- `usecols`: Return a subset of the columns.

### Example with Additional Parameters

df = pd.read_csv('data.csv', sep=';', header=0, index_col='id', usecols=['id', 'name', 'age'])<br>
print(df.head())


## Exporting Data to CSV

After processing the data, you may want to save the DataFrame back to a CSV file. Pandas provides the `to_csv` function for this purpose.

### Syntax

df.to_csv('path_to_save_file.csv')

### Example

import pandas as pd<br>
data = {<br>
    'Name': ['Alice', 'Bob', 'Charlie'],<br>
    'Age': [25, 30, 35]<br>
}<br>
df = pd.DataFrame(data)<br>
df.to_csv('output.csv', index=False)<br>


### Additional Parameters

- `sep`: Specify a different delimiter (default is comma).
- `index`: Whether to write row names (default is True).
- `header`: Write out the column names (default is True).

### Example with Additional Parameters

df.to_csv('output.csv', sep=';', index=False, header=True)

