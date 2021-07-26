import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,5,6,7,8,9,21,4,32,3,5,6,2])
y = np.array([10,12,16,14,17,18,19,31,6,11,30,15,4,27])
func1 = np.polyfit(x,y,1)

plt.plot(x, y, '.')
plt.plot(x, np.polyval(func1, x), 'r-')

plt.show()
