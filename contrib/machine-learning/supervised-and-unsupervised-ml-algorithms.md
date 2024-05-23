# **Supervised Machine Learning**

Supervised learning algorithms are trained using labeled data. This means the model is provided with input-output pairs, and it learns to map inputs to the desired outputs.

### **Linear Regression**
**Description**: Linear Regression is used for predicting a continuous value. It finds the best-fit line through the data points.

**Use Case Example**: Predicting house prices based on features like size, location, and number of rooms.

**Key Points**:
- Simple and interpretable.
- Sensitive to outliers.

**Image Idea**: ![Linear Regression](url-to-linear-regression-image)

### **Decision Trees**
**Description**: Decision Trees split the data into subsets based on the value of input features, creating a tree structure.

**Use Case Example**: Classifying whether an email is spam or not based on words present in the email.

**Key Points**:
- Easy to understand and interpret.
- Can handle both numerical and categorical data.
- Prone to overfitting.

**Image Idea**: ![Decision Tree](url-to-decision-tree-image)

### **Support Vector Machines (SVM)**
**Description**: SVM finds the hyperplane that best separates the classes in the input feature space.

**Use Case Example**: Image classification (e.g., distinguishing between cats and dogs).

**Key Points**:
- Effective in high-dimensional spaces.
- Works well with clear margin of separation.
- Sensitive to the choice of kernel.

**Image Idea**: ![SVM](url-to-svm-image)

# **Unsupervised Machine Learning**

Unsupervised learning algorithms work with unlabeled data. The model tries to learn the underlying structure of the data.

### **K-Means Clustering**
**Description**: K-Means Clustering partitions the data into K distinct clusters based on feature similarity.

**Use Case Example**: Customer segmentation in marketing to identify distinct customer groups.

**Key Points**:
- Simple and easy to implement.
- Assumes clusters are spherical and equally sized.
- Requires specifying the number of clusters (K) beforehand.

**Image Idea**: ![K-Means Clustering](url-to-k-means-clustering-image)

### **Principal Component Analysis (PCA)**
**Description**: PCA reduces the dimensionality of data by transforming to a new set of variables (principal components) that are orthogonal.

**Use Case Example**: Reducing the number of features in a dataset while retaining most of the variance.

**Key Points**:
- Useful for data visualization.
- Helps in reducing computational cost.
- Sensitive to the scaling of the data.

**Image Idea**: ![PCA](url-to-pca-image)

### **Association Rules**
**Description**: Association Rules discover interesting relationships or associations between variables in large datasets.

**Use Case Example**: Market basket analysis to find associations between products bought together.

**Key Points**:
- Helps in understanding the relationship between items.
- Measures like support, confidence, and lift are used.

**Image Idea**: ![Association Rules](url-to-association-rules-image)
