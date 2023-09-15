import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from python.metadata.responses import Responses


"""
The elbow method is a graphical method for finding the 
optimal K value in a k-means clustering algorithm. 
The elbow graph shows the within-cluster-sum-of-square (WCSS)
values on the y-axis corresponding to the different values 
of K (on the x-axis). The optimal K value is the point at which
the graph forms an elbow.  

"""

def executor():
    data, _ = make_blobs(
        n_samples=300, centers=4, random_state=0, cluster_std=0.60)

    # Calculate WCSS for different values of k
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(
            n_clusters=i,
            init='k-means++',
            max_iter=300,
            n_init=10,
            random_state=0,
        )
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)

    # Plot the elbow method
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.show()

print(Responses.elbow)
