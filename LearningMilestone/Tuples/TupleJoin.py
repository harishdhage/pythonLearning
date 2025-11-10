tuple1 = ('Apple', "Mango", 'Banana', 'Car')
tuple2 = (23, 12.21, 242, 21)

joinTupleByPlus = tuple1+tuple2
print("Tuple joined using + : ",joinTupleByPlus)

#Using list comprehension
joinByListComprehension = [item for subTuple in [tuple1, tuple2] for item in subTuple]
print('Tuples joined using List Comprehension - ',joinByListComprehension)

# Using sum
tupleSum = sum((tuple1, tuple2),())
print('Tuple joined using sum - ',tupleSum)

#using for loop
for t in tuple2:
    tuple1+=(t,)
print("tuple joined by for loop - ",tuple1)