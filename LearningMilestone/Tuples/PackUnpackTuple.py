#Pack tuple
pack1 = (1, 'Apple', 3.45, True) # Using parenthesis, explicitly creates tuple
packTuple = 1, 'Beet', 9.23, False # No need to use parenthesis but can be used, implicitly creates tuple
print(packTuple)

#Unpack Tuple
a, b, c, d = packTuple
print(a)
print(b)
print(c)
print(d)

'''x, y, z = packTuple #Not allowed here variriable is not enough to num item in tuple
print(x)
print(y)
print(z)'''

#Unpack using *
start, *mid, end = packTuple # *mid will take all middle elements as list
print('start:', start)
print('mid:', mid)
print('end:', end)

*h, i = packTuple
print(type(h), h)
print(i)
#print(j)

j, k, *_ = packTuple   # _ is used to ignore the remaining values
print(j)
print(k)
