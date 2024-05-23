# **Supervised Machine Learning**

Supervised learning algorithms are trained using labeled data. This means the model is provided with input-output pairs, and it learns to map inputs to the desired outputs.

### **Linear Regression**
**Description**: Linear Regression is used for predicting a continuous value. It finds the best-fit line through the data points.

**Use Case Example**: Predicting house prices based on features like size, location, and number of rooms.

**Key Points**:
- Simple and interpretable.
- Sensitive to outliers.

![Linear Regression](https://static.javatpoint.com/tutorial/machine-learning/images/linear-regression-in-machine-learning.png)

### **Decision Trees**
**Description**: Decision Trees split the data into subsets based on the value of input features, creating a tree structure.

**Use Case Example**: Classifying whether an email is spam or not based on words present in the email.

**Key Points**:
- Easy to understand and interpret.
- Can handle both numerical and categorical data.
- Prone to overfitting.

![Decision Tree](https://imgs.search.brave.com/esTzDDMBHsnp8wjalK-eu9YbUif9-EOHY6TuCY7tlLo/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZWVrc2Zvcmdl/ZWtzLm9yZy93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMzA0MjQx/NDE3MjcvRGVjaXNp/b24tVHJlZS53ZWJw)

### **Support Vector Machines (SVM)**
**Description**: SVM finds the hyperplane that best separates the classes in the input feature space.

**Use Case Example**: Image classification (e.g., distinguishing between cats and dogs).

**Key Points**:
- Effective in high-dimensional spaces.
- Works well with clear margin of separation.
- Sensitive to the choice of kernel.

![SVM](https://imgs.search.brave.com/zW6OP_38IXxA882c1U3GXvSBKQVbmnSNxH14a4rQYWM/rs:fit:500:0:0/g:ce/aHR0cDovL3Jlcy5j/bG91ZGluYXJ5LmNv/bS9keWQ5MTFrbWgv/aW1hZ2UvdXBsb2Fk/L2ZfYXV0byxxX2F1/dG86YmVzdC92MTUy/NjI4ODQ1My9pbmRl/eDNfc291b2F6LnBu/Zw)

# **Unsupervised Machine Learning**

Unsupervised learning algorithms work with unlabeled data. The model tries to learn the underlying structure of the data.

### **K-Means Clustering**
**Description**: K-Means Clustering partitions the data into K distinct clusters based on feature similarity.

**Use Case Example**: Customer segmentation in marketing to identify distinct customer groups.

**Key Points**:
- Simple and easy to implement.
- Assumes clusters are spherical and equally sized.
- Requires specifying the number of clusters (K) beforehand.

![K-Means Clustering](https://imgs.search.brave.com/UUeVC05fNdfs2awFKlx8jyU5hz63XwombWbrtrSPwLw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zY2lr/aXQtbGVhcm4ub3Jn/L3N0YWJsZS9faW1h/Z2VzL3NwaHhfZ2xy/X3Bsb3RfYWZmaW5p/dHlfcHJvcGFnYXRp/b25fMDAxLnBuZw)

### **Principal Component Analysis (PCA)**
**Description**: PCA reduces the dimensionality of data by transforming to a new set of variables (principal components) that are orthogonal.

**Use Case Example**: Reducing the number of features in a dataset while retaining most of the variance.

**Key Points**:
- Useful for data visualization.
- Helps in reducing computational cost.
- Sensitive to the scaling of the data.

![PCA](https://i0.wp.com/statisticsbyjim.com/wp-content/uploads/2023/01/PCA_original.png?w=596&ssl=1)

### **Association Rules**
**Description**: Association Rules discover interesting relationships or associations between variables in large datasets.

**Use Case Example**: Market basket analysis to find associations between products bought together.

**Key Points**:
- Helps in understanding the relationship between items.
- Measures like support, confidence, and lift are used.

