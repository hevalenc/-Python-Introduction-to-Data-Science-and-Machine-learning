import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

x = [3, 6, 7, 9, 10]
y = [5, 10, 15, 3, 1]

plt.scatter(x, y)

plt.title('Test Scatter Plot')
plt.xlabel('test x')
plt.ylabel('test y')

plt.show()
