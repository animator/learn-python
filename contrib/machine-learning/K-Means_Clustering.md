# K-Means Clustering 
Unsupervised Learning Algorithm for Grouping Similar Data.
## Introduction
K-means clustering is a fundamental unsupervised machine learning algorithm that excels at grouping similar data points together. It's a popular choice due to its simplicity and efficiency in uncovering hidden patterns within unlabeled datasets.
## Unsupervised Learning
Unlike supervised learning algorithms that rely on labeled data for training, unsupervised algorithms, like K-means, operate solely on input data (without predefined categories). Their objective is to discover inherent structures or groupings within the data.
## The K-Means Objective
Organize similar data points into clusters to unveil underlying patterns. The main objective is to minimize total intra-cluster variance or the squared function.

![enter image description here](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQnDTFfxrrAttYMwwjZV0RAA8J8rmUxgrnWc2gU_ArEqrxEMlHm)
## Clusters and Centroids
A cluster represents a collection of data points that share similar characteristics. K-means identifies a pre-determined number (k) of clusters within the dataset. Each cluster is represented by a centroid, which acts as its central point (imaginary or real).
## Minimizing In-Cluster Variation
The K-means algorithm strategically assigns each data point to a cluster such that the total variation within each cluster (measured by the sum of squared distances between points and their centroid) is minimized. In simpler terms, K-means strives to create clusters where data points are close to their respective centroids.
## The Meaning Behind "K-Means"
The "means" in K-means refers to the averaging process used to compute the centroid, essentially finding the center of each cluster.
## K-Means Algorithm in Action
![enter image description here](https://d3i71xaburhd42.cloudfront.net/2f49631bb3103a61fbc3045dd035c3d8f2175887/11-Figure2-1.png)
The K-means algorithm follows an iterative approach to optimize cluster formation:

1.  **Initial Centroid Placement:** The process begins with randomly selecting k centroids to serve as initial reference points for each cluster.
2.  **Data Point Assignment:** Each data point is assigned to the closest centroid, effectively creating a preliminary clustering.
3.  **Centroid Repositioning:** Once data points are assigned, the centroids are recalculated by averaging the positions of the points within their respective clusters. These new centroids represent the refined centers of the clusters.
4.  **Iteration Until Convergence:** Steps 2 and 3 are repeated iteratively until a stopping criterion is met. This criterion can be either:
    -   **Centroid Stability:** No significant change occurs in the centroids' positions, indicating successful clustering.
    -   **Reaching Maximum Iterations:** A predefined number of iterations is completed.
 ##  Code
 Following is a simple implementation of K-Means.
 
	
	# Generate and Visualize Sample Data
	# import the necessary Libraries 
	
	import numpy as np
	import matplotlib.pyplot as plt

    # Create data points for cluster 1 and cluster 2
	X = -2 * np.random.rand(100, 2) 
	X1 = 1 + 2 * np.random.rand(50, 2)
	
	# Combine data points from both clusters  
	X[50:100, :] = X1
	  
    # Plot data points and display the plot
	plt.scatter(X[:, 0], X[:, 1], s=50, c='b')  
	plt.show()  

	# K-Means Model Creation and Training 
	from sklearn.cluster import KMeans
    
    # Create KMeans object with 2 clusters
	kmeans = KMeans(n_clusters=2)  
	kmeans.fit(X)  # Train the model on the data

	# Visualize Data Points with Centroids 
	centroids = kmeans.cluster_centers_  # Get centroids (cluster centers)

	plt.scatter(X[:, 0], X[:, 1], s=50, c='b')  # Plot data points again
	plt.scatter(centroids[0, 0], centroids[0, 1], s=200, c='g', marker='s')  # Plot centroid 1
	plt.scatter(centroids[1, 0], centroids[1, 1], s=200, c='r', marker='s')  # Plot centroid 2
	plt.show()  # Display the plot with centroids

	# Predict Cluster Label for New Data Point 
	new_data = np.array([-3.0, -3.0])
	new_data_reshaped = new_data.reshape(1, -1)
	predicted_cluster = kmeans.predict(new_data_reshaped)
	print("Predicted cluster for new data:", predicted_cluster)

 ### Output:
 Before Implementing K-Means Clustering :
![Before Implementing K-Means Clustering](https://miro.medium.com/v2/resize:fit:640/format:webp/1*jnyQxmEj7rFhazeMH7KXVg.png)
                    
 
 After Implementing K-Means Clustering:![enter image description here](https://miro.medium.com/v2/resize:fit:640/format:webp/1*H3L3EH3Jh6kWFmbec0ewKA.png)
## Conclusion
**K-Means** can be applied to data that has a smaller number of dimensions, is numeric, and is continuous or can be used to find groups that have not been explicitly labeled in the data. As an example, it can be used for Document Classification, Delivery Store Optimization, or Customer Segmentation.




 

	

