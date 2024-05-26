# Indexing Arrays 
  There are mainly three types of indexing.
  - Basic Indexing 
  - Fancy Indexing
  - Boolean Indexing
  
### Basic Indexing 
  Basic indexing is accessing an element of an array by its index number. The indexes start from 0.

  **Example 1**<br>
  ```python
  import numpy as np 
  arr = np.array([10, 20, 30, 40, 50]) 
  print(arr[0])  
  ```
  **Output**<br>
  ```python
  10  #accessing the first element.
  ```
<br>

  **Example 2**<br>
   ```python
  import numpy as np 
  arr = np.array([10, 20, 30, 40, 50]) 
  print(arr[-1]) 
   ``` 
  **Output**<br>
  ```python
  50  #accessing the first element from the other end of the array.
  ```
<br>

**Example 3**<br>
  ```python
 import numpy as np
 arr = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
 print(arr[0, 1]) 
```
**Output**<br>
  ```python
  2  #accessing the element from the first row, second column.
  ```
<br>

**Example 4** <br>
```python
 import numpy as np
 arr = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
 print(arr[-1, -1])
```
**Output**<br>
  ```python
9  #accessing the element from the last row, last column.
```
<br>

### Fancy Indexing
Fancy indexing is where elements of an array are accessed by another array of indices.

**Example 5**<br>
   ```python
  import numpy as np 
  arr = np.array([10, 20, 30, 40, 50]) 
  print(arr[[0, 2, 4]])
   ``` 
**Output** 
```python
[10, 30, 50]
 ```
<br>

### Boolean Indexing
Boolean indexing is the indexing where we select the elements by their actual value instead of indexes.

**Example 6**<br>
 ```python
  import numpy as np 
  arr = np.array([10, 20, 30, 40, 50])
  print(arr[arr > 25])
```  
**Output** 
```python
[30 40 50]
``` 

