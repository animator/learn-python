# Grid Search

Grid Search is a hyperparameter tuning technique in Machine Learning that helps to find the best combination of hyperparameters for a given model. It works by defining a grid of hyperparameters and then training the model with all the possible combinations of hyperparameters to find the best performing set.
The Grid Search Method considers some hyperparameter combinations and selects the one returning a lower error score. This method is specifically useful when there are only some hyperparameters in order to optimize. However, it is outperformed by other weighted-random search methods when the Machine Learning model grows in complexity.

## Implementation

Before applying Grid Searching on any algorithm, Data is used to divided into training and validation set, a validation set is used to validate the models. A model with all possible combinations of hyperparameters is tested on the validation set to choose the best combination.
Grid Searching can be applied to any hyperparameters algorithm whose performance can be improved by tuning hyperparameter. For example, we can apply grid searching on K-Nearest Neighbors by validating its performance on a set of values of K in it. Same thing we can do with Logistic Regression by using a set of values of learning rate to find the best learning rate at which Logistic Regression achieves the best accurac
Let us consider that the model accepts the below three parameters in the form of input:
1. Number of hidden layers [2, 4]
2. Number of neurons in every layer [5, 10]
3. Number of epochs [10, 50]

If we want to try out two options for every parameter input (as specified in square brackets above), it estimates different combinations. For instance, one possible combination can be [2, 5, 10]. Finding such combinations manually would be a headache.
Now, suppose that we had ten different parameters as input, and we would like to try out five possible values for each and every parameter. It would need manual input from the programmer's end every time we like to alter the value of a parameter, re-execute the code, and keep a record of the outputs for every combination of the parameters.
Grid Search automates that process, as it accepts the possible value for every parameter and executes the code in order to try out each and every possible combination outputs the result for the combinations and outputs the combination having the best accuracy.
Higher values of C tell the model, the training data resembles real world information, place a greater weight on the training data. While lower values of C do the opposite.

## Explaination of the Code 

The code provided performs hyperparameter tuning for a Logistic Regression model using a manual grid search approach. It evaluates the model's performance for different values of the regularization strength hyperparameter C on the Iris dataset.
1. datasets from sklearn is imported to load the Iris dataset.
2. LogisticRegression from sklearn.linear_model is imported to create and fit the logistic regression model.
3. The Iris dataset is loaded, with X containing the features and y containing the target labels.
4. A LogisticRegression model is instantiated with max_iter=10000 to ensure convergence during the fitting process, as the default maximum iterations (100) might not be sufficient.
5. A list of different values for the regularization strength C is defined. The hyperparameter C controls the regularization strength, with smaller values specifying stronger regularization.
6. An empty list scores is initialized to store the model's performance scores for different values of C.
7. A for loop iterates over each value in the C list:
8. logit.set_params(C=choice) sets the C parameter of the logistic regression model to the current value in the loop.
9. logit.fit(X, y) fits the logistic regression model to the entire Iris dataset (this is typically done on training data in a real scenario, not the entire dataset).
10. logit.score(X, y) calculates the accuracy of the fitted model on the dataset and appends this score to the scores list.
11. After the loop, the scores list is printed, showing the accuracy for each value of C.

## Python Code

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
iris = datasets.load_iris()
X = iris['data']
y = iris['target']
logit = LogisticRegression(max_iter = 10000)
C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []
for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))
print(scores)

## Results

[0.9666666666666667, 0.9666666666666667, 0.9733333333333334, 0.9733333333333334, 0.98, 0.98, 0.9866666666666667, 0.9866666666666667]

We can see that the lower values of C performed worse than the base parameter of 1. However, as we increased the value of C to 1.75 the model experienced increased accuracy.
It seems that increasing C beyond this amount does not help increase model accuracy.
