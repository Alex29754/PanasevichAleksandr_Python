import numpy as np

def log_density_multivariate_normal(X, m, C):
    D = len(m)
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    constant = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    centered_X = X - m
    exponent = -0.5 * np.sum(centered_X @ inv_C * centered_X, axis=1)
    return constant + exponent

# Тестирование функции
X = np.array([[1, 2], [2, 3], [3, 4]])
m = np.array([0, 0])
C = np.array([[1, 0], [0, 1]])
result = log_density_multivariate_normal(X, m, C)
print("Результат:", result)
