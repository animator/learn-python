
**Feature:**

In the context of machine learning, a feature (also known as a variable
or attribute) is an individual measurable property or characteristic of
a data point that is used as input for a machine learning algorithm.
Features can be numerical, categorical, or text-based, and they
represent different aspects of the data that are relevant to the problem
at hand.

For example, in a dataset of housing prices, features could include the
number of bedrooms, the square footage, the location, and the age of the
property. In a dataset of customer demographics, features could include
age, gender, income level, and occupation.

**What is Feature Engineering?**

Feature engineering is the process of transforming raw data into
features that are suitable for machine learning models. In other words,
it is the process of selecting, extracting, and transforming the most
relevant features from the available data to build more accurate and
efficient machine learning models.

**Why need it?**

*Improve User Experience:* The primary reason we engineer features is to
enhance the user experience of a product or service. By adding new
features, we can make the product more intuitive, efficient, and
user-friendly, which can increase user satisfaction and engagement.

*Competitive Advantage:* Another reason we engineer features is to gain
a competitive advantage in the marketplace. By offering unique and
innovative features, we can differentiate our product from competitors
and attract more customers.

*Meet Customer Needs:* We engineer features to meet the evolving needs
of customers. By analyzing user feedback, market trends, and customer
behavior, we can identify areas where new features could enhance the
product's value and meet customer needs.

*Increase Revenue:* Features can also be engineered to generate more
revenue. For example, a new feature that streamlines the checkout
process can increase sales, or a feature that provides additional
functionality could lead to more upsells or cross-sells.

*Future-Proofing:* Engineering features can also be done to future-proof
a product or service. By anticipating future trends and potential
customer needs, we can develop features that ensure the product remains
relevant and useful in the long term.

![FE](https://tse3.mm.bing.net/th?id=OIP.sCoM-hxdiEZW73coQYeQawHaDA&pid=Api&P=0&h=180)

**Processes involved:-**

-   Feature Transformation

-   Feature Construction

-   Feature Extraction

-   Feature Selection

**FEATURE TRANSFORMATION:-**

Feature Transformation is the process of transforming the features into
a more suitable representation for the machine learning model. This is
done to ensure that the model can effectively learn from the data.

-   Missing Value Imputation
-   Handling Categorical Values
-   Outlier Detection
-   Feature Scaling

1.) Missing Value Imputation

Missing value imputation is a critical step in data preprocessing where
missing data points are filled in with estimated values.

-   Simple Imputation

-   K-Nearest Neighbours (KNN) Imputation

-   Multivariate Imputation by Chained Equations (MICE)

**SIMPLE IMPUTATION**
:
``` python
#Simple Imputation
#Lets first create Some sample dataset
import numpy as np
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': ['cat', 'dog', np.nan, 'mouse', 'rabbit']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
```

Output:

     Original DataFrame:
         A    B       C
    0  1.0  NaN     cat
    1  2.0  2.0     dog
    2  NaN  3.0     NaN
    3  4.0  4.0   mouse
    4  5.0  5.0  rabbit

Mean Imputation

``` python
from sklearn.impute import SimpleImputer

# Mean Imputation for numerical columns
mean_imputer = SimpleImputer(strategy='mean')
df['A'] = mean_imputer.fit_transform(df[['A']])

print("\nDataFrame after Mean Imputation:")
print(df)
```
Output: 

    DataFrame after Mean Imputation:
         A    B       C
    0  1.0  NaN     cat
    1  2.0  2.0     dog
    2  3.0  3.0     NaN
    3  4.0  4.0   mouse
    4  5.0  5.0  rabbit

The above code performs Mean imputation.

Replacing missing values with the mean of the column

`SimpleImputer` is a class in the `sklearn.impute` module of the
Scikit-learn library, used for handling missing data by providing basic
strategies for imputing missing values. It replaces missing values with
specified constant values or statistical values (like mean, median, or
mode) of the corresponding column.

Above code selects the column A and then replaces `NaN` with mean of the
column

