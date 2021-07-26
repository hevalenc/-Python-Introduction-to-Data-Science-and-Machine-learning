import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset('diamonds')
print(database)

sb.distplot(database['carat'], bins=1)
plt.show()
