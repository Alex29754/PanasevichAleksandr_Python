import numpy as np

# Генерация массива случайных чисел нормального распределения размером 10x4
data = np.random.normal(size=(10, 4))

# Нахождение минимального значения
min_value = np.min(data)

# Нахождение максимального значения
max_value = np.max(data)

# Нахождение среднего значения
mean_value = np.mean(data)

# Нахождение стандартного отклонения
std_deviation = np.std(data)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = data[:5]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)
print("Первые 5 строк:")
print(first_five_rows)
