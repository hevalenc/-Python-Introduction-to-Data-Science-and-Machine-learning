import pandas as pd

employee = {'number':[1, 2, 3, 4, 5], 'name':['abby', 'john', 'lina', 'marc', 'bob'], 'hourly salary':[15, 25, 32, 27, 40]}
print('Dicionário: ', employee)

table1 = pd.DataFrame(employee)
print('\nConvertido o dicionário em tabela:\n', table1)

print('\nAs duas primeiras linhas da tabela:\n', table1.head(2))
print('\nAs duas últimas linhas da tabela:\n', table1.tail(2))
