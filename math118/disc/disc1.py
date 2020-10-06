import numpy as np


def sum_of_squares(x, y):
    return np.sum((x - y) ** 2)


def r_squared(y, y_pred):
    return 1 - sum_of_squares(y, y_pred) / sum_of_squares(y, np.mean(y))


A = np.random.rand(20, 5)
x = np.random.rand(5, 1)
noise = 0.01 * np.random.randn(20, 1)
b = A @ x + noise

# print(f"Dimensions: A: {A.shape}, x: {x.shape}, b: {b.shape}, noise: {noise.shape}")

x_hat = np.linalg.lstsq(A, b, rcond=None)[0]

print(f"SS(x_hat): {sum_of_squares(A @ x_hat, b)}")
print(f"SS(x): {sum_of_squares(A @ x, b)}")
print(f"R^2: {r_squared(b,A @ x_hat)}")
