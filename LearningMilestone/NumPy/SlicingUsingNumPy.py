import numpy as np

array_num = np.array([[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12],
                      [13,14,15,16]])

# array[staring index:ending index:step]
print(f'First row - {array_num[0]}')
print(f'3rd row - {array_num[2]}')
print(f'2nd row with -ve index - {array_num[-3]}')
#Ending index is exclusive as index starts from 1 not 0
print(f'2nd to 4th row  - {array_num[1:4]}')
print(f'Alternative row starting from 1st row  - {array_num[0:4:2]}')
print(f'Alternative row without start and end  - {array_num[::2]}')
print(f'Returns reverse order  - {array_num[::-1]}')
print(f'Returns reverse order with alternative  - {array_num[::-2]}')
#Accessing columns, we need to use comma to specify the row and column index
print(f'Printing 2nd column from each row - {array_num[:,2]}')
print(f'Printing last column from each row using -ve index - {array_num[:,-1]}')
print(f'Printing subset from each row - {array_num[:,2:4]}')
print(f'Printing subset from each row using step index - {array_num[:,::2]}')
print(f'Printing subset from each row using step index start from col 1 - '
      f'{array_num[:,1::2]}')
print(f'Reverse index - {array_num[:,::-1]}')
print(f'Reverse index alternative col- {array_num[:,::-2]}')
print(f'Get subset to make quadrant- {array_num[0:2,0:2]}')
print(f'Get subset to make quadrant- {array_num[0:2,1:3]}')
print(f'Get subset - {array_num[::-1,1:4:2]}')