``` python
# Median Imputation for numerical columns
median_imputer = SimpleImputer(strategy='median')
df['B'] = median_imputer.fit_transform(df[['B']])

print("\nDataFrame after Median Imputation:")
print(df)
```

Output:

    DataFrame after Median Imputation:
         A    B       C
    0  1.0  3.5     cat
    1  2.0  2.0     dog
    2  3.0  3.0     NaN
    3  4.0  4.0   mouse
    4  5.0  5.0  rabbit

Above code is for median imputation.

Replacing missing values with the median of the column. Useful for
skewed distributions.

Above code selects the column B and then replaces `Nan` with the median
of the column.

**KNN IMPUTATION**

``` python
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
# Sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [7, 8, 9, np.nan, 11]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Initialize the KNNImputer
knn_imputer = KNNImputer(n_neighbors=3)

# Fit the imputer and transform the data
df_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)

print("\nDataFrame after KNN Imputation:")
print(df_imputed)
```

Output: 

    Original DataFrame:
         A    B     C
    0  1.0  NaN   7.0
    1  2.0  2.0   8.0
    2  NaN  3.0   9.0
    3  4.0  4.0   NaN
    4  5.0  5.0  11.0


    DataFrame after KNN Imputation:
              A    B          C
    0  1.000000  3.0   7.000000
    1  2.000000  2.0   8.000000
    2  2.333333  3.0   9.000000
    3  4.000000  4.0   9.333333
    4  5.000000  5.0  11.000000

KNN (K-Nearest Neighbors) imputation is a method that replaces missing
values by considering the values of the nearest neighbors. The KNN
imputer finds the k-nearest neighbors of an instance with missing values
and then uses their values to fill in the gaps. This method can handle
both numerical and categorical data, and it tends to be more robust than
simpler imputation methods like mean or median imputation.

Scikit-learn provides a `KNNImputer` class in the `sklearn.impute`
module, which makes it straightforward to perform KNN imputation.

**MULTIVARIATE IMPUTATION BY CHAINED EQUATIONS**

``` python
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [7, 8, 9, np.nan, 11]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Initialize the IterativeImputer
mice_imputer = IterativeImputer(max_iter=10, random_state=0)

# Fit the imputer and transform the data
df_imputed = pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)

print("\nDataFrame after MICE Imputation:")
print(df_imputed)
```

Output: 

    Original DataFrame:
         A    B     C
    0  1.0  NaN   7.0
    1  2.0  2.0   8.0
    2  NaN  3.0   9.0
    3  4.0  4.0   NaN
    4  5.0  5.0  11.0

    DataFrame after MICE Imputation:
             A         B          C
    0  1.00000  0.999988   7.000000
    1  2.00000  2.000000   8.000000
    2  3.00005  3.000000   9.000000
    3  4.00000  4.000000   9.999993
    4  5.00000  5.000000  11.000000

Multivariate Imputation by Chained Equations (MICE), also known as Fully
Conditional Specification (FCS), is a method for handling missing data
by iteratively imputing each missing value using a regression model. It
allows for complex relationships between variables and can provide more
accurate imputations than simpler methods.

In this example, the `IterativeImputer` iteratively imputes the missing
values in columns \'A\', \'B\', and \'C\' using regression models. This
imputation method takes into account the relationships between all the
columns, providing a more accurate imputation than simpler methods.

2.)Handling categorical values Handling categorical values is a critical
step in feature transformation for machine learning. Categorical data
can be transformed into numerical values in various ways to make them
suitable for modeling.

Common techniques used to handle categorical values:-

-   One Hot Encoding

-   Label Encoding

-   Ordinal Encoding

**One-Hot Encoding**

One-hot encoding transforms categorical variables into a set of binary
columns. Each category is represented as a binary column (0 or 1).

``` python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample DataFrame
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Initialize the OneHotEncoder
onehot_encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the data
onehot_encoded = onehot_encoder.fit_transform(df[['Color']])

# Create a DataFrame with the encoded features
onehot_encoded_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['Color']))

print(onehot_encoded_df)
```

