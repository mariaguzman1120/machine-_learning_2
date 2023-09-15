# Own libraries
from python.utils.datasets import (compare_clustering_algorithms,
                                   generate_datasets, plot_datasets)


def executor():
    datasets = generate_datasets()

    plot_datasets(datasets)

    results = compare_clustering_algorithms(datasets)

    print(results)