from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from python.utils.mnist_lr import mnist_model_classification

def executor():

    svd = TruncatedSVD(n_components=2)
    print('Sklearn SVD')
    mnist_model_classification(dimensionality_reduction=svd)

    pca = PCA(n_components=2)
    print('Sklearn PCA')
    mnist_model_classification(dimensionality_reduction=pca)

    tsne = TSNE(n_components=2)
    print('Sklearn t-SNE')
    mnist_model_classification(dimensionality_reduction=tsne)

    




