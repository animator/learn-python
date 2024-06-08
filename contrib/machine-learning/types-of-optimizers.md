
---
# Optimizers in Machine Learning

Optimizers are algorithms or methods used to change the attributes of your neural network such as weights and learning rate in order to reduce the losses. Optimization algorithms help to minimize (or maximize) an objective function (also called a loss function) which is simply a mathematical function dependent on the model's internal learnable parameters which are used in computing the target values from the set of features.

## Types of Optimizers



### 1. Gradient Descent 

**Explanation:**
Gradient Descent is the simplest and most commonly used optimization algorithm. It works by iteratively updating the model parameters in the opposite direction of the gradient of the objective function with respect to the parameters. The idea is to find the minimum of a function by taking steps proportional to the negative of the gradient of the function at the current point.

**Mathematical Formulation:**

The update rule for the parameter vector θ in gradient descent is represented by the equation:

- $$\theta_{\text{new}} = \theta_{\text{old}} - \alpha \cdot \nabla J(\theta)$$

Where:
- θold is the old parameter vector.
-  θnew is the updated parameter vector.
- alpha(α) is the learning rate.
-  ∇J(θ) is the gradient of the objective function with respect to the parameters.



**Intuition:**
- At each iteration, we calculate the gradient of the cost function.
- The parameters are updated in the opposite direction of the gradient.
- The size of the step is controlled by the learning rate α.

**Advantages:**
- Simple to implement.
- Suitable for convex problems.

**Disadvantages:**
- Can be slow for large datasets.
- May get stuck in local minima for non-convex problems.
- Requires careful tuning of the learning rate.

**Python Implementation:**
```python
import numpy as np

def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for epoch in range(epochs):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / m
        theta -= lr * gradient
    return theta
```

### 2. Stochastic Gradient Descent (SGD)

**Explanation:**
SGD is a variation of gradient descent where we use only one training example to calculate the gradient and update the parameters. This introduces noise into the parameter updates, which can help to escape local minima but may cause the loss to fluctuate.

**Mathematical Formulation:**

-  $$θ = θ - α \cdot \frac{∂J (θ; xᵢ, yᵢ)}{∂θ}$$


- xᵢ, yᵢ are a single training example and its target.

**Intuition:**
- At each iteration, a random training example is selected.
- The gradient is calculated and the parameters are updated for this single example.
- This process is repeated for a specified number of epochs.

**Advantages:**
- Faster updates compared to batch gradient descent.
- Can handle large datasets.
- Helps to escape local minima due to the noise in updates.

**Disadvantages:**
- Loss function may fluctuate.
- Requires more iterations to converge.

**Python Implementation:**
```python
def stochastic_gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for epoch in range(epochs):
        for i in range(m):
            rand_index = np.random.randint(0, m)
            xi = X[rand_index:rand_index+1]
            yi = y[rand_index:rand_index+1]
            gradient = np.dot(xi.T, (np.dot(xi, theta) - yi))
            theta -= lr * gradient
    return theta
```

### 3. Mini-Batch Gradient Descent

**Explanation:**
Mini-Batch Gradient Descent is a variation where instead of a single training example or the whole dataset, a mini-batch of examples is used to compute the gradient. This reduces the variance of the parameter updates, leading to more stable convergence.

**Mathematical Formulation:**

- $$θ = θ - α \cdot \frac{1}{k} \sum_{i=1}^{k} \frac{∂J (θ; xᵢ, yᵢ)}{∂θ}$$


Where:
- \( k \) is the batch size.

**Intuition:**
- At each iteration, a mini-batch of training examples is selected.
- The gradient is calculated for this mini-batch.
- The parameters are updated based on the average gradient of the mini-batch.

**Advantages:**
- More stable updates compared to SGD.
- Faster convergence than batch gradient descent.
- Efficient on large datasets.

**Disadvantages:**
- Requires tuning of batch size.
- Computationally more expensive than SGD per iteration.

