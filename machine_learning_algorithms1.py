import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

candidates = {'finance':[1,2,3,4,5,6,7,8,9,10,2,3,5,6,9,8,7,11,10,2,3,5],
              'management':[1,2,3,5,4,6,7,8,9,2,4,10,12,15,6,7,8,3,11,12,11,10],
              'logistic':[1,5,2,3,4,6,7,8,9,10,11,2,3,5,6,9,9,8,7,10,11,12],
              'get_work':[1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0]}

data = pd.DataFrame(candidates,columns=['finance','management','logistic','get_work'])

x = data[['finance','management','logistic']]
y = data['get_work']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_prediction = lr.predict(x_test)

conf_matrix = pd.crosstab(y_test, y_prediction, rownames=['True'], colnames=['prevision'])
sb.heatmap(conf_matrix, annot=True)

print('Accurace: ', metrics.accuracy_score(y_test, y_prediction))

plt.show()
