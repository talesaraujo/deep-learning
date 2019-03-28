import numpy as np
import pandas as pd

from numpy.random import randint
from datahandler import *

def test_format_matrix():
    df = pd.DataFrame(np.random.randint(0, 10, size=(30, 4)), columns=list('ABCD'))

    print("DATAFRAME")
    print(df.head(10))

    X, y = format_matrix(df)


def main():
    test_format_matrix()


if __name__ == '__main__':
    main()
