import numpy as np

multiD_Array = np.array([['a','b','c'],
                         ['d','e','f'],
                         ['g','h','i']])
print("Array dimention - ", multiD_Array.ndim)
print("Array shape - ", multiD_Array.shape)
multiD_Array1 = np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
                          [['j','k','l'],['m','n','o'],['p','q','s']],
                          [['t','r','w'],['x','y','z'],['qq','we','qa']]])
print("Array dimention multiD_Array1 - ", multiD_Array1.ndim)
print("Array shape multiD_Array1 - ", multiD_Array1.shape)
print(multiD_Array1[0][2][1])
print(multiD_Array1[1,1,2])
print(multiD_Array1[::2])
#Below array multiD_Array2 will throw value error
multiD_Array2 = np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
                          [['j','k','l'],['m','n','o'],['p','q','s']],
                          [['t','r','w'],['x','y','z'],['qq','we']]])