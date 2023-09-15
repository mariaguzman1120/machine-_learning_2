# External libraries
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import DBSCAN, KMeans, SpectralClustering
from sklearn.metrics import silhouette_score
from sklearn_extra.cluster import KMedoids

warnings.simplefilter("ignore")


def generate_datasets(n_samples: int = 500) -> dict:
    """Generate and return a dictionary of toy datasets for clustering and
        classification.

    Args:
        n_samples: The number of samples to generate for each dataset.

    Returns:
        A dictionary containing various toy datasets for testing clustering
            and classification algorithms.

    """
    noisy_circles = datasets.make_circles(
        n_samples=n_samples, factor=0.5, noise=0.05
    )

    noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)

    blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)

    no_structure = np.random.rand(n_samples, 2), None

    # Anisotropically distributed data
    random_state = 170

    x, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)

    transformation = [[0.6, -0.6], [-0.4, 0.8]]

    x_aniso = np.dot(x, transformation)

    aniso = (x_aniso, y)

    # Blobs with varied variances
    varied = datasets.make_blobs(
        n_samples=n_samples,
        cluster_std=[1.0, 2.5, 0.5],
        random_state=random_state,
    )

    datasets_dic = {
        'noisy_circles': noisy_circles,
        'noisy_moons': noisy_moons,
        'blobs': blobs,
        'no_structure': no_structure,
        'aniso': aniso,
        'varied': varied,
    }

    return datasets_dic


def plot_datasets(datasets_dict: dict) -> None:
    """Plot scatter plots for multiple datasets in subplots.

    Args:
        datasets_dict: A dictionary of datasets where keys are dataset names
            and values are tuples (X, y) representing the data.

    Returns:
        None (displays the subplots).

    """
    num_datasets = len(datasets_dict)
    num_rows = int(np.ceil(num_datasets / 2))
    num_cols = 2

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    for i, (dataset_name, dataset) in enumerate(datasets_dict.items()):
        row = i // num_cols
        col = i % num_cols

        x, y = dataset

        ax = axes[row, col]

        ax.scatter(x[:, 0], x[:, 1], cmap=plt.cm.Paired)
        ax.set_title(dataset_name)
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")

    # Hide any empty subplots
    for i in range(len(datasets_dict), num_rows * num_cols):
        row = i // num_cols
        col = i % num_cols
        fig.delaxes(axes[row, col])

    plt.tight_layout()
    plt.show()


def compare_clustering_algorithms(
    datasets_dict: dict, n_clusters: int = 3
) -> pd.DataFrame:
    """Apply K-Means, K-Medoids, DBSCAN, and Spectral Clustering to each
        dataset and compare results.

    Args:
        datasets_dict: A dictionary of datasets where keys are dataset names
            and values are tuples (X, y) representing the data.
        n_clusters: Number of clusters for K-Means and K-Medoids.

    Returns:
        A DataFrame containing the results of each clustering algorithm on
            each dataset.

    """
    results = []

    for dataset_name, dataset in datasets_dict.items():
        x, y = dataset

        # Apply K-Means
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans_labels = kmeans.fit_predict(x)
        kmeans_score = silhouette_score(x, kmeans_labels)

        # Apply K-Medoids
        kmedoids = KMedoids(n_clusters=n_clusters, random_state=0)
        kmedoids_labels = kmedoids.fit_predict(x)
        kmedoids_score = silhouette_score(x, kmedoids_labels)

        # Apply DBSCAN
        dbscan = DBSCAN()
        dbscan_labels = dbscan.fit_predict(x)
        # Check if DBSCAN found more than one cluster
        if len(np.unique(dbscan_labels)) > 1:
            dbscan_score = silhouette_score(x, dbscan_labels)
        else:
            dbscan_score = None

        # Apply Spectral Clustering
        spectral = SpectralClustering(n_clusters=n_clusters, random_state=0)
        spectral_labels = spectral.fit_predict(x)
        spectral_score = silhouette_score(x, spectral_labels)

        results.append(
            {
                'Dataset': dataset_name,
                'K-Means': kmeans_score,
                'K-Medoids': kmedoids_score,
                'DBSCAN': dbscan_score,
                'Spectral Clustering': spectral_score,
            }
        )

    results_df = pd.DataFrame(results)

    return results_df
