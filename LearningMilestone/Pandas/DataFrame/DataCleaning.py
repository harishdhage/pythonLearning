import pandas as pd

df = pd.read_csv('csvData.csv')

#Drop irrerelavant columns
#df = df.drop(columns=['Legendary','No'])

#Handle Missing data
#df = df.dropna(subset='Type2') # It will clears the NaN rows
#df = df.fillna({'Type2':'None'})

#Fix inconsistant values
#df['Type1'] = df['Type1'].replace({'Fire':'FIRE', 'Water':'WATER'})

#Standerdize text
df['Name'] = df['Name'].str.lower()

#Fix data type
df['Legendary'] = df['Legendary'].astype(bool)

#Remove duplicate rows
copyRow = df.iloc[0:50:2]
print(copyRow)
df = pd.concat([df,copyRow])
totalRow = df.shape
df = df.drop_duplicates()
print(df.to_string())
print(f'Total rows \nbefore removing duplicate - {totalRow} '
      f'\nafter removing duplicate - {df.shape}')

#print(df.to_string())

