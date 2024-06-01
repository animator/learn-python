# Data Aggregation using Pandas -

In data analysis and manipulation, aggregating data is a crucial step that involves combining multiple values into a single summary statistic. Pandas, a powerful data manipulation library in Python, provides various aggregation functions to perform these operations efficiently on DataFrame objects. 

Aggregation refers to the process of transforming data into a summarized form by applying specific functions on subsets of the data. Aggregation functions consolidate multiple values into a single value, revealing essential insights into the data as a whole. Pandas offers a wide range of built-in aggregation functions to fit diverse data analysis scenarios.

The main task of DataFrame.aggregate() function is to apply some aggregation to one or more column. Most frequently used aggregations are:

1. sum: It is used to return the sum of the values for the requested axis.

2. min: It is used to return the minimum of the values for the requested axis.

3. max: It is used to return the maximum values for the requested axis.
   
4. mean: Calculates the average value of a column or across all columns.

5. median: Determines the middle value of a column or across all columns.

6. count: Counts the number of non-null values in a column or across all columns.

7. nunique: Counts the number of unique values in a column or across all columns.

8. idxmax: The idxmax() function in pandas is used to return the index of the maximum value in a Series or DataFrame column. In other words, it gives us the row index where the maximum value occurs in the column.  

## Aggregation using agg() -

Syntax - DataFrame.aggregate(func, axis=0, *args, **kwargs)

Parameters - 
1. func - callable, string, dictionary, or list of string/callables. Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. For a DataFrame, can pass a dict, if the keys are DataFrame column names.
2. axis - (default 0) {0 or ‘index’, 1 or ‘columns’} 0 or ‘index’: apply function to each column. 1 or ‘columns’: apply function to each row.
3. *args, **kwargs - Optional arguments to be passed to the aggregation functions.

## Implementation in Python

import pandas as pd

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

df = pd.DataFrame(data)

x = df.aggregate(["sum"])

print(x)

## Output

Returns the sum of each row 

      x     y
sum  120  1454
