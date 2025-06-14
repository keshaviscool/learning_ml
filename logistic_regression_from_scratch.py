import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def calculate_gradient(thetha, X, y): # @ operator is matrix multiplication wow!!!!
    m = y.size # number of instances
    return ((X.T @ sigmoid(X @ thetha)) / m)


def gradient_descent(X, y, alpha=0.1, num_iter=100, tol=1e-7):
    # add bias
    X_b = np.c_[np.ones((X.shape[0], 1)), X]

    thetha = np.zeros(X_b.shape[1]) # initialisation

    for epoch in range(num_iter):
        grad = calculate_gradient(thetha, X, y)
        thetha -= alpha * grad

        if np.linalg.norm(grad) < tol:
            break

    return thetha

def predict_proba(X, thetha):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    return sigmoid(X_b @ thetha)


def predict(X, thetha, threshold=0.5):
    return (predict_proba(X, thetha) >= threshold).astype(int)


from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


