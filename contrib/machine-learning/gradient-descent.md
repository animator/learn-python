# Gradient Descent

Gradient Descent is a fundamental optimization algorithm widely used in machine learning and deep learning for minimizing the cost function. It iteratively adjusts the parameters of the model to find the optimal values that minimize the error between the predicted and actual values.

## Introduction
Gradient Descent is an optimization algorithm used for minimizing a function by iteratively moving towards the minimum value of the function. It is commonly used in training machine learning models, especially in neural networks.

## Detailed Working Mechanism
#### Step 1: Initialize Parameters
Randomly initialize the model parameters (weights) before starting the optimization process.
#### Step 2: Compute Gradient
Calculate the gradient (partial derivatives) of the cost function with respect to each parameter. The gradient indicates the direction and rate of the steepest increase in the cost function.
#### Step 3: Update Parameters
Update the parameters by subtracting the product of the learning rate and the gradient. This moves the parameters in the direction that reduces the cost function.
#### Step 4: Iteration
Repeat steps 2 and 3 for a specified number of iterations or until the change in the cost function is below a certain threshold.

### Types of Gradient Descent
#### Batch Gradient Descent
* Uses the entire training dataset to compute the gradient at each step.
#### Stochastic Gradient Descent (SGD)
* Uses a single training example to compute the gradient at each step.
#### Mini-batch Gradient Descent
* Uses a small subset of the training dataset (mini-batch) to compute the gradient at each step.

## Advantages and Disadvantages
#### Advantages
* Simplicity: Easy to understand and implement.
* Efficiency: Can handle large datasets efficiently (especially SGD and mini-batch).
* Scalability: Works well with a variety of machine learning algorithms.

#### Disadvantages
* Convergence Issues: May converge to a local minimum instead of the global minimum.
* Sensitivity to Learning Rate: Choosing the appropriate learning rate is crucial for effective convergence.
* Computational Cost: Batch gradient descent can be slow with large datasets.

## Hyperparameters
#### Key Hyperparameters
* Learning Rate: Controls the step size during parameter updates.
* Number of Iterations: Number of times the algorithm iterates over the training dataset.
* Batch Size (for Mini-batch GD): Number of training examples used to compute the gradient at each step.

### Tuning Hyperparameters
Hyperparameter tuning involves selecting the appropriate values for learning rate, number of iterations, and batch size to optimize the performance of the gradient descent algorithm.

## Code Examples
#### Linear Regression using Gradient Descent
Below is a simple example of using gradient descent for a linear regression task with the Boston housing dataset.

```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load dataset
boston = load_boston()
X, y = boston.data, boston.target

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Add bias term (intercept)
X = np.c_[np.ones(X.shape[0]), X]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize parameters
theta = np.zeros(X_train.shape[1])
learning_rate = 0.01
num_iterations = 1000

# Gradient Descent
for i in range(num_iterations):
    gradients = X_train.T.dot(X_train.dot(theta) - y_train) / len(y_train)
    theta -= learning_rate * gradients

# Predictions
y_pred = X_test.dot(theta)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
```

#### Logistic Regression using Gradient Descent
Below is an example of logistic regression using gradient descent with a binary classification dataset.
```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Add bias term (intercept)
X = np.c_[np.ones(X.shape[0]), X]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize parameters
theta = np.zeros(X_train.shape[1])
learning_rate = 0.01
num_iterations = 1000

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Gradient Descent
for i in range(num_iterations):
    z = np.dot(X_train, theta)
    h = sigmoid(z)
    gradient = np.dot(X_train.T, (h - y_train)) / y_train.size
    theta -= learning_rate * gradient

# Predictions
z_test = np.dot(X_test, theta)
y_pred = sigmoid(z_test) >= 0.5

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
```

## Conclusion

Gradient Descent is a powerful optimization algorithm used in machine learning to minimize cost functions and improve model accuracy. Understanding its mechanics and properly tuning its hyperparameters are key to leveraging its full potential.
