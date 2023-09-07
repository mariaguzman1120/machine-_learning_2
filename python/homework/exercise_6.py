from unsupervised.dimensionality_reduction import SVD
from unsupervised.dimensionality_reduction import PCA
from unsupervised.dimensionality_reduction import TSNE
from python.utils.mnist_lr import mnist_model_classification

if __name__ == '__main__':

    svd = SVD(n_components=2)
    print('Own SVD')
    mnist_model_classification(dimensionality_reduction=svd)

    pca = PCA(n_components=2)
    print('Own PCA')
    mnist_model_classification(dimensionality_reduction=pca)

    tsne = TSNE(n_components=2)
    print('Own t-SNE')
    mnist_model_classification(dimensionality_reduction=tsne)


