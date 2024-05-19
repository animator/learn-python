# Loading Arrays From Files
The ability to load data from various file formats is a critical feature for scientific computing and data analysis. 
NumPy provides several functions to read data from different file types and convert them into ndarrays. 
This section will cover how to load ndarrays from common file formats, including CSV, TSV, and binary files.

### Here are the methods available:

`numpy.loadtxt`: The loadtxt function allows you to load data from a text file.You can specify various parameters such as the file name, data type, delimiter,
and more. It reads the file line by line, splits it at the specified delimiter, and converts the values into an array.

- **Syntax:**
  ```python
  numpy.loadtxt(fname, dtype = float, delimiter=None, converters=None, skiprows=0, usecols=None)
  ```

  `fname` : Name of the file <br>
  `dtype` : Data type of the resulting array. (By default is float) <br>
  `delimiter`: String or character separating columns; default is any whitespace. <br>
  `converters`: Dictionary mapping column number to a function to convert that column's string to a float. <br>
  `skiprows`: Number of lines to skip at the beginning of the file. <br>
  `usecols`: Which columns to read starting from 0.

- **Example for `loadtxt`:**

  **example.txt** <br>
  
  ![image](https://github.com/Santhosh-Siddhardha/learn-python/assets/103999924/a0148d29-5fba-45fa-b3f4-058406b3016b)

  **Code** <br>
  ```python
  import numpy as np 
  arr = np.loadtxt("loadtxt.txt", dtype=int) 
  print(arr) 
  ```

  **Output**<br>
  ```python
  [1 2 3 4 5]
  ```
  

`numpy.genfromtxt`:  The genfromtxt function is similar to loadtxt but provides more flexibility. It handles missing values (such as NaNs), allows custom converters
for data parsing, and can handle different data types within the same file. It’s particularly useful for handling complex data formats.

- **Syntax:**
  ```python
  numpy.genfromtxt(fname, dtype=float, delimiter=None, skip_header=0, skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=None)
  ```

  `fname` : Name of the file <br>
  `dtype` : Data type of the resulting array. (By default is float) <br>
  `delimiter`: String or character separating columns; default is any whitespace. <br>
  `skip_header`: Number of lines to skip at the beginning of the file.<br>
  `skip_footer`: Number of lines to skip at the end of the file.<br>
  `converters`: Dictionary mapping column number to a function to convert that column's string to a float. <br>
  `missing_values`: Set of strings corresponding to missing data.<br>
  `filling_values`: Value used to fill in missing data. Default is NaN.<br>
  `usecols`: Which columns to read starting from 0.

- **Examples for `genfromtxt`:**


`numpy.fromfile`: The fromfile function reads binary data directly from a file into a NumPy array. It doesn’t assume any specific format or delimiter;
instead, it interprets the raw binary data according to the specified data type.

`numpy.load`: Load arrays saved in NumPy’s native binary format (.npy or .npz). These files preserve the array structure, data types, and metadata.
It’s an efficient way to store and load large arrays.
