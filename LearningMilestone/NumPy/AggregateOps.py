import numpy as np

a1 = np.array([[1,2,3,4],
               [5,6,7,8]])
print(np.sum(a1))
print(np.var(a1))
print(np.std(a1))
print(np.mean(a1))
print(np.max(a1))
print(np.sum(a1,axis=0)) #row1 + row2
print(np.sum(a1,axis=1)) # sum (ele in row 1) , sum (ele in row2)