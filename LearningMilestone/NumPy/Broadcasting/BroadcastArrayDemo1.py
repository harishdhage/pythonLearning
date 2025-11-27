import numpy as py

a1 = py.array([[1,2,3,4]])
b1 = py.array([[1],[2],[3],[4]])
print(a1.shape)
print(b1.shape)
print(a1+b1)
b2 = py.array([[1,3],[2,5],[3,7],[4,8]])
print(b2.shape)
print(a1+b2) # will get value error