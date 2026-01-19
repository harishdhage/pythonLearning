def even(x):
    if x%2==0:
        return True
#filter function filters the items of the iterable based on the function provided
#filter(function, iterable)
num = [1,4,2,6,1,9,5,21,87,44,22,6,31]
print(list(filter(even,num)))
print(list(filter(lambda x:x%2==0,num)))
print(list(filter(lambda x:x%2==0 and x>5,num)))
