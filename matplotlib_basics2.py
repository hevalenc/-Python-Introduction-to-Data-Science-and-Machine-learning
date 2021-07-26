import matplotlib.pyplot as plt
from matplotlib import style

style.use('bmh')

numbers = [1,3,5,6,9,12,15,16,18,20,2,24,29,33,4,35,39,42,44,46,11,48,55,59,60,61,68,72,77,88,89,91,93,99,100]
jumps = [0,15,30,45,60,75,90,105]

plt.hist(numbers, jumps, histtype='bar')

plt.show()

plt.hist(numbers, jumps, histtype='step')

plt.title('Test Histogram')
plt.xlabel('test x labe')
plt.ylabel('test y labe')

plt.show()
