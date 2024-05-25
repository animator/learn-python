# Importing_and_Exporting_Data_in_Pandas

>Created by Krishna Kaushik

- **Now we're able to create `Series` and `DataFrames` in pandas, but we usually do not do this , in practice we import the data which is in the form of .csv (Comma Seperated Values) , a spreadsheet file or something similar.**

- *Good news is that pandas allows for easy importing of data like this through functions such as ``pd.read_csv()`` and ``pd.read_excel()`` for Microsoft Excel files.*

## 1. Importing from a Google sheet to a pandas dataframe

*Let's say that you wanted to get the information from Google Sheet document into a pandas DataFrame.*.

*You could export it as a .csv file and then import it using ``pd.read_csv()``.*

*In this case, the exported .csv file is called `car-sales.csv`*


```python
## Importing Titanic Data set 
import pandas as pd

car_sales_df= pd.read_csv("https://raw.githubusercontent.com/kRiShNa-429407/learn-python/main/contrib/pandas/Datasets/car-sales.csv")
print(car_sales_df)
```

         Make Colour  Odometer (KM)  Doors       Price
    0  Toyota  White         150043      4   $4,000.00
    1   Honda    Red          87899      4   $5,000.00
    2  Toyota   Blue          32549      3   $7,000.00
    3     BMW  Black          11179      5  $22,000.00
    4  Nissan  White         213095      4   $3,500.00
    5  Toyota  Green          99213      4   $4,500.00
    6   Honda   Blue          45698      4   $7,500.00
    7   Honda   Blue          54738      4   $7,000.00
    8  Toyota  White          60000      4   $6,250.00
    9  Nissan  White          31600      4   $9,700.00
    

The dataset I am using here for your reference is taken from the same repository i.e ``learn-python`` (https://raw.githubusercontent.com/kRiShNa-429407/learn-python/main/contrib/pandas/Datasets/car-sales.csv) I uploaded it in the Datasets folder,you can use it from there.

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

**We haven't made any changes yet to the ``car_sales_df`` DataFrame but let's try to export it.**


```python
#Export the titanic_df DataFrame to csv
car_sales_df.to_csv("exported_car_sales_df.csv")  
```

Running this will save a file called ``exported_titanic.csv`` to the current folder.
