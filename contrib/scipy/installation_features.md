## Installation of Scipy

You can install scipy using the command:

```
$ pip install scipy
```

You can also use a Python distribution that already has Scipy installed like Anaconda, or Spyder.

### Importing SciPy

```python
from scipy import constants
```

## Key Features of SciPy
### 1. Numerical Integration

It helps in computing definite or indefinite integrals of functions

```python
from scipy import integrate

#Define the function to integrate
def f(x):
    return x**2

#Compute definite integral of f from 0 to 1
result, error = integrate.quad(f, 0, 1)
print(result)
```

#### Output

```
0.33333333333333337
```

### 2. Optimization

It can be used to minimize or maximize functions, here is an example of minimizing roots of an equation

```python
from scipy.optimize import minimize

# Define an objective function to minimize
def objective(x):
    return x**2 + 10*np.sin(x)

# Minimize the objective function starting from x=0
result = minimize(objective, x0=0)
print(result.x)
```

#### Output

```
array([-1.30644012])
```

### 3. Linear Algebra

Solving Linear computations

```python
from scipy import linalg
import numpy as np

# Define a square matrix
A = np.array([[1, 2], [3, 4]])

# Define a vector
b = np.array([5, 6])

# Solve Ax = b for x
x = linalg.solve(A, b)
print(x)
```

#### Output

```
array([-4. ,  4.5])
```

### 4. Statistics

Performing statistics functions, like here we'll be distributing the data

```python
from scipy import stats
import numpy as np

# Generate random data from a normal distribution
data = stats.norm.rvs(loc=0, scale=1, size=1000)

# Fit a normal distribution to the data
mean, std = stats.norm.fit(data)
```

### 5. Signal Processing

To process spectral signals, like EEG or MEG

```python
from scipy import signal
import numpy as np

# Create a signal (e.g., sine wave)
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(1000)

# Apply a low-pass Butterworth filter
b, a = signal.butter(4, 0.1, 'low')
filtered_signal = signal.filtfilt(b, a, signal)
```

The various filters applied that are applied here, are a part of signal analysis at a deeper level.

### 6. Sparse Matrix

The word ' sparse 'means less, i.e., the data is mostly unused during some operation or analysis. So, to handle this data, a Sparse Matrix is created

There are two types of Sparse Matrices:

1. CSC: Compressed Sparse Column, it is used for efficient math functions and for column slicing
2. CSR: Compressed Sparse Row, it is used for fast row slicing

#### In CSC format

```python
from scipy import sparse
import numpy as np

data = np.array([[0, 0], [0, 1], [2, 0]])

row_indices = np.array([1, 2, 1])  
col_indices = np.array([1, 0, 2])  
values = np.array([1, 2, 1])       

sparse_matrix_csc = sparse.csc_matrix((values, (row_indices, col_indices)))
```

#### In CSR format

```python
from scipy import sparse
import numpy as np

data = np.array([[0, 0], [0, 1], [2, 0]])
sparse_matrix = sparse.csr_matrix(data)
```

### 7. Image Processing

It is used to process the images, like changing dimensions or properties. For example, when you're doing a project on medical imaging, this library is mainly used.

```python
from scipy import ndimage
import matplotlib.pyplot as plt

image = plt.imread('path/to/image.jpg')
plt.imshow(image)
plt.show()

# Apply Gaussian blur to the image
blurred_image = ndimage.gaussian_filter(image, sigma=1)
plt.imshow(blurred_image)
plt.show()
```

The gaussian blur is one of the properties of the ' ndimage ' package in SciPy libraries, it used for better understanding of the image.
