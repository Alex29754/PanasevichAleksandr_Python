
import numpy as np

# Заданная матрица
matrix = np.array([
    [3, 4, 17, -3],
    [5, 11, -1, 6],
    [0, 2, -5, 8]
])

# Чтение матрицы из файла
read_matrix = np.loadtxt('matrix.txt', dtype=int)

# Сумма всех элементов матрицы
sum_of_elements = np.sum(read_matrix)

# Максимальный элемент матрицы
max_element = np.max(read_matrix)

# Минимальный элемент матрицы
min_element = np.min(read_matrix)

print("Сумма всех элементов матрицы:", sum_of_elements)
print("Максимальный элемент матрицы:", max_element)
print("Минимальный элемент матрицы:", min_element)
