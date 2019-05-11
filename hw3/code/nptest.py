import numpy as np

from numpy.random import rand
from nn import MCPerceptron



X = rand(10,)

print(X)

y = 1


n1 = MCPerceptron(X, y)

print(n1.X)
