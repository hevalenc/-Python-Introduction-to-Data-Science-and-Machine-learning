import pandas as pd

food1 = {'number':[1, 2, 3, 4, 5], 'name':['apple', 'banana', 'chips', 'popcorn', 'pizza'], 'price':[2, 3, 4, 8, 6]}
food2 = {'number':[1, 2, 3, 4, 5], 'name':['apple', 'banana', 'chips', 'popcorn', 'pizza'], 'price':[2, 3, 4, 8, 6]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = pd.merge(table1, table2) #unir os items iguais de duas tabelas em uma só

print(fusion)
print()

food3 = {'number':[1, 2, 3, 4, 5], 'name':['apple', 'banana', 'chips', 'popcorn', 'pizza'], 'price':[2, 3, 4, 8, 6]}
#diferenças em number, name e price
food4 = {'number':[1, 2, 3, 4, 6], 'name':['bacon', 'banana', 'chips', 'popcorn', 'pizza'], 'price':[2, 3, 4, 1, 6]}

table3 = pd.DataFrame(food3)
table4 = pd.DataFrame(food4)

fusion1 = pd.merge(table3, table4)
fusion2 = pd.merge(table3, table4, on='name') #união baseado nos item iguais de uma coluna, mostrando as diferenças das demais
fusion3 = pd.merge(table3, table4, on='number')

print(fusion1)
print()
print(fusion2)
print()
print(fusion3)
