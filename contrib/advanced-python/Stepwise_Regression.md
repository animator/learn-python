## Stepwise Regression


# Definition
Stepwise Regression is a method of fitting regression models in which the choice of predictive variables is carried out by an automatic procedure. This technique is useful for identifying a subset of variables that have the most significant impact on the dependent variable.

# Purpose
The main goal of Stepwise Regression is to simplify the model by including only the most significant variables, thereby improving model interoperability and performance.

# Types
Forward Selection: Starts with no variables in the model, testing each variable one by one, and adding them if they improve the model significantly.
Backward Elimination: Starts with all candidate variables and removes the least significant variables one at a time.
Bidirectional Elimination: A combination of forward selection and backward elimination.
# Steps Involved

## Forward Selection:

Begin with an empty model.
Add the predictor that improves the model the most (lowest p-value).
Continue adding predictors one by one until no further significant improvement is made.
Backward Elimination:

Start with all candidate predictors.
Remove the predictor with the highest p-value (least significant).
Continue removing predictors until all remaining predictors are statistically significant.
Bidirectional Elimination:

Combine forward selection and backward elimination steps iteratively.
Add significant predictors and remove non-significant ones in each step until the model stabilizes.
Practical Example in Python
Here's an example using the statsmodels library:

# code
import statsmodels.api as sm
import pandas as pd
import numpy as np

# Sample Data
np.random.seed(0)
X = pd.DataFrame({
    'X1': np.random.randn(100),
    'X2': np.random.randn(100),
    'X3': np.random.randn(100)
})
y = 1 + 2*X['X1'] + 0.5*X['X2'] + np.random.randn(100)

# Forward Selection
def forward_selection(X, y):
    initial_features = []
    remaining_features = list(X.columns)
    best_features = []
    while remaining_features:
        scores_with_candidates = []
        for candidate in remaining_features:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[initial_features + [candidate]]))).fit()
            score = model.aic
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_score, best_candidate = scores_with_candidates[0]
        initial_features.append(best_candidate)
        remaining_features.remove(best_candidate)
        best_features.append(best_candidate)
    return best_features

# Applying Forward Selection
selected_features = forward_selection(X, y)
print("Selected features:", selected_features)

# Building final model with selected features
final_model = sm.OLS(y, sm.add_constant(X[selected_features])).fit()
print(final_model.summary())

This code demonstrates forward selection by iteratively adding features to the model and selecting the ones that improve the model's AIC (Akaike Information Criterion) the most. The final model is then built using the selected features.