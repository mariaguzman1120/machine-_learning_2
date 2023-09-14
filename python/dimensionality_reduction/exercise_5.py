from python.utils.mnist_lr import mnist_model_classification

def executor():
    # Model without processing
    mnist_model_classification()

    # Model with processing
    mnist_model_classification(True)