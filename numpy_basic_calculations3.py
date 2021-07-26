import numpy as np

var1 = np.array([(2, 4, 6), (1, 3, 5)])
var2 = np.array([(5, 9, 3), (6, 7, 15)])

print('var 1:\n', var1)
print('var 2:\n', var2)
print('soma:\n', var1 + var2)
print('subtração:\n', var1 - var2)
print('divisão:\n', var1 / var2)
print('multiplicação:\n', var1 * var2)
print()
print('var1:\n', var1)
print('imprimir a array com uma dimensão: ', var1.ravel())
print('soma dos elementos de cada coluna: ', var1.sum(axis=1))
print('soma dos elementos de cada linha: ', var1.sum(axis=0))
print('raiz quadrado de cada elemento do array:\n', np.sqrt(var1))

'''o desvio padrão indica o quanto um conjunto de dados é uniforme.
Quanto mais próximo de 0 for o desvio padrão, mais homogêneo são os dados.'''
print('\ndesvio padrão do array: ', np.std(var1))
