# STATISTICAL OPERATIONS ON ARRAYS

NumPy library can be used to perform wide range of statistical operations on arrays. This statistical operations plays a major role in data analysis and machine learning. It majorly helps people in extracting data and analysing it.
The statistical operations using NumPy includes mean, median,finding minimum and maximum element, percentile,variance and standard deviation. 

- Below is the illustration of performing statistical operations on a given array.
```
# creating an array
#Aliasing numpy
import numpy as np
arr = np.array([ 1, 2, 3, 4, 5])
```
     
-  **Median Using NumPy**
   ```
   median = np.median(arr)
   print (median)
   # Output 3.0
    ```

- **Mean Using NumPy**
  ```
  mean = np.mean(arr)
  print (mean)
  # Output 3.0
  ```
- **Percentile Using NumPy**
  ```
  perc = numpy.percentile(arr, 75)
  print (perc)
  # Output 4.0
  ```

- **Min Element Using NumPy**
  ```
  min_val = np.min(arr)
  print(min_val)
  # Output 1
  ```
- **Max Element Using NumPy**
  ```
  max_val = np.max(arr)
  print(max_val)
  # Output 5
   ```
- **Variance Using NumPy**
  ```
  variance = np.var(arr)
  print(variance)
  # Output 2.0
  ```
- **Standard Deviation Using NumPy**
  ```
  std_arr = np.std(arr)
  print(std_arr)
  # Output 1.4142135623730951
  ```