Output: 

       Color_Blue  Color_Green  Color_Red
    0         0.0          0.0        1.0
    1         1.0          0.0        0.0
    2         0.0          1.0        0.0
    3         1.0          0.0        0.0
    4         0.0          0.0        1.0

Above code performs one hot encoding. `get_features_names_out` extracts
the features present in the dataset.

**Label Encoding**

Label encoding converts each category into a numerical value. This can
be useful for ordinal data but may not be suitable for nominal data
since it introduces an ordinal relationship between categories.

``` python
from sklearn.preprocessing import LabelEncoder

# Sample DataFrame
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the data
df['Color_Encoded'] = label_encoder.fit_transform(df['Color'])

print(df)
```

Output: 

       Color  Color_Encoded
    0    Red              2
    1   Blue              0
    2  Green              1
    3   Blue              0
    4    Red              2

`LabelEncoder` assigns each color in the above code with a numerical
value.

Blue - 0

Green - 1

Red - 2

**Ordinal Encoding**

Ordinal encoding is useful for ordinal categorical data where there is
an inherent order. It assigns integers to categories while preserving
the order.

``` python
from sklearn.preprocessing import OrdinalEncoder

# Sample DataFrame
data = {'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']}
df = pd.DataFrame(data)

# Initialize the OrdinalEncoder
ordinal_encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])

# Fit and transform the data
df['Size_Encoded'] = ordinal_encoder.fit_transform(df[['Size']])

print(df)
```

Output: 
   
         Size  Size_Encoded
    0   Small           0.0
    1  Medium           1.0
    2   Large           2.0
    3  Medium           1.0
    4   Small           0.0

Above code encodes the ordinal data \[Small,Medium,Large\] based on
their ranking by assigning a numerical value to it .

3.)Outlier Detection:Outlier detection is an important step in data
preprocessing as outliers can significantly affect the performance of
machine learning models. Outliers are data points that differ
significantly from other observations in the dataset. Detecting and
handling outliers can improve model accuracy and reliability.

Here are some common techniques for detecting outliers:

-   Z-score
-   Interquartile Range (IQR)

**Z-Score (Standard Score)**

Z-score is a measure of how many standard deviations a data point is
from the mean. It assumes that the data follows a Gaussian (normal)
distribution.

![Zscore](https://tse4.mm.bing.net/th?id=OIP.WF_pHaZPSWI5RNvMOcH8zQAAAA&pid=Api&P=0&h=180)

``` python
import numpy as np
import pandas as pd

# Sample DataFrame
data = {'Value': [10, 12, 12, 13, 12, 14, 100, 12, 15, 10, 12]}
df = pd.DataFrame(data)

# Calculate Z-scores
df['Z-Score'] = (df['Value'] - df['Value'].mean()) / df['Value'].std()

# Identify outliers
threshold = 3
df['Outlier'] = df['Z-Score'].abs() > threshold

print(df)
```


Output: 

        Value   Z-Score  Outlier
    0      10 -0.384024    False
    1      12 -0.308591    False
    2      12 -0.308591    False
    3      13 -0.270874    False
    4      12 -0.308591    False
    5      14 -0.233158    False
    6     100  3.010478     True
    7      12 -0.308591    False
    8      15 -0.195441    False
    9      10 -0.384024    False
    10     12 -0.308591    False


Particular data item z-score is calculated and if value is greater than
given threshold value then it returns `True` else `False`


**Interquartile Range (IQR)**

The IQR method is based on the quartiles of the data. Outliers are
defined as points outside the range \[Q1 - 1.5 \* IQR, Q3 + 1.5 \*
IQR\], where Q1 is the first quartile and Q3 is the third quartile.

``` python
# Calculate IQR
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
df['Outlier'] = (df['Value'] < lower_bound) | (df['Value'] > upper_bound)

print(df)
```

Output: 

        Value   Z-Score  Outlier
    0      10 -0.384024    False
    1      12 -0.308591    False
    2      12 -0.308591    False
    3      13 -0.270874    False
    4      12 -0.308591    False
    5      14 -0.233158    False
    6     100  3.010478     True
    7      12 -0.308591    False
    8      15 -0.195441    False
    9      10 -0.384024    False
    10     12 -0.308591    False


lower_bound and upper_bound mentions the range. Below lower_bound or
above upper_bound then data point is said to be an outlier




4.)Feature Scaling:Feature scaling is a crucial step in data
preprocessing for machine learning. It ensures that the numerical
features are on a similar scale, which can improve the performance of
many machine learning algorithms.

