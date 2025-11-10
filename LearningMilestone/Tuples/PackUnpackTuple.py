#Pack tuple
packTuple = 1, 'Beet', 9.23, False
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
start, *mid, end = packTuple
print(start)
print(mid)
print(end)

*h, i = packTuple
print(type(h), h)
print(i)
#print(j)
