import pandas as pd

df = pd.read_csv('csvData.csv')

print(df) # It will print first 5 and last 5 rows
print(df.to_string()) # It will print whole file data

df_json = pd.read_json('pokemonData.json')
print(df_json)

#Selecting column
print(df_json['Name'])

#Selecting row
print(df.loc[3])
#print(df_json.loc['Pikachu']) # It will throw keyError, because index Name is not defined
df_csv = pd.read_csv('csvData.csv', index_col='Name')
print(df_csv.loc['Pikachu'])
print(df_csv.loc['Pikachu',['Height','Weight']])
print(df_csv.loc['Pikachu':'Blastoise',['Height','Weight']])
print(df_csv.iloc[0:11:2,0:3])