Here are some common methods of feature scaling:

-   Standardization
-   Normalisation


**Standardization**

It is also called z-score Normalisation.

`Z = (X - μ) / σ`


``` python
from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the data
df['Value_Standardized'] = scaler.fit_transform(df[['Value']])

print(df)
```

Output: 

        Value   Z-Score  Outlier  Value_Standardized
    0      10 -0.384024    False           -0.402768
    1      12 -0.308591    False           -0.323653
    2      12 -0.308591    False           -0.323653
    3      13 -0.270874    False           -0.284095
    4      12 -0.308591    False           -0.323653
    5      14 -0.233158    False           -0.244538
    6     100  3.010478     True            3.157416
    7      12 -0.308591    False           -0.323653
    8      15 -0.195441    False           -0.204980
    9      10 -0.384024    False           -0.402768
    10     12 -0.308591    False           -0.323653

Above code uses `StandardScaler` to standardize the values

**Normalisation**

-   MinMax Scaling

-   Robust Scaling

-   MaxAbs Scaling


**MinMax Scaling**

Min-max scaling transforms the features to a fixed range, usually \[0,
1\].

![MinMax](https://tse4.mm.bing.net/th?id=OIP.vBO3wyehnnOLY67eMrXt7wHaCS&pid=Api&P=0&h=180)


``` python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample DataFrame
data = {'Value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
df['Value_Scaled'] = scaler.fit_transform(df[['Value']])

print(df)
```

Output:

       Value  Value_Scaled
    0     10          0.00
    1     20          0.25
    2     30          0.50
    3     40          0.75
    4     50          1.00

`MinMaxScaler` is used to perform MinMaxScaling.


**Robust Scaling**

Robust scaling uses the median and the interquartile range (IQR). It is
useful for data with outliers.

![Robust](https://tse1.mm.bing.net/th?id=OIP.g0PtmCXLTAQJmzKyAUJQPAAAAA&pid=Api&P=0&h=180)

``` python
from sklearn.preprocessing import RobustScaler

# Initialize the RobustScaler
scaler = RobustScaler()

# Fit and transform the data
df['Value_Robust'] = scaler.fit_transform(df[['Value']])

print(df)
```
Output:

          Value  Value_Scaled  Value_Robust
      0     10          0.00          -1.0
      1     20          0.25          -0.5
      2     30          0.50           0.0
      3     40          0.75           0.5
      4     50          1.00           1.0

`RobustScaler' is used for performing Robust Scaling

**MaxAbs Scaling**

MaxAbs scaling scales each feature by its maximum absolute value. The
result is a dataset where each feature has a range of \[-1, 1\].

![MaxAbs](https://tse4.mm.bing.net/th?id=OIP.dQzNvcQua99b3Pwyk0VnoAAAAA&pid=Api&P=0&h=180)

``` python
from sklearn.preprocessing import MaxAbsScaler

# Initialize the MaxAbsScaler
scaler = MaxAbsScaler()

# Fit and transform the data
df['Value_MaxAbs'] = scaler.fit_transform(df[['Value']])

print(df)
```
Output:

        Value  Value_Scaled  Value_Robust  Value_MaxAbs
      0     10          0.00          -1.0           0.2
      1     20          0.25          -0.5           0.4
      2     30          0.50           0.0           0.6
      3     40          0.75           0.5           0.8
      4     50          1.00           1.0           1.0

`MaxAbsScaler` performs the MaxAbs Scaling

**FEATURE CONSTRUCTION**

Feature construction, involves creating new features from the existing
ones to improve the performance of machine learning models.

-   Polynomial Features

-   Interaction Features

-   Logarithmic and Exponential Transformations

**Polynomial Features**

Creating polynomial features involves generating new features by taking
combinations of existing features to a certain power.

``` python
from sklearn.preprocessing import PolynomialFeatures

# Sample data
X = [[2, 3], [3, 4], [4, 5]]

# Create polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

print(X_poly)
```

Output:

    [[ 1.  2.  3.  4.  6.  9.]
     [ 1.  3.  4.  9. 12. 16.]
     [ 1.  4.  5. 16. 20. 25.]]

If you have a feature X , polynomial features could be X\^2, X\^3

**Interaction Features**

Interaction features are created by multiplying two or more existing
features to capture interactions between variables.

``` python
import pandas as pd

# Sample data
X = pd.DataFrame({'X1': [1, 2, 3], 'X2': [4, 5, 6]})

# Create interaction features
X['X1_X2'] = X['X1'] * X['X2']

print(X)
```
Output:

     X1  X2  X1_X2
    0   1   4      4
    1   2   5     10
    2   3   6     18
    
For features 𝑋1 and 𝑋2, interaction features could be 𝑋 1 × 𝑋 2

**Logarithmic and Exponential Transformations**

Applying logarithmic or exponential transformations can stabilize
variance and make the data more normally distributed.

``` python
import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5])

