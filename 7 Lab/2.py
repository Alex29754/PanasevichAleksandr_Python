import numpy as np


def run_length_encoding(x):
    # Индексы, где значения меняются
    change_indices = np.where(np.roll(x, 1) != x)[0]

    # Уникальные значения
    values = x[change_indices]

    # Количество повторений
    counts = np.diff(np.concatenate((change_indices, [len(x)])))

    return values, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = run_length_encoding(x)
print("Ответ:", (values, counts))
