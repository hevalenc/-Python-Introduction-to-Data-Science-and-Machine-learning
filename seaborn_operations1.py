import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset('tips')
print(database)

sb.jointplot(x='tip', y='total_bill', data=database)

plt.show()