**Python Implementation:**
```python
def mini_batch_gradient_descent(X, y, lr=0.01, epochs=1000, batch_size=32):
    m, n = X.shape
    theta = np.zeros(n)
    for epoch in range(epochs):
        indices = np.random.permutation(m)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        for i in range(0, m, batch_size):
            X_i = X_shuffled[i:i+batch_size]
            y_i = y_shuffled[i:i+batch_size]
            gradient = np.dot(X_i.T, (np.dot(X_i, theta) - y_i)) / batch_size
            theta -= lr * gradient
    return theta
```

### 4. Momentum

**Explanation:**
Momentum helps accelerate gradient vectors in the right directions, thus leading to faster converging. It accumulates a velocity vector in directions of persistent reduction in the objective function, which helps to smooth the path towards the minimum.

**Mathematical Formulation:**

- $$v_t = γ \cdot v_{t-1} + α \cdot ∇J(θ)$$
- $$θ = θ - v_t$$

where:

- \( v_t \) is the velocity.
- γ is the momentum term, typically set between 0.9 and 0.99.

**Intuition:**
- At each iteration, the gradient is calculated.
- The velocity is updated based on the current gradient and the previous velocity.
- The parameters are updated based on the velocity.

**Advantages:**
- Faster convergence.
- Reduces oscillations in the parameter updates.

**Disadvantages:**
- Requires tuning of the momentum term.

**Python Implementation:**
```python
def momentum_gradient_descent(X, y, lr=0.01, epochs=1000, gamma=0.9):
    m, n = X.shape
    theta = np.zeros(n)
    v = np.zeros(n)
    for epoch in range(epochs):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / m
        v = gamma * v + lr * gradient
        theta -= v
    return theta
```

### 5. Nesterov Accelerated Gradient (NAG)

**Explanation:**
NAG is a variant of the gradient descent with momentum. It looks ahead by a step and calculates the gradient at that point, thus providing more accurate updates. This method helps to correct the overshooting problem seen in standard momentum.

**Mathematical Formulation:**

- $$v_t = γv_{t-1} + α \cdot ∇J(θ - γ \cdot v_{t-1})$$

- $$θ = θ - v_t$$




**Intuition:**
- At each iteration, the parameters are temporarily updated using the previous velocity.
- The gradient is calculated at this lookahead position.
- The velocity and parameters are then updated based on this gradient.

**Advantages:**
- More accurate updates compared to standard momentum.
- Faster convergence.

**Disadvantages:**
- Requires tuning of the momentum term.

**Python Implementation:**
```python
def nesterov_accelerated_gradient(X, y, lr=0.01, epochs=1000, gamma=0.9):
    m, n = X.shape
    theta = np.zeros(n)
    v = np.zeros(n)
    for epoch in range(epochs):
        lookahead_theta = theta - gamma * v
        gradient = np.dot(X.T, (np.dot(X, lookahead_theta) - y)) / m
        v = gamma * v + lr * gradient
        theta -= v
    return theta
```

### 6. AdaGrad

**Explanation:**
AdaGrad adapts the learning rate to the parameters, performing larger updates for infrequent and smaller updates for frequent parameters. It scales the learning rate inversely proportional to the square root of the sum of all historical squared values of the gradient.

**Mathematical Formulation:**

- $$G_t = G_{t-1} + (∂J(θ)/∂θ)^2$$

- $$θ = θ - \frac{α}{\sqrt{G_t + ε}} \cdot ∇J(θ)$$

Where:
- \(G_t\)   is the sum of squares of the gradients up to time step \( t \).
- ε is a small constant to avoid division by zero.

**Intuition:**
- Accumulates the sum of the squares of the gradients for each parameter.
- Uses this accumulated

 sum to scale the learning rate.
- Parameters with large gradients in the past have smaller learning rates.

**Advantages:**
- Effective for sparse data.
- Automatically adjusts learning rate.

**Disadvantages:**
- Learning rate decreases continuously, which can lead to premature convergence.

