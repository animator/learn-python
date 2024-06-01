# View the top rows of the frame 

**Pandas Dataframe/Series.head() method**:

 The pandas library in Python provides a convenient method called head() that allows you to view the first few rows of a DataFrame. Let me explain how it works:
* The head() function returns the first n rows of a DataFrame or Series.
* By default, it displays the first 5 rows, but you can specify a different number of rows using the n parameter.

**Syntax**:

     dataframe.head(n)
     
 n is the Optional value. The number of rows to return. Default value is 5.

**Example** :
  
     import pandas as pd
     df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion','tiger','rabit','dog','fox','monkey','elephant']})
     df.head(n=5)

**Output**:

'alligator',
'bee', 
'falcon', 
'lion',
'tiger'
# View the bottom rows of the frame 

**Pandas Dataframe/Series.tail() method**:

The tail function in Python displays the last five rows of the dataframe by default. It takes in a single parameter: the number of rows. We can use this parameter to display the number of rows of our choice.
* The tail() function returns the last n rows of a DataFrame or Series.
* By default, it displays the last 5 rows, but you can specify a different number of rows using the n parameter.

**Syntax**:

     dataframe.tail(n)
     
 n is the Optional value. The number of rows to return. Default value is 5.

 **Example** :
  
     import pandas as pd
     df = pd.DataFrame({'fruits': ['mongo', 'orange', 'apple', 'lemon','banana','water melon','papaya','grapes','cherry','coconut']})
     df.tail(n=5)

**Output**:


'water melon',
'papaya',
'grapes',
'cherry',
'coconut'
# View basic statistical details

**Pandas DataFrame describe() Method**:

Pandas describe() is used to view some basic statistical details like percentile, mean, std, etc. of a data frame or a series of numeric values.Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.

Analyzes both numeric and object series, as well as DataFrame column sets of mixed data types.The output will vary depending on what is provided.

**Syntax**:

    DataFrame.describe(percentiles=None, include=None, exclude=None)
**percentiles** : list-like of numbers, optional

The percentiles to include in the output. All should fall between 0 and 1. The default is [.25, .5, .75], which returns the 25th, 50th, and 75th percentiles. 

**include** :‘all’, list-like of dtypes or None (default), optional

A  list of data types to include in the result. 
* all’ : All columns of the input will be included in the output.

* A list-like of dtypes : Limits the results to the provided data types. To limit the result to numeric types submit numpy.number. To select pandas categorical columns, use 'category'

* None (default) : The result will include all numeric columns.

**exclude** : list-like of dtypes or None (default), optional.

A black list of data types to omit from the result. 
* A list-like of dtypes : Excludes the provided data types from the result. To exclude numeric types submit numpy.number. To exclude object columns submit the data type numpy.object.

* None (default) : The result will exclude nothing.

**Example** :

Describing a numeric Series.

        import pandas as pd
        s = pd.Series([1, 2, 3])
        s.describe()
        
**Output** :

count    3.0

mean     2.0

std      1.0

min      1.0

25%      1.5

50%      2.0

75%      2.5

max      3.0

dtype: float64

**Example** :

Describing a categorical Series.


         import pandas as pd
         s = pd.Series(['a', 'a', 'b', 'c'])
         s.describe()

**Output** :

count     4

unique    3

top       a

freq      2

dtype: object


        

      









  
     
