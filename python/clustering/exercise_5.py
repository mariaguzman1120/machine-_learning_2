# External libraries
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from unsupervised.clustering import KMeans, KMedoids
from python.utils.silhouette import plot_silhouette_comparison

def executor():
    X, y = make_blobs(
        n_samples=500,
        n_features=2,
        centers=4,
        cluster_std=1,
        center_box=(-10.0, 10.0),
        shuffle=True,
        random_state=1,
    )

    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

    for clusters in range(1, 6):
        try:
            kmeans = KMeans(n_clusters=clusters)
            kmedoids = KMedoids(n_clusters=clusters)

            kmeans_labels = kmeans.fit_transform(X)
            kmedoids_labels = kmedoids.fit_transform(X)

            plot_silhouette_comparison(X, kmeans_labels, kmedoids_labels)

        except Exception as e:
            print(e)
