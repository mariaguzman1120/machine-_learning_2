# External libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score


def plot_silhouette_comparison(
    x: np.array, kmeans_labels: np.array, kmedoids_labels: np.array
) -> None:
    """Plot a comparison of silhouette plots for K-Means and K-Medoids.

    Args:
        x: Feature matrix (n_samples, n_features).
        kmeans_labels: Cluster labels for K-Means.
        kmedoids_labels: Cluster labels for K-Medoids.

    Returns:
        None (displays the silhouette comparison plot).

    """
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    plot_silhouette(x, axs[0], kmeans_labels, "K-Means Silhouette Plot")

    plot_silhouette(x, axs[1], kmedoids_labels, "K-Medoids Silhouette Plot")

    plt.show()


def plot_silhouette(
    x: np.ndarray, ax: plt.Axes, labels: np.ndarray, title: str
):
    """
    Plot a silhouette plot for clusters.

    Args:
        x (np.ndarray): Feature matrix (n_samples, n_features).
        ax (plt.Axes): Matplotlib Axes object to plot the silhouette.
        labels (np.ndarray): Cluster labels for each data point.
        title (str): Title for the silhouette plot.

    Returns:
        None (displays the silhouette plot).
    """
    ax.set_xlim([-0.1, 1])
    ax.set_ylim([0, len(x) + (len(np.unique(labels)) + 1) * 10])
    ax.set_title(title)

    y_lower = 10

    for j in range(len(np.unique(labels))):
        ith_cluster_silhouette_values = silhouette_samples(x, labels)
        ith_cluster_silhouette_values.sort()

        size_cluster_j = ith_cluster_silhouette_values[labels == j].shape[0]
        y_upper = y_lower + size_cluster_j

        color = plt.cm.nipy_spectral(float(j) / len(np.unique(labels)))
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values[labels == j],
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        ax.text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))

        y_lower = y_upper + 10

    silhouette_avg = silhouette_score(x, labels)
    ax.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax.set_yticks([])
    ax.text(
        0.5,
        1.1,
        f"Silhouette Score: {silhouette_avg:.2f}",
        transform=ax.transAxes,
        ha="center",
    )