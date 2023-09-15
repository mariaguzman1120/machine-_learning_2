DBSCAN
=

Clustering analysis or simply Clustering is basically an Unsupervised learning method that divides the data points into a number of specific batches or groups, such that the data points in the same groups have similar properties and data points in different groups have different properties in some sense. Clusters are dense regions in the data space, separated by regions of the lower density of points. The DBSCAN algorithm is based on this intuitive notion of “clusters” and “noise”. The key idea is that for each point of a cluster, the neighborhood of a given radius has to contain at least a minimum number of points. 

a. In which cases might it be more useful to apply?
-
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm used to group data sets based on their density in an n-dimensional space. Unlike distance-based clustering methods, DBSCAN is able to find arbitrarily-shaped clusters and is less sensitive to outliers and noise in the data.

1. Geolocation data analysis: DBSCAN is often used to analyze datasets of geographic coordinates to find groups of nearby locations that may indicate the presence of points of interest, traffic patterns, etc.
2. Image segmentation: DBSCAN can be used to segment images into groups of similar pixels, which can be useful in object recognition applications and image analysis.
3. Social media analysis: DBSCAN can be used to analyze social media datasets to find groups of users who share similar interests, which can be useful for market segmentation and personalized advertising campaigns.


b. What are the mathematical fundamentals of it?
-

eps: It defines the neighborhood around a data point i.e. if the distance between two points is lower or equal to ‘eps’ then they are considered neighbors. If the eps value is chosen too small then a large part of the data will be considered as an outlier. If it is chosen very large then the clusters will merge and the majority of the data points will be in the same clusters. One way to find the eps value is based on the k-distance graph.
MinPts: Minimum number of neighbors (data points) within eps radius. The larger the dataset, the larger value of MinPts must be chosen. As a general rule, the minimum MinPts can be derived from the number of dimensions D in the dataset as, MinPts >= D+1. The minimum value of MinPts must be chosen at least 3.

GeeksforGeeks. (2023). DBSCAN Clustering in Machine Learning (Density-Based Clustering). GeeksforGeeks. https://www.geeksforgeeks.org/dbscan-clustering-in-ml-density-based-clustering/

c. Is there any relation between DBSCAN and Spectral Clustering? If so, what is it?
-

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) and Spectral Clustering are two different clustering techniques used in machine learning, and they have distinct approaches and principles. that they have different characteristics:

DBSCAN is a density-based clustering algorithm that excels at finding clusters of varying shapes and handling noisy data. It does not require specifying the number of clusters in advance and can discover clusters based on the density of data points.

Spectral Clustering, on the other hand, is based on spectral graph theory and focuses on discovering clusters using the eigenvalues and eigenvectors of a similarity graph. It is effective at capturing complex relationships between data points but may require specifying the number of clusters in advance or using additional techniques to determine cluster numbers.


