import numpy as np

var1 = np.array([2, 4, 6])

print(var1)
print(var1.dtype)
print('numero de dimensões: ', var1.ndim)
print()

var1 = np.array([(2, 4, 6), (1, 3, 5)])

print(var1)
print(var1.dtype)
print('numero de dimensões: ', var1.ndim)
print('qtde de elementos: ', var1.size)
print('quantas colunas e linhas: ', var1.shape)
print()

var1 = var1.reshape(3, 2) #3 colunas e 2 linhas

print(var1)
print('quantas colunas e linhas: ', var1.shape)
