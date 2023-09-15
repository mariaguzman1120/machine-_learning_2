Spectral Clustering
=

Spectral Clustering is a variant of the clustering algorithm that uses the connectivity between the data points to form the clustering. It uses eigenvalues and eigenvectors of the data matrix to forecast the data into lower dimensions space to cluster the data points. It is based on the idea of a graph representation of data where the data point are represented as nodes and the similarity between the data points are represented by an edge. GeeksforGeeks. (2023). ML | Spectral Clustering. GeeksforGeeks. https://www.geeksforgeeks.org/ml-spectral-clustering/

a. In which cases might it be more useful to apply?
-

Non-spherical clusters: Unlike algorithms like k-means, which tend to find spherical clusters, spectral clustering can identify clusters with non-convex or irregular shapes.

Clusters with varying densities: Spectral clustering can detect clusters that have different point densities, which can be challenging for distance-based methods like k-means.

Non-linear dimensionality reduction: Spectral clustering can also be used for non-linear dimensionality reduction, as the eigenvectors of the Laplacian matrix represent a projection of the data into a lower-dimensional space.

Image segmentation: Spectral clustering can be used to segment images based on the similarity of pixels, taking into account both color intensity and spatial location of the pixels. This can help identify regions of interest in images with complex or irregular shapes.

Text analysis and natural language processing (NLP): Spectral clustering can be applied in text analysis to group documents or words based on their semantic similarity. This can be useful for identifying common themes, organizing large collections of documents, or improving search and recommendation systems.

b. What is the algorithm to compute it?
-

The mathematical foundations of spectral clustering are based on graph theory, linear algebra, and spectral analysis.

Graph: In the context of spectral clustering, each node corresponds to a data point, and the edges represent the similarity between the data points.

Similarity measure: To construct the graph, a similarity (or distance) measure between data points is needed. There are various similarity measures, such as Euclidean distance, Manhattan distance, or Gaussian kernel. The choice of similarity measure will depend on the specific problem and the nature of the data. 

Affinity matrix: The affinity matrix is a square matrix that stores the similarities between all pairs of data points. The elements of the affinity matrix (A) represent the similarity between data points i and j, with A(i, j) = 0 if the points are not connected in the graph.

Laplacian matrix: The Laplacian matrix is derived from the affinity matrix and is a central concept in spectral graph analysis. There are several ways to compute the Laplacian matrix, but the normalized Laplacian is the most common. It is calculated as L = D^(-1/2) * A * D^(-1/2), where D is a diagonal matrix with elements D(i, i) being the sum of row i in the affinity matrix.

Eigenvectors and eigenvalues: Eigenvectors and eigenvalues are fundamental concepts in linear algebra and are used in spectral analysis. In the context of spectral clustering, the eigenvectors and eigenvalues of the Laplacian matrix are calculated. The eigenvectors associated with the k smallest eigenvalues are used to transform the data into a lower-dimensional space.

Projection into a lower-dimensional space: The k selected eigenvectors are used to form a feature matrix (Y) that projects the data into a lower-dimensional space. This allows identifying the structure of the data and simplifying the clustering problem.

Clustering in the transformed space: Finally, a clustering algorithm, such as k-means, is applied in the transformed space using the feature matrix Y. This allows identifying clusters in the original data based on the structure revealed by the spectral analysis.


c. What is the algorithm to compute it?
-

1. Project data into  Rn matrix
2. Define an Affinity matrix A , using a Gaussian Kernel K or an Adjacency matrix
3. Construct the Graph Laplacian from A (i.e. decide on a normalization)
4. Solve the Eigenvalue problem
5. Select k eigenvectors corresponding to the k lowest (or highest) eigenvalues to define a k-dimensional subspace
6. Form clusters in this subspace using k-means

Gandhi, V. (2023). Spectral Clustering - Detailed Explanation. Kaggle. https://www.kaggle.com/code/vipulgandhi/spectral-clustering-detailed-explanation

d. Does it hold any relation to some of the concepts previously mentioned in class? Which, and how?
-

Spectral Clustering and K-means are both unsupervised learning algorithms, meaning they do not require prior class labels for clustering.Both methods aim to group data based on similarities, with the goal of forming clusters where points within a cluster are similar to each other and dissimilar to points in other clusters.

Spectral clustering employs similarity metrics like k-means 
and k-medoids to gauge the degree of similarity or dissimilarity 
among data points. It then leverages eigenvalues and eigenvectors to 
perform a transformation of the data, reducing it to a 
lower-dimensional space.


