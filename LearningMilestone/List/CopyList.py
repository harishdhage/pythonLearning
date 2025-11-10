#Shallow Copy
import copy

list1 =[[1,3,3,9],['a',4,9,True, 9.43]]
copyList = copy.copy(list1) #Shallow copy doesn't copy element, it just point to original reference.
copyList[0][2]=23 #If any modification made on shallowed copy list, it also change in original list
print(list1)
print('copyList',copyList)
copyList1 = list1
list1[1][-2]=False
print('copyList1',copyList1)

deepCopy = copy.deepcopy(list1) #Deep copy copy the element from onle list to other list
deepCopy[0][2] = 31 #Any list manupulation made on copied/origin list, doesn't affect the other
print('Original list - ',list1)
print('Deep copy list - ',deepCopy)

copiedList = list1[1:2]
copiedList.append(76)
print('Original list - ',list1)
print('Copied list - ',copiedList)