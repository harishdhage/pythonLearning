import pandas as pd

a1 = pd.Series([10,23,31,12,87,13])
#[start (included) : stop(excluded) : step value (values to jump)]
print(a1[2:4])
print(a1[::2])
print(a1[::-1])

#iloc -> location based indexing
print(a1.iloc[4])
print(a1.iloc[[1,3,4]])

#Adding row names/value
names = ['Harish','Goonda','Pooja', 'Bonda','Diskow','Pachak']
a1.index = names
print(a1)
print(a1['Goonda'])
#print(a1.iloc['Goonda']) #Not allowed, as this is from list. Not part of original
# Panda array. It is a label
print(a1.iloc[4])
#Access using label
print(a1.loc['Diskow'])
print(a1.loc[['Goonda','Diskow']])
print(a1.loc['Goonda':'Diskow'])