**Python Implementation:**
```python
def adagrad(X, y, lr=0.01, epochs=1000, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    G = np.zeros(n)
    for epoch in range(epochs):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / m
        G += gradient**2
        adjusted_lr = lr / (np.sqrt(G) + epsilon)
        theta -= adjusted_lr * gradient
    return theta
```

### 7. RMSprop

**Explanation:**
RMSprop modifies AdaGrad to perform well in non-convex settings by using a moving average of squared gradients to scale the learning rate. It helps to keep the learning rate in check, especially in the presence of noisy gradients.

**Mathematical Formulation:**

-                                                    E[g²]ₜ = βE[g²]ₜ₋₁ + (1 - β)(∂J(θ) / ∂θ)² 

- $$θ = θ - \frac{α}{\sqrt{E[g^2]_t + ε}} \cdot ∇J(θ)$$

Where:
-  \( E[g^2]_t \)  is the exponentially decaying average of past squared gradients.
- β is the decay rate.

**Intuition:**
- Keeps a running average of the squared gradients.
- Uses this average to scale the learning rate.
- Parameters with large gradients have their learning rates reduced.

**Advantages:**
- Effective for non-convex problems.
- Reduces oscillations in parameter updates.

**Disadvantages:**
- Requires tuning of the decay rate.

**Python Implementation:**
```python
def rmsprop(X, y, lr=0.01, epochs=1000, beta=0.9, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    E_g = np.zeros(n)
    for epoch in range(epochs):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / m
        E_g = beta * E_g + (1 - beta) * gradient**2
        adjusted_lr = lr / (np.sqrt(E_g) + epsilon)
        theta -= adjusted_lr * gradient
    return theta
```

### 8. Adam

**Explanation:**
Adam (Adaptive Moment Estimation) combines the advantages of both RMSprop and AdaGrad by keeping an exponentially decaying average of past gradients and past squared gradients.

**Mathematical Formulation:**

- $$m_t = β_1m_{t-1} + (1 - β_1)(∂J(θ)/∂θ)$$
- $$v_t = β_2v_{t-1} + (1 - β_2)(∂J(θ)/∂θ)^2$$
- $$\hat{m}_t = \frac{m_t}{1 - β_1^t}$$
- $$\hat{v}_t = \frac{v_t}{1 - β_2^t}$$
- $$θ = θ - \frac{α\hat{m}_t}{\sqrt{\hat{v}_t} + ε}$$

Where:
- \( m<sub>t \) is the first moment (mean) of the gradient.
- \( v<sub>t \) is the second moment (uncentered variance) of the gradient.
- β_1.β_2 are the decay rates for the moment estimates.

**Intuition:**
- Keeps track of both the mean and the variance of the gradients.
- Uses these to adaptively scale the learning rate.
- Provides a balance between AdaGrad and RMSprop.

**Advantages:**
- Efficient for large datasets.
- Well-suited for non-convex optimization.
- Handles sparse gradients well.

**Disadvantages:**
- Requires careful tuning of hyperparameters.
- Can be computationally intensive.

**Python Implementation:**
```python
def adam(X, y, lr=0.01, epochs=1000, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m, n = X.shape
    theta = np.zeros(n)
    m_t = np.zeros(n)
    v_t = np.zeros(n)
    for epoch in range(1, epochs+1):
        gradient = np.dot(X.T, (np.dot(X, theta) - y)) / m
        m_t = beta1 * m_t + (1 - beta1) * gradient
        v_t = beta2 * v_t + (1 - beta2) * gradient**2
        m_t_hat = m_t / (1 - beta1**epoch)
        v_t_hat = v_t / (1 - beta2**epoch)
        theta -= lr * m_t_hat / (np.sqrt(v_t_hat) + epsilon)
    return theta
```

These implementations are basic examples of how these optimizers can be implemented in Python using NumPy. In practice, libraries like TensorFlow and PyTorch provide highly optimized and more sophisticated implementations of these and other optimization algorithms.

---
