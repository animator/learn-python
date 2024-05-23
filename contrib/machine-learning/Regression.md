# Regression


*  Regression is a supervised machine learning technique which is used to predict continuous values. 


> Now, Supervised learning is a category of machine learning that uses labeled datasets to train algorithms to predict outcomes and recognize patterns.

*   Regression is a statistical method used to model the relationship between a dependent variable (often denoted as 'y') and one or more independent variables (often denoted as 'x'). The goal of regression analysis is to understand how the dependent variable changes as the independent variables change.
   # Types Of Regression

1.   Linear Regression
2.   Polynomial Regression
3.   Stepwise Regression
4.   Decision Tree Regression
5.   Random Forest Regression
6.   Ridge Regression
7.   Lasso Regression
8.   ElasticNet Regression
9.   Bayesian Linear Regression
10.  Support Vector Regression

But, we'll first start with Linear Regression
# Linear Regression

* Linear regression is a fundamental statistical method used to model the relationship between a dependent variable (often denoted as
𝑌) and one or more independent variables (often denoted as
𝑋). The relationship is assumed to be linear, meaning that changes in the independent variables are associated with changes in the dependent variable in a straight-line fashion.

The basic form of linear regression for a single independent variable is:

**𝑌=𝛽0+𝛽1𝑋+𝜖**

Where:

*   Y is the dependent variable.
*   X is the independent variable.
*   𝛽0 is the intercept, representing the value of Y when X is zero
*   𝛽1 is the slope coefficient, representing the change in Y for a one-unit change in X
*   ϵ is the error term, representing the variability in Y that is not explained by the linear relationship with X.

# Basic Code of Linear Regression

* This line imports the numpy library, which is widely used for numerical operations in Python. We use np as an alias for numpy, making it easier to reference functions and objects from the library.
```
import numpy as np
```

* This line imports the LinearRegression class from the linear_model module of the scikit-learn library.scikit-learn is a powerful library for machine learning tasks in Python, and LinearRegression is a class provided by it for linear regression.
```
from sklearn.linear_model import LinearRegression
```
* This line creates a NumPy array X containing the independent variable values. In this example, we have a simple one-dimensional array representing the independent variable. The reshape(-1, 1) method reshapes the array into a column vector, necessary for use with scikit-learn

```
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
```
* This line creates a NumPy array Y containing the corresponding dependent variable values. These are the observed values of the dependent variable corresponding to the independent variable values in X.
```
Y = np.array([2, 4, 5, 8, 5])
```

* This line creates an instance of the LinearRegression class, which represents the linear regression model. We'll use this object to train the model and make predictions.
```
model = LinearRegression()
```

* This line fits the linear regression model to the data. The fit() method takes two arguments: the independent variable (X) and the dependent variable (Y). This method estimates the coefficients of the linear regression equation that best fit the given data.
```
model.fit(X, Y)
```
* These lines print out the intercept (beta_0) and coefficient (beta_1) of the linear regression model. model.intercept_ gives the intercept value, and model.coef_ gives an array of coefficients, where model.coef_[0] corresponds to the coefficient of the first independent variable (in this case, there's only one).
```
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])
```

* These lines demonstrate how to use the trained model to make predictions for new data. 
* We create a new NumPy array new_data containing the values of the independent variable for which we want to predict the dependent variable values.
* We then use the predict() method of the model to obtain the predictions for these new data points. Finally, we print out the predicted values.
```
new_data = np.array([[6], [7]])
predictions = model.predict(new_data)
print("Predictions:", predictions)
```
# Assumptions of Linear Regression

# Linearity:

* To assess the linearity assumption, we can visually inspect a scatter plot of the observed values versus the predicted values.
* If the relationship between them appears linear, it suggests that the linearity assumption is reasonable.
```
import matplotlib.pyplot as plt
predictions = model.predict(X)
plt.scatter(predictions,Y)
plt.xlabel("Predicted Values")
plt.ylabel("Observed Values")
plt.title("Linearity Check: Observed vs Predicted")
plt.show()
```
# Homoscedasticity:
* Homoscedasticity refers to the constant variance of the residuals across all levels of the independent variable(s). We can visually inspect a plot of residuals versus predicted values to check for homoscedasticity.
```
residuals = Y - predictions
plt.scatter(predictions, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Homoscedasticity Check: Residuals vs Predicted Values")
plt.axhline(y=0, color='red', linestyle='--')  # Add horizontal line at y=0
plt.show()

```
# Normality of Residuals:
* To assess the normality of residuals, we can visually inspect a histogram or a Q-Q plot of the residuals.
```
import seaborn as sns

sns.histplot(residuals, kde=True)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Normality of Residuals: Histogram")
plt.show()

import scipy.stats as stats

stats.probplot(residuals, dist="norm", plot=plt)
plt.title("Normal Q-Q Plot")
plt.show()

```
# Metrics for Regression


# Mean Absolute Error (MAE)

* MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average of the absolute differences between predicted and actual values.
```
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(Y, predictions)
print(f"Mean Absolute Error (MAE): {mae}")

```
# Mean Squared Error (MSE)

* MSE measures the average of the squares of the errors. It gives more weight to larger errors, making it sensitive to outliers.
```
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y, predictions)
print(f"Mean Squared Error (MSE): {mse}")
```
# Root Mean Squared Error (RMSE)
* RMSE is the square root of the MSE. It provides an error metric that is in the same units as the dependent variable, making it more interpretable.
```
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")

```
# R-squared (Coefficient of Determination)
* R-squared measures the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, where 1 indicates a perfect fit.
```
from sklearn.metrics import r2_score

r2 = r2_score(Y, predictions)
print(f"R-squared (R^2): {r2}")
```

> In this tutorial, The sample dataset is there for learning purpose only


