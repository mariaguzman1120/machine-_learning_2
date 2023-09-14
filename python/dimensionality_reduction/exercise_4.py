import matplotlib.pyplot as plt

from unsupervised.dimensionality_reduction import SVD
from python.utils.image_processing import transform_image
from python.metadata.path import Path

# Apply SVD over the picture of your face, progressively increasing 
# the number of singular values used.

def executor():
    picture = transform_image(Path.picture)

    fig, axes = plt.subplots(2, 5, figsize=(12, 6))

    for j, k in enumerate(range(2, 22, 2)):
        svd = SVD(n_components=k)
        matrix = svd.inverse_transform(picture)

        row = j // 5
        col = j % 5

        axes[row, col].imshow(matrix, cmap='gray')
        axes[row, col].axis('off')
        axes[row, col].set_title(f'n_components: {k}')

    plt.tight_layout()
    plt.show()
