# Naive Bayes 

## Introduction

The Naive Bayes model uses probabilities to predict an outcome.It is a supervised machine learning technique, i.e. it reqires labelled data for training. It is used for classification and is based on the Bayes' Theorem. The basic assumption of this model is the independence among the features, i.e. a feature is unaffected by any other feture.

## Bayes' Theorem

Bayes' theorem is given by: 

$$
P(a|b) = \frac{P(b|a)*P(a)}{P(b)}
$$

where:
- $P(a|b)$ is the posterior probability, i.e. probability of 'a' given that 'b' is true,
- $P(b|a)$ is the likelihood probability i.e. probability of 'b' given that 'a' is true,
- $P(a)$ and $P(b)$ are the probabilities of 'a' and 'b' respectively, independent of each other.


## Applications

Naive Bayes classifier has numerous applications including :
  1. Text classification.
  2. Sentiment analysis.
  3. Spam filtering.
  4. Multiclass classification (eg. Weather prediction).
  5. Recommendation Systems.
  6. Healthcare sector.
  7. Document categorization.


## Advantages

  1. Easy to implement.
  2. Useful even if training dataset is limited (where a decision tree would not be recommended).
  3. Supports multiclass classification which is not supported by some machine learning algorithms like SVM and logistic regression.
  4. Scalable, fast and efficient.

## Disadvantages

  1. Assumes features to be independent, which may not be true in certain scenarios.
  2. Zero probability error.
  3. Sensitive to noise.

## Zero Probability Error

  Zero probability error is said to occur if in some case the number of occurances of an event given another event is zero.
  To handle zero probability error, Laplace's correction is used by adding a small constant .

**Example:**


Given the data below, find whether tennis can be played if  ( outlook=overcast, wind=weak ).

**Data**

---
| SNo | Outlook (A)  |  Wind (B)  |   PlayTennis (R)  |
|-----|--------------|------------|-------------------|
| 1   | Rain         | Weak       | No                |
| 2   | Rain         | Strong     | No                |
| 3   | Overcast     | Weak       | Yes               |
| 4   | Rain         | Weak       | Yes               |
| 5   | Overcast     | Weak       | Yes               |
| 6   | Rain         | Strong     | No                |
| 7   | Overcast     | Strong     | Yes               |
| 8   | Rain         | Weak       | No                |
| 9   | Overcast     | Weak       | Yes               |
| 10  | Rain         | Weak       | Yes               |
---

- **Calculate prior probabilities**

$$
   P(Yes)  =  \frac{6}{10} = 0.6
$$
$$
   P(No)  =  \frac{4}{10} = 0.4
$$

- **Calculate likelihoods**

    1.**Outlook (A):** 

    ---
    | A\R       |  Yes  | No  |
    |-----------|-------|-----|
    | Rain      |   2   |  4  |
    | Overcast  |   4   |  0  |
    | Total     |   6   |  4  |
    ---

- Rain:

$$
P(Rain|Yes) = \frac{2}{6}
$$

$$
P(Rain|No) = \frac{4}{4}
$$

- Overcast:

$$
   P(Overcast|Yes)  =  \frac{4}{6} 
$$
$$
   P(Overcast|No)  =  \frac{0}{4}
$$


Here, we can see that
  $$
    P(Overcast|No)  = 0
  $$
This is a zero probability error! 

Since probability is 0, naive bayes model fails to predict.

  **Applying Laplace's correction:**

  In Laplace's correction, we scale the values for 1000 instances.
  - **Calculate prior probabilities**

  $$
     P(Yes)  =  \frac{600}{1002} 
  $$
  
  $$
     P(No)  =  \frac{402}{1002} 
  $$

