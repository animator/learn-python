# Logistic Regression

Logistic Regression is a statistical method used for binary classification problems. It is a type of regression analysis where the dependent variable is categorical. This README provides an overview of logistic regression, including its fundamental concepts, assumptions, and how to implement it using Python.

## Table of Contents

1. [Introduction](#introduction)
2. [Concepts](#concepts)
3. [Assumptions](#assumptions)
4. [Implementation](#implementation)
    - [Using Scikit-learn](#using-scikit-learn)
    - [Code Example](#code-example)
5. [Evaluation Metrics](#evaluation-metrics)
6. [Conclusion](#conclusion)
7. [References](#references)

## Introduction

Logistic Regression is used to model the probability of a binary outcome based on one or more predictor variables (features). It is widely used in various fields such as medical research, social sciences, and machine learning for tasks such as spam detection, fraud detection, and predicting user behavior.

## Concepts

### Sigmoid Function

The logistic regression model uses the sigmoid function to map predicted values to probabilities. The sigmoid function is defined as:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where \( z \) is a linear combination of the input features.

### Odds and Log-Odds

- **Odds**: The odds represent the ratio of the probability of an event occurring to the probability of it not occurring.
  
$$\text{Odds} = \frac{P(Y=1)}{P(Y=0)}$$

- **Log-Odds**: The log-odds is the natural logarithm of the odds.

  $$\text{Log-Odds} = \log \left( \frac{P(Y=1)}{P(Y=0)} \right)$$

Logistic regression models the log-odds as a linear combination of the input features.

### Model Equation

The logistic regression model equation is:

$$
\log \left( \frac{P(Y=1)}{P(Y=0)} \right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n
$$

Where:
- &beta;₀ is the intercept.
- &beta;<sub>i</sub> are the coefficients for the predictor variables X<sub>i</sub>.


## Assumptions

1. **Linearity**: The log-odds of the response variable are a linear combination of the predictor variables.
2. **Independence**: Observations should be independent of each other.
3. **No Multicollinearity**: Predictor variables should not be highly correlated with each other.
4. **Large Sample Size**: Logistic regression requires a large sample size to provide reliable results.

## Implementation

### Using Scikit-learn

Scikit-learn is a popular machine learning library in Python that provides tools for logistic regression.

### Code Example

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv('path/to/your/dataset.csv')

# Define features and target variable
X = data[['feature1', 'feature2', 'feature3']]
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
```

## Evaluation Metrics

- **Accuracy**: The proportion of correctly classified instances among all instances.
- **Confusion Matrix**: A table showing the number of true positives, true negatives, false positives, and false negatives.
- **Precision, Recall, and F1-Score**: Metrics to evaluate the performance of the classification model.

## Conclusion

Logistic regression is a fundamental classification technique that is easy to implement and interpret. It is a powerful tool for binary classification problems and provides a probabilistic framework for predicting binary outcomes.
