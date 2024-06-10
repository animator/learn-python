# Statistical Operations on Arrays

Statistics involves collecting data, analyzing it, and drawing conclusions from the gathered information.

NumPy provides powerful statistical functions to perform efficient data analysis on arrays, including `minimum`, `maximum`, `mean`, `median`, `variance`, `standard deviation`, and more.

## Minimum

In NumPy, the minimum value of an array is the smallest element present.

The smallest element of an array is calculated using the `np.min()` function.

**Code**
```python
import numpy as np
array = np.array([100,20,300,400])
#Calculating the minimum
result = np.min(array)
print("Minimum :", result)
```

**Output**
```
Minimum : 20
```

## Maximum

In NumPy, the maximum value of an array is the largest element present.

The largest element of an array is calculated using the `np.max()` function.

**Code**
```python
import numpy as np
array = np.array([100,20,300,400])
#Calculating the maximum
result = np.max(array)
print("Maximum :", result)
```

**Output**
```
Maximum : 400
```

## Mean

The mean value of a NumPy array is the average of all its elements.

It is calculated by summing all the elements and then dividing by the total number of elements.

The mean of an array is calculated using the `np.mean()` function.

**Code**
```python
import numpy as np
array = np.array([10,20,30,40])
#Calculating the mean
result = np.mean(array)
print("Mean :", result)
```

**Output**
```
Mean : 25.0
```

## Median

The median value of a NumPy array is the middle value in a sorted array.

It separates the higher half of the data from the lower half.

The median of an array is calculated using the `np.median()` function.

It is important to note that:

- If the number of elements is `odd`, the median is the middle element.
- If the number of elements is `even`, the median is the average of the two middle elements.

**Code**
```python
import numpy as np
#The number of elements is odd
array = np.array([5,6,7,8,9])
#Calculating the median
result = np.median(array)
print("Median :", result)
```

**Output**
```
Median : 7.0
```

**Code**
```python
import numpy as np
#The number of elements is even
array = np.array([1,2,3,4,5,6])
#Calculating the median
result = np.median(array)
print("Median :", result)
```

**Output**
```
Median : 3.5
```

## Variance

Variance in a NumPy array measures the spread or dispersion of data points.

Calculated as the average of the squared differences from the mean.

The variance of an array is calculated using the `np.var()` function.

**Code**
```python
import numpy as np
array = np.array([10,70,80,50,30])
#Calculating the variance
result = np.var(array)
print("Variance :", result)
```

**Output**
```
Variance : 656.0
```

## Standard Deviation

The standard deviation of a NumPy array measures the amount of variation or dispersion of the elements in the array.

It is calculated as the square root of the average of the squared differences from the mean, providing insight into how spread out the values are around the mean.

The standard deviation of an array is calculated using the `np.std()` function.

**Code**
```python
import numpy as np
array = np.array([25,30,40,55,75,100])
#Calculating the standard deviation
result = np.std(array)
print("Standard Deviation :", result)
```

**Output**
```
Standard Deviation : 26.365486699260625
```
