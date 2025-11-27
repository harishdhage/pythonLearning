import pandas as pd

a1 = pd.Series([10,23,31,12,87,13])
print(a1)
a1 = pd.Series([10,23,31,12,87,13,'and'])
print(a1)
print(a1.values)
print(a1.index)
print(a1.name) # Its empty due column name is not defined
a1.name = 'Age'
print(a1.name)
print(a1)