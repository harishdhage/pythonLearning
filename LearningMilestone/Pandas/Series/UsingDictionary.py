import pandas as pd

fruits = {'Apple':2.42,
          'Mango':0.42,
          'Banana':1.32,
          'Pineapple':1.02,
          'Gava':3.1,
          'Watermelon':1.1}

fruitProtien = pd.Series(fruits, name='Protien')
print(fruitProtien)
fruitProtien['Banana'] += 1
print(fruitProtien)

#Conditional Selection
print(fruitProtien>2)
print(fruitProtien[fruitProtien>2])

#Logical ops
print(fruitProtien[(fruitProtien > 1) & (fruitProtien <=3)]) #AND
print(fruitProtien[(fruitProtien > 1) | (fruitProtien <=3)]) # OR
print(fruitProtien[~(fruitProtien > 1)]) # NOT