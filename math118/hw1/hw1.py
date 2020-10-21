from sklearn.datasets import load_iris
import numpy as np
import numpy.linalg as la
import numpy.random as npr
import matplotlib.pyplot as plt


def q9b():
    A = np.matrix([[0.7922, 0.6787, 0.7060, 0.6948],
                   [0.9595, 0.7577, 0.0318, 0.3171],
                   [0.6557, 0.7431, 0.2769, 0.9502],
                   [0.0357, 0.3922, 0.0462, 0.0344],
                   [0.8491, 0.6555, 0.0971, 0.4384],
                   [0.9340, 0.1712, 0.8235, 0.3816]])
    b = np.array([[0.7655, 0.7952, 0.1869, 0.4898, 0.4456, 0.6463]]).T
    x_star = np.linalg.lstsq(A, b, rcond=None)[0]
    print(x_star)

if __name__ == "__main__":
    q9b()
