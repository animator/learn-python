# Gradient Descent in Machine Learning

## Introduction

Gradient Descent is an optimization algorithm used to minimize the cost function in various machine learning algorithms. It is essential for training models, especially in linear regression, logistic regression, and neural networks.

## Algorithm

### Basic Idea

The core idea of Gradient Descent is to move in the direction of the steepest descent as defined by the negative of the gradient. Starting from an initial set of parameters, the algorithm iteratively updates them to minimize the cost function.

### Steps of the Algorithm

1. **Initialize Parameters**: Start with initial guesses for the parameters.
2. **Compute the Gradient**: Calculate the gradient of the cost function with respect to each parameter.
3. **Update Parameters**: Adjust the parameters in the opposite direction of the gradient.
4. **Repeat**: Iterate steps 2 and 3 until convergence.

### Mathematical Formulation

For a parameter \( \theta \):

\[ \theta := \theta - \alpha \frac{\partial J(\theta)}{\partial \theta} \]

Where:
- \( \theta \) is the parameter.
- \( \alpha \) is the learning rate.
- \( J(\theta) \) is the cost function.

## Hyperparameters

### Learning Rate (\( \alpha \))

The learning rate determines the size of the steps taken towards the minimum. 

### Number of Iterations

This is the number of times the algorithm will update the parameters.

### Batch Size

In batch gradient descent, the entire dataset is used to compute the gradient. In stochastic gradient descent, each iteration uses a single data point. Mini-batch gradient descent uses a subset of data points.

### Regularization Parameter

This parameter is used to prevent overfitting by adding a penalty to the cost function based on the size of the parameters.

## Advantages and Disadvantages

### Advantages

- **Simplicity**: Easy to understand and implement.
- **Efficiency**: Suitable for large datasets and high-dimensional spaces.
- **Flexibility**: Can be used with various types of models and cost functions.

### Disadvantages

- **Local Minima**: May get stuck in local minima instead of finding the global minimum.
- **Choice of Learning Rate**: Requires careful tuning of the learning rate.
- **Convergence Issues**: May converge slowly or not at all if poorly initialized or if the learning rate is not optimal.

## Scikit-Learn Example

Gradient Descent using Scikit-learn with a linear regression model.

```python
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the SGDRegressor model
sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3)
sgd_reg.fit(X_train, y_train.ravel())

# Predict and evaluate the model
y_pred = sgd_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Output: Mean Squared Error: <some_value>
```

## Custom Gradient Descent Implementation

Custom implementation of Gradient Descent for linear regression

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add x0 = 1 to each instance
X_b = np.c_[np.ones((100, 1)), X]

# Hyperparameters
learning_rate = 0.1
n_iterations = 1000
m = 100

# Initialize theta
theta = np.random.randn(2, 1)

# Gradient Descent
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - learning_rate * gradients

print(f"Optimal Parameters: {theta}")

# Predict using the model
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

# Plot the results
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.title("Linear Regression using Gradient Descent")
plt.show()

# Output: Optimal Parameters: [[<theta_0_value>], [<theta_1_value>]]
```

![image](https://github.com/animator/learn-python/assets/118645569/485d7cf8-d806-490a-ab21-76d6ce21a243)

## Conclusion

Gradient Descent is a powerful and widely-used optimization algorithm in machine learning. It is critical for training various models and ensuring they perform well on unseen data.