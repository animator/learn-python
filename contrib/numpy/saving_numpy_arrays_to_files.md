# Saving NumPy Arrays to Files

- Saving arrays in NumPy is important due to its efficiency in storage and speed, maintaining data integrity and precision, and offering convenience and interoperability.
- NumPy provides several methods to save arrays efficiently, either in binary or text formats.
- The primary methods are `save`, `savez`, and `savetxt`.

### 1. numpy.save():

The `np.save` function saves a single NumPy array to a binary file with a `.npy` extension. This format is efficient and preserves the array's data type and shape.

#### Syntax :

  ```python
  numpy.save(file, arr, allow_pickle=True, fix_imports=True)
  ```
- **file** : Name of the file.
- **arr** : Array to be saved.
- **allow_pickle** : This is an Optional parameter, Allows saving object arrays using Python pickles.(By Default True)
- **fix_imports** : This is an Optional parameter, Fixes issues for Python 2 to Python 3 compatibility.(By Default True)

#### Example :

```python
import numpy as np

arr = np.array([1,2,3,4,5])
np.save("example.npy",arr) #saves arr into example.npy file in binary format
```

Inorder to load the array from example.npy

```python
arr1 = np.load("example.npy")
print(arr1)
```
**Output** :
  
```python
[1,2,3,4,5]
```
### 2. numpy.savez():

The `np.savez` function saves multiple NumPy arrays into a single file with a `.npz` extension. Each array is stored with a unique name.

#### Syntax :

  ```python
numpy.savez(file, *args, **kwds)
  ```
- **file** : Name of the file.
- **args** : Arrays to be saved.( If arrays are unnamed, they are stored with default names like arr_0, arr_1, etc.)
- **kwds** : Named arrays to be saved.

#### Example :

```python
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array(['a','b','c','d'])
arr3 = np.array([1.2,3.4,5])
np.savez('example.npz', a1=arr1, a2=arr2, a3 = arr3) #saves arrays in npz format

```

Inorder to load the array from example.npz

```python

arr = np.load('example.npz')
print(arr['a1'])
print(arr['a2'])
print(arr['a3'])

```
**Output** :
```python
[1 2 3 4 5]
['a' 'b' 'c' 'd']
[1.2 3.4 5. ]
```

### 3. np.savetxt()

The `np.savetxt` function saves a NumPy array to a text file, such as `.txt` or `.csv`. This format is human-readable and can be used for interoperability with other tools.

#### Syntax :

  ```python
numpy.savetxt(fname, X, delimiter=' ', newline='\n', header='', footer='', encoding=None)
  ```
- **fname** : Name of the file.
- **X** : Array to be saved.
- **delimiter** : It is a Optional parameter,This is a character or string that is used to separate columns.(By Default it is " ")
- **newline** : It is a Optional parameter, Character for seperating lines.(By Default it is "\n")
- **header** : It is a Optional parameter, String that is written at beginning of the file.
- **footer** : It is a Optional parameter, String that is written at ending of the file.
- **encoding** : It is a Optional parameter, Encoding of the output file. (By Default it is None)

#### Example :

```python
import numpy as np

arr = np.array([1.1,2.2,3,4.4,5])
np.savetxt("example.txt",arr) #saves the array in example.txt

```

Inorder to load the array from example.txt

```python

arr1 = np.loadtxt("example.txt")
print(arr1)

```
**Output** :
```python
[1.1 2.2 3. 4.4 5. ]
```


By using these methods, you can efficiently save and load NumPy arrays in various formats suitable for your needs.


