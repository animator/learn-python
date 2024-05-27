# Handling Missing Values in Pandas

In real life, many datasets arrive with missing data either because it exists and was not collected or it never existed.

In Pandas missing data is represented by two values:

* `None` : None is simply is `keyword` refer as empty or none.
* `NaN` : Acronym for `Not a Number`.

There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame:

1. `isnull()`
2. `notnull()`
3. `dropna()`
4. `fillna()`
5. `replace()`

## 2. Checking for missing values using `isnull()` and `notnull()`

Let's import pandas and our fancy car-sales dataset having some missing values.

```python
import pandas as pd

car_sales_missing_df = pd.read_csv("Datasets/car-sales-missing-data.csv")
print(car_sales_missing_df)
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue       NaN    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green       NaN    4.0   $4,500
    6   Honda    NaN       NaN    4.0   $7,500
    7   Honda   Blue       NaN    4.0      NaN
    8  Toyota  White   60000.0    NaN      NaN
    9     NaN  White   31600.0    4.0   $9,700
    


```python
## Using isnull()

print(car_sales_missing_df.isnull())
```

        Make  Colour  Odometer  Doors  Price
    0  False   False     False  False  False
    1  False   False     False  False  False
    2  False   False      True  False  False
    3  False   False     False  False  False
    4  False   False     False  False  False
    5  False   False      True  False  False
    6  False    True      True  False  False
    7  False   False      True  False   True
    8  False   False     False   True   True
    9   True   False     False  False  False
    

Note here:
* `True` means for `NaN` values
* `False` means for no `Nan` values

If we want to find the number of missing values in each column use `isnull().sum()`.


```python
print(car_sales_missing_df.isnull().sum())
```

    Make        1
    Colour      1
    Odometer    4
    Doors       1
    Price       2
    dtype: int64
    

You can also check presense of null values in a single column.


```python
print(car_sales_missing_df["Odometer"].isnull())
```

    0    False
    1    False
    2     True
    3    False
    4    False
    5     True
    6     True
    7     True
    8    False
    9    False
    Name: Odometer, dtype: bool
    


```python
## using notnull()

print(car_sales_missing_df.notnull())
```

        Make  Colour  Odometer  Doors  Price
    0   True    True      True   True   True
    1   True    True      True   True   True
    2   True    True     False   True   True
    3   True    True      True   True   True
    4   True    True      True   True   True
    5   True    True     False   True   True
    6   True   False     False   True   True
    7   True    True     False   True  False
    8   True    True      True  False  False
    9  False    True      True   True   True
    

Note here:
* `True` means no `NaN` values
* `False` means for `NaN` values

`isnull()` means having null values so it gives boolean `True` for NaN values. And `notnull()` means having no null values so it gives `True` for no NaN value.

## 2. Filling missing values using `fillna()`, `replace()`.


```python
## Filling missing values  with a single value using `fillna`
print(car_sales_missing_df.fillna(0))
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue       0.0    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green       0.0    4.0   $4,500
    6   Honda      0       0.0    4.0   $7,500
    7   Honda   Blue       0.0    4.0        0
    8  Toyota  White   60000.0    0.0        0
    9       0  White   31600.0    4.0   $9,700
    


```python
## Filling missing values with the previous value using `ffill()`
print(car_sales_missing_df.ffill())
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue   87899.0    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green  213095.0    4.0   $4,500
    6   Honda  Green  213095.0    4.0   $7,500
    7   Honda   Blue  213095.0    4.0   $7,500
    8  Toyota  White   60000.0    4.0   $7,500
    9  Toyota  White   31600.0    4.0   $9,700
    


```python
## illing null value with the next ones  using 'bfill()'
print(car_sales_missing_df.bfill())
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue   11179.0    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green   60000.0    4.0   $4,500
    6   Honda   Blue   60000.0    4.0   $7,500
    7   Honda   Blue   60000.0    4.0   $9,700
    8  Toyota  White   60000.0    4.0   $9,700
    9     NaN  White   31600.0    4.0   $9,700
    

#### Filling a null values using `replace()` method

Now we are going to replace the all `NaN` value in the data frame with -125 value

For this we will also need numpy


```python
import numpy as np

print(car_sales_missing_df.replace(to_replace = np.nan, value = -125))
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue    -125.0    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green    -125.0    4.0   $4,500
    6   Honda   -125    -125.0    4.0   $7,500
    7   Honda   Blue    -125.0    4.0     -125
    8  Toyota  White   60000.0 -125.0     -125
    9    -125  White   31600.0    4.0   $9,700
    

## 3. Dropping missing values using `dropna()`

In order to drop a null values from a dataframe, we used `dropna()` function this function drop Rows/Columns of datasets with Null values in different ways.

#### Dropping rows with at least 1 null value. 


```python
print(car_sales_missing_df.dropna(axis = 0))  ##Now we drop rows with at least one Nan value (Null value) 
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    

#### Dropping rows if all values in that row are missing.


```python
print(car_sales_missing_df.dropna(how = 'all',axis = 0))  ## If not have leave the row as it is
```

         Make Colour  Odometer  Doors    Price
    0  Toyota  White  150043.0    4.0   $4,000
    1   Honda    Red   87899.0    4.0   $5,000
    2  Toyota   Blue       NaN    3.0   $7,000
    3     BMW  Black   11179.0    5.0  $22,000
    4  Nissan  White  213095.0    4.0   $3,500
    5  Toyota  Green       NaN    4.0   $4,500
    6   Honda    NaN       NaN    4.0   $7,500
    7   Honda   Blue       NaN    4.0      NaN
    8  Toyota  White   60000.0    NaN      NaN
    9     NaN  White   31600.0    4.0   $9,700
    

#### Dropping columns with at least 1 null value


```python
print(car_sales_missing_df.dropna(axis = 1))
```

    Empty DataFrame
    Columns: []
    Index: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

Now we drop a columns which have at least 1 missing values.

Here the dataset becomes empty after `dropna()` because each column as atleast 1 null value so it remove that columns resulting in an empty dataframe.
