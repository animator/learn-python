# Machine Learning Evaluation Metrics and Performance Measures

In the field of machine learning, evaluating the performance of a model is crucial for understanding its effectiveness in solving a particular task. There exist various metrics and techniques to assess the performance of machine learning models, each serving different purposes based on the nature of the problem being solved. In this section, we'll explore some commonly used evaluation metrics and performance measures.

## 1. Accuracy

Accuracy is one of the most straightforward metrics used for classification problems. It measures the ratio of correctly predicted instances to the total number of instances evaluated. While accuracy is easy to understand, it might not be the best metric for imbalanced datasets where one class dominates the others.

$$ \text{Accuracy} = \frac{\text{Total Number of Predictions}}{\text{Number of Correct Predictions}} $$

## 2. Precision, Recall, and F1 Score

Precision, recall, and the F1 score are commonly used metrics for evaluating classification models, especially in cases of class imbalance. Precision measures the ratio of true positives to the total predicted positives, recall measures the ratio of true positives to the total actual positives, and the F1 score is the harmonic mean of precision and recall.

- Precision: $$\( \frac{\text{True Positives} + \text{False Positives}}{\text{True Positives}} \)$$
- Recall: $$\( \frac{\text{True Positives} + \text{False Negatives}}{\text{True Positives}} \)$$
- F1 Score: $$\( \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \)$$

## 3. Confusion Matrix

A confusion matrix provides a comprehensive summary of the performance of a classification model. It tabulates the number of true positives, true negatives, false positives, and false negatives, allowing for a more in-depth analysis of the model's performance across different classes.

- True Positives (TP): Instances correctly classified as positive.
- True Negatives (TN): Instances correctly classified as negative.
- False Positives (FP): Instances incorrectly classified as positive.
- False Negatives (FN): Instances incorrectly classified as negative.

## 4. ROC Curve and AUC

The Receiver Operating Characteristic (ROC) curve is a graphical representation of the true positive rate against the false positive rate at various threshold settings. The Area Under the ROC Curve (AUC) provides an aggregated measure of the model's performance across all possible classification thresholds.

$$\[ True Positive Rate(TPR/Sensitivity/Recall) = \frac{True \ Positive}{True \ Positive + False \ Negative} \]$$

$$\[ False Positive Rate(FPR) = \frac{False \ Positive}{False \ Positive + True \ Negative} \]$$

## 5. Mean Absolute Error (MAE)

MAE is a metric used to evaluate regression models. It represents the average of the absolute differences between predicted and actual values.

  $$ MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| $$

- **Parameters:**
  - $\( y_i \)$: Actual value of the dependent variable for the \(i\)th observation.
  - $\( \hat{y}_i \)$: Predicted value of the dependent variable for the \(i\)th observation.
  - $\( n \)$: Total number of observations.

## 6. Mean Squared Error (MSE)

MSE is another regression metric that calculates the average of the squared differences between predicted and actual values.

$$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
- **Parameters:**
  - \( y_i \): Actual value of the dependent variable for the \(i\)th observation.
  - \( \hat{y}_i \): Predicted value of the dependent variable for the \(i\)th observation.
  - \( n \): Total number of observations.

## 7. Root Mean Squared Error (RMSE)

RMSE is the square root of the MSE. It provides a measure of the spread of errors in the predictions.

$$ RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} $$

- **Parameters:**
  - \( y_i \): Actual value of the dependent variable for the \(i\)th observation.
  - \( \hat{y}_i \): Predicted value of the dependent variable for the \(i\)th observation.
  - \( n \): Total number of observations.


## 8. R-squared (Coefficient of Determination)

The R-squared, denoted as \( R^2 \), measures the proportion of the variance in the dependent variable that is predictable from the independent variables. It indicates how well the independent variables explain the variability of the dependent variable.

The formula for R-squared is:

$$ \large R^2 = 1- \dfrac{SS_{RES}}{SS_{TOT}} = 1 - \dfrac{\sum_i(y_i - \hat y_i)^2}{\sum_i(y_i - \overline y_i)^2} $$

- **Parameters:**
  - $\( R^2 \)$: Coefficient of determination
  - $\( SS_{RES} \)$: Sum of squares of residuals
  - $\( SS_{TOT} \)$: Total sum of squares
  - $\( y_i \)$: Observed value of the dependent variable for the \(i\)th observation
  - $\( \hat{y}_i \)$: Predicted value of the dependent variable for the \(i\)th observation
  - $\( \overline{y}_i \)$: Mean of the observed values of the dependent variable

These metrics provide different perspectives on model performance and are selected based on the specific characteristics of the problem at hand. It's essential to choose metrics that align with the objectives and requirements of the task.
