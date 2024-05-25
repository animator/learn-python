# Importing_and_Exporting_Data_in_Pandas

>Created by Krishna Kaushik

- **Now we're able to create `Series` and `DataFrames` in pandas, but we usually do not do this , in practice we import the data which is in the form of .csv (Comma Seperated Values) , a spreadsheet file or something similar.**

- *Good news is that pandas allows for easy importing of data like this through functions such as ``pd.read_csv()`` and ``pd.read_excel()`` for Microsoft Excel files.*

## 1. Importing from a Google sheet to a pandas dataframe

*Let's say that you wanted to get the information from Google Sheet document into a pandas DataFrame.*.

*You could export it as a .csv file and then import it using ``pd.read_csv()``.*

*In this case, the exported .csv file is called `Titanic.csv`*


```python
## Importing Titanic Data set 
import pandas as pd

titanic_df= pd.read_csv("https://raw.githubusercontent.com/kRiShNa-429407/learn-python/main/contrib/pandas/Datasets/Titanic.csv")
print(titanic_df)
```

          pclass  survived                                             name  \
    0          1         1                    Allen, Miss. Elisabeth Walton   
    1          1         1                   Allison, Master. Hudson Trevor   
    2          1         0                     Allison, Miss. Helen Loraine   
    3          1         0             Allison, Mr. Hudson Joshua Creighton   
    4          1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)   
    ...      ...       ...                                              ...   
    1304       3         0                             Zabour, Miss. Hileni   
    1305       3         0                            Zabour, Miss. Thamine   
    1306       3         0                        Zakarian, Mr. Mapriededer   
    1307       3         0                              Zakarian, Mr. Ortin   
    1308       3         0                               Zimmerman, Mr. Leo   
    
             sex    age  sibsp  parch  ticket      fare    cabin embarked boat  \
    0     female  29.00      0      0   24160  211.3375       B5        S    2   
    1       male   0.92      1      2  113781  151.5500  C22 C26        S   11   
    2     female   2.00      1      2  113781  151.5500  C22 C26        S  NaN   
    3       male  30.00      1      2  113781  151.5500  C22 C26        S  NaN   
    4     female  25.00      1      2  113781  151.5500  C22 C26        S  NaN   
    ...      ...    ...    ...    ...     ...       ...      ...      ...  ...   
    1304  female  14.50      1      0    2665   14.4542      NaN        C  NaN   
    1305  female    NaN      1      0    2665   14.4542      NaN        C  NaN   
    1306    male  26.50      0      0    2656    7.2250      NaN        C  NaN   
    1307    male  27.00      0      0    2670    7.2250      NaN        C  NaN   
    1308    male  29.00      0      0  315082    7.8750      NaN        S  NaN   
    
           body                        home.dest  
    0       NaN                     St Louis, MO  
    1       NaN  Montreal, PQ / Chesterville, ON  
    2       NaN  Montreal, PQ / Chesterville, ON  
    3     135.0  Montreal, PQ / Chesterville, ON  
    4       NaN  Montreal, PQ / Chesterville, ON  
    ...     ...                              ...  
    1304  328.0                              NaN  
    1305    NaN                              NaN  
    1306  304.0                              NaN  
    1307    NaN                              NaN  
    1308    NaN                              NaN  
    
    [1309 rows x 14 columns]
    

The dataset I am using here for your reference is taken from the same repository i.e ``learn-python`` (https://raw.githubusercontent.com/kRiShNa-429407/learn-python/main/contrib/pandas/Datasets/Titanic.csv) I uploaded it in the Datasets folder,you can use it from there.

You can also place the filename with its path in `pd.read_csv()`.

**Now we've got the same data from the Google Spreadsheet , but now available as ``pandas DataFrame`` which means we can now apply all pandas functionality over it.**

#### Note: The quiet important thing i am telling is that ``pd.read_csv()`` takes the location of the file (which is in your current working directory) or the hyperlink of the dataset from the other source.

#### But if you want to import the data from Github you can't directly use its link , you have to first convert it to raw by clicking on the raw button present in the repo .

#### Also you can't use the data directly from `Kaggle` you have to use ``kaggle API``

## 2. The Anatomy of DataFrame

**Different functions use different labels for different things, and can get a little confusing.**

- Rows are refer as ``axis=0``
- columns are refer as ``axis=1``

## 3. Exporting Data

**OK, so after you've made a few changes to your data, you might want to export it and save it so someone else can access the changes.**

**pandas allows you to export ``DataFrame's`` to ``.csv`` format using ``.to_csv()``, or to a spreadsheet format using .to_excel().**

### Exporting a dataframe to a CSV

**We haven't made any changes yet to the ``titanic_df`` DataFrame but let's try to export it.**


```python
#Export the titanic_df DataFrame to csv
titanic_df.to_csv("exported_titanic.csv")  
```

Running this will save a file called ``exported_titanic.csv`` to the current folder.
