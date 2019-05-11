import numpy as np

class MCPerceptron:
    def __init__(self, X, y, leaning_rate=0.3):
        self.n_features = X.shape[0]
        self.X = X
        self.y = y
        self.W = np.zeros(self.n_features + 1)
        self.leaning_rate = leaning_rate

    def thresold(self, x):
        return 1 if (x > 0) else 0

    def output(self):
        return self.thresold(self.W @ self.X)

    def update_weights(self):
        self.W = self.W + (self.leaning_rate * (self.output() - self.y) * self.X)

    def __str__(self):
        return "Input: {}\nOutput: {}\nWeights: {}\nLearning Rate: {}".format(self.X, self.y,
                                                                              self.W, self.leaning_rate)




class MLP(Object):
    """
        This is a class which represents a neural network architecture. It takes an array of features X, an
        output y,
    """

        def __init__(self, sizes)
