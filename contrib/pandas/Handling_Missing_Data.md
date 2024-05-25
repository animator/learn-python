# Handling Missing Data
## Intuition

Real-world data is rarely clean and uniform, which is how it differs from the data seen in many courses. More specifically, there will be some missing data in a lot of valuable datasets.

# Missing Data In Pandas

Pandas's handling of missing values is limited since it depends on the NumPy package, which lacks an internal concept of NA values for non-floating-point data types.

## None: Pythonic missing data
None, a Python singleton object that is frequently used for missing data in Python programs, is the initial sentinel value utilized by Pandas. The only NumPy/Pandas arrays in which None can be used are those of data type "object," or arrays containing Python objects, as None is a Python object:

```
In[1]: import numpy as np
import pandas as pd
In[2]: vals1 = np.array([1, None, 3, 4])
vals1
Out[2]: array([1, None, 3, 4], dtype=object)
```
> The use of Python objects in an array also means that if you perform aggregations
like sum() or min() across an array with a None value, you will generally get an error:

```
In[4]: vals1.sum()
TypeError Traceback (most recent call last)
<ipython-input-4-749fd8ae6030> in <module>()
----> 1 vals1.sum()
/path here
30
31 def _sum(a, axis=None, dtype=None, out=None, keepdims=False):
---> 32 return umr_sum(a, axis, dtype, out, keepdims)
33
34 def _prod(a, axis=None, dtype=None, out=None, keepdims=False):
```
---
## NaN: Missing numerical data
The other missing data representation, NaN (acronym for Not a Number), is different;
it is a special floating-point value recognized by all systems that use the standard
IEEE floating-point representation:

```
In[5]: vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype
Out[5]: dtype('float64')
```

Notice that NumPy chose a native floating-point type for this array: this means that
unlike the object array from before, this array supports fast operations pushed into
compiled code. You should be aware that NaN is a bit like a data virus—it infects any
other object it touches. Regardless of the operation, the result of arithmetic with NaN
will be another NaN:

```
In[6]: 1 + np.nan
Out[6]: nan
In[7]: 0 * np.nan
Out[7]: nan
```
Note that this means that aggregates over the values are well defined (i.e., they don’t
result in an error) but not always useful:
```
In[8]: vals2.sum(), vals2.min(), vals2.max()
Out[8]: (nan, nan, nan)
```
NumPy does provide some special aggregations that will ignore these missing values:
```
In[9]: np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)
Out[9]: (8.0, 1.0, 4.0)
```
Keep in mind that NaN is specifically a floating-point value; there is no equivalent
NaN value for integers, strings, or other types.

---
## NaN and None in Pandas

NaN and None both have their place, and Pandas is built to handle the two of them
nearly interchangeably, converting between them where appropriate:
```
In[10]: pd.Series([1, np.nan, 2, None])
Out[10]: 0 1.0
         1 NaN
         2 2.0
         3 NaN
         dtype: float64
```
For types that don’t have an available sentinel value, Pandas automatically type-casts
when NA values are present. For example, if we set a value in an integer array to
np.nan, it will automatically be upcast to a floating-point type to accommodate the
NA:
```
In[11]: x = pd.Series(range(2), dtype=int)
        x
Out[11]: 0 0
         1 1
         dtype: int64
In[12]: x[0] = None
        x
Out[12]: 0 NaN
         1 1.0
         dtype: float64
```
Notice that in addition to casting the integer array to floating point, Pandas automati‐
cally converts the None to a NaN value. (Be aware that there is a proposal to add a
native integer NA to Pandas in the future; as of this writing, it has not been included.)

--- 
## Operating on Null Values
 Pandas treats None and NaN as essentially interchangeable for indi‐
cating missing or null values. To facilitate this convention, there are several useful
methods for detecting, removing, and replacing null values in Pandas data structures.
They are:

 isnull()
  > Generate a Boolean mask indicating missing values
 
 notnull()
  > Opposite of isnull()
 
 dropna()
  > Return a filtered version of the data

fillna()
  > Return a copy of the data with missing values filled or imputed

