# Importing and Exporting Data in Pandas

## Importing Data from a CSV

We can create `Series` and `DataFrame` in pandas, but often we have to import the data which is in the form of `.csv` (Comma Separated Values), a spreadsheet file or similar tabular data file format.

`pandas` allows for easy importing of this data using functions such as `read_csv()` and `read_excel()` for Microsoft Excel files.

*Note: In case you want to get the information from a **Google Sheet** you can export it as a .csv file.*

The `read_csv()` function can be used to import a CSV file into a pandas DataFrame. The path can be a file system path or a URL where the CSV is available.

```python
import pandas as pd

car_sales_df= pd.read_csv("Datasets/car-sales.csv")
print(car_sales_df)
```

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
```    

You can find the dataset used above in the `Datasets` folder.

*Note: If you want to import the data from Github you can't directly use its link, you have to first obtain the raw file URL by clicking on the raw button present in the repo*

## Exporting Data to a CSV

`pandas` allows you to export `DataFrame` to `.csv` format using `.to_csv()`, or to a Excel spreadsheet using `.to_excel()`.

```python
car_sales_df.to_csv("exported_car_sales.csv")  
```

Running this will save a file called ``exported_car_sales.csv`` to the current folder.
