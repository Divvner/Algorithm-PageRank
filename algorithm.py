import numpy as np

# указываем матрицу
matrix = np.array([
    [0, 0, 1, 1/2],
    [1/3, 0, 0, 0],
    [1/3, 1/2, 0, 1/2],
    [1/3, 1/2, 0, 0]
])

# функция, вычсиляющая значение собственного вектора(с точностью до пропорциональности)
# с собственным значением 1 через сингулярное разложение
def find_eigenvectors_for_eigenvalue_1(init_matrix):

    n = init_matrix.shape[0]
    I = np.eye(n)
    matrix_to_solve = init_matrix - I

    u, s, vh = np.linalg.svd(matrix_to_solve) # сингулярное разложение
    x = vh[-1] # необходимый вектор, к-рый стоит в конце списка

    return x

eigenvector = find_eigenvectors_for_eigenvalue_1(matrix)

# результат будет хрониться в этом списке
result_list = []

# вывод вероятностей на экран
sum = 0
for i in range(len(eigenvector)):
    sum += eigenvector[i]

for i in range(len(eigenvector)):
    result_list.append(eigenvector[i]/sum)

# вывод вероятностей
for i in range(len(eigenvector)):
    print(f"p{i + 1} = {result_list[i]}")
