import pandas as pd

fruits = {'Apple':2.42,
          'Mango':0.42,
          'Banana':1.32,
          'Pineapple':1.02,
          'Gava':3.1,
          'Watermelon':1.1}

fruitProtien = pd.Series(fruits, name='Protien')
fruitProtien['Gava']=1.09
print(fruitProtien)