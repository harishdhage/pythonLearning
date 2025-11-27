import numpy as np

rng = np.random.default_rng()
a1 = np.array([1,2,3,4,5])
rng.shuffle(a1)
print(a1)

fruits = np.array(['aaple','mango','cherry','banana','pineapple','jackfruit'])
fruit = rng.choice(fruits)
print(fruit)
fruit = rng.choice(fruits,3)
print(fruit)
fruit = rng.choice(fruits,(3,2))
print(fruit)
fruits = np.array([':apple',':mango','cherry','banana','pineapple','jackfruit'])