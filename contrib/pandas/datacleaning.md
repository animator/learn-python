# Data Cleaning and Preparation with Pandas

In real life, many datasets come with missing data, either because it wasn't collected or it never existed. In Pandas, missing data is represented by two values:

- `None`: A keyword referring to empty or none.
- `NaN`: Acronym for Not a Number.

There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame:

- `isnull()`
- `notnull()`
- `dropna()`
- `fillna()`
- `replace()`

## Checking for Missing Values using isnull() and notnull()

Let's import Pandas and our fancy car-sales dataset with some missing values.

```python
import pandas as pd

car_sales_missing_df = pd.read_csv("Datasets/car-sales-missing-data.csv")
print(car_sales_missing_df)
```
Output:

        Make Colour  Odometer  Doors    Price
    0 Toyota White 150043.0 4.0 $4,000
    1 Honda Red 87899.0 4.0 $5,000
    2 Toyota Blue NaN 3.0 $7,000
    3 BMW Black 11179.0 5.0 $22,000
    4 Nissan White 213095.0 4.0 $3,500
    5 Toyota Green NaN 4.0 $4,500
    6 Honda NaN NaN 4.0 $7,500
    7 Honda Blue NaN 4.0 NaN
    8 Toyota White 60000.0 NaN NaN
    9 NaN White 31600.0 4.0 $9,700

## Using isnull()

```
print(car_sales_missing_df.isnull())
```

Output:

        Make  Colour  Odometer  Doors  Price
    0 False False False False False
    1 False False False False False
    2 False False True False False
    3 False False False False False
    4 False False False False False
    5 False False True False False
    6 False True True False False
    7 False False True False True
    8 False False False True True
    9 True False False False False


- True indicates NaN values.

- False indicates no NaN values.

To find the number of missing values in each column:

```
print(car_sales_missing_df.isnull().sum())
```

Output:
```
Make 1
Colour 1
Odometer 4
Doors 1
Price 2
dtype: int64
```
You can also check the presence of null values in a single column:

```
print(car_sales_missing_df["Odometer"].isnull())
```

Output:
```
0 False
1 False
2 True
3 False
4 False
5 True
6 True
7 True
8 False
9 False
Name: Odometer, dtype: bool
```
## Using notnull()

```

print(car_sales_missing_df.notnull())
```

Output:
```
       Make  Colour  Odometer  Doors  Price
    0 True True True True True
    1 True True True True True
    2 True True False True True
    3 True True True True True
    4 True True True True True
    5 True True False True True
    6 True False False True True
    7 True True False True False
    8 True True True False False
    9 False True True True True
```
- True indicates no NaN values.
- False indicates NaN values.
 -isnull() indicates the presence of null values, returning True for NaN values. notnull() indicates no null values, returning True for no NaN value.

## Removing Columns with Null Values
You can drop columns with null values by setting the axis parameter to 1.

```
print(car_sales_missing_df.dropna(axis=1))



```

Output:

        Make Colour
    0 Toyota White
    1 Honda Red
    2 Toyota Blue
    3 BMW Black
    4 Nissan White
    5 Toyota Green
    6 Honda NaN
    7 Honda Blue
    8 Toyota White
    9 NaN White
    ```

   ## Filling Missing Values with the Previous Value using ffill()

   ```
   print(car_sales_missing_df.ffill())

```
Output: 

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

