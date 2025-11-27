import numpy as np

ages = np.array([[22,42,5,76,12,18,91],
                [31,15,55,57,73,28,82]])

teenager = ages[(ages >14) & (ages <=18)]
print(teenager)
print(f'Children - {ages[ages<10]}')
print(f'Seniors - {ages[ages>60]}')
print(f'Evens - {ages[ages%2 == 0]}')
print(f'Odds - {ages[ages%2 != 0]}')
adults = np.where(ages >= 18, ages, -1) # Wheare clause will preserve the array original
# dimention also its little slow, if need to faster then need to use boolean filter
# in ComparisionOps.py
print(adults)