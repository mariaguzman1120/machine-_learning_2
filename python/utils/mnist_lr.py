import numpy as np

from keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def mnist_model_classification(normalization=False, dimensionality_reduction=None):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    if normalization:
        x_train = x_train.astype(float) / 255
        x_test = x_test.astype(float) / 255
        
    filter_train = np.where((y_train == 0) | (y_train == 8))
    filter_test = np.where((y_test == 0) | (y_test == 8))
    
    x_train = x_train[filter_train]
    x_test = x_test[filter_test]
    
    y_train = y_train[filter_train]
    y_test = y_test[filter_test]
    
    x_train = x_train.reshape(-1, 28*28)
    x_test = x_test.reshape(-1, 28*28)

    if dimensionality_reduction:
        x_train = dimensionality_reduction.fit_transform(x_train)
        x_test = dimensionality_reduction.fit_transform(x_test)
    
    logistic_regression = LogisticRegression(random_state=2)
    
    logistic_regression.fit(x_train, y_train)
    
    y_predict = logistic_regression.predict(x_test)
    
    accuracy = metrics.accuracy_score(y_test, y_predict)
    
    print(f'Accuracy Logistic Regression: {accuracy}')