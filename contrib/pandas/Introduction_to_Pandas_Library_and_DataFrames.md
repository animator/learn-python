# Introduction_to_Pandas_Library_and_DataFrames

> Content Creator - Krishna Kaushik

**As you have learnt Python Programming , now it's time for some applications.**

- Machine Learning and Data Science is the emerging field of today's time , to work in this this field your first step should be `Data Science` as Machine Learning is all about data.
- To begin with Data Science your first tool will be `Pandas Library`.

## Introduction of Pandas Library

Pandas is a data analysis and manipulation tool, built on top of the python programming language. Pandas got its name from the term Panel data (‘Pa’ from Panel and ‘da’ from data). Panel data is a data which have rows and columns in it like excel spreadsheets, csv files etc.

**To use Pandas, first we’ve to import it.**

## Why pandas?

* Pandas provides a simple-to-use but very capable set of functions that you can use on your data.
* It is  also associate with other machine learning libraries , so it is important to learn it.

* For example - It is highly used to transform tha data which will be use by machine learning model during the training.


```python
# Importing the pandas
import pandas as pd
```

*To import any module in Python use “import 'module name' ” command, I used “pd” as pandas abbreviation because we don’t need to type pandas every time only type “pd” to use pandas.*


```python
# To check available pandas version
print(f"Pandas Version is : {pd.__version__}")
```

    Pandas Version is : 2.1.4
    

## Understanding Pandas data types

Pandas has two main data types : `Series` and `DataFrames`

* `pandas.Series` is a 1-dimensional column of data.
* `pandas.DataFrames` is 2 -dimensional data table having rows and columns.

### 1. Series datatype

**To creeate a series you can use `pd.Series()` and passing a python list inside()**.

Note: S in Series is capital if you use small s it will give you an error.

> Let's create a series



```python
# Creating a series of car companies
cars = pd.Series(["Honda","Audi","Thar","BMW"])
cars
```




    0    Honda
    1     Audi
    2     Thar
    3      BMW
    dtype: object



The above code creates a Series of cars companies the name of series is “cars” the code “pd.Series([“Honda” , “Audi” , “Thar”, "BMW"])” means Hey! pandas (pd) create a Series of cars named "Honda" , "Audi" , "Thar" and "BMW".

The default index of a series is 0,1,2….(Remember it starts from 0)

To change the index of any series set the “index” parameter accordingly. It takes the list of index values:


```python
cars = pd.Series(["Honda","Audi","Thar","BMW"],index = ["A" , "B" , "C" ,"D"])
cars
```




    A    Honda
    B     Audi
    C     Thar
    D      BMW
    dtype: object



You can see that the index has been changed from numbers to A, B ,C and D.

And the mentioned ‘dtype’ tells us about the type of data we have in the series.

### 2. DataFrames datatype

DataFrame contains rows and columns like a csv file have.

You can also create a DataFrame by using `pd.DataFrame()` and passing it a Python dictionary.


```python
# Let's create
cars_with_colours = pd.DataFrame({"Cars" : ["BMW","Audi","Thar","Honda"],
                                "Colour" : ["Black","White","Red","Green"]})
cars_with_colours
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cars</th>
      <th>Colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BMW</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Audi</td>
      <td>White</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Thar</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Honda</td>
      <td>Green</td>
    </tr>
  </tbody>
</table>
</div>



The dictionary key is the `column name` and value are the `column data`.

*You can also create a DataFrame with the help of series.*


```python
# Let's create two series
students = pd.Series(["Ram","Mohan","Krishna","Shivam"])
age = pd.Series([19,20,21,24])

students
```




    0        Ram
    1      Mohan
    2    Krishna
    3     Shivam
    dtype: object




```python
age
```




    0    19
    1    20
    2    21
    3    24
    dtype: int64




```python
# Now let's create a dataframe with the help of above series
# pass the series name to the dictionary value

record = pd.DataFrame({"Student_Name":students , 
                      "Age" :age})
record
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student_Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ram</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mohan</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Krishna</td>
      <td>21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Shivam</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To print the list of columns names
record.columns
```




    Index(['Student_Name', 'Age'], dtype='object')



### Describe Data 

**The good news is that pandas has many built-in functions which allow you to quickly get information about a DataFrame.**
Let's explore the `record` dataframe

#### 1. Use `.dtypes` to find what datatype a column contains


```python
record.dtypes
```




    Student_Name    object
    Age              int64
    dtype: object



#### 2. use `.describe()` for statistical overview.


```python
record.describe()  # It only display the results for numeric data
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>21.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2.160247</td>
    </tr>
    <tr>
      <th>min</th>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>21.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>24.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. Use `.info()` to find information about the dataframe


```python
record.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3
    Data columns (total 2 columns):
     #   Column        Non-Null Count  Dtype 
    ---  ------        --------------  ----- 
     0   Student_Name  4 non-null      object
     1   Age           4 non-null      int64 
    dtypes: int64(1), object(1)
    memory usage: 196.0+ bytes
    


```python

```
