import numpy as np
import pandas as pd

from numpy.random import shuffle

def format_matrix(df_model):
    # This function takes a dataframe with features and output previously
    # selected and returns an matrix with a ones column added at the beginning.
    m, n = (df_model.shape[0], df_model.shape[1])

    X = df_model.iloc[:, 0:n-1]

    print(type(X))
    ones = np.ones(m, 1)

    print("Type of X: {}\nType of ones: {}".format(X, ones))

    X = np.concatenate((ones, X), axis=1)

    y = df_model.iloc[:, n].values
    y = y.reshape((m, ))

    return (X, y)


def train_test_split(X, y, test_size_perc):
    # This function takes a matrix of features X, a vector of outputs y
    # and the referred percentage for the test set size.

    A = np.concatenate((X, y), axis=1)

    m = A.shape[0]
    n = A.shape[1]

    index_split = int(test_size_perc * m)
    shuffle(A)

    X_test = A[:index_split, :n-1]
    y_test = A[:index_split, n-1]

    X_train = A[index_split:, :n-1]
    y_train = A[index_split:, n-1]

    return (X_train, y_train, X_test, y_test)
