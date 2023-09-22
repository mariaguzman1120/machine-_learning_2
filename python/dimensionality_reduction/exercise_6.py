from unsupervised.dimensionality_reduction import PCA, SVD, TSNE

from python.utils.mnist_lr import mnist_model_classification


def executor():

    svd = SVD(n_components=2)
    print('Own SVD')
    mnist_model_classification(dimensionality_reduction=svd, plot=True)

    pca = PCA(n_components=2)
    print('Own PCA')
    mnist_model_classification(dimensionality_reduction=pca, plot=True)

    tsne = TSNE(n_components=2)
    print('Own t-SNE')
    mnist_model_classification(dimensionality_reduction=tsne, plot=True)

