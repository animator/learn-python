# Loading Arrays From Files
Scientific computing and data analysis require the critical feature of being able to load data from different file formats. NumPy has several functionalities for reading data from various file types and converting them into arrays. This part of the content will show how one can load arrays from standard file formats.

## Here are the methods available:

### 1. numpy.loadtxt(): 
The `loadtxt` function allows you to load data from a text file.You can specify various parameters such as the file name, data type, delimiter,
and more. It reads the file line by line, splits it at the specified delimiter, and converts the values into an array.

- #### Syntax:
  ```python
  numpy.loadtxt(fname, dtype = float, delimiter=None, converters=None, skiprows=0, usecols=None)
  ```

  **fname** : Name of the file <br>
  **dtype** : Data type of the resulting array. (By default is float) <br>
  **delimiter**: String or character separating columns. (By default is whitespace) <br>
  **converters**: Dictionary mapping column number to a function to convert that column's string to a float. <br>
  **skiprows**: Number of lines to skip at the beginning of the file. <br>
  **usecols**: Which columns to read starting from 0.

- #### Example for `loadtxt`:

  **example.txt** <br>
  
  ![image](https://github.com/Santhosh-Siddhardha/learn-python/assets/103999924/a0148d29-5fba-45fa-b3f4-058406b3016b)

  **Code** <br>
  ```python
  import numpy as np
  
  arr = np.loadtxt("example.txt", dtype=int) 
  print(arr) 
  ```

  **Output**<br>
  ```python
  [1 2 3 4 5]
  ```
  
<br>

### 2. numpy.genfromtxt():  
The `genfromtxt` function is similar to loadtxt but provides more flexibility. It handles missing values (such as NaNs), allows custom converters
for data parsing, and can handle different data types within the same file. It’s particularly useful for handling complex data formats.

- #### Syntax:
  ```python
  numpy.genfromtxt(fname, dtype=float, delimiter=None, converters=None, missing_values=None, filling_values=None, usecols=None)
  ```

  **fname** : Name of the file <br>
  **dtype** : Data type of the resulting array. (By default is float) <br>
  **delimiter**: String or character separating columns; default is any whitespace. <br>
  **converters**: Dictionary mapping column number to a function to convert that column's string to a float. <br>
  **missing_values**: Set of strings corresponding to missing data.<br>
  **filling_values**: Value used to fill in missing data. Default is NaN.<br>
  **usecols**: Which columns to read starting from 0.

- #### Example for `genfromtxt`:

   **example.txt** <br>
  
  ![image](https://github.com/Santhosh-Siddhardha/learn-python/assets/103999924/3f9cdd91-4255-4e30-923d-f29c5f237798)


  **Code** <br>
  ```python
  import numpy as np
  
  arr = np.genfromtxt("example.txt", dtype='str', usecols=1) 
  print(arr) 
  ```

  **Output**<br>
  ```python
  ['Name' 'Kohli' 'Dhoni' 'Rohit']
  ```
  
<br>


### 3. numpy.load():
`load` method is used to load arrays saved in NumPy’s native binary format (.npy or .npz). These files preserve the array structure, data types, and metadata.
It’s an efficient way to store and load large arrays.

- #### Syntax:
  ```python
  numpy.load(fname, mmap_mode=None, encoding='ASCII')
  ```

  **fname** : Name of the file <br>
  **mmap_mode** : Memory-map the file using the given mode (r, r+, w+, c)(By Default None).Memory-mapping only works with arrays stored in a binary file on disk, not with compressed archives like .npz.<br>
  **encoding**:Encoding is used when reading Python2 strings only. (By Default ASCII) <br>

- #### Example for `load`:

  **Code** <br>
  ```python
  import numpy as np
  
  arr = np.array(['a','b','c'])
  np.savez('example.npz', array=arr)  # stores arr in data.npz in NumPy's native binary format
 
  data = np.load('example.npz')
  print(data['array'])
  ```

  **Output**<br>
  ```python
  ['a' 'b' 'c']
  ```
<br>

These methods empower users to seamlessly integrate data into their scientific workflows, whether from text files or binary formats.
