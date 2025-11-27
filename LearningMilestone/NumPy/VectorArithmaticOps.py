import numpy as np

#Vectorize math func

arr = np.array([1.03,2.43,3.13,4.97])

print(np.sqrt(arr))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))
print(np.pi)
print('Radius for each ele - ',np.pi * arr ** 2)