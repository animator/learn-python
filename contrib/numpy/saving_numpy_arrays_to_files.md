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
