# Introduction to Scikit learn and Getting Data ready for modelling

**Scikit learn or sklearn is an open soure machine learning library.**

**It's built on top of NumPy, which is a Python library for numerical computing, and Matplotlib, which is a Python library for data visualization.**

## Why scikit learn??

*The field of data science and machine leaning is so vast, our main goal is to find the patterns within the data and use those patterns to make a predictions.*

For example:

* If you're trying to create a machine learning model to predict whether an email is spam or not spam, you're working on a classification problem (whether something is one thing or another).
* If you're trying to create a machine learning model to predict the price of houses given their characteristics, you're working on a regression problem (predicting a number).

**Once you find the problem , now it's time to use machine learning to solve it.**

### An end-to-end Scikit-Learn workflow

Here’s the steps to be follow :

1. Get the data ready (split into features and labels, prepare train and test steps)
2. Choose a model for our problem
3. Fit the model to the data and use it to make a prediction
4. Evaluate the model
5. Experiment to improve
6. Save a model for someone else to use

In this notebook we will only look the first step i.e getting data ready.

We'll look all other steps one by one in future notebooks.


#### 1. Getting the data ready


```python
# Importing the essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
print(f"Current Scikit learn version is :{sklearn.__version__}")
```

    Current Scikit learn version is :1.4.1.post1
    

We're going to use a `heart-disease` dataset. This data set contains the patient attributes also called features which we use to predict the target variable.

Whether a patient has heart disease (1) or not (0)


```python
# Loading the data set
df = pd.read_csv("https://raw.githubusercontent.com/kRiShNa-429407/learn-python/main/contrib/pandas/Datasets/heart-disease.csv")
print(df.head())
```

       age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \
    0   63    1   3       145   233    1        0      150      0      2.3      0   
    1   37    1   2       130   250    0        1      187      0      3.5      0   
    2   41    0   1       130   204    0        0      172      0      1.4      2   
    3   56    1   1       120   236    0        1      178      0      0.8      2   
    4   57    0   0       120   354    0        1      163      1      0.6      2   
    
       ca  thal  target  
    0   0     1       1  
    1   0     2       1  
    2   0     2       1  
    3   0     2       1  
    4   0     2       1  
    


```python
# Create X(features)
X = df.drop("target",axis=1)

# Create y(target)
y = df["target"]
```


```python
print(X.head())
```

       age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  \
    0   63    1   3       145   233    1        0      150      0      2.3      0   
    1   37    1   2       130   250    0        1      187      0      3.5      0   
    2   41    0   1       130   204    0        0      172      0      1.4      2   
    3   56    1   1       120   236    0        1      178      0      0.8      2   
    4   57    0   0       120   354    0        1      163      1      0.6      2   
    
       ca  thal  
    0   0     1  
    1   0     2  
    2   0     2  
    3   0     2  
    4   0     2  
    


```python
print(y.head())
```

    0    1
    1    1
    2    1
    3    1
    4    1
    Name: target, dtype: int64
    

One of the most important practices in Machine Learning is to split datasets into training and test sets.

This way, a model will train on the training set to learn patterns, and then those patterns can be evaluated on the test set.

It’s important that a model never sees testing data during training. This is equivalent to a student studying course materials during the semester (training set) and then testing their abilities on the following exam (testing set).

Scikit-learn provides the `sklearn.model_selection.train_test_split` method to split datasets in training and test sets


```python
# Split the data into training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y,
                                                    test_size=0.25) # by default train_test_split uses 25% of the data for the test set

X_train.shape, X_test.shape, y_train.shape, y_test.shape
```




    ((227, 13), (76, 13), (227,), (76,))



**Note: A common practice to use an 80/20 or 70/30 or 75/25 split for training/testing data. There is also a third set, known as a validation set (e.g. 70/15/15 for training/validation/test) for hyperparameter tuning, but for now we'll focus on training and test sets.**
