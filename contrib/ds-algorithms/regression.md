
# Regression Models in Scikit-Learn

Scikit-Learn provides a variety of regression models to tackle different types of prediction problems. Below are 15 regression models ranging from simple to complex.

## 1. Linear Regression

### Description
Linear Regression is a fundamental algorithm that uses linear equation and develops the relationship between a dependent variable and one or more independent variables .

### Use Case
Linear Regression is commonly used for predicting continuous values such as house prices, stock prices, and sales revenue. It is suitable for applications where the relationship between variables is approximately linear and the goal is to understand or predict numerical outcomes.

### Code Sample
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 2. Logistic Regression

### Description
Logistic Regression is used for binary classification tasks . It predicts the chance or probability that a given data point belongs to a specific class out of the ones given

### Use Case
Logistic Regression is used for classification tasks like spam detection, cancer detection, and customer churn prediction. It is ideal for scenarios where the goal is to classify data into two distinct categories based on input features.

### Code Sample
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset and create a binary target variable
data = load_diabetes()
X = data.data
y = (data.target > data.target.mean()).astype(int)  # Binary target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 3. Ridge Regression

### Description
Ridge Regression is a technique for analyzing multiple regression data that is  multicollinear. It adds a degree of bias to the regression estimates by adding some penalty for complication

### Use Case
Used when there is multicollinearity in the data.

### Code Sample
```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 4. Lasso Regression

### Description
Lasso Regression or L1 regularization is similar to Ridge Regression and can lead to sparse models. Regularization is a statistical technique used to minimize errors caused by overfitting on training data.

### Use Case
Used when feature selection and sparsity is desired.

### Code Sample
```python
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 5. ElasticNet Regression

### Description
ElasticNet is a hybrid regression technique obtained by mixing up the penalties of Lasso with Ridge Regression. By incorporating both L1 and L2 regularization, it is better than before methods,, especially when dealing with datasets with multiple correlated features. It is way more robust

### Use Case
Used when neither Ridge nor Lasso alone performs well.

### Code Sample
```python
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = ElasticNet(alpha=0.1, l1_ratio=0.7)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 6. Bayesian Ridge Regression

### Description
Bayesian Ridge Regression estimates a probabilistic model for regression problems with the aid of Bayesian inference. It includes prior distributions on model parameters, which rises prediction accuracy , while helping with uncertainty. It uses confidenc intervals for accurate model results

### Use Case
Used when we want probabilistic predictions and model uncertainty.

### Code Sample
```python
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = BayesianRidge()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 7. Huber Regressor

### Description
Huber Regressor, which helps treat outliers,  derives from the best of Least Squares and Absolute Deviation. Thus it helps in maintaining the robustness of traditional linear regression methods, making it suitable for datasets with noisy or extreme values, which is useful for real world problems

### Use Case
Used when data has outliers, and noisy datasets

### Code Sample
```python
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = HuberRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 8. Quantile Regression

### Description
Quantile Regression estimates the conditional median or other quantiles of the response variable, providing a more complete view of possible outcomes.

### Use Case
Used for predicting medians or other quantiles, especially when the distribution is not normal.

### Code Sample
```python
from sklearn.linear_model import QuantileRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = QuantileRegressor(quantile=0.5)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 9. Polynomial Regression

### Description
Polynomial Regression is a form of linear regression in which the relationship between the independent variable and dependent variable is modeled as an nth degree polynomial.

### Use Case
Used when the relationship between variables is non-linear.

### Code Sample
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 10. Decision Tree Regression

### Description
Decision Tree Regression uses a decision tree to model the relationship between the input features and the target value, making decisions based on feature splits.

### Use Case
Used for non-linear relationships and when interpretability of decision rules is desired.

### Code Sample
```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 11. Random Forest Regression

### Description
Random Forest Regression is an ensemble method that uses multiple decision trees to improve predictive accuracy and control over-fitting.

### Use Case
Used for complex regression tasks where accuracy is important.

### Code Sample
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 12. Gradient Boosting Regression

### Description
Gradient

 Boosting Regression builds an ensemble of trees in a stage-wise fashion, where each tree tries to correct the errors of the previous one.

### Use Case
Used for high predictive accuracy in various applications.

### Code Sample
```python
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 13. AdaBoost Regression

### Description
AdaBoost Regression is a boosting technique that combines weak learners to create a strong learner by focusing on mistakes of previous learners.

### Use Case
Used when we want to boost the performance of simple regression models.

### Code Sample
```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = AdaBoostRegressor(DecisionTreeRegressor(), n_estimators=100)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 14. Extra Trees Regression

### Description
Extra Trees Regression is an ensemble method that fits multiple randomized decision trees and averages their predictions.

### Use Case
Used for high variance datasets.

### Code Sample
```python
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = ExtraTreesRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
```

## 15. Isotonic Regression

### Description
Isotonic Regression is a non-parametric regression technique that fits a non-decreasing function to the data.

### Use Case
Used when the relationship between variables is monotonic but not necessarily linear.

### Code Sample
```python
from sklearn.isotonic import IsotonicRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X = data.data[:, 0]  # Use only one feature for simplicity
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = IsotonicRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

```