# Apply logarithmic transformation
X_log = np.log(X)

print(X_log)
```
Output:

    [0.         0.69314718 1.09861229 1.38629436 1.60943791]
    
For a feature 𝑋 , a logarithmic transformation could be log ( 𝑋 )

**FEATURE EXTRACTION**

Feature extraction is a process of transforming raw data into a set of
features that can be used for machine learning models. The goal is to
reduce the dimensionality of the data while preserving its relevant
information.

-   Principal Component Analysis
-   Linear Discriminant Analysis

**Principal Component Analysis (PCA)**

Principal Component Analysis (PCA) is a technique that transforms the
data into a new coordinate system such that the greatest variances by
any projection of the data come to lie on the first coordinates (called
principal components).

``` python
from sklearn.decomposition import PCA
import numpy as np

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Apply PCA
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)

print(X_pca)
```

Output:

    [[ 4.24264069]
     [ 1.41421356]
     [-1.41421356]
     [-4.24264069]]

`PCA` is used for Principal component analysis

**Linear Discriminant Analysis (LDA)**

Linear Discriminant Analysis (LDA) is a technique used to find a linear
combination of features that separates two or more classes of objects or
events.

``` python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import numpy as np

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 1, 0, 1])

# Apply LDA
lda = LDA(n_components=1)
X_lda = lda.fit_transform(X, y)

print(X_lda)
```
Output:

    [[-1.06066017]
     [-0.35355339]
     [ 0.35355339]
     [ 1.06066017]]

`LinearDiscriminantAnalysis` is used

**Feature Selection**

Feature selection is the process of selecting a subset of relevant
features (variables, predictors) for use in model construction. It helps
in improving model performance, reducing overfitting, and decreasing
computational cost.

-   Filter methods

-   Wrapper methods

-   Embedded methods

**Filter Methods**

Filter methods apply statistical measures to score the relevance of
features. They are computationally efficient and independent of any
machine learning algorithms.

Examples:

1.  Correlation Coefficient
2.  Chi-Square Test
3.  ANOVA

**Wrapper Methods**

Wrapper methods evaluate the performance of a subset of features using a
specific machine learning algorithm. They are more computationally
intensive compared to filter methods.

Examples:

1.  Forward Selection
2.  Backward Elimination
3.  Recursive Feature Elimination (RFE)

**Embedded Methods**

Embedded methods perform feature selection as part of the model training
process. They include methods like regularization and tree-based
methods.

Examples:

1.  Lasso (L1 Regularization)
2.  Ridge (L2 Regularization)
3.  Decision Trees

