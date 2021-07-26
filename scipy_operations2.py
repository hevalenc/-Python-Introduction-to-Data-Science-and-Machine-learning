import scipy as sp
import numpy as np
from scipy import fft
from scipy import linalg

#var1 = np.array([(2, 4, 6), (1, 3, 5)])
#print(var1)
#print()

#trans1 = sp.fft(var1)
#print(trans1)
#print()

array1 = np.array([(1, 3), (2, 4)])
array2 = np.array([(5, 9), (6, 8)])

print(array1, '\n', array2)
print()
print(sp.linalg.solve(array1, array2))
print()

function1 = sp.linalg.inv(array1)
print(function1)