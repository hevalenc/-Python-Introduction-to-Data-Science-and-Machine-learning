import pandas as pd

food1 = {'number':[1, 2, 3, 4, 5], 'name':['apple', 'banana', 'chips', 'popcorn', 'pizza'], 'price':[2, 3, 4, 8, 6]}
food2 = {'color':['red', 'yellow', 'orange', 'white', 'blue'], 'weight':[100, 200, 150, 175, 225], 'qt':[1, 2, 1, 3, 4]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = table1.join(table2) #unindo duas tabelas, sendo a segunda adiciona colunas na primeira tabela

print(fusion)
