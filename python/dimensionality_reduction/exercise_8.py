import matplotlib.pyplot as plt
from keras.datasets import mnist

from python.utils.robustpca import RobustPCA


def executor():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(-1, 28*28)

    rpca = RobustPCA()
    l, s, example = rpca.pcp(x_train.T)

    image_list = x_train[:10]
    image_list = image_list.reshape(-1, 28, 28)
    
    fig,axes = plt.subplots(2, 10, figsize=(10,5))
    
    for i in range(10):
        axes[0, i].imshow(image_list[i])
        axes[0, i].axis('off')
        axes[0, i].set_title('Original')

    image = l.T.reshape(-1, 28, 28)

    for i in range(10):
        axes[1, i].imshow(image[i])
        axes[1, i].axis('off')
        axes[1, i].set_title('Filtrado')

    plt.show()