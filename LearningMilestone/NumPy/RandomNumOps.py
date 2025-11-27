import numpy as np

#Integers

rpn = np.random.default_rng(seed=1) #seed will retain the result, used for debugging
print(rpn.random())
print(rpn.integers(1,100)) #2nd argument 100 which means from 1 to 99
print(rpn.integers(low=1,high=101)) #low and high declarion is not needed,
# its just for readability
rpn = np.random.default_rng()
print(rpn.integers(1,100,2)) # 3rd argument is size of array
print(rpn.integers(1,100,(3,2))) # 3rd argument is size amd dimention of array