## Detecting null values
Pandas data structures have two useful methods for detecting null data: isnull() and
notnull(). Either one will return a Boolean mask over the data. For example:
```
In[13]: data = pd.Series([1, np.nan, 'hello', None])
In[14]: data.isnull()
Out[14]: 0 False
         1 True
         2 False
         3 True
         dtype: bool
```
```
In[15]: data[data.notnull()]
Out[15]: 0 1
         2 hello
         dtype: object
```
The isnull() and notnull() methods produce similar Boolean results for Data
Frames.

---

## Dropping null values
In addition to the masking used before, there are the convenience methods, dropna()
(which removes NA values) and fillna() (which fills in NA values). For a Series,
the result is straightforward:
```
In[16]: data.dropna()
Out[16]: 0 1
         2 hello
         dtype: object
```
For a DataFrame, there are more options. Consider the following DataFrame:
```
In[17]: df = pd.DataFrame([[1, np.nan, 2],
                            [2, 3, 5],
                          [np.nan, 4, 6]])
df
Out[17]: 0 1 2
         0 1.0 NaN 2
         1 2.0 3.0 5
         2 NaN 4.0 6
```
We cannot drop single values from a DataFrame; we can only drop full rows or full
columns. Depending on the application, you might want one or the other, so
dropna() gives a number of options for a DataFrame.
By default, dropna() will drop all rows in which any null value is present:
```
In[18]: df.dropna()
Out[18]: 0 1 2
         1 2.0 3.0 5
```
Alternatively, you can drop NA values along a different axis; axis=1 drops all col‐
umns containing a null value:
```
In[19]: df.dropna(axis='columns')
Out[19]: 2
         0 2
         1 5
         2 6
```
However, this also eliminates some useful data; you might be more interested in eliminating rows or columns that include either a majority of NA values or all NA values. The how and thresh parameters, which enable precise control over the quantity of nulls to permit through, can be used to specify this.
The default setting, how='any,' means that any row or column that contains a null value, depending on the axis key word, will be removed. Additionally, you can set how='all,' which will only remove rows and columns with all null values:

```
In[20]: df[3] = np.nan
        df
Out[20]: 0 1 2 3
         0 1.0 NaN 2 NaN
         1 2.0 3.0 5 NaN
         2 NaN 4.0 6 NaN
In[21]: df.dropna(axis='columns', how='all')
Out[21]: 0 1 2
         0 1.0 NaN 2
         1 2.0 3.0 5
         2 NaN 4.0 6
```
---
## Filling null values

Sometimes it makes more sense to substitute a valid value for NA values rather than discarding them. This value could be an interpolation or imputation from the good values, or it could be a single integer, such as zero. Although you could perform this in-place using a mask created by the isnull() method, given how frequently this process is done The fillna() method in Pandas generates a replica of the array with the null values swapped out.

Consider the following Series:
```
In[23]: data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
        data
Out[23]: a 1.0
         b NaN
         c 2.0
         d NaN
         e 3.0
         dtype: float64
```
We can fill NA entries with a single value, such as zero:
```
In[24]: data.fillna(0)
Out[24]: a 1.0
         b 0.0
         c 2.0
         d 0.0
         e 3.0
         dtype: float64
```
We can specify a forward-fill to propagate the previous value forward:
```
In[25]: # forward-fill
        data.fillna(method='ffill')
Out[25]: a 1.0
         b 1.0
         c 2.0
         d 2.0
         e 3.0
         dtype: float64
```
Or we can specify a back-fill to propagate the next values backward:
```
In[26]: # back-fill
        data.fillna(method='bfill')
Out[26]: a 1.0
         b 2.0
         c 2.0
         d 3.0
         e 3.0
         dtype: float64
```
For DataFrames, the options are similar, but we can also specify an axis along which
the fills take place:
```
In[27]: df
Out[27]: 0 1 2 3
         0 1.0 NaN 2 NaN
         1 2.0 3.0 5 NaN
         2 NaN 4.0 6 NaN
In[28]: df.fillna(method='ffill', axis=1)
Out[28]: 0 1 2 3
>
         0 1.0 1.0 2.0 2.0
         1 2.0 3.0 5.0 5.0
         2 NaN 4.0 6.0 6.0
```
Notice that if a previous value is not available during a forward fill, the NA value
remains.

> If any method is depreciated, you can Refer [Pandas Documentation](https://pandas.pydata.org/docs/) for updated code
