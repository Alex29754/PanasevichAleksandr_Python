import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Столбец species находится в последнем столбце
species_column = iris[:, -1]

# Находим уникальные значения и их количество
unique_species, counts = np.unique(species_column, return_counts=True)

print("Уникальные значения в столбце species:", unique_species)
print("Количество каждого уникального значения:", counts)
