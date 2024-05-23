## Confusion Matrix 

A confusion matrix is a fundamental performance evaluation tool used in machine learning to assess the accuracy of a classification model. It is an N x N matrix, where N represents the number of target classes.

For binary classification, it results in a 2 x 2 matrix that outlines four key parameters:
1. True Positive (TP) - The predicted value matches the actual value, or the predicted class matches the actual class. 
For example - the actual value was positive, and the model predicted a positive value.
2. True Negative (TN) - The predicted value matches the actual value, or the predicted class matches the actual class. 
For example - the actual value was negative, and the model predicted a negative value.
3. False Positive (FP)/Type I Error - The predicted value was falsely predicted.
For example - the actual value was negative, but the model predicted a positive value.
4. False Negative (FN)/Type II Error - The predicted value was falsely predicted.
For example - the actual value was positive, but the model predicted a negative value.

The confusion matrix enables the calculation of various metrics like accuracy, precision, recall, F1-Score and specificity.
1. Accuracy - It represents the proportion of correctly classified instances out of the total number of instances in the dataset.
2. Precision - It quantifies the accuracy of positive predictions made by the model.
3. Recall -  It quantifies the ability of a model to correctly identify all positive instances in the dataset and is also known as sensitivity or true positive rate.
4. F1-Score - It is a single measure that combines precision and recall, offering a balanced evaluation of a classification model's effectiveness.

To implement the confusion matrix in Python, we can use the confusion_matrix() function from the sklearn.metrics module of the scikit-learn library. 
The function returns a 2D array that represents the confusion matrix.
We can also visualize the confusion matrix using a heatmap.

```python
# Import necessary libraries
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt 

# Create the NumPy array for actual and predicted labels
actual = np.array(['Apple', 'Apple', 'Apple', 'Not Apple', 'Apple',
                   'Not Apple', 'Apple', 'Apple', 'Not Apple', 'Not Apple'])
predicted = np.array(['Apple', 'Not Apple', 'Apple', 'Not Apple', 'Apple',
                      'Apple', 'Apple', 'Apple', 'Not Apple', 'Not Apple'])

# Compute the confusion matrix
cm = confusion_matrix(actual,predicted)

# Plot the confusion matrix with the help of the seaborn heatmap
sns.heatmap(cm, 
            annot=True,
            fmt='g', 
            xticklabels=['Apple', 'Not Apple'],
            yticklabels=['Apple', 'Not Apple'])
plt.xlabel('Prediction', fontsize=13)
plt.ylabel('Actual', fontsize=13)
plt.title('Confusion Matrix', fontsize=17)
plt.show()

# Classifications Report based on Confusion Metrics
print(classification_report(actual, predicted))
```

### Results 

```
1. Confusion Matrix:
[[5 1]
[1 3]]
2. Classification Report:
              precision  recall   f1-score   support
Apple           0.83      0.83      0.83         6
Not Apple       0.75      0.75      0.75         4

accuracy                            0.80        10
macro avg       0.79      0.79      0.79        10
weighted avg    0.80      0.80      0.80        10
```
