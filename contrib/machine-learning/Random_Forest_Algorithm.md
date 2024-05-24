# Random Forest Algorithm

Random Forest is an ensemble learning method for classification, regression, and other tasks that operates by constructing multiple decision trees during training and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.

## How Random Forest Works

1. **Bootstrapping**: Multiple subsets of the training data are created by random sampling with replacement.
2. **Building Trees**: For each subset, a decision tree is built. During the construction, only a random subset of features is considered for splitting at each node.
3. **Aggregation**: The final prediction is made by averaging the predictions of all the individual trees (regression) or by taking the majority vote (classification).

## Advantages of Random Forest

- **Improved Accuracy**: By combining multiple trees, the overall performance improves.
- **Robustness**: It reduces overfitting by averaging multiple trees, making it robust to noise.
- **Feature Importance**: Provides a way to determine feature importance.

## Implementing Random Forest in Python

Below is a step-by-step guide to implementing the Random Forest algorithm using the popular `scikit-learn` library in Python.

### 1. Import Libraries

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
