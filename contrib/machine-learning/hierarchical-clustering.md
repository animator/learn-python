# Hierarchical Clustering

Hierarchical Clustering is a method of cluster analysis that seeks to build a hierarchy of clusters. This README provides an overview of the hierarchical clustering algorithm, including its fundamental concepts, types, steps, and how to implement it using Python.

## Introduction

Hierarchical Clustering is an unsupervised learning method used to group similar objects into clusters. Unlike other clustering techniques, hierarchical clustering does not require the number of clusters to be specified beforehand. It produces a tree-like structure called a dendrogram, which displays the arrangement of the clusters and their sub-clusters.

## Concepts

### Dendrogram

A dendrogram is a tree-like diagram that records the sequences of merges or splits. It is a useful tool for visualizing the process of hierarchical clustering.

### Distance Measure

Distance measures are used to quantify the similarity or dissimilarity between data points. Common distance measures include Euclidean distance, Manhattan distance, and cosine similarity.

### Linkage Criteria

Linkage criteria determine how the distance between clusters is calculated. Different linkage criteria include single linkage, complete linkage, average linkage, and Ward's linkage.

## Types of Hierarchical Clustering

1. **Agglomerative Clustering (Bottom-Up Approach)**: 
    - Starts with each data point as a separate cluster.
    - Repeatedly merges the closest pairs of clusters until only one cluster remains or a stopping criterion is met.

2. **Divisive Clustering (Top-Down Approach)**: 
    - Starts with all data points in a single cluster.
    - Repeatedly splits clusters into smaller clusters until each data point is its own cluster or a stopping criterion is met.

## Steps in Hierarchical Clustering

1. **Calculate Distance Matrix**: Compute the distance between each pair of data points.
2. **Create Clusters**: Treat each data point as a single cluster.
3. **Merge Closest Clusters**: Find the two clusters that are closest to each other and merge them into a single cluster.
4. **Update Distance Matrix**: Update the distance matrix to reflect the distance between the new cluster and the remaining clusters.
5. **Repeat**: Repeat steps 3 and 4 until all data points are merged into a single cluster or the desired number of clusters is achieved.

## Linkage Criteria

1. **Single Linkage (Minimum Linkage)**: The distance between two clusters is defined as the minimum distance between any single data point in the first cluster and any single data point in the second cluster.
2. **Complete Linkage (Maximum Linkage)**: The distance between two clusters is defined as the maximum distance between any single data point in the first cluster and any single data point in the second cluster.
3. **Average Linkage**: The distance between two clusters is defined as the average distance between all pairs of data points, one from each cluster.
4. **Ward's Linkage**: The distance between two clusters is defined as the increase in the sum of squared deviations from the mean when the two clusters are merged.

## Implementation

### Using Scikit-learn

Scikit-learn is a popular machine learning library in Python that provides tools for hierarchical clustering.

### Code Example

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('path/to/your/dataset.csv')

# Preprocess the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Perform hierarchical clustering
Z = linkage(data_scaled, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Perform Agglomerative Clustering
agg_clustering = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
labels = agg_clustering.fit_predict(data_scaled)

# Add cluster labels to the original data
data['Cluster'] = labels
print(data.head())
```

## Evaluation Metrics

- **Silhouette Score**: Measures how similar a data point is to its own cluster compared to other clusters.
- **Cophenetic Correlation Coefficient**: Measures how faithfully a dendrogram preserves the pairwise distances between the original data points.
- **Dunn Index**: Ratio of the minimum inter-cluster distance to the maximum intra-cluster distance.

## Conclusion

Hierarchical clustering is a versatile and intuitive method for clustering data. It is particularly useful when the number of clusters is not known beforehand. By understanding the different linkage criteria and evaluation metrics, one can effectively apply hierarchical clustering to various types of data.
