empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))
tup = tuple() #Here tuple() is class object
print(type(tup))
num = (1,2,3,3,4,5)
print(num)
mix_tuple = ('string word', 12, False, 92.14)
print(mix_tuple)
listToTuple1 = tuple([1,'demo',90.345])
print('listToTuple1 type - ',type(listToTuple1))
lst = [23, 65, 1, .53, True]
listToTuple2 = tuple(lst)
print('listToTuple2 type - ',type(listToTuple2))

tupleWithList = (2,3,5,1,2,[2,6,1,7,1])
print(tupleWithList[5][3])
print(tupleWithList)
