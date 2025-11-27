import pandas as pd

df = pd.read_csv('csvData.csv')

#print(df.mean()) # It will throw error, because it table contains String columns
print(df.mean(numeric_only=True))
print('Height : ',df['Height'].sum())

#Grouping the data
group = df.groupby('Type1')
print(group)
print(group['Height'].mean())
