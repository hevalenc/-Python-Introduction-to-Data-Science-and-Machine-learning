import matplotlib.pyplot as plt
from matplotlib import style

style.use('classic')

food = ['pizza', 'ice cream', 'burger']
sales = [20, 10, 30]
color = ['red', 'blue', 'yellow']

plt.pie(sales, labels=food, colors=color)

plt.title('Pie Graph Example')

plt.show()
