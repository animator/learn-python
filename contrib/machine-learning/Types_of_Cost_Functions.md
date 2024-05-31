
# Cost Functions in Machine Learning

Cost functions, also known as loss functions, play a crucial role in training machine learning models. They measure how well the model performs on the training data by quantifying the difference between predicted and actual values. Different types of cost functions are used depending on the problem domain and the nature of the data.

## Types of Cost Functions

### 1. Mean Squared Error (MSE)

**Explanation:**
MSE is one of the most commonly used cost functions, particularly in regression problems. It calculates the average squared difference between the predicted and actual values.

**Mathematical Formulation:**
The MSE is defined as:
$$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
Where:
- \( n \) is the number of samples.
- \( y_i \) is the actual value.
- \( y^i\) is the predicted value.

**Advantages:**
- Sensitive to large errors due to squaring.
- Differentiable and convex, facilitating optimization.

**Disadvantages:**
- Sensitive to outliers, as the squared term amplifies their impact.

**Python Implementation:**
```python
import numpy as np

def mean_squared_error(y_true, y_pred):
    n = len(y_true)
    return np.mean((y_true - y_pred) ** 2)
```

### 2. Mean Absolute Error (MAE)

**Explanation:**
MAE is another commonly used cost function for regression tasks. It measures the average absolute difference between predicted and actual values.

**Mathematical Formulation:**
The MAE is defined as:
$$ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$
Where:
- \( n \) is the number of samples.
- \( y_i \) is the actual value.
- \( y^i\) is the predicted value.

**Advantages:**
- Less sensitive to outliers compared to MSE.
- Provides a linear error term, which can be easier to interpret.


**Disadvantages:**
- Not differentiable at zero, which can complicate optimization.

**Python Implementation:**
```python
import numpy as np

def mean_absolute_error(y_true, y_pred):
    n = len(y_true)
    return np.mean(np.abs(y_true - y_pred))
```

### 3. Cross-Entropy Loss (Binary)

**Explanation:**
Cross-entropy loss is commonly used in binary classification problems. It measures the dissimilarity between the true and predicted probability distributions.

**Mathematical Formulation:**
For binary classification, the cross-entropy loss is defined as:
$$ \text{Cross-Entropy} = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$
Where:
- \( n \) is the number of samples.
- \( y_i \) is the actual class label (0 or 1).
- \( y^i\)  is the predicted probability of the positive class.


**Advantages:**
- Penalizes confident wrong predictions heavily.
- Suitable for probabilistic outputs.

**Disadvantages:**
- Sensitive to class imbalance.

**Python Implementation:**
```python
import numpy as np

def binary_cross_entropy(y_true, y_pred):
    n = len(y_true)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
```

### 4. Cross-Entropy Loss (Multiclass)

**Explanation:**
For multiclass classification problems, the cross-entropy loss is adapted to handle multiple classes.

**Mathematical Formulation:**
The multiclass cross-entropy loss is defined as:
$$ \text{Cross-Entropy} = -\frac{1}{n} \sum_{i=1}^{n} \sum_{c=1}^{C} y_{i,c} \log(\hat{y}_{i,c}) $$
Where:
- \( n \) is the number of samples.
- \( C \) is the number of classes.
- \( y_{i,c} \) is the indicator function for the true class of sample \( i \).

- (y^i,c) is the predicted probability of sample \( i \) belonging to class \( c \).

**Advantages:**
- Handles multiple classes effectively.
- Encourages the model to assign high probabilities to the correct classes.

**Disadvantages:**
- Requires one-hot encoding for class labels, which can increase computational complexity.

**Python Implementation:**
```python
import numpy as np

def categorical_cross_entropy(y_true, y_pred):
    n = len(y_true)
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
```

### 5. Hinge Loss (SVM)

**Explanation:**
Hinge loss is commonly used in support vector machines (SVMs) for binary classification tasks. It penalizes misclassifications by a linear margin.

**Mathematical Formulation:**
For binary classification, the hinge loss is defined as:
$$ \text{Hinge Loss} = \frac{1}{n} \sum_{i=1}^{n} \max(0, 1 - y_i \cdot \hat{y}_i) $$
Where:
- \( n \) is the number of samples.
- \( y_i \) is the actual class label (-1 or 1).
- \( \hat{y}_i \) is the predicted score for sample \( i \).

**Advantages:**
- Encourages margin maximization in SVMs.
- Robust to outliers due to the linear penalty.

**Disadvantages:**
- Not differentiable at the margin, which can complicate optimization.

**Python Implementation:**
```python
import numpy as np

def hinge_loss(y_true, y_pred):
    n = len(y_true)
    loss = np.maximum(0, 1 - y_true * y_pred)
    return np.mean(loss)
```

### 6. Huber Loss

**Explanation:**
Huber loss is a combination of MSE and MAE, providing a compromise between the two. It is less sensitive to outliers than MSE and provides a smooth transition to MAE for large errors.

**Mathematical Formulation:**

The Huber loss is defined as:


$$
\text{Huber Loss} = \frac{1}{n} \sum_{i=1}^{n} \left\{
\begin{array}{ll}
\frac{1}{2} (y_i - \hat{y}_i)^2 & \text{if } |y_i - \hat{y}_i| \leq \delta \\
\delta(|y_i - \hat{y}_i| - \frac{1}{2} \delta) & \text{otherwise}
\end{array}
\right.
$$
Where:
- \( n \) is the number of samples.
- \( \delta \) is a threshold parameter.

**Advantages:**
- Provides a smooth loss function.
- Less sensitive to outliers than MSE.

**Disadvantages:**
- Requires tuning of the threshold parameter.

**Python Implementation:**
```python
import numpy as np

def huber_loss(y_true, y_pred, delta):
    error = y_true - y_pred
    loss = np.where(np.abs(error) <= delta, 0.5 * error ** 2, delta * (np.abs(error) - 0.5 * delta))
    return np.mean(loss)
```

### 7. Log-Cosh Loss

**Explanation:**
Log-Cosh loss is a smooth approximation of the MAE and is less sensitive to outliers than MSE. It provides a smooth transition from quadratic for small errors to linear for large errors.

**Mathematical Formulation:**
The Log-Cosh loss is defined as:
$$ \text{Log-Cosh Loss} = \frac{1}{n} \sum_{i=1}^{n} \log(\cosh(y_i - \hat{y}_i)) $$
Where:
- \( n \) is the number of samples.

**Advantages:**
- Smooth and differentiable everywhere.
- Less sensitive to outliers.

**Disadvantages:**
- Computationally more expensive than simple losses like MSE.

**Python Implementation:**
```python
import numpy as np

def logcosh_loss(y_true, y_pred):
    error = y_true - y_pred
    loss = np.log(np.cosh(error))
    return np.mean(loss)
```

These implementations provide various options for cost functions suitable for different machine learning tasks. Each function has its advantages and disadvantages, making them suitable for different scenarios and problem domains.

--- 