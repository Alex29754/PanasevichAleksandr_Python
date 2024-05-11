import numpy as np


def max_after_zero(x):
    zeros_indices = np.where(x == 0)[0]  # находим индексы нулевых элементов
    max_value = None

    for index in zeros_indices:
        if index + 1 < len(x):  # убеждаемся, что есть элемент после нуля
            if max_value is None or x[index + 1] > max_value:
                max_value = x[index + 1]  # обновляем максимальное значение

    return max_value


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
result = max_after_zero(x)
print("Максимальный элемент после нуля:", result)
