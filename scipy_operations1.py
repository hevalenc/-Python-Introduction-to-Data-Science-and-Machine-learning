import scipy as sp
from scipy import integrate

var1 = lambda x: x**3
function1 = integrate.quad(var1, 0, 6)

print(function1)

var2 = lambda y, x: x * y ** 4
function2 = integrate.dblquad(var2, 0, 6, lambda x:0, lambda x:1)

print(function2)