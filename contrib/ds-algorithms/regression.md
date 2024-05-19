
# Regression Models in Scikit-Learn

Scikit-Learn provides a variety of regression models to tackle different types of prediction problems. Below are popular regression models ranging from simple to complex.

## 1. Linear Regression

### Description
Linear Regression is a fundamental algorithm that uses linear equation and develops the relationship between a dependent variable and one or more independent variables .

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
Quantile Regression estimates all quantiles in the response variable distribution. Unlike traditional regression, which focuses on the mean, Quantile Regression provides a comprehensive understanding of the data distribution's different percentiles like median, 25th percentile, etc which are of high necessity in some datasets. 


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
Polynomial Regression is a form of linear regression in which the relationship between the independent variable and dependent variable is modeled as an nth degree polynomial. The numerical method for obtaining and solving it is pretty similar to linear equation, except that polynomial regression is used for more complex data and is a broader use case than simple regression models


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
Decision Tree Regression employs a decision tree to investigate the relationship between  features or attributes  under input data  and the target value we aim to find. By recursively partitioning the feature space, it uses splits based on features for decision making , allowing more complex models also suited for text data , etc



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
Random Forest Regression is an ensemble method that uses multiple decision trees to improve predictive accuracy and control over-fitting. Ensemble learning is a method in machine learning that aggregates predictions from multiple models to produce a more precise and robust prediction.



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
NOTE: following code samples are AI generated for uniformity