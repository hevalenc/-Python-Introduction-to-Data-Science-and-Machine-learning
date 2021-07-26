import numpy as np

var1 = np.linspace(10, 50) #gerar números aleatórios entre 10 e 50
var2 = np.linspace(10, 50, 4) #gerar 4 números aleatórios entre 10 e 50

print(var1)
print(var2)
print()

var3 = np.array([(2, 4, 6), (1, 3, 5)])

print(var3)
print(var3[0, 1])
print(var3[0:, 1]) #imprimir de todos os índice, os elementos na posição 1
print()

var4 = np.array([(2, 4, 6), (1, 3, 5), (7, 24, 21), (10, 30, 50)])

print(var4[0:, 1])
print()

var5 = np.array([(2, 4, 6), (1, 3, 5)])

print(var5)
print('maior número: ', var5.max())
print('menor número: ', var5.min())
print('soma de todos os números: ', var5.sum())