- **Calculate likelihoods**

  1. **Outlook (A):** 


   ( Converted to 1000 instances )

   We will add 1 instance each to the (PlayTennis|No) column {Laplace's correction}

    ---
    | A\R       |  Yes  |      No       |
    |-----------|-------|---------------|
    | Rain      |  200  |  (400+1)=401  |
    | Overcast  |  400  |    (0+1)=1    |
    | Total     |  600  |      402      |
    ---

    - **Rain:**

  $$
     P(Rain|Yes)  =  \frac{200}{600} 
  $$
  $$
     P(Rain|No)  =  \frac{401}{402} 
  $$

  - **Overcast:**

  $$
     P(Overcast|Yes)  =  \frac{400}{600} 
  $$
  $$
     P(Overcast|No)  =  \frac{1}{402}
  $$


  2. **Wind (B):** 

    
  ---
  | B\R       |   Yes   |  No   |
  |-----------|---------|-------|
  | Weak      |   500   |  200  |
  | Strong    |   100   |  200  |
  | Total     |   600   |  400  |
  ---

    - **Weak:**

    $$
       P(Weak|Yes)  =  \frac{500}{600} 
    $$
    $$
       P(Weak|No)  =  \frac{200}{400} 
    $$

    - **Strong:**

    $$
       P(Strong|Yes)  =  \frac{100}{600} 
    $$
    $$
       P(Strong|No)  =  \frac{200}{400}
    $$

  - **Calculting probabilities:**
  
  $$
     P(PlayTennis|Yes)  =  P(Yes) * P(Overcast|Yes) * P(Weak|Yes)
  $$
  $$
                 =  \frac{600}{1002} * \frac{400}{600} * \frac{500}{600} 
  $$
  $$
                 =  0.3326
  $$

  $$
     P(PlayTennis|No)  =  P(No) * P(Overcast|No) * P(Weak|No)
  $$
  $$
                 =  \frac{402}{1002} * \frac{1}{402} * \frac{200}{400} 
  $$
  $$
                 =  0.000499 =  0.0005
  $$


Since ,
$$
     P(PlayTennis|Yes)  >  P(PlayTennis|No) 
$$
we can conclude that tennis can be played if outlook is overcast and wind is weak.


# Types of Naive Bayes classifier 


## Guassian Naive Bayes
  
  It is used when the dataset has **continuous data**. It assumes that the data is distributed normally (also known as guassian distribution).
  A guassian distribution can be characterized by a bell-shaped curve.

  **Continuous data features :**  Features which can take any real values within a certain range. These features have an infinite number of possible values.They are  generally measured, not counted.
  eg. weight, height, temperature, etc. 

  **Code**

  ```python

#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

#read data
d=pd.read_csv("data.csv")
df=pd.DataFrame(d)

X = df.iloc[:,1:7:1]
y = df.iloc[:,7:8:1]

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# training the model on training set
obj = GaussianNB()
obj.fit(X_train, y_train)

#making predictions on the testing set
y_pred = obj.predict(X_train)

#comparing y_test and y_pred
print("Gaussian Naive Bayes model accuracy:", metrics.accuracy_score(y_train, y_pred))
print("Confusion matrix: \n",confusion_matrix(y_train,y_pred))

  ```

  
## Multinomial Naive Bayes

  Appropriate when the features are categorical or countable. It models the likelihood of each feature as a multinomial distribution.
  Multinomial distribution is used to find probabilities of each category, given multiple categories (eg. Text classification).
  
  **Code**

  ```python

#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

#read data
d=pd.read_csv("data.csv")
df=pd.DataFrame(d)

X = df.iloc[:,1:7:1]
y = df.iloc[:,7:8:1]

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# training the model on training set
obj = MultinomialNB()
obj.fit(X_train, y_train)

#making predictions on the testing set
y_pred = obj.predict(X_train)

#comparing y_test and y_pred
print("Gaussian Naive Bayes model accuracy:", metrics.accuracy_score(y_train, y_pred))
print("Confusion matrix: \n",confusion_matrix(y_train,y_pred))


  ```

## Bernoulli Naive Bayes

  It is specifically designed for binary features (eg. Yes or No). It models the likelihood of each feature as a Bernoulli distribution. 
  Bernoulli distribution is used when there are only two possible outcomes (eg. success or failure of an event).

  **Code**

  ```python
  
#import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix

#read data
d=pd.read_csv("data.csv")
df=pd.DataFrame(d)

X = df.iloc[:,1:7:1]
y = df.iloc[:,7:8:1]

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# training the model on training set
obj = BernoulliNB()
obj.fit(X_train, y_train)

#making predictions on the testing set
y_pred = obj.predict(X_train)

#comparing y_test and y_pred
print("Gaussian Naive Bayes model accuracy:", metrics.accuracy_score(y_train, y_pred))
print("Confusion matrix: \n",confusion_matrix(y_train,y_pred))

  ```


## Evaluation

  1. Confusion matrix.
  2. Accuracy.
  3. ROC curve.


## Conclusion

 Although the assumption that the features are independent of each other may limit the naive bayes model in some cases, the simplicity and efficiency of this classifier makes it a valuable and reliable model in the domain of machine learning. Naive Bayes classifiers are suitable for a wide range of classification problems.